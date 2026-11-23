# Padrões de layout, KPI, gráficos e movimento

Destilado das 18 referências (ver `visual-index.md`). Valores numéricos de espaçamento e raio são estimativas
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

### E. Mapa/foto aérea como canvas (série @felvrabr `Dfui4V5BMbz`, `DfpCOjIB1Rb`, `Dfr9S5yhlvX`)
```
┌───────────────────────────── foto aérea = mapa ─────────────────────────────┐
│ ◆ Marca  [⌕ busca……]                                   🔔  (AP) Nome/cargo │
│ ┌sidebar┐   ● pin "Field 01"        ┌popover──────┐   [NDVI]  ┌Overview───┐ │
│ │ ▢ ... │   ▱ polígono "Dry"  ───── │ foto · chip │   Moist.  │ KPI │ KPI │ │
│ │(pílula│                           │ 18%  [CTA]  │   Yield   │ KPI │gauge│ │
│ └───────┘                           └─────────────┘   Pivots  │ plano 3/4 │ │
│ ┌Mix (anéis)┐┌Forecast (12 barras, 1 destacada)──┐            │ mensagens │ │
└─────────────────────────────────────────────────────────────────────────────┘
```
- Os objetos do domínio (talhão, bloco de painéis, vila) são **polígonos/pins clicáveis** sobre a foto; o estado
  pinta o objeto (âmbar = problema, acento = ok/em ação).
- Popover ancorado ao pin com foto, chip de estado, 1 número e **1 CTA cheio**; após a ação o CTA vira linha de estado.
- Camadas do mapa como pílulas verticais à direita (ativa no acento).
- Coluna "Overview" de vidro escuro à direita: grade 2x2 de KPIs → card de plano/ordem com responsável e checklist
  segmentado → mensagens recentes.
- Mesmo esqueleto, acento trocado por domínio: lima (agro), âmbar (solar), menta + coral (resort).

### F. Gantt de reservas (resort `Dfr9S5yhlvX`)
Dias em colunas, **hoje destacado como coluna mais clara**, uma linha por unidade (vila), barras arredondadas com
nome + noites; nova reserva entra na cor do acento (menta) enquanto as existentes ficam em coral. Embaixo, grade de
ocupação (heatmap de células) + área de receita por noite com tooltip. Bom para qualquer alocação recurso × tempo.

## 2. KPI cards — anatomia
1. Rótulo: 11–12px, caps ou sentence case, cinza (60% opacidade), às vezes com ícone de 14px.
2. Valor: 28–36px, peso regular/medium (saúde usa peso leve), tabular nums (complemento: `font-variant-numeric: tabular-nums`).
3. Delta: chip pequeno com fundo tingido (verde/vermelho/âmbar) — ou texto verde simples (varejo).
4. Opcional: sparkline de 1px embaixo (varejo), ou unidade pequena ao lado do número ("3.4 d", "807 hours", "25 min").

Variações vistas:
- **KPI-mestre invertido** (card preto no tema claro) — varejo; no Dashboard do varejo **cada KPI tem um mini-visual
  diferente** (mini-barras, linha, anel, barras) escolhido pela natureza da métrica.
- **KPI cards tingidos** em tons terrosos diferentes (teal, marrom, azul-acinzentado, ferrugem) com sparkline — seguros.
- **1º KPI em material diferente** (vidro âmbar enquanto os outros são escuros) — glass V7.
- **KPIs sem caixa** em faixa, separados só por espaço — saúde e tasks. Menos ruído, mais densidade.
- **Mini-KPIs dentro do card do gráfico** (Submitted / Decided / Backlog change) — saúde.
- **Card de cor sólida** no meio de um layout glass (azul com barras brancas) — V8.
- **Grade 2x2 com chip de estado em palavra** ("Healthy", "Rising", "On track", "Clear") no canto direito do valor e
  mini-visual próprio embaixo (linha, pirulitos, gauge) — série @felvrabr.
- **Mini-KPIs com ícone circular colorido** no canto, uma cor por categoria — e-commerce `Dfct0mNvg3f`, ad campaign.
- **KPI de urgência cheio de cor** ("Overdue 2" coral) + 3 KPIs neutros (Today / Upcoming / Completed) — Ember V29
  `DfrtgFyTmOM`: o acento marca o que pede ação, não o maior número.
