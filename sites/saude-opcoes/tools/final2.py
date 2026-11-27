#!/usr/bin/env python3
"""Landing geral da RG AI (apps sob medida) — visual da opção 4, tema claro/escuro e PT/EN.
Uso: final2.py <saida.html> [--artifact]"""
import sys, os, json, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gerar as G

OUT = sys.argv[1]
ARTIFACT = "--artifact" in sys.argv
E = lambda s: html.escape(s, quote=True)

T = {
 "title": ("RG AI · Apps sob medida", "RG AI · Custom apps"),
 "desc": ("Apps web de dados e IA sob medida, do requisito à produção. Especialidade em crédito e finanças; também saúde e agências de marca pessoal.",
          "Custom data and AI web apps, from requirements to production. Specialized in credit and finance; also healthcare and personal-brand agencies."),
 "skip": ("Pular para o conteúdo", "Skip to content"),
 "nav_apps": ("Apps", "Apps"), "nav_como": ("Como funciona", "How it works"), "nav_planos": ("Planos", "Plans"), "nav_faq": ("Dúvidas", "FAQ"),
 "cta": ("Agendar uma conversa", "Book a call"),
 "kicker": ("Apps sob medida · dados e IA", "Custom apps · data and AI"),
 "h1a": ("Apps sob medida, do requisito à", "Custom apps, from requirements to"),
 "h1b": ("produção.", "production."),
 "sub": ("Construímos o app que a sua operação precisa e cuidamos dele depois do deploy. Três já estão em produção, em uso diário.",
         "We build the app your operation needs and look after it once it's live. Three are already in production, in daily use."),
 "fine": ("Resposta por e-mail, sem compromisso.", "We reply by email, no commitment."),
 "deck_note": ("Telas reais com dados fictícios", "Real screens with fictional data"),
 "prova_k": ("Prova social", "Track record"), "prova_h": ("O que já está no ar", "What's already live"),
 "s1b": ("3 apps", "3 apps"), "s1": ("em produção, construídos do requisito ao deploy", "in production, built from requirements to deploy"),
 "s2b": ("mar/2026", "Mar 2026"), "s2": ("no ar desde então, em uso diário", "live since then, in daily use"),
 "s3b": ("+200%", "+200%"), "s3": ("de produtividade em prospecção e gestão de carteira", "productivity in prospecting and portfolio management"),
 "s4b": ("INPI", "Trademark"), "s4": ("registramos a marca do seu app", "we register your app's brand with the INPI (Brazil)"),
 "apps_k": ("Apps que fizemos", "Apps we built"),
 "apps_h": ("Quatro apps, três em produção", "Four apps, three in production"),
 "apps_p": ("As telas são da versão de demonstração, com nomes e valores fictícios. Nenhum cliente é identificado.",
            "Screens come from the demo version, with fictional names and figures. No client is identified."),
 "more": ("Ver no portfólio", "See in portfolio"),
 "a1t": ("Em produção · comitê de crédito", "In production · credit committee"),
 "a1o": ("Leitura de risco e deterioração da carteira por cedente e grupo econômico, para o comitê decidir limites e a continuidade da relação.",
         "Risk and portfolio-deterioration reading by client and economic group, so the credit committee can set limits and decide on each relationship."),
 "a1x": ("Retreino diário que só publica modelos aprovados na validação.", "Daily retraining that only publishes models that pass validation."),
 "a1alt": ("RiskAI FIDC: resumo da carteira com grupos por faixa de risco.", "RiskAI FIDC: portfolio summary with groups by risk band."),
 "a2t": ("Em produção · área comercial", "In production · sales"),
 "a2o": ("Prospecção com pesquisa de IA auditada: um modelo confere o outro, e afirmação sem fonte verificável fica marcada como indeterminada.",
         "Prospecting with audited AI research: one model checks the other, and any claim without a verifiable source is flagged as undetermined."),
 "a2x": ("Integrado ao CRM: funil, agenda e distribuição de leads.", "Integrated with the CRM: pipeline, schedule and lead distribution."),
 "a2alt": ("LeadScout: ficha do lead com nota, parecer e fontes.", "LeadScout: lead profile with score, assessment and sources."),
 "a3t": ("Em produção · gestão de carteira", "In production · portfolio management"),
 "a3o": ("Agenda, rotas de visita e alerta de cliente que parou de operar, com visões para gestor, gerente e celular em campo.",
         "Schedules, visit routes and alerts when a client stops operating, with views for managers, account managers and phones in the field."),
 "a3x": ("Junto com o LeadScout, +200% de produtividade.", "Together with LeadScout, +200% productivity."),
 "a3alt": ("Carteira360: rota de visitas do dia no mapa.", "Carteira360: today's visit route on a map."),
 "a4t": ("Produto próprio · em construção", "Our own product · in development"),
 "a4o": ("App para agências que cuidam da marca pessoal de médicos. Agência e médico trabalham no mesmo dado, em tempo real.",
         "An app for agencies that manage doctors' personal brands. Agency and doctor work on the same data, in real time."),
 "a4x": ("Demonstração completa ao vivo, com acordo de confidencialidade.", "Full demo live, under a confidentiality agreement."),
 "a4alt": ("Wonespace: painel da agência e app do médico lado a lado.", "Wonespace: agency dashboard and doctor's app side by side."),
 "seg_k": ("Para quem", "Who it's for"), "seg_h": ("Onde já sabemos trabalhar", "Where we already know the ground"),
 "g1k": ("Especialidade", "Specialty"), "g1h": ("Crédito e finanças", "Credit and finance"),
 "g1p": ("Risco, prospecção, gestão de carteira e relatórios para fundos de recebíveis, financeiras e times comerciais.",
         "Risk, prospecting, portfolio management and reporting for receivables funds, lenders and sales teams."),
 "g2k": ("Também", "Also"), "g2h": ("Saúde", "Healthcare"),
 "g2p": ("Back-office de clínicas: autorizações, guias de convênio, agenda e fila, com dado de saúde tratado como sensível.",
         "Clinic back-office: authorizations, insurance claims, scheduling and queues, with health data treated as sensitive."),
 "g3k": ("Também", "Also"), "g3h": ("Agências de marca pessoal", "Personal-brand agencies"),
 "g3p": ("Produção, aprovação e mensagens entre agência e cliente no mesmo app. Foi daí que nasceu a Wonespace.",
         "Production, approvals and messages between agency and client in one app. That's where Wonespace came from."),
 "como_k": ("Como funciona", "How it works"), "como_h": ("Quatro etapas, da conversa ao app no ar", "Four steps, from first call to a live app"),
 "st1h": ("Conversa", "Call"), "st1": ("Você conta onde o processo trava hoje. Saímos com o problema escrito.", "You tell us where the process gets stuck today. We leave with the problem written down."),
 "st2h": ("Protótipo", "Prototype"), "st2": ("Você vê e clica nas telas principais antes da construção, com estimativa de prazo e custo.", "You see and click through the main screens before we build, with a time and cost estimate."),
 "st3h": ("Construção", "Build"), "st3": ("Construímos em ciclos curtos. A cada entrega, a sua equipe testa e opina.", "We build in short cycles. At each delivery, your team tests and gives feedback."),
 "st4h": ("Operação", "Operation"), "st4": ("Colocamos no ar, treinamos a equipe e cuidamos de hospedagem, backups e ajustes.", "We go live, train your team and take care of hosting, backups and adjustments."),
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
 "faq_k": ("Dúvidas", "FAQ"), "faq_h": ("Perguntas frequentes", "Frequently asked questions"),
 "q1": ("Que tipo de app vocês fazem?", "What kind of apps do you build?"),
 "a1": ("Aplicações web de dados e IA sob medida: painéis de risco, prospecção e CRM, gestão de carteira, agenda e operação. A especialidade é crédito e finanças; também atendemos saúde e agências de marca pessoal.",
        "Custom data and AI web apps: risk dashboards, prospecting and CRM, portfolio management, scheduling and operations. Our specialty is credit and finance; we also serve healthcare and personal-brand agencies."),
 "q2": ("Quanto custa?", "How much does it cost?"),
 "a2": ("Depende do escopo. O Diagnóstico existe para isso: ao final, você recebe por escrito o prazo e o valor do Projeto e da Operação.",
        "It depends on scope. That's what the Assessment is for: at the end, you get the time and price of the Project and Operation in writing."),
 "q3": ("Quanto tempo leva?", "How long does it take?"),
 "a3": ("Depende do tamanho do app. Você recebe a estimativa junto com o protótipo, antes de decidir construir.", "It depends on the size of the app. You get the estimate with the prototype, before deciding to build."),
 "q4": ("Como vocês usam IA?", "How do you use AI?"),
 "a4": ("Quando ela ajuda. Comparamos modelos por acurácia, custo e desempenho, escrevemos o critério de aprovação antes de ver o resultado, e um modelo que não passa não vai para a tela.",
        "Where it helps. We compare models on accuracy, cost and performance, write the approval criterion before seeing results, and a model that fails doesn't reach the screen."),
 "q5": ("Como vocês cuidam dos dados?", "How do you handle data?"),
 "a5": ("Acesso por papéis, senhas com hash, conexão criptografada, backups e monitoramento. Em saúde, todo dado clínico é tratado como dado sensível, como manda a LGPD.",
        "Role-based access, hashed passwords, encrypted connections, backups and monitoring. In healthcare, all clinical data is treated as sensitive data, as Brazil's LGPD requires."),
 "q6": ("Funciona no celular?", "Does it work on phones?"),
 "a6": ("Sim. Os apps são web e funcionam no navegador do computador e do celular, sem instalar nada.", "Yes. Our apps run in the browser on desktop and phone, with nothing to install."),
 "q7": ("Vocês registram a marca do app?", "Do you register the app's brand?"),
 "a7": ("Sim. No plano Projeto, registramos a marca do seu app no INPI.", "Yes. In the Project plan, we register your app's brand with the INPI, Brazil's trademark office."),
 "fd_k": ("Apresentação", "About"),
 "fd_role": ("Fundador · Product Owner · Engenheiro mecânico (PUC-Rio e Technion)", "Founder · Product Owner · Mechanical engineer (PUC-Rio and Technion)"),
 "fd_p1": ("Há mais de três anos levo produtos de dados e IA do conceito à produção. Na Radix, como Product Owner, coloquei em produção dois produtos de IA de visão computacional.",
           "For more than three years I've taken data and AI products from concept to production. At Radix, as Product Owner, I shipped two computer-vision AI products."),
 "fd_p2": ("Desde março de 2026, a RG AI constrói apps sob medida. Os três apps de crédito desta página estão em produção e em uso diário.",
           "Since March 2026, RG AI has built custom apps. The three credit apps on this page are in production and in daily use."),
 "fd_c1": ("Product Owner certificado (CSPO)", "Certified Product Owner (CSPO)"),
 "fd_c2": ("Inglês fluente", "Fluent English"),
 "row_mail": ("E-mail", "Email"), "row_li": ("LinkedIn", "LinkedIn"),
 "fin_k": ("Contato", "Contact"), "fin_h": ("Vamos conversar sobre o seu app.", "Let's talk about your app."),
 "fin_p": ("Mande um e-mail contando qual processo você quer tirar da planilha. Respondemos com um horário para conversar.",
           "Send us an email about the process you want to get out of spreadsheets. We'll reply with a time to talk."),
 "copy": ("Copiar e-mail", "Copy email"),
 "foot1": ("RG AI Ltda · Rafael Gruber Bernstein", "RG AI Ltda · Rafael Gruber Bernstein"),
 "foot2": ("Telas de demonstração com dados fictícios. Sem promessa de resultado.", "Demo screens with fictional data. No promised results."),
 "foot_p": ("Portfólio", "Portfolio"),
}
UI = {"pt": {"copied": "E-mail copiado.", "sel": "E-mail selecionado. Use Ctrl+C ou Cmd+C para copiar.", "toLight": "Mudar para o tema claro", "toDark": "Mudar para o tema escuro", "lang": "Idioma"},
      "en": {"copied": "Email copied.", "sel": "Email selected. Press Ctrl+C or Cmd+C to copy.", "toLight": "Switch to light theme", "toDark": "Switch to dark theme", "lang": "Language"}}

