#!/usr/bin/env python3
"""Cartões genéricos no hero, 'ligar' em sequência (linhas dos projetos + a–e), fundo discreto,
contador crescente, escuro sempre por padrão, entradas voltam ao chegar no topo."""
import sys, re, json
p = sys.argv[1]
s = open(p, encoding="utf8").read()

def rep(old, new):
    global s
    assert old in s, "não achei: " + old[:100]
    s = s.replace(old, new, 1)

# ---------- textos ----------
rep(' "fl1": ("Em produção", "In production"), "fl1b": ("Retreino diário", "Daily retraining"),',
    ' "fl1": ("3 aplicações", "3 applications"), "fl1b": ("em produção", "in production"),\n "fl3": ("Uso diário", "Daily use"), "fl3b": ("desde mar/2026", "since Mar 2026"),')
rep(' "m4v": ("mar/2026", "Mar 2026"),', ' "m4v": ("mar/2026", "Mar 2026"), "m4p": ("mar/", "Mar "),')

# ---------- cartões flutuantes do herói ----------
a = s.index('        <div class="float fB" aria-hidden="true">')
b = s.index('</div>\n', s.index('</span></span>', a)) + len('</div>\n')
fb = s[a:b]
fc = ('        <div class="float fC" aria-hidden="true"><span class="ic"><svg viewBox="0 0 24 24"><rect x="4" y="5.5" width="16" height="14" rx="3" fill="none" stroke="currentColor" stroke-width="2"/>'
      '<path d="M4 10h16M9 3.5v4M15 3.5v4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>'
      "<span><b {ti('fl3')}>{tx('fl3')}</b><span {ti('fl3b')}>{tx('fl3b')}</span></span></div>\n")
s = s[:b] + fc + s[b:]
rep(".fB{right:-18px;top:28%;animation:bob 7s var(--ease-io) -2s infinite}",
    ".fB{right:-18px;top:28%;animation:bob 7s var(--ease-io) -2s infinite}\n.fC{left:-22px;top:-24px;animation:bob 8s var(--ease-io) -4s infinite}")
rep(":root.paused .mq-track,:root.paused .fA,:root.paused .fB,", ":root.paused .mq-track,:root.paused .fA,:root.paused .fB,:root.paused .fC,")
rep("@media(max-width:980px){.fA{left:8px}.fB{right:8px}}", "@media(max-width:980px){.fA{left:8px}.fB{right:8px}.fC{left:8px;top:-18px}}")

# ---------- métrica 4 com ano contando ----------
rep("""<div class="metric"><span class="n"><span {ti('m4v')}>{tx('m4v')}</span></span>""",
    """<div class="metric"><span class="n" data-to="2026" data-from="2000"><span {ti('m4p')}>{tx('m4p')}</span><span class="v">2026</span></span>""")

# ---------- fundo mais discreto ----------
rep("'for(int i=0;i<9;i++){float fi=float(i);float k=fi/8.;'+", "'for(int i=0;i<5;i++){float fi=float(i);float k=fi/4.;'+")
rep("col+=ca*exp(-dot(q,q)*4.)*.16;'+", "col+=ca*exp(-dot(q,q)*4.)*.08;'+")
rep("'col*=al;gl_FragColor", "'col*=al*.5;gl_FragColor")
rep("var last=0;function loop(ts){if(last)tt+=ts-last;", "var last=0;function loop(ts){if(last)tt+=(ts-last)*.55;")
rep("opacity:.9;top:-10%}", "opacity:.45;top:-10%}")
rep(':root[data-theme="light"] .amb::before{opacity:.6}', ':root[data-theme="light"] .amb::before{opacity:.3}')
rep("rgba(61,220,168,.06),transparent 70%)}", "rgba(61,220,168,.03),transparent 70%)}")

# ---------- escuro sempre por padrão ----------
rep("try{var th=localStorage.getItem('rgai-theme3');if(th==='light')r.setAttribute('data-theme','light');var l=", "try{var l=")
rep("try{localStorage.setItem('rgai-theme3',n)}catch(e){}paint();", "paint();")

