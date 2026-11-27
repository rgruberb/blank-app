#!/usr/bin/env python3
"""Landing final (opção 4, TPL-SAU-04) com tema claro/escuro e PT/EN. Uso: final.py <arquivo-de-saida> [--artifact]"""
import sys, os, json, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gerar as G

OUT = sys.argv[1]
ARTIFACT = "--artifact" in sys.argv

# ---------- textos: chave -> (pt, en) ----------
T = {
 "title": ("RG AI Saúde · Back-office de saúde", "RG AI Health · Healthcare back-office"),
 "desc": ("Painéis sob medida para a operação da clínica enxergar prazos de autorização, guias de convênio e fila antes que virem prejuízo.",
          "Custom dashboards that show your clinic's operations team authorization deadlines, insurance claims and queues before they turn into losses."),
 "skip": ("Pular para o conteúdo", "Skip to content"),
 "brand": ("RG AI Saúde", "RG AI Health"),
 "nav_como": ("Como funciona", "How it works"),
 "nav_planos": ("Planos", "Plans"),
 "nav_faq": ("Dúvidas", "FAQ"),
 "cta": ("Agendar uma conversa", "Book a call"),
 "kicker": ("Back-office de saúde", "Healthcare back-office"),
 "h1": ("Autorizações, convênios e fila sob controle", "Authorizations, insurers and queues under control"),
 "sub": ("Painéis para a operação da clínica enxergar prazos e guias paradas antes que virem prejuízo.",
         "Dashboards that show your clinic's operations team deadlines and stalled claims before they turn into losses."),
 "fine": ("Resposta por e-mail, sem compromisso.", "We reply by email, no commitment."),
 "mk_tag": ("Exemplo de tela · dados fictícios", "Sample screen · fictional data"),
 "mk_h": ("Guias que precisam de alguém", "Claims that need someone"),
 "mk_1": ("Guia 1042 · Convênio A · ressonância", "Claim 1042 · Insurer A · MRI"),
 "mk_1v": ("R$ 1.240,00", "R$1,240.00"),
 "mk_1s": ("Vence em 2 dias", "Due in 2 days"),
 "mk_2": ("Guia 1038 · Convênio B · consulta", "Claim 1038 · Insurer B · visit"),
 "mk_2v": ("R$ 180,00", "R$180.00"),
 "mk_2s": ("Negada", "Denied"),
 "mk_3": ("Guia 1031 · Convênio A · exame", "Claim 1031 · Insurer A · lab test"),
 "mk_3v": ("R$ 96,50", "R$96.50"),
 "mk_3s": ("Autorizada", "Approved"),
 "prova_k": ("Prova social", "Track record"),
 "prova_h": ("O que já está no ar", "What's already live"),
 "s1b": ("3 apps", "3 apps"), "s1": ("em produção, construídos do requisito ao deploy", "in production, built from requirements to deploy"),
 "s2b": ("mar/2026", "Mar 2026"), "s2": ("no ar desde então, em uso diário", "live since then, in daily use"),
 "s3b": ("+200%", "+200%"), "s3": ("de produtividade em prospecção e gestão de carteira", "productivity in prospecting and portfolio management"),
 "s4b": ("INPI", "Trademark"), "s4": ("registramos a marca do seu sistema", "we register your system's brand with the INPI (Brazil)"),
 "case_k": ("Caso em produção · crédito e recebíveis", "Live case · credit and receivables"),
 "case_h": ("Carteira360: agenda, rotas de visita e alertas para uma equipe comercial", "Carteira360: schedules, visit routes and alerts for a sales team"),
 "case_p1": ("Construímos para uma empresa de crédito (FIDC) um app que organiza a agenda e as rotas de visita e avisa quando um cliente parou de operar. O gestor vê a equipe toda; o gerente vê a própria carteira, no computador ou no celular.",
             "We built an app for a credit company (a Brazilian receivables fund) that organizes schedules and visit routes and flags when a client stops operating. Managers see the whole team; each account manager sees their own portfolio, on desktop or phone."),
 "case_p2": ("É o mesmo problema de uma operação clínica com muitas guias: nenhuma pode ficar esquecida.",
             "It's the same problem as a clinic handling many insurance claims: none of them can be forgotten."),
 "case_src": ("O cliente não é identificado. Números informados pelo próprio uso em produção.", "The client is not named. Figures come from production use."),
 "como_k": ("Como funciona", "How it works"),
 "como_h": ("Quatro etapas, da conversa ao sistema no ar", "Four steps, from first call to a live system"),
 "st1h": ("Conversa", "Call"), "st1": ("Você mostra onde a operação trava: autorizações, guias, glosas, fila da central.", "You show us where operations get stuck: authorizations, claims, denials, the call-center queue."),
 "st2h": ("Protótipo", "Prototype"), "st2": ("Você vê e clica nos painéis principais antes da construção, com estimativa de prazo e custo.", "You see and click through the main dashboards before we build, with a time and cost estimate."),
 "st3h": ("Construção", "Build"), "st3": ("Ligamos o painel às planilhas e sistemas que a clínica já usa, em ciclos curtos.", "We connect the dashboards to the spreadsheets and systems your clinic already uses, in short cycles."),
 "st4h": ("Operação", "Operation"), "st4": ("Colocamos no ar, treinamos a equipe e cuidamos de hospedagem, backups e ajustes.", "We go live, train your team and take care of hosting, backups and adjustments."),
 "pl_k": ("Preços e planos", "Pricing and plans"),
 "pl_h": ("Comece pequeno, cresça com a clínica", "Start small, grow with your clinic"),
 "flag": ("Recomendado", "Recommended"),
 "price": ("Sob consulta", "On request"), "price_s": ("valor enviado por escrito", "quoted in writing"),
 "p1h": ("Diagnóstico", "Assessment"), "p1f": ("Para entender o problema antes de investir", "To understand the problem before investing"),
 "p1a": ("Mapeamento do processo atual", "Map of your current process"), "p1b": ("Protótipo clicável dos painéis principais", "Clickable prototype of the main dashboards"), "p1c": ("Estimativa de prazo e custo por escrito", "Written time and cost estimate"),
 "p2h": ("Projeto", "Project"), "p2f": ("Para construir o painel da operação", "To build your operations dashboards"),
 "p2a": ("Sistema web sob medida, no computador e no celular", "Custom web system, on desktop and phone"), "p2b": ("Acesso por papéis e backups diários", "Role-based access and daily backups"), "p2c": ("Treinamento da equipe", "Team training"), "p2d": ("Registro da marca no INPI", "Trademark registration with the INPI"),
 "p3h": ("Operação", "Operation"), "p3f": ("Para manter o sistema de pé, todo mês", "To keep the system running, every month"),
 "p3a": ("Hospedagem e monitoramento", "Hosting and monitoring"), "p3b": ("Backups e atualizações de segurança", "Backups and security updates"), "p3c": ("Ajustes e pequenas melhorias", "Adjustments and small improvements"), "p3d": ("Suporte por e-mail", "Email support"),
 "pl_note": ("Os valores dependem do escopo e são enviados por escrito depois do Diagnóstico. Sem cobrança automática e sem fidelidade escondida.",
             "Prices depend on scope and are sent in writing after the Assessment. No automatic charges and no hidden lock-in."),
 "faq_k": ("Dúvidas", "FAQ"), "faq_h": ("Perguntas frequentes", "Frequently asked questions"),
 "q1": ("Vocês já fizeram sistema para clínica?", "Have you built systems for clinics before?"),
 "a1": ("Nossos três apps em produção são do setor de crédito, onde prazo, valor em risco e fila são o dia a dia. Em saúde, estamos construindo um produto próprio para agências que atendem médicos. O método é o mesmo: requisito, protótipo, produção e operação.",
        "Our three apps in production are in the credit sector, where deadlines, money at risk and queues are daily work. In healthcare, we are building our own product for agencies that serve doctors. The method is the same: requirements, prototype, production and operation."),
 "q2": ("Como vocês cuidam dos dados dos pacientes?", "How do you handle patient data?"),
 "a2": ("Dado de saúde é dado sensível pela LGPD (art. 5º, II). Usamos acesso por papéis, senhas com hash, conexão criptografada e backups. Os painéis mostram só o que cada papel precisa ver, e nada é compartilhado com terceiros.",
        "Health data is sensitive personal data under Brazil's LGPD (art. 5, II). We use role-based access, hashed passwords, encrypted connections and backups. Dashboards show each role only what it needs, and nothing is shared with third parties."),
 "q3": ("Quanto custa?", "How much does it cost?"),
 "a3": ("Depende do escopo. O Diagnóstico existe para isso: ao final, você recebe por escrito o prazo e o valor do Projeto e da Operação.",
        "It depends on scope. That's what the Assessment is for: at the end, you get the time and price of the Project and Operation in writing."),
 "q4": ("Vocês substituem o sistema que a clínica já usa?", "Do you replace the system the clinic already uses?"),
 "a4": ("Não precisa. O painel pode ler as planilhas e exportações do sistema atual e mostrar o que está parado, vencendo ou negado.",
        "No need. The dashboards can read your current system's spreadsheets and exports and show what is stalled, due or denied."),
 "q5": ("Funciona no celular?", "Does it work on phones?"),
 "a5": ("Sim. Os sistemas são web e funcionam no navegador do computador e do celular, sem instalar nada.", "Yes. Our systems run in the browser on desktop and phone, with nothing to install."),
 "q6": ("Vocês registram a marca do sistema?", "Do you register the system's brand?"),
 "a6": ("Sim. No plano Projeto, registramos a marca do seu sistema no INPI.", "Yes. In the Project plan, we register your system's brand with the INPI, Brazil's trademark office."),
 "fin_k": ("Contato", "Contact"),
 "fin_h": ("Vamos conversar sobre a operação da sua clínica.", "Let's talk about your clinic's operations."),
 "fin_p": ("Mande um e-mail contando onde a operação mais trava hoje. Respondemos com um horário para conversar.",
           "Send us an email about where your operations get stuck most. We'll reply with a time to talk."),
 "copy": ("Copiar e-mail", "Copy email"),
 "foot1": ("RG AI Ltda · Rafael Gruber Bernstein", "RG AI Ltda · Rafael Gruber Bernstein"),
 "foot2": ("Telas de exemplo com dados fictícios. Sem promessa de resultado.", "Sample screens with fictional data. No promised results."),
}
UI = {  # textos só do JavaScript
 "pt": {"copied": "E-mail copiado.", "sel": "E-mail selecionado. Use Ctrl+C ou Cmd+C para copiar.", "toLight": "Mudar para o tema claro", "toDark": "Mudar para o tema escuro",
        "mk_aria": "Exemplo de tela: guias de convênio com prazo e valor em risco, uma vencendo em 2 dias, uma negada e uma autorizada."},
 "en": {"copied": "Email copied.", "sel": "Email selected. Press Ctrl+C or Cmd+C to copy.", "toLight": "Switch to light theme", "toDark": "Switch to dark theme",
        "mk_aria": "Sample screen: insurance claims with deadline and amount at risk; one due in 2 days, one denied and one approved."},
}

