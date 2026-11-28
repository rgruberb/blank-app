#!/usr/bin/env python3
"""Aplica os 10 incrementos (A–J) em final3.py."""
import sys
p = sys.argv[1]
s = open(p, encoding="utf8").read()

def rep(old, new, count=1):
    global s
    assert old in s, "não achei: " + old[:80]
    s = s.replace(old, new, count)

# ---------------- textos novos ----------------
rep(' "fin_k": ("Contato", "Contact"),', ''' "in_k": ("Por dentro", "Inside"),
 "in_h1": ("Por dentro de um app", "Inside an app"), "in_h2": ("em produção", "in production"),
 "in_p": ("Role para ver como o comitê de crédito usa o RiskAI no dia a dia. Telas reais, carteira fictícia.", "Scroll to see how the credit committee uses RiskAI day to day. Real screens, fictional portfolio."),
 "in1h": ("O dia começa no resumo", "The day starts with the summary"), "in1": ("Grupos por faixa de risco e o que mais mudou desde ontem, numa tela só.", "Groups by risk band and what changed most since yesterday, on one screen."),
 "in2h": ("Um clique abre o grupo", "One click opens the group"), "in2": ("Risco total, uso do limite e os sinais de cada grupo econômico.", "Total risk, limit usage and the signals of each economic group."),
 "in3h": ("Os sinais aparecem cedo", "Signals show up early"), "in3": ("Recompras, prorrogações e vencidos aparecem antes de virar perda.", "Buybacks, extensions and overdue items show up before they turn into losses."),
 "in4h": ("A carteira ao lado do mercado", "The portfolio next to the market"), "in4": ("A PDD do mês comparada com indicadores do Banco Central.", "The month's provisions compared with Central Bank indicators."),
 "dm_k": ("Teste a lógica", "Try the logic"),
 "dm_h1": ("Um modelo", "One model"), "dm_h2": ("audita o outro.", "audits the other."),
 "dm_p": ("Simulação da lógica do LeadScout, com uma empresa fictícia. Verifique cada afirmação e veja o que acontece quando não há fonte.", "A simulation of LeadScout's logic, with a fictional company. Check each claim and see what happens when there's no source."),
 "dm_co": ("Metalúrgica Exemplo Ltda", "Example Metalworks Ltd"), "dm_meta": ("Lead fictício · Rio de Janeiro", "Fictional lead · Rio de Janeiro"),
 "dm_score": ("Nota do lead", "Lead score"), "dm_check": ("Verificar fonte", "Check source"), "dm_auditing": ("Auditando…", "Auditing…"),
 "dm_ok": ("Fonte verificada", "Source verified"), "dm_no": ("Indeterminada", "Undetermined"),
 "dm_c1": ("Atende mais de 50 clientes PJ", "Serves more than 50 business clients"), "dm_s1": ("Site da empresa, página Clientes", "Company website, Clients page"),
 "dm_c2": ("Vende a prazo, de 30 a 90 dias", "Sells on 30 to 90-day terms"), "dm_s2": ("Catálogo comercial em PDF", "Sales catalogue (PDF)"),
 "dm_c3": ("Faturamento anual acima de R$ 20 milhões", "Annual revenue above R$20 million"), "dm_s3": ("Nenhuma fonte pública confirma", "No public source confirms it"),
 "dm_c4": ("Fornece para uma rede varejista nacional", "Supplies a national retail chain"), "dm_s4": ("Só aparece em texto gerado, sem link", "Only appears in generated text, no link"),
 "dm_reset": ("Recomeçar", "Start over"), "dm_note": ("Demonstração com dados fictícios. No app real, a pesquisa usa a API da Anthropic.", "Demo with fictional data. In the real app, research uses the Anthropic API."),
 "eg_k": ("Como entregamos", "How we deliver"), "eg_h": ("O que mantém um app de pé depois do deploy", "What keeps an app standing after deploy"),
 "eg1h": ("Validação fora do tempo", "Out-of-time validation"), "eg1": ("O critério de aprovação é escrito antes de ver o resultado. Modelo que não passa não vai para a tela.", "The approval criterion is written before seeing results. A model that fails never reaches the screen."),
 "eg2h": ("Retreino diário", "Daily retraining"), "eg2": ("Só publica modelos aprovados na validação, com recuo automático se o realizado sair do previsto.", "Only publishes models that pass validation, with automatic fallback if reality drifts from the forecast."),
 "eg3h": ("Deploy com rollback", "Deploy with rollback"), "eg3": ("Via GitHub, com health check antes de trocar a versão.", "Through GitHub, with a health check before switching versions."),
 "eg4h": ("Acesso e SSO", "Access and SSO"), "eg4": ("Acesso por papéis, senhas com hash e login único entre os apps.", "Role-based access, hashed passwords and single sign-on across apps."),
 "eg5h": ("Backups e monitoramento", "Backups and monitoring"), "eg5": ("Servidor Linux com Cloudflare Tunnel e Access, backups diários.", "Linux server with Cloudflare Tunnel and Access, daily backups."),
 "eg6h": ("QA antes de cada release", "QA before every release"), "eg6": ("Testes de API e de interface antes de publicar.", "API and interface tests before publishing."),
 "tech_k": ("Ferramentas do dia a dia", "Everyday tools"),
 "tl1": ("Requisito", "Requirements"), "tl2": ("Protótipo", "Prototype"), "tl3": ("Produção", "Production"), "tl3b": ("Em construção", "In development"),
 "bd_ra1": ("Retreino diário", "Daily retraining"), "bd_ra2": ("Validação fora do tempo", "Out-of-time validation"),
 "bd_ls1": ("IA auditada", "Audited AI"), "bd_ls2": ("+200% com o Carteira360", "+200% with Carteira360"),
 "bd_c31": ("+200% de produtividade", "+200% productivity"), "bd_c32": ("3 visões: gestor, gerente, celular", "3 views: manager, account manager, phone"),
 "bd_wn1": ("Tempo real", "Real time"), "bd_wn2": ("Demonstração sob NDA", "Demo under NDA"),
 "fin_k": ("Contato", "Contact"),''')
