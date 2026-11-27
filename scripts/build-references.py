#!/usr/bin/env python3
"""Gera a biblioteca versionada de referências reais em referencias/.

FONTES (dados de terceiros; lidos como dado, nunca executados). Caminhos relativos a SCRATCH
(--scratch, ou a variável REFS_SCRATCH; padrão abaixo):
  ig/vid_hd/<ID>.mp4              vídeos em resolução máxima (PREFERIDOS quando existem e abrem)
  ig/vid/<ID>.mp4                 vídeos dos reels (yt-dlp; fallback)
  ig/meta/, meta10/, ig/meta3/    metadados do yt-dlp (1ª linha JSON: autor, legenda, datas)
  ig/tr/<ID>.txt, sources/<ID>.md transcrição e resumo por reel
  achados/prints-jpg/rodada-3B, achados/prints-jpg/solto      (4A e 4B EXCLUÍDAS: investimento)
  achados2/prints-jpg/rodada-1, rodada-2                       (exclui DfowdSMiPzc_*: quant)
  jpg-new/rodada-5, rodada-6, rodada-7                         (exclui 4 carrosséis quant)
  nova/jpg9                                                    (9A–9F, ref_, tool_; exclui miniaturas < 600 px)
  r10/jpg                                                      (10A e 10C)
E na repo:
  docs/achados/rodada-*.md, docs/sources.md, .claude/skills/*/references/visual-index.md
  .claude/skills/*/assets/visual-refs/*.jpg (só para casar ID → skill/segmento e data do git)
Datas de envio (WhatsApp), em UPLOADS (--uploads ou REFS_UPLOADS):
  4bf5eb8d-chat.md, d7ab0dd1-chat.md, e288bbd7-chat.txt
  Sem timestamp para o ID: usa a data do git em que a imagem/ID entrou na repo.

SAÍDA:
  referencias/reels/<ID>/frame-1..4.jpg (largura nativa até 1080 px, sem upscale, q85)
                         + loop.webp (até 540 px, 12 fps, ~4 s, ≤ 700 KB)
  referencias/prints/<arquivo>.jpg (resolução original; JPG copiado byte a byte, PNG → JPG q85;
                         dedupe por nome e hash)
  referencias/index.json

Idempotente: pula reels/prints já gerados; refaz um reel quando o vídeo de origem muda (ex.: chegou
o vid_hd/<ID>.mp4). --force refaz tudo; --reels-only refaz só os reels (os prints vêm do cache) e
reescreve o index.json. Requer ffmpeg/ffprobe (com libwebp) e Pillow.
Uso:  python3 -I scripts/build-references.py [--force | --reels-only] [--only ID,...]
"""
import datetime
import hashlib
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys

from PIL import Image, ImageFilter, ImageStat

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "referencias")
SCRATCH = os.environ.get(
    "REFS_SCRATCH",
    "/tmp/claude-0/-home-user-blank-app/981406e5-c4ec-5917-b9a7-38c020783fdd/scratchpad")
UPLOADS = os.environ.get("REFS_UPLOADS", "/root/.claude/uploads/981406e5-c4ec-5917-b9a7-38c020783fdd")
for i, a in enumerate(sys.argv):
    if a == "--scratch" and i + 1 < len(sys.argv):
        SCRATCH = sys.argv[i + 1]
    if a == "--uploads" and i + 1 < len(sys.argv):
        UPLOADS = sys.argv[i + 1]

VID_DIR = "ig/vid"
VID_HD_DIR = "ig/vid_hd"
FRAME_MAX_W = 1080
FRAME_Q = 85
LOOP_W = 540
LOOP_LIMIT = 700 * 1024
META_DIRS = ["ig/meta", "meta10", "ig/meta10", "ig/meta3"]
TR_DIR = "ig/tr"
SRC_DIR = "sources"
PRINT_DIRS = [
    "achados/prints-jpg/rodada-3B",
    "achados/prints-jpg/solto",
    "achados2/prints-jpg/rodada-1",
    "achados2/prints-jpg/rodada-2",
    "jpg-new/rodada-5",
    "jpg-new/rodada-6",
    "jpg-new/rodada-7",
    "nova/jpg9",
    "r10/jpg",
]
CHATS = ["4bf5eb8d-chat.md", "e288bbd7-chat.txt", "d7ab0dd1-chat.md"]
# Último recurso para a data de envio: quando o zip da rodada chegou (mtime do upload).
FOLDER_UPLOAD = {"nova/jpg9": "7d77a0e8-Nova_rodada.zip", "r10/jpg": "dd00b13e-prints-10A.zip",
                 "jpg-new/rodada-7": "e1577a6a-prints-rodada-7.zip", "jpg-new/rodada-5": "2444c8ed-imagens-rodadas-5-e-6.zip",
                 "jpg-new/rodada-6": "2444c8ed-imagens-rodadas-5-e-6.zip"}

