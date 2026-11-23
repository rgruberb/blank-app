# Receitas CSS/JS

Código próprio implementando os padrões das fontes. Os valores vêm das fontes; as escolhas de implementação (curvas `cubic-bezier`, nomes de vars) são (complemento).

## 0. Tokens
```css
:root {
  --press-scale: 0.95;            /* DfP6EoLBtgg */
  --lift-scale: 1.05;             /* drag / long press */
  --dur-press: 160ms;             /* Dfvja0XCyIi */
  --dur-reorder: 200ms;
  --dur-icon: 300ms;
  --dur-expand: 350ms;            /* ease-out */
  --dur-success: 470ms;
  --dur-reveal: 700ms;
  --stagger-tight: 70ms;
  --stagger: 100ms;
  --ease-out: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);  /* overshoot leve */
}
@media (prefers-reduced-motion: reduce) {
  :root { --press-scale: 1; --lift-scale: 1; --stagger: 0ms; --stagger-tight: 0ms; }
  *, *::before, *::after {
    animation-duration: 1ms !important; animation-iteration-count: 1 !important;
    transition-duration: 120ms !important; scroll-behavior: auto !important;
  }
}
```

## 1. Press / squish (0 ms no touchdown, 95%, volta com spring)
```css
.btn { transition: transform var(--dur-press) var(--ease-spring); touch-action: manipulation; }
.btn:active, .btn.is-pressed { transform: scale(var(--press-scale)); transition-duration: 0ms; }
```
`:active` atrasa em alguns browsers mobile; garanta com `pointerdown`:
```js
btn.addEventListener('pointerdown', () => btn.classList.add('is-pressed'));
['pointerup','pointercancel','pointerleave'].forEach(e =>
  btn.addEventListener(e, () => btn.classList.remove('is-pressed')));
```

## 2. Spring real em CSS via `linear()`
Gera a curva de um spring (massa 1) para usar como timing function. Damping ratio 0.8 ≈ overshoot pequeno (iOS); stiffness 180 / damping 20 = toasts.
```js
function springEasing({ stiffness = 180, damping = 20, mass = 1, samples = 60 } = {}) {
  const w0 = Math.sqrt(stiffness / mass), zeta = damping / (2 * Math.sqrt(stiffness * mass));
  const wd = w0 * Math.sqrt(Math.max(0, 1 - zeta * zeta));
  const x = t => zeta < 1
    ? 1 - Math.exp(-zeta * w0 * t) * (Math.cos(wd * t) + (zeta * w0 / wd) * Math.sin(wd * t))
    : 1 - Math.exp(-w0 * t) * (1 + w0 * t);
  let dur = 0; // tempo até assentar (|1-x| < 0.001 por um tempo)
  for (let t = 0, still = 0; t < 10 && still < 0.1; t += 0.001) { dur = t; still = Math.abs(1 - x(t)) < 0.001 ? still + 0.001 : 0; }
  const pts = Array.from({ length: samples + 1 }, (_, i) => +x((i / samples) * dur).toFixed(4));
  return { easing: `linear(${pts.join(', ')})`, duration: Math.round(dur * 1000) };
}
const { easing, duration } = springEasing();          // toast stack
el.animate([{ transform: 'translateY(16px)' }, { transform: 'none' }], { duration, easing });
```
Springs CSS não são interrompíveis com velocidade preservada; para drag/fling use uma lib de spring (Motion/Framer Motion, react-spring) ou GSAP. (complemento)

