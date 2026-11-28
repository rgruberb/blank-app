#!/usr/bin/env python3
"""Etapas em loop, remove 'Como entregamos' e 'Teste a lógica', FAQ sem custo/tempo, linguagem formal."""
import sys, re
p = sys.argv[1]
s = open(p, encoding="utf8").read()

def rep(old, new):
    global s
    assert old in s, "não achei: " + old[:90]
    s = s.replace(old, new, 1)

def cut(a_mark, b_mark):
    global s
    a = s.index(a_mark); b = s.index(b_mark, a); s = s[:a] + s[b:]

# ---------- remover seções ----------
cut('\n  <section id="demo"', '\n  <section id="segmentos"')
rep("""      <a class="nl" href="#demo" {ti('dm_k')}>{tx('dm_k')}</a>\n""", "")
cut('/* ---------- D: demonstração do LeadScout ---------- */', '/* ---------- A + H: geração das telas e autoplay da galeria ---------- */')

# ---------- FAQ sem custo e tempo ----------
s = s.replace("for i in range(1, 10))", "for i in (1, 4, 5, 6, 7, 8, 9))")

# ---------- etapas em loop contínuo ----------
a = s.index("/* ---------- etapas:")
b = s.index("else setP(1);", a) + len("else setP(1);")
s = s[:a] + r"""/* ---------- etapas: acendem em sequência, em loop ---------- */
var steps=document.querySelector('.steps'),items=[].slice.call(steps.querySelectorAll('li')),N=items.length,sk=0,stT=0,stIn=false;
function setP(k){steps.style.setProperty('--p',(k<1?0:(k-1)/N).toFixed(3));items.forEach(function(li,i){li.classList.toggle('on',i<k);li.classList.toggle('cur',i===k-1)})}
function tick(){clearTimeout(stT);if(!stIn||r.classList.contains('paused')||RM.matches)return;sk=sk>=N?0:sk+1;setP(sk);stT=setTimeout(tick,sk>=N?2000:(sk===0?600:950))}
if(RM.matches)setP(N);else{setP(0);new IntersectionObserver(function(e){stIn=e[0].isIntersecting;clearTimeout(stT);if(stIn)stT=setTimeout(tick,350)},{threshold:.3}).observe(steps)}""" + s[b:]
rep("pb.setAttribute('aria-pressed',allPaused?'true':'false');pbLabel();stream.setPaused(allPaused)});",
    "pb.setAttribute('aria-pressed',allPaused?'true':'false');pbLabel();stream.setPaused(allPaused);if(!allPaused&&typeof tick==='function')tick()});")
rep('<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>\n<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>\n', "")
rep(".steps .rail i{display:block;height:100%;background:linear-gradient(90deg,var(--accent-2),var(--accent));transform-origin:left;transform:scaleX(var(--p,1))}",
    ".steps .rail i{display:block;height:100%;background:linear-gradient(90deg,var(--accent-2),var(--accent));transform-origin:left;transform:scaleX(var(--p,.75));transition:transform .8s var(--ease)}\n"
    ".steps li.on .num{box-shadow:0 0 0 6px var(--accent-soft),0 0 28px -6px var(--accent)}\n"
    ".steps li.cur .num{animation:lit .9s var(--ease)}\n@keyframes lit{40%{transform:scale(1.14)}100%{transform:none}}\n"
    ".steps li h3,.steps li p{transition:opacity .45s var(--ease)}\n.js .steps li:not(.on) h3,.js .steps li:not(.on) p{opacity:.4}")