rep('"pause": "Pausar animação", "play": "Retomar animação"}', '"pause": "Pausar animações", "play": "Retomar animações"}')
rep('"pause": "Pause animation", "play": "Resume animation"}', '"pause": "Pause animations", "play": "Resume animations"}')

# ---------------- G: selos + linha do tempo por projeto ----------------
rep('PHONE = {"carteira360-m1.webp", "wonespace-m1.webp"}', '''PHONE = {"carteira360-m1.webp", "wonespace-m1.webp"}
BADGES = {"riskai": ["bd_ra1", "bd_ra2"], "leadscout": ["bd_ls1", "bd_ls2"], "carteira360": ["bd_c31", "bd_c32"], "wonespace": ["bd_wn1", "bd_wn2"]}''')
rep('''          <dl class="spec">{rows}</dl>''', '''          <div class="badges">{''.join(f'<span {ti(b)}>{tx(b)}</span>' for b in BADGES[p["id"]])}</div>
          <ol class="tline" aria-label="Etapas">
            <li class="done"><span {ti("tl1")}>{tx("tl1")}</span></li><li class="done"><span {ti("tl2")}>{tx("tl2")}</span></li>
            <li class="{"wip" if p["own"] else "done"}"><span {ti("tl3b" if p["own"] else "tl3")}>{tx("tl3b" if p["own"] else "tl3")}</span></li>
          </ol>
          <dl class="spec">{rows}</dl>''')
# H: barra de progresso (autoplay) nas miniaturas
rep('''<img src="{IMG}{f}" alt="" loading="lazy" width="160" height="100"><span {ti(s)}>{tx(s)}</span></button>''',
    '''<img src="{IMG}{f}" alt="" loading="lazy" width="160" height="100"><span {ti(s)}>{tx(s)}</span><i class="prog" aria-hidden="true"></i></button>''')