def tx(k): return E(T[k][0])
def ti(k): return f'data-i18n="{k}"'

LIGHT = """--bg:#F5F6F7;--alt:#FFFFFF;--surface:#FFFFFF;--ink-2:#2E3338;--muted:#59626A;--head:#101214;--rule:#DDE1E4;--rule-strong:#B5BCC2;
--link:#0B6E52;--focus:#0B6E52;--kicker:#0B6E52;--cta:#0E7A5C;--cta-h:#0B6650;--cta-ink:#FFFFFF;
--top-bg:#F5F6F7;--top-ink:#101214;--top-rule:#DDE1E4;--hero-bg:#F5F6F7;--hero-ink:#2E3338;--hero-head:#101214;--hero-kicker:#0B6E52;
--mk-bg:#FFFFFF;--mk-ink:#2E3338;--mk-head:#101214;--mk-muted:#59626A;--mk-rule:#E4E7EA;--mk-shadow:0 1px 2px rgba(16,18,20,.06),0 20px 44px -20px rgba(14,122,92,.30);
--chip-bg:#EEF0F2;--chip-ink:#2E3338;--ok-bg:#DDF3EA;--ok-ink:#0B5A43;--warn-bg:#FFF1D1;--warn-ink:#5C4400;--bad-bg:#FBE3E1;--bad-ink:#8A1C12;
--stat-line:1px solid #0E7A5C;--step-bg:#FFFFFF;--step-border:1px solid #DDE1E4;--num-bg:#DDF3EA;--num-ink:#0B5A43;--check:#0E7A5C;
--final-bg:#101214;--final-ink:#C9CED3;--final-head:#FFFFFF;--final-kicker:#5FD3B0;--final-cta:#2FB58F;--final-cta-ink:#04130E;--final-rule:#3A3D42;
--foot-bg:#F5F6F7;--foot-ink:#59626A;--cta-shadow:none;--plan-shadow:0 18px 40px -20px rgba(14,122,92,.30);
--shot-shadow:0 1px 2px rgba(16,18,20,.06),0 18px 40px -18px rgba(14,60,46,.32);--accent-em:#0E7A5C;--tag:#0B6E52;--own:#9A4A12;color-scheme:light;"""