def t(k, tag="span"):
    return f'<{tag} data-i18n="{k}">{html.escape(T[k][0])}</{tag}>' if tag != "raw" else html.escape(T[k][0])

def ti(k):  # texto dentro de um elemento que já existe: data-i18n no próprio elemento
    return f'data-i18n="{k}"'

def tx(k): return html.escape(T[k][0])

THEME_LIGHT = """
--bg:#F5F6F7;--alt:#FFFFFF;--surface:#FFFFFF;--ink-2:#2E3338;--muted:#59626A;--head:#101214;--rule:#DDE1E4;--rule-strong:#B5BCC2;
--link:#0B6E52;--focus:#0B6E52;--kicker:#0B6E52;--cta:#0E7A5C;--cta-h:#0B6650;--cta-ink:#FFFFFF;
--top-bg:#F5F6F7;--top-ink:#101214;--top-rule:#DDE1E4;--hero-bg:#F5F6F7;--hero-ink:#2E3338;--hero-head:#101214;--hero-kicker:#0B6E52;
--mk-bg:#FFFFFF;--mk-ink:#2E3338;--mk-head:#101214;--mk-muted:#59626A;--mk-rule:#E4E7EA;--mk-shadow:0 1px 2px rgba(16,18,20,.06),0 20px 44px -20px rgba(14,122,92,.30);
--chip-bg:#EEF0F2;--chip-ink:#2E3338;--ok-bg:#DDF3EA;--ok-ink:#0B5A43;--warn-bg:#FFF1D1;--warn-ink:#5C4400;--bad-bg:#FBE3E1;--bad-ink:#8A1C12;
--stat-line:1px solid #0E7A5C;--step-bg:#FFFFFF;--step-border:1px solid #DDE1E4;--num-bg:#DDF3EA;--num-ink:#0B5A43;--check:#0E7A5C;
--final-bg:#101214;--final-ink:#C9CED3;--final-head:#FFFFFF;--final-kicker:#5FD3B0;--final-cta:#2FB58F;--final-cta-ink:#04130E;--final-rule:#3A3D42;
--foot-bg:#F5F6F7;--foot-ink:#59626A;--cta-shadow:none;--plan-shadow:0 18px 40px -20px rgba(14,122,92,.30);color-scheme:light;
"""