# ---------------- novas seções (C, D, E, F) ----------------
INSIDE = '''
  <section id="por-dentro" class="amb amb-l" aria-labelledby="h-in">
    <div class="w">
      <div class="sh rv"><div><p class="lbl" {ti('in_k')}>{tx('in_k')}</p><h2 id="h-in"><span {ti('in_h1')}>{tx('in_h1')}</span> <span class="em" {ti('in_h2')}>{tx('in_h2')}</span></h2></div><p {ti('in_p')}>{tx('in_p')}</p></div>
      <div class="story">
        <div class="story-media" aria-hidden="true">
          <div class="browser"><div class="bar"><i></i><i></i><i></i><span>riskai.app</span></div>
            <div class="story-stage">
              <img class="on" src="{IMG}riskai-1.webp" width="1500" height="938" alt="" loading="lazy">
              <img src="{IMG}riskai-2.webp" width="1500" height="938" alt="" loading="lazy">
              <img src="{IMG}riskai-4.webp" width="1500" height="938" alt="" loading="lazy">
              <img src="{IMG}riskai-5.webp" width="1500" height="938" alt="" loading="lazy">
            </div>
            <div class="story-bar"><i></i></div>
          </div>
        </div>
        <ol class="story-steps">
          {''.join(f'<li class="sstep{" on" if i==1 else ""}" data-i="{i-1}"><span class="sn">0{i}</span><h3 {ti(f"in{i}h")}>{tx(f"in{i}h")}</h3><p {ti(f"in{i}")}>{tx(f"in{i}")}</p><img class="sm" src="{IMG}{["riskai-1","riskai-2","riskai-4","riskai-5"][i-1]}.webp" width="1500" height="938" alt="{tx(["ra_a1","ra_a2","ra_a3","ra_a4"][i-1])}" data-i18n-alt="{["ra_a1","ra_a2","ra_a3","ra_a4"][i-1]}" loading="lazy"></li>' for i in range(1,5))}
        </ol>
      </div>
    </div>
  </section>
'''
DEMO = '''
  <section id="demo" class="amb amb-r" aria-labelledby="h-dm">
    <div class="w demo-grid">
      <div class="rv">
        <p class="lbl" {ti('dm_k')}>{tx('dm_k')}</p>
        <h2 id="h-dm" class="dm-h"><span {ti('dm_h1')}>{tx('dm_h1')}</span> <span class="em" {ti('dm_h2')}>{tx('dm_h2')}</span></h2>
        <p class="dm-p" {ti('dm_p')}>{tx('dm_p')}</p>
        <p class="dm-note" {ti('dm_note')}>{tx('dm_note')}</p>
      </div>
      <div class="lead rv" id="lead">
        <div class="lead-top">
          <div class="lead-av" aria-hidden="true">ME</div>
          <div><p class="lead-co" {ti('dm_co')}>{tx('dm_co')}</p><p class="lead-meta" {ti('dm_meta')}>{tx('dm_meta')}</p></div>
          <div class="score"><span class="score-n" id="score">40</span><span class="score-l" {ti('dm_score')}>{tx('dm_score')}</span></div>
        </div>
        <div class="score-bar" aria-hidden="true"><i id="scorebar" style="--s:.4"></i></div>
        <ul class="claims">
          {''.join(f'<li class="claim" data-ok="{1 if i<3 else 0}"><div class="c-txt"><p {ti(f"dm_c{i}")}>{tx(f"dm_c{i}")}</p><p class="c-src"><span {ti(f"dm_s{i}")}>{tx(f"dm_s{i}")}</span></p></div><button type="button" class="c-btn"><span class="c-lab" {ti("dm_check")}>{tx("dm_check")}</span></button><span class="c-res ok"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8.5l3 3 6-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span {ti("dm_ok")}>{tx("dm_ok")}</span></span><span class="c-res no"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 3.5v5M8 11.5v.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><span {ti("dm_no")}>{tx("dm_no")}</span></span></li>' for i in range(1,5))}
        </ul>
        <div class="lead-foot"><p class="sr" id="dmlive" role="status" aria-live="polite"></p><button type="button" class="btn sm" id="dmreset" {ti('dm_reset')}>{tx('dm_reset')}</button></div>
      </div>
    </div>
  </section>
'''
DELIVER = '''
  <section id="entrega" class="amb amb-l" aria-labelledby="h-eg">
    <div class="w">
      <div class="sh rv"><div><p class="lbl" {ti('eg_k')}>{tx('eg_k')}</p><h2 id="h-eg" {ti('eg_h')}>{tx('eg_h')}</h2></div></div>
      <div class="dbento">{''.join(f'<article class="cell rv d{i}"><span class="ico">{EG_ICONS[i-1]}</span><h3 {ti(f"eg{i}h")}>{tx(f"eg{i}h")}</h3><p {ti(f"eg{i}")}>{tx(f"eg{i}")}</p></article>' for i in range(1,7))}</div>
    </div>
    <div class="marquee" aria-label="{tx('tech_k')}" role="group">
      <p class="lbl w" {ti('tech_k')}>{tx('tech_k')}</p>
      <div class="mq"><div class="mq-track">{TECH}{TECH_DUP}</div></div>
    </div>
  </section>
'''
rep('''  <section id="projetos" aria-labelledby="h-proj">''', INSIDE + '''  <section id="projetos" class="amb amb-r" aria-labelledby="h-proj">''')
rep('''  <section id="segmentos" aria-labelledby="h-seg">''', DEMO + DELIVER + '''  <section id="segmentos" class="amb amb-r" aria-labelledby="h-seg">''')
rep('''  <section id="duvidas" aria-labelledby="h-faq">''', '''  <section id="duvidas" class="amb amb-l" aria-labelledby="h-faq">''')

rep("ICONS = {", '''TECHS = ["Python","pandas","LightGBM","SQL Server","Power BI","Flask","JavaScript","TypeScript","React","SQLite","APIs REST","Linux","Cloudflare","GitHub","Claude Code","API da Anthropic"]
TECH = "".join(f'<span>{t}</span>' for t in TECHS)
TECH_DUP = "".join(f'<span aria-hidden="true">{t}</span>' for t in TECHS)
_i = lambda d: f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{d}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
EG_ICONS = [_i("M4 19h16M6 15l4-4 3 3 5-6"), _i("M20 12a8 8 0 1 1-2.3-5.6M20 4v4h-4"), _i("M12 3v12M7 10l5 5 5-5M5 21h14"),
            _i("M7 11V8a5 5 0 0 1 10 0v3M5 11h14v10H5z"), _i("M4 6h16v5H4zM4 13h16v5H4zM8 8.5h.01M8 15.5h.01"), _i("M9 12l2 2 4-4M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z")]
ICONS = {''')

