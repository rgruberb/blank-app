#!/usr/bin/env python3
"""Landing RG AI v3 — escura por padrão, impactante, projetos em abas na própria página, PT/EN e tema claro.
Uso: final3.py <saida.html> [--artifact]"""
import sys, json, html

OUT = sys.argv[1]
ARTIFACT = "--artifact" in sys.argv
E = lambda s: html.escape(s, quote=True)

T = {
 "title": ("RG AI · Apps sob medida", "RG AI · Custom apps"),
 "desc": ("Apps web de dados e IA sob medida, do requisito à produção. Três em produção desde março de 2026. Especialidade em crédito e finanças.",
          "Custom data and AI web apps, from requirements to production. Three in production since March 2026. Specialized in credit and finance."),
 "skip": ("Pular para o conteúdo", "Skip to content"),
 "nav_proj": ("Projetos", "Projects"), "nav_como": ("Como funciona", "How it works"), "nav_planos": ("Planos", "Plans"), "nav_faq": ("Dúvidas", "FAQ"),
 "cta": ("Agendar uma conversa", "Book a call"),
 "see": ("Ver os projetos", "See the projects"),
 "badge": ("3 apps em produção desde mar/2026", "3 apps in production since Mar 2026"),
 "h1a": ("Apps sob medida,", "Custom apps,"),
 "h1b": ("do requisito à", "from requirements to"),
 "h1c": ("produção.", "production."),
 "sub": ("Construímos o app que a sua operação precisa, com dados e IA, e cuidamos dele depois do deploy.",
         "We build the app your operation needs, with data and AI, and look after it once it's live."),
 "fl1": ("Em produção", "In production"), "fl1b": ("Retreino diário", "Daily retraining"),
 "fl2": ("Produtividade", "Productivity"),
 "frame_alt": ("RiskAI FIDC: resumo da carteira com grupos por faixa de risco, dados fictícios.", "RiskAI FIDC: portfolio summary with groups by risk band, fictional data."),
 "m1": ("apps em produção", "apps in production"),
 "m2": ("de produtividade em prospecção e gestão de carteira", "productivity in prospecting and portfolio management"),
 "m3": ("telas reais nesta página, com dados fictícios", "real screens on this page, with fictional data"),
 "m4": ("no ar e em uso diário desde", "live and in daily use since"),
 "m4v": ("mar/2026", "Mar 2026"),
 "proj_k": ("Projetos", "Projects"),
 "proj_h": ("Apps que já estão rodando", "Apps that are already running"),
 "proj_p": ("Escolha um projeto e navegue pelas telas. Tudo com dados fictícios; nenhum cliente é identificado.",
            "Pick a project and browse its screens. All with fictional data; no client is identified."),
 "lb_hint": ("Clique na tela para ampliar", "Click the screen to enlarge"),
 "dt_prob": ("Problema", "Problem"), "dt_what": ("O que faz", "What it does"), "dt_how": ("Como", "How"), "dt_stat": ("Situação", "Status"), "dt_for": ("Para quem", "For whom"),
 # RiskAI
 "ra_tag": ("Em produção · comitê de crédito", "In production · credit committee"),
 "ra_out": ("Leitura de risco e deterioração da carteira, por cedente e grupo econômico.", "Risk and deterioration reading of the portfolio, by client and economic group."),
 "ra_prob": ("O comitê decide se ajusta o limite ou encerra a relação com um cedente. Precisa ver cedo onde a carteira piora.",
             "The committee decides whether to adjust a client's limit or end the relationship. It needs to see early where the portfolio is getting worse."),
 "ra_what": ("Mostra o estado de cada cedente e os sinais que antecedem a piora: freada da originação, recompras e prorrogações. Compara a PDD do mês com indicadores do BCB e do IBGE.",
             "Shows each client's state and the signals that come before deterioration: slowing origination, buybacks and extensions. Compares the month's provisions with Central Bank and IBGE indicators."),
 "ra_how": ("Validação fora do tempo, com critério de aprovação escrito antes de ver o resultado. Retreino diário que só publica modelos aprovados.",
            "Out-of-time validation, with the approval criterion written before seeing results. Daily retraining that only publishes approved models."),
 "ra_stat": ("Em produção.", "In production."),
 "ra_s1": ("Resumo", "Summary"), "ra_s2": ("Ficha do grupo", "Group profile"), "ra_s3": ("Sinais", "Signals"), "ra_s4": ("PDD e indicadores", "Provisions vs. indicators"),
 "ra_a1": ("Resumo da carteira com grupos por faixa de risco e maiores variações.", "Portfolio summary with groups by risk band and largest changes."),
 "ra_a2": ("Ficha de um grupo econômico com risco total, limite e sinais.", "Economic group profile with total risk, limit and signals."),
 "ra_a3": ("Sinais de piora na carteira, com número de grupos e risco de cada sinal.", "Deterioration signals, with number of groups and risk per signal."),
 "ra_a4": ("PDD lançada mês a mês ao lado da inadimplência PJ do Banco Central.", "Monthly provisions next to the Central Bank's corporate default rate."),
 # LeadScout
 "ls_tag": ("Em produção · área comercial", "In production · sales"),
 "ls_out": ("Pesquisa de IA para prospectar, em que um modelo audita o outro.", "AI research for prospecting, where one model audits the other."),
 "ls_prob": ("Prospectar exige pesquisar cada empresa. Pesquisa de IA sem checagem pode afirmar o que ninguém confirmou.",
             "Prospecting means researching every company. Unchecked AI research can state things nobody confirmed."),
 "ls_what": ("Pesquisa cada lead com a API da Anthropic, dá uma nota e escreve um parecer com provas e fontes. Integra com o CRM: funil, agenda e distribuição de leads.",
             "Researches each lead with the Anthropic API, scores it and writes an assessment with evidence and sources. Integrates with the CRM: pipeline, schedule and lead distribution."),
 "ls_how": ("Afirmação sem fonte verificável fica marcada como indeterminada, visível na tela.", "Any claim without a verifiable source is flagged as undetermined, right on screen."),
 "ls_stat": ("Em produção, junto com o Carteira360.", "In production, alongside Carteira360."),
 "ls_s1": ("Ficha do lead", "Lead profile"), "ls_s2": ("Lista", "List"), "ls_s3": ("Funil", "Pipeline"),
 "ls_a1": ("Ficha do lead com nota, lastro, parecer e fontes. CNPJ e telefone borrados.", "Lead profile with score, assessment and sources. Tax ID and phone blurred."),
 "ls_a2": ("Lista de leads com fila, nota, lastro, etapa e próximo passo.", "Lead list with queue, score, backing, stage and next step."),
 "ls_a3": ("Funil por etapa, de Novo a Cadastro efetivo.", "Pipeline by stage, from New to Signed up."),
 # Carteira360
 "c3_tag": ("Em produção · gestão de carteira", "In production · portfolio management"),
 "c3_out": ("Agenda, rotas de visita e alerta de cliente que parou de operar.", "Schedules, visit routes and alerts when a client stops operating."),
 "c3_prob": ("Numa carteira grande, quem para de operar ou fica sem visita passa despercebido.", "In a large portfolio, clients who stop operating or go unvisited slip through."),
 "c3_what": ("Organiza agenda e rotas e avisa quando um cliente parou. O gestor vê a equipe toda; o gerente vê a própria carteira, no computador ou no celular.",
             "Organizes schedules and routes and flags when a client stops. Managers see the whole team; account managers see their own portfolio, on desktop or phone."),
 "c3_how": ("Regras ambíguas viraram lógica determinística: prazo de visita, o que conta como atraso, o que é cliente parado.",
            "Ambiguous rules became deterministic logic: visit deadlines, what counts as late, what counts as a stalled client."),
 "c3_stat": ("Em produção. Com o LeadScout, +200% de produtividade.", "In production. With LeadScout, +200% productivity."),
 "c3_s1": ("Gestor", "Manager"), "c3_s2": ("Relatório", "Report"), "c3_s3": ("Rota", "Route"), "c3_s4": ("Gerente", "Account manager"), "c3_s5": ("Celular", "Phone"),
 "c3_a1": ("Mesa do gestor com visitas atrasadas, vencidos e parados por pessoa.", "Manager desk with late visits, overdue and stalled clients per person."),
 "c3_a2": ("Relatório de receita mês a mês contra a meta, por gerente.", "Monthly revenue report against target, per account manager."),
 "c3_a3": ("Rota do dia no mapa com paradas numeradas.", "Today's route on a map with numbered stops."),
 "c3_a4": ("Tela Hoje do gerente com pendências e ficha do cliente.", "Account manager's Today screen with tasks and client profile."),
 "c3_a5": ("Relatórios e alertas no celular.", "Reports and alerts on the phone."),
 # Wonespace
 "wn_tag": ("Produto próprio · em construção", "Our own product · in development"),
 "wn_out": ("Agência e médico trabalham no mesmo dado, em tempo real.", "Agency and doctor work on the same data, in real time."),
 "wn_for": ("Agências que produzem conteúdo para a marca pessoal de médicos, e os próprios médicos.", "Agencies producing personal-brand content for doctors, and the doctors themselves."),
 "wn_what": ("A agência acompanha produção e prazos. O médico aprova, responde e vê o que está pendente, no celular.", "The agency tracks production and deadlines. The doctor approves, replies and sees what's pending, on the phone."),
 "wn_stat": ("Em construção. Demonstração completa ao vivo, com acordo de confidencialidade.", "In development. Full demo live, under a confidentiality agreement."),
 "wn_s1": ("Lado a lado", "Side by side"), "wn_s2": ("App do médico", "Doctor's app"),
 "wn_a1": ("Painel da agência e app do médico lado a lado.", "Agency dashboard and doctor's app side by side."),
 "wn_a2": ("App do médico no celular, tela Hoje.", "Doctor's app on the phone, Today screen."),
 # segmentos
 "seg_k": ("Para quem", "Who it's for"), "seg_h": ("Onde já conhecemos o terreno", "Where we already know the ground"),
 "g1k": ("Especialidade", "Specialty"), "g1h": ("Crédito e finanças", "Credit and finance"),
 "g1p": ("Risco, prospecção, carteira e relatórios para fundos de recebíveis, financeiras e times comerciais.", "Risk, prospecting, portfolio and reporting for receivables funds, lenders and sales teams."),
 "g2k": ("Também", "Also"), "g2h": ("Saúde", "Healthcare"),
 "g2p": ("Back-office de clínicas: autorizações, guias de convênio, agenda e fila, com dado de saúde tratado como sensível.", "Clinic back-office: authorizations, insurance claims, scheduling and queues, with health data treated as sensitive."),
 "g3k": ("Também", "Also"), "g3h": ("Agências de marca pessoal", "Personal-brand agencies"),
 "g3p": ("Produção, aprovação e mensagens entre agência e cliente no mesmo app.", "Production, approvals and messages between agency and client in one app."),
 # como funciona
 "como_k": ("Como funciona", "How it works"), "como_h": ("Da conversa ao app no ar, em quatro etapas", "From first call to a live app, in four steps"),
 "st1h": ("Conversa", "Call"), "st1": ("Você conta onde o processo trava hoje. Saímos com o problema escrito.", "You tell us where the process gets stuck. We leave with the problem written down."),
 "st2h": ("Protótipo", "Prototype"), "st2": ("Você clica nas telas principais antes da construção, com estimativa de prazo e custo.", "You click through the main screens before we build, with a time and cost estimate."),
 "st3h": ("Construção", "Build"), "st3": ("Ciclos curtos. A cada entrega, a sua equipe testa e opina.", "Short cycles. At each delivery, your team tests and gives feedback."),
 "st4h": ("Operação", "Operation"), "st4": ("Colocamos no ar, treinamos a equipe e cuidamos de hospedagem, backups e ajustes.", "We go live, train your team and take care of hosting, backups and adjustments."),
 # fundador
 "fd_k": ("Quem constrói", "Who builds it"),
 "fd_role": ("Fundador · Product Owner · Engenheiro mecânico (PUC-Rio e Technion)", "Founder · Product Owner · Mechanical engineer (PUC-Rio and Technion)"),
 "fd_p": ("Há mais de três anos levo produtos de dados e IA do conceito à produção, dois deles de visão computacional na Radix. Desde março de 2026, a RG AI constrói apps sob medida.",
          "For more than three years I've taken data and AI products from concept to production, two of them computer-vision products at Radix. Since March 2026, RG AI has built custom apps."),
 "fd_c1": ("CSPO", "CSPO"), "fd_c2": ("Inglês fluente", "Fluent English"), "fd_c3": ("Claude Code", "Claude Code"),
 # planos
 "pl_k": ("Preços e planos", "Pricing and plans"), "pl_h": ("Comece pequeno, cresça com o app", "Start small, grow with the app"),
 "flag": ("Recomendado", "Recommended"), "price": ("Sob consulta", "On request"), "price_s": ("valor enviado por escrito", "quoted in writing"),
 "p1h": ("Diagnóstico", "Assessment"), "p1f": ("Para entender o problema antes de investir", "To understand the problem before investing"),
 "p1a": ("Mapeamento do processo atual", "Map of your current process"), "p1b": ("Protótipo clicável das telas principais", "Clickable prototype of the main screens"), "p1c": ("Estimativa de prazo e custo por escrito", "Written time and cost estimate"),
 "p2h": ("Projeto", "Project"), "p2f": ("Para construir o app", "To build the app"),
 "p2a": ("App web sob medida, no computador e no celular", "Custom web app, on desktop and phone"), "p2b": ("Acesso por papéis e backups diários", "Role-based access and daily backups"), "p2c": ("Treinamento da equipe", "Team training"), "p2d": ("Registro da marca no INPI", "Trademark registration with the INPI"),
 "p3h": ("Operação", "Operation"), "p3f": ("Para manter o app de pé, todo mês", "To keep the app running, every month"),
 "p3a": ("Hospedagem e monitoramento", "Hosting and monitoring"), "p3b": ("Backups e atualizações de segurança", "Backups and security updates"), "p3c": ("Ajustes e pequenas melhorias", "Adjustments and small improvements"), "p3d": ("Suporte por e-mail", "Email support"),
 "pl_note": ("Os valores dependem do escopo e são enviados por escrito depois do Diagnóstico. Sem cobrança automática e sem fidelidade escondida.",
             "Prices depend on scope and are sent in writing after the Assessment. No automatic charges and no hidden lock-in."),
 # faq
 "faq_k": ("Dúvidas", "FAQ"), "faq_h": ("Perguntas frequentes", "Frequently asked questions"),
 "q1": ("Que tipo de app vocês fazem?", "What kind of apps do you build?"),
 "a1": ("Aplicações web de dados e IA sob medida: painéis de risco, prospecção e CRM, gestão de carteira, agenda e operação. A especialidade é crédito e finanças; também atendemos saúde e agências de marca pessoal.",
        "Custom data and AI web apps: risk dashboards, prospecting and CRM, portfolio management, scheduling and operations. Our specialty is credit and finance; we also serve healthcare and personal-brand agencies."),
 "q2": ("Quanto custa?", "How much does it cost?"),
 "a2": ("Depende do escopo. Depois da primeira conversa, enviamos prazo e valor por escrito.", "It depends on scope. After our first call, we send the timeline and price in writing."),
 "q3": ("Quanto tempo leva?", "How long does it take?"),
 "a3": ("Depende do tamanho do app. Você recebe a estimativa junto com o protótipo, antes de decidir construir.", "It depends on the size of the app. You get the estimate with the prototype, before deciding to build."),
 "q4": ("Como vocês usam IA?", "How do you use AI?"),
 "a4": ("Quando ela ajuda. Comparamos modelos por acurácia, custo e desempenho, escrevemos o critério de aprovação antes de ver o resultado, e um modelo que não passa não vai para a tela.",
        "Where it helps. We compare models on accuracy, cost and performance, write the approval criterion before seeing results, and a model that fails doesn't reach the screen."),
 "q5": ("Como vocês cuidam dos dados?", "How do you handle data?"),
 "a5": ("Acesso por papéis, senhas com hash, conexão criptografada, backups e monitoramento. Em saúde, todo dado clínico é tratado como sensível, como manda a LGPD.",
        "Role-based access, hashed passwords, encrypted connections, backups and monitoring. In healthcare, all clinical data is treated as sensitive, as Brazil's LGPD requires."),
 "q6": ("Funciona no celular?", "Does it work on phones?"),
 "a6": ("Sim. Os apps são web e funcionam no navegador do computador e do celular, sem instalar nada.", "Yes. Our apps run in the browser on desktop and phone, with nothing to install."),
 "q7": ("Vocês registram a marca do app?", "Do you register the app's brand?"),
 "a7": ("Sim. Registramos a marca do seu app no INPI.", "Yes. We register your app's brand with the INPI, Brazil's trademark office."),
 "q8": ("Vocês cuidam do app depois de pronto?", "Do you look after the app once it's live?"),
 "a8": ("Sim. Cuidamos de hospedagem, backups, monitoramento, atualizações de segurança e ajustes, todo mês.", "Yes. We take care of hosting, backups, monitoring, security updates and adjustments, every month."),
 "q9": ("Dá para integrar com o que já usamos?", "Can it integrate with what we already use?"),
 "a9": ("Sim. O app pode ler planilhas e exportações do sistema atual ou conversar com ele por API.", "Yes. The app can read spreadsheets and exports from your current system or talk to it through an API."),
 # final
 "fin_k": ("Contato", "Contact"), "fin_h1": ("Qual processo você quer", "Which process do you want"), "fin_h2": ("tirar da planilha?", "out of spreadsheets?"),
 "fin_p": ("Mande um e-mail contando onde a sua operação trava. Respondemos com um horário para conversar.", "Email us about where your operation gets stuck. We'll reply with a time to talk."),
 "copy": ("Copiar e-mail", "Copy email"),
 "foot1": ("RG AI Ltda · Rafael Gruber Bernstein", "RG AI Ltda · Rafael Gruber Bernstein"),
 "foot2": ("Telas de demonstração com dados fictícios. Sem promessa de resultado.", "Demo screens with fictional data. No promised results."),
}
UI = {"pt": {"copied": "E-mail copiado", "sel": "E-mail selecionado. Use Ctrl+C ou Cmd+C.", "toLight": "Mudar para o tema claro", "toDark": "Mudar para o tema escuro", "lang": "Idioma", "close": "Fechar", "zoom": "Ampliar tela", "screens": "Telas", "projects": "Projetos", "pause": "Pausar animação", "play": "Retomar animação"},
      "en": {"copied": "Email copied", "sel": "Email selected. Press Ctrl+C or Cmd+C.", "toLight": "Switch to light theme", "toDark": "Switch to dark theme", "lang": "Language", "close": "Close", "zoom": "Enlarge screen", "screens": "Screens", "projects": "Projects", "pause": "Pause animation", "play": "Resume animation"}}