CSS = f"""
:root{{--cta-shadow:none;--f-serif:"Instrument Serif",Georgia,serif;--f-mono:"JetBrains Mono",ui-monospace,Menlo,monospace;--f-label:"JetBrains Mono",ui-monospace,Menlo,monospace;
--shot-shadow:0 0 0 1px rgba(47,181,143,.10),0 24px 60px -26px rgba(47,181,143,.45);--accent-em:#5FD3B0;--tag:#5FD3B0;--own:#F2A66B}}
@media (prefers-color-scheme:light){{:root:not([data-theme="dark"]){{{LIGHT}}}}}
:root[data-theme="light"]{{{LIGHT}}}
.kicker{{font-weight:500;font-size:.74rem;letter-spacing:.09em}}
.hero h1 .em{{font-family:var(--f-serif);font-style:italic;font-weight:400;color:var(--accent-em);letter-spacing:0}}
.hero h1{{max-width:15ch}}
.final{{border-top:1px solid var(--rule)}}
/* topo */
.tools{{display:flex;align-items:center;gap:8px}}
.seg{{display:inline-flex;border:1px solid var(--rule-strong);border-radius:999px;padding:2px}}
.seg button{{min-width:44px;min-height:40px;border:0;border-radius:999px;background:transparent;color:var(--top-ink);font:600 .85rem/1 var(--f-body);cursor:pointer}}
.seg button[aria-pressed="true"]{{background:var(--top-ink);color:var(--top-bg)}}
.icon-btn{{display:inline-grid;place-items:center;width:44px;height:44px;border-radius:50%;border:1px solid var(--rule-strong);background:transparent;color:var(--top-ink);cursor:pointer}}
.icon-btn svg{{width:20px;height:20px}}
.icon-btn .i-sun{{display:none}}.is-dark .icon-btn .i-sun{{display:block}}.is-dark .icon-btn .i-moon{{display:none}}
.top nav{{gap:20px}}
@media(max-width:1100px){{.top nav a.nl{{display:none}}}}
@media(max-width:600px){{.top .w{{gap:8px}}.top nav .btn{{display:none}}}}
/* maço de telas reais (único momento animado) */
.deck{{position:relative;aspect-ratio:1500/1150}}
.deck figure{{position:absolute;margin:0;width:80%;aspect-ratio:1500/938;border-radius:12px;overflow:hidden;border:1px solid var(--rule);background:var(--surface);box-shadow:var(--shot-shadow)}}
.deck img{{width:100%;height:100%;object-fit:cover;object-position:top left}}
.deck .d1{{left:0;top:0}}.deck .d2{{left:10%;top:16%}}.deck .d3{{left:20%;top:32%}}
.deck figcaption{{position:absolute;right:10px;top:10px;font:500 .7rem/1 var(--f-mono);letter-spacing:.05em;text-transform:uppercase;background:var(--surface);color:var(--head);border:1px solid var(--rule);padding:6px 8px;border-radius:6px}}
.deck-note{{margin-top:12px;font:500 .72rem/1.3 var(--f-mono);letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}}
@media(prefers-reduced-motion:no-preference){{
 .deck figure{{animation:fan .7s cubic-bezier(.2,.7,.2,1) both}}
 .deck .d1{{animation-delay:.05s}}.deck .d2{{animation-delay:.14s}}.deck .d3{{animation-delay:.23s}}
 @keyframes fan{{from{{transform:translate(16%,10%);opacity:0}}to{{transform:none;opacity:1}}}}
 .hero .mockup{{animation:none}}
}}
/* apps */
.apps{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}}
@media(max-width:860px){{.apps{{grid-template-columns:1fr}}}}
.app{{display:grid;grid-template-rows:auto 1fr;background:var(--surface);border:1px solid var(--rule);border-radius:var(--r-card);overflow:hidden;min-width:0;color:inherit;text-decoration:none;transition:border-color .15s ease}}
.app:hover{{border-color:var(--cta)}}
.app .shot{{aspect-ratio:1500/860;overflow:hidden;border-bottom:1px solid var(--rule);background:var(--bg)}}
.app .shot img{{width:100%;height:100%;object-fit:cover;object-position:top left;transition:transform .35s ease}}
@media(prefers-reduced-motion:no-preference){{.app:hover .shot img{{transform:scale(1.02)}}}}
.app .txt{{padding:24px;display:flex;flex-direction:column;gap:10px}}
.app .tag{{display:inline-flex;align-items:center;gap:8px;font:500 .72rem/1.3 var(--f-mono);letter-spacing:.06em;text-transform:uppercase;color:var(--tag)}}
.app .tag i{{width:7px;height:7px;border-radius:50%;background:currentColor;flex:none}}
.app .tag.own{{color:var(--own)}}
.app h3{{font-size:1.5rem}}
.app p{{font-size:.95em}}
.app .x{{color:var(--muted);font-size:.9em}}
.app .more{{margin-top:auto;padding-top:6px;font-weight:600;color:var(--link);font-size:.95rem}}
.apps-note{{margin-top:20px;font-size:.9rem;color:var(--muted);max-width:70ch}}
/* segmentos */
.segs{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}}
@media(max-width:900px){{.segs{{grid-template-columns:1fr}}}}
.segs article{{border-top:1px solid var(--rule-strong);padding-top:20px;display:grid;gap:8px;align-content:start}}
.segs article.main{{border-top:2px solid var(--cta)}}
.segs h3{{font-size:1.35rem}}
.segs p{{font-size:.95em}}
"""