# ---------------- B: WebGL + pausa global, I: spotlight ----------------
rep('''    <button type="button" class="pause" id="pause" aria-pressed="false" aria-label="Pausar animação">''', '''    <button type="button" class="pause" id="pause" aria-pressed="false" aria-label="Pausar animações">''')
rep('''<footer>''', '''<div class="spot" aria-hidden="true"></div>
<footer>''')
# hero: a moldura deixa de ter entrada própria (a geração da imagem cuida disso)
rep(".js .hero .browser{opacity:0;animation:frame 1.1s var(--ease) .25s forwards}", ".js .hero .browser{animation:frame 1.1s var(--ease) .1s both}")
rep("@keyframes frame{from{opacity:0;transform:translateY(40px) rotateX(14deg) scale(.96)}to{opacity:1;transform:none}}", "@keyframes frame{from{transform:translateY(30px) rotateX(10deg) scale(.97)}to{transform:none}}")

CSS_ADD = r"""
/* pausa global (fixa) */
.pause{position:fixed!important;right:max(16px,env(safe-area-inset-right,0px))!important;bottom:calc(16px + env(safe-area-inset-bottom,0px))!important;z-index:45!important;width:44px!important;height:44px!important;background:color-mix(in srgb,var(--surface) 80%,transparent)!important}
:root.paused .mq-track,:root.paused .fA,:root.paused .fB,:root.paused .badge .dot::after,:root.paused .prog{animation-play-state:paused!important}
/* J: luz ambiente por seção */
.amb{isolation:isolate}
.amb::before{content:"";position:absolute;z-index:-1;pointer-events:none;width:min(900px,90vw);aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,var(--accent-soft),transparent 62%);opacity:.9;top:-10%}
.amb-l::before{left:-25%}.amb-r::before{right:-25%}
:root[data-theme="light"] .amb::before{opacity:.6}
/* I: luz que segue o cursor */
.spot{position:fixed;inset:0;pointer-events:none;z-index:30;opacity:0;transition:opacity .4s var(--ease);background:radial-gradient(480px circle at var(--sx,50%) var(--sy,50%),rgba(61,220,168,.06),transparent 70%)}
.spot.on{opacity:1}
:root[data-theme="light"] .spot{display:none}
/* I: odômetro */
.odo{display:inline-flex;align-items:baseline}
.dg{display:inline-block;height:1em;overflow:hidden;line-height:1em;vertical-align:bottom}
.dg .col{display:flex;flex-direction:column;transition:transform 1.3s cubic-bezier(.2,.8,.2,1)}
.dg .col span{height:1em;line-height:1em;text-align:center}
/* C: rolagem guiada */
.story{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:clamp(32px,5vw,72px);align-items:start}
.story-media{position:sticky;top:calc(96px + env(safe-area-inset-top,0px))}
.story-stage{position:relative;aspect-ratio:1500/938;background:var(--bg-2)}
.story-stage img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top left;opacity:0;transform:scale(1.02);transition:opacity .6s var(--ease),transform .9s var(--ease)}
.story-stage img.on{opacity:1;transform:none}
.story-bar{height:3px;background:var(--rule)}
.story-bar i{display:block;height:100%;background:linear-gradient(90deg,var(--accent-2),var(--accent));transform-origin:left;transform:scaleX(var(--sp,.25));transition:transform .5s var(--ease)}
.story-steps{list-style:none;margin:0;padding:0}
.sstep{min-height:62vh;display:flex;flex-direction:column;justify-content:center;gap:12px;padding-left:24px;border-left:2px solid var(--rule);transition:border-color .4s var(--ease)}
.sstep .sn{font:500 .8rem/1 var(--f-mono);color:var(--muted);letter-spacing:.08em}
.sstep h3{font-size:clamp(1.6rem,1.2rem + 1.4vw,2.4rem);font-weight:500;letter-spacing:-.03em;color:var(--muted);transition:color .4s var(--ease)}
.sstep p{max-width:38ch;color:var(--muted);transition:color .4s var(--ease)}
.sstep.on{border-left-color:var(--accent)}.sstep.on h3{color:var(--ink)}.sstep.on p{color:var(--ink-2)}.sstep.on .sn{color:var(--accent)}
.sstep .sm{display:none}
@media(max-width:900px){.story{grid-template-columns:1fr}.story-media{display:none}.sstep{min-height:0;padding:20px 0 28px 20px}.sstep .sm{display:block;border-radius:12px;border:1px solid var(--glass-b);margin-top:8px}.sstep h3,.sstep p{color:var(--ink)}}
/* G: selos e linha do tempo */
.badges{display:flex;flex-wrap:wrap;gap:8px}
.badges span{font:600 .8rem/1 var(--f-body);padding:9px 12px;border-radius:999px;background:var(--accent-soft);color:var(--accent);border:1px solid color-mix(in srgb,var(--accent) 30%,transparent)}
.tline{list-style:none;margin:4px 0 0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);position:relative}
.tline::before{content:"";position:absolute;left:6px;right:calc(33.3% - 6px);top:6px;height:2px;background:var(--accent)}
.tline li{position:relative;padding-top:20px;font:500 .74rem/1.2 var(--f-mono);letter-spacing:.05em;text-transform:uppercase;color:var(--ink-2)}
.tline li::before{content:"";position:absolute;left:0;top:0;width:14px;height:14px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 3px var(--bg)}
.tline li.wip{color:var(--own)}.tline li.wip::before{background:var(--bg);border:2px dashed var(--own)}
.tline:has(.wip)::before{right:calc(66.6% - 6px)}
/* H: virada 3D na troca de aba + autoplay */
.panel.enter .viewer{animation:flipIn .6s var(--ease)}
.panel.enter .info{animation:panelIn .5s var(--ease) .08s both}
@keyframes flipIn{from{opacity:0;transform:perspective(1400px) rotateY(-12deg) translateX(-24px)}to{opacity:1;transform:none}}
.thumb{position:relative;overflow:hidden}
.thumb .prog{position:absolute;left:0;right:0;bottom:0;height:3px;background:var(--accent);transform-origin:left;transform:scaleX(0)}
.panel.auto .thumb.on .prog{animation:prog 4.5s linear forwards}
@keyframes prog{to{transform:scaleX(1)}}
.panel.auto .viewer:hover .prog,.panel.auto .viewer:focus-within .prog,#projetos:not(.inview) .prog{animation-play-state:paused}
/* D: demonstração interativa */
.demo-grid{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(32px,5vw,72px);align-items:center}
@media(max-width:960px){.demo-grid{grid-template-columns:1fr}}
.dm-h{margin-top:14px;font-size:clamp(2.2rem,1.4rem + 3vw,4rem);line-height:1;font-weight:500;letter-spacing:-.04em}
.dm-p{margin-top:20px;max-width:44ch}
.dm-note{margin-top:16px;font-size:.85rem;color:var(--muted);max-width:44ch}
.lead{border-radius:var(--r-lg);border:1px solid var(--glass-b);background:var(--glass);backdrop-filter:blur(20px) saturate(140%);-webkit-backdrop-filter:blur(20px) saturate(140%);box-shadow:var(--shadow);padding:clamp(18px,3vw,28px)}
.lead-top{display:flex;align-items:center;gap:14px}
.lead-av{width:48px;height:48px;border-radius:12px;display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);font:700 .95rem/1 var(--f-head);flex:none}
.lead-co{color:var(--ink);font-weight:700;font-size:1.05rem}
.lead-meta{font-size:.85rem;color:var(--muted)}
.score{margin-left:auto;text-align:right}
.score-n{display:block;font:300 2.4rem/1 var(--f-head);color:var(--ink);font-variant-numeric:tabular-nums}
.score-l{font:500 .7rem/1 var(--f-mono);letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.score-bar{margin:16px 0 8px;height:6px;border-radius:6px;background:var(--glass-2);overflow:hidden}
.score-bar i{display:block;height:100%;background:linear-gradient(90deg,var(--accent-2),var(--accent));transform-origin:left;transform:scaleX(var(--s));transition:transform .6s var(--ease)}
.claims{list-style:none;margin:0;padding:0;display:grid}
.claim{display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:center;gap:10px 16px;padding:14px 0;border-bottom:1px solid var(--rule)}
.claim .c-txt p{color:var(--ink);font-size:.98rem}
.claim .c-src{font-size:.82rem;color:var(--muted);display:grid;grid-template-rows:0fr;transition:grid-template-rows .35s var(--ease),opacity .35s var(--ease);opacity:0}
.claim .c-src span{overflow:hidden;min-height:0}
.claim.done .c-src{grid-template-rows:1fr;opacity:1;margin-top:4px}
.c-btn{min-height:40px;padding:0 16px;border-radius:999px;border:1px solid var(--glass-b);background:var(--glass);color:var(--ink);font:700 .85rem/1 var(--f-body);cursor:pointer;transition:transform .16s var(--ease),border-color .2s var(--ease)}
.c-btn:hover{border-color:var(--accent)}.c-btn:active{transform:scale(.96)}
.claim.busy .c-btn{pointer-events:none;color:var(--muted)}
.claim.busy .c-btn::before{content:"";display:inline-block;width:12px;height:12px;margin-right:8px;border-radius:50%;border:2px solid var(--accent);border-right-color:transparent;vertical-align:-1px;animation:spin .7s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.c-res{display:none;align-items:center;gap:6px;font:700 .8rem/1 var(--f-body);padding:9px 12px;border-radius:999px;white-space:nowrap;animation:pop .45s var(--spring)}
.c-res svg{width:14px;height:14px}
.c-res.ok{background:var(--accent-soft);color:var(--accent)}
.c-res.no{background:rgba(245,168,107,.14);color:var(--own)}
.claim.done .c-btn{display:none}
.claim.done[data-ok="1"] .c-res.ok,.claim.done[data-ok="0"] .c-res.no{display:inline-flex}
@keyframes pop{from{opacity:0;transform:scale(.85)}to{opacity:1;transform:none}}
.lead-foot{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-top:16px}
.sr{font-size:.85rem;color:var(--muted)}
/* E: bento de entrega */
.dbento{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.dbento .d1{grid-column:span 2;background:linear-gradient(150deg,color-mix(in srgb,var(--accent) 18%,var(--surface)),var(--surface) 70%)}
.dbento .cell{min-height:190px}
@media(max-width:900px){.dbento{grid-template-columns:1fr 1fr}.dbento .d1{grid-column:span 2}}
@media(max-width:560px){.dbento{grid-template-columns:1fr}.dbento .d1{grid-column:auto}}
/* F: faixa de tecnologias */
.marquee{margin-top:clamp(48px,6vw,72px)}
.marquee .lbl{display:flex;margin-bottom:18px}
.mq{overflow:hidden;-webkit-mask:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent);mask:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent)}
.mq-track{display:flex;gap:12px;width:max-content;animation:mq 48s linear infinite}
.mq:hover .mq-track{animation-play-state:paused}
.mq-track span{flex:none;font:500 1rem/1 var(--f-mono);padding:14px 20px;border-radius:999px;border:1px solid var(--glass-b);background:var(--glass);color:var(--ink)}
@keyframes mq{to{transform:translateX(calc(-50% - 6px))}}
@media(prefers-reduced-motion:reduce){.mq-track{animation:none;flex-wrap:wrap;width:auto;padding-inline:16px}.mq{-webkit-mask:none;mask:none}.mq-track span[aria-hidden]{display:none}.panel.enter .viewer,.panel.enter .info{animation:none}}
"""
rep('@media(prefers-reduced-transparency:reduce){', CSS_ADD + '@media(prefers-reduced-transparency:reduce){')

