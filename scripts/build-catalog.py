#!/usr/bin/env python3
"""Gera catalogo/catalogo.json e catalogo/media/<REF>/ a partir das skills de design e da biblioteca
de referências reais.

Fontes:
- referencias/index.json (gerado por scripts/build-references.py): fonte PRINCIPAL das referências
  (reels com frames + loop.webp, carrosséis, prints e galerias enviados pelo usuário);
- .claude/skills/segmento-*/references/{templates,componentes,visual-index}.md, SKILL.md de cada
  segmento e os visual-index.md das skills de tema/plataforma (templates, componentes e as imagens
  das skills que não estão na biblioteca; as que estão viram alias, sem duplicar).
Exclui ext-* e quant-investing (não é de design).

Saída: catalogo/catalogo.json e catalogo/media/<REF>/{thumb.webp (480 px), 1.jpg..N.jpg (grandes),
loop.webp (reels)}. Códigos REF em ordem de data de envio (o mais antigo é REF-0001).

Uso (da raiz da repo):  python3 -I scripts/build-catalog.py [--no-thumbs]
Requer só a stdlib e o ffmpeg (com libwebp) no PATH para as miniaturas.
"""
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, ".claude", "skills")
OUT_DIR = os.path.join(ROOT, "catalogo")
THUMBS = os.path.join(OUT_DIR, "thumbs")   # legado: removido ao gerar media/
MEDIA = os.path.join(OUT_DIR, "media")
LIB = os.path.join(ROOT, "referencias")
EXCLUDE = {"quant-investing"}

SEGMENTS = [
    ("FIN", "Financeiro", "segmento-financeiro"),
    ("CRM", "CRM", "segmento-crm"),
    ("PUB", "Publicidade", "segmento-publicidade"),
    ("MPE", "Marca pessoal", "segmento-marca-pessoal"),
    ("SAU", "Saúde", "segmento-saude"),
    ("JUR", "Jurídico", "segmento-juridico"),
    ("GER", "Geral", None),
]
SEG_BY_SKILL = {s: c for c, _, s in SEGMENTS if s}
PLATFORM_SKILLS = {"mobile-app-ui": "mobile", "desktop-app-ui": "desktop", "website-ui": "website"}

HEX_RE = re.compile(r"(~?)#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})(?![0-9A-Za-z])")
JPG_RE = re.compile(r"([A-Za-z0-9_.\-]+\.jpg)")
BOLD_LABEL_RE = re.compile(r"\*\*([^*\n]{2,60}?):\*\*")


# ---------------------------------------------------------------- helpers
def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def clean(text, limit=None):
    """Markdown leve -> texto: tira **, mantém `código`, junta linhas."""
    t = text.replace("**", "")
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", t)
    t = re.sub(r"[ \t]*\n[ \t]*", " ", t)
    t = re.sub(r"\s{2,}", " ", t).strip(" -|;")
    if limit and len(t) > limit:
        cut = t[:limit].rsplit(" ", 1)[0]
        t = cut.rstrip(",;:") + "…"
    return t


def norm_hex(h):
    h = h.upper()
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return "#" + h


def hexes(text):
    out = []
    for m in HEX_RE.finditer(text):
        h = norm_hex(m.group(2))
        if h not in out:
            out.append(h)
    return out


def split_sections(text, level=2):
    """Devolve [(título, corpo)] para cabeçalhos do nível pedido."""
    pat = re.compile(r"^%s (.+)$" % ("#" * level), re.M)
    ms = list(pat.finditer(text))
    out = []
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        out.append((m.group(1).strip(), text[m.end():end]))
    return out


def table_rows(text):
    """Linhas de tabela markdown (sem cabeçalho/separador) como listas de células."""
    rows = []
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c or "--") for c in cells):
            continue
        rows.append(cells)
    return rows


def tables(text):
    """Blocos de tabela: [(cabeçalho, [linhas])]."""
    out, cur = [], []
    for line in text.splitlines() + [""]:
        if line.strip().startswith("|"):
            cur.append(line)
        elif cur:
            rows = table_rows("\n".join(cur))
            if rows:
                out.append(([c.lower() for c in rows[0]], rows[1:]))
            cur = []
    return out


def kv_fields(body):
    """Campos 'chave → valor' de um bloco: linhas de tabela | k | v | e rótulos **K:** v."""
    fields = {}
    order = []
    for cells in table_rows(body):
        if len(cells) >= 2 and cells[0].lower() not in ("token", "campo"):
            k = clean(cells[0]).lower()
            fields.setdefault(k, cells[1])
            order.append(k)
    ms = list(BOLD_LABEL_RE.finditer(body))
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(body)
        val = body[m.end():end]
        val = re.sub(r"\n\s*-\s*$", "", val.rstrip())
        val = val.rstrip(" -\n")
        k = m.group(1).strip().lower()
        if k not in fields:
            fields[k] = val
            order.append(k)
    return fields, order


def pick(fields, *prefixes):
    for p in prefixes:
        for k, v in fields.items():
            if k.startswith(p):
                return v
    return ""


def git_first_date(path):
    try:
        out = subprocess.run(
            ["git", "-C", ROOT, "log", "--diff-filter=A", "--follow", "--format=%aI", "--", path],
            capture_output=True, text=True, check=False, timeout=60).stdout.strip().splitlines()
        return out[-1] if out else None
    except Exception:
        return None


def git_first_date_string(needle, path):
    try:
        out = subprocess.run(
            ["git", "-C", ROOT, "log", "-S", needle, "--format=%aI", "--", path],
            capture_output=True, text=True, check=False, timeout=60).stdout.strip().splitlines()
        return out[-1] if out else git_first_date(path)
    except Exception:
        return None