# Investimento/quant e fora do tema: nunca entram.
EXCLUDE_IDS = {
    "DfowdSMiPzc", "De7NqmHkbzU", "DfFnuSOkqi9", "Dfr5It0xAzA", "DfztwFuxh4f",   # carrosséis quant
    "DfVf0L-AIkP", "DfoRErMChB-", "DftZ6l2CC_e", "DfuDLH7BUsx",                  # reels quant
    "Dfm0NTiIfyd",   # "Traders skill" (trading automático)
    "De9oszIIQ4V",   # repositório de acesso a plataformas para agentes (fora de design)
}
# Revisão de privacidade (feita olhando cada print): arquivos excluídos por mostrar dado pessoal
# de pessoa real (e-mail, telefone, rosto identificável fora de contexto público).
PRIVACY_EXCLUDE = set()
# Recortes: arquivo -> (esq, topo, dir, base) em fração da imagem original.
PRIVACY_CROP = {
    "10A_1A19QTSisE_1.jpg": (0.43, 0.0, 1.0, 1.0),     # página do FB: tira a coluna "Contact info" (telefone/e-mail)
    "9F_youtube-figma_1.jpg": (0.205, 0.0, 1.0, 1.0),  # tira a barra lateral com as inscrições da conta logada
    "9F_youtube-nngroup_1.jpg": (0.205, 0.0, 1.0, 1.0),
}

SEGMENT_RX = [
    ("FIN", r"fintech|\bbank|banco|pagament|payment|wallet|carteira|crédito|credit|\binvest|trading|\bcripto|crypto|"
            r"financ|budget|money|saldo|fatura|invoice|billing|insurance|seguro|\bpix\b|checkout|ticker"),
    ("CRM", r"\bcrm\b|pipeline|\bleads?\b|\bdeals?\b|sales|vendas|kanban de neg|contatos?\b"),
    ("PUB", r"campaign|campanha|\bads?\b|anúncio|marketing|agência|record label|social media|criativo"),
    ("MPE", r"creator|criador|portf[oó]lio|link (in|na) bio|personal brand|marca pessoal|freelanc|palestrante"),
    ("SAU", r"health|saúde|clínic|clinic|medic|médic|hospital|paciente|patient|fitness|wellness|telemedic|exame"),
    ("JUR", r"\blegal\b|jurídic|advoga|\blaw\b|contrato|contract|processual|oab\b"),
]
TAG_RX = [
    ("motion", r"motion|anima|transi[cç]|spring|easing|micro-?intera|scroll"),
    ("micro-interação", r"micro-?intera|toggle|press|tap|hover|haptic|feedback"),
    ("glassmorphism", r"glass|vidro"),
    ("dashboard", r"dashboard|painel|analytics|kpi"),
    ("paleta", r"paleta|palette|colou?rs?\b|\bcores?\b|acento|accent"),
    ("tipografia", r"tipogra|typograph|fontes?\b|\bfonts?\b|serif"),
    ("gráfico", r"gráfico|chart|graph|heatmap|barras"),
    ("kanban", r"kanban"),
    ("login", r"login|senha|password|sign ?in"),
    ("sidebar", r"sidebar|barra lateral"),
    ("tab bar", r"tab ?bar|navega[cç]ão inferior"),
    ("bottom sheet", r"sheet|detent"),
    ("loader", r"loader|loading|skeleton|carregando"),
    ("toast", r"toast|snackbar"),
    ("drag-and-drop", r"drag|arrastar"),
    ("⌘K", r"⌘k|command palette|paleta de comandos|cmd\+k"),
    ("botão", r"\bbot[aã]o|button|\bcta\b"),
    ("formulário", r"formul|\bform\b|campo|input"),
    ("onboarding", r"onboarding"),
    ("landing", r"landing|\bhero\b|website|\bsite\b"),
    ("gamificação", r"gamifi|progresso|progress|\bmeta(s)?\b|ranking|streak"),
    ("leis de UX", r"\blaws?\b|\bleis? de|hick|fitts|jakob|miller"),
    ("dark mode", r"dark|escuro"),
    ("IA", r"\bai\b|\bia\b|claude|prompt|agent"),
    ("branding", r"brand|marca|logo|identidade"),
    ("mobile", r"\bios\b|android|iphone|mobile|celular|\bapp\b"),
    ("3D", r"\b3d\b"),
]