# ---------------- JS ----------------
# B: WebGL no lugar do 2D (2D fica como reserva)
rep("var stream=window.__s=(function(){var c=document.getElementById('stream'),x=c.getContext('2d'),",
    "var stream=window.__s=(function(){var c=document.getElementById('stream'),GL=webgl(c);if(GL)return GL;var x=c.getContext('2d'),")
WEBGL = r"""
function webgl(c){var g=c.getContext('webgl',{premultipliedAlpha:false,antialias:false,alpha:true});if(!g)return null;
 var vs='attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
 var fs='precision mediump float;uniform vec2 r;uniform float t;uniform vec3 ca;uniform vec3 cb;uniform float al;uniform float mob;'+
 'void main(){vec2 uv=gl_FragCoord.xy/r;float asp=r.x/r.y;vec3 col=vec3(0.);'+
 'float cx=mix(.62,.5,mob);'+
 'for(int i=0;i<9;i++){float fi=float(i);float k=fi/8.;'+
 'float y=.5+.17*sin(uv.x*2.1+t*.22+fi*.55)+.09*sin(uv.x*4.7-t*.31+fi*1.27)+(k-.5)*.42*(uv.x-.15)+(k-.5)*.08;'+
 'float d=abs(uv.y-y);float w=.0011+.0009*k;'+
 'float core=w/(d+w);float glow=exp(-d*d*700.)*.22;'+
 'float fade=smoothstep(.02,.4,uv.x)*(1.-smoothstep(.92,1.08,uv.x));'+
 'vec3 c=mix(cb,ca,smoothstep(.25,.85,uv.x+.08*sin(t*.2+fi)));'+
 'col+=c*(core*.55+glow)*fade*(.45+.55*sin(fi*1.7+1.));}'+
 'vec2 q=(uv-vec2(cx,.5))*vec2(asp*.7,1.);col+=ca*exp(-dot(q,q)*4.)*.16;'+
 'col*=al;gl_FragColor=vec4(col,clamp(max(max(col.r,col.g),col.b)*1.2,0.,1.));}';
 function sh(t,src){var s=g.createShader(t);g.shaderSource(s,src);g.compileShader(s);return g.getShaderParameter(s,g.COMPILE_STATUS)?s:null}
 var v=sh(g.VERTEX_SHADER,vs),f=sh(g.FRAGMENT_SHADER,fs);if(!v||!f)return null;var pr=g.createProgram();g.attachShader(pr,v);g.attachShader(pr,f);g.linkProgram(pr);
 if(!g.getProgramParameter(pr,g.LINK_STATUS))return null;g.useProgram(pr);
 var b=g.createBuffer();g.bindBuffer(g.ARRAY_BUFFER,b);g.bufferData(g.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),g.STATIC_DRAW);
 var lp=g.getAttribLocation(pr,'p');g.enableVertexAttribArray(lp);g.vertexAttribPointer(lp,2,g.FLOAT,false,0,0);
 var U={};['r','t','ca','cb','al','mob'].forEach(function(n){U[n]=g.getUniformLocation(pr,n)});
 var run=false,paused=false,raf=0,t0=performance.now(),tt=8000;
 function rgb(v){return v.split(',').map(function(n){return parseFloat(n)/255})}
 function recolor(){var s=getComputedStyle(r);var a=rgb(s.getPropertyValue('--stream-a')),bb=rgb(s.getPropertyValue('--stream-b'));g.uniform3f(U.ca,a[0],a[1],a[2]);g.uniform3f(U.cb,bb[0],bb[1],bb[2]);g.uniform1f(U.al,(parseFloat(s.getPropertyValue('--stream-alpha'))||1)*(cur()==='dark'?1:1.6));draw()}
 function size(){var dpr=Math.min(devicePixelRatio||1,innerWidth<700?1:1.25);c.width=c.clientWidth*dpr;c.height=c.clientHeight*dpr;g.viewport(0,0,c.width,c.height);g.uniform2f(U.r,c.width,c.height);g.uniform1f(U.mob,innerWidth<980?1:0);draw()}
 function draw(){g.uniform1f(U.t,tt/1000);g.clearColor(0,0,0,0);g.clear(g.COLOR_BUFFER_BIT);g.drawArrays(g.TRIANGLE_STRIP,0,4)}
 var last=0;function loop(ts){if(last)tt+=ts-last;last=ts;draw();raf=requestAnimationFrame(loop)}
 function start(){if(run||RM.matches||paused)return;run=true;last=0;raf=requestAnimationFrame(loop)}
 function stop(){run=false;cancelAnimationFrame(raf)}
 addEventListener('resize',size);
 new IntersectionObserver(function(e){e[0].isIntersecting?start():stop()}).observe(c);
 document.addEventListener('visibilitychange',function(){document.hidden?stop():start()});
 recolor();size();
 return {recolor:recolor,setPaused:function(p){paused=p;p?stop():start()},label:function(){}};
}
"""
rep("/* ---------- fluxo de luz (canvas) ---------- */", "/* ---------- fluxo de luz (WebGL, com reserva em 2D) ---------- */" + WEBGL)
# pausa global (substitui a do 2D)
rep(""" var pb=document.getElementById('pause');if(RM.matches)pb.hidden=true;
 pb.addEventListener('click',function(){paused=!paused;pb.setAttribute('aria-pressed',paused?'true':'false');pb.setAttribute('aria-label',paused?UI[lang].play:UI[lang].pause);paused?stop():start()});
 return {recolor:recolor,label:function(){pb.setAttribute('aria-label',paused?UI[lang].play:UI[lang].pause)}}})();""",
""" return {recolor:recolor,setPaused:function(p){paused=p;p?stop():start()},label:function(){}}})();
var pb=document.getElementById('pause'),allPaused=false;if(RM.matches)pb.hidden=true;
function pbLabel(){pb.setAttribute('aria-label',allPaused?UI[lang].play:UI[lang].pause)}
pb.addEventListener('click',function(){allPaused=!allPaused;r.classList.toggle('paused',allPaused);pb.setAttribute('aria-pressed',allPaused?'true':'false');pbLabel();stream.setPaused(allPaused)});""")
rep("paint();movePill(false);if(window.__s)__s.label()}", "paint();movePill(false);if(typeof pbLabel==='function')pbLabel()}")