EXTRA_CSS = f"""
@media (prefers-color-scheme:light){{:root:not([data-theme="dark"]){{{THEME_LIGHT}}}}}
:root[data-theme="light"]{{{THEME_LIGHT}}}
.mk .val{{color:var(--mk-head)}}
.final{{border-top:1px solid var(--rule)}}
.tools{{display:flex;align-items:center;gap:8px}}
.seg{{display:inline-flex;border:1px solid var(--rule-strong);border-radius:999px;padding:2px}}
.seg button{{min-width:44px;min-height:40px;border:0;border-radius:999px;background:transparent;color:var(--top-ink);font:600 .85rem/1 var(--f-body);cursor:pointer}}
.seg button[aria-pressed="true"]{{background:var(--top-ink);color:var(--top-bg)}}
.icon-btn{{display:inline-grid;place-items:center;width:44px;height:44px;border-radius:50%;border:1px solid var(--rule-strong);background:transparent;color:var(--top-ink);cursor:pointer}}
.icon-btn svg{{width:20px;height:20px}}
.icon-btn .i-sun{{display:none}}
.is-dark .icon-btn .i-sun{{display:block}}.is-dark .icon-btn .i-moon{{display:none}}
.top nav{{gap:20px}}
@media(max-width:1060px){{.top nav a.nl{{display:none}}}}
@media(max-width:600px){{.top .w{{gap:8px}}.top nav .btn{{display:none}}}}
@media(max-width:360px){{.brand span{{display:none}}}}
"""