def tx(k): return E(T[k][0])
def ti(k): return f'data-i18n="{k}"'
def tt(k, tag="span", cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} {ti(k)}>{tx(k)}</{tag}>'

IMG = "portfolio/img/"
PROJECTS = [
 dict(id="riskai", name="RiskAI FIDC", p="ra", own=False, rows=[("dt_prob","ra_prob"),("dt_what","ra_what"),("dt_how","ra_how"),("dt_stat","ra_stat")],
      shots=[("riskai-1.webp","ra_s1","ra_a1"),("riskai-2.webp","ra_s2","ra_a2"),("riskai-4.webp","ra_s3","ra_a3"),("riskai-5.webp","ra_s4","ra_a4")]),
 dict(id="leadscout", name="LeadScout", p="ls", own=False, rows=[("dt_prob","ls_prob"),("dt_what","ls_what"),("dt_how","ls_how"),("dt_stat","ls_stat")],
      shots=[("leadscout-1.webp","ls_s1","ls_a1"),("leadscout-2.webp","ls_s2","ls_a2"),("leadscout-3.webp","ls_s3","ls_a3")]),
 dict(id="carteira360", name="Carteira360", p="c3", own=False, rows=[("dt_prob","c3_prob"),("dt_what","c3_what"),("dt_how","c3_how"),("dt_stat","c3_stat")],
      shots=[("carteira360-3.webp","c3_s1","c3_a1"),("carteira360-4.webp","c3_s2","c3_a2"),("carteira360-5.webp","c3_s3","c3_a3"),("carteira360-1.webp","c3_s4","c3_a4"),("carteira360-m1.webp","c3_s5","c3_a5")]),
 dict(id="wonespace", name="Wonespace", p="wn", own=True, rows=[("dt_for","wn_for"),("dt_what","wn_what"),("dt_stat","wn_stat")],
      shots=[("wonespace-1.webp","wn_s1","wn_a1"),("wonespace-m1.webp","wn_s2","wn_a2")]),
]
PHONE = {"carteira360-m1.webp", "wonespace-m1.webp"}