CSS2 = r"""
/* inspiração: pílulas, vidro e brilho */
:root{--glass:rgba(255,255,255,.035);--glass-b:rgba(255,255,255,.09);--glow:rgba(47,181,143,.16);--line:rgba(95,211,176,.22)}
@media (prefers-color-scheme:light){:root:not([data-theme="dark"]){--glass:#FFFFFF;--glass-b:#DDE1E4;--glow:rgba(14,122,92,.10);--line:rgba(14,122,92,.18)}}
:root[data-theme="light"]{--glass:#FFFFFF;--glass-b:#DDE1E4;--glow:rgba(14,122,92,.10);--line:rgba(14,122,92,.18)}
.kicker{display:inline-flex;align-items:center;gap:8px;padding:6px 12px;border:1px solid var(--glass-b);border-radius:999px;background:var(--glass)}
.kicker::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--kicker);flex:none}
.final .kicker{border-color:var(--final-rule);background:transparent}
.hero{position:relative;overflow:hidden;background:radial-gradient(55% 60% at 78% 35%,var(--glow),transparent 70%),var(--hero-bg)}
.hero .w{position:relative;z-index:1}
.hero .rays{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.hero .rays path{fill:none;stroke:var(--line);stroke-width:1}
.stat{background:var(--glass);border:1px solid var(--glass-b);border-top:1px solid var(--glass-b);border-radius:16px;padding:24px}
.stat b{color:var(--accent-em)}
.app,.plan,.steps li,.case{background:var(--glass);border-color:var(--glass-b)}
.plan.hl{border-color:var(--cta)}
/* fundador */
.founder{display:grid;grid-template-columns:auto minmax(0,1fr);gap:clamp(24px,4vw,48px);align-items:start;background:var(--glass);border:1px solid var(--glass-b);border-radius:20px;padding:clamp(24px,4vw,48px)}
@media(max-width:700px){.founder{grid-template-columns:1fr}}
.mono-av{width:112px;height:112px;border-radius:50%;display:grid;place-items:center;font:300 2.4rem/1 var(--f-head);letter-spacing:-.02em;color:var(--accent-em);background:radial-gradient(circle at 35% 30%,var(--glow),transparent 70%),var(--bg);border:1px solid var(--glass-b);box-shadow:0 0 0 6px var(--glass)}
.founder h3{font-size:clamp(1.5rem,1.2rem + 1vw,1.95rem)}
.founder .role{color:var(--tag);font-size:.95rem;margin-top:6px}
.founder .bio{display:grid;gap:14px;margin-top:20px;max-width:62ch}
.founder .chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px}
.founder .chips span{font:500 .8rem/1 var(--f-mono);padding:8px 12px;border-radius:999px;border:1px solid var(--glass-b);color:var(--head)}
/* contato em cartão com linhas */
.contact-card{margin-top:32px;max-width:720px;border:1px solid var(--final-rule);border-radius:20px;background:rgba(255,255,255,.03);padding:8px 24px}
.crow{display:flex;flex-wrap:wrap;align-items:center;gap:12px 16px;padding:16px 0;border-top:1px solid var(--final-rule)}
.crow:first-child{border-top:0}
.crow .ic{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;border:1px solid var(--final-rule);color:var(--final-kicker);flex:none}
.crow .ic svg{width:18px;height:18px}
.crow .lbl{font:500 .72rem/1 var(--f-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--final-kicker);width:100%;display:none}
.crow .val{flex:1;min-width:0}
.crow a.val{color:var(--final-head);text-decoration:none;font-size:1.05rem;display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:44px}
.crow a.val:hover{text-decoration:underline}
.crow .arrow{color:var(--final-kicker);flex:none}
.crow a.val span:first-child{min-width:0;overflow-wrap:anywhere}
.final code.val{font-size:clamp(1rem,.9rem + .6vw,1.3rem);overflow-wrap:anywhere}
footer a{display:inline-flex;align-items:center;min-height:28px}
"""