def to_utc(iso):
    if not iso:
        return None
    try:
        d = datetime.datetime.fromisoformat(iso)
        return d.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return iso


# ---------------------------------------------------------------- inferência
PLATFORM_KW = [
    ("mobile", r"mobile|celular|\bios\b|android|\bapp\b(?! desktop)|tab bar|smartphone|iphone|link na bio|tablet"),
    ("desktop", r"desktop|painel|dashboard|web app|\bweb\b|saas|admin|tabela|sidebar|back-office|kanban"),
    ("website", r"website|\bsite\b|landing|hero|home\b|página|portfólio|portfolio|vitrine"),
]


def infer_platforms(text, default=None):
    t = text.lower()
    if re.search(r"\btodas\b|\btodos\b", t):
        return ["mobile", "desktop", "website"]
    out = [p for p, rx in PLATFORM_KW if re.search(rx, t)]
    return out or list(default or [])


CATEGORY_KW = [
    ("confiança", r"consentimento|lgpd|selo|confiança|aviso|regulat|ético|auditoria|publicidade/patrocinado|parceria paga|depoimento|prova social|assinatura|termo|cet|rentabilidade|segurança|fraude"),
    ("navegação", r"tab bar|navega|menu|paleta de comandos|alternância|seletor de período|breadcrumb|hierarquia|botão de link|trilho|abas"),
    ("formulário", r"busca|campo|seletor|formul|checkout|captura|reserve|agendamento|orçamento|objetivo|filtro"),
    ("feedback", r"alerta|toast|badge|status|estado|checagem|sala de espera|fila|pontuação|confirmação"),
    ("dados", r"tabela|kpi|saldo|extrato|linha do tempo|histórico|gráfico|receita|anel|barra|resultado|insight|limite|números|custo|preço|pipeline|calendário|prazo"),
    ("layout", r"painel|grade|cartão|card|coluna|vitrine|perfil|estudo de caso|leitor|prévia"),
    ("motion", r"motion|anima|transição|arrastar"),
    ("conteúdo", r"glossário|termo explicado|depoimento|conteúdo|ia\b|assistente|caixa de ia"),
]

CATEGORY_ORDER = ["navegação", "dados", "formulário", "feedback", "motion", "layout", "confiança", "conteúdo"]


def infer_category(name, desc):
    n = name.lower()
    for cat, rx in CATEGORY_KW:
        if re.search(rx, n):
            return cat
    d = desc.lower()
    for cat, rx in CATEGORY_KW:
        if re.search(rx, d):
            return cat
    return "conteúdo"


SCREEN_KW = [
    ("dashboard", r"dashboard|painel|kpi|analytics|métrica|relatório"),
    ("landing", r"landing|hero|\bsite\b|website|vitrine|página de preços"),
    ("lista/tabela", r"tabela|lista|extrato|kanban|pipeline|fila|feed"),
    ("formulário", r"formul|checkout|campo|cadastro|captura|busca|agendamento|login|senha"),
    ("detalhe", r"detalhe|perfil|prontuário|case|estudo de caso|contato\b"),
    ("onboarding", r"onboarding|boas-vindas|permiss|primeiro uso"),
    ("motion", r"motion|anima|transição|micro-intera|loader|scroll|reel|slow-mo|spring"),
    ("marca/cor", r"paleta|tipograf|fontes?\b|logo|branding|\bcores?\b"),
]


def infer_screens(text):
    t = text.lower()
    return [s for s, rx in SCREEN_KW if re.search(rx, t)]


# ---------------------------------------------------------------- segmentos
def segment_rules(skill_dir):
    text = read(os.path.join(skill_dir, "SKILL.md"))
    secs = split_sections(text, 2)
    rules = {}
    for title, body in secs:
        tl = title.lower()
        if tl.startswith("tom"):
            rules["tone"] = clean(body, 420)
        elif tl.startswith("anti-padr"):
            items = [clean(b, 220) for b in re.findall(r"^- (.+(?:\n {2,}.+)*)", body, re.M)]
            rules["anti_patterns"] = items[:8]
        elif tl.startswith("prioridade"):
            rules["priority"] = clean(body, 500)
        elif tl.startswith("regras centrais"):
            blocks = re.split(r"\n(?=\*\*)", "\n" + body)
            for b in blocks:
                b = b.strip()
                m = re.match(r"\*\*(.+?)\*\*", b)
                if not m:
                    continue
                head = m.group(1).lower()
                content = b
                key = None
                for k, rx in (("palette", "paleta"), ("typography", "tipograf"), ("density", "densidade"),
                              ("motion", "motion"), ("data", "dados"), ("trust", "confiança"),
                              ("regulation", "regulação"), ("accessibility", "acessibilidade|linguagem simples")):
                    if re.search(rx, head):
                        key = k
                        break
                if key and key not in rules:
                    if key == "palette":
                        rules[key] = clean(re.sub(r"\|.*\|", "", content), 520)
                    else:
                        rules[key] = clean(content, 620)
                    if key == "motion":
                        nm = re.search(r"Nunca animar[^:]*:?\*?\*?\s*(.+?)(?:\n-|\n\n|$)", content, re.S)
                        if nm:
                            rules["never_animate"] = clean(nm.group(1), 320)
    return rules


# ---------------------------------------------------------------- templates
ROLE_WORDS = [
    ("bg", r"fundo|superf|cards?\b|hero|surface|neutro"),
    ("text", r"texto|tipografia|principal|secundár|terciár|desabilitado"),
    ("action", r"aç[aã]o|acento|cta|link|destaque|pílula|marca|título"),
    ("border", r"borda"),
    ("state", r"estado|sucesso|erro|alerta|semânt|ganho|perda|risco"),
]


