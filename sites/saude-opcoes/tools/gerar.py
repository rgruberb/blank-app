#!/usr/bin/env python3
"""Gera as 6 landings de saúde (uma por direção TPL-SAU) + índice. Uso: gerar.py <pasta-de-saida>"""
import sys, os, html

OUT = sys.argv[1]
FONTS = {
    1: "family=Arimo:wght@400;700",
    2: "family=Figtree:wght@400;600;700",
    3: "family=Inter:wght@400;600;700",
    4: "family=Manrope:wght@300;400;500;700",
    5: "family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans:wght@400;600&family=Schibsted+Grotesk:wght@600;700",
    6: "family=DM+Sans:opsz,wght@9..40,400;9..40,600;9..40,700",
}

BASE_CSS = r"""
*{box-sizing:border-box}
:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
html{scroll-behavior:smooth;scroll-padding-top:calc(80px + env(safe-area-inset-top,0px))}
body{margin:0;background:var(--bg);color:var(--ink-2);font:400 1rem/1.6 var(--f-body);-webkit-font-smoothing:antialiased}
@media(min-width:641px){body{font-size:1.1875rem;line-height:1.55}}
img{max-width:100%;display:block}
a{color:var(--link)}
:focus-visible{outline:3px solid var(--focus);outline-offset:3px}
h1,h2,h3{font-family:var(--f-head);color:var(--head);margin:0;text-wrap:balance;font-weight:var(--hw,700);letter-spacing:var(--track,-.01em)}
p{margin:0}
.w{max-width:1200px;margin-inline:auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
@media(min-width:768px){.w{padding-left:max(32px,env(safe-area-inset-left,0px));padding-right:max(32px,env(safe-area-inset-right,0px))}}
.skip{position:absolute;left:16px;top:-80px;z-index:40;background:var(--cta);color:var(--cta-ink);padding:12px 16px;font-weight:600}
.skip:focus{top:calc(8px + env(safe-area-inset-top,0px))}
.kicker{font:600 .8rem/1.3 var(--f-label);letter-spacing:.07em;text-transform:uppercase;color:var(--kicker)}
.prev{background:#1B2126;color:#E8ECEF;font:500 13px/1.4 system-ui,sans-serif}
.prev .w{display:flex;flex-wrap:wrap;justify-content:space-between;gap:4px 16px;padding-block:8px}
.prev a{color:#9CC8F5;display:inline-flex;align-items:center;min-height:28px}
/* topo */
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:31;background:var(--top-bg)}
.top{position:sticky;top:env(safe-area-inset-top,0px);z-index:30;background:var(--top-bg);border-bottom:1px solid var(--top-rule)}
.top .w{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:72px}
.brand{display:flex;align-items:center;gap:10px;font:700 1.15rem/1 var(--f-head);color:var(--top-ink);text-decoration:none;letter-spacing:-.01em}
.brand svg{width:30px;height:30px;flex:none}
.top nav{display:flex;align-items:center;gap:24px;font-size:1rem}
.top nav a{color:var(--top-ink);text-decoration:none}
.top nav a:hover{text-decoration:underline}
@media(max-width:860px){.top nav a.nl{display:none}}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 24px;font:600 1rem/1 var(--f-body);text-decoration:none;border-radius:var(--r);border:2px solid transparent;cursor:pointer;transition:transform .16s ease,background-color .15s ease}
.btn:active{transform:scale(.97)}
.btn.pri{background:var(--cta);color:var(--cta-ink);box-shadow:var(--cta-shadow,none)}
.btn.pri:hover{background:var(--cta-h)}
.btn.sec{background:transparent;color:var(--head);border-color:var(--rule-strong)}
.top nav .btn{min-height:44px;padding:0 18px;font-size:.95rem}
/* hero */
.hero{background:var(--hero-bg);color:var(--hero-ink);padding-block:clamp(48px,7vw,96px)}
.hero h1{color:var(--hero-head);font-size:clamp(2.2rem,1.5rem + 3vw,3.8rem);line-height:1.06;margin-top:16px;max-width:18ch}
.hero .kicker{color:var(--hero-kicker)}
.hero .sub{margin-top:20px;max-width:46ch;font-size:1.1em}
.hero .acts{margin-top:32px;display:flex;flex-wrap:wrap;gap:12px 20px;align-items:center}
.hero .fine{font-size:.85rem;opacity:.9}
.hero-grid{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:clamp(32px,5vw,72px);align-items:center}
@media(max-width:960px){.hero-grid{grid-template-columns:1fr}}
@media(prefers-reduced-motion:no-preference){
  .hero .mockup{animation:rise .6s cubic-bezier(.2,.7,.2,1) both .1s}
  @keyframes rise{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
}
/* maquete: próxima consulta (CMP-SAU-10) */
.mockup{min-width:0}
.mk{background:var(--mk-bg);color:var(--mk-ink);border:1px solid var(--mk-rule);border-radius:var(--r-card);box-shadow:var(--mk-shadow,none);padding:24px;display:grid;gap:16px;font-size:1rem;line-height:1.5}
.mk .tagx{font:600 .75rem/1.2 var(--f-label);letter-spacing:.06em;text-transform:uppercase;color:var(--mk-muted)}
.mk h3{font-size:1.25rem;color:var(--mk-head)}
.mk .when{font-variant-numeric:tabular-nums;font-weight:600;color:var(--mk-head);font-size:1.15rem}
.mk .who{font-size:.95rem;color:var(--mk-muted)}
.mk .row{display:flex;flex-wrap:wrap;gap:8px}
.mk .b{display:inline-flex;align-items:center;min-height:44px;padding:0 16px;border-radius:var(--r);font-weight:600;font-size:.95rem;border:2px solid var(--mk-rule);color:var(--mk-head)}
.mk .b.p{background:var(--cta);color:var(--cta-ink);border-color:var(--cta)}
.mk ul{list-style:none;margin:0;padding:0;display:grid;border-top:1px solid var(--mk-rule)}
.mk li{display:grid;grid-template-columns:4.2rem minmax(0,1fr) auto;gap:12px;align-items:center;padding:10px 0;border-bottom:1px solid var(--mk-rule);font-size:.95rem}
.mk li time{font-variant-numeric:tabular-nums;font-weight:600;color:var(--mk-head)}
.chip{display:inline-flex;align-items:center;gap:6px;font-size:.8rem;font-weight:600;padding:4px 10px;border-radius:999px;background:var(--chip-bg);color:var(--chip-ink);white-space:nowrap}
.chip.ok{background:var(--ok-bg);color:var(--ok-ink)}
.chip.warn{background:var(--warn-bg);color:var(--warn-ink)}
.chip.bad{background:var(--bad-bg);color:var(--bad-ink)}
/* seções */
section{padding-block:clamp(56px,8vw,112px)}
.band{background:var(--alt)}
.sh{max-width:720px;margin-bottom:clamp(32px,5vw,56px)}
.sh h2{font-size:clamp(1.95rem,1.4rem + 1.8vw,2.45rem);line-height:1.12;margin-top:12px}
.sh p{margin-top:16px;max-width:60ch}
/* prova social */
.stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px}
@media(max-width:900px){.stats{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:480px){.stats{grid-template-columns:1fr}}
.stat{border-top:var(--stat-line);padding-top:16px;display:grid;gap:6px;align-content:start}
.stat b{font:var(--hw-stat,700) clamp(1.95rem,1.5rem + 1.4vw,2.45rem)/1.05 var(--f-head);color:var(--head);letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.stat span{font-size:.95rem}
.case{margin-top:clamp(32px,5vw,48px);display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.4fr);gap:clamp(24px,4vw,48px);background:var(--surface);border:1px solid var(--rule);border-radius:var(--r-card);padding:clamp(24px,4vw,40px);align-items:start}
@media(max-width:860px){.case{grid-template-columns:1fr}}
.case h3{font-size:1.5rem;line-height:1.2;margin-top:10px}
.case p+p{margin-top:12px}
.case .src{font-size:.85rem;color:var(--muted)}
/* como funciona */
.steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;counter-reset:s}
@media(max-width:960px){.steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:560px){.steps{grid-template-columns:1fr}}
.steps li{counter-increment:s;display:grid;gap:10px;align-content:start;background:var(--step-bg);border:var(--step-border);border-radius:var(--r-card);padding:var(--step-pad)}
.steps li::before{content:counter(s);display:grid;place-items:center;width:44px;height:44px;border-radius:var(--num-r);background:var(--num-bg);color:var(--num-ink);font:700 1.15rem/1 var(--f-head);font-variant-numeric:tabular-nums}
.steps h3{font-size:1.25rem}
.steps p{font-size:.95em}
/* planos */
.plans{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;align-items:stretch}
@media(max-width:960px){.plans{grid-template-columns:1fr}}
.plan{background:var(--surface);border:1px solid var(--rule);border-radius:var(--r-card);padding:28px;display:flex;flex-direction:column;gap:14px;min-width:0}
.plan.hl{border:2px solid var(--cta);box-shadow:var(--plan-shadow,none)}
.plan .flag{align-self:flex-start;font:600 .75rem/1 var(--f-label);letter-spacing:.06em;text-transform:uppercase;background:var(--cta);color:var(--cta-ink);padding:6px 10px;border-radius:var(--r)}
.plan h3{font-size:1.5rem}
.plan .for{font-size:.95em;color:var(--muted)}
.plan .price{font:700 1.5rem/1.1 var(--f-head);color:var(--head)}
.plan .price small{display:block;font:400 .85rem/1.4 var(--f-body);color:var(--muted);margin-top:4px}
.plan ul{list-style:none;margin:0;padding:0;display:grid;gap:10px;font-size:.95em;flex:1}
.plan li{padding-left:28px;position:relative}
.plan li::before{content:"";position:absolute;left:2px;top:.45em;width:14px;height:8px;border-left:2.5px solid var(--check);border-bottom:2.5px solid var(--check);transform:rotate(-45deg)}
.plan .btn{width:100%}
.plans-note{margin-top:24px;font-size:.95rem;color:var(--muted);max-width:70ch}
/* FAQ */
.faq{max-width:820px;display:grid;border-top:1px solid var(--rule)}
.faq details{border-bottom:1px solid var(--rule)}
.faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;gap:16px;align-items:center;min-height:64px;padding-block:16px;font:600 1.1em/1.35 var(--f-head);color:var(--head)}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";flex:none;display:grid;place-items:center;width:32px;height:32px;border-radius:50%;border:2px solid var(--rule-strong);font:500 1.2rem/1 var(--f-body);color:var(--head)}
.faq details[open] summary::after{content:"−"}
.faq details p{padding-bottom:20px;max-width:64ch}
/* CTA final */
.final{background:var(--final-bg);color:var(--final-ink)}
.final h2{color:var(--final-head);font-size:clamp(2.2rem,1.5rem + 2.6vw,3.05rem);line-height:1.08;max-width:20ch;margin-top:12px}
.final .kicker{color:var(--final-kicker)}
.final p.l{margin-top:20px;max-width:52ch}
.final .acts{margin-top:32px;display:flex;flex-wrap:wrap;gap:12px 16px;align-items:center}
.final code{font:600 clamp(1.1rem,.95rem + .8vw,1.45rem)/1.3 var(--f-mono,ui-monospace,monospace);color:var(--final-head);user-select:all;-webkit-user-select:all;overflow-wrap:anywhere}
.final .btn.pri{background:var(--final-cta);color:var(--final-cta-ink)}
.final .btn.pri:hover{background:var(--final-cta);filter:brightness(1.08)}
.final .btn.sec{color:var(--final-head);border-color:var(--final-rule)}
.final .copied{min-height:1.5em;margin-top:12px;font-size:.95rem}
.final .human{margin-top:24px;font-size:.95rem;opacity:.9}
footer{background:var(--foot-bg);color:var(--foot-ink);font-size:.95rem;padding-block:32px}
footer .w{display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px 24px}
footer a{color:inherit}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation:none!important;transition:none!important}}
"""