def tabs_html():
    btns = "".join(f'<button role="tab" id="tab-{p["id"]}" aria-controls="pan-{p["id"]}" aria-selected="{"true" if i==0 else "false"}" tabindex="{0 if i==0 else -1}">{p["name"]}</button>'
                   for i, p in enumerate(PROJECTS))
    panels = ""
    for i, p in enumerate(PROJECTS):
        f0 = p["shots"][0]
        thumbs = "".join(
            f'<button type="button" class="thumb{" on" if j==0 else ""}" data-src="{IMG}{f}" data-alt-key="{a}" data-phone="{1 if f in PHONE else 0}" aria-pressed="{"true" if j==0 else "false"}">'
            f'<img src="{IMG}{f}" alt="" loading="lazy" width="160" height="100"><span {ti(s)}>{tx(s)}</span></button>'
            for j, (f, s, a) in enumerate(p["shots"]))
        rows = "".join(f'<div><dt {ti(d)}>{tx(d)}</dt><dd {ti(v)}>{tx(v)}</dd></div>' for d, v in p["rows"])
        panels += f'''
      <div class="panel" role="tabpanel" id="pan-{p["id"]}" aria-labelledby="tab-{p["id"]}"{"" if i==0 else " hidden"}>
        <div class="viewer">
          <div class="browser">
            <div class="bar" aria-hidden="true"><i></i><i></i><i></i><span>{p["name"].lower().replace(" ","")}.app</span></div>
            <button type="button" class="stage{" phone" if f0[0] in PHONE else ""}" data-zoom aria-label="{E(UI['pt']['zoom'])}">
              <img class="main" src="{IMG}{f0[0]}" width="1500" height="938" alt="{tx(f0[2])}" data-i18n-alt="{f0[2]}" loading="lazy">
            </button>
          </div>
          <div class="thumbs" role="group" aria-label="{UI['pt']['screens']}">{thumbs}</div>
        </div>
        <div class="info">
          <p class="ptag{" own" if p["own"] else ""}"><i></i>{tt(p["p"]+"_tag")}</p>
          <h3>{p["name"]}</h3>
          <p class="out" {ti(p["p"]+"_out")}>{tx(p["p"]+"_out")}</p>
          <dl class="spec">{rows}</dl>
        </div>
      </div>'''
    return btns, panels

TAB_BTNS, TAB_PANELS = tabs_html()