def _role_in(text):
    best, pos = None, -1
    for r, rx in ROLE_WORDS:
        for m in re.finditer(rx, text):
            if m.start() > pos:
                best, pos = r, m.start()
    return best


def palette_roles(fields):
    """Classifica cada hex por papel (bg/text/action/border/state/unknown) pelo texto entre o hex
    anterior e este, pelo parêntese logo depois e, por último, pelo rótulo da linha."""
    roles = {"bg": [], "text": [], "action": [], "border": [], "state": [], "unknown": []}
    approx = set()
    color_keys = [k for k in fields if not re.match(r"(fontes|imagens|quando|par tipo|escala|raio|sombra|densidade|motion|estrutura|cuidado|atenção)", k)]
    allhex = []
    for k in color_keys:
        val = fields[k]
        key_role = _role_in(k)
        last_role, last_end = None, 0
        for m in HEX_RE.finditer(val):
            h = norm_hex(m.group(2))
            if m.group(1):
                approx.add(h)
            between = val[last_end:m.start()].lower()
            after = re.match(r"`?\s*\(([^)]{0,40})\)", val[m.end():])
            role = _role_in(between)
            if role is None and after:
                role = _role_in(after.group(1).lower())
            if role is None and last_role and len(between.strip(" `")) <= 28:
                role = last_role
            if role is None:
                role = key_role or "unknown"
            last_role, last_end = role, m.end()
            if h not in allhex:
                allhex.append(h)
            if h not in roles[role]:
                roles[role].append(h)
    return roles, allhex, sorted(approx)


def _rgb(h):
    return tuple(int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))


def _hex(rgb):
    return "#" + "".join("%02X" % max(0, min(255, round(c * 255))) for c in rgb)