THEMES = {
1: """
:root{color-scheme:light;--bg:#FFFFFF;--alt:#F0F4F5;--surface:#FFFFFF;--ink-2:#212B32;--muted:#4C6272;--head:#212B32;--rule:#D8DDE0;--rule-strong:#AEB7BD;
--link:#005EB8;--focus:#FFB81C;--kicker:#003087;--cta:#007F3B;--cta-h:#00662F;--cta-ink:#FFFFFF;--r:4px;--r-card:4px;
--f-head:"Arimo",Arial,sans-serif;--f-body:"Arimo",Arial,sans-serif;--f-label:"Arimo",Arial,sans-serif;
--top-bg:#005EB8;--top-ink:#FFFFFF;--top-rule:#005EB8;--hero-bg:#FFFFFF;--hero-ink:#212B32;--hero-head:#212B32;--hero-kicker:#003087;
--mk-bg:#F0F4F5;--mk-ink:#212B32;--mk-head:#212B32;--mk-muted:#4C6272;--mk-rule:#D8DDE0;
--chip-bg:#E8EDEE;--chip-ink:#212B32;--ok-bg:#E3F1E8;--ok-ink:#00401E;--warn-bg:#FFF4D1;--warn-ink:#5C4400;--bad-bg:#FBE3E1;--bad-ink:#8A1C12;
--stat-line:4px solid #005EB8;--step-bg:#FFFFFF;--step-border:1px solid #D8DDE0;--step-pad:24px;--num-bg:#005EB8;--num-ink:#FFFFFF;--num-r:50%;--check:#007F3B;
--final-bg:#003087;--final-ink:#E8EDF7;--final-head:#FFFFFF;--final-kicker:#C8D3EB;--final-cta:#FFFFFF;--final-cta-ink:#003087;--final-rule:rgba(255,255,255,.6);
--foot-bg:#F0F4F5;--foot-ink:#4C6272;--track:0}
.btn.pri{border-bottom:4px solid #00401E}
.top nav .btn.pri{background:#FFFFFF;color:#005EB8;border-bottom-color:#003087}
.top nav .btn.pri:hover{background:#E8F0F9}
.hero{border-bottom:1px solid #D8DDE0}
.mk{border-left:8px solid #005EB8}
.plan{border-top:6px solid #005EB8}
.plan.hl{border-top-width:6px}
.final .btn.pri{border-bottom-color:#AEB7BD}
""",
2: """
:root{color-scheme:light;--bg:#FFFFFF;--alt:#DFF9F2;--surface:#FFFFFF;--ink-2:#2A2623;--muted:#57504A;--head:#1E3A33;--rule:#E2DBD5;--rule-strong:#B6AEA5;
--link:#006A59;--focus:#27455C;--kicker:#006A59;--cta:#006A59;--cta-h:#00574A;--cta-ink:#FFFFFF;--r:999px;--r-card:20px;
--f-head:"Figtree",system-ui,sans-serif;--f-body:"Figtree",system-ui,sans-serif;--f-label:"Figtree",system-ui,sans-serif;
--top-bg:#FFFFFF;--top-ink:#1E3A33;--top-rule:#EEE8E3;--hero-bg:#006A59;--hero-ink:#DFF9F2;--hero-head:#FFFFFF;--hero-kicker:#B9EFE0;
--mk-bg:#FFFFFF;--mk-ink:#2A2623;--mk-head:#1E3A33;--mk-muted:#57504A;--mk-rule:#EEE8E3;--mk-shadow:0 18px 40px -16px rgba(0,40,33,.45);
--chip-bg:#EEE8E3;--chip-ink:#2A2623;--ok-bg:#DFF9F2;--ok-ink:#00463B;--warn-bg:#FFF1D6;--warn-ink:#5C4100;--bad-bg:#FBE4E1;--bad-ink:#8A1C12;
--stat-line:0;--step-bg:#FFFFFF;--step-border:0;--step-pad:28px;--num-bg:#DFF9F2;--num-ink:#006A59;--num-r:50%;--check:#006A59;
--final-bg:#EEE8E3;--final-ink:#2A2623;--final-head:#1E3A33;--final-kicker:#006A59;--final-cta:#006A59;--final-cta-ink:#FFFFFF;--final-rule:#B6AEA5;
--foot-bg:#FFFFFF;--foot-ink:#57504A;--plan-shadow:0 18px 40px -20px rgba(0,60,50,.35)}
.hero .btn.pri{background:#FFFFFF;color:#006A59}
.hero .btn.pri:hover{background:#DFF9F2}
.stat{background:#FFFFFF;border-radius:20px;padding:24px}
.band .case{border:0}
.plan{border-color:#EEE8E3}
""",
3: """
:root{color-scheme:light;--bg:#F5F7F8;--alt:#FFFFFF;--surface:#FFFFFF;--ink-2:#2F3B45;--muted:#56636E;--head:#27455C;--rule:#D8DDE0;--rule-strong:#9AA6AF;
--link:#005EB8;--focus:#005EB8;--kicker:#27455C;--cta:#005EB8;--cta-h:#004A93;--cta-ink:#FFFFFF;--r:6px;--r-card:8px;
--f-head:"Inter",system-ui,sans-serif;--f-body:"Inter",system-ui,sans-serif;--f-label:"Inter",system-ui,sans-serif;--track:-.02em;
--top-bg:#FFFFFF;--top-ink:#27455C;--top-rule:#D8DDE0;--hero-bg:#F5F7F8;--hero-ink:#2F3B45;--hero-head:#27455C;--hero-kicker:#56636E;
--mk-bg:#FFFFFF;--mk-ink:#2F3B45;--mk-head:#1F3547;--mk-muted:#56636E;--mk-rule:#E1E6E9;
--chip-bg:#EEF2F4;--chip-ink:#27455C;--ok-bg:#E3F1E8;--ok-ink:#0C5A2E;--warn-bg:#FFF4D1;--warn-ink:#5C4400;--bad-bg:#FBE3E1;--bad-ink:#8A1C12;
--stat-line:1px solid #9AA6AF;--step-bg:#F5F7F8;--step-border:1px solid #D8DDE0;--step-pad:24px;--num-bg:#27455C;--num-ink:#FFFFFF;--num-r:8px;--check:#005EB8;
--final-bg:#27455C;--final-ink:#D5DFE6;--final-head:#FFFFFF;--final-kicker:#A9BCCB;--final-cta:#FFFFFF;--final-cta-ink:#27455C;--final-rule:rgba(255,255,255,.5);
--foot-bg:#F5F7F8;--foot-ink:#56636E;--f-mono:"Inter",system-ui,sans-serif}
.mk table{width:100%;border-collapse:collapse;font-size:.9rem;font-variant-numeric:tabular-nums}
.mk th{text-align:left;font-weight:600;font-size:.78rem;letter-spacing:.04em;text-transform:uppercase;color:#56636E;padding:8px 8px 8px 0;border-bottom:1px solid #D8DDE0}
.mk td{padding:10px 8px 10px 0;border-bottom:1px solid #E1E6E9;vertical-align:middle}
.mk td:first-child{font-weight:600;color:#1F3547}
.mk .tw{overflow-x:auto}
""",
4: """
:root{color-scheme:dark;--bg:#0B0C0E;--alt:#101114;--surface:#151618;--ink-2:#C9CED3;--muted:#9AA2AA;--head:#F1F3F4;--rule:#26282C;--rule-strong:#3A3D42;
--link:#5FD3B0;--focus:#5FD3B0;--kicker:#2FB58F;--cta:#2FB58F;--cta-h:#3CC9A0;--cta-ink:#04130E;--r:12px;--r-card:16px;--hw:500;--hw-stat:300;--track:-.025em;
--f-head:"Manrope",system-ui,sans-serif;--f-body:"Manrope",system-ui,sans-serif;--f-label:"Manrope",system-ui,sans-serif;
--top-bg:#0B0C0E;--top-ink:#E3E6E8;--top-rule:#1D1F22;--hero-bg:#0B0C0E;--hero-ink:#C9CED3;--hero-head:#F1F3F4;--hero-kicker:#2FB58F;
--mk-bg:#151618;--mk-ink:#C9CED3;--mk-head:#F1F3F4;--mk-muted:#9AA2AA;--mk-rule:#26282C;--mk-shadow:0 0 0 1px rgba(47,181,143,.12),0 24px 60px -24px rgba(47,181,143,.35);
--chip-bg:#1F2124;--chip-ink:#C9CED3;--ok-bg:#12352A;--ok-ink:#7FE3C2;--warn-bg:#3A2C10;--warn-ink:#F2C66B;--bad-bg:#3A1714;--bad-ink:#FF9C90;
--stat-line:1px solid #2FB58F;--step-bg:#151618;--step-border:1px solid #26282C;--step-pad:28px;--num-bg:#12352A;--num-ink:#7FE3C2;--num-r:12px;--check:#2FB58F;
--final-bg:#151618;--final-ink:#C9CED3;--final-head:#F1F3F4;--final-kicker:#2FB58F;--final-cta:#2FB58F;--final-cta-ink:#04130E;--final-rule:#3A3D42;
--foot-bg:#0B0C0E;--foot-ink:#9AA2AA;--cta-shadow:0 0 28px -8px rgba(47,181,143,.6);--plan-shadow:0 0 40px -16px rgba(47,181,143,.45)}
.mk li{grid-template-columns:minmax(0,1fr) auto}
.mk .val{font-variant-numeric:tabular-nums;color:#F1F3F4;font-weight:500}
.final{border-top:1px solid #26282C}
""",
5: """
:root{color-scheme:light;--bg:#F2F4F3;--alt:#FFFFFF;--surface:#FFFFFF;--ink-2:#3A4540;--muted:#56625C;--head:#141C19;--rule:#D3DAD6;--rule-strong:#9AA7A0;
--link:#1D5A45;--focus:#1D5A45;--kicker:#56625C;--cta:#1D5A45;--cta-h:#164836;--cta-ink:#FFFFFF;--r:6px;--r-card:10px;--track:-.02em;
--f-head:"Schibsted Grotesk",system-ui,sans-serif;--f-body:"IBM Plex Sans",system-ui,sans-serif;--f-label:"IBM Plex Mono",ui-monospace,monospace;--f-mono:"IBM Plex Mono",ui-monospace,monospace;
--top-bg:#F2F4F3;--top-ink:#141C19;--top-rule:#D3DAD6;--hero-bg:#F2F4F3;--hero-ink:#3A4540;--hero-head:#141C19;--hero-kicker:#56625C;
--mk-bg:#FFFFFF;--mk-ink:#3A4540;--mk-head:#141C19;--mk-muted:#56625C;--mk-rule:#D3DAD6;--mk-shadow:0 1px 2px rgba(20,28,25,.06),0 16px 40px -18px rgba(20,28,25,.28);
--chip-bg:#E8ECEA;--chip-ink:#141C19;--ok-bg:#DDEBE5;--ok-ink:#164836;--warn-bg:#F7E6D9;--warn-ink:#7A3510;--bad-bg:#FBE3E1;--bad-ink:#8A1C12;
--stat-line:2px solid #141C19;--step-bg:transparent;--step-border:0;--step-pad:0;--num-bg:#DDEBE5;--num-ink:#1D5A45;--num-r:6px;--check:#1D5A45;
--final-bg:#141C19;--final-ink:#CDD6D1;--final-head:#FFFFFF;--final-kicker:#9FB0A8;--final-cta:#FFFFFF;--final-cta-ink:#141C19;--final-rule:rgba(255,255,255,.35);
--foot-bg:#F2F4F3;--foot-ink:#56625C}
.kicker{font-weight:500;font-size:.75rem;letter-spacing:.08em}
.hero h1 em{font-style:normal;color:#1D5A45}
.steps li{border-top:2px solid #141C19;padding-top:20px;border-radius:0}
""",
6: """
:root{color-scheme:light;--bg:#F7F5FC;--alt:#FFFFFF;--surface:#FFFFFF;--ink-2:#3D3354;--muted:#5E5474;--head:#2A1B47;--rule:#E4DDF3;--rule-strong:#B3A6D6;
--link:#5B3EC0;--focus:#7457D1;--kicker:#5B3EC0;--cta:#2A1B47;--cta-h:#3A2862;--cta-ink:#FFFFFF;--r:10px;--r-card:16px;--track:-.02em;
--f-head:"DM Sans",system-ui,sans-serif;--f-body:"DM Sans",system-ui,sans-serif;--f-label:"DM Sans",system-ui,sans-serif;
--top-bg:#F7F5FC;--top-ink:#2A1B47;--top-rule:#E4DDF3;--hero-bg:#F7F5FC;--hero-ink:#3D3354;--hero-head:#2A1B47;--hero-kicker:#5B3EC0;
--mk-bg:#FFFFFF;--mk-ink:#3D3354;--mk-head:#2A1B47;--mk-muted:#5E5474;--mk-rule:#E4DDF3;
--chip-bg:#ECE6FA;--chip-ink:#2A1B47;--ok-bg:#E3F1E8;--ok-ink:#0C5A2E;--warn-bg:#FDE8DA;--warn-ink:#7A3510;--bad-bg:#FBE3E1;--bad-ink:#8A1C12;
--stat-line:2px solid #7457D1;--step-bg:#FFFFFF;--step-border:1px solid #E4DDF3;--step-pad:28px;--num-bg:#ECE6FA;--num-ink:#5B3EC0;--num-r:12px;--check:#7457D1;
--final-bg:#2A1B47;--final-ink:#D9D0F0;--final-head:#FFFFFF;--final-kicker:#C7B8F2;--final-cta:#F26B1D;--final-cta-ink:#1E1030;--final-rule:rgba(255,255,255,.4);
--foot-bg:#F7F5FC;--foot-ink:#5E5474;--plan-shadow:0 20px 44px -22px rgba(42,27,71,.45)}
.hero h1 em{font-style:normal;color:#C24E0C}
.ill{display:grid;grid-template-columns:minmax(0,1fr) 56px minmax(0,1fr);align-items:center;gap:8px}
.ill .side{padding:20px;gap:10px}
.ill .phone{border-radius:24px;border-width:2px}
.ill .link{height:2px;background:repeating-linear-gradient(90deg,#7457D1 0 6px,transparent 6px 10px);position:relative}
.ill .link span{position:absolute;left:50%;top:-26px;transform:translateX(-50%);font-size:.7rem;color:#5B3EC0;white-space:nowrap;font-weight:600}
@media(max-width:560px){.ill{grid-template-columns:1fr}.ill .link{height:32px;width:2px;justify-self:center;background:repeating-linear-gradient(180deg,#7457D1 0 6px,transparent 6px 10px)}.ill .link span{top:50%;left:12px;transform:translateY(-50%)}}
.shots{position:relative;padding-bottom:6%}
.shots .desk{border-radius:12px;border:1px solid #E4DDF3;box-shadow:0 24px 50px -24px rgba(42,27,71,.45);width:100%;aspect-ratio:1500/938;object-fit:cover;object-position:top left;background:#fff}
.shots .phone{position:absolute;right:-2%;bottom:0;width:30%;border-radius:18px;border:1px solid #E4DDF3;box-shadow:0 24px 50px -20px rgba(42,27,71,.55);background:#fff}
.mk-note{margin-top:14px;font-size:.85rem;color:#5E5474}
""",
}