CSS = r"""
/* Layout: escura por padrão; herói com fluxo de luz em canvas + navegador de vidro; faixa de números; projetos em abas com galeria;
   segmentos em bento; etapas com trilho que se preenche ao rolar; planos; FAQ; CTA final em bloco menta. */
:root{
  color-scheme:dark;
  --bg:#07090B;--bg-2:#0C0F12;--surface:#11151A;--glass:rgba(255,255,255,.045);--glass-2:rgba(255,255,255,.08);--glass-b:rgba(255,255,255,.10);--rim:rgba(255,255,255,.16);
  --ink:#F2F5F4;--ink-2:#C4CCC9;--muted:#8E9A96;--rule:rgba(255,255,255,.09);
  --accent:#3DDCA8;--accent-2:#1FA67C;--accent-ink:#04130D;--accent-soft:rgba(61,220,168,.12);--own:#F5A86B;
  --shadow:0 10px 40px rgba(0,0,0,.45),inset 0 1px 0 rgba(255,255,255,.08);
  --stream-a:61,220,168;--stream-b:74,170,255;--stream-alpha:1;
  --f-head:"Manrope",system-ui,-apple-system,"Segoe UI",sans-serif;--f-body:"Manrope",system-ui,-apple-system,"Segoe UI",sans-serif;
  --f-serif:"Instrument Serif",Georgia,serif;--f-mono:"JetBrains Mono",ui-monospace,Menlo,monospace;
  --ease:cubic-bezier(.22,1,.36,1);--ease-io:cubic-bezier(.65,0,.35,1);--spring:cubic-bezier(.34,1.56,.64,1);
  --r:14px;--r-lg:22px;
}
:root[data-theme="light"]{
  color-scheme:light;
  --bg:#F4F6F5;--bg-2:#EAEFED;--surface:#FFFFFF;--glass:rgba(255,255,255,.75);--glass-2:#FFFFFF;--glass-b:rgba(12,40,30,.10);--rim:rgba(255,255,255,.9);
  --ink:#0C1210;--ink-2:#334039;--muted:#5A6862;--rule:rgba(12,40,30,.10);
  --accent:#0E7A5C;--accent-2:#0B6650;--accent-ink:#FFFFFF;--accent-soft:rgba(14,122,92,.10);--own:#A3500F;
  --shadow:0 4px 8px rgba(14,60,46,.06),0 16px 32px rgba(14,60,46,.10);
  --stream-a:14,122,92;--stream-b:40,110,190;--stream-alpha:.55;
}
*{box-sizing:border-box}
:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
html{scroll-behavior:smooth;scroll-padding-top:calc(84px + env(safe-area-inset-top,0px))}
body{margin:0;background:var(--bg);color:var(--ink-2);font:400 1rem/1.6 var(--f-body);-webkit-font-smoothing:antialiased;overflow-x:hidden}
@media(min-width:1024px){body{font-size:1.0625rem}}
img{max-width:100%;height:auto;display:block}
[hidden]{display:none!important}
a{color:var(--accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:6px}
h1,h2,h3{font-family:var(--f-head);color:var(--ink);margin:0;text-wrap:balance;letter-spacing:-.02em}
p{margin:0}
.w{max-width:1240px;margin-inline:auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
@media(min-width:768px){.w{padding-left:max(32px,env(safe-area-inset-left,0px));padding-right:max(32px,env(safe-area-inset-right,0px))}}
.skip{position:absolute;left:16px;top:-80px;z-index:60;background:var(--accent);color:var(--accent-ink);padding:12px 16px;border-radius:8px;font-weight:700}
.skip:focus{top:calc(8px + env(safe-area-inset-top,0px))}
.lbl{display:inline-flex;align-items:center;gap:8px;font:500 .74rem/1 var(--f-mono);letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.lbl::before{content:"";width:18px;height:1px;background:currentColor}
.em{font-family:var(--f-serif);font-style:italic;font-weight:400;letter-spacing:0;color:var(--accent)}
.btn{position:relative;display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:0 26px;border-radius:999px;font:700 1rem/1 var(--f-body);text-decoration:none;cursor:pointer;border:1px solid var(--glass-b);background:var(--glass);color:var(--ink);transition:transform .16s var(--ease),background-color .2s var(--ease),border-color .2s var(--ease);-webkit-tap-highlight-color:transparent}
.btn:hover{border-color:var(--accent)}
.btn:active{transform:scale(.96)}
.btn.pri{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.btn.pri:hover{background:var(--accent-2);border-color:var(--accent-2)}
:root:not([data-theme="light"]) .btn.pri:hover{background:#5BE7B9;border-color:#5BE7B9}
.btn .arr{transition:transform .2s var(--ease)}
.btn:hover .arr{transform:translateX(4px)}
.btn.sm{min-height:42px;padding:0 18px;font-size:.92rem}

/* topo */
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:41;background:var(--bg)}
.top{position:fixed;left:0;right:0;top:env(safe-area-inset-top,0px);z-index:40;transition:background-color .3s var(--ease),border-color .3s var(--ease),backdrop-filter .3s}
.top.scrolled{background:color-mix(in srgb,var(--bg) 72%,transparent);backdrop-filter:blur(16px) saturate(140%);-webkit-backdrop-filter:blur(16px) saturate(140%);border-bottom:1px solid var(--rule)}
.top .w{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:72px}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);text-decoration:none;font:800 1.1rem/1 var(--f-head);letter-spacing:-.01em}
.brand svg{width:32px;height:32px}
.top nav{display:flex;align-items:center;gap:22px;font-size:.95rem}
.top nav a.nl{color:var(--ink-2);text-decoration:none;position:relative;padding:8px 0}
.top nav a.nl::after{content:"";position:absolute;left:0;right:0;bottom:2px;height:1px;background:var(--accent);transform:scaleX(0);transform-origin:left;transition:transform .25s var(--ease)}
.top nav a.nl:hover{color:var(--ink)}.top nav a.nl:hover::after{transform:scaleX(1)}
.tools{display:flex;align-items:center;gap:8px}
.seg{position:relative;display:inline-flex;border:1px solid var(--glass-b);border-radius:999px;padding:3px;background:var(--glass)}
.seg .knob{position:absolute;top:3px;bottom:3px;left:3px;width:44px;border-radius:999px;background:var(--ink);transition:transform .3s var(--ease)}
.seg[data-on="en"] .knob{transform:translateX(44px)}
.seg button{position:relative;z-index:1;width:44px;min-height:38px;border:0;border-radius:999px;background:transparent;color:var(--ink-2);font:700 .82rem/1 var(--f-body);cursor:pointer;transition:color .3s var(--ease)}
.seg button[aria-pressed="true"]{color:var(--bg)}
.icon-btn{display:inline-grid;place-items:center;width:44px;height:44px;border-radius:50%;border:1px solid var(--glass-b);background:var(--glass);color:var(--ink);cursor:pointer;transition:transform .16s var(--ease)}
.icon-btn:active{transform:scale(.92)}
.icon-btn svg{width:19px;height:19px;transition:transform .5s var(--spring)}
.icon-btn:hover svg{transform:rotate(-20deg)}
.icon-btn .i-sun{display:none}:root[data-theme="light"] .icon-btn .i-sun{display:block}:root[data-theme="light"] .icon-btn .i-moon{display:none}
@media(max-width:1080px){.top nav a.nl{display:none}}
@media(max-width:600px){.top nav .btn{display:none}.top .w{gap:8px}}

/* herói */
.hero{position:relative;overflow:hidden;padding-top:calc(72px + clamp(40px,6vw,80px));padding-bottom:clamp(56px,7vw,88px);isolation:isolate}
.hero canvas{position:absolute;inset:0;width:100%;height:100%;z-index:-1}
.pause{position:absolute;right:max(16px,env(safe-area-inset-right,0px));bottom:16px;z-index:2;width:36px;height:36px;border-radius:50%;display:grid;place-items:center;border:1px solid var(--glass-b);background:var(--glass);color:var(--ink-2);cursor:pointer;backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.pause svg{width:14px;height:14px}.pause .pl{display:none}.pause[aria-pressed="true"] .pl{display:block}.pause[aria-pressed="true"] .pa{display:none}
.hero::after{content:"";position:absolute;inset:auto 0 0;height:160px;background:linear-gradient(transparent,var(--bg));z-index:-1;pointer-events:none}
.hero-grid{display:grid;grid-template-columns:minmax(0,1.12fr) minmax(0,1fr);gap:clamp(32px,5vw,64px);align-items:center}
@media(max-width:980px){.hero-grid{grid-template-columns:1fr}}
.badge{display:inline-flex;align-items:center;gap:10px;padding:7px 14px 7px 8px;border-radius:999px;border:1px solid var(--glass-b);background:var(--glass);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);font-size:.85rem;color:var(--ink)}
.badge .dot{position:relative;width:8px;height:8px;border-radius:50%;background:var(--accent)}
.badge .dot::after{content:"";position:absolute;inset:-4px;border-radius:50%;border:1px solid var(--accent);opacity:0;animation:ping 2.4s var(--ease) infinite}
@keyframes ping{0%{transform:scale(.6);opacity:.9}80%,100%{transform:scale(1.8);opacity:0}}
.hero h1{margin-top:24px;font-size:clamp(2.5rem,1.2rem + 4vw,4.7rem);line-height:.98;font-weight:500;letter-spacing:-.045em}
.hero h1 .ln{display:block;overflow:hidden;padding-bottom:.08em;margin-bottom:-.08em}
.hero h1 .ln>span{display:inline-block}
.hero h1 .em{font-size:1.08em;letter-spacing:-.01em}
.hero .sub{margin-top:26px;max-width:44ch;font-size:clamp(1.05rem,1rem + .3vw,1.2rem);color:var(--ink-2)}
.hero .acts{margin-top:34px;display:flex;flex-wrap:wrap;gap:12px}
.js .hero h1 .ln>span{transform:translateY(105%);animation:rise .7s var(--ease) forwards}
.js .hero h1 .ln:nth-child(2)>span{animation-delay:.08s}.js .hero h1 .ln:nth-child(3)>span{animation-delay:.16s}
.js .hero .fade-in{opacity:0;transform:translateY(12px);animation:fadeup .7s var(--ease) forwards}
.js .hero .d1{animation-delay:.3s}.js .hero .d2{animation-delay:.42s}.js .hero .d3{animation-delay:.5s}
@keyframes rise{to{transform:none}}
@keyframes fadeup{to{opacity:1;transform:none}}
/* navegador de vidro */
.scene{perspective:1400px}
.browser{position:relative;border-radius:var(--r-lg);border:1px solid var(--glass-b);background:var(--glass);backdrop-filter:blur(20px) saturate(140%);-webkit-backdrop-filter:blur(20px) saturate(140%);box-shadow:var(--shadow);overflow:hidden}
.browser .bar{display:flex;align-items:center;gap:6px;height:36px;padding:0 14px;border-bottom:1px solid var(--rule);font:500 .72rem/1 var(--f-mono);color:var(--muted)}
.browser .bar i{width:10px;height:10px;border-radius:50%;background:var(--glass-2);border:1px solid var(--glass-b)}
.browser .bar span{margin-left:10px;padding:5px 10px;border-radius:6px;background:var(--glass)}
.hero .browser{transform-style:preserve-3d;transition:transform .5s var(--ease)}
.js .hero .browser{opacity:0;animation:frame 1.1s var(--ease) .25s forwards}
@keyframes frame{from{opacity:0;transform:translateY(40px) rotateX(14deg) scale(.96)}to{opacity:1;transform:none}}
.hero .browser img{width:100%;aspect-ratio:1500/938;object-fit:cover;object-position:top left}
.glare{position:absolute;inset:0;pointer-events:none;background:radial-gradient(420px circle at var(--gx,50%) var(--gy,0%),rgba(255,255,255,.16),transparent 60%);opacity:0;transition:opacity .3s var(--ease)}
.scene:hover .glare{opacity:1}
.float{position:absolute;display:flex;align-items:center;gap:12px;padding:12px 16px;border-radius:16px;border:1px solid var(--glass-b);background:color-mix(in srgb,var(--surface) 70%,transparent);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);box-shadow:var(--shadow);font-size:.82rem;color:var(--muted);line-height:1.3}
.float b{display:block;font:700 1.2rem/1.1 var(--f-head);color:var(--ink);font-variant-numeric:tabular-nums}
.float .ic{width:34px;height:34px;border-radius:10px;display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);flex:none}
.float .ic svg{width:18px;height:18px}
.fA{left:-28px;bottom:-26px;animation:bob 6s var(--ease-io) infinite}
.fB{right:-18px;top:28%;animation:bob 7s var(--ease-io) -2s infinite}
@keyframes bob{50%{transform:translateY(-10px)}}
.hero-visual{position:relative}
@media(min-width:1100px){.hero .scene{width:124%}.fB{right:-22%}}
@media(max-width:980px){.fA{left:8px}.fB{right:8px}}
@media(max-width:560px){.float{display:none}}

/* números */
.metrics{position:relative;border-block:1px solid var(--rule);background:linear-gradient(180deg,var(--bg),var(--bg-2))}
.metrics .w{display:grid;grid-template-columns:repeat(4,minmax(0,1fr))}
.metric{padding:clamp(28px,4vw,44px) 24px;display:grid;gap:10px;align-content:start;border-left:1px solid var(--rule)}
.metric:first-child{border-left:0;padding-left:0}
.metric .n{font:300 clamp(1.9rem,1.1rem + 3.4vw,4.4rem)/1 var(--f-head);letter-spacing:-.04em;color:var(--ink);font-variant-numeric:tabular-nums;white-space:nowrap}
.metric .n .u{color:var(--accent)}
.metric p{font-size:.92rem;max-width:26ch}
.meter{height:4px;border-radius:4px;background:var(--glass-2);overflow:hidden;margin-top:6px;max-width:220px}
.meter i{display:block;height:100%;width:100%;background:linear-gradient(90deg,var(--accent-2),var(--accent));transform-origin:left;transform:scaleX(0);transition:transform 1.4s var(--ease)}
.metric.in .meter i{transform:scaleX(var(--v,1))}
@media(max-width:900px){.metrics .w{grid-template-columns:repeat(2,minmax(0,1fr))}.metric:nth-child(3){border-left:0;padding-left:0}.metric:nth-child(n+3){border-top:1px solid var(--rule)}}
@media(max-width:560px){.metric{padding:22px 14px}.metric:nth-child(odd){padding-left:0}.metric p{font-size:.85rem}.meter{display:none}}
@media(max-width:330px){.metrics .w{grid-template-columns:1fr}.metric{border-left:0!important;padding-left:0!important}.metric+.metric{border-top:1px solid var(--rule)}}

/* seções */
section{position:relative;padding-block:clamp(64px,8vw,104px)}
.sh{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:16px 48px;align-items:end;margin-bottom:clamp(32px,4vw,48px)}
.sh h2{margin-top:14px;font-size:clamp(2rem,1.4rem + 2.4vw,3.4rem);line-height:1.04;font-weight:500;letter-spacing:-.035em}
.sh p{max-width:46ch;color:var(--ink-2)}
@media(max-width:860px){.sh{grid-template-columns:1fr;align-items:start}}
.js .rv{opacity:0;transform:translateY(8px);transition:opacity .5s var(--ease),transform .5s var(--ease)}
.js .rv.in{opacity:1;transform:none}

/* projetos */
#projetos{background:radial-gradient(60% 50% at 80% 0%,var(--accent-soft),transparent 70%)}
.tablist{position:relative;display:inline-flex;gap:4px;padding:5px;border-radius:999px;border:1px solid var(--glass-b);background:var(--glass);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);max-width:100%;overflow-x:auto;scrollbar-width:none}
.tablist::-webkit-scrollbar{display:none}
.tablist .pill{position:absolute;top:5px;bottom:5px;left:0;border-radius:999px;background:var(--accent);transition:transform .25s var(--ease),width .25s var(--ease);z-index:0}
.tablist button{position:relative;z-index:1;flex:none;min-height:44px;padding:0 20px;border:0;border-radius:999px;background:transparent;color:var(--ink-2);font:700 .95rem/1 var(--f-body);cursor:pointer;white-space:nowrap;transition:color .25s var(--ease)}
.tablist button:hover{color:var(--ink)}
.tablist button[aria-selected="true"]{color:var(--accent-ink)}
.panels{margin-top:28px}
.panel{display:grid;grid-template-columns:minmax(0,1.55fr) minmax(0,1fr);gap:clamp(24px,4vw,56px);align-items:start}
@media(max-width:980px){.panel{grid-template-columns:1fr}}
.panel.enter{animation:panelIn .35s var(--ease)}
@keyframes panelIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.viewer{min-width:0}
.stage{display:block;width:100%;padding:0;border:0;background:var(--bg-2);cursor:zoom-in;position:relative;aspect-ratio:1500/938;overflow:hidden}
.stage img{width:100%;height:100%;object-fit:cover;object-position:top left;transition:opacity .25s var(--ease),transform .6s var(--ease)}
.stage:hover img{transform:scale(1.015)}
.stage.phone img{object-fit:contain;object-position:center;padding:14px 0}
.stage.swap img{opacity:0}
.thumbs{margin-top:14px;display:flex;gap:10px;overflow-x:auto;padding-bottom:4px;scrollbar-width:thin;-webkit-mask:linear-gradient(90deg,#000 calc(100% - 24px),transparent);mask:linear-gradient(90deg,#000 calc(100% - 24px),transparent)}
.thumb{flex:none;display:grid;gap:6px;width:150px;padding:6px 6px 8px;border-radius:12px;border:1px solid var(--glass-b);background:var(--glass);color:var(--muted);font:600 .78rem/1.2 var(--f-body);text-align:left;cursor:pointer;transition:border-color .2s var(--ease),color .2s var(--ease),transform .16s var(--ease)}
.thumb img{width:100%;aspect-ratio:16/10;object-fit:cover;object-position:top left;border-radius:7px;background:var(--bg-2)}
.thumb:hover{color:var(--ink)}
.thumb:active{transform:scale(.97)}
.thumb.on{border-color:var(--accent);color:var(--ink)}
.info{display:grid;gap:14px;align-content:start}
.ptag{display:inline-flex;align-items:center;gap:8px;font:500 .74rem/1.3 var(--f-mono);letter-spacing:.07em;text-transform:uppercase;color:var(--accent)}
.ptag i{width:7px;height:7px;border-radius:50%;background:currentColor}
.ptag.own{color:var(--own)}
.info h3{font-size:clamp(1.8rem,1.4rem + 1.4vw,2.6rem);font-weight:600;letter-spacing:-.03em}
.info .out{font-size:1.12rem;color:var(--ink);line-height:1.45}
.spec{margin:6px 0 0;display:grid;border-top:1px solid var(--rule)}
.spec div{display:grid;grid-template-columns:6.5rem minmax(0,1fr);gap:14px;padding:13px 0;border-bottom:1px solid var(--rule);font-size:.94rem}
.spec dt{font:500 .72rem/1.9 var(--f-mono);letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.spec dd{margin:0}
@media(max-width:420px){.spec div{grid-template-columns:1fr;gap:2px}}
.hint{margin-top:10px;font:500 .72rem/1 var(--f-mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}

/* lightbox */
.lb{position:fixed;inset:0;z-index:80;display:grid;place-items:center;padding:calc(56px + env(safe-area-inset-top,0px)) max(16px,env(safe-area-inset-right,0px)) calc(24px + env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px));background:rgba(3,5,6,.86);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);opacity:0;transition:opacity .25s var(--ease)}
.lb.on{opacity:1}
.lb figure{margin:0;display:grid;gap:12px;justify-items:center;max-width:min(1400px,100%);transform:scale(.96);transition:transform .35s var(--ease)}
.lb.on figure{transform:none}
.lb img{max-width:100%;max-height:calc(100vh - 160px);width:auto;height:auto;border-radius:12px;box-shadow:0 30px 80px -20px rgba(0,0,0,.8);background:#fff}
.lb figcaption{color:#DDE5E2;font-size:.92rem;text-align:center;max-width:70ch}
.lb-x{position:absolute;top:calc(12px + env(safe-area-inset-top,0px));right:max(12px,env(safe-area-inset-right,0px));width:48px;height:48px;border-radius:50%;border:1px solid rgba(255,255,255,.3);background:rgba(255,255,255,.08);color:#fff;font:400 26px/1 var(--f-body);cursor:pointer}

/* segmentos (bento) */
.bento{display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:16px}
@media(max-width:900px){.bento{grid-template-columns:1fr}}
.cell{position:relative;overflow:hidden;border-radius:var(--r-lg);border:1px solid var(--glass-b);background:var(--glass);padding:clamp(24px,3vw,32px);display:grid;gap:10px;align-content:start;min-height:220px;transition:border-color .25s var(--ease),transform .3s var(--ease)}
.cell::before{content:"";position:absolute;inset:0;background:radial-gradient(300px circle at var(--mx,80%) var(--my,0%),var(--accent-soft),transparent 70%);opacity:.0;transition:opacity .3s var(--ease);pointer-events:none}
.cell:hover{border-color:color-mix(in srgb,var(--accent) 50%,transparent)}
.cell:hover::before{opacity:1}
.cell.main{background:linear-gradient(160deg,color-mix(in srgb,var(--accent) 22%,var(--surface)),var(--surface) 70%);border-color:color-mix(in srgb,var(--accent) 35%,transparent)}
.cell .k{font:500 .72rem/1 var(--f-mono);letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.cell h3{font-size:clamp(1.4rem,1.2rem + .8vw,1.8rem);font-weight:600}
.cell p{font-size:.95rem}
.cell .ico{width:44px;height:44px;border-radius:12px;display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);margin-bottom:8px}
.cell .ico svg{width:22px;height:22px}

/* etapas com trilho */
.steps{position:relative;list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px}
.steps .rail{position:absolute;left:0;right:0;top:27px;height:2px;background:var(--rule);overflow:hidden}
.steps .rail i{display:block;height:100%;background:linear-gradient(90deg,var(--accent-2),var(--accent));transform-origin:left;transform:scaleX(var(--p,1))}
.steps li{position:relative;display:grid;gap:10px;align-content:start}
.steps .num{position:relative;z-index:1;width:56px;height:56px;border-radius:50%;display:grid;place-items:center;font:600 1.15rem/1 var(--f-head);color:var(--muted);background:var(--bg);border:1px solid var(--glass-b);transition:color .3s var(--ease),border-color .3s var(--ease),background-color .3s var(--ease),box-shadow .3s var(--ease)}
.steps li.on .num{color:var(--accent-ink);background:var(--accent);border-color:var(--accent)}
.steps h3{font-size:1.3rem;margin-top:8px}
.steps p{font-size:.95rem}
@media(max-width:900px){.steps{grid-template-columns:1fr 1fr}.steps .rail{display:none}}
@media(max-width:520px){.steps{grid-template-columns:1fr}}

/* fundador */
.founder{display:grid;grid-template-columns:auto minmax(0,1fr);gap:clamp(24px,4vw,48px);align-items:center;border-radius:var(--r-lg);border:1px solid var(--glass-b);background:var(--glass);padding:clamp(24px,4vw,44px)}
@media(max-width:700px){.founder{grid-template-columns:1fr}}
.av{width:120px;height:120px;border-radius:50%;display:grid;place-items:center;font:300 2.6rem/1 var(--f-head);letter-spacing:-.03em;color:var(--accent);background:radial-gradient(circle at 30% 25%,var(--accent-soft),transparent 70%),var(--bg-2);border:1px solid var(--glass-b)}
.founder h3{font-size:clamp(1.6rem,1.3rem + 1vw,2.2rem);font-weight:600}
.founder .role{color:var(--accent);margin-top:6px;font-size:.95rem}
.founder p.bio{margin-top:16px;max-width:62ch}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}
.chips span{font:500 .78rem/1 var(--f-mono);padding:9px 12px;border-radius:999px;border:1px solid var(--glass-b);color:var(--ink)}

/* planos */
.plans{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;align-items:stretch}
@media(max-width:960px){.plans{grid-template-columns:1fr}}
.plan{position:relative;display:flex;flex-direction:column;gap:14px;border-radius:var(--r-lg);border:1px solid var(--glass-b);background:var(--glass);padding:28px;transition:transform .3s var(--ease),border-color .25s var(--ease)}
.plan:hover{transform:translateY(-4px)}
.plan.hl{background:linear-gradient(180deg,color-mix(in srgb,var(--accent) 16%,var(--surface)),var(--surface));border-color:var(--accent)}
@media(min-width:961px){.plan.hl{transform:translateY(-12px)}.plan.hl:hover{transform:translateY(-16px)}}
.plan .flag{align-self:flex-start;font:600 .72rem/1 var(--f-mono);letter-spacing:.07em;text-transform:uppercase;background:var(--accent);color:var(--accent-ink);padding:7px 10px;border-radius:999px}
.plan h3{font-size:1.6rem;font-weight:600}
.plan .for{color:var(--muted);font-size:.95rem}
.plan .price{font:600 1.5rem/1.1 var(--f-head);color:var(--ink)}
.plan .price small{display:block;font:400 .82rem/1.4 var(--f-body);color:var(--muted);margin-top:4px}
.plan ul{list-style:none;margin:0;padding:0;display:grid;gap:10px;font-size:.95rem;flex:1}
.plan li{padding-left:28px;position:relative}
.plan li::before{content:"";position:absolute;left:2px;top:.42em;width:13px;height:7px;border-left:2px solid var(--accent);border-bottom:2px solid var(--accent);transform:rotate(-45deg)}
.plan .btn{width:100%}
.pl-note{margin-top:22px;font-size:.92rem;color:var(--muted);max-width:70ch}

/* FAQ */
.faq{max-width:860px;display:grid;gap:10px}
.qa{border-radius:16px;border:1px solid var(--glass-b);background:var(--glass);transition:border-color .25s var(--ease)}
.qa.open{border-color:color-mix(in srgb,var(--accent) 45%,transparent)}
.qa button{width:100%;display:flex;justify-content:space-between;align-items:center;gap:16px;min-height:64px;padding:16px 20px;border:0;background:transparent;color:var(--ink);font:600 1.05rem/1.35 var(--f-head);text-align:left;cursor:pointer}
.qa .chev{flex:none;width:32px;height:32px;border-radius:50%;display:grid;place-items:center;border:1px solid var(--glass-b);transition:transform .35s var(--ease),background-color .25s var(--ease)}
.qa.open .chev{transform:rotate(180deg);background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.qa .chev svg{width:14px;height:14px}
.qa .body{display:grid;grid-template-rows:0fr;transition:grid-template-rows .35s var(--ease)}
.qa.open .body{grid-template-rows:1fr}
.qa .body>div{overflow:hidden;opacity:0;transition:opacity .3s var(--ease)}
.qa.open .body>div{opacity:1}
.qa .body p{padding:0 20px 20px;max-width:66ch}

/* CTA final */
.final{padding-block:clamp(64px,8vw,104px)}
.cta-card{position:relative;overflow:hidden;border-radius:28px;padding:clamp(32px,6vw,72px);background:var(--accent);color:var(--accent-ink)}
.cta-card::before{content:"";position:absolute;inset:-40% -10% auto auto;width:70%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.35),transparent 65%);pointer-events:none}
.cta-card .lbl{color:var(--accent-ink)}
.cta-card h2{margin-top:16px;color:var(--accent-ink);font-size:clamp(2.2rem,1.4rem + 3.4vw,4.4rem);line-height:1;font-weight:500;letter-spacing:-.04em;max-width:16ch}
.cta-card h2 .em{color:var(--accent-ink)}
.cta-card p.l{margin-top:20px;max-width:48ch;font-size:1.1rem;opacity:.85}
.cta-card h2+.crow{margin-top:28px}
.crow{position:relative;display:flex;flex-wrap:wrap;align-items:center;gap:12px 16px;padding:16px 0;border-top:1px solid color-mix(in srgb,var(--accent-ink) 22%,transparent);max-width:760px}
.crow .ic{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;border:1px solid color-mix(in srgb,var(--accent-ink) 30%,transparent);flex:none}
.crow .ic svg{width:20px;height:20px}
.crow code{flex:1;min-width:0;font:600 clamp(1rem,.9rem + .6vw,1.35rem)/1.2 var(--f-mono);user-select:all;-webkit-user-select:all;overflow-wrap:anywhere}
.crow .lnk{flex:1;min-width:0;display:flex;justify-content:space-between;gap:12px;align-items:center;min-height:44px;color:var(--accent-ink);text-decoration:none;font:600 clamp(1rem,.9rem + .5vw,1.25rem)/1.3 var(--f-body);overflow-wrap:anywhere}
.crow .lnk:hover{text-decoration:underline}
@media(max-width:600px){.crow code{flex-basis:calc(100% - 60px)}.crow #copy{margin-left:60px}}
.faqwrap{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.4fr);gap:24px 56px;align-items:start}
.faqwrap .sh{position:sticky;top:110px;grid-template-columns:1fr;margin:0}
@media(max-width:900px){.faqwrap{grid-template-columns:1fr}.faqwrap .sh{position:static}}
.mailrow{margin-top:32px;display:flex;flex-wrap:wrap;align-items:center;gap:12px}
.mailbox{display:flex;align-items:center;gap:6px;flex-wrap:wrap;padding:6px 6px 6px 20px;border-radius:999px;background:rgba(0,0,0,.14);max-width:100%}
.mailbox code{font:600 clamp(.98rem,.9rem + .5vw,1.2rem)/1.2 var(--f-mono);user-select:all;-webkit-user-select:all;overflow-wrap:anywhere;min-width:0}
.cta-card .btn{border-color:transparent}
.cta-card .btn.dark{background:var(--accent-ink);color:var(--accent)}
:root[data-theme="light"] .cta-card .btn.dark{color:var(--accent)}
.cta-card .btn.ghost{background:transparent;color:var(--accent-ink);border-color:color-mix(in srgb,var(--accent-ink) 35%,transparent)}
.ok-mark{width:18px;height:18px;display:none}
.copied .ok-mark{display:block}
.copied .ok-mark circle{stroke-dasharray:57;stroke-dashoffset:57;animation:draw .28s var(--ease) forwards}
.copied .ok-mark path{stroke-dasharray:14;stroke-dashoffset:14;animation:draw .19s var(--ease) .28s forwards}
@keyframes draw{to{stroke-dashoffset:0}}
.status{min-height:1.4em;margin-top:12px;font-weight:600}

footer{padding-block:28px 40px;font-size:.9rem;color:var(--muted)}
footer .w{display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px 24px}

@media(prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;animation-delay:0s!important;transition-duration:.01ms!important}
  .js .hero h1 .ln>span,.js .hero .fade-in,.js .hero .browser,.js .rv{opacity:1!important;transform:none!important}
  .fA,.fB,.badge .dot::after{animation:none!important}
}
@media(prefers-reduced-transparency:reduce){.browser,.badge,.float,.tablist,.top.scrolled{backdrop-filter:none;-webkit-backdrop-filter:none;background:var(--surface)}}
"""

