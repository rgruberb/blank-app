# Padrões de layout, KPI, gráficos e movimento

Destilado das 11 referências (ver `visual-index.md`). Valores numéricos de espaçamento e raio são estimativas
visuais; os que não vêm das imagens estão marcados "(complemento)".

## 1. Esqueletos de página

### A. Rail + top nav (varejo `De12lc1vUmr`, tasks `Deoi1WhP83h`, SaaS `DffBnb2vlUn`, CRM V7 `DfHrMboTVDZ`)
```
┌──────────────────────────────────────────────────────────┐
│ logo  [pill][PILL ATIVA][pill][pill]          ⌕  ●  👤   │  top nav
├──┬───────────────────────────────────────────────────────┤
│▣ │ Título grande                      [filtros] [CTA]    │
│○ │ subtítulo de contexto                                 │
│○ │ ┌KPI★┐┌KPI─┐┌KPI─┐┌KPI─┐┌KPI─┐                        │
│○ │ └────┘└────┘└────┘└────┘└────┘                        │
│○ │ ┌──────── gráfico principal ───────┐┌── breakdown ──┐ │
│  │ └──────────────────────────────────┘└───────────────┘ │
└──┴───────────────────────────────────────────────────────┘
```
- Rail: 56–64px, só ícones; no varejo é uma **pílula preta flutuante** com margem da borda.
- Top nav em pílulas: ativo preenchido (preto no claro; teal em seguros; azul em SaaS).

### B. Sidebar larga (saúde `DfV39ohhwAC`, smart home `DfrqAX9v59S`, orçamento `DfkNvnePItL`, V8, sidebar V5)
- 220–260px. Topo: logo + nome do produto/workspace (+ botão recolher). Busca com atalho (`⌘K`).
- Grupos rotulados em caps pequenas e cinza (MAIN, WORKSPACE). Itens: ícone 16–18px + label + badge à direita.
- Item ativo: **pílula** (branca sobre glass cinza; translúcida com borda clara na V5; menta no orçamento).
- Sub-itens com ponto colorido e linha-guia vertical (Projects na V5).
- Rodapé: toggle de tema e/ou card do usuário (avatar, nome, e-mail, menu).

### C. Kanban (tasks, seguros Pipeline, SaaS Campaigns)
- Colunas de largura igual, fundo um degrau acima do canvas, raio ~16px.
- Cabeçalho: ponto/ícone de estado + nome + contagem em badge + menu `⋯`.
- Card: tags no topo (projeto com ponto colorido; prioridade em laranja/vermelho) → título 13–14px semibold →
  barra de progresso fina (2–3px) na cor do projeto com fração à direita → meta (data, comentários) + avatar.

### D. Página de detalhe (seguros, light)
Título da entidade + metadados → **stepper de etapas** horizontal → grid 3 colunas de campos (rótulo 11px cinza,
valor 13–14px) → card lateral com o número que importa (prêmio `$66,500`) e lista chave/valor.

## 2. KPI cards — anatomia
1. Rótulo: 11–12px, caps ou sentence case, cinza (60% opacidade), às vezes com ícone de 14px.
2. Valor: 28–36px, peso regular/medium (saúde usa peso leve), tabular nums (complemento: `font-variant-numeric: tabular-nums`).
3. Delta: chip pequeno com fundo tingido (verde/vermelho/âmbar) — ou texto verde simples (varejo).
4. Opcional: sparkline de 1px embaixo (varejo), ou unidade pequena ao lado do número ("3.4 d", "807 hours", "25 min").

Variações vistas:
- **KPI-mestre invertido** (card preto no tema claro) — varejo.
- **KPIs sem caixa** em faixa, separados só por espaço — saúde e tasks. Menos ruído, mais densidade.
- **Mini-KPIs dentro do card do gráfico** (Submitted / Decided / Backlog change) — saúde.
- **Card de cor sólida** no meio de um layout glass (azul com barras brancas) — V8.