LOGOS = {
1: '<svg viewBox="0 0 30 30" aria-hidden="true"><rect width="30" height="30" fill="#FFFFFF"/><path d="M15 7v16M7 15h16" stroke="#005EB8" stroke-width="4"/></svg>',
2: '<svg viewBox="0 0 30 30" aria-hidden="true"><circle cx="15" cy="15" r="15" fill="#006A59"/><path d="M15 8v14M8 15h14" stroke="#fff" stroke-width="3.2" stroke-linecap="round"/></svg>',
3: '<svg viewBox="0 0 30 30" aria-hidden="true"><rect width="30" height="30" rx="7" fill="#27455C"/><path d="M6 16h5l2-5 4 9 2-4h5" fill="none" stroke="#fff" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/></svg>',
4: '<svg viewBox="0 0 30 30" aria-hidden="true"><rect width="30" height="30" rx="9" fill="#12352A"/><path d="M6 16h5l2-5 4 9 2-4h5" fill="none" stroke="#2FB58F" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/></svg>',
5: '<svg viewBox="0 0 26 26" aria-hidden="true"><rect x="1" y="1" width="24" height="24" rx="4" fill="#1D5A45"/><path d="M6 19V15h4v4M10 15v-4h4v4M14 11V7h4v4" fill="none" stroke="#fff" stroke-width="1.8" stroke-linejoin="round"/></svg>',
6: '<svg viewBox="0 0 30 30" aria-hidden="true"><rect width="30" height="30" rx="9" fill="#2A1B47"/><circle cx="11" cy="15" r="5" fill="#7457D1"/><circle cx="19" cy="15" r="5" fill="#F26B1D" fill-opacity=".9"/></svg>',
}