MOCK = f"""
<div class="mk" role="img" data-i18n-aria="mk_aria" aria-label="{html.escape(UI['pt']['mk_aria'])}">
  <p class="tagx">{t('mk_tag')}</p>
  <h3>{t('mk_h')}</h3>
  <ul>
    <li><span>{t('mk_1')}<br><span class="val">{t('mk_1v')}</span></span><span class="chip warn"><span aria-hidden="true">▲</span> {t('mk_1s')}</span></li>
    <li><span>{t('mk_2')}<br><span class="val">{t('mk_2v')}</span></span><span class="chip bad"><span aria-hidden="true">✕</span> {t('mk_2s')}</span></li>
    <li><span>{t('mk_3')}<br><span class="val">{t('mk_3v')}</span></span><span class="chip ok"><span aria-hidden="true">✓</span> {t('mk_3s')}</span></li>
  </ul>
</div>"""

def plan(i, items, hl):
    lis = "".join(f"<li>{t(k)}</li>" for k in items)
    flag = f'<span class="flag">{t("flag")}</span>' if hl else ""
    return (f'<article class="plan{" hl" if hl else ""}">{flag}<h3>{t(f"p{i}h")}</h3><p class="for">{t(f"p{i}f")}</p>'
            f'<p class="price">{t("price")}<small>{t("price_s")}</small></p><ul>{lis}</ul>'
            f'<a class="btn {"pri" if hl else "sec"}" href="#contato">{t("cta")}</a></article>')

EN = {k: v[1] for k, v in T.items()}
faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": T[f"q{i}"][0], "acceptedAnswer": {"@type": "Answer", "text": T[f"a{i}"][0]}} for i in range(1, 7)]}, ensure_ascii=False)

HEAD_JS = """(function(){var r=document.documentElement;try{var th=localStorage.getItem('rgai-saude-theme');if(th==='dark'||th==='light')r.setAttribute('data-theme',th);var l=localStorage.getItem('rgai-saude-lang');if(l==='en'||l==='pt')r.setAttribute('data-lang',l)}catch(e){}if(!r.getAttribute('data-lang')){r.setAttribute('data-lang',/^pt/i.test(navigator.language||'pt')?'pt':'en')}})();"""