def img(src, k, extra=""):
    return f'<img src="{src}" width="1500" height="938" alt="{E(T[k][0])}" data-i18n-alt="{k}" {extra}>'

DECK = f"""<div class="deck">
  <figure class="d1">{img("portfolio/img/leadscout-2.webp","a2alt",'fetchpriority="high"')}<figcaption>LeadScout</figcaption></figure>
  <figure class="d2">{img("portfolio/img/carteira360-3.webp","a3alt",'fetchpriority="high"')}<figcaption>Carteira360</figcaption></figure>
  <figure class="d3">{img("portfolio/img/riskai-1.webp","a1alt",'fetchpriority="high"')}<figcaption>RiskAI FIDC</figcaption></figure>
</div>
<p class="deck-note" {ti('deck_note')}>{tx('deck_note')}</p>"""

LAZY = 'loading="lazy"'
def app(n, name, src, anchor, own=False):
    return (f'<a class="app" href="portfolio/{"index.html" if ARTIFACT else ""}#{anchor}"><div class="shot">{img(src, f"a{n}alt", LAZY)}</div>'
            f'<div class="txt"><p class="tag{" own" if own else ""}"><i></i><span {ti(f"a{n}t")}>{tx(f"a{n}t")}</span></p><h3>{name}</h3>'
            f'<p {ti(f"a{n}o")}>{tx(f"a{n}o")}</p><p class="x" {ti(f"a{n}x")}>{tx(f"a{n}x")}</p><span class="more"><span {ti("more")}>{tx("more")}</span> →</span></div></a>')