## 3. Pull-to-refresh com resistência (dedo 100% → lista 35%)
```js
const RESIST = 0.35, TRIGGER = 72; // TRIGGER: complemento
let startY = null, offset = 0;
list.addEventListener('pointerdown', e => { if (list.scrollTop === 0) startY = e.clientY; });
list.addEventListener('pointermove', e => {
  if (startY == null) return;
  offset = Math.max(0, (e.clientY - startY) * RESIST);
  list.style.transition = 'none';
  list.style.transform = `translateY(${offset}px)`;
  indicator.classList.toggle('ready', offset >= TRIGGER);   // release cue
});
list.addEventListener('pointerup', async () => {
  if (startY == null) return; startY = null;
  list.style.transition = 'transform 400ms var(--ease-spring)';
  if (offset >= TRIGGER) { list.style.transform = `translateY(${TRIGGER}px)`; await refresh(); }
  list.style.transform = 'none'; offset = 0;
});
```
Rubber band estilo iOS (overscroll): `f(x) = (1 - 1 / (x * 0.55 / d + 1)) * d`. Com `d = 400`, puxar 200 px dá ≈ 86 px — o valor do reel De4B0UxPXIk.

## 4. Cascade / stagger (70 ms)
```css
.list > * { opacity: 0; transform: translateY(8px);
  animation: rise var(--dur-expand) var(--ease-out) forwards;
  animation-delay: calc(var(--i) * var(--stagger-tight)); }
@keyframes rise { to { opacity: 1; transform: none; } }
```
```js
[...list.children].forEach((el, i) => el.style.setProperty('--i', i));
```

## 5. Número rolando (dígitos 100 ms separados)
```css
.roll { display: inline-flex; height: 1em; line-height: 1em; overflow: hidden; font-variant-numeric: tabular-nums; }
.roll .col { display: flex; flex-direction: column;
  transform: translateY(calc(var(--v) * -1em));
  transition: transform 600ms var(--ease-spring) calc(var(--i) * var(--stagger)); }
```
```js
function renderRoll(el, value) {            // value: string, ex. "529"
  el.setAttribute('aria-label', value);
  const digits = [...value];
  while (el.children.length < digits.length) {
    const col = document.createElement('span'); col.className = 'col'; col.setAttribute('aria-hidden', 'true');
    col.innerHTML = '0123456789'.split('').map(d => `<span>${d}</span>`).join('');
    el.append(col);
  }
  digits.forEach((d, i) => { const c = el.children[i]; c.style.setProperty('--i', i); c.style.setProperty('--v', d); });
}
```
A curva do reel tem leve overshoot ao assentar cada dígito.

## 6. Card expand / shared element (card → página)
View Transitions (mesmo documento):
```css
.card img { view-transition-name: var(--vt); }        /* defina --vt só no card clicado */
::view-transition-group(*) { animation-duration: var(--dur-expand); animation-timing-function: var(--ease-out); }
@media (prefers-reduced-motion: reduce) { ::view-transition-group(*) { animation: none; } }
```
```js
card.style.setProperty('--vt', 'hero');
document.startViewTransition(() => renderDetail(item));   // a página de detalhe usa view-transition-name: hero
```
Fallback FLIP:
```js
function flip(el, mutate) {
  const a = el.getBoundingClientRect(); mutate(); const b = el.getBoundingClientRect();
  el.animate([{ transform: `translate(${a.left-b.left}px,${a.top-b.top}px) scale(${a.width/b.width},${a.height/b.height})`, transformOrigin: 'top left' },
              { transform: 'none', transformOrigin: 'top left' }], { duration: 350, easing: 'cubic-bezier(0.22,1,0.36,1)' });
}
```
Voltar deve fazer o inverso até a posição original do card.

## 7. Morph de botão (pílula → spinner → tick)
```css
.submit { width: 260px; height: 64px; border-radius: 999px;
  transition: width 270ms var(--ease-in-out); }
.submit.loading { width: 64px; }          /* 260 → 64 px */
.submit .tick path { stroke-dasharray: 24; stroke-dashoffset: 24; }
.submit.done .tick path { stroke-dashoffset: 0; transition: stroke-dashoffset 470ms var(--ease-in-out); }
```
(Para listas grandes prefira animar `transform: scaleX` num pseudo-elemento em vez de `width`.)