def load_catalog_helpers():
    spec = importlib.util.spec_from_file_location("bcat", os.path.join(ROOT, "scripts", "build-catalog.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


BC = load_catalog_helpers()
clean = BC.clean
infer_platforms = BC.infer_platforms
infer_screens = BC.infer_screens
ID_RX = r"[A-Za-z0-9_\-]{10,11}"


def sp(*p):
    return os.path.join(SCRATCH, *p)


def read(p):
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()


def sha1(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


# ------------------------------------------------------------------ datas
MESES = {m: i for i, m in enumerate(["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto",
                                     "setembro", "outubro", "novembro", "dezembro"], 1)}
LINK_RX = re.compile(r"(?:instagram\.com/(?:reel|p)/(" + ID_RX + r")|facebook\.com/share/(?:[rv]/)?(" + ID_RX + r"))")


def chat_dates():
    """{id: (iso_local -03:00, url_enviada)} — primeira vez que o ID aparece nos chats."""
    out = {}
    for name in CHATS:
        p = os.path.join(UPLOADS, name)
        if not os.path.exists(p):
            continue
        day = None
        for line in read(p).splitlines():
            m = re.match(r"## (\d{1,2}) de (\w+) de (\d{4})", line)
            if m:
                day = datetime.date(int(m.group(3)), MESES.get(m.group(2).lower(), 1), int(m.group(1)))
                continue
            ts = None
            m = re.match(r"\[(\d{1,2}):(\d{2})\] \*\*You:\*\*", line)
            if m and day:
                ts = datetime.datetime(day.year, day.month, day.day, int(m.group(1)), int(m.group(2)))
            m = re.match(r"\[(\d{1,2})/(\d{1,2})/(\d{2}), (\d{1,2}):(\d{2}):(\d{2}) ([AP]M)\] You:", line)
            if m:
                h = int(m.group(4)) % 12 + (12 if m.group(7) == "PM" else 0)
                ts = datetime.datetime(2000 + int(m.group(3)), int(m.group(1)), int(m.group(2)), h,
                                       int(m.group(5)), int(m.group(6)))
            if not ts or line.lstrip().startswith(">"):
                continue
            for lm in LINK_RX.finditer(line):
                i = lm.group(1) or lm.group(2)
                url = re.search(r"https?://\S+", line[lm.start() - 40 if lm.start() > 40 else 0:])
                iso = ts.strftime("%Y-%m-%dT%H:%M:00-03:00")
                if i not in out or iso < out[i][0]:
                    kind = "reel" if "/reel/" in line or "/share/r/" in line or "/share/v/" in line else "post"
                    out[i] = (iso, kind)
    return out


def git_add_dates():
    """{basename e caminho relativo: data ISO do commit que adicionou o arquivo pela 1ª vez}."""
    out = {}
    try:
        txt = subprocess.run(["git", "-C", ROOT, "log", "--diff-filter=A", "--name-only", "--format=@@%aI", "--",
                              ".claude/skills", "docs"], capture_output=True, text=True, timeout=120).stdout
    except Exception:
        return out
    cur = None
    for line in txt.splitlines():
        if line.startswith("@@"):
            cur = line[2:]
        elif line.strip() and cur:
            for k in (line.strip(), os.path.basename(line.strip())):
                if k not in out or cur < out[k]:
                    out[k] = cur
    return out


def first_text_date(needle, files_dates):
    """Data do git do 1º documento (rodada/visual-index) que cita o texto."""
    best = None
    for path, d in files_dates:
        try:
            if needle in read(os.path.join(ROOT, path)):
                if best is None or d < best:
                    best = d
        except OSError:
            pass
    return best


def utc(iso):
    if not iso:
        return None
    try:
        return datetime.datetime.fromisoformat(iso).astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return iso


# ------------------------------------------------------------------ metadados textuais
def md_docs():
    docs = []
    for d in (os.path.join(ROOT, "docs", "achados"),):
        for f in sorted(os.listdir(d)):
            if f.endswith(".md") and not re.match(r"rodada-4[AB]", f):
                docs.append(os.path.join(d, f))
    for skill in sorted(os.listdir(BC.SKILLS)):
        if skill.startswith("ext-") or skill in BC.EXCLUDE:
            continue
        vi = os.path.join(BC.SKILLS, skill, "references", "visual-index.md")
        if os.path.exists(vi):
            docs.append(vi)
    return docs


def table_index(docs):
    """{stem: [(doc, header_dict)]} das linhas de tabela cujo 1º campo cita um arquivo de imagem."""
    out = {}
    for doc in docs:
        for header, body in BC.tables(read(doc)):
            for cells in body:
                if not cells:
                    continue
                for f in re.findall(r"([A-Za-z0-9_.\-]+)\.(?:jpg|png)", cells[0]):
                    d = {h: cells[i] for i, h in enumerate(header) if i < len(cells)}
                    out.setdefault(f, []).append((doc, d))
    return out


def section_index(docs):
    """{ID: {author, title, body, doc}} para cabeçalhos '### <ID> — @autor'."""
    out = {}
    for doc in docs:
        text = read(doc)
        ms = list(re.finditer(r"^#{3,4} (" + ID_RX + r")\b[^\n]*", text, re.M))
        for i, m in enumerate(ms):
            end = len(text)
            nxt = re.search(r"^#{2,4} ", text[m.end():], re.M)
            if nxt:
                end = m.end() + nxt.start()
            pid = m.group(1)
            title = m.group(0)
            am = re.search(r"@([A-Za-z0-9_.]+)", title)
            if pid in out:
                continue
            out[pid] = {"author": ("@" + am.group(1)) if am else "", "title": title, "body": text[m.end():end],
                        "doc": doc}
            if not am:
                cm = re.search(r"—\s*([^\n(]+)", title)
                if cm:
                    out[pid]["author"] = cm.group(1).strip()
    return out


def bullet(body, *labels):
    for lab in labels:
        m = re.search(r"^\s*-\s*(?:\*\*)?" + lab + r"(?:\*\*)?\s*:\s*(?:\*\*)?(.+?)(?=\n\s*-\s*(?:\*\*)?[A-ZÁÉÍÓÚ][^:\n]{1,30}:|\n\n|\Z)",
                      body, re.M | re.S | re.I)
        if m:
            return clean(m.group(1))
    return ""


def row_get(d, *names):
    for n in names:
        for k, v in d.items():
            if k.startswith(n) and v and v.strip() not in ("—", "-", "idem"):
                return v
    return ""


def first_url(text):
    m = re.search(r"https?://[^\s|)`>\]]+", text or "")
    return m.group(0).rstrip(".,;") if m else ""


def yt_meta(pid):
    for d in META_DIRS:
        p = sp(d, pid + ".json")
        if os.path.exists(p) and os.path.getsize(p) > 0:
            try:
                with open(p, encoding="utf-8") as f:
                    return json.loads(f.readline())
            except (ValueError, OSError):
                continue
    return {}


def short_caption(desc, limit=160):
    if not desc:
        return ""
    t = re.sub(r"#\w+", "", desc)
    t = re.sub(r"\s+", " ", t).strip(" .")
    return clean(t, limit)


def unquote(t):
    t = (t or "").strip()
    if len(t) > 1 and t[0] in "\"“'" and t.count(t[0]) % 2 == 1 or (t[:1] in "\"“" and t[-1:] in "\"”"):
        t = t[1:]
        if t[-1:] in "\"”":
            t = t[:-1]
    return t.strip()


def infer_segments(text):
    t = text.lower()
    return [c for c, rx in SEGMENT_RX if re.search(rx, t)]


def infer_tags(text):
    t = text.lower()
    return [n for n, rx in TAG_RX if re.search(rx, t)]


# ------------------------------------------------------------------ vídeo
def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=width,height:format=duration", "-of", "json", path],
                         capture_output=True, text=True).stdout
    j = json.loads(out or "{}")
    st = (j.get("streams") or [{}])[0]
    return float(j.get("format", {}).get("duration") or 0), st.get("width"), st.get("height")


def scene_times(path):
    r = subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-i", path, "-an", "-vf",
                        "scale=320:-2,select='gt(scene,0.3)',showinfo", "-f", "null", "-"],
                       capture_output=True, text=True)
    return [float(x) for x in re.findall(r"pts_time:([0-9.]+)", r.stderr)]


