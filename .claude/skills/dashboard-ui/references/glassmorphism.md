# Glassmorphism — receita

Base: série @code.xr (Login V3 `DeoGCPlzKOs`, Dashboard V7 `DfHrMboTVDZ`, V8 `DfKPFDwz2aA`, Sidebar V5 `DfMH6YTTcwx`),
smart home `DfrqAX9v59S` (frosted cinza) e a tela Settings de `Deoi1WhP83h` (opções Glass Clear/Tinted e
Reduce transparency). Os valores CSS abaixo são uma tradução do que se vê; não vêm do código-fonte original,
exceto as classes Tailwind citadas no snippet (`glass-card p-6 rounded-2xl`, `text-white/60`, `text-emerald-400`).

## O que as referências mostram
1. **O fundo faz o trabalho.** V7, V8 e V5 usam foto de interior (madeira, TV, planta, luz quente); o login usa
   ondas 3D pretas com faixas ciano. O vidro herda a cor do que está atrás: na V5 a parte inferior da sidebar fica
   laranja porque passa sobre o móvel de madeira.
2. **Duas famílias:**
   - *Dark tinted* (login, V8): superfície escura translúcida, alto contraste de texto branco.
   - *Warm/clear* (V7, V5, smart home): superfície clara/média translúcida, tinge com a foto.
3. **Aresta de luz:** borda de 1px mais clara que a superfície em todos os cards; no login o card tem **os cantos
   superior-esquerdo e inferior-direito cortados em diagonal**, cada um marcado por um triângulo ciano.
4. **Raios grandes:** cards ~16–24px; sidebar V5 ~28–32px; item ativo e botões em pílula completa.
5. **Um ancoradouro de cor sólida**: card azul na V8, pílulas laranja na V7, botão ciano no login.
6. **Item ativo** = pílula com fundo branco ~15–20% + borda branca ~30% (V5) ou pílula branca opaca (smart home).

7. **Entrada a partir do desfoque:** V7 e V8 começam com a foto limpa e os painéis aparecem "condensando" do blur;
   a troca de página repete o efeito. Na V8 a coluna de widgets da direita fica fixa e só os números mudam.
8. **Sidebar recolhível (V5):** rail de ~56px com ícones, tooltips de vidro ("Dashboard", "Projects") e badges em
   ponto; um botão circular no topo expande para ~250px (tooltip "Collapse"). O hover é uma pílula com borda clara
   que desliza entre os itens.

## Tokens
```css
:root {
  /* superfícies */
  --glass-dark:  rgba(18, 22, 30, .55);   /* login / V8 */
  --glass-warm:  rgba(70, 55, 48, .42);   /* V7 / V5 sobre madeira */
  --glass-clear: rgba(255,255,255,.10);   /* genérico sobre foto */
  --glass-gray:  rgba(85, 87, 86, .70);   /* smart home frosted ~#555756 */
  --glass-border: rgba(255,255,255,.16);
  --glass-hi:     rgba(255,255,255,.12);  /* brilho interno no topo */
  --blur: 20px;
  --radius-card: 20px;
  --radius-panel: 28px;
  /* acentos vistos */
  --cyan: #4cc3f5;   --cyan-deep: #2d8bb6;   /* login */
  --amber: #d59353;                           /* V7 */
  --blue-soft: #7488c7; --blue-cta: #7098ed;  /* V8 */
  --text-1: #fff; --text-2: rgba(255,255,255,.6); --pos: #34d399; /* emerald-400 */
}
```

## Card
```css
.glass-card {
  background: var(--glass-clear);
  backdrop-filter: blur(var(--blur)) saturate(140%);
  -webkit-backdrop-filter: blur(var(--blur)) saturate(140%);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-card);
  box-shadow: 0 10px 40px rgba(0,0,0,.30), inset 0 1px 0 var(--glass-hi);
  padding: 24px;                         /* p-6 */
  color: var(--text-1);
}
.glass-card .label { font-size: 14px; color: var(--text-2); }       /* text-sm text-white/60 */
.glass-card .value { font-size: 24px; font-weight: 700; }           /* text-2xl font-bold */
.glass-card .delta { font-size: 14px; color: var(--pos); display: inline-flex; gap: 4px; }
```
React (estrutura do snippet dos reels):
```jsx
<motion.div whileHover={{ y: -5 }} className="glass-card p-6 rounded-2xl">
  <div className="flex items-center justify-between">
    <div>
      <p className="text-sm text-white/60">{title}</p>
      <h3 className="text-2xl font-bold text-white">{value}</h3>
      <p className="flex items-center gap-1 text-sm text-emerald-400"><ArrowUpRight size={16}/> {change}%</p>
    </div>
    {/* ícone em quadrado com gradient */}
  </div>
</motion.div>
```