def plan(i, items, hl):
    lis = "".join(f"<li {ti(k)}>{tx(k)}</li>" for k in items)
    flag = f'<span class="flag" {ti("flag")}>{tx("flag")}</span>' if hl else ""
    return (f'<article class="plan{" hl" if hl else ""}">{flag}<h3 {ti(f"p{i}h")}>{tx(f"p{i}h")}</h3><p class="for" {ti(f"p{i}f")}>{tx(f"p{i}f")}</p>'
            f'<p class="price"><span {ti("price")}>{tx("price")}</span><small {ti("price_s")}>{tx("price_s")}</small></p><ul>{lis}</ul>'
            f'<a class="btn {"pri" if hl else "sec"}" href="#contato" {ti("cta")}>{tx("cta")}</a></article>')

EN = {k: v[1] for k, v in T.items()}
faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": T[f"q{i}"][0], "acceptedAnswer": {"@type": "Answer", "text": T[f"a{i}"][0]}} for i in range(1, 8)]}, ensure_ascii=False)
org_ld = json.dumps({"@context": "https://schema.org", "@type": "Organization", "name": "RG AI Ltda", "url": "https://gruberia.com/", "email": "rafael@gruberia.com",
    "founder": {"@type": "Person", "name": "Rafael Gruber Bernstein"}, "sameAs": ["https://www.linkedin.com/in/rafaelgruberbernstein"]}, ensure_ascii=False)

HEAD_JS = """(function(){var r=document.documentElement;try{var th=localStorage.getItem('rgai-theme');if(th==='dark'||th==='light')r.setAttribute('data-theme',th);var l=localStorage.getItem('rgai-lang');if(l==='en'||l==='pt')r.setAttribute('data-lang',l)}catch(e){}if(!r.getAttribute('data-lang')){r.setAttribute('data-lang',/^pt/i.test(navigator.language||'pt')?'pt':'en')}})();"""
BODY_JS = """(function(){
var r=document.documentElement,EN=__EN__,UI=__UI__,PT={},lang='pt';
var nodes=[].slice.call(document.querySelectorAll('[data-i18n]')),alts=[].slice.call(document.querySelectorAll('[data-i18n-alt]'));
nodes.forEach(function(n){PT[n.getAttribute('data-i18n')]=n.textContent});
alts.forEach(function(n){PT[n.getAttribute('data-i18n-alt')]=n.alt});
var md=document.querySelector('meta[name=description]');PT.title=document.title;PT.desc=md.content;
function setLang(l,save){lang=l;var D=l==='en'?EN:PT;
 nodes.forEach(function(n){var k=n.getAttribute('data-i18n');if(D[k]!=null)n.textContent=D[k]});
 alts.forEach(function(n){var k=n.getAttribute('data-i18n-alt');if(D[k]!=null)n.alt=D[k]});
 document.title=D.title;md.content=D.desc;r.lang=l==='en'?'en':'pt-BR';r.setAttribute('data-lang',l);
 [].forEach.call(document.querySelectorAll('[data-setlang]'),function(b){b.setAttribute('aria-pressed',b.getAttribute('data-setlang')===l?'true':'false')});
 document.getElementById('langgrp').setAttribute('aria-label',UI[l].lang);
 if(save){try{localStorage.setItem('rgai-lang',l)}catch(e){}}paint()}
[].forEach.call(document.querySelectorAll('[data-setlang]'),function(b){b.addEventListener('click',function(){setLang(b.getAttribute('data-setlang'),true)})});
var tb=document.getElementById('theme'),mq=matchMedia('(prefers-color-scheme: light)');
function cur(){var v=r.getAttribute('data-theme');return v?v:(mq.matches?'light':'dark')}
function paint(){var d=cur()==='dark';r.classList.toggle('is-dark',d);tb.setAttribute('aria-label',d?UI[lang].toLight:UI[lang].toDark)}
tb.addEventListener('click',function(){var n=cur()==='dark'?'light':'dark';r.setAttribute('data-theme',n);try{localStorage.setItem('rgai-theme',n)}catch(e){}paint()});
if(mq.addEventListener)mq.addEventListener('change',paint);
setLang(r.getAttribute('data-lang')==='en'?'en':'pt',false);
var b=document.getElementById('copy'),m=document.getElementById('copied'),e=document.getElementById('mail');
function sel(){try{var x=document.createRange();x.selectNodeContents(e);var s=getSelection();s.removeAllRanges();s.addRange(x)}catch(z){}}
b.addEventListener('click',function(){var tt=e.textContent.trim();function ok(){m.textContent=UI[lang].copied;setTimeout(function(){m.textContent=''},2500)}function no(){sel();m.textContent=UI[lang].sel}try{navigator.clipboard.writeText(tt).then(ok,no)}catch(z){no()}});
})();""".replace("__EN__", json.dumps(EN, ensure_ascii=False)).replace("__UI__", json.dumps(UI, ensure_ascii=False))