def lum(h):
    def ch(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in _rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def chroma(h):
    r, g, b = _rgb(h)
    return max(r, g, b) - min(r, g, b)


def mix(a, b, t):
    ra, rb = _rgb(a), _rgb(b)
    return _hex(tuple(x + (y - x) * t for x, y in zip(ra, rb)))


def ensure(fg, bg, target=4.5):
    """Aproxima fg de preto/branco até atingir o contraste pedido com bg."""
    if contrast(fg, bg) >= target:
        return fg, False
    pole = "#000000" if lum(bg) > 0.18 else "#FFFFFF"
    for i in range(1, 21):
        c = mix(fg, pole, i / 20)
        if contrast(c, bg) >= target:
            return c, True
    return pole, True


def preview_theme(roles, allhex, name, fonts, radius_shadow, density):
    dark_hint = bool(re.search(r"escur|preto|dark", name.lower()))
    text = roles["text"][:]
    bgs = roles["bg"][:]
    if bgs and not dark_hint:
        light = [h for h in bgs if lum(h) > 0.5]
        bgs = light or ["#FFFFFF"]
    pool = roles["unknown"] + roles["bg"] + roles["action"]
    if not bgs:
        neutrals = [h for h in roles["unknown"] if chroma(h) < 0.12]
        if text:
            cands = [h for h in neutrals if h not in text] or [h for h in roles["unknown"] if h not in text]
            if cands:
                bgs = [max(cands, key=lambda h: contrast(h, text[0]))]
        elif neutrals:
            bgs = [min(neutrals, key=lum)] if dark_hint else [max(neutrals, key=lum)]
    if not bgs:
        bgs = ["#0E0F11" if dark_hint else "#FFFFFF"]
    bg = bgs[0]
    if dark_hint and lum(bg) > 0.4:
        darks = [h for h in roles["bg"] + roles["unknown"] if lum(h) < 0.05]
        if darks:
            bg = darks[0]
    is_dark = lum(bg) < 0.18
    if not text:
        neutrals = [h for h in pool if h != bg and chroma(h) < 0.12 and contrast(h, bg) >= 3]
        text = [max(neutrals, key=lambda h: contrast(h, bg))] if neutrals else ["#F3F4F6" if is_dark else "#1A1C1F"]
    best = max(text, key=lambda h: contrast(h, bg))
    t0, adj_t = ensure(text[0] if contrast(text[0], bg) >= 4.5 else best, bg)
    text = [t0] + [h for h in text if h != t0 and contrast(h, bg) >= 3]
    surface = next((h for h in bgs[1:] + roles["unknown"] if h != bg and chroma(h) < 0.12
                    and contrast(h, bg) < 1.35 and contrast(t0, h) >= 4.5), None)
    if not surface:
        surface = mix(bg, "#FFFFFF" if is_dark else "#000000", 0.05 if is_dark else 0.035)
    muted_src = text[1] if len(text) > 1 else mix(t0, bg, 0.38)
    muted, _ = ensure(muted_src, bg)
    acts = [h for h in roles["action"] if h not in (bg,)]
    acts_sat = [h for h in acts if chroma(h) >= 0.12]
    if acts_sat:
        action = acts_sat[0]
    elif acts and contrast(acts[0], bg) >= 1.5:
        action = acts[0]
    else:
        others = [h for h in roles["unknown"] + roles["bg"] + roles["text"] + roles["state"]
                  if h not in (bg, t0) and chroma(h) >= 0.12]
        action = max(others, key=chroma) if others else t0
    on_action = "#FFFFFF" if contrast("#FFFFFF", action) >= contrast("#111111", action) else "#111111"
    if contrast(on_action, action) < 4.5:
        on_action = ensure(on_action, action)[0]
    if contrast(action, bg) < 3:
        action_text, adj_a = t0, False
    else:
        action_text, adj_a = ensure(action, bg)
    accent2 = next((h for h in roles["action"] + roles["state"] + roles["unknown"]
                    if h not in (bg, action, t0) and chroma(h) >= 0.12), None)
    border = roles["border"][0] if roles["border"] else mix(bg, t0, 0.14)
    f = fonts.lower()
    display = "Inter"
    for fam in ("Inter Tight", "Akshar"):
        if fam.lower() in f:
            display = fam
            break
    else:
        if re.search(r"arial|helvetica|frutiger", f):
            display = "Arial"
        elif "system-ui" in f:
            display = "system-ui"
    mono = "JetBrains Mono"
    body = "Arial" if display == "Arial" else ("system-ui" if display == "system-ui" else "Inter")
    rs = radius_shadow.lower()
    nums = [int(n) for n in re.findall(r"(\d+)\s*px", rs.split("sombra")[0])]
    if nums:
        radius = round(sum(nums[:2]) / len(nums[:2]))
    elif re.search(r"\balto\b|bem arredond", rs):
        radius = 16
    elif "pequeno" in rs:
        radius = 6
    elif "médio" in rs or "arredond" in rs:
        radius = 10
    else:
        radius = 8
    pill = bool(re.search(r"pílula", rs))
    d = density.lower()
    dens = "compact" if re.match(r"\s*(alta|média-alta|alta-média)", d) else ("airy" if re.match(r"\s*baixa", d) else "regular")
    return {"bg": bg, "surface": surface, "text": t0, "muted": muted, "action": action,
            "on_action": on_action, "action_text": action_text, "accent2": accent2, "border": border,
            "dark": is_dark, "font_display": display, "font_body": body, "font_mono": mono, "radius": radius, "pill": pill,
            "density": dens, "adjusted": adj_t or adj_a}


def parse_templates():
    items = []
    for code, segname, skill in SEGMENTS:
        if not skill:
            continue
        path = os.path.join(SKILLS, skill, "references", "templates.md")
        if not os.path.exists(path):
            continue
        text = read(path)
        for title, body in split_sections(text, 2):
            m = re.match(r"(TPL-[A-Z]{3}-\d+)\s*[—–-]\s*(.+)", title)
            if not m:
                continue
            tcode, name = m.group(1), m.group(2).strip()
            fields, _ = kv_fields(body)
            roles, allhex, approx = palette_roles(fields)
            imgs = []
            for mm in JPG_RE.finditer(pick(fields, "imagens")):
                b = os.path.basename(mm.group(1))
                if b not in imgs:
                    imgs.append(b)
            when = clean(pick(fields, "quando usar"), 400)
            raio = pick(fields, "raio")
            sombra = pick(fields, "sombra")
            rs = pick(fields, "raio / sombra", "raio/sombra")
            radius_shadow = clean(rs) if rs else clean("Raio: %s · Sombra: %s" % (clean(raio) or "—", clean(sombra) or "—"))
            extras = []
            for k in ("cuidado", "atenção", "estrutura"):
                if pick(fields, k):
                    extras.append("%s: %s" % (k.capitalize(), clean(pick(fields, k), 380)))
            scale = clean(pick(fields, "escala"), 260)
            density = clean(pick(fields, "densidade"), 200)
            plat_text = " ".join([when, scale, density, name])
            fonts_txt = clean(pick(fields, "par tipo"), 260)
            item = {
                "type": "template",
                "code": tcode,
                "name": name,
                "segment": code,
                "tokens": {
                    "palette": allhex,
                    "palette_roles": roles,
                    "palette_approx": approx,
                    "fonts": fonts_txt,
                    "scale": scale,
                    "radius_shadow": radius_shadow,
                    "density": density,
                    "motion": clean(pick(fields, "motion"), 320),
                },
                "when": when,
                "sources": clean(pick(fields, "fontes"), 320),
                "images": imgs,
                "rules_excerpt": " ".join(extras),
                "preview": preview_theme(roles, allhex, name, fonts_txt, radius_shadow, density),
                "platforms": infer_platforms(plat_text, ["mobile", "desktop", "website"]),
                "source_file": rel(path),
                "date_added": to_utc(git_first_date_string("## " + tcode, path)),
            }
            item["screens"] = infer_screens(when + " " + name)
            items.append(item)
    return items


# ---------------------------------------------------------------- componentes
def parse_components():
    items = []
    for code, _, skill in SEGMENTS:
        if not skill:
            continue
        path = os.path.join(SKILLS, skill, "references", "componentes.md")
        if not os.path.exists(path):
            continue
        text = read(path)
        for title, body in split_sections(text, 2):
            m = re.match(r"(CMP-[A-Z]{3}-\d+)\s*[—–-]\s*(.+)", title)
            if not m:
                continue
            ccode, name = m.group(1), m.group(2).strip()
            fields, _ = kv_fields(body)
            desc = pick(fields, "descrição") or pick(fields, "anatomia")
            anatomy = pick(fields, "anatomia")
            rules = pick(fields, "regras")
            states = pick(fields, "estados")
            plat = pick(fields, "plataformas")
            refs_txt = pick(fields, "referências")
            refimgs = []
            for mm in JPG_RE.finditer(body):
                b = os.path.basename(mm.group(1))
                if b not in refimgs:
                    refimgs.append(b)
            category = infer_category(name, clean(desc))
            item = {
                "type": "component",
                "code": ccode,
                "name": name,
                "segment": code,
                "category": category,
                "platforms": infer_platforms(clean(plat) or clean(desc), ["mobile", "desktop", "website"]),
                "description": clean(desc, 420),
                "anatomy": clean(anatomy, 520) if anatomy and anatomy != desc else "",
                "states": clean(states, 300),
                "rules": clean(rules, 520),
                "refs": clean(refs_txt, 360),
                "ref_images": refimgs,
                "source_file": rel(path),
                "date_added": to_utc(git_first_date_string("## " + ccode, path)),
            }
            item["screens"] = infer_screens(name + " " + clean(desc))
            items.append(item)
    return items


# ---------------------------------------------------------------- referências
def skill_dirs():
    for d in sorted(os.listdir(SKILLS)):
        p = os.path.join(SKILLS, d)
        if d.startswith("ext-") or d in EXCLUDE or not os.path.isdir(p):
            continue
        yield d, p


def index_rows():
    """{basename: [(skill, header_dict)]} de todas as tabelas dos visual-index.md."""
    rows = {}
    for skill, p in skill_dirs():
        vi = os.path.join(p, "references", "visual-index.md")
        if not os.path.exists(vi):
            continue
        for header, body in tables(read(vi)):
            for cells in body:
                if not cells:
                    continue
                first = cells[0]
                found = JPG_RE.findall(first) or ([] if len(cells) < 2 else [])
                if not found:
                    continue
                d = {}
                for i, h in enumerate(header):
                    if i < len(cells):
                        d[h] = cells[i]
                for f in found:
                    rows.setdefault(os.path.basename(f), []).append((skill, d))
    return rows


def first_url(text):
    m = re.search(r"https?://[^\s|)`>]+", text or "")
    return m.group(0).rstrip(".,;") if m else ""


def row_get(d, *names):
    for n in names:
        for k, v in d.items():
            if k.startswith(n) and v and v.strip() not in ("—", "-"):
                return v
    return ""


def sha1(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_references(make_thumbs=True):
    files = []
    for skill, p in skill_dirs():
        vr = os.path.join(p, "assets", "visual-refs")
        if not os.path.isdir(vr):
            continue
        for f in sorted(os.listdir(vr)):
            if f.lower().endswith(".jpg"):
                files.append((skill, os.path.join(vr, f)))

    # dedupe: por nome, depois por hash
    groups = {}   # key -> list[(skill, path)]
    by_hash = {}
    name_key = {}
    for skill, path in files:
        b = os.path.basename(path)
        if b in name_key:
            groups[name_key[b]].append((skill, path))
            continue
        h = sha1(path)
        if h in by_hash:
            key = by_hash[h]
        else:
            key = b
            by_hash[h] = key
            groups[key] = []
        name_key[b] = key
        groups[key].append((skill, path))

    rows = index_rows()
    # segmentos que citam imagens de outras skills
    seg_mentions = {}
    for skill, p in skill_dirs():
        if skill not in SEG_BY_SKILL:
            continue
        for fn in ("visual-index.md", "templates.md", "componentes.md"):
            fp = os.path.join(p, "references", fn)
            if os.path.exists(fp):
                for mm in JPG_RE.finditer(read(fp)):
                    seg_mentions.setdefault(os.path.basename(mm.group(1)), set()).add(SEG_BY_SKILL[skill])

    refs = []
    for key, members in groups.items():
        names = []
        for _, path in members:
            b = os.path.basename(path)
            if b not in names:
                names.append(b)
        owner_skills = []
        for s, _ in members:
            if s not in owner_skills:
                owner_skills.append(s)
        # linhas do índice: dono primeiro
        cand = []
        for n in names:
            for s, d in rows.get(n, []):
                cand.append((0 if s in owner_skills else 1, s, d))
        cand.sort(key=lambda x: x[0])
        meta = {"name": "", "what": "", "author": "", "url": "", "platform": "", "when": "", "domain": "", "style": "", "observe": ""}
        for _, s, d in cand:
            meta["name"] = meta["name"] or row_get(d, "nome")
            meta["what"] = meta["what"] or row_get(d, "o que mostra", "o que observar", "o que serve", "por que abrir")
            meta["author"] = meta["author"] or row_get(d, "autor", "produto/autor")
            meta["url"] = meta["url"] or first_url(row_get(d, "url")) or first_url(row_get(d, "autor", "produto/autor"))
            meta["platform"] = meta["platform"] or row_get(d, "plataforma")
            meta["when"] = meta["when"] or row_get(d, "quando abrir", "como adaptar")
            meta["domain"] = meta["domain"] or row_get(d, "domínio")
            meta["style"] = meta["style"] or row_get(d, "estilo")
        # plataformas
        plats = []
        if meta["platform"]:
            plats = infer_platforms(meta["platform"])
        for s, _, in [(s, d) for _, s, d in cand]:
            if s in PLATFORM_SKILLS and PLATFORM_SKILLS[s] not in plats:
                plats.append(PLATFORM_SKILLS[s])
        if not plats:
            plats = infer_platforms(" ".join([meta["what"], meta["domain"], meta["when"]]))
        # segmentos
        segs = []
        for s in owner_skills:
            if s in SEG_BY_SKILL and SEG_BY_SKILL[s] not in segs:
                segs.append(SEG_BY_SKILL[s])
        primary = segs[0] if segs else "GER"
        if not segs:
            segs = ["GER"]
        for n in names:
            for sc in sorted(seg_mentions.get(n, ())):
                if sc not in segs:
                    segs.append(sc)
        # data mais antiga entre as cópias
        dates = [to_utc(git_first_date(rel(p))) for _, p in members]
        dates = [d for d in dates if d]
        date = min(dates) if dates else None
        name = clean(meta["name"]) or clean(meta["domain"], 70) or clean(meta["what"], 70) or names[0]
        author = clean(meta["author"])
        author = re.sub(r"\s*https?://\S+", "", author).strip()
        refs.append({
            "type": "reference",
            "file": names[0],
            "aliases": names[1:],
            "name": name,
            "author": author,
            "url": meta["url"],
            "what": clean(meta["what"], 420),
            "when": clean(meta["when"], 260),
            "style": clean(meta["style"], 80),
            "segment": primary,
            "segments": segs,
            "platforms": plats,
            "skills": owner_skills,
            "image": rel(members[0][1]),
            "copies": [rel(p) for _, p in members[1:]],
            "date_added": date,
            "screens": infer_screens(" ".join([meta["what"], meta["domain"], meta["when"], name])),
        })

    refs.sort(key=lambda r: (r["date_added"] is None, r["date_added"] or "", r["image"]))
    for i, r in enumerate(refs, 1):
        r["code"] = "REF-%04d" % i
    if make_thumbs:
        os.makedirs(THUMBS, exist_ok=True)
        for f in os.listdir(THUMBS):
            if f.endswith(".webp"):
                os.remove(os.path.join(THUMBS, f))
    for r in refs:
        thumb = os.path.join(THUMBS, r["code"] + ".webp")
        r["thumb"] = "thumbs/%s.webp" % r["code"]
        if make_thumbs:
            subprocess.run(
                ["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", os.path.join(ROOT, r["image"]),
                 "-vf", "scale=480:-2", "-c:v", "libwebp", "-quality", "70", "-frames:v", "1", thumb],
                check=False)
        r["thumb_w"], r["thumb_h"] = probe_size(thumb) if os.path.exists(thumb) else (480, 300)
    return refs


def probe_size(path):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                              "stream=width,height", "-of", "csv=p=0:s=x", path],
                             capture_output=True, text=True, check=False).stdout.strip()
        w, h = out.split("x")[:2]
        return int(w), int(h)
    except Exception:
        return 480, 300