## 8. Success: círculo, depois tick (470 ms)
```css
.ok circle { stroke-dasharray: 151; stroke-dashoffset: 151; animation: draw 280ms var(--ease-in-out) forwards; }
.ok path   { stroke-dasharray: 30;  stroke-dashoffset: 30;  animation: draw 190ms var(--ease-out) 280ms forwards; }
@keyframes draw { to { stroke-dashoffset: 0; } }
```
(280 + 190 = 470 ms; a divisão é complemento.)

## 9. Toast stack (máx. 3, spring 180/20, pausa no hover)
```js
const LIMITS = { info: 4000, warning: 7000, error: Infinity };
function toast(type, msg) {
  const el = Object.assign(document.createElement('div'), { className: `toast toast--${type}`, role: type === 'error' ? 'alert' : 'status', textContent: msg });
  stack.prepend(el);
  [...stack.children].slice(3).forEach(n => n.remove());               // máx 3 visíveis
  el.animate([{ transform: 'translateY(-100%)', opacity: 0 }, { transform: 'none', opacity: 1 }], springEasing({ stiffness: 180, damping: 20 }));
  let left = LIMITS[type], t0 = Date.now(), id;
  const run = () => { if (left !== Infinity) id = setTimeout(() => el.remove(), left); };
  el.onmouseenter = () => { clearTimeout(id); left -= Date.now() - t0; };
  el.onmouseleave = () => { t0 = Date.now(); run(); };
  run();
}
```
```css
.toast { border-left: 4px solid var(--c); }   /* + ícone por tipo; não só tingir o fundo */
.toast-stack { position: fixed; right: 16px; bottom: 16px; }
@media (max-width: 640px) { .toast-stack { top: 16px; bottom: auto; left: 16px; } }
```
(Para animar os toasts antigos subindo, aplique FLIP nos irmãos ao inserir.)

## 10. Drag para reordenar (lift 105%, outros 200 ms)
```css
.row { transition: transform var(--dur-reorder) var(--ease-out); }
.row.dragging { transform: scale(var(--lift-scale)); box-shadow: 0 12px 32px rgb(0 0 0 / .25); transition: none; z-index: 1; }
```

## 11. Interrupção
Prefira `transition` (CSS reverte a partir do valor atual) a `@keyframes` para estados abre/fecha. Com WAAPI/GSAP, não espere `finished`: chame `reverse()` ou crie a nova animação a partir do estilo computado atual.

## 12. Cantos contínuos (squircle)
`border-radius` é arco circular. Aproximação: `corner-shape: squircle` (onde suportado) ou `clip-path`/máscara SVG de superellipse. Cantos concêntricos: `inner-radius = outer-radius - padding` (36 − 12 = 24).

## 13. Reduce Motion de verdade (regras Apple + Motion for React)
Regras da Apple HIG (Accessibility) e da doc do Motion; detalhes em `official-motion-guidelines.md` §1.1 e §5.

**Motion for React: obrigatório.** `MotionConfig reducedMotion` tem padrão `"never"` (ignora a preferência do sistema). Envolva a raiz:
```jsx
import { MotionConfig } from "motion/react";   // exige React 18.2+
export function App({ children }) {
  return <MotionConfig reducedMotion="user">{children}</MotionConfig>;  // desliga transform/layout, mantém opacity e cor
}
```
Onde precisar de lógica própria (complemento):
```jsx
const reduce = useReducedMotion();
const enter = reduce ? { opacity: 1 } : { opacity: 1, y: 0 };                 // x/y/z → fade
const spring = reduce ? { type: "spring", bounce: 0 }                           // spring mais firme, sem bounce
                      : { type: "spring", visualDuration: 0.35, bounce: 0.15 };
// sem filter: blur() animado, sem scale de profundidade, sem autoplay/parallax
```
**CSS:** além do §0, nada de `filter: blur()` animado, `translateZ`/`perspective` ou zoom de fundo dentro de `prefers-reduced-motion: reduce`; drag/swipe continua 1:1 com o dedo, mas sem inércia nem rubber band (complemento).
**GSAP:** `gsap.matchMedia().add("(prefers-reduced-motion: reduce)", () => { /* fades */ })` (ver `ext-gsap-core`).