def samples(path, fps=2, w=160):
    """Frames em cinza a cada 1/fps s: [(t, PIL.Image)]."""
    r = subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-i", path, "-an", "-vf",
                        "fps=%d,scale=%d:-2,format=gray" % (fps, w), "-f", "image2pipe", "-c:v", "pgm", "-"],
                       capture_output=True)
    data = r.stdout
    out, pos, idx = [], 0, 0
    while pos < len(data):
        m = re.match(rb"P5\s+(\d+)\s+(\d+)\s+(\d+)\s", data[pos:pos + 40])
        if not m:
            break
        wd, ht = int(m.group(1)), int(m.group(2))
        start = pos + m.end()
        im = Image.frombytes("L", (wd, ht), data[start:start + wd * ht])
        out.append(((idx + 0.5) / fps, im))
        pos = start + wd * ht
        idx += 1
    return out


def quality(im):
    st = ImageStat.Stat(im)
    mean, std = st.mean[0], st.stddev[0]
    sharp = ImageStat.Stat(im.filter(ImageFilter.FIND_EDGES)).mean[0]
    return mean, std, sharp


def choose_frames(dur, scenes, smp, n):
    q = [(t, *quality(im)) for t, im in smp]
    if not q:
        return [dur * f for f in (0.15, 0.4, 0.65, 0.88)][:n]
    sharp_sorted = sorted(x[3] for x in q)
    med = sharp_sorted[len(sharp_sorted) // 2]

    def ok(x):
        # preto/chapado = std baixo (UIs escuras têm média ~15, então não filtramos só pela média)
        return 5 <= x[1] <= 250 and x[2] >= 9 and x[3] >= 0.6 * med

    def nearest(t):
        return min(q, key=lambda x: abs(x[0] - t))
    gap = max(1.5, dur / (n + 2))
    chosen = []
    # 1) mudanças de cena: frame ~0.6 s depois do corte (evita o borrão da transição)
    cands = []
    for s in scenes:
        x = nearest(min(dur - 0.3, s + 0.6))
        if ok(x) and 0.4 < x[0] < dur - 0.6:
            cands.append(x)
    cands.sort(key=lambda x: -x[3])
    for x in cands:
        if len(chosen) >= n:
            break
        if all(abs(x[0] - c[0]) >= gap for c in chosen):
            chosen.append(x)
    # 2) fallback: instantes distribuídos, o mais nítido de uma janela
    for frac in (0.12, 0.38, 0.62, 0.86, 0.25, 0.5, 0.75):
        if len(chosen) >= n:
            break
        win = [x for x in q if abs(x[0] - dur * frac) <= dur * 0.08 and ok(x)]
        if not win:
            continue
        x = max(win, key=lambda x: x[3])
        if all(abs(x[0] - c[0]) >= gap * 0.7 for c in chosen):
            chosen.append(x)
    if len(chosen) < n:
        for x in sorted(q, key=lambda x: -x[3]):
            if len(chosen) >= n:
                break
            if ok(x) and all(abs(x[0] - c[0]) >= gap * 0.5 for c in chosen):
                chosen.append(x)
    for x in sorted(q, key=lambda x: -x[3]):
        if len(chosen) >= n:
            break
        if all(abs(x[0] - c[0]) >= 1.0 for c in chosen):
            chosen.append(x)
    return sorted(c[0] for c in chosen)


def loop_window(dur, smp, length=4.0):
    if dur <= length + 1:
        return 0.0, min(dur, length)
    # diferença absoluta média entre amostras vizinhas = atividade
    from PIL import ImageChops
    diffs = [0.0] + [ImageStat.Stat(ImageChops.difference(a, b)).mean[0] for (_, a), (_, b) in zip(smp, smp[1:])]
    qual = [quality(im) for _, im in smp]
    best, best_s = None, -1
    step = 0.5
    t = 1.0
    while t + length <= dur - 1.5:
        idx = [i for i, (ts, _) in enumerate(smp) if t <= ts <= t + length]
        if idx and all(5 <= qual[i][0] <= 250 and qual[i][1] >= 8 for i in idx):
            act = sum(min(diffs[i], 40) for i in idx) / len(idx)
            sharp = sum(qual[i][2] for i in idx) / len(idx)
            score = act * 0.6 + sharp * 0.4 - abs((t + length / 2) / dur - 0.4) * 6
            if score > best_s:
                best, best_s = t, score
        t += step
    if best is None:
        best = max(0.0, dur * 0.35 - length / 2)
    return best, length


def video_source(pid):
    """vid_hd/<ID>.mp4 se existir e tiver vídeo decodificável; senão vid/<ID>.mp4."""
    hd = sp(VID_HD_DIR, pid + ".mp4")
    if os.path.exists(hd) and os.path.getsize(hd) > 50000:
        try:
            dur, w, h = probe(hd)
            if dur > 1 and w:
                return hd
        except Exception:
            pass
    return sp(VID_DIR, pid + ".mp4")


def extract_frame(path, t, out, width=900, q=FRAME_Q):
    r = subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-ss", "%.3f" % t, "-i", path, "-frames:v", "1",
                        "-vf", "scale=%d:-2:flags=lanczos" % width, "-f", "image2pipe", "-c:v", "png", "-"],
                       capture_output=True)
    im = Image.open(io.BytesIO(r.stdout)).convert("RGB")
    im.save(out, "JPEG", quality=q, optimize=True, progressive=True)
    return im.size