# ---------------------------------------------------------------- biblioteca referencias/ (fonte principal)
ID_RX = r"[A-Za-z0-9_\-]{10,11}"
KIND_LABEL = {"reel": "Reel", "carrossel": "Carrossel", "print": "Print", "galeria": "Galeria", "skill": "Imagem de skill"}


def post_id_of(fname):
    stem = os.path.basename(fname).rsplit(".", 1)[0]
    for rx in (r"^(?:10A_)?(" + ID_RX + r")(?:_\d+)?$", r"^9E_.+?_(" + ID_RX + r")_\d+$"):
        m = re.match(rx, stem)
        if m:
            return m.group(1)
    return None


def short_name(*texts, limit=72):
    for t in texts:
        t = (t or "").strip().strip('"“”')
        if not t:
            continue
        t = re.sub(r"\s+", " ", t)
        m = re.match(r"(.{12,}?[.!?])(\s|$)", t)
        if m and len(m.group(1)) <= limit:
            return m.group(1).rstrip(".")
        return clean(t, limit)
    return ""


def load_library():
    p = os.path.join(LIB, "index.json")
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8") as f:
        recs = json.load(f).get("referencias", [])
    out = []
    for rec in recs:
        a = rec.get("arquivos", {})
        if rec["tipo"] == "reel":
            imgs = [{"path": "referencias/" + x["arquivo"], "w": x["w"], "h": x["h"], "t": x.get("t")} for x in a.get("frames", [])]
            imgs += [{"path": "referencias/" + x["arquivo"], "w": x["w"], "h": x["h"]} for x in a.get("prints", [])]
            lp = a.get("loop")
            loop = {"path": "referencias/" + lp["arquivo"], "w": lp["w"], "h": lp["h"], "start": lp.get("inicio"),
                    "dur": lp.get("duracao")} if lp else None
        else:
            imgs = [{"path": "referencias/" + x["arquivo"], "w": x["w"], "h": x["h"]} for x in a.get("imagens", [])]
            loop = None
        segs = [x for x in rec.get("segmentos") or ["GER"]]
        nonger = [x for x in segs if x != "GER"]
        segs = nonger or ["GER"]
        files = [os.path.basename(i["path"]) for i in imgs if "/prints/" in i["path"]]
        out.append({
            "type": "reference", "kind": rec["tipo"], "id_post": rec["id_post"],
            "name": short_name(rec.get("nome"), rec.get("legenda"), rec.get("o_que_mostra")) or rec["id_post"],
            "author": rec.get("autor") or "", "author_name": rec.get("autor_nome") or "",
            "url": rec.get("url") or "", "what": clean(rec.get("o_que_mostra") or "", 420), "when": "",
            "caption": clean(rec.get("legenda_completa") or rec.get("legenda") or "", 600),
            "segment": segs[0], "segments": segs, "platforms": rec.get("plataformas") or [],
            "skills": rec.get("skills") or [], "lib_tags": rec.get("tags") or [],
            "date_added": to_utc(rec.get("data_envio")), "date_source": rec.get("data_envio_fonte"),
            "date_origin": rec.get("data_origem"), "duration": rec.get("duracao"),
            "src_images": imgs, "src_loop": loop, "aliases": files, "image": imgs[0]["path"] if imgs else "",
            "doc": rec.get("doc") or "",
        })
    return out