# ---------- CSS: linhas que acendem e estados 'aceso' ----------
rep(""".tline::before{content:"";position:absolute;left:6px;right:calc(33.3% - 6px);top:6px;height:2px;background:var(--accent)}""",
    """.tline::before,.tline::after{content:"";position:absolute;left:6px;width:66.6%;top:6px;height:2px}
.tline::before{background:var(--glass-2)}
.tline::after{background:var(--accent);transform-origin:left;transform:scaleX(var(--tp,1));transition:transform .8s var(--ease)}""")
rep(""".tline li::before{content:"";position:absolute;left:0;top:0;width:14px;height:14px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 3px var(--bg)}""",
    """.tline li::before{content:"";position:absolute;z-index:1;left:0;top:0;width:14px;height:14px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 3px var(--bg);transition:background-color .4s var(--ease),box-shadow .4s var(--ease),border-color .4s var(--ease)}
.tline li span{transition:opacity .4s var(--ease)}
.js .tline li:not(.on):not(.wip)::before{background:var(--bg-2);box-shadow:0 0 0 3px var(--bg),inset 0 0 0 2px var(--glass-b)}
.js .tline li:not(.on) span{opacity:.45}
.tline li.on::before{box-shadow:0 0 0 3px var(--bg),0 0 16px -2px var(--accent)}
.tline li.cur::before{animation:lit .9s var(--ease)}
.tline li.wip.pulse::before{animation:wip 1.4s var(--ease-io) infinite}
.tline li.wip.pulse span{opacity:1}
@keyframes wip{50%{transform:scale(1.25);opacity:.55}}""")
rep(".tline:has(.wip)::before{right:calc(66.6% - 6px)}", "")
rep(".badges span{", ".badges span{transition:opacity .45s var(--ease),background-color .45s var(--ease),color .45s var(--ease),border-color .45s var(--ease);")
CSS_LIT = r"""
/* 'ligar' em sequência (a–e) */
.js .badges span:not(.lit){opacity:.4;background:transparent;color:var(--muted);border-color:var(--glass-b)}
.badges span.lit{box-shadow:0 0 18px -8px var(--accent)}
.js .metric:not(.in) .meter i{transform:scaleX(0)}
.cell .ico{transition:background-color .5s var(--ease),color .5s var(--ease),box-shadow .5s var(--ease)}
.cell.lit{border-color:color-mix(in srgb,var(--accent) 55%,transparent)}
.cell.lit .ico{background:var(--accent);color:var(--accent-ink);box-shadow:0 0 24px -6px var(--accent)}
.chips span{transition:border-color .45s var(--ease),color .45s var(--ease),background-color .45s var(--ease)}
.chips span.lit{border-color:var(--accent);color:var(--accent);background:var(--accent-soft)}
.crow .ic{transition:background-color .45s var(--ease),color .45s var(--ease)}
.crow.lit .ic{background:var(--accent-ink);color:var(--accent)}
"""
rep('@media(prefers-reduced-transparency:reduce){', CSS_LIT + '@media(prefers-reduced-transparency:reduce){')

# ---------- JS: contador crescente + grupos que acendem + linhas dos projetos + replay no topo ----------
a = s.index("function countUp(el){")
b = s.index("[].forEach.call(document.querySelectorAll('.rv'),function(el){el.classList.remove('rv')});")
s = s[:a] + r"""function countUp(el){var to=+el.getAttribute('data-to'),from=+(el.getAttribute('data-from')||0),pre=el.getAttribute('data-pre')||'',v=el.querySelector('.v');
 cancelAnimationFrame(el._r);if(RM.matches){v.textContent=pre+to;return}var t0=null,d=1500;
 function f(ts){if(!t0)t0=ts;var p=Math.min(1,(ts-t0)/d),e=1-Math.pow(1-p,3);v.textContent=pre+Math.round(from+(to-from)*e);if(p<1)el._r=requestAnimationFrame(f)}el._r=requestAnimationFrame(f)}
function resetNum(el){cancelAnimationFrame(el._r);el.querySelector('.v').textContent=(el.getAttribute('data-pre')||'')+(el.getAttribute('data-from')||0)}
""" + s[b:]
# revelação: vira função que pode ser rearmada
rep(" els.forEach(function(el){var rc=el.getBoundingClientRect();if(rc.top<innerHeight*.9)return;",
    " function arm(){els.forEach(function(el){var rc=el.getBoundingClientRect();if(rc.top<innerHeight*.9)return;")
rep("  el.style.setProperty('--d',(i*80)+'ms');el.classList.add('rv2');io.observe(el)})})();",
    "  el.style.setProperty('--d',(i*80)+'ms');el.classList.remove('in');el.classList.add('rv2');io.observe(el)})}arm();window.__rearm=arm})();")