BODY_JS = """(function(){
var r=document.documentElement,EN=__EN__,UI=__UI__,PT={},PTA={};
var nodes=[].slice.call(document.querySelectorAll('[data-i18n]')),anodes=[].slice.call(document.querySelectorAll('[data-i18n-aria]'));
nodes.forEach(function(n){PT[n.getAttribute('data-i18n')]=n.textContent});
var md=document.querySelector('meta[name=description]');PT.title=document.title;PT.desc=md.content;
var lang='pt';
function setLang(l,save){lang=l;var D=l==='en'?EN:PT;
 nodes.forEach(function(n){var k=n.getAttribute('data-i18n');if(D[k]!=null)n.textContent=D[k]});
 anodes.forEach(function(n){n.setAttribute('aria-label',UI[l][n.getAttribute('data-i18n-aria')])});
 document.title=D.title;md.content=D.desc;r.lang=l==='en'?'en':'pt-BR';r.setAttribute('data-lang',l);
 [].forEach.call(document.querySelectorAll('[data-setlang]'),function(b){b.setAttribute('aria-pressed',b.getAttribute('data-setlang')===l?'true':'false')});
 if(save){try{localStorage.setItem('rgai-saude-lang',l)}catch(e){}}paintTheme()}
[].forEach.call(document.querySelectorAll('[data-setlang]'),function(b){b.addEventListener('click',function(){setLang(b.getAttribute('data-setlang'),true)})});
var tb=document.getElementById('theme'),mq=matchMedia('(prefers-color-scheme: light)');
function curTheme(){var v=r.getAttribute('data-theme');return v?v:(mq.matches?'light':'dark')}
function paintTheme(){var d=curTheme()==='dark';r.classList.toggle('is-dark',d);tb.setAttribute('aria-label',d?UI[lang].toLight:UI[lang].toDark)}
tb.addEventListener('click',function(){var n=curTheme()==='dark'?'light':'dark';r.setAttribute('data-theme',n);try{localStorage.setItem('rgai-saude-theme',n)}catch(e){}paintTheme()});
if(mq.addEventListener)mq.addEventListener('change',paintTheme);
setLang(r.getAttribute('data-lang')==='en'?'en':'pt',false);
var b=document.getElementById('copy'),m=document.getElementById('copied'),e=document.getElementById('mail');
function sel(){try{var x=document.createRange();x.selectNodeContents(e);var s=getSelection();s.removeAllRanges();s.addRange(x)}catch(z){}}
b.addEventListener('click',function(){var tt=e.textContent.trim();function ok(){m.textContent=UI[lang].copied;setTimeout(function(){m.textContent=''},2500)}function no(){sel();m.textContent=UI[lang].sel}try{navigator.clipboard.writeText(tt).then(ok,no)}catch(z){no()}});
})();""".replace("__EN__", json.dumps(EN, ensure_ascii=False)).replace("__UI__", json.dumps(UI, ensure_ascii=False))

SUN = '<svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2" fill="currentColor"/><g stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/></g></svg>'
MOON = '<svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z" fill="currentColor"/></svg>'

head_meta = f"""<title>{tx('title')}</title>
<meta name="description" content="{tx('desc')}">
<meta property="og:title" content="{tx('title')}">
<meta property="og:description" content="{tx('desc')}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:locale:alternate" content="en_US">
<script type="application/ld+json">{faq_ld}</script>
<script>{HEAD_JS}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{G.FONTS[4]}&display=swap">
<style>{G.BASE_CSS}{G.THEMES[4]}{EXTRA_CSS}</style>"""