def plan(i, items, hl):
    lis = "".join(f"<li {ti(k)}>{tx(k)}</li>" for k in items)
    flag = f'<span class="flag" {ti("flag")}>{tx("flag")}</span>' if hl else ""
    return (f'<article class="plan rv{" hl" if hl else ""}">{flag}<h3 {ti(f"p{i}h")}>{tx(f"p{i}h")}</h3><p class="for" {ti(f"p{i}f")}>{tx(f"p{i}f")}</p>'
            f'<p class="price"><span {ti("price")}>{tx("price")}</span><small {ti("price_s")}>{tx("price_s")}</small></p><ul>{lis}</ul>'
            f'<a class="btn {"pri" if hl else ""}" href="#contato" {ti("cta")}>{tx("cta")}</a></article>')

CHEV = '<svg viewBox="0 0 14 14" aria-hidden="true"><path d="M3 5l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
FAQ = "".join(f'<div class="qa rv"><button type="button" aria-expanded="false" aria-controls="qa{i}" id="qb{i}"><span {ti(f"q{i}")}>{tx(f"q{i}")}</span><span class="chev">{CHEV}</span></button>'
              f'<div class="body" id="qa{i}" role="region" aria-labelledby="qb{i}"><div><p {ti(f"a{i}")}>{tx(f"a{i}")}</p></div></div></div>' for i in range(1, 10))