# ---------- linguagem formal ----------
FORMAL = {
 "desc": ("Desenvolvimento de aplicações web sob medida com dados e inteligência artificial, do levantamento de requisitos à produção. Especialidade em crédito e finanças.",
          "Custom web applications built with data and artificial intelligence, from requirements gathering to production. Specialized in credit and finance."),
 "nav_como": ("Metodologia", "Methodology"), "nav_faq": ("Perguntas frequentes", "FAQ"),
 "cta": ("Agendar uma reunião", "Schedule a meeting"), "see": ("Conhecer os projetos", "View the projects"),
 "badge": ("3 aplicações em produção desde mar/2026", "3 applications in production since Mar 2026"),
 "h1a": ("Aplicações sob medida,", "Custom applications,"),
 "sub": ("Desenvolvemos aplicações sob medida com dados e inteligência artificial, com suporte contínuo após a implantação.",
         "We develop custom applications with data and artificial intelligence, with ongoing support after deployment."),
 "m1": ("aplicações em produção", "applications in production"),
 "m2": ("de ganho de produtividade em prospecção e gestão de carteira", "productivity gain in prospecting and portfolio management"),
 "m3": ("telas reais apresentadas, com dados fictícios", "real screens shown, with fictional data"),
 "m4": ("em produção e em uso diário desde", "in production and in daily use since"),
 "proj_h": ("Projetos desenvolvidos", "Developed projects"),
 "proj_p": ("Selecione um projeto para visualizar as telas. Todos os dados são fictícios e nenhum cliente é identificado.",
            "Select a project to view its screens. All data is fictional and no client is identified."),
 "lb_hint": ("Clique na tela para ampliá-la", "Click the screen to enlarge it"),
 "seg_k": ("Segmentos", "Industries"), "seg_h": ("Segmentos de atuação", "Industries we serve"),
 "g3p": ("Gestão de produção, aprovações e mensagens entre a agência e o cliente em uma única aplicação.", "Production management, approvals and messaging between agency and client in a single application."),
 "como_k": ("Metodologia", "Methodology"), "como_h": ("Metodologia em quatro etapas", "A four-step methodology"),
 "st1h": ("Levantamento", "Discovery"), "st1": ("Levantamento dos processos atuais e definição formal do problema.", "Review of current processes and formal definition of the problem."),
 "st2h": ("Protótipo", "Prototype"), "st2": ("Protótipo navegável das telas principais, com estimativa de prazo e custo.", "Clickable prototype of the main screens, with a time and cost estimate."),
 "st3h": ("Desenvolvimento", "Development"), "st3": ("Desenvolvimento em ciclos curtos, com validação da equipe a cada entrega.", "Development in short cycles, validated by your team at each delivery."),
 "st4h": ("Implantação e suporte", "Deployment and support"), "st4": ("Implantação, treinamento da equipe e suporte contínuo de hospedagem, backups e ajustes.", "Deployment, team training and ongoing support for hosting, backups and adjustments."),
 "fd_k": ("Fundador", "Founder"),
 "fd_p": ("Mais de três anos de experiência conduzindo produtos de dados e inteligência artificial do conceito à produção, incluindo dois produtos de visão computacional na Radix. Desde março de 2026, à frente da RG AI.",
          "More than three years of experience taking data and artificial intelligence products from concept to production, including two computer-vision products at Radix. Leading RG AI since March 2026."),
 "faq_k": ("Perguntas frequentes", "FAQ"), "faq_h": ("Perguntas frequentes", "Frequently asked questions"),
 "q1": ("Que tipo de aplicação a RG AI desenvolve?", "What kind of applications does RG AI develop?"),
 "a1": ("Aplicações web sob medida com dados e inteligência artificial: painéis de risco, prospecção e CRM, gestão de carteira, agenda e operação. A especialidade é crédito e finanças, com atuação também em saúde e em agências de marca pessoal.",
        "Custom web applications with data and artificial intelligence: risk dashboards, prospecting and CRM, portfolio management, scheduling and operations. Our specialty is credit and finance, and we also serve healthcare and personal-brand agencies."),
 "q4": ("Como a inteligência artificial é utilizada?", "How is artificial intelligence used?"),
 "a4": ("Sempre que agrega valor ao processo. Os modelos são comparados por acurácia, custo e desempenho, e o critério de aprovação é definido antes da avaliação dos resultados. Modelos que não atingem o critério não são publicados.",
        "Wherever it adds value to the process. Models are compared on accuracy, cost and performance, and the approval criterion is set before results are evaluated. Models that do not meet the criterion are not published."),
 "q5": ("Como os dados são protegidos?", "How is data protected?"),
 "a5": ("Controle de acesso por perfil, senhas armazenadas com hash, conexões criptografadas, backups e monitoramento. Em saúde, todo dado clínico é tratado como dado sensível, conforme a LGPD.",
        "Role-based access control, hashed passwords, encrypted connections, backups and monitoring. In healthcare, all clinical data is treated as sensitive data, in accordance with Brazil's LGPD."),
 "q6": ("As aplicações funcionam em dispositivos móveis?", "Do the applications work on mobile devices?"),
 "a6": ("Sim. As aplicações são web e funcionam no navegador do computador e do celular, sem necessidade de instalação.", "Yes. The applications are web-based and run in the browser on desktop and mobile, with no installation required."),
 "q7": ("A RG AI realiza o registro da marca?", "Does RG AI register the brand?"),
 "a7": ("Sim. Realizamos o registro da marca da aplicação no INPI.", "Yes. We register the application's brand with the INPI, Brazil's trademark office."),
 "q8": ("Há suporte após a implantação?", "Is there support after deployment?"),
 "a8": ("Sim. O suporte contínuo inclui hospedagem, backups, monitoramento, atualizações de segurança e ajustes.", "Yes. Ongoing support includes hosting, backups, monitoring, security updates and adjustments."),
 "q9": ("É possível integrar com os sistemas já utilizados?", "Can it integrate with existing systems?"),
 "a9": ("Sim. A aplicação pode ler planilhas e exportações do sistema atual ou integrar-se a ele por meio de API.", "Yes. The application can read spreadsheets and exports from your current system or integrate with it through an API."),
 "foot2": ("Telas de demonstração com dados fictícios.", "Demo screens with fictional data."),
}
import json
for k, (pt, en) in FORMAL.items():
    m = re.search(r'"' + re.escape(k) + r'": \(\s*("[^"]*"),\s*("[^"]*")\s*\)', s)
    assert m, "chave não encontrada: " + k
    s = s[:m.start()] + '"' + k + '": (' + json.dumps(pt, ensure_ascii=False) + ", " + json.dumps(en, ensure_ascii=False) + ")" + s[m.end():]

open(p, "w", encoding="utf8").write(s)
print("ok")
