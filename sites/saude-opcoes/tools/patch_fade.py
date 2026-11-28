#!/usr/bin/env python3
"""Crossfade nas telas, fade na troca de aba e revelação em cascata ao rolar."""
import sys, re
p = sys.argv[1]
s = open(p, encoding="utf8").read()

def rep(old, new):
    global s
    assert old in s, "não achei: " + old[:90]
    s = s.replace(old, new, 1)

# ---------- CSS ----------
rep(".stage img{width:100%;height:100%;object-fit:cover;object-position:top left;transition:opacity .25s var(--ease),transform .6s var(--ease)}",
    ".stage img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top left;transition:opacity .7s cubic-bezier(.65,0,.35,1),transform .9s var(--ease)}\n"
    ".stage img.in{opacity:0;transform:scale(1.02)}\n.stage img.out{opacity:0}")
rep(".stage.swap img{opacity:0}", "")
rep(".panel.enter{animation:panelIn .35s var(--ease)}", ".panel.enter{animation:fadeIn .55s cubic-bezier(.65,0,.35,1)}\n.panel.leaving{opacity:0;transition:opacity .26s cubic-bezier(.65,0,.35,1)}\n@keyframes fadeIn{from{opacity:0}to{opacity:1}}")
rep(".panel.enter .viewer{animation:flipIn .6s var(--ease)}\n.panel.enter .info{animation:panelIn .5s var(--ease) .08s both}", "")
rep(".js .rv.in{opacity:1;transform:none}",
    ".js .rv.in{opacity:1;transform:none}\n"
    ".js .rv2{opacity:0;transform:translateY(24px);transition:opacity .7s var(--ease),transform .7s var(--ease);transition-delay:var(--d,0ms)}\n"
    ".js .rv2.in{opacity:1;transform:none}")
rep(".js .hero h1 .ln>span,.js .hero .fade-in,.js .hero .browser,.js .rv{opacity:1!important;transform:none!important}",
    ".js .hero h1 .ln>span,.js .hero .fade-in,.js .hero .browser,.js .rv,.js .rv2{opacity:1!important;transform:none!important}")

# ---------- JS: troca de aba com fade out → fade in ----------
a = s.index("function selectTab(t,focus){")
b = s.index("if(focus)t.focus();", a)
s = s[:a] + r"""var swapT=0;function selectTab(t,focus){var np=document.getElementById(t.getAttribute('aria-controls')),pp=null;
 tabs.forEach(function(b){var on=b===t;b.setAttribute('aria-selected',on?'true':'false');b.tabIndex=on?0:-1;var p=document.getElementById(b.getAttribute('aria-controls'));if(!on&&!p.hidden)pp=p});
 [].forEach.call(np.querySelectorAll('img[loading=lazy]'),function(i){i.loading='eager'});clearTimeout(swapT);
 function show(){[].forEach.call(document.querySelectorAll('.panel'),function(p){if(p!==np){p.hidden=true;p.classList.remove('leaving')}});
  if(np.hidden){np.hidden=false;np.classList.remove('enter');np.offsetWidth;np.classList.add('enter')}document.dispatchEvent(new CustomEvent('tabshown',{detail:np}))}
 if(pp&&!RM.matches){pp.classList.add('leaving');swapT=setTimeout(show,260)}else show();
 movePill(true);""" + s[b:]

# ---------- JS: galeria com crossfade ----------
a = s.index("var k=th.getAttribute('data-alt-key');st.classList.add('swap');")
b = s.index("},RM.matches?0:180)})})});", a) + len("},RM.matches?0:180)})})});")
s = s[:a] + r"""var k=th.getAttribute('data-alt-key'),old=[].slice.call(st.querySelectorAll('img'));
  var n=new Image();n.className='main in';n.width=1500;n.height=938;n.alt=D()[k];n.setAttribute('data-i18n-alt',k);n.decoding='async';n.src=th.getAttribute('data-src');
  var go=function(){st.classList.toggle('phone',th.getAttribute('data-phone')==='1');st.appendChild(n);n.offsetWidth;n.classList.remove('in');
   old.forEach(function(o){o.classList.add('out')});setTimeout(function(){old.forEach(function(o){if(o.parentNode)o.remove()})},RM.matches?0:760)};
  (n.decode?n.decode():Promise.resolve()).then(go,go)})})});""" + s[b:]

# idioma: textos alternativos lidos a cada troca (imagens novas da galeria)
rep(" alts.forEach(function(n){var k=n.getAttribute('data-i18n-alt');if(d[k]!=null)n.alt=d[k]});",
    " [].forEach.call(document.querySelectorAll('[data-i18n-alt]'),function(n){var k=n.getAttribute('data-i18n-alt');if(d[k]!=null)n.alt=d[k]});")
# zoom: usa a imagem visível (a última)
rep("b.addEventListener('click',function(){last=b;var im=b.querySelector('img');",
    "b.addEventListener('click',function(){last=b;var ims=b.querySelectorAll('img'),im=ims[ims.length-1];")

# ---------- JS: revelação em cascata ao rolar (uma vez) ----------
rep("[].forEach.call(document.querySelectorAll('.rv,.metric'),function(el){",
    r"""[].forEach.call(document.querySelectorAll('.rv'),function(el){el.classList.remove('rv')});
(function(){if(RM.matches)return;
 var SEL='main section .lbl, main section h2, main section .sh p, .tablist, .panels, .hint, .sstep, .dm-p, .dm-note, .lead, .cell, .steps li, .founder, .qa, .cta-card h2, .crow, .mq';
 var els=[].slice.call(document.querySelectorAll(SEL)).filter(function(e){return !e.closest('.hero')&&!e.closest('.story-media')});
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;var el=e.target;io.unobserve(el);el.classList.add('in');
  var d=parseInt(getComputedStyle(el).getPropertyValue('--d'))||0;setTimeout(function(){el.classList.remove('rv2','in');el.style.removeProperty('--d')},760+d)})},{rootMargin:'0px 0px -10% 0px'});
 els.forEach(function(el){var rc=el.getBoundingClientRect();if(rc.top<innerHeight*.9)return;
  var sib=[].slice.call(el.parentNode.children).filter(function(c){return els.indexOf(c)>-1});var i=Math.min(sib.indexOf(el),6);
  el.style.setProperty('--d',(i*80)+'ms');el.classList.add('rv2');io.observe(el)})})();
[].forEach.call(document.querySelectorAll('.metric'),function(el){""")

open(p, "w", encoding="utf8").write(s)
print("ok")