## Sidebar flutuante (V5)
```css
.glass-sidebar {
  position: fixed; inset: 16px auto 16px 16px; width: 248px;
  background: var(--glass-warm);
  backdrop-filter: blur(24px) saturate(150%);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-panel);
  display: flex; flex-direction: column; gap: 4px; padding: 14px;
}
.glass-sidebar .group-label { font-size: 10px; letter-spacing: .08em; text-transform: uppercase; color: rgba(255,255,255,.45); margin: 14px 10px 6px; }
.glass-sidebar a { display:flex; align-items:center; gap:10px; padding:9px 12px; border-radius:999px; color: rgba(255,255,255,.85); }
.glass-sidebar a[aria-current="page"] {
  background: rgba(255,255,255,.16);
  border: 1px solid rgba(255,255,255,.35);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.25);
}
.glass-sidebar .badge { margin-left:auto; min-width:20px; padding:0 6px; border-radius:999px; background: rgba(255,255,255,.14); font-size:11px; }
.glass-sidebar .badge.alert { background: #e9786a; color:#fff; }   /* badge vermelho visto */
```
Anatomia vista na V5: logo circular vermelho + "Vertix" + subtítulo, botão de recolher circular branco
flutuando fora da borda, busca com chip de atalho, MAIN (Dashboard ativo, Activity 11, Wallet, Schedule com ponto
vermelho), WORKSPACE (Messages badge vermelho, Projects expandido com sub-itens Website redesign / Mobile app /
Brand kit e pontos verde/vermelho/roxo + linha-guia), Reports, Settings, Night mode com toggle, card do usuário
"Alex Morgan" com status online.

## Login glass (V3)
```css
.auth-card {
  position: relative; width: min(440px, 92vw); padding: 32px;
  background: rgba(20, 28, 38, .55);
  backdrop-filter: blur(18px);
  border: 1px solid rgba(120, 200, 255, .18);
  border-radius: 18px;
}
/* cantos superior-esquerdo e inferior-direito cortados em diagonal, como no V3 */
.auth-card {
  --cut: 44px;
  clip-path: polygon(var(--cut) 0, 100% 0, 100% calc(100% - var(--cut)),
                     calc(100% - var(--cut)) 100%, 0 100%, 0 var(--cut));
}
/* triângulos ciano nos cantos cortados (o original usa uma peça de vidro azul em cada corte) */
.auth-card::before, .auth-card::after {
  content:""; position:absolute; width: 56px; height: 56px; pointer-events:none;
  background: linear-gradient(135deg, rgba(76,195,245,.55), rgba(45,139,182,.15));
}
.auth-card::before { top:0; left:0;     clip-path: polygon(0 0, 100% 0, 0 100%); }
.auth-card::after  { bottom:0; right:0; clip-path: polygon(100% 0, 100% 100%, 0 100%); }
/* com clip-path a borda some: desenhe a aresta com um SVG ou um pseudo-elemento interno (complemento) */
.auth-card h1 span { color: var(--cyan); }                 /* "Create <span>Account</span>" */
.auth-input { background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.10); border-radius: 10px; height: 44px; }
.auth-input:focus-within { border-color: var(--cyan); box-shadow: 0 0 0 3px rgba(76,195,245,.18); }
.auth-btn {
  height: 44px; border-radius: 10px; font-weight: 600; color: #04121a;
  background: linear-gradient(180deg, var(--cyan), var(--cyan-deep));
  box-shadow: 0 0 24px rgba(76,195,245,.45);               /* glow neon */
}
```
**Troca Welcome Back ↔ Create Account (vista nos quadros):** campos somem → card vazio só com o logo (quadrado ciano
dividido na diagonal) → anel de luz azul pulsa ao redor do logo → o card ajusta a altura → os campos do outro
formulário entram. Com Framer Motion (complemento): `AnimatePresence mode="wait"` nos formulários + `layout` no card
+ um `motion.div` do logo com `scale`/`opacity` e um anel com `boxShadow` animado.

## Fundos
- Foto real desfocada atrás de tudo (interior, paisagem) — preferível.
- Alternativa sem foto (complemento): `radial-gradient(60% 50% at 20% 10%, #1d3aa8 0, transparent 60%), radial-gradient(50% 40% at 80% 80%, #0f766e 0, transparent 60%), #050814` — como o glow do SaaS `DffBnb2vlUn`.

## Acessibilidade e fallback (a tela Settings de `Deoi1WhP83h` tem "Reduce transparency")
```css
@supports not (backdrop-filter: blur(1px)) { .glass-card, .glass-sidebar { background: rgba(30,30,34,.92); } }
@media (prefers-reduced-transparency: reduce) { .glass-card, .glass-sidebar { backdrop-filter: none; background: #1d1e22; } }
```
- Texto sobre vidro: contraste mínimo 4.5:1 — teste sobre a parte **mais clara** da foto.
- Blur entre 12 e 28px; acima disso perde a leitura do fundo e pesa na GPU.
- Não empilhe muitos níveis de `backdrop-filter` (complemento: custo de performance em telas grandes).
- Ofereça modo opaco (Clear / Tinted / Off) em apps de uso diário, como o app de tasks faz.