def merge_references(lib, skill_refs):
    """Biblioteca primeiro; imagens das skills que casam por ID/arquivo viram alias (enriquecem texto,
    skills e segmentos). As que sobram entram como referências próprias (kind 'skill')."""
    by_key = {}
    for r in lib:
        by_key.setdefault(r["id_post"], r)
        for f in r["aliases"]:
            by_key.setdefault(f, r)
            by_key.setdefault(f.rsplit(".", 1)[0], r)
    out = list(lib)
    for sr in skill_refs:
        names = [sr["file"]] + sr["aliases"]
        hit = None
        for n in names:
            stem = n.rsplit(".", 1)[0]
            hit = by_key.get(n) or by_key.get(stem) or by_key.get(post_id_of(n) or "\0")
            if hit:
                break
        if hit:
            for n in names:
                if n not in hit["aliases"]:
                    hit["aliases"].append(n)
            for k in ("skills",):
                for v in sr[k]:
                    if v not in hit[k]:
                        hit[k].append(v)
            for sg in sr["segments"]:
                if sg != "GER" and sg not in hit["segments"]:
                    hit["segments"] = [x for x in hit["segments"] if x != "GER"] + [sg]
            hit["segment"] = hit["segments"][0]
            if not hit["what"] and sr["what"]:
                hit["what"] = sr["what"]
            hit["when"] = hit["when"] or sr["when"]
            hit["author"] = hit["author"] or sr["author"]
            hit["url"] = hit["url"] or sr["url"]
            if not hit["date_added"] and sr["date_added"]:
                hit["date_added"], hit["date_source"] = sr["date_added"], "git"
            for p in sr["platforms"]:
                if p not in hit["platforms"]:
                    hit["platforms"].append(p)
            hit.setdefault("skill_images", []).append(sr["image"])
            continue
        w, h = image_size(os.path.join(ROOT, sr["image"]))
        out.append({
            "type": "reference", "kind": "skill", "id_post": post_id_of(sr["file"]) or sr["file"].rsplit(".", 1)[0],
            "name": sr["name"], "author": sr["author"], "author_name": "", "url": sr["url"], "what": sr["what"],
            "when": sr["when"], "caption": "", "segment": sr["segment"], "segments": sr["segments"],
            "platforms": sr["platforms"], "skills": sr["skills"], "lib_tags": [],
            "date_added": sr["date_added"], "date_source": "git", "date_origin": None, "duration": None,
            "src_images": [{"path": sr["image"], "w": w, "h": h}], "src_loop": None,
            "aliases": [sr["file"]] + sr["aliases"], "image": sr["image"], "doc": "",
        })
    return out