MOCK_CONSULTA = """
<div class="mk" role="img" aria-label="Exemplo de tela: próxima consulta com data, profissional e botões de reagendar e cancelar, e a agenda de hoje.">
  <p class="tagx">Exemplo de tela · dados fictícios</p>
  <div>
    <h3>Próxima consulta</h3>
    <p class="when">qua, 03/12/2026 · 14:30 <span style="font-weight:400;font-size:.85rem">(horário de Brasília)</span></p>
    <p class="who">Dra. Ana Exemplo · Dermatologia · CRM-RJ 000000</p>
  </div>
  <div class="row"><span class="b p">Confirmar presença</span><span class="b">Reagendar</span></div>
  <ul>
    <li><time>08:30</time><span>Retorno · J. S.</span><span class="chip ok">Confirmado</span></li>
    <li><time>09:15</time><span>Primeira consulta · M. A.</span><span class="chip warn">Aguardando</span></li>
    <li><time>10:00</time><span>Retorno · R. P.</span><span class="chip ok">Confirmado</span></li>
  </ul>
</div>"""

MOCK_TABELA = """
<div class="mk" role="img" aria-label="Exemplo de tela: agenda do dia por sala, com horário, paciente, tipo de atendimento e status.">
  <p class="tagx">Exemplo de tela · dados fictícios</p>
  <h3>Agenda de hoje · qua, 03/12/2026</h3>
  <div class="tw"><table>
    <thead><tr><th>Hora</th><th>Paciente</th><th>Sala</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>08:30</td><td>J. S.</td><td>2</td><td><span class="chip ok">Na recepção</span></td></tr>
      <tr><td>09:15</td><td>M. A.</td><td>1</td><td><span class="chip warn">Sem confirmação</span></td></tr>
      <tr><td>10:00</td><td>R. P.</td><td>2</td><td><span class="chip">Agendado</span></td></tr>
      <tr><td>10:45</td><td>L. C.</td><td>3</td><td><span class="chip">Agendado</span></td></tr>
    </tbody>
  </table></div>
</div>"""

