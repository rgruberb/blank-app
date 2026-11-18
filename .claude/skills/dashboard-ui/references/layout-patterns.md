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

Regras que se repetem: histórico em neutro + destaque no "agora"; nenhum gráfico 3D; legendas como lista
tabular; eixos mínimos. Para cores e marcas, use a skill `dataviz`.

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

**Leitura honesta das referências:** nenhum dos 18 reels mostra gamificação explícita — **não há pontos/XP, níveis,
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
| métrica de progresso | % da equipe/área no prazo (gauge "92% TODAY"), checklists por ordem de serviço | 1 meta pessoal grande (anel), marco seguinte com prazo |
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