ICONS = {
 "g1": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19V9M10 19V5M16 19v-7M22 19H2" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
 "g2": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
 "g3": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="3.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M5 20c1-3.6 3.8-5.5 7-5.5s6 1.9 7 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
}
SUN = '<svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2" fill="currentColor"/><g stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/></g></svg>'
MOON = '<svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z" fill="currentColor"/></svg>'
LOGO = '<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#0F2A21"/><path d="M8.5 22.5v-4.5h5v4.5M13.5 18v-5h5v5M18.5 13V8h5v5" fill="none" stroke="#3DDCA8" stroke-width="2" stroke-linejoin="round"/></svg>'

EN = {k: v[1] for k, v in T.items()}
faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": T[f"q{i}"][0], "acceptedAnswer": {"@type": "Answer", "text": T[f"a{i}"][0]}} for i in range(1, 8)]}, ensure_ascii=False)
org_ld = json.dumps({"@context": "https://schema.org", "@type": "Organization", "name": "RG AI Ltda", "url": "https://gruberia.com/", "email": "rafael@gruberia.com",
    "founder": {"@type": "Person", "name": "Rafael Gruber Bernstein"}, "sameAs": ["https://www.linkedin.com/in/rafaelgruberbernstein"]}, ensure_ascii=False)

HEAD_JS = r"""(function(){var r=document.documentElement;r.classList.add('js');try{var th=localStorage.getItem('rgai-theme3');if(th==='light')r.setAttribute('data-theme','light');var l=localStorage.getItem('rgai-lang');if(l==='en'||l==='pt')r.setAttribute('data-lang',l)}catch(e){}if(!r.getAttribute('data-lang')){r.setAttribute('data-lang',/^pt/i.test(navigator.language||'pt')?'pt':'en')}})();"""