def image_size(path):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                              "stream=width,height", "-of", "csv=p=0:s=x", path],
                             capture_output=True, text=True, check=False).stdout.strip()
        w, h = out.split("x")[:2]
        return int(w), int(h)
    except Exception:
        return 1200, 800


def ffmpeg_img(src, dst, width, webp=False, q=None):
    vf = "scale='min(%d,iw)':-2:flags=lanczos" % width
    args = ["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", src, "-vf", vf, "-frames:v", "1"]
    if webp:
        args += ["-c:v", "libwebp", "-quality", str(q or 72)]
    else:
        args += ["-q:v", str(q or 3)]
    subprocess.run(args + [dst], check=False)


def build_media(refs, make):
    """catalogo/media/<REF>/: thumb.webp (480), 1.jpg..N.jpg (grandes: frames 900 / prints ≤ 1200), loop.webp."""
    if make:
        if os.path.isdir(MEDIA):
            shutil.rmtree(MEDIA)
        if os.path.isdir(THUMBS):
            shutil.rmtree(THUMBS)
        os.makedirs(MEDIA)
    for r in refs:
        d = os.path.join(MEDIA, r["code"])
        rel_d = "media/" + r["code"]
        if make:
            os.makedirs(d, exist_ok=True)
        media = []
        for i, im in enumerate(r["src_images"], 1):
            dst = os.path.join(d, "%d.jpg" % i)
            src = os.path.join(ROOT, im["path"])
            if make:
                if im["path"].startswith("referencias/") and im["w"] <= 1200:
                    shutil.copyfile(src, dst)
                else:
                    ffmpeg_img(src, dst, 1200)
            w, h = (im["w"], im["h"]) if im["w"] <= 1200 else (1200, round(im["h"] * 1200 / im["w"]))
            media.append({"src": "%s/%d.jpg" % (rel_d, i), "w": w, "h": h, "t": im.get("t")})
        thumb = os.path.join(d, "thumb.webp")
        if make and r["src_images"]:
            ffmpeg_img(os.path.join(ROOT, r["src_images"][0]["path"]), thumb, 480, webp=True, q=70)
        tw, th = image_size(thumb) if os.path.exists(thumb) else (480, 300)
        r["media"] = media
        r["thumb"], r["thumb_w"], r["thumb_h"] = rel_d + "/thumb.webp", tw, th
        r["loop"] = None
        if r["src_loop"]:
            if make:
                shutil.copyfile(os.path.join(ROOT, r["src_loop"]["path"]), os.path.join(d, "loop.webp"))
            r["loop"] = {"src": rel_d + "/loop.webp", "w": r["src_loop"]["w"], "h": r["src_loop"]["h"],
                         "dur": r["src_loop"]["dur"]}
        r["image"] = r["image"] or (r["src_images"][0]["path"] if r["src_images"] else "")
        r.pop("src_images", None)
        r.pop("src_loop", None)


CAT_TAGS = {"navegação": ["tab bar", "sidebar", "⌘K", "bottom sheet"], "dados": ["dashboard", "gráfico", "kanban"],
            "formulário": ["formulário", "login", "botão"], "feedback": ["toast", "loader", "micro-interação"],
            "motion": ["motion", "micro-interação", "drag-and-drop", "loader"], "layout": ["landing", "dashboard"],
            "confiança": ["landing", "formulário"], "conteúdo": ["IA", "tipografia"]}