def make_loop(path, start, length, out, width, limit=LOOP_LIMIT):
    tries = [(4.0, 12, 72), (4.0, 12, 58), (4.0, 12, 45), (3.5, 12, 40), (3.5, 10, 36), (3.0, 10, 30)]
    w = width
    for ln, fps, q in tries:
        ln = min(ln, length)
        subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-ss", "%.3f" % start, "-t", "%.2f" % ln,
                        "-i", path, "-an", "-vf", "fps=%d,scale=%d:-2:flags=lanczos" % (fps, w), "-c:v", "libwebp_anim",
                        "-q:v", str(q), "-compression_level", "5", "-loop", "0", out], check=False)
        if os.path.exists(out) and os.path.getsize(out) <= limit:
            return ln, w, fps
    return ln, w, fps


def build_reel(pid, force=False):
    path = video_source(pid)
    od = os.path.join(OUT, "reels", pid)
    info_p = os.path.join(od, ".build.json")
    if not force and os.path.exists(info_p) and os.path.getmtime(info_p) >= os.path.getmtime(path):
        with open(info_p, encoding="utf-8") as f:
            info = json.load(f)
        if info.get("origem") == os.path.relpath(path, SCRATCH) and info.get("v") == 2:
            return info
    os.makedirs(od, exist_ok=True)
    for f in os.listdir(od):
        os.remove(os.path.join(od, f))
    dur, w, h = probe(path)
    scenes = scene_times(path)
    smp = samples(path)
    n = 4 if dur >= 12 else 3
    times = choose_frames(dur, scenes, smp, n)
    frames = []
    for i, t in enumerate(times, 1):
        fn = "frame-%d.jpg" % i
        fw, fh = extract_frame(path, t, os.path.join(od, fn), width=min(FRAME_MAX_W, w or FRAME_MAX_W))
        frames.append({"arquivo": "reels/%s/%s" % (pid, fn), "t": round(t, 2), "w": fw, "h": fh})
    start, length = loop_window(dur, smp)
    ln, lw, lfps = make_loop(path, start, length, os.path.join(od, "loop.webp"), min(LOOP_W, w or LOOP_W))
    lh = round(lw * (h or 16) / (w or 9) / 2) * 2
    info = {"v": 2, "origem": os.path.relpath(path, SCRATCH), "duracao": round(dur, 1), "w": w, "h": h,
            "cenas": len(scenes), "frames": frames,
            "loop": {"arquivo": "reels/%s/loop.webp" % pid, "inicio": round(start, 2), "duracao": ln, "w": lw,
                     "h": lh, "fps": lfps, "bytes": os.path.getsize(os.path.join(od, "loop.webp"))}}
    with open(info_p, "w", encoding="utf-8") as f:
        json.dump(info, f)
    return info


# ------------------------------------------------------------------ prints
def collect_prints():
    """[(src_path, basename)] já filtrados e deduplicados (por nome: maior; por hash: 1º)."""
    by_name = {}
    for d in PRINT_DIRS:
        full = sp(d)
        if not os.path.isdir(full):
            continue
        for f in sorted(os.listdir(full)):
            if not f.lower().endswith(".jpg"):
                continue
            p = os.path.join(full, f)
            pid = print_post_id(f)
            if pid and pid in EXCLUDE_IDS:
                continue
            if f in PRIVACY_EXCLUDE:
                continue
            with Image.open(p) as im:
                w, h = im.size
            if d.startswith("nova/jpg9") and w < 600 and h < 600:
                continue   # miniatura ilegível
            if f not in by_name or w > by_name[f][1]:
                by_name[f] = (p, w)
    out, seen = [], {}
    for f in sorted(by_name):
        p = by_name[f][0]
        h = sha1(p)
        if h in seen:
            continue
        seen[h] = f
        out.append((p, f))
    return out