BODY_JS = r"""(function(){
var r=document.documentElement,EN=__EN__,UI=__UI__,PT={},lang='pt';
var RM=matchMedia('(prefers-reduced-motion: reduce)');
/* ---------- idioma ---------- */
var nodes=[].slice.call(document.querySelectorAll('[data-i18n]')),alts=[].slice.call(document.querySelectorAll('[data-i18n-alt]'));
nodes.forEach(function(n){PT[n.getAttribute('data-i18n')]=n.textContent});
alts.forEach(function(n){PT[n.getAttribute('data-i18n-alt')]=n.alt});
[].forEach.call(document.querySelectorAll('[data-alt-key]'),function(b){var k=b.getAttribute('data-alt-key');if(PT[k]==null)PT[k]=__PTALT__[k]});
var md=document.querySelector('meta[name=description]');PT.title=document.title;PT.desc=md.content;
function D(){return lang==='en'?EN:PT}
function setLang(l,save){lang=l;var d=D();
 nodes.forEach(function(n){var k=n.getAttribute('data-i18n');if(d[k]!=null)n.textContent=d[k]});
 alts.forEach(function(n){var k=n.getAttribute('data-i18n-alt');if(d[k]!=null)n.alt=d[k]});
 document.title=d.title;md.content=d.desc;r.lang=l==='en'?'en':'pt-BR';r.setAttribute('data-lang',l);
 var sg=document.getElementById('langgrp');sg.setAttribute('data-on',l);sg.setAttribute('aria-label',UI[l].lang);
 [].forEach.call(sg.querySelectorAll('button'),function(b){b.setAttribute('aria-pressed',b.getAttribute('data-setlang')===l?'true':'false')});
 [].forEach.call(document.querySelectorAll('[data-zoom]'),function(b){b.setAttribute('aria-label',UI[l].zoom)});
 [].forEach.call(document.querySelectorAll('.thumbs'),function(b){b.setAttribute('aria-label',UI[l].screens)});
 document.querySelector('.tablist').setAttribute('aria-label',UI[l].projects);
 if(save){try{localStorage.setItem('rgai-lang',l)}catch(e){}}paint();movePill(false);if(window.__s)__s.label()}
[].forEach.call(document.querySelectorAll('[data-setlang]'),function(b){b.addEventListener('click',function(){setLang(b.getAttribute('data-setlang'),true)})});
/* ---------- tema (escuro por padrão) ---------- */
var tb=document.getElementById('theme');
function cur(){return r.getAttribute('data-theme')==='light'?'light':'dark'}
function paint(){tb.setAttribute('aria-label',cur()==='dark'?UI[lang].toLight:UI[lang].toDark)}
tb.addEventListener('click',function(){var n=cur()==='dark'?'light':'dark';if(n==='light')r.setAttribute('data-theme','light');else r.removeAttribute('data-theme');try{localStorage.setItem('rgai-theme3',n)}catch(e){}paint();stream.recolor()});
/* ---------- topo ---------- */
var top=document.querySelector('.top');function onScroll(){top.classList.toggle('scrolled',scrollY>12)}addEventListener('scroll',onScroll,{passive:true});onScroll();
/* ---------- fluxo de luz (canvas) ---------- */
var stream=window.__s=(function(){var c=document.getElementById('stream'),x=c.getContext('2d'),w=0,h=0,dpr=1,t=0,run=false,raf=0,ca,cb,al;
 function recolor(){var s=getComputedStyle(r);ca=s.getPropertyValue('--stream-a').trim();cb=s.getPropertyValue('--stream-b').trim();al=parseFloat(s.getPropertyValue('--stream-alpha'))||1;if(!run)draw()}
 function size(){dpr=Math.min(devicePixelRatio||1,1.5);w=c.clientWidth;h=c.clientHeight;c.width=w*dpr;c.height=h*dpr;x.setTransform(dpr,0,0,dpr,0,0);draw()}
 function draw(){x.clearRect(0,0,w,h);x.globalCompositeOperation=cur()==='dark'?'lighter':'source-over';
  var N=w<700?22:38,cx=w*(w<980?.5:.62),cy=h*.52;
  for(var i=0;i<N;i++){var k=i/N,ph=t*.00022+k*2.2;
   x.beginPath();
   for(var s=0;s<=60;s++){var u=s/60,px=-w*.1+u*w*1.25,
     bend=Math.sin(u*3.1+ph)*h*.14*(1-k*.4)+Math.cos(u*1.7-ph*1.3)*h*.08,
     py=cy+(u-.55)*(u-.55)*h*1.6*(k-.5)+bend+(k-.5)*h*.18;
     if(s===0)x.moveTo(px,py);else x.lineTo(px,py)}
   var g=x.createLinearGradient(0,0,w,0);var a=(.05+.22*Math.pow(Math.sin(k*Math.PI),2))*al;
   g.addColorStop(0,'rgba('+cb+',0)');g.addColorStop(.35,'rgba('+cb+','+(a*.6)+')');g.addColorStop(.65,'rgba('+ca+','+a+')');g.addColorStop(1,'rgba('+ca+',0)');
   x.strokeStyle=g;x.lineWidth=k>.45&&k<.55?1.6:1;x.stroke()}
  var rg=x.createRadialGradient(cx,cy,0,cx,cy,Math.max(w,h)*.45);rg.addColorStop(0,'rgba('+ca+','+(.16*al)+')');rg.addColorStop(1,'rgba('+ca+',0)');
  x.globalCompositeOperation='source-over';x.fillStyle=rg;x.fillRect(0,0,w,h)}
 function loop(ts){t=ts;draw();raf=requestAnimationFrame(loop)}
 var paused=false;
 function start(){if(run||RM.matches||paused)return;run=true;raf=requestAnimationFrame(loop)}
 function stop(){run=false;cancelAnimationFrame(raf)}
 addEventListener('resize',size);
 var io=new IntersectionObserver(function(e){e[0].isIntersecting?start():stop()});io.observe(c);
 document.addEventListener('visibilitychange',function(){document.hidden?stop():start()});
 recolor();size();
 var pb=document.getElementById('pause');if(RM.matches)pb.hidden=true;
 pb.addEventListener('click',function(){paused=!paused;pb.setAttribute('aria-pressed',paused?'true':'false');pb.setAttribute('aria-label',paused?UI[lang].play:UI[lang].pause);paused?stop():start()});
 return {recolor:recolor,label:function(){pb.setAttribute('aria-label',paused?UI[lang].play:UI[lang].pause)}}})();
/* ---------- inclinação 3D do navegador ---------- */
var fine=matchMedia('(hover:hover) and (pointer:fine)');
[].forEach.call(document.querySelectorAll('.scene'),function(sc){var b=sc.querySelector('.browser'),gl=sc.querySelector('.glare');
 sc.addEventListener('pointermove',function(e){if(!fine.matches||RM.matches)return;var rc=sc.getBoundingClientRect(),px=(e.clientX-rc.left)/rc.width,py=(e.clientY-rc.top)/rc.height;
  b.style.transition='transform .12s linear';b.style.transform='rotateY('+((px-.5)*10)+'deg) rotateX('+((.5-py)*8)+'deg)';gl.style.setProperty('--gx',px*100+'%');gl.style.setProperty('--gy',py*100+'%')});
 sc.addEventListener('pointerleave',function(){b.style.transition='transform .5s var(--ease)';b.style.transform=''})});
/* ---------- brilho que segue o cursor nos cartões ---------- */
[].forEach.call(document.querySelectorAll('.cell'),function(c){c.addEventListener('pointermove',function(e){var rc=c.getBoundingClientRect();c.style.setProperty('--mx',(e.clientX-rc.left)+'px');c.style.setProperty('--my',(e.clientY-rc.top)+'px')})});
/* ---------- revelação ao rolar + números ---------- */
function countUp(el){var to=parseFloat(el.getAttribute('data-to')),pre=el.getAttribute('data-pre')||'',suf=el.getAttribute('data-suf')||'',sp=el.querySelector('.v');
 if(RM.matches){sp.textContent=pre+to;return}var t0=null,dur=1400;
 function f(ts){if(!t0)t0=ts;var p=Math.min(1,(ts-t0)/dur),e=1-Math.pow(1-p,4);sp.textContent=pre+Math.round(to*e);if(p<1)requestAnimationFrame(f)}requestAnimationFrame(f)}
var seen=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;var el=e.target;el.classList.add('in');
 [].forEach.call(el.querySelectorAll('[data-to]'),countUp);seen.unobserve(el)})},{rootMargin:'0px 0px -8% 0px'});
[].forEach.call(document.querySelectorAll('.rv,.metric'),function(el){var rc=el.getBoundingClientRect();if(rc.top<innerHeight*.92){el.classList.add('in');[].forEach.call(el.querySelectorAll('[data-to]'),countUp)}else seen.observe(el)});
/* ---------- abas de projeto ---------- */
var tl=document.querySelector('.tablist'),pill=tl.querySelector('.pill'),tabs=[].slice.call(tl.querySelectorAll('[role=tab]'));
function movePill(anim){var on=tl.querySelector('[aria-selected=true]');if(!on)return;if(!anim)pill.style.transition='none';
 pill.style.width=on.offsetWidth+'px';pill.style.transform='translateX('+on.offsetLeft+'px)';if(!anim){pill.offsetWidth;pill.style.transition=''}}
function selectTab(t,focus){tabs.forEach(function(b){var on=b===t;b.setAttribute('aria-selected',on?'true':'false');b.tabIndex=on?0:-1;var p=document.getElementById(b.getAttribute('aria-controls'));
 if(on&&p.hidden){p.hidden=false;p.classList.remove('enter');p.offsetWidth;p.classList.add('enter');[].forEach.call(p.querySelectorAll('img[loading=lazy]'),function(i){i.loading='eager'})}else if(!on)p.hidden=true});
 movePill(true);if(focus)t.focus();t.scrollIntoView({block:'nearest',inline:'nearest'})}
tabs.forEach(function(b,i){b.addEventListener('click',function(){selectTab(b)});b.addEventListener('keydown',function(e){var n=null;
 if(e.key==='ArrowRight')n=tabs[(i+1)%tabs.length];else if(e.key==='ArrowLeft')n=tabs[(i-1+tabs.length)%tabs.length];else if(e.key==='Home')n=tabs[0];else if(e.key==='End')n=tabs[tabs.length-1];
 if(n){e.preventDefault();selectTab(n,true)}})});
addEventListener('resize',function(){movePill(false)});
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(function(){movePill(false)});
/* ---------- galeria ---------- */
[].forEach.call(document.querySelectorAll('.panel'),function(p){var st=p.querySelector('.stage'),im=st.querySelector('img');
 [].forEach.call(p.querySelectorAll('.thumb'),function(th){th.addEventListener('click',function(){if(th.classList.contains('on'))return;
  [].forEach.call(p.querySelectorAll('.thumb'),function(o){o.classList.toggle('on',o===th);o.setAttribute('aria-pressed',o===th?'true':'false')});
  var k=th.getAttribute('data-alt-key');st.classList.add('swap');
  setTimeout(function(){im.src=th.getAttribute('data-src');im.setAttribute('data-i18n-alt',k);im.alt=D()[k];st.classList.toggle('phone',th.getAttribute('data-phone')==='1');
   var done=function(){st.classList.remove('swap')};if(im.complete)requestAnimationFrame(done);else im.onload=done},RM.matches?0:180)})})});
/* ---------- lightbox ---------- */
var last=null;
function closeLb(lb){lb.classList.remove('on');document.body.style.overflow='';setTimeout(function(){lb.remove()},250);if(last)last.focus()}
[].forEach.call(document.querySelectorAll('[data-zoom]'),function(b){b.addEventListener('click',function(){last=b;var im=b.querySelector('img');
 var lb=document.createElement('div');lb.className='lb';lb.setAttribute('role','dialog');lb.setAttribute('aria-modal','true');lb.setAttribute('aria-label',im.alt);
 lb.innerHTML='<button type="button" class="lb-x"></button><figure><img alt=""><figcaption></figcaption></figure>';
 var x=lb.querySelector('.lb-x');x.textContent='×';x.setAttribute('aria-label',UI[lang].close);lb.querySelector('img').src=im.src;lb.querySelector('img').alt=im.alt;lb.querySelector('figcaption').textContent=im.alt;
 lb.addEventListener('click',function(e){if(e.target===lb||e.target===x||e.target.tagName==='IMG')closeLb(lb)});
 lb.addEventListener('keydown',function(e){if(e.key==='Escape'){e.preventDefault();closeLb(lb)}if(e.key==='Tab'){e.preventDefault();x.focus()}});
 document.body.appendChild(lb);document.body.style.overflow='hidden';requestAnimationFrame(function(){lb.classList.add('on')});x.focus()})});
/* ---------- FAQ ---------- */
[].forEach.call(document.querySelectorAll('.qa button'),function(b){b.addEventListener('click',function(){var q=b.parentNode,o=!q.classList.contains('open');q.classList.toggle('open',o);b.setAttribute('aria-expanded',o?'true':'false')})});
/* ---------- etapas: trilho que se preenche ao rolar (GSAP ScrollTrigger quando disponível) ---------- */
var steps=document.querySelector('.steps'),items=[].slice.call(steps.querySelectorAll('li'));
function setP(p){steps.style.setProperty('--p',p.toFixed(3));items.forEach(function(li,i){li.classList.toggle('on',p>=(i/(items.length-1))-.001)})}
if(window.gsap&&window.ScrollTrigger&&!RM.matches){gsap.registerPlugin(ScrollTrigger);
 ScrollTrigger.create({trigger:steps,start:'top 75%',end:'bottom 45%',scrub:.6,onUpdate:function(s){setP(s.progress)}});setP(0)}
else setP(1);
/* ---------- copiar e-mail ---------- */
var cb=document.getElementById('copy'),st=document.getElementById('status'),ml=document.getElementById('mail');
function sel(){try{var x=document.createRange();x.selectNodeContents(ml);var s=getSelection();s.removeAllRanges();s.addRange(x)}catch(z){}}
cb.addEventListener('click',function(){var t=ml.textContent.trim();function ok(){cb.classList.add('copied');st.textContent=UI[lang].copied;setTimeout(function(){cb.classList.remove('copied');st.textContent=''},2600)}function no(){sel();st.textContent=UI[lang].sel}
 try{navigator.clipboard.writeText(t).then(ok,no)}catch(z){no()}});
setLang(r.getAttribute('data-lang')==='en'?'en':'pt',false);
})();"""

PTALT = {}
for p in PROJECTS:
    for f, s, a in p["shots"]:
        PTALT[a] = T[a][0]
BODY_JS = BODY_JS.replace("__EN__", json.dumps(EN, ensure_ascii=False)).replace("__UI__", json.dumps(UI, ensure_ascii=False)).replace("__PTALT__", json.dumps(PTALT, ensure_ascii=False))