SUN = '<svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2" fill="currentColor"/><g stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/></g></svg>'
MOON = '<svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z" fill="currentColor"/></svg>'
LOGO = '<svg viewBox="0 0 30 30" aria-hidden="true"><rect width="30" height="30" rx="8" fill="#12352A"/><path d="M8 21v-4h4.5v4M12.5 17v-4.5H17V17M17 12.5V8h4.5v4.5" fill="none" stroke="#2FB58F" stroke-width="2" stroke-linejoin="round"/></svg>'
FONTS = "family=Instrument+Serif:ital@1&family=JetBrains+Mono:wght@500&family=Manrope:wght@300;400;500;600;700"
pf = "portfolio/index.html" if ARTIFACT else "portfolio/"

head_meta = f"""<title>{tx('title')}</title>
<meta name="description" content="{tx('desc')}">
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
<style>{G.BASE_CSS}{G.THEMES[4]}{CSS}{CSS2}</style>"""

body = f"""<a class="skip" href="#conteudo" {ti('skip')}>{tx('skip')}</a>
<header class="top">
  <div class="w">
    <a class="brand" href="#conteudo">{LOGO}RG AI</a>
    <nav aria-label="Seções">
      <a class="nl" href="#apps" {ti('nav_apps')}>{tx('nav_apps')}</a>
      <a class="nl" href="#como-funciona" {ti('nav_como')}>{tx('nav_como')}</a>
      <a class="nl" href="#planos" {ti('nav_planos')}>{tx('nav_planos')}</a>
      <a class="nl" href="#duvidas" {ti('nav_faq')}>{tx('nav_faq')}</a>
      <div class="tools">
        <div class="seg" role="group" id="langgrp" aria-label="Idioma"><button type="button" data-setlang="pt" aria-pressed="true" lang="pt-BR">PT</button><button type="button" data-setlang="en" aria-pressed="false" lang="en">EN</button></div>
        <button class="icon-btn" id="theme" type="button" aria-label="Mudar para o tema claro">{MOON}{SUN}</button>
      </div>
      <a class="btn pri" href="#contato" {ti('cta')}>{tx('cta')}</a>
    </nav>
  </div>
</header>
<main id="conteudo">
  <div class="hero">
    <svg class="rays" viewBox="0 0 1440 800" preserveAspectRatio="none" aria-hidden="true"><path d="M760 -40C900 180 1080 330 1500 380"/><path d="M820 -40C940 200 1110 360 1500 430"/><path d="M880 -40C990 230 1150 400 1500 490"/><path d="M700 820C900 640 1120 560 1500 560"/></svg>
    <div class="w hero-grid">
      <div>
        <h1><span {ti('h1a')}>{tx('h1a')}</span> <span class="em" {ti('h1b')}>{tx('h1b')}</span></h1>
        <p class="sub" {ti('sub')}>{tx('sub')}</p>
        <div class="acts"><a class="btn pri" href="#contato" {ti('cta')}>{tx('cta')}</a><span class="fine" {ti('fine')}>{tx('fine')}</span></div>
      </div>
      <div class="mockup">{DECK}</div>
    </div>
  </div>

  <section class="band" id="prova" aria-labelledby="h-prova">
    <div class="w">
      <div class="sh"><p class="kicker" {ti('prova_k')}>{tx('prova_k')}</p><h2 id="h-prova" {ti('prova_h')}>{tx('prova_h')}</h2></div>
      <div class="stats">{''.join(f'<div class="stat"><b {ti(f"s{i}b")}>{tx(f"s{i}b")}</b><span {ti(f"s{i}")}>{tx(f"s{i}")}</span></div>' for i in range(1,5))}</div>
    </div>
  </section>

  <section id="apps" aria-labelledby="h-apps">
    <div class="w">
      <div class="sh"><p class="kicker" {ti('apps_k')}>{tx('apps_k')}</p><h2 id="h-apps" {ti('apps_h')}>{tx('apps_h')}</h2></div>
      <div class="apps">
        {app(1, "RiskAI FIDC", "portfolio/img/riskai-2.webp", "riskai")}
        {app(2, "LeadScout", "portfolio/img/leadscout-1.webp", "leadscout")}
        {app(3, "Carteira360", "portfolio/img/carteira360-5.webp", "carteira360")}
        {app(4, "Wonespace", "portfolio/img/wonespace-1.webp", "wonespace", own=True)}
      </div>
      <p class="apps-note" {ti('apps_p')}>{tx('apps_p')}</p>
    </div>
  </section>

  <section id="segmentos" aria-labelledby="h-seg">
    <div class="w">
      <div class="sh"><p class="kicker" {ti('seg_k')}>{tx('seg_k')}</p><h2 id="h-seg" {ti('seg_h')}>{tx('seg_h')}</h2></div>
      <div class="segs">{''.join(f'<article class="{"main" if i==1 else ""}"><p class="kicker" {ti(f"g{i}k")}>{tx(f"g{i}k")}</p><h3 {ti(f"g{i}h")}>{tx(f"g{i}h")}</h3><p {ti(f"g{i}p")}>{tx(f"g{i}p")}</p></article>' for i in range(1,4))}</div>
    </div>
  </section>

  <section id="fundador" aria-labelledby="h-fd">
    <div class="w">
      <div class="sh"><p class="kicker" {ti('fd_k')}>{tx('fd_k')}</p></div>
      <div class="founder">
        <div class="mono-av" aria-hidden="true">RG</div>
        <div>
          <h3 id="h-fd">Rafael Gruber Bernstein</h3>
          <p class="role" {ti('fd_role')}>{tx('fd_role')}</p>
          <div class="bio"><p {ti('fd_p1')}>{tx('fd_p1')}</p><p {ti('fd_p2')}>{tx('fd_p2')}</p></div>
          <div class="chips"><span {ti('fd_c1')}>{tx('fd_c1')}</span><span {ti('fd_c2')}>{tx('fd_c2')}</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="band" id="como-funciona" aria-labelledby="h-como">
    <div class="w">
      <div class="sh"><p class="kicker" {ti('como_k')}>{tx('como_k')}</p><h2 id="h-como" {ti('como_h')}>{tx('como_h')}</h2></div>
      <ol class="steps">{''.join(f'<li><h3 {ti(f"st{i}h")}>{tx(f"st{i}h")}</h3><p {ti(f"st{i}")}>{tx(f"st{i}")}</p></li>' for i in range(1,5))}</ol>
    </div>
  </section>

  <section id="planos" aria-labelledby="h-planos">
    <div class="w">
      <div class="sh"><p class="kicker" {ti('pl_k')}>{tx('pl_k')}</p><h2 id="h-planos" {ti('pl_h')}>{tx('pl_h')}</h2></div>
      <div class="plans">{plan(1,['p1a','p1b','p1c'],False)}{plan(2,['p2a','p2b','p2c','p2d'],True)}{plan(3,['p3a','p3b','p3c','p3d'],False)}</div>
      <p class="plans-note" {ti('pl_note')}>{tx('pl_note')}</p>
    </div>
  </section>

  <section class="band" id="duvidas" aria-labelledby="h-faq">
    <div class="w">
      <div class="sh"><p class="kicker" {ti('faq_k')}>{tx('faq_k')}</p><h2 id="h-faq" {ti('faq_h')}>{tx('faq_h')}</h2></div>
      <div class="faq">{''.join(f'<details><summary {ti(f"q{i}")}>{tx(f"q{i}")}</summary><p {ti(f"a{i}")}>{tx(f"a{i}")}</p></details>' for i in range(1,8))}</div>
    </div>
  </section>

  <section class="final" id="contato" aria-labelledby="h-final">
    <div class="w">
      <p class="kicker" {ti('fin_k')}>{tx('fin_k')}</p>
      <h2 id="h-final" {ti('fin_h')}>{tx('fin_h')}</h2>
      <p class="l" {ti('fin_p')}>{tx('fin_p')}</p>
      <div class="contact-card">
        <div class="crow"><span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M3.5 6.5l8.5 6 8.5-6" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></span><code class="val" id="mail">rafael@gruberia.com</code><button class="btn pri" id="copy" type="button" {ti('copy')}>{tx('copy')}</button></div>
        <div class="crow"><span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="3" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8 10.5v6M8 7.5v.01M11.5 16.5v-3.2c0-1.6 1-2.8 2.4-2.8s2.1 1 2.1 2.6v3.4M11.5 10.5v6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span><a class="val" href="https://www.linkedin.com/in/rafaelgruberbernstein" target="_blank" rel="noopener"><span>linkedin.com/in/rafaelgruberbernstein</span><span class="arrow" aria-hidden="true">↗</span></a></div>
      </div>
      <p class="copied" id="copied" role="status" aria-live="polite"></p>
    </div>
  </section>
</main>
<footer><div class="w"><span {ti('foot1')}>{tx('foot1')}</span><span><a href="{pf}" {ti('foot_p')}>{tx('foot_p')}</a> · <span {ti('foot2')}>{tx('foot2')}</span></span></div></footer>
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