def related_refs(item, refs, cited, n=6):
    seg = item["segment"]
    words = norm_words(" ".join([item["name"], item.get("when", ""), item.get("description", ""),
                                 item.get("category", ""), " ".join(item.get("screens", []))]))
    want = set(CAT_TAGS.get(item.get("category"), []))
    scored = []
    for r in refs:
        if r["code"] in cited:
            continue
        sc = 0.0
        if seg != "GER" and seg in r["segments"]:
            sc += 4
        elif seg != "GER":
            sc -= 1
        sc += 1.2 * len(set(item.get("screens", [])) & set(r["screens"]))
        sc += 0.4 * len(set(item.get("platforms", [])) & set(r["platforms"]))
        tags = set(r["lib_tags"])
        sc += 1.0 * len(want & tags)
        sc += 0.6 * sum(1 for t in tags if t.lower() in words)
        if r["kind"] in ("reel", "carrossel", "print", "galeria"):
            sc += 0.5
        if sc >= 3:
            scored.append((sc, r["date_added"] or "", r["code"]))
    scored.sort(key=lambda x: x[1], reverse=True)   # mais novas primeiro no empate
    scored.sort(key=lambda x: -x[0])
    return [c for _, _, c in scored[:n]]


def norm_words(t):
    return t.lower()


# ---------------------------------------------------------------- main
def main():
    make_thumbs = "--no-thumbs" not in sys.argv
    templates = parse_templates()
    components = parse_components()
    skill_refs = parse_references(False)
    lib = load_library()
    references = merge_references(lib, skill_refs)
    for r in references:
        r["screens"] = infer_screens(" ".join([r["name"], r["what"], r["caption"], " ".join(r["lib_tags"])]))
    references.sort(key=lambda r: (r["date_added"] is None, r["date_added"] or "", r["id_post"]))
    for i, r in enumerate(references, 1):
        r["code"] = "REF-%04d" % i
    build_media(references, make_thumbs)

    ref_by_file = {}
    for r in references:
        for n in [r["id_post"]] + r["aliases"]:
            ref_by_file.setdefault(n, r["code"])
            ref_by_file.setdefault(n.rsplit(".", 1)[0], r["code"])

    def resolve(names):
        out = []
        for n in names:
            c = ref_by_file.get(n) or ref_by_file.get(n.rsplit(".", 1)[0]) or ref_by_file.get(post_id_of(n) or "\0")
            if c and c not in out:
                out.append(c)
        return out
    for t in templates:
        t["ref_codes"] = resolve(t["images"])
    for c in components:
        c["ref_codes"] = resolve(c["ref_images"])
    # citações nas skills por ID de post (sem .jpg), dentro do texto do template/componente
    for coll in (templates, components):
        for it in coll:
            it["ref_related"] = related_refs(it, references, set(it["ref_codes"]))

    # tags
    for t in templates:
        t["tags"] = sorted(set([t["segment"], "template"] + t["platforms"] + t["screens"] + t["tokens"]["palette"]))
    for c in components:
        c["tags"] = sorted(set([c["segment"], "componente", c["category"]] + c["platforms"] + c["screens"]))
    for r in references:
        tg = set(r["segments"] + r["platforms"] + r["screens"] + r["skills"] + r["lib_tags"] + ["referência", KIND_LABEL.get(r["kind"], r["kind"]).lower()])
        if r["author"]:
            tg.add(r["author"])
        tg.update(hexes(r["what"]))
        r["tags"] = sorted(tg)
    cited_by = {}
    for it in templates + components:
        for c in it["ref_codes"]:
            cited_by.setdefault(c, []).append(it["code"])
    for r in references:
        r["cited_by"] = cited_by.get(r["code"], [])
        r.pop("lib_tags", None)

    segs = []
    for code, name, skill in SEGMENTS:
        rules = segment_rules(os.path.join(SKILLS, skill)) if skill else {
            "tone": "Referências gerais das skills de tema e plataforma (design-direction, dashboard-ui, ui-motion, ux-patterns, mobile-app-ui, desktop-app-ui, website-ui). Valem para qualquer segmento, abaixo das regras do segmento."}
        count = (sum(1 for t in templates if t["segment"] == code)
                 + sum(1 for c in components if c["segment"] == code)
                 + sum(1 for r in references if code in r["segments"]))
        segs.append({"code": code, "name": name, "skill": skill, "count": count,
                     "counts": {"templates": sum(1 for t in templates if t["segment"] == code),
                                "components": sum(1 for c in components if c["segment"] == code),
                                "references": sum(1 for r in references if code in r["segments"])},
                     "rules": rules})

    data = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "theme_skills": ["design-direction", "dashboard-ui", "ui-motion", "ux-patterns"],
        "platform_skills": {"mobile": "mobile-app-ui", "desktop": "desktop-app-ui", "website": "website-ui"},
        "segments": segs,
        "templates": templates,
        "components": components,
        "references": references,
    }
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, "catalogo.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")

    nfiles, size = 0, 0
    for dp, _, fs in os.walk(MEDIA):
        for f in fs:
            nfiles += 1
            size += os.path.getsize(os.path.join(dp, f))
    from collections import Counter
    nodate = sum(1 for r in references if not r["date_added"])
    print("templates:   %d" % len(templates))
    print("componentes: %d" % len(components))
    print("referências: %d (sem data: %d) por tipo: %s" % (len(references), nodate, dict(Counter(r["kind"] for r in references))))
    print("media:       %d arquivos (%.1f MB)" % (nfiles, size / 1048576))
    print("json:        %s (%.1f KB)" % (rel(out), os.path.getsize(out) / 1024))
    for s_ in segs:
        print("  %s %-14s %s" % (s_["code"], s_["name"], s_["counts"]))


if __name__ == "__main__":
    main()