## 3. Gráficos vistos e como foram estilizados
| tipo | onde | estilo |
|---|---|---|
| Área + linha, 2 séries | varejo | linha escura 1.5px + área cinza clara, curva suave, grid quase invisível |
| Sparkline | varejo (todos os KPIs) | linha fina sem eixo |
| Barras verticais com destaque | saúde "Requests vs decisions" | todas cinza-escuro, só a barra atual em mint |
| Duas linhas com faixa entre elas | saúde (estado 2) | linhas mint/cinza claro, fita preenchida translúcida, coluna destacada + tooltip com marcadores |
| Gauge semicircular de ticks | saúde "On time decisions" | ~40 ticks, mint → âmbar no fim, valor grande no centro + legenda "x of y" |
| Barras verticais coloridas | saúde "Open pipeline" | mint, última barra rosa (alerta) |
| Donut segmentado | tasks "By project" | segmentos com gaps, cores dos projetos, total no centro, legenda em lista com % |
| Barra empilhada horizontal | varejo breakdown | preto + cinza, percentuais acima |
| Barras de progresso duplas | SaaS Campaigns | teal + azul, valor à direita |
| Barras brancas em card azul | V8 | barras arredondadas brancas sobre azul |

Regras que se repetem: histórico em neutro + destaque no "agora"; nenhum gráfico 3D; legendas como lista
tabular; eixos mínimos. Para cores e marcas, use a skill `dataviz`.

## 4. Densidade
- Operacional (saúde, tasks): denso — 5 KPIs + 2 gráficos + tabela + card de IA na primeira dobra, padding de card ~16–20px, gaps ~12–16px.
- Executivo/vitrine (varejo, glass V7/V8): mais ar — padding ~24px, menos itens por linha.
- Glass sobre foto: poucos cards grandes; a foto precisa respirar entre eles.

## 5. Cartão de insight / IA (saúde)
Orbe animado com glow → nome do assistente + linha de contexto → **uma frase acionável com prazo**
("4 Sunvale cases lapse within 12 hours. Follow up by 2 PM") → evidência (avatares, IDs) → barra de urgência →
CTA primário ("Review 4 cases") + secundário ("Dismiss"). Nunca um parágrafo genérico.

## 6. Movimento (dos snippets nos reels)

### Troca de tema com círculo (varejo)
```js
themeBtn.addEventListener('click', () => {
  const root = document.documentElement;
  const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
  const r = themeBtn.getBoundingClientRect();
  const x = r.left + r.width / 2, y = r.top + r.height / 2;
  const end = Math.hypot(Math.max(x, innerWidth - x), Math.max(y, innerHeight - y));
  document.startViewTransition(() => { root.dataset.theme = next; })
    .ready.then(() => root.animate(
      { clipPath: [`circle(0px at ${x}px ${y}px)`, `circle(${end}px at ${x}px ${y}px)`] },
      { duration: 620, easing: 'ease-in-out', pseudoElement: '::view-transition-new(root)' }));
});
```
(`duration` lida como ~620; `easing` é complemento. Fallback sem `startViewTransition`: trocar direto — complemento.)

### Pílula ativa elástica (SaaS, orçamento, smart home)
Ideia: a pílula é um elemento absoluto recortado por `clip-path: inset(t r b l round 999px)`. Ao mudar de item,
a borda na direção do movimento ("lead") anima primeiro e rápido; a oposta ("trail") vai depois, mais lenta.
```js
function slidePill(pill, target, prev) {           // prev = {t,r,b,l} atual
  const box = pill.parentElement;
  const to = { t: target.offsetTop, l: target.offsetLeft,
               r: box.offsetWidth - (target.offsetLeft + target.offsetWidth),
               b: box.offsetHeight - (target.offsetTop + target.offsetHeight) };
  const st = { ...prev };
  const fwd = to.t > prev.t;                       // vertical; use l/r para horizontal
  const [lead, trail] = fwd ? ['b', 't'] : ['t', 'b'];
  const paint = () => gsap.set(pill, { clipPath: `inset(${st.t}px ${st.r}px ${st.b}px ${st.l}px round 999px)` });
  gsap.to(st, { [lead]: to[lead], duration: 0.3, ease: 'power3.out', onUpdate: paint });
  gsap.to(st, { [trail]: to[trail], duration: 0.5, ease: 'power3.inOut', onUpdate: paint });
  return to;
}
```
(Reconstruído do snippet; durações de leitura incerta.)

### Objeto percorrendo rota (seguros)
`path.getPointAtLength(len * t)` para posição, `Math.atan2` entre dois pontos próximos para rotação,
`strokeDashoffset` para revelar a linha percorrida; `gsap.to(progress, { t, duration: ~1.3, ease: 'power3.inOut' })`.

### Hover de card (série glass)
Framer Motion `whileHover={{ y: -5 }}`. Complemento: `transition={{ type: 'spring', stiffness: 300, damping: 24 }}`.

Sempre respeite `prefers-reduced-motion` (complemento): sem clip-path animado, troca instantânea.