def print_post_id(fname):
    stem = fname.rsplit(".", 1)[0]
    m = re.match(r"^(?:10A_)?(" + ID_RX + r")_\d+$", stem)
    if m:
        return m.group(1)
    m = re.match(r"^9E_.+?_(" + ID_RX + r")_\d+$", stem)
    if m:
        return m.group(1)
    return None


def build_print(src, fname, force=False):
    out = os.path.join(OUT, "prints", fname)
    if force or fname in PRIVACY_CROP or not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(src):
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with Image.open(src) as im0:
            fmt = im0.format
        if fname not in PRIVACY_CROP and fmt == "JPEG":
            shutil.copyfile(src, out)          # resolução e bytes originais
        else:
            im = Image.open(src).convert("RGB")
            if fname in PRIVACY_CROP:
                l, t, r, b = PRIVACY_CROP[fname]
                W, H = im.size
                im = im.crop((int(l * W), int(t * H), int(r * W), int(b * H)))
            im.save(out, "JPEG", quality=85, optimize=True, progressive=True)
    with Image.open(out) as im:
        return {"arquivo": "prints/" + fname, "w": im.width, "h": im.height}


# ------------------------------------------------------------------ main
def main():
    force = "--force" in sys.argv
    reels_force = force or "--reels-only" in sys.argv
    only = None
    if "--only" in sys.argv:
        only = set(sys.argv[sys.argv.index("--only") + 1].split(","))
    os.makedirs(OUT, exist_ok=True)
    sent = chat_dates()
    gdates = git_add_dates()
    docs = md_docs()
    doc_dates = [(os.path.relpath(d, ROOT), gdates.get(os.path.relpath(d, ROOT)) or "9999") for d in docs]
    tix = table_index(docs)
    six = section_index(docs)
    skill_rows = BC.index_rows()            # {basename.jpg: [(skill, row)]}
    # que skills/segmentos citam cada ID ou arquivo
    seg_cite = {}
    skill_cite = {}
    for skill in sorted(os.listdir(BC.SKILLS)):
        if skill.startswith("ext-") or skill in BC.EXCLUDE:
            continue
        refdir = os.path.join(BC.SKILLS, skill, "references")
        if not os.path.isdir(refdir):
            continue
        txt = " ".join(read(os.path.join(refdir, f)) for f in os.listdir(refdir) if f.endswith(".md"))
        for m in re.finditer(r"(" + ID_RX + r")(?:_\d+)?\.jpg|(\b[0-9A-Za-z_\-]+_\d)\.jpg", txt):
            key = m.group(1) or m.group(2)
            skill_cite.setdefault(key, set()).add(skill)
            if skill in BC.SEG_BY_SKILL:
                seg_cite.setdefault(key, set()).add(BC.SEG_BY_SKILL[skill])
    skill_imgs = {}
    for skill in sorted(os.listdir(BC.SKILLS)):
        vr = os.path.join(BC.SKILLS, skill, "assets", "visual-refs")
        if os.path.isdir(vr) and not skill.startswith("ext-") and skill not in BC.EXCLUDE:
            for f in os.listdir(vr):
                skill_imgs.setdefault(f.rsplit(".", 1)[0], []).append(skill)

    def send_date(pid, names):
        if pid and pid in sent:
            return sent[pid][0], "whatsapp"
        cands = []
        for n in names:
            for k in (n + ".jpg", n):
                if k in gdates:
                    cands.append(gdates[k])
        if pid:
            for k, v in gdates.items():
                if k.startswith(pid) and k.endswith(".jpg"):
                    cands.append(v)
        if cands:
            return min(cands), "git"
        d = first_text_date(pid or names[0], doc_dates)
        if d and d != "9999":
            return d, "git-doc"
        return None, None

    records = []
    # ---------------- reels
    vids = sorted(f[:-4] for f in os.listdir(sp(VID_DIR)) if f.endswith(".mp4"))
    for pid in vids:
        if pid in EXCLUDE_IDS or (only and pid not in only):
            continue
        info = build_reel(pid, reels_force)
        meta = yt_meta(pid)
        rows = skill_rows.get(pid + ".jpg", [])
        what = ""
        for _, d in rows:
            what = what or row_get(d, "o que mostra", "o que observar", "o que serve")
        srcmd = sp(SRC_DIR, pid + ".md")
        transcript = ""
        if os.path.exists(srcmd):
            mt = re.search(r"## Transcrição do áudio\s*\n(?:\[[a-z]{2}\]\s*)?(.+)", read(srcmd), re.S)
            if mt:
                transcript = clean(mt.group(1), 600)
        desc = meta.get("description") or ""
        channel = meta.get("channel") or meta.get("uploader_id") or ""
        author = "@" + channel if channel and not channel.isdigit() else (meta.get("uploader") or "")
        up = meta.get("upload_date")
        origin = "%s-%s-%s" % (up[:4], up[4:6], up[6:8]) if up else None
        if meta.get("timestamp"):
            origin = datetime.datetime.fromtimestamp(meta["timestamp"], datetime.timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ")
        ds, dsrc = send_date(pid, [pid])
        text = " ".join([desc, what, transcript[:300]])
        segs = sorted(seg_cite.get(pid, set()))
        for s in infer_segments(" ".join([desc, what])):
            if s not in segs:
                segs.append(s)
        skills = sorted(skill_cite.get(pid, set()) | set(skill_imgs.get(pid, [])))
        records.append({
            "id_post": pid, "tipo": "reel", "autor": author, "autor_nome": meta.get("uploader") or "",
            "legenda": short_caption(desc), "legenda_completa": clean(desc, 1200),
            "url": "https://www.instagram.com/reel/%s/" % pid,
            "data_envio": ds, "data_envio_fonte": dsrc, "data_origem": origin,
            "segmentos": segs or ["GER"], "plataformas": infer_platforms(text, ["mobile"]),
            "o_que_mostra": clean(what, 600) or transcript[:400], "transcricao": transcript,
            "tags": sorted(set(infer_tags(text) + infer_screens(text))),
            "skills": skills, "duracao": info["duracao"],
            "arquivos": {"frames": info["frames"], "loop": info["loop"], "imagem": info["frames"][0]["arquivo"]},
            "fonte": os.path.dirname(info.get("origem", VID_DIR)), "origem_video": info.get("origem", ""),
            "video_w": info.get("w"), "video_h": info.get("h"),
        })
    # ---------------- prints
    prints = collect_prints()
    groups = {}
    order = []
    for src, fname in prints:
        stem = fname.rsplit(".", 1)[0]
        pid = print_post_id(fname)
        key = pid or stem
        if key not in groups:
            groups[key] = {"pid": pid, "files": []}
            order.append(key)
        groups[key]["files"].append((src, fname, stem))
    reel_ids = {r["id_post"]: r for r in records}
    for key in order:
        g = groups[key]
        pid = g["pid"]
        if only and key not in only:
            continue
        files = sorted(g["files"], key=lambda x: x[1])
        imgs = [build_print(src, fname, force) for src, fname, _ in files]
        stems = [s for _, _, s in files]
        if pid and pid in reel_ids:
            # print de um reel que já temos em vídeo: vira imagem extra do reel
            reel_ids[pid]["arquivos"].setdefault("prints", []).extend(imgs)
            continue
        # metadados: seção ### ID, linhas de tabela por arquivo, linhas do visual-index das skills, yt-dlp
        sec = six.get(pid, {}) if pid else {}
        body = sec.get("body", "")
        rows = []
        for s in stems:
            rows += [d for _, d in tix.get(s, [])]
            rows += [d for _, d in skill_rows.get(s + ".jpg", [])]
        meta = yt_meta(pid) if pid else {}
        name = bullet(body, "Nome sugerido") or next((clean(row_get(d, "nome")) for d in rows
                                                       if row_get(d, "nome") and not re.search(r"\.(jpg|png)", row_get(d, "nome"))), "")
        what = next((clean(row_get(d, "o que mostra", "o que observar", "o que serve", "descrição", "por que abrir"))
                     for d in rows if row_get(d, "o que mostra", "o que observar", "o que serve", "descrição",
                                                 "por que abrir")), "")
        if not what and body:
            what = bullet(body, "Slide a slide", "Componentes mostrados", "O que mostra", "Resumo", "Tema")
        if not what and len(rows) == 0 and body:
            what = clean(body, 400)
        legend = bullet(body, "Legenda") or short_caption(meta.get("description") or "")
        author = sec.get("author") or ""
        if not author:
            author = next((clean(re.sub(r"https?://\S+", "", row_get(d, "autor", "produto/autor", "produto")))
                           for d in rows if row_get(d, "autor", "produto/autor", "produto")), "")
        if not author and meta.get("channel"):
            author = "@" + meta["channel"]
        m9 = re.match(r"^9E_(.+?)_" + ID_RX + r"_\d+$", stems[0])
        if not author and m9:
            author = "@" + m9.group(1)
        url = next((first_url(row_get(d, "url")) for d in rows if first_url(row_get(d, "url"))), "")
        if not name and not pid:
            # nome legível a partir do arquivo: "9F_youtube-nngroup_1" -> "youtube nngroup"
            name = re.sub(r"^(?:\d+[A-F]|ref|tool)_(?:[A-Z]{3}_)?", "", stems[0])
            name = re.sub(r"_\d+$", "", name).replace("_", " · ").replace("-", " ")
        fb = pid and re.match(r"^1[A-Za-z0-9]{9}$", pid)
        if pid and not fb:
            kind = sent.get(pid, (None, None))[1]
            url = "https://www.instagram.com/%s/%s/" % ("reel" if kind == "reel" or "reel" in body[:300].lower()
                                                        and "carrossel" not in body[:300].lower() else "p", pid)
        elif fb:
            url = url or "https://www.facebook.com/share/%s/" % pid
        if not url:
            url = first_url(body)
        if not author and url:
            author = re.sub(r"^www\.", "", re.sub(r"^https?://([^/]+).*$", r"\1", url))
        seg_txt = " ".join([name, what, legend, " ".join(row_get(d, "segmento") for d in rows), stems[0],
                            bullet(body, "Segmento")])
        segs = []
        m10 = re.match(r"^10C_([A-Z]{3})_", stems[0])
        if m10:
            segs.append(m10.group(1))
        for s in stems + ([pid] if pid else []):
            for c in sorted(seg_cite.get(s, ())):
                if c not in segs:
                    segs.append(c)
        for c in infer_segments(seg_txt):
            if c not in segs:
                segs.append(c)
        plat_txt = " ".join([bullet(body, "Plataforma"), " ".join(row_get(d, "plataforma") for d in rows)])
        plats = infer_platforms(plat_txt) or infer_platforms(" ".join([name, what, legend]))
        galeria = bool(re.match(r"^(ref_|tool_|9C_landing|9C_portfolio|9D_figma|9D_supabase|9D_shadcn-blocks|9F_)",
                                stems[0]))
        tipo = "galeria" if galeria else ("carrossel" if pid and not fb and len(imgs) > 1 else "print")
        if pid and not fb and sent.get(pid, (0, ""))[1] == "post" and len(imgs) == 1:
            tipo = "print"
        ds, dsrc = send_date(pid, stems)
        if not ds:
            z = os.path.join(UPLOADS, FOLDER_UPLOAD.get(os.path.relpath(os.path.dirname(files[0][0]), SCRATCH), "-"))
            if os.path.exists(z):
                ds = datetime.datetime.fromtimestamp(os.path.getmtime(z), datetime.timezone.utc).strftime(
                    "%Y-%m-%dT%H:%M:%SZ")
                dsrc = "upload"
        up = meta.get("upload_date")
        origin = "%s-%s-%s" % (up[:4], up[4:6], up[6:8]) if up else None
        if not origin:
            dp = next((row_get(d, "data de publ") for d in rows if re.search(r"\d{4}", row_get(d, "data de publ"))),
                      "")
            mm = re.search(r"(\d{2})/(\d{2})/(\d{4})", dp)
            origin = "%s-%s-%s" % (mm.group(3), mm.group(2), mm.group(1)) if mm else None
        skills = set()
        for s in stems + ([pid] if pid else []):
            skills |= skill_cite.get(s, set()) | set(skill_imgs.get(s, []))
        text = " ".join([name, what, legend])
        records.append({
            "id_post": pid or stems[0], "tipo": tipo, "autor": author, "autor_nome": meta.get("uploader") or "",
            "nome": unquote(name), "legenda": unquote(clean(legend, 160)), "legenda_completa": unquote(clean(legend, 1200)),
            "url": url, "data_envio": ds, "data_envio_fonte": dsrc, "data_origem": origin,
            "segmentos": segs or ["GER"], "plataformas": plats or ["website"],
            "o_que_mostra": clean(what, 600), "tags": sorted(set(infer_tags(text) + infer_screens(text))),
            "skills": sorted(skills),
            "arquivos": {"imagens": imgs, "imagem": imgs[0]["arquivo"]},
            "fonte": os.path.relpath(os.path.dirname(files[0][0]), SCRATCH),
            "doc": os.path.relpath(sec["doc"], ROOT) if sec.get("doc") else "",
        })
    records.sort(key=lambda r: (r["data_envio"] is None, utc(r["data_envio"]) or "", r["id_post"]))
    idx = {
        "gerado_em": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fontes": {"scratch": "<scratchpad da sessão>", "pastas": [VID_DIR] + META_DIRS + PRINT_DIRS,
                   "chats": CHATS, "docs": "docs/achados/rodada-*.md, .claude/skills/*/references/visual-index.md"},
        "excluidos": sorted(EXCLUDE_IDS),
        "referencias": records,
    }
    with open(os.path.join(OUT, "index.json"), "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=1)
        f.write("\n")
    # limpeza de reels/prints órfãos
    if not only:
        keep_r = {r["id_post"] for r in records if r["tipo"] == "reel"}
        for d in os.listdir(os.path.join(OUT, "reels")):
            if d not in keep_r:
                p = os.path.join(OUT, "reels", d)
                for f in os.listdir(p):
                    os.remove(os.path.join(p, f))
                os.rmdir(p)
        keep_p = {i["arquivo"].split("/", 1)[1] for r in records for i in
                  r["arquivos"].get("imagens", []) + r["arquivos"].get("prints", [])}
        for f in os.listdir(os.path.join(OUT, "prints")):
            if f not in keep_p:
                os.remove(os.path.join(OUT, "prints", f))
    reels = [r for r in records if r["tipo"] == "reel"]
    nf = sum(len(r["arquivos"]["frames"]) for r in reels)
    big = [r["id_post"] for r in reels if r["arquivos"]["loop"]["bytes"] > LOOP_LIMIT]
    npr = sum(len(r["arquivos"].get("imagens", [])) + len(r["arquivos"].get("prints", [])) for r in records)
    hd = sum(1 for r in reels if r.get("origem_video", "").startswith(VID_HD_DIR))
    print("reels: %d (de vid_hd: %d)  frames: %d  loops: %d (acima de 700 KB: %s)" % (len(reels), hd, nf, len(reels), big or "nenhum"))
    print("prints: %d  registros: %d  sem data: %d" % (npr, len(records), sum(1 for r in records if not r["data_envio"])))
    from collections import Counter
    print("tipos:", dict(Counter(r["tipo"] for r in records)))
    print("segmentos:", dict(Counter(s for r in records for s in r["segmentos"])))


if __name__ == "__main__":
    main()