MOCK_OPER = """
<div class="mk" role="img" aria-label="Exemplo de tela: guias de convênio com prazo e valor em risco, uma vencendo em 2 dias e uma negada.">
  <p class="tagx">Exemplo de tela · dados fictícios</p>
  <h3>Guias que precisam de alguém</h3>
  <ul>
    <li><span>Guia 1042 · Convênio A · ressonância<br><span class="val">R$ 1.240,00</span></span><span class="chip warn">▲ Vence em 2 dias</span></li>
    <li><span>Guia 1038 · Convênio B · consulta<br><span class="val">R$ 180,00</span></span><span class="chip bad">✕ Negada</span></li>
    <li><span>Guia 1031 · Convênio A · exame<br><span class="val">R$ 96,50</span></span><span class="chip ok">✓ Autorizada</span></li>
  </ul>
</div>"""

MOCK_W = """
<div class="ill" role="img" aria-label="Ilustração: a agência envia um conteúdo para aprovação e o médico aprova pelo celular; os dois veem o mesmo status.">
  <div class="mk side"><p class="tagx">Agência</p><h3>Conteúdo da semana</h3><p class="who">Vídeo curto · bastidores</p><span class="chip warn">Enviado para aprovação</span></div>
  <div class="link" aria-hidden="true"><span>mesmo dado</span></div>
  <div class="mk side phone"><p class="tagx">Médico, no celular</p><h3>1 conteúdo para aprovar</h3><div class="row"><span class="b p">Aprovar</span><span class="b">Comentar</span></div></div>
</div>
<p class="mk-note">Ilustração. As telas reais são mostradas na demonstração.</p>"""