- **Card preto único** num tema claro com cartões menta — verificação `Dfz0mLAzsjg` (mesma lógica do KPI invertido).
- **KPI com subtotal de contexto** embaixo do número ("86 Today · Old Patients: 12"; "Cash $7,000 · Crypto $5,420.22")
  — CareNest `DfUvP_ulPC6`, Vaulto `DfcdrhgFFMR` (`domain-examples.md` §22).
- **Score de confiança** = número grande + delta em pontos + palavra ("Excellent") + data de atualização, e o número
  posicionado dentro de faixas coloridas com marcador — CreditPros `DfaQe-CiBfJ` (§23).
- **Número de score em fonte de matriz de pontos** dentro de arco fino ("93%", "89%") — fitness `DffCenmFASU` (§29a).
- **Cor do delta pelo sentido bom/ruim, não pelo sinal**: "Critical Alerts +6%" em verde (MediCore §26) e "−45%" de
  distância sem leitura (logística §25) são os contraexemplos. (complemento) Defina por métrica se "subir" é bom.

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
| Gauge semicircular em card preto | varejo "Sales performance" | arco claro sobre preto, marcas ao redor, % central |
| Barras de ticks empilhados | saúde "Open pipeline" | barras feitas de segmentos horizontais (equalizador) sobre trilhos de ticks cinza |
| Funil em barras com trilhos | SaaS Funnels / Campaigns | 1ª barra cheia (gradiente azul ou verde), demais cada vez menores dentro de trilhos vazios |
| Heatmap de coorte em triângulo | SaaS Cohorts | células azuis com intensidade = retenção, diagonal em escada |
| Anéis concêntricos | tasks "Today" | 3 anéis (rosa, verde, azul) + legenda vertical com valor/meta |
| Barras horizontais por categoria + anel | orçamento Insights | barras finas com valor à direita; anel menta com total |
| Pilares de luz | glass V7 | barras verticais em gradiente branco→transparente, selecionada em laranja com rótulo |
| Dial de termostato | smart home | arco branco com knob, valor central, +/- nas laterais |
| Grade de agenda (heatmap binário) | smart home Climate | 7 dias x 24 h, célula branca = ligado |
| Barras de 12 meses em trilhos, 1 mês destacado | série @felvrabr (Harvest Forecast, Generation) | pílulas cinza-gradiente, o mês-alvo no acento com tooltip-pílula ("Mar · 4.2k t") |
| Pirulitos com limite | @felvrabr (Pivots running, Crews on site) | hastes finas com bolinha, marcador "Max 4", o ativo no acento |
| Anéis concêntricos de mix | @felvrabr (Crop Mix, Energy Mix) | 3 arcos (acento, tom médio, branco), total no centro, legenda com % |
| Progresso segmentado N/M | @felvrabr ("Zones irrigated 3/4", "Pre-job checklist 3/4") | 4 células lado a lado que enchem uma a uma, % à direita |
| Anel de ocupação "5/6 · 83%" | resort `Dfr9S5yhlvX` | anel menta com fração no centro, % ao lado, sobe até 100% |
| Gantt | resort `Dfr9S5yhlvX` | barras coral, nova reserva em menta, coluna de hoje clara |
| Anel multicolor com orbe | ad campaign `DfXoXVFPBfd` | 4 segmentos (azul, verde, amarelo, vermelho) + esfera azul brilhante no centro |
| Barras horizontais por canal | ad campaign Reports | barras finas coloridas com valor à direita e total no topo ("Total 140,708") |
| Área empilhada | e-commerce `Dfct0mNvg3f` | rosa/amarelo/azul opacos, curvas suaves |
| Dial circular | glass V30 `Dfj_FGsTAVB` | anel azul com knob, valor em graus que anima (50° → 65°) |
| Barras-pirulito com linha de meta | vendas `Dfjx6Stv3-d` | haste + ponto; acima da meta tracejada no acento (laranja), abaixo em cinza, a atual em branco |
| Barra segmentada + cards | vendas Channels | 1 barra horizontal em 4 cores + 4 cards de valor alinhados embaixo |
| Heatmap de quadrados arredondados | verificação `Dfz0mLAzsjg` | quadrados em tons de menta/cinza = volume por período, legenda Passed/Declined/Flagged |
| Linha + área com comparação tracejada | verificação Reports | área clara no acento + linha preta tracejada "período anterior" |
| Matriz de risco 5x5 | crédito privado `Dfo0F0Pvo4Y` | escala de um tom (terracota claro→escuro), número na célula, selecionada com contorno no acento |
| Colunas em relevo | skeuomorfismo `DfuS2Jbzsjt` | colunas creme com sombra interna, a última no acento |
| Gráfico de pontos como barra | RH `DYJwy9aCSYP` | altura = nº de pontos empilhados, pontos crescem de tamanho |
| Candles + seletor de período | trading `DXeeUP7FKGs_1` | candles acento/vermelho sem grid; 1D·1W·1M·3M·1Y·ALL com ativo em pílula |
| Linha com cursor vertical | Borea `DSIMwtvDluO_3` | linha laranja fina, cursor vertical + ponto de leitura, seletor de período no rodapé |
| Rosca de score | Borea `DSIMwtvDluO_1` | segmentos com gaps em gradiente laranja→azul, score grande no centro |
| Sankey de conversão | Vaulto `DfcdrhgFFMR_2` | nós por moeda, fluxos cinza, 1 nó em vermelho (destaque) |
| Heatmap de quadradinhos (cashflow) | Vaulto `DfcdrhgFFMR_2` | grade cinza/branco, claro = mais movimento, sem eixo |
| Barras semanais com 1 dia aceso | Vaulto `DfcdrhgFFMR_2` | trilhos cinza, só "Wed" em vermelho com gradiente |
| 2 linhas + tooltip com ponto no acento | Vaulto `DfcdrhgFFMR_3`, Zentra `Dfr6X8qFPwC` | branca + vermelha (Vaulto) ou laranja + azul + 1 neutra sobre barras de volume (Zentra) |
| Barras hachuradas + 1 cheia | logística `DftsSH-jnfs_1` | histórico em hachura diagonal cinza, barra atual teal com tooltip "$329" |
| Faixas de score com marcador | CreditPros `DfaQe-CiBfJ_1` | 3 faixas pastel (rosa/amarelo/verde), marcos 300/630/690/730, triângulo preto na posição |
| Grade mensal ✓/✕ | CreditPros `DfaQe-CiBfJ_2` | células por mês; ✓ em círculo limão, mês perdido ✕ cinza |
| Gauge semicircular em gradiente | CareNest `DfUvP_ulPC6_2` | arco bege → teal com agulha |
| Arco radial de traços (risco) | CareNest `DfUvP_ulPC6_2` | traços bege/laranja em leque + 3 contagens de risco acima |
| Área com projeção tracejada | Deuce `Dfus5sWFAov` | área verde até o "hoje" (linha vertical tracejada), depois linha tracejada |
| Radar de atributos / mapa de quadra | Deuce `Dfus5sWFAov` | radar verde de 5 eixos; quadra com zonas em % |
| Barra de progresso por status | Zentra `Dfr6X8qFPwC` | uma barra por estado (Pending 80%, On Hold 30%…) com % e delta |
| Barra segmentada com marcador + N/M | fitness `DffCenmFASU` | teal-claro → teal, marcador no ponto atual, "Exercises 8/12" ao lado |