FONTS = "family=Instrument+Serif:ital@1&family=JetBrains+Mono:wght@500&family=Manrope:wght@300;400;500;600;700;800"

head_meta = f"""<title>{tx('title')}</title>
<meta name="description" content="{tx('desc')}">
<meta name="theme-color" content="#07090B">
<meta property="og:title" content="{tx('title')}">
<meta property="og:description" content="{tx('desc')}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:locale:alternate" content="en_US">
<meta property="og:image" content="https://gruberia.com/portfolio/img/riskai-1.webp">
<script type="application/ld+json">{org_ld}</script>
<script type="application/ld+json">{faq_ld}</script>
<script>{HEAD_JS}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{FONTS}&display=swap">
<link rel="preload" as="image" href="{IMG}riskai-1.webp" fetchpriority="high">
<style>{CSS}</style>"""

metrics = f"""
<div class="metrics">
  <div class="w">
    <div class="metric"><span class="n" data-to="3" aria-label="3"><span class="v" aria-hidden="true">3</span></span><p {ti('m1')}>{tx('m1')}</p><div class="meter" aria-hidden="true"><i style="--v:.75"></i></div></div>
    <div class="metric"><span class="n" data-to="200" data-pre="+" aria-label="+200%"><span class="v" aria-hidden="true">+200</span><span class="u" aria-hidden="true">%</span></span><p {ti('m2')}>{tx('m2')}</p><div class="meter" aria-hidden="true"><i style="--v:1"></i></div></div>
    <div class="metric"><span class="n" data-to="14" aria-label="14"><span class="v" aria-hidden="true">14</span></span><p {ti('m3')}>{tx('m3')}</p><div class="meter" aria-hidden="true"><i style="--v:.6"></i></div></div>
    <div class="metric"><span class="n"><span {ti('m4v')}>{tx('m4v')}</span></span><p {ti('m4')}>{tx('m4')}</p><div class="meter" aria-hidden="true"><i style="--v:.4"></i></div></div>
  </div>
</div>"""

body = f"""<a class="skip" href="#conteudo" {ti('skip')}>{tx('skip')}</a>
<header class="top">
  <div class="w">
    <a class="brand" href="#conteudo">{LOGO}RG AI</a>
    <nav aria-label="Seções">
      <a class="nl" href="#projetos" {ti('nav_proj')}>{tx('nav_proj')}</a>
      <a class="nl" href="#como-funciona" {ti('nav_como')}>{tx('nav_como')}</a>
      <a class="nl" href="#duvidas" {ti('nav_faq')}>{tx('nav_faq')}</a>
      <div class="tools">
        <div class="seg" role="group" id="langgrp" aria-label="Idioma" data-on="pt"><span class="knob" aria-hidden="true"></span><button type="button" data-setlang="pt" aria-pressed="true" lang="pt-BR">PT</button><button type="button" data-setlang="en" aria-pressed="false" lang="en">EN</button></div>
        <button class="icon-btn" id="theme" type="button" aria-label="Mudar para o tema claro">{MOON}{SUN}</button>
      </div>
      <a class="btn pri sm" href="#contato" {ti('cta')}>{tx('cta')}</a>
    </nav>
  </div>
</header>
<main id="conteudo">
  <div class="hero">
    <canvas id="stream" aria-hidden="true"></canvas>
    <button type="button" class="pause" id="pause" aria-pressed="false" aria-label="Pausar animação"><svg class="pa" viewBox="0 0 14 14" aria-hidden="true"><path d="M4 2.5v9M10 2.5v9" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><svg class="pl" viewBox="0 0 14 14" aria-hidden="true"><path d="M4 2.5l8 4.5-8 4.5z" fill="currentColor"/></svg></button>
    <div class="w hero-grid">
      <div>
        <p class="badge fade-in d1"><span class="dot" aria-hidden="true"></span><span {ti('badge')}>{tx('badge')}</span></p>
        <h1><span class="ln"><span {ti('h1a')}>{tx('h1a')}</span></span><span class="ln"><span {ti('h1b')}>{tx('h1b')}</span></span><span class="ln"><span class="em" {ti('h1c')}>{tx('h1c')}</span></span></h1>
        <p class="sub fade-in d2" {ti('sub')}>{tx('sub')}</p>
        <div class="acts fade-in d3"><a class="btn pri" href="#contato"><span {ti('cta')}>{tx('cta')}</span><span class="arr" aria-hidden="true">→</span></a><a class="btn" href="#projetos" {ti('see')}>{tx('see')}</a></div>
      </div>
      <div class="hero-visual">
        <div class="scene">
          <div class="browser">
            <div class="bar" aria-hidden="true"><i></i><i></i><i></i><span>riskai.app</span></div>
            <img src="{IMG}riskai-1.webp" width="1500" height="938" alt="{tx('frame_alt')}" data-i18n-alt="frame_alt" fetchpriority="high">
            <div class="glare" aria-hidden="true"></div>
          </div>
        </div>
        <div class="float fA" aria-hidden="true"><span class="ic"><svg viewBox="0 0 24 24"><path d="M4 12.5l5 5L20 6.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span><b {ti('fl1')}>{tx('fl1')}</b><span {ti('fl1b')}>{tx('fl1b')}</span></span></div>
        <div class="float fB" aria-hidden="true"><span class="ic"><svg viewBox="0 0 24 24"><path d="M4 17l6-6 4 4 6-7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span><b>+200%</b><span {ti('fl2')}>{tx('fl2')}</span></span></div>
      </div>
    </div>
  </div>
{metrics}
  <section id="projetos" aria-labelledby="h-proj">
    <div class="w">
      <div class="sh rv"><div><p class="lbl" {ti('proj_k')}>{tx('proj_k')}</p><h2 id="h-proj"><span {ti('proj_h')}>{tx('proj_h')}</span></h2></div><p {ti('proj_p')}>{tx('proj_p')}</p></div>
      <div class="tablist" role="tablist" aria-label="Projetos"><span class="pill" aria-hidden="true"></span>{TAB_BTNS}</div>
      <div class="panels">{TAB_PANELS}</div>
      <p class="hint" {ti('lb_hint')}>{tx('lb_hint')}</p>
    </div>
  </section>

  <section id="segmentos" aria-labelledby="h-seg">
    <div class="w">
      <div class="sh rv"><div><p class="lbl" {ti('seg_k')}>{tx('seg_k')}</p><h2 id="h-seg" {ti('seg_h')}>{tx('seg_h')}</h2></div></div>
      <div class="bento">{''.join(f'<article class="cell rv{" main" if i==1 else ""}"><span class="ico">{ICONS[f"g{i}"]}</span><p class="k" {ti(f"g{i}k")}>{tx(f"g{i}k")}</p><h3 {ti(f"g{i}h")}>{tx(f"g{i}h")}</h3><p {ti(f"g{i}p")}>{tx(f"g{i}p")}</p></article>' for i in range(1,4))}</div>
    </div>
  </section>

  <section id="como-funciona" aria-labelledby="h-como">
    <div class="w">
      <div class="sh rv"><div><p class="lbl" {ti('como_k')}>{tx('como_k')}</p><h2 id="h-como" {ti('como_h')}>{tx('como_h')}</h2></div></div>
      <ol class="steps"><span class="rail" aria-hidden="true"><i></i></span>{''.join(f'<li><span class="num" aria-hidden="true">{i}</span><h3 {ti(f"st{i}h")}>{tx(f"st{i}h")}</h3><p {ti(f"st{i}")}>{tx(f"st{i}")}</p></li>' for i in range(1,5))}</ol>
    </div>
  </section>

  <section id="fundador" aria-labelledby="h-fd">
    <div class="w">
      <div class="founder rv">
        <div class="av" aria-hidden="true">RG</div>
        <div><p class="lbl" {ti('fd_k')}>{tx('fd_k')}</p><h3 id="h-fd" style="margin-top:12px">Rafael Gruber Bernstein</h3><p class="role" {ti('fd_role')}>{tx('fd_role')}</p><p class="bio" {ti('fd_p')}>{tx('fd_p')}</p>
          <div class="chips"><span {ti('fd_c1')}>{tx('fd_c1')}</span><span {ti('fd_c2')}>{tx('fd_c2')}</span><span {ti('fd_c3')}>{tx('fd_c3')}</span></div></div>
      </div>
    </div>
  </section>

  <section id="duvidas" aria-labelledby="h-faq">
    <div class="w">
      <div class="faqwrap"><div class="sh rv"><div><p class="lbl" {ti('faq_k')}>{tx('faq_k')}</p><h2 id="h-faq" {ti('faq_h')}>{tx('faq_h')}</h2></div></div>
      <div class="faq">{FAQ}</div></div>
    </div>
  </section>

  <section class="final" id="contato" aria-labelledby="h-final">
    <div class="w">
      <div class="cta-card rv">
        <h2 id="h-final" {ti('fin_k')}>{tx('fin_k')}</h2>
        <div class="crow"><span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M3.5 6.5l8.5 6 8.5-6" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></span><code id="mail">rafael@gruberia.com</code><button class="btn dark" id="copy" type="button"><svg class="ok-mark" viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M6 10.5l2.8 2.6L14 7.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span {ti('copy')}>{tx('copy')}</span></button></div>
        <div class="crow"><span class="ic" aria-hidden="true"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="3" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8 10.5v6M8 7.5v.01M11.5 16.5v-3.2c0-1.6 1-2.8 2.4-2.8s2.1 1 2.1 2.6v3.4M11.5 10.5v6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span><a class="lnk" href="https://www.linkedin.com/in/rafaelgruberbernstein" target="_blank" rel="noopener">linkedin.com/in/rafaelgruberbernstein <span aria-hidden="true">↗</span></a></div>
        <p class="status" id="status" role="status" aria-live="polite"></p>
      </div>
    </div>
  </section>
</main>
<footer><div class="w"><span {ti('foot1')}>{tx('foot1')}</span><span {ti('foot2')}>{tx('foot2')}</span></div></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>{BODY_JS}</script>"""

if ARTIFACT:
    doc = head_meta.replace("<title>", '<meta name="claude:viewport-fit-sides" content="cover">\n<title>', 1) + "\n" + body + "\n"
else:
    doc = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<link rel="canonical" href="https://gruberia.com/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
{head_meta}
</head>
<body>
{body}
</body>
</html>
"""
open(OUT, "w", encoding="utf-8").write(doc)
print("ok", OUT, len(doc))