MOCK_LISTA1 = """
<div class="mk" role="img" aria-label="Exemplo de tela: lembrete enviado ao paciente com data, hora e opção de confirmar.">
  <p class="tagx">Exemplo de tela · dados fictícios</p>
  <h3>Lembrete enviado ao paciente</h3>
  <p>Olá, Maria. Sua consulta é na <b>quarta, 03/12/2026, às 14:30</b> (horário de Brasília), com a Dra. Ana Exemplo, CRM-RJ 000000.</p>
  <div class="row"><span class="b p">Confirmar</span><span class="b">Preciso remarcar</span></div>
  <p class="who">Dúvidas: ligue para a recepção, (21) 0000-0000.</p>
</div>"""

RG_STEPS = [
 ("Conversa", "Você conta como a clínica funciona hoje: agenda, recepção, convênios e relatórios. Saímos com o problema escrito."),
 ("Protótipo", "Você vê e clica nas telas principais antes da construção, e a estimativa de prazo e custo vem junto."),
 ("Construção", "Construímos em ciclos curtos. A cada entrega, a equipe da clínica testa e opina."),
 ("Operação", "Colocamos no ar, treinamos a equipe e cuidamos de hospedagem, backups e ajustes."),
]
RG_PLANS = [
 ("Diagnóstico", "Para entender o problema antes de investir", ["Mapeamento do processo atual", "Protótipo clicável das telas principais", "Estimativa de prazo e custo por escrito"], False),
 ("Projeto", "Para construir o sistema da clínica", ["Sistema web sob medida, no computador e no celular", "Acesso por papéis e backups diários", "Treinamento da equipe", "Registro da marca no INPI"], True),
 ("Operação", "Para manter o sistema de pé, todo mês", ["Hospedagem e monitoramento", "Backups e atualizações de segurança", "Ajustes e pequenas melhorias", "Suporte por e-mail"], False),
]
RG_FAQ = [
 ("Vocês já fizeram sistema para clínica?", "Nossos três apps em produção são do setor de crédito. Em saúde, estamos construindo a Wonespace, um app para agências que cuidam da marca pessoal de médicos. O método é o mesmo: requisito, protótipo, produção e operação."),
 ("Como vocês cuidam dos dados dos pacientes?", "Dado de saúde é dado sensível pela LGPD (art. 5º, II). Usamos acesso por papéis, senhas com hash, conexão criptografada e backups. Quando o sistema coleta dado de saúde, o consentimento fica numa caixa própria, desmarcada, separada dos termos gerais."),
 ("Quanto custa?", "Depende do escopo. O Diagnóstico existe para isso: ao final, você recebe por escrito o prazo e o valor do Projeto e da Operação."),
 ("Quanto tempo leva?", "Depende do tamanho do sistema. Você recebe a estimativa junto com o protótipo, antes de decidir construir."),
 ("Funciona no celular?", "Sim. Os sistemas são web e funcionam no navegador do computador e do celular, sem instalar nada."),
 ("Vocês registram a marca do sistema?", "Sim. No plano Projeto, registramos a marca do seu sistema no INPI."),
]
RG_STATS = [("3 apps", "em produção, construídos do requisito ao deploy"), ("mar/2026", "no ar desde então, em uso diário"), ("+200%", "de produtividade em prospecção e gestão de carteira"), ("INPI", "registramos a marca do seu sistema")]
RG_CASE = ("Caso em produção · crédito e recebíveis", "Carteira360: agenda, rotas de visita e alertas para uma equipe comercial",
 ["Construímos para uma empresa de crédito (FIDC) um app que organiza a agenda e as rotas de visita e avisa quando um cliente parou de operar. O gestor vê a equipe toda; o gerente vê a própria carteira, no computador ou no celular.",
  "É o mesmo problema de uma clínica com muitos pacientes: ninguém pode ficar esquecido."],
 "O cliente não é identificado. Números informados pelo próprio uso em produção.")