Regras que se repetem: histórico em neutro + destaque no "agora"; nenhum gráfico 3D; legendas como lista
tabular; eixos mínimos. Para cores e marcas, use a skill `dataviz`.
**Ressalva (rodada 9B):** a tabela acima registra o que as referências fazem, não o que é mais legível. Antes de copiar
um gauge, donut ou anel, passe pelo critério do §11 (arco só para 1 número com meta; comparar → barras; tendência → linha).

## 4. Densidade e heros de domínio
- Heros que não são gráfico aparecem quando o objeto do domínio é visual: cartão de crédito 3D (orçamento),
  câmera da sala (smart home), stepper-rota com barco (seguros). Use no máximo um por tela.
- **Foto aérea como mapa operacional** (fazenda, usina, resort — @felvrabr): o hero é clicável e carrega estado.

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
  gsap.to(st, { [trail]: to[trail], duration: 0.55, ease: 'power3.inOut', onUpdate: paint });
  return to;
}
```
(Reconstruído do snippet; durações de leitura aproximada. A versão do smart home detecta o eixo e também anima as bordas do eixo cruzado, ~0.4s `power2.inOut`.)

### Objeto percorrendo rota (seguros)
`path.getPointAtLength(len * t)` para posição, `Math.atan2` entre dois pontos próximos para rotação,
`strokeDashoffset` para revelar a linha percorrida; `gsap.to(progress, { t, duration: ~1.3, ease: 'power3.inOut' })`.

### Troca de página com desfoque (SaaS, orçamento, smart home, V7, V8)
Em todos esses reels há um quadro intermediário em que o conteúdo inteiro está borrado: a página sai desfocando e a
nova entra do desfoque, enquanto a navegação fica nítida. Implementação sugerida (complemento):
```css
.page-exit  { animation: out .22s ease-in forwards; }
.page-enter { animation: in .32s ease-out; }
@keyframes out { to   { filter: blur(16px); opacity: 0; transform: scale(.985); } }
@keyframes in  { from { filter: blur(16px); opacity: 0; transform: scale(1.015); } }
```
Variações temáticas: seguros cobre a tela com **ondas do mar**; tasks usa **motion blur vertical**; varejo usa o
círculo do `startViewTransition` também para a troca de tema.

### Entrada escalonada e contagem de números
- Saúde: sidebar → header → KPIs → cards, com linhas se desenhando e ticks do gauge acendendo.
- V8: só a foto, depois os painéis surgem do desfoque; a coluna de widgets da direita **permanece entre páginas**
  e os números contam até o novo valor.
- Varejo: o gauge cresce (79% → 86%) e os KPIs mudam de valor ao trocar de tela.

### Ação → estado no objeto (série @felvrabr)
CTA cheio no popover ("Start irrigation", "Dispatch technician") → o botão é trocado por uma linha de estado
("✓ Irrigating · 40 min", "Crew 3 · ETA 11:50") e o objeto no mapa muda de cor (âmbar → verde). Sem modal, sem toast.
Complemento: `button` → `role="status"` com `aria-live="polite"`; crossfade ~200ms.

### Pílula elástica, variantes novas
- Raio configurável: `slidePill(pill, target, { radius = 12 })` → `inset(... round ${radius}px)` (CRM interiores `DfeT74YvQaD`).
- Eixo cruzado também anima, ~0.45s (e-commerce `Dfct0mNvg3f`); top nav horizontal (ad campaign `DfXoXVFPBfd`).

### Ilha de estado (tasks)
Pílula preta fixa no topo central ("Focus 24:56") que expande num card com detalhes e ações; um toast confirma
o modo ("notifications are held"). Bom para um modo ativo global (foco, gravação, sync).

### Hover de card (série glass)
Framer Motion `whileHover={{ y: -5 }}`. Complemento: `transition={{ type: 'spring', stiffness: 300, damping: 24 }}`.

Sempre respeite `prefers-reduced-motion` (complemento): sem clip-path animado, troca instantânea.

## 7. Padrões de gamificação

**Leitura honesta das referências:** nenhum dos 18 reels (nem os posts das rodadas 2–7) mostra gamificação explícita — **não há pontos/XP, níveis,
badges, streaks, rankings/leaderboards nem tela de recompensa**. O que aparece, e muito bem resolvido, é a
**camada de progresso e meta** sobre a qual a gamificação se constrói. Abaixo, primeiro o que se vê (com ID), depois
como usar num painel de gestor e num de cliente. Tudo marcado "(complemento)" é sugestão, não está nas imagens.

### 7.1 O que se vê
| mecânica | como aparece | onde |
|---|---|---|
| **Progresso até a meta do dia** | gauge semicircular de ticks que enche e conta (33% → 92% "TODAY"; 33% → 91%) | `Dfui4V5BMbz` Crop health, `DfpCOjIB1Rb` Performance ratio |
| **Checklist segmentado N/M** | barra em 4 células que enchem uma a uma, fração no rótulo ("Zones irrigated 3/4", "Pre-job checklist 3/4") e % à direita | `Dfui4V5BMbz`, `DfpCOjIB1Rb` |
| **Meta que se completa** | anel "5/6 · 83%" → 95% → 100% enquanto uma reserva entra pelo chat | `Dfr9S5yhlvX` |
| **Limite/capacidade visível** | pirulitos com marcador "Max 4" (pivôs ou equipes ativas) | `Dfui4V5BMbz`, `DfpCOjIB1Rb` |
| **Comparação com alvo** | texto pequeno ao lado do valor no popover (18%, leitura "vs target") | `Dfui4V5BMbz`, `DfpCOjIB1Rb` |
| **Estado em palavra, colorido** | chips "Healthy", "Rising", "On track", "Clear", "Low moisture", "Alert" | série @felvrabr |
| **Feedback imediato da ação** | CTA → "✓ Irrigating · 40 min" e o polígono do talhão vira de âmbar para verde | `Dfui4V5BMbz` (também "Dispatch technician" → "Crew 3 · ETA 11:50") |
| **Números que contam até o valor** | gasto £19,076 → £23,094; receita $41,849 → $48,490; MWh 47.4 → 48.6 | `DfXoXVFPBfd`, `DfeT74YvQaD`, `DfpCOjIB1Rb` |
| **Destaque do "agora"** | um único mês aceso no acento com tooltip-pílula ("Mar · 4.2k t") | série @felvrabr |
| **Progresso de metas/pacing (rótulos ilegíveis)** | 3 barras coloridas sob um número "23"; barra azul sob 3 números; anéis de % | `Dfct0mNvg3f`, `DfXoXVFPBfd`, `DfeT74YvQaD` Growth |
| Já na skill | anéis concêntricos com valor/meta (Tasks 3/8, Focus 1.1h/2h), timer de foco, check magenta em tarefa | `Deoi1WhP83h` |
| **Score do dia + 1 ação** | "Today's Health Score 93%" + "Your Body Is Ready" + botão único "Start Workout" | `DffCenmFASU` (§29a) |
| **Conquistas como mini-anéis** | "Nutrition Achievements": hidratação, fibra, vitaminas 9/12 em anéis pequenos | `DffCenmFASU` |
| **Score com palavra** | anel lima "74% Excellent!" (finanças), "730 +6 pts Excellent" (crédito), "Nutrition Score 88 · Excellent" | `DfmwyDclA0Q`, `DfaQe-CiBfJ`, `DffCenmFASU` |
| **Sequência de meses ✓/✕** | grade de pagamentos em dia, mês perdido em ✕ (base de streak) | `DfaQe-CiBfJ_2` |
| **Onboarding com passos** | card "Finish Setup · 2 of 4 · Skip · Next" na sidebar | Zentra `Dfr6X8qFPwC` |
| **Progresso da temporada** | "Season progress 68% TODAY" (gauge), "Rows picked 3/4 75%" | Caféra `Df4Shdgmafx` (§28a) |

### 7.2 Blocos de UI gamificada derivados (complemento, construídos sobre 7.1)
- **Anel/gauge de meta** com fração e prazo: "3/4 zonas · fecha hoje". Ao chegar a 100%: o arco troca para a cor do
  acento cheio e um check aparece (um pulso, ~400ms, uma vez só).
- **Checklist segmentado como "trilha de missão"**: cada célula = uma etapa nomeada no hover; a célula ativa pulsa de leve.
- **Nível/tier** derivado de uma métrica existente (ex.: NDVI médio → "Bronze/Prata/Ouro" ou "Nível 3 · Saudável"),
  exibido como chip ao lado do KPI, nunca como tela separada.
- **Streak**: fileira de 7 pontos (dias) acima do KPI, preenchidos no acento quando a meta do dia foi batida —
  reaproveita a grade de células de `Dfr9S5yhlvX`/`DfrqAX9v59S`.
- **Ranking**: lista tabular (posição · avatar · nome · barra horizontal · valor), como as barras por canal de
  `DfXoXVFPBfd` Reports; destaque só para "você" ou para o 1º, o resto neutro.
- **Badge/conquista**: ícone 3D pequeno (estilo dos produtos do V30 `Dfj_FGsTAVB`) dentro do card de mensagens
  recentes ("Marcos concluiu 4/4 zonas"), em vez de modal de comemoração.
- **Recompensa**: barra de pontos até o próximo benefício com o valor restante em texto ("faltam 120 pts para frete grátis").

### 7.3 Painel do gestor vs. painel do cliente (complemento)
| | **gestor** (opera, acompanha a equipe) | **cliente** (acompanha o próprio resultado) |
|---|---|---|
| pergunta | "quem/qual área está atrás da meta e o que faço agora?" | "como estou indo e o que falta para o próximo marco?" |
| métrica de progresso | % da equipe/área no prazo em barras horizontais (painel operacional: sem gauge, §11), checklists por ordem de serviço | 1 meta pessoal grande (anel), marco seguinte com prazo |
| ranking | sim, entre equipes/talhões/vendedores, com filtro e ordenação por risco (como a saúde `DfV39ohhwAC`) | evitar ranking contra outros clientes; no máximo "você vs. sua média" |
| badges/níveis | atribuídos pelo gestor ou automáticos; visíveis como chips na lista da equipe | nível/tier do cliente como chip no header; conquistas em histórico |
| streaks | por equipe (dias sem atraso), discreto | pessoal, visível no topo da home |
| feedback de ação | ação no objeto → estado muda no mapa/lista (padrão Verdan) | marco atingido → anel completa + mensagem curta; nunca bloquear a tela |
| densidade | operacional: mapa/lista + coluna de KPIs 2x2 + plano + mensagens | vitrine: poucos cards grandes, um hero de progresso, CTA único |
| tom | chips de estado em palavra ("On track", "Atrasado"), âmbar para risco | linguagem positiva ("faltam 2 etapas"), sem vermelho para o próprio cliente |

**Como montar a partir do Verdan `Dfui4V5BMbz`** (complemento): gestor = layout E inteiro (mapa + Overview), com o
card de plano virando "missão" (responsável, checklist 3/4, prazo) e um card de ranking de talhões/equipes no lugar de
Recent Messages; cliente = mesma coluna Overview em largura total, sem o mapa operacional, com o gauge como hero
("Saúde da sua lavoura 92%"), streak de 7 dias, chip de nível e o mês destacado como "próximo marco".

### 7.4 Regras e anti-padrões (complemento)
- Gamifique **comportamento que o usuário controla** (concluir checklist, responder no prazo), não números que ele
  não move (preço, clima).
- Gauge/anel de meta sempre com o número e a meta em texto; ranking e comparação entre equipes em **barras**, nunca em anéis (§11).
- Uma barra de progresso principal por tela; o resto em chips. Celebração = 1 animação curta, uma vez, com
  `prefers-reduced-motion` respeitado.
- Mostre o próximo passo junto do progresso ("3/4 · falta Zona 4 · Start irrigation"), como o popover faz com o CTA.
- Sem dark patterns: nada de streak que "quebra" para pressionar compra, nem ranking público de clientes
  (ver a skill `ux-patterns`).
```css
/* checklist segmentado "3/4" (complemento, a partir de Dfui4V5BMbz) */
.seg { display:grid; grid-template-columns:repeat(var(--n,4),1fr); gap:6px; }
.seg i { height:28px; border-radius:8px; background:rgba(255,255,255,.06); }
.seg i.done { background: var(--accent, #c6e17a); transition: background .3s ease-out; }
```


## 8. Design para o momento de decisão (apps de investimento/trading)

Fonte: "Markets" de @rish_designs (`DXeeUP7FKGs_1`) e Borea AI da @ramotion (`DSIMwtvDluO_1–3`). Regras de UX gerais
de tela de decisão e fluxo de compra estão em `ux-patterns`; aqui fica a parte visual.

**Princípio:** a tela é desenhada para o instante em que a pessoa decide comprar, vender ou esperar. Ela responde de
imediato *o que está se mexendo, o que acontece agora e para onde olhar*; mostra só sinais imediatos e contexto
suficiente; o bloco de IA serve para **reduzir dúvida**. Tirar atrito vale mais que adicionar função.

**Anatomia do card/linha de ticker**
1. Logo do ativo (círculo/quadrado 32–40px).
2. **Ticker em negrito** (AAPL) + **nome completo embaixo** em cinza (Apple Inc.) — ou ticker em pílula/chip (Borea).
3. À direita: **preço** (tabular nums; complemento) + **variação com sinal e cor em pílula** (+1.24% verde, −1.24%
   vermelho). Nunca só cor: sempre o sinal +/− também.
4. Estado selecionado = borda no acento + fundo um pouco mais claro.
5. Variante "mover" (horizontal, carrossel): card mais alto com nome, preço e pílula de variação.

**Home de mercado:** busca no topo → abas de classe (Stocks / Crypto / ETFs) → **listas prontas** ("Today's Movers",
"Top Traded", "Gainers / Losers" em duas colunas, "Trending") em vez de feed genérico → "All assets" em linhas.

**Detalhe do ativo (de cima para baixo):** nome + tag de setor → preço grande + variação do período → gráfico (candles
ou linha com cursor + ponto de leitura) → **seletor 1D · 1W · 1M · 3M · 1Y · ALL** → **card de IA** (selo de veredito
BULLISH/BEARISH + 2–3 frases + "View full analysis →") → **Sell / Buy do mesmo tamanho, lado a lado, fixos no rodapé**
(zona do polegar; Sell vermelho, Buy no acento).

**Cor:** base quase preta + **um acento** (limão no Markets) para aba ativa, período ativo e CTA positivo; ou 2 cores
de marca (azul + laranja no Borea) para score/seleção. **Verde/vermelho reservados à variação de preço** — não use o
verde da variação como cor de marca (complemento: se a marca for verde, diferencie o tom do verde semântico).
Preço em sans, dados auxiliares em mono.

**Anti-padrões (complemento):** gráfico gigante sem preço legível; Buy maior que Sell (empurra decisão — ver dark
patterns em `ux-patterns`); IA com parágrafo genérico sem veredito; ticker errado em mockup (o case Borea mostra "APPL").

## 9. Fluxos de app de serviço/pedido (série @ui.pixel)

Fonte: Qwash (`DX_bA4rCWf0`), WayLoo (`DVv7OOECewR`); descrições em `domain-examples.md` §21.
- **Progresso do pedido em 4 etapas** com rótulos curtos (Picked → Washing → Out for delivery → Delivered): mesma
  barra no card "Active order" da home **e** no detalhe do pedido, com chip de estado ("On Process") e mapa de rota.
- **Rodapé fixo com total + 1 botão primário** nas telas de montagem (lista de preços com stepper − 0 +) e no
  checkout ("Estimated Total $21" + "Schedule a collection"; "Pay now"). O valor do botão tem de bater com o total.
- **Tab bar**: 5 abas com **botão central circular** para a ação principal (Qwash) ou **pílula flutuante** com aba ativa
  no acento (WayLoo, Markets).
- **Saudação em duas camadas**: nome em branco/preto + pergunta em cinza ("Hello, Denis! *You want to book something?*").
- Gradiente/acento de marca só no cabeçalho, botões e aba ativa; corpo neutro com cards arredondados.
- Para apresentar: pares de telas que contam o fluxo inteiro (oferta → home → serviço → detalhe → agendamento → revisão).

## 10. Dashboard fintech web e apps de score (rodadas 2, 5, 7)

Fonte: Vaulto `DfcdrhgFFMR`, Zentra `Dfr6X8qFPwC`, finanças pessoais `DfmwyDclA0Q`, CreditPros `DfaQe-CiBfJ`,
fitness `DffCenmFASU`; descrições em `domain-examples.md` §22–23 e §29. Complementa o §8 (app de trading).

**Ordem de leitura do dashboard fintech web** (a legenda do Vaulto diz "peso visual para o que você lê primeiro"):
1. Saldo total gigante + delta em chip → **composição do total logo abaixo** (Cash + Crypto).
2. Ações: **1 CTA cheio no acento** ("Add Funds") + 2 secundárias em contorno (Send, Convert).
3. Cards por ativo/moeda (com sparkline e delta) + **card tracejado "adicionar"** no fim da fileira.
4. Gráfico principal com tooltip e seletor de período/dia.
5. Lista de atividade ou tabela de transações; coluna lateral com **uma ação** (Convert) e **um monitor** (Watchlist).
Sidebar com grupos em caps (GENERAL / TOOLS / INSIGHTS ou MAIN MENU / FINANCE OPS), badges de contagem, card de
upgrade ou de onboarding no rodapé, barra de comando com atalho (⌘ Space, ⌘D "Ask AI").

**Cor:** base quase preta + 1 acento de UI (laranja Vaulto, roxo Zentra, teal CareNest) + verde/vermelho só para
variação. **As séries de gráfico podem ter cores próprias** (vermelho de gasto no Vaulto; laranja BTC + azul ETH no
Zentra) desde que não usem o acento de UI em fundo grande. **Divergência com a regra 5 do SKILL.md ("uma cor de
destaque só"):** o app de finanças `DfmwyDclA0Q` usa **dois acentos com papéis fixos** (azul = dinheiro/ação, lima =
score/resultado). Aceite dois só se o papel de cada um for documentado e nunca trocar.

**Score (crédito, saúde financeira, fitness):** número grande + delta + palavra + data; posição dentro de faixas;
anel/arco fino; botão único com o próximo passo. A palavra ("Excellent", "Healthy") dá o veredito sem exigir leitura
do gráfico. (complemento) Faixas com rótulo de texto, não só cor, para daltonismo.

**Profundidade sem sombra pesada:** textura granulada sutil nos cards (Vaulto), vidro em gradiente terroso como drawer
(CreditPros). Para sombras em tema claro, ver a regra de sombra tingida em `design-direction`
(`layers-and-trust-layout.md` §4).

**Apresentação** (todos os posts do Orbix Studio): tablet/celular nas mãos → UI plana em 2 metades → recorte 3D
inclinado com desfoque → CTA. Detalhe em `design-direction` (`claude-web-design-workflow.md`).

## 11. Escolha de gráfico: divergência NN/g × skill (rodada 9B)

**A divergência.** As referências desta skill (rodadas 2–7) usam muito gauge, donut, anel concêntrico e rosca de score:
é a linguagem de progresso/gamificação (§7) e de apps de score (§10). O NN/g ("Dashboards: Making Charts and Graphs
Easier to Understand", https://www.nngroup.com/articles/dashboards-preattentive/, 2017) recomenda o contrário para
**leitura rápida**: valores por **comprimento (barras)** e **posição 2D (linhas, dispersão)**; evitar pizza, donut,
gauge, treemap e 3D; cor para **categoria, não magnitude**, e nunca como único sinal (até ~4,5% da população tem
daltonismo: ~8% dos homens, ~0,5% das mulheres). Print: `9B_dashboards_linha-e-barras_1.jpg` (linha semanal + barras
horizontais de uso).

**Por que as duas coisas convivem:** o olho compara comprimentos alinhados bem e ângulos/arcos mal. Um anel com **um**
número e **uma** meta não pede comparação, pede "quanto falta" — aí o arco funciona como moldura do número. O problema
é usar arco/fatia para **comparar** (categorias, períodos, equipes).

**Critério** (a linha do gauge/anel vale só fora de painel operacional de uso diário, que fica em barras/linhas; padrão 17):
| Pergunta do card | Use | Não use |
|---|---|---|
| "Quanto falta para a meta?" (1 número, 1 meta: progresso, score, ocupação, % do dia) | gauge/anel **com o valor numérico ao lado ou no centro** + meta/fração em texto ("5/6 · 83%", "730 · Excellent") | anel sem número; anel com 3+ séries para comparar |
| Comparar categorias (canais, equipes, projetos, clientes) | **barras** horizontais ordenadas, valor no fim da barra | pizza, donut, anéis concêntricos, treemap |
| Tendência no tempo | **linha** ou área (período anterior tracejado neutro) / barras por período | gauge "deste mês", donut por mês |
| Composição de um total (2–4 partes) | barra empilhada única + rótulos com % | donut com legenda distante |
| Status / alerta | palavra + ícone + cor ("Atrasado ⚠", "On track ✓") | só ponto colorido |

**Regras:**
- **Cor nunca é o único sinal**: todo delta leva sinal (+/−) ou seta; todo status leva palavra ou ícone; séries têm
  rótulo direto ou padrão (tracejado, hachura — como as barras hachuradas de `DftsSH-jnfs_1`).
- No máximo **1 gauge/anel por card e 1–2 por tela**; o resto do painel em barras/linhas. Em painel **operacional**
  (decisão imediata, uso diário) **sem gauge/anel**: barras/linhas; em painel de **cliente/vitrine** um anel-hero de meta é aceitável.
- Anéis concêntricos de "mix" (Crop Mix, Energy Mix, "By project") (complemento): troque por barra empilhada ou
  barras horizontais quando o usuário precisar comparar as partes; mantenha o anel só se a leitura for "total + 1 destaque".
- Escala de cor sequencial (heatmap, matriz de risco) só com o **número dentro da célula** ou legenda de faixas.
- Teste em escala de cinza (complemento): se o card perde o sentido, falta forma/texto.
- Divergência registrada, não resolvida por gosto: quando o usuário pedir "dashboard gamificado", siga §7 **com** este
  critério; quando pedir "painel de análise/gestão", comece por barras e linhas.