body = f"""<a class="skip" href="#conteudo">{t('skip', 'raw')}</a>
<header class="top">
  <div class="w">
    <a class="brand" href="#conteudo">{G.LOGOS[4]}<span data-i18n="brand">{tx('brand')}</span></a>
    <nav aria-label="Seções">
      <a class="nl" href="#como-funciona" {ti('nav_como')}>{tx('nav_como')}</a>
      <a class="nl" href="#planos" {ti('nav_planos')}>{tx('nav_planos')}</a>
      <a class="nl" href="#duvidas" {ti('nav_faq')}>{tx('nav_faq')}</a>
      <div class="tools">
        <div class="seg" role="group" aria-label="Idioma / Language"><button type="button" data-setlang="pt" aria-pressed="true" lang="pt-BR">PT</button><button type="button" data-setlang="en" aria-pressed="false" lang="en">EN</button></div>
        <button class="icon-btn" id="theme" type="button" aria-label="Mudar para o tema claro">{MOON}{SUN}</button>
      </div>
      <a class="btn pri" href="#contato" {ti('cta')}>{tx('cta')}</a>
    </nav>
  </div>
</header>
<main id="conteudo">
  <div class="hero">
    <div class="w hero-grid">
      <div>
        <p class="kicker" {ti('kicker')}>{tx('kicker')}</p>
        <h1 {ti('h1')}>{tx('h1')}</h1>
        <p class="sub" {ti('sub')}>{tx('sub')}</p>
        <div class="acts"><a class="btn pri" href="#contato" {ti('cta')}>{tx('cta')}</a><span class="fine" {ti('fine')}>{tx('fine')}</span></div>
      </div>
      <div class="mockup">{MOCK}</div>
    </div>
  </div>

  <section class="band" id="prova" aria-labelledby="h-prova">
    <div class="w">
      <div class="sh"><p class="kicker" {ti('prova_k')}>{tx('prova_k')}</p><h2 id="h-prova" {ti('prova_h')}>{tx('prova_h')}</h2></div>
      <div class="stats">{''.join(f'<div class="stat"><b {ti(f"s{i}b")}>{tx(f"s{i}b")}</b><span {ti(f"s{i}")}>{tx(f"s{i}")}</span></div>' for i in range(1,5))}</div>
      <div class="case"><div><p class="kicker" {ti('case_k')}>{tx('case_k')}</p><h3 {ti('case_h')}>{tx('case_h')}</h3></div>
        <div><p {ti('case_p1')}>{tx('case_p1')}</p><p {ti('case_p2')}>{tx('case_p2')}</p><p class="src" {ti('case_src')}>{tx('case_src')}</p></div></div>
    </div>
  </section>

  <section id="como-funciona" aria-labelledby="h-como">
    <div class="w">
      <div class="sh"><p class="kicker" {ti('como_k')}>{tx('como_k')}</p><h2 id="h-como" {ti('como_h')}>{tx('como_h')}</h2></div>
      <ol class="steps">{''.join(f'<li><h3 {ti(f"st{i}h")}>{tx(f"st{i}h")}</h3><p {ti(f"st{i}")}>{tx(f"st{i}")}</p></li>' for i in range(1,5))}</ol>
    </div>
  </section>

  <section class="band" id="planos" aria-labelledby="h-planos">
    <div class="w">
      <div class="sh"><p class="kicker" {ti('pl_k')}>{tx('pl_k')}</p><h2 id="h-planos" {ti('pl_h')}>{tx('pl_h')}</h2></div>
      <div class="plans">{plan(1,['p1a','p1b','p1c'],False)}{plan(2,['p2a','p2b','p2c','p2d'],True)}{plan(3,['p3a','p3b','p3c','p3d'],False)}</div>
      <p class="plans-note" {ti('pl_note')}>{tx('pl_note')}</p>
    </div>
  </section>

  <section id="duvidas" aria-labelledby="h-faq">
    <div class="w">
      <div class="sh"><p class="kicker" {ti('faq_k')}>{tx('faq_k')}</p><h2 id="h-faq" {ti('faq_h')}>{tx('faq_h')}</h2></div>
      <div class="faq">{''.join(f'<details><summary {ti(f"q{i}")}>{tx(f"q{i}")}</summary><p {ti(f"a{i}")}>{tx(f"a{i}")}</p></details>' for i in range(1,7))}</div>
    </div>
  </section>

  <section class="final" id="contato" aria-labelledby="h-final">
    <div class="w">
      <p class="kicker" {ti('fin_k')}>{tx('fin_k')}</p>
      <h2 id="h-final" {ti('fin_h')}>{tx('fin_h')}</h2>
      <p class="l" {ti('fin_p')}>{tx('fin_p')}</p>
      <div class="acts">
        <code id="mail">rafael@gruberia.com</code>
        <button class="btn pri" id="copy" type="button" {ti('copy')}>{tx('copy')}</button>
        <a class="btn sec" href="https://www.linkedin.com/in/rafaelgruberbernstein" target="_blank" rel="noopener">LinkedIn</a>
      </div>
      <p class="copied" id="copied" role="status" aria-live="polite"></p>
    </div>
  </section>
</main>
<footer><div class="w"><span {ti('foot1')}>{tx('foot1')}</span><span {ti('foot2')}>{tx('foot2')}</span></div></footer>
<script>{BODY_JS}</script>"""

# skip link usa t(...,'raw'): marcar para tradução também
body = body.replace(f'<a class="skip" href="#conteudo">{tx("skip")}</a>', f'<a class="skip" href="#conteudo" {ti("skip")}>{tx("skip")}</a>')

if ARTIFACT:
    doc = head_meta.replace("<title>", '<meta name="claude:viewport-fit-sides" content="cover">\n<title>', 1) + "\n" + body + "\n"
else:
    doc = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<link rel="canonical" href="https://gruberia.com/saude/">
{head_meta}
</head>
<body>
{body}
</body>
</html>
"""
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(doc)
print("ok", OUT, len(doc))