W_STEPS = [
 ("Conversa", "Você mostra como a agência trabalha hoje com os médicos: pautas, gravações, aprovações e entregas."),
 ("Configuração", "Cadastramos a agência, a equipe e os médicos, com os projetos e etapas que vocês já usam."),
 ("Piloto", "Começamos com um ou dois médicos. A agência usa no dia a dia e nós ajustamos o que precisar."),
 ("Rotina", "Toda a carteira entra no app. O médico aprova pelo celular e a agência acompanha prazos e resultados."),
]
W_PLANS = [
 ("Piloto", "Para testar com poucos médicos", ["Um ou dois médicos", "Configuração feita por nós", "Acompanhamento próximo", "Ajustes durante o piloto"], False),
 ("Agência", "Para toda a carteira de médicos", ["Todos os médicos da agência", "App do médico no celular", "Produção, aprovação e mensagens", "Métricas por médico"], True),
 ("Rede", "Para várias agências ou unidades", ["Várias equipes no mesmo lugar", "Acesso por papéis", "Relatórios consolidados", "Suporte prioritário"], False),
]
W_FAQ = [
 ("O que é a Wonespace?", "Um app de gestão para agências que produzem conteúdo para a marca pessoal de médicos. A agência e o médico trabalham no mesmo dado: o que um faz aparece para o outro, em tempo real."),
 ("O médico precisa instalar alguma coisa?", "O médico usa pelo celular, com uma tela simples para aprovar, responder e ver o que está pendente."),
 ("A Wonespace já está pronta?", "Ainda não. É um produto próprio em construção. Agências interessadas podem ver uma demonstração ao vivo e entrar no piloto. A demonstração é feita com acordo de confidencialidade."),
 ("Como ficam os dados dos médicos e pacientes?", "O app é para conteúdo de marca, não para prontuário. Mesmo assim, usamos acesso por papéis e senhas com hash, e nada é compartilhado com terceiros."),
 ("Quanto custa?", "Os preços serão definidos no lançamento. No piloto, combinamos as condições por escrito antes de começar."),
 ("O app ajuda com as regras de publicidade médica?", "O fluxo de aprovação garante que o médico veja e aprove cada conteúdo antes de publicar. A responsabilidade pelo que é publicado continua do médico, conforme as normas do CFM."),
]
W_STATS = [("2 lados", "agência e médico no mesmo dado, em tempo real"), ("Celular", "o médico aprova e responde de onde estiver"), ("3 apps", "em produção feitos pela mesma equipe (RG AI)"), ("mar/2026", "desde quando a equipe mantém apps em uso diário")]
W_CASE = ("Feito por quem já tem apps em produção", "A RG AI construiu três apps que estão em uso diário desde março de 2026",
 ["A Wonespace é o produto próprio da RG AI. A mesma equipe construiu, do requisito ao deploy, três aplicações de crédito em produção, com +200% de produtividade nos processos atendidos.",
  "Na demonstração, mostramos o app funcionando, com dados fictícios, numa conversa de 30 minutos."],
 "Produto em construção. Demonstração ao vivo, com acordo de confidencialidade.")

OPTS = {
1: dict(tpl="TPL-SAU-01", nome="Sistema público claro", brand="RG AI Saúde",
  kicker="Sistemas para clínicas e consultórios", h1="Agenda, lembretes e relatórios da sua clínica no mesmo lugar",
  sub="Construímos o sistema da sua clínica sob medida e cuidamos dele depois de pronto.", cta="Agendar uma conversa", mock=MOCK_LISTA1, w=False),
2: dict(tpl="TPL-SAU-02", nome="Marketplace acolhedor", brand="RG AI Saúde",
  kicker="Para clínicas e consultórios", h1="Sua clínica com agenda online e menos telefone tocando",
  sub="Um sistema feito para a rotina da sua equipe, do agendamento ao relatório do mês.", cta="Agendar uma conversa", mock=MOCK_CONSULTA, w=False),
3: dict(tpl="TPL-SAU-03", nome="Clínico profissional", brand="RG AI Saúde",
  kicker="Software clínico sob medida", h1="O sistema da sua clínica, desenhado com a sua equipe",
  sub="Agenda, recepção e indicadores com dados organizados, acesso por papéis e backups diários.", cta="Agendar uma conversa", mock=MOCK_TABELA, w=False),
4: dict(tpl="TPL-SAU-04", nome="Operação clínica escura", brand="RG AI Saúde",
  kicker="Back-office de saúde", h1="Autorizações, convênios e fila sob controle",
  sub="Painéis para a operação da clínica enxergar prazos e guias paradas antes que virem prejuízo.", cta="Agendar uma conversa", mock=MOCK_OPER, w=False),
5: dict(tpl="TPL-SAU-02 · marca RG AI", nome="Acolhedor com a marca RG AI", brand="RG AI",
  kicker="Apps sob medida para saúde", h1='Apps sob medida para clínicas, do requisito <em>à produção</em>',
  sub="A mesma equipe que tem três apps em produção, agora para a rotina da sua clínica.", cta="Agendar uma conversa", mock=MOCK_CONSULTA, w=False),
6: dict(tpl="TPL-SAU-02 · marca Wonespace", nome="Acolhedor com a marca Wonespace", brand="Wonespace",
  kicker="Para agências de marca pessoal de médicos", h1='Agência e médico no <em>mesmo app</em>, em tempo real',
  sub="Pauta, gravação, aprovação e publicação num lugar só. O médico aprova pelo celular.", cta="Agendar uma demonstração", mock=MOCK_W, w=True),
}

def esc(s): return html.escape(s, quote=True)

