#!/usr/bin/env python3
"""Gera catalogo/catalogo.json e catalogo/thumbs/*.webp a partir das skills de design.

Fonte única: .claude/skills/segmento-*/references/{templates,componentes,visual-index}.md,
SKILL.md de cada segmento e os visual-index.md das skills de tema/plataforma.
Exclui ext-* e quant-investing (não é de design).

Uso (da raiz da repo):  python3 -I scripts/build-catalog.py [--no-thumbs]
Requer só a stdlib e o ffmpeg (com libwebp) no PATH para as miniaturas.
"""
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, ".claude", "skills")
OUT_DIR = os.path.join(ROOT, "catalogo")
THUMBS = os.path.join(OUT_DIR, "thumbs")
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
    ("landing", r"landing|hero|home\b|site|vitrine|página de preços|preços"),
    ("lista/tabela", r"tabela|lista|extrato|kanban|pipeline|fila|feed"),
    ("formulário", r"formul|checkout|campo|cadastro|captura|busca|agendamento|login|senha"),
    ("detalhe", r"detalhe|perfil|prontuário|case|estudo de caso|contato\b"),
    ("onboarding", r"onboarding|boas-vindas|permiss|primeiro uso"),
    ("motion", r"motion|anima|transição|micro-intera|loader|scroll|reel|slow-mo|spring"),
    ("marca/cor", r"paleta|tipograf|fonte|logo|marca|branding|cor\b|cores"),
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
    ("bg", r"fundo|superf|hero|claro|escuro|neutro|surface"),
    ("text", r"texto|principal|secundár|terciár"),
    ("action", r"aç[aã]o|acento|cta|link|destaque|marca|pílula|azul|verde|lima|lilás"),
    ("border", r"borda"),
    ("state", r"estado|sucesso|erro|alerta|semânt|ganho|perda"),
]


def palette_roles(fields):
    """Classifica cada hex por papel (bg/text/action/border/state) usando o rótulo da linha
    e as palavras imediatamente antes do hex."""
    roles = {"bg": [], "text": [], "action": [], "border": [], "state": []}
    approx = set()
    color_keys = [k for k in fields if not re.match(r"(fontes|imagens|quando|par tipo|escala|raio|sombra|densidade|motion|estrutura|cuidado|atenção)", k)]
    allhex = []
    for k in color_keys:
        val = fields[k]
        last_role = None
        for m in HEX_RE.finditer(val):
            h = norm_hex(m.group(2))
            if m.group(1):
                approx.add(h)
            before = val[max(0, m.start() - 48):m.start()].lower()
            before = re.split(r"[;,(]\s*(?=[a-zà-ú])", before)[-1] if before else ""
            role = None
            for r, rx in ROLE_WORDS:
                if re.search(rx, before):
                    role = r
            if role is None:
                for r, rx in ROLE_WORDS:
                    if re.search(rx, k):
                        role = r
                        break
            if role is None:
                role = last_role or "action"
            last_role = role
            if h not in roles[role]:
                roles[role].append(h)
            if h not in allhex:
                allhex.append(h)
    return roles, allhex, sorted(approx)


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
            item = {
                "type": "template",
                "code": tcode,
                "name": name,
                "segment": code,
                "tokens": {
                    "palette": allhex,
                    "palette_roles": roles,
                    "palette_approx": approx,
                    "fonts": clean(pick(fields, "par tipo"), 260),
                    "scale": scale,
                    "radius_shadow": radius_shadow,
                    "density": density,
                    "motion": clean(pick(fields, "motion"), 320),
                },
                "when": when,
                "sources": clean(pick(fields, "fontes"), 320),
                "images": imgs,
                "rules_excerpt": " ".join(extras),
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


# ---------------------------------------------------------------- main
def main():
    make_thumbs = "--no-thumbs" not in sys.argv
    templates = parse_templates()
    components = parse_components()
    references = parse_references(make_thumbs)

    ref_by_file = {}
    for r in references:
        for n in [r["file"]] + r["aliases"]:
            ref_by_file[n] = r["code"]
    for t in templates:
        t["ref_codes"] = [ref_by_file[i] for i in t["images"] if i in ref_by_file]
    for c in components:
        c["ref_codes"] = [ref_by_file[i] for i in c["ref_images"] if i in ref_by_file]

    # tags
    for t in templates:
        t["tags"] = sorted(set([t["segment"], "template"] + t["platforms"] + t["screens"] + t["tokens"]["palette"]))
    for c in components:
        c["tags"] = sorted(set([c["segment"], "componente", c["category"]] + c["platforms"] + c["screens"]))
    for r in references:
        tg = set(r["segments"] + r["platforms"] + r["screens"] + r["skills"] + ["referência"])
        if r["author"]:
            tg.add(r["author"])
        tg.update(hexes(r["what"]))
        r["tags"] = sorted(tg)

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

    thumbs = [os.path.join(THUMBS, f) for f in os.listdir(THUMBS)] if os.path.isdir(THUMBS) else []
    size = sum(os.path.getsize(p) for p in thumbs)
    nodate = sum(1 for r in references if not r["date_added"])
    print("templates:   %d" % len(templates))
    print("componentes: %d" % len(components))
    print("referências: %d (sem data: %d)" % (len(references), nodate))
    print("miniaturas:  %d (%.1f KB)" % (len(thumbs), size / 1024))
    print("json:        %s (%.1f KB)" % (rel(out), os.path.getsize(out) / 1024))
    for s in segs:
        print("  %s %-14s %s" % (s["code"], s["name"], s["counts"]))


if __name__ == "__main__":
    main()