# I: odômetro no lugar da contagem simples
rep("""function countUp(el){var to=parseFloat(el.getAttribute('data-to')),pre=el.getAttribute('data-pre')||'',suf=el.getAttribute('data-suf')||'',sp=el.querySelector('.v');
 if(RM.matches){sp.textContent=pre+to;return}var t0=null,dur=1400;
 function f(ts){if(!t0)t0=ts;var p=Math.min(1,(ts-t0)/dur),e=1-Math.pow(1-p,4);sp.textContent=pre+Math.round(to*e);if(p<1)requestAnimationFrame(f)}requestAnimationFrame(f)}""",
"""function countUp(el){var to=String(el.getAttribute('data-to')),pre=el.getAttribute('data-pre')||'',sp=el.querySelector('.v');
 if(RM.matches){sp.textContent=pre+to;return}
 var h=pre?'<span>'+pre+'</span>':'';to.split('').forEach(function(){h+='<span class="dg"><span class="col">'+'0123456789'.split('').map(function(d){return '<span>'+d+'</span>'}).join('')+'</span></span>'});
 sp.innerHTML='<span class="odo">'+h+'</span>';var cols=sp.querySelectorAll('.col');
 requestAnimationFrame(function(){requestAnimationFrame(function(){[].forEach.call(cols,function(c,i){c.style.transitionDelay=(i*90)+'ms';c.style.transform='translateY(-'+to[i]+'em)'})})})}""")