def page(n):
    o = OPTS[n]; w = o["w"]
    steps, plans, faq, stats, case = (W_STEPS, W_PLANS, W_FAQ, W_STATS, W_CASE) if w else (RG_STEPS, RG_PLANS, RG_FAQ, RG_STATS, RG_CASE)
    if n == 4:
        steps = [("Conversa", "Você mostra onde a operação trava: autorizações, guias, glosas, fila da central."),
                 ("Protótipo", "Você vê e clica nos painéis principais antes da construção, com estimativa de prazo e custo."),
                 ("Construção", "Ligamos o painel às planilhas e sistemas que a clínica já usa, em ciclos curtos."),
                 ("Operação", "Colocamos no ar, treinamos a equipe e cuidamos de hospedagem, backups e ajustes.")]
    h1_plain = o["h1"].replace("<em>", "").replace("</em>", "")
    title = f'{o["brand"]} · Opção {n}'
    desc = o["sub"]
    stat_html = "".join(f'<div class="stat"><b>{esc(a)}</b><span>{esc(b)}</span></div>' for a, b in stats)
    step_html = "".join(f'<li><h3>{esc(a)}</h3><p>{esc(b)}</p></li>' for a, b in steps)
    plan_html = ""
    for nm, fr, items, hl in plans:
        lis = "".join(f"<li>{esc(i)}</li>" for i in items)
        flag = '<span class="flag">Recomendado</span>' if hl else ""
        cls = "plan hl" if hl else "plan"
        bcls = "btn pri" if hl else "btn sec"
        plan_html += f'<article class="{cls}">{flag}<h3>{esc(nm)}</h3><p class="for">{esc(fr)}</p><p class="price">Sob consulta<small>{"definido no lançamento" if w else "valor enviado por escrito"}</small></p><ul>{lis}</ul><a class="{bcls}" href="#contato">{esc(o["cta"])}</a></article>'
    faq_html = "".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faq)
    case_p = "".join(f"<p>{esc(p)}</p>" for p in case[2])
    if w:
        case_side = '<p class="kicker">' + esc(case[0]) + '</p><h3>' + esc(case[1]) + '</h3>'
    else:
        case_side = '<p class="kicker">' + esc(case[0]) + '</p><h3>' + esc(case[1]) + '</h3>'
    plans_note = ("A Wonespace está em construção. As condições do piloto são combinadas por escrito antes de começar."
                  if w else "Os valores dependem do escopo e são enviados por escrito depois do Diagnóstico. Sem cobrança automática e sem fidelidade escondida.")
    final_h = "Quer ver a Wonespace funcionando?" if w else "Vamos conversar sobre a sua clínica."
    final_p = ("Mande um e-mail contando quantos médicos a agência atende. Respondemos com um horário para a demonstração."
               if w else "Mande um e-mail contando o que hoje toma mais tempo da sua equipe. Respondemos com um horário para conversar.")
    fonts = FONTS[n]
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(h1_plain)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{",".join('{"@type":"Question","name":' + _j(q) + ',"acceptedAnswer":{"@type":"Answer","text":' + _j(a) + '}}' for q, a in faq)}]}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
<style>{BASE_CSS}{THEMES[n]}</style>
</head>
<body>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<div class="prev"><div class="w"><span>Prévia · Opção {n} de 6 · {esc(o["tpl"])} · {esc(o["nome"])}</span><a href="index.html">Ver as 6 opções</a></div></div>
<header class="top">
  <div class="w">
    <a class="brand" href="#conteudo">{LOGOS[n]}{esc(o["brand"])}</a>
    <nav aria-label="Seções">
      <a class="nl" href="#como-funciona">Como funciona</a>
      <a class="nl" href="#planos">Planos</a>
      <a class="nl" href="#duvidas">Dúvidas</a>
      <a class="btn pri" href="#contato">{esc(o["cta"])}</a>
    </nav>
  </div>
</header>
<main id="conteudo">
  <div class="hero">
    <div class="w hero-grid">
      <div>
        <p class="kicker">{esc(o["kicker"])}</p>
        <h1>{o["h1"]}</h1>
        <p class="sub">{esc(o["sub"])}</p>
        <div class="acts"><a class="btn pri" href="#contato">{esc(o["cta"])}</a><span class="fine">{"Resposta por e-mail, sem compromisso." }</span></div>
      </div>
      <div class="mockup">{o["mock"]}</div>
    </div>
  </div>

  <section class="band" id="prova" aria-labelledby="h-prova">
    <div class="w">
      <div class="sh"><p class="kicker">Prova social</p><h2 id="h-prova">{"O que já está no ar" if not w else "Por que confiar na Wonespace"}</h2></div>
      <div class="stats">{stat_html}</div>
      <div class="case"><div>{case_side}</div><div>{case_p}<p class="src">{esc(case[3])}</p></div></div>
    </div>
  </section>

  <section id="como-funciona" aria-labelledby="h-como">
    <div class="w">
      <div class="sh"><p class="kicker">Como funciona</p><h2 id="h-como">Quatro etapas, da conversa {"à rotina da agência" if w else "ao sistema no ar"}</h2></div>
      <ol class="steps">{step_html}</ol>
    </div>
  </section>

  <section class="band" id="planos" aria-labelledby="h-planos">
    <div class="w">
      <div class="sh"><p class="kicker">Preços e planos</p><h2 id="h-planos">{"Comece pelo piloto" if w else "Comece pequeno, cresça com a clínica"}</h2></div>
      <div class="plans">{plan_html}</div>
      <p class="plans-note">{esc(plans_note)}</p>
    </div>
  </section>

  <section id="duvidas" aria-labelledby="h-faq">
    <div class="w">
      <div class="sh"><p class="kicker">Dúvidas</p><h2 id="h-faq">Perguntas frequentes</h2></div>
      <div class="faq">{faq_html}</div>
    </div>
  </section>

  <section class="final" id="contato" aria-labelledby="h-final">
    <div class="w">
      <p class="kicker">Contato</p>
      <h2 id="h-final">{esc(final_h)}</h2>
      <p class="l">{esc(final_p)}</p>
      <div class="acts">
        <code id="mail">rafael@gruberia.com</code>
        <button class="btn pri" id="copy" type="button">Copiar e-mail</button>
        <a class="btn sec" href="https://www.linkedin.com/in/rafaelgruberbernstein" target="_blank" rel="noopener">LinkedIn</a>
      </div>
      <p class="copied" id="copied" role="status" aria-live="polite"></p>
    </div>
  </section>
</main>
<footer><div class="w"><span>{"Wonespace · produto da RG AI Ltda" if w else "RG AI Ltda · Rafael Gruber Bernstein"}</span><span>Telas de exemplo com dados fictícios. Sem promessa de resultado.</span></div></footer>
<script>
(function(){{var b=document.getElementById('copy'),m=document.getElementById('copied'),e=document.getElementById('mail');
function sel(){{try{{var r=document.createRange();r.selectNodeContents(e);var s=getSelection();s.removeAllRanges();s.addRange(r)}}catch(x){{}}}}
b.addEventListener('click',function(){{var t=e.textContent.trim();function ok(){{m.textContent='E-mail copiado.';setTimeout(function(){{m.textContent=''}},2500)}}function no(){{sel();m.textContent='E-mail selecionado. Use Ctrl+C ou Cmd+C para copiar.'}}try{{navigator.clipboard.writeText(t).then(ok,no)}}catch(x){{no()}}}});}})();
</script>
</body>
</html>
"""

import json
def _j(s): return json.dumps(s, ensure_ascii=False)

for n in OPTS:
    open(os.path.join(OUT, f"opcao-{n}.html"), "w", encoding="utf-8").write(page(n))
print("ok")