# grupos que acendem uma vez (a, b, d, e) — substitui o observador antigo dos números
rep("[].forEach.call(document.querySelectorAll('.metric'),function(el){var rc=el.getBoundingClientRect();if(rc.top<innerHeight*.92){el.classList.add('in');[].forEach.call(el.querySelectorAll('[data-to]'),countUp)}else seen.observe(el)});",
r"""var GROUPS=[
 {sel:'.metrics .w',kids:'.metric',on:function(el){el.classList.add('in');var n=el.querySelector('[data-to]');if(n)countUp(n)},off:function(el){el.classList.remove('in');var n=el.querySelector('[data-to]');if(n)resetNum(n)},step:380},
 {sel:'.bento',kids:'.cell',step:420},{sel:'.founder .chips',kids:'span',step:350},{sel:'.cta-card',kids:'.crow',step:420}];
var gio=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;gio.unobserve(e.target);lightGroup(e.target.__g)})},{threshold:.35});
function lightGroup(g){var kids=[].slice.call(g.el.querySelectorAll(g.kids));g.timers=(g.timers||[]);kids.forEach(function(k,i){g.timers.push(setTimeout(function(){k.classList.add('lit');if(g.on)g.on(k)},RM.matches?0:150+i*g.step))})}
function resetGroup(g){(g.timers||[]).forEach(clearTimeout);g.timers=[];[].forEach.call(g.el.querySelectorAll(g.kids),function(k){k.classList.remove('lit');if(g.off)g.off(k)});gio.observe(g.el)}
GROUPS.forEach(function(g){g.el=document.querySelector(g.sel);if(!g.el)return;g.el.__g=g;if(g.off)[].forEach.call(g.el.querySelectorAll(g.kids),g.off);gio.observe(g.el)});""")

JS_TL = r"""
/* ---------- linhas dos projetos: acendem em sequência, em loop; selos acendem ao abrir a aba ---------- */
var tlT=0,tlK=0,tlCur=null,tlIn=false;
function tlSet(tl,k){var lis=[].slice.call(tl.querySelectorAll('li')),max=lis.filter(function(l){return !l.classList.contains('wip')}).length;
 lis.forEach(function(li,i){li.classList.toggle('on',i<k&&!li.classList.contains('wip'));li.classList.toggle('cur',i===k-1&&!li.classList.contains('wip'))});
 tl.style.setProperty('--tp',(k<1?0:Math.min(k-1,lis.length-1)/(lis.length-1)).toFixed(3));var w=tl.querySelector('.wip');if(w)w.classList.toggle('pulse',k>max)}
function tlTick(){clearTimeout(tlT);var tl=document.querySelector('.panel:not([hidden]) .tline');if(!tl)return;
 if(RM.matches){tlSet(tl,3);return}if(!tlIn||r.classList.contains('paused'))return;
 if(tl!==tlCur){tlCur=tl;tlK=0}tlK=tlK>=3?0:tlK+1;tlSet(tl,tlK);tlT=setTimeout(tlTick,tlK>=3?1900:(tlK===0?550:950))}
[].forEach.call(document.querySelectorAll('.tline'),function(tl){tlSet(tl,RM.matches?3:0)});
function lightBadges(p){var b=[].slice.call(p.querySelectorAll('.badges span'));b.forEach(function(x){clearTimeout(x._t);x.classList.remove('lit')});
 b.forEach(function(x,i){x._t=setTimeout(function(){x.classList.add('lit')},RM.matches?0:400+i*420)})}
new IntersectionObserver(function(e){tlIn=e[0].isIntersecting;clearTimeout(tlT);if(tlIn){tlK=0;tlTick();var on=projSec.querySelector('.panel:not([hidden])');if(on&&!on._badged){on._badged=1;lightBadges(on)}}},{threshold:.25}).observe(projSec);
document.addEventListener('tabshown',function(e){tlK=0;tlCur=null;tlTick();e.detail._badged=1;lightBadges(e.detail)});
/* ---------- ao voltar ao topo, as entradas tocam de novo ---------- */
var away=false;
addEventListener('scroll',function(){if(scrollY>innerHeight*.6)away=true;else if(scrollY<=2&&away){away=false;replay()}},{passive:true});
function replay(){if(RM.matches)return;
 [].forEach.call(document.querySelectorAll('.hero h1 .ln>span,.hero .fade-in,.hero .browser,.brand .mk i'),function(el){el.style.animation='none';void el.offsetWidth;el.style.animation=''});
 if(window.__rearm)window.__rearm();
 GROUPS.forEach(function(g){if(g.el)resetGroup(g)});
 [].forEach.call(document.querySelectorAll('.panel'),function(p){p._badged=0;[].forEach.call(p.querySelectorAll('.badges span'),function(x){clearTimeout(x._t);x.classList.remove('lit')})});
 [].forEach.call(document.querySelectorAll('.tline'),function(tl){tlSet(tl,0)});tlK=0}
"""
rep("var heroImg=document.querySelector('.hero .browser img');", JS_TL + "var heroImg=document.querySelector('.hero .browser img');")
rep("pbLabel();stream.setPaused(allPaused);if(!allPaused&&typeof tick==='function')tick()});",
    "pbLabel();stream.setPaused(allPaused);if(!allPaused&&typeof tick==='function')tick();if(!allPaused&&typeof tlTick==='function')tlTick()});")

open(p, "w", encoding="utf8").write(s)
print("ok")