JS_ADD = r"""
/* ---------- I: luz que segue o cursor ---------- */
(function(){var sp=document.querySelector('.spot');if(!fine.matches||RM.matches)return;var x=0,y=0,q=false;
 addEventListener('pointermove',function(e){x=e.clientX;y=e.clientY;if(!q){q=true;requestAnimationFrame(function(){sp.style.setProperty('--sx',x+'px');sp.style.setProperty('--sy',y+'px');q=false})}sp.classList.add('on')},{passive:true});
 document.addEventListener('pointerleave',function(){sp.classList.remove('on')})})();
/* ---------- C: rolagem guiada ---------- */
(function(){var steps=[].slice.call(document.querySelectorAll('.sstep')),imgs=[].slice.call(document.querySelectorAll('.story-stage img')),bar=document.querySelector('.story-bar i');
 function show(i){steps.forEach(function(s,j){s.classList.toggle('on',j===i)});imgs.forEach(function(m,j){m.classList.toggle('on',j===i);if(j===i)m.loading='eager'});bar.style.setProperty('--sp',((i+1)/steps.length).toFixed(3))}
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)show(+e.target.getAttribute('data-i'))})},{rootMargin:'-45% 0px -45% 0px'});
 steps.forEach(function(s){io.observe(s)});
 imgs.forEach(function(m){m.loading='eager'})})();
/* ---------- D: demonstração do LeadScout ---------- */
(function(){var lead=document.getElementById('lead'),cl=[].slice.call(lead.querySelectorAll('.claim')),sc=document.getElementById('score'),sb=document.getElementById('scorebar'),live=document.getElementById('dmlive');
 var base=40,score=base;
 function setScore(v){score=v;sc.textContent=v;sb.style.setProperty('--s',(v/100).toFixed(2))}
 cl.forEach(function(c){var b=c.querySelector('.c-btn');b.addEventListener('click',function(){c.classList.add('busy');b.querySelector('.c-lab').textContent=D().dm_auditing;
  setTimeout(function(){c.classList.remove('busy');c.classList.add('done');b.querySelector('.c-lab').textContent=D().dm_check;var ok=c.getAttribute('data-ok')==='1';
   if(ok)setScore(Math.min(100,score+24));
   live.textContent=c.querySelector('.c-txt p').textContent+': '+(ok?D().dm_ok:D().dm_no)},RM.matches?0:900)})});
 document.getElementById('dmreset').addEventListener('click',function(){cl.forEach(function(c){c.classList.remove('done','busy')});setScore(base);live.textContent=''})})();
/* ---------- A + H: geração das telas e autoplay da galeria ---------- */
var genDone={};
function whenGen(cb){if(window.__gen)cb(window.__gen);else document.addEventListener('gen-ready',function(){cb(window.__gen)},{once:true})}
function genImg(img,opt){return new Promise(function(res){whenGen(function(g){(img.decode?img.decode():Promise.resolve()).catch(function(){}).then(function(){try{g(img,Object.assign({variant:'image',duration:2400},opt||{})).finished.then(res,res)}catch(e){res()}})})})}
function startAuto(p){if(RM.matches||p.getAttribute('data-userpick'))return;p.classList.add('auto')}
function genPanel(p){var id=p.id;if(genDone[id])return;genDone[id]=1;var im=p.querySelector('.stage img');im.loading='eager';genImg(im,{duration:2200}).then(function(){startAuto(p)})}
var projSec=document.getElementById('projetos');
new IntersectionObserver(function(es){es.forEach(function(e){projSec.classList.toggle('inview',e.isIntersecting);if(e.isIntersecting){var on=projSec.querySelector('.panel:not([hidden])');if(on)genPanel(on)}})},{threshold:.25}).observe(projSec);
document.addEventListener('tabshown',function(e){if(projSec.classList.contains('inview'))genPanel(e.detail)});
[].forEach.call(document.querySelectorAll('.panel'),function(p){p.addEventListener('animationend',function(e){if(!e.target.classList.contains('prog'))return;
 var th=[].slice.call(p.querySelectorAll('.thumb')),i=th.findIndex(function(t){return t.classList.contains('on')});var n=th[(i+1)%th.length];n.dataset.auto='1';n.click();delete n.dataset.auto})});
var heroImg=document.querySelector('.hero .browser img');if(!RM.matches)genImg(heroImg,{duration:2600,delay:250});
"""
rep("setLang(r.getAttribute('data-lang')==='en'?'en':'pt',false);\n})();", "setLang(r.getAttribute('data-lang')==='en'?'en':'pt',false);\n" + JS_ADD + "})();")
# tab shown event + user pick stops autoplay
rep("movePill(true);if(focus)t.focus();", "movePill(true);document.dispatchEvent(new CustomEvent('tabshown',{detail:document.getElementById(t.getAttribute('aria-controls'))}));if(focus)t.focus();")
rep(" [].forEach.call(p.querySelectorAll('.thumb'),function(th){th.addEventListener('click',function(){if(th.classList.contains('on'))return;",
    " [].forEach.call(p.querySelectorAll('.thumb'),function(th){th.addEventListener('click',function(){if(!th.dataset.auto){p.classList.remove('auto');p.setAttribute('data-userpick','1')}if(th.classList.contains('on'))return;")

# módulo da biblioteca de geração + CSS dela
rep('<link rel="preload" as="image"', '<link rel="stylesheet" href="vendor/ui-generation.css">\n<link rel="stylesheet" href="vendor/text-image-generation.css">\n<link rel="preload" as="image"')
rep('<script>{BODY_JS}</script>', '''<script type="module">import {{ generate }} from "./vendor/ui-generation.js"; window.__gen = generate; document.dispatchEvent(new Event("gen-ready"));</script>
<script>{BODY_JS}</script>''')
# nav: Demonstração
rep("""      <a class="nl" href="#como-funciona" {ti('nav_como')}>{tx('nav_como')}</a>""", """      <a class="nl" href="#demo" {ti('dm_k')}>{tx('dm_k')}</a>
      <a class="nl" href="#como-funciona" {ti('nav_como')}>{tx('nav_como')}</a>""")

open(p, "w", encoding="utf8").write(s)
print("ok")
