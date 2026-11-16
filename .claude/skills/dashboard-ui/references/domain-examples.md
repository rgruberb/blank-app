# Exemplos por domínio — o que cada referência faz e o que copiar

Descrições feitas a partir das folhas de contato (12 quadros por reel). Textos muito pequenos são citados só
quando legíveis. Hex aproximados. Itens marcados "(complemento)" não aparecem na referência; são sugestões para
completar o padrão.

---

## 1. Vendas de varejo — `De12lc1vUmr` (@_code_and_chill_)
**Tema:** claro monocromático com versão dark. Fundo `~#eceeed`, cards brancos `~#f7f8f7` e cinza `~#e2e4e3`,
cards-destaque e rail `~#0f1110`, texto quase preto.

**Estrutura comum:** logo quadrado preto + "Cellar Supply Co."; **top nav em pílulas** (Dashboard, Orders, Products,
Customers, Messages com contador, Analytics, Automations — ativo em pílula preta); **rail de ícones vertical flutuante**
(pílula preta) à esquerda; ícones à direita.

**Telas**
- **Dashboard:** título + tabs pequenas (Overview…) + "Export" em pílula preta. 4 KPI cards **com visuais diferentes
  por métrica**: preto com mini-barras (`$48,322`), branco com linha (`$39,496`), cinza com anel de progresso
  (`3,642`), cinza com barras (`4.8%`). Abaixo, card preto **"Sales performance" com gauge semicircular** (marcas
  ao redor, valor "79%" ou "86%" crescendo) e card claro de receita com barras verticais cinza.
- **Analytics:** segmented de período, 5 KPI cards com sparkline (o 1º preto, `$37,163`), gráfico de área largo com
  tooltip, coluna de breakdown com barra empilhada e lista.
- **Spring Launch (campanha):** header com descrição, avatares e indicador de progresso circular, CTA preto; kanban
  de 4 colunas com cards de tarefa (tag, título, barra de progresso, avatar).
- **Dark:** mesma tela em `~#0d0e0e`, cards `~#1a1b1b`, ativo vira pílula branca.

**Animação:** troca de tema com `document.startViewTransition` + `clipPath: circle()` expandindo a partir do
botão de tema (no quadro 10 o círculo preto cresce do canto inferior esquerdo), `duration: 620`,
`pseudoElement: '::view-transition-new(root)'`. Na troca de página o conteúdo esmaece/desfoca e o novo entra.

**Copiar:** KPI-mestre invertido; cada KPI com o mini-gráfico que combina com a métrica; disciplina de cor
(só o verde dos deltas tem cor); rail flutuante + top nav em pílulas.

---

## 2. Gestão de projetos em equipe — `Deoi1WhP83h` (@_code_and_chill_)
**Tema:** escuro neutro. Fundo `~#141517`, superfícies `~#1b1c1e`–`#25262b`, bordas sutis, cantos ~16–20px; o próprio
app oferece Glass "Clear/Tinted". Destaques: azul `~#3b82f6` (logo, CTA, Up next), magenta `~#e0337f` (accent
escolhido, checks, CTA "Join"), anéis rosa/verde/azul.

**Telas**
- **Home "Good morning, Lin":** subtítulo com data e "4 meetings and 6 tasks left today"; faixa de stats sem cards
  (Done today 3/8 · Focus today 1.1h · Overdue 0); CTA "New task" + CTA magenta com horário da próxima reunião.
  Cards: **Today** com 3 anéis concêntricos (Tasks 3/8, Focus 1.1h/2h, Meetings 1/4) e legenda vertical colorida;
  **Up next** com o próximo evento num bloco azul (em 20 min, "Tide sync review", avatares, botão Join) e agenda
  com barras coloridas à esquerda; **Focus** com timer circular âmbar "24:43" + Pause/End; **My tasks** com
  checkbox circular, tag de projeto, prioridade (Urgent vermelho, High laranja), concluídas com check magenta;
  **This week** "27" com barras rosa por dia.
- **Ilha de foco no topo** (estilo dynamic island): pílula preta "Focus 24:56" que expande para card
  "25-minute block · 24:58" com botões; toast "Focus started — notifications are held".
- **Tasks:** faixa Open 31 · Due this week 11 · Overdue 0 · Done this week 26; filtros em pílula; Board/List;
  kanban In progress / In review / Done com tags de projeto coloridas, prioridade, **barra de progresso fina**, avatar.
- **By project:** donut segmentado "333 finished" + legenda tabular (Orbit 2.0 launch 78 23%, Tide mobile app 67 20%…);
  "Focus 807 hours, about 63h a week".
- **Settings:** perfil "Lin Zhao"; sub-nav com ícones quadrados coloridos; Notifications (toggles magenta); Appearance
  (Theme Light/Dark/Auto, Wallpaper com 10 miniaturas nomeadas: Ash, Sand, Sage, Aurora, Smoke, Tide, Bloom, Ember,
  Grove, Dusk; Accent com 6 swatches; Glass Clear/Tinted; **Reduce transparency**); Focus (Session 25 min / Break 5 min);
  Data (Export tasks as CSV, ação destrutiva em vermelho).

**Animação:** troca de tela com forte motion blur vertical; ilha que expande.

**Copiar:** home pessoal com anéis + "up next"; faixa de stats sem caixa; anatomia do card de kanban; Settings
com "Reduce transparency"; ilha de estado no topo para um modo ativo (foco, gravação, sync).

---

## 3. Portal de corretora de seguros marítimos — `DfCWtPgPcfP` (@_code_and_chill_)
**Tema:** par dark/light ("Moorly"). Destaque teal `~#4fb1a2`.
- Dark: fundo `~#04121a`, brilho âmbar difuso no topo direito (sol), **ondas teal escuras** embaixo.
- Light: fundo branco com névoa teal `~#e6f7f8` e toque pêssego no canto superior direito; cards `~#d8f3f6`.

**Telas**
- **Home "Good morning, Noa":** subtítulo com resumo do dia; botões "Inbox" + CTA teal. **4 KPI cards tingidos**
  (teal, marrom, azul-acinzentado, ferrugem — `14`, `$308.00`, `$1.75M`, `$34.3k` aprox.) com sparkline em cada.
  Gráfico de área teal largo com tooltip + coluna "Waiting on you" (lista com ícone, título, subtítulo e chip de status).
- **Pipeline:** busca + filtros em pílula, toggle; kanban de 6 estágios, cards com tipo (Hull, Cargo, P&I…),
  empresa, valor (`$85,750`…), avatar e ações.
- **Transição:** a tela vira mar — ondas teal sobem e cobrem tudo antes de revelar a próxima página.
- **Detalhe "Pell Harbor Ferry Co."** (light): breadcrumbs + abas (Overview, Quote, Documents…); **stepper em forma
  de rota** (nós teal ligados por linha; o barco/marcador escuro sobre a etapa atual); **cotador**: valor grande
  (`$66,104` → `$66,500`) que muda ao arrastar um **slider** de limite; card "Indicated premium $66,500" com lista.

**Animação (GSAP):** barco percorre o path da rota — `getPointAtLength`, rotação por `Math.atan2`,
`stroke-dasharray` para revelar a linha percorrida, `duration` ~1.3s (leitura aproximada), `ease: 'power3.inOut'`, e no `onUpdate` reposiciona o barco.

**Copiar:** metáfora do domínio aplicada a componentes funcionais (stepper-rota, transição de ondas) e não espalhada
em tudo; KPI cards tingidos com tons terrosos (alternativa a "todos iguais"); cotador com feedback imediato.

---

## 4. Analytics de receita SaaS — `DffBnb2vlUn` (@_code_and_chill_)
**Tema:** dark azul profundo. Fundo `~#061a2a`→`#0b1640`, **glow radial azul `~#1d3aa8` e teal**, cards `~#122670`
translúcidos com borda azul clara, CTA azul `~#4e6ad1`, série de destaque azul claro `~#6f8ff0` ou verde `~#5ee3a1`.

**Telas**
- **Funnels:** coluna esquerda com lista de funis (nome, taxa, mini barra; selecionado destacado); painel principal com
  abas, 5 KPIs de etapa e **funil em 5 barras verticais** — a 1ª cheia em gradiente azul, as seguintes cada vez mais
  baixas dentro de "trilhos" vazios; tabela de conversão embaixo.
- **Campaigns:** board de 4 colunas (cards com pares de barras de progresso teal/azul) e **detalhe** com funil em
  barras verdes, valor `$10,292` à direita com lista, e barras finas espaçadas ao longo do tempo.
- **Cohorts:** 4 KPI cards translúcidos e **heatmap de retenção em triângulo** (linhas = coortes, colunas = semanas),
  intensidade de azul caindo da esquerda para a direita.
- Entre páginas o conteúdo dissolve num desfoque azul e a pílula ativa do rail desliza.

**Animação (GSAP `slidePill`):** pílula ativa recortada com `clip-path`; a borda na direção do movimento anda primeiro
(~0.3s, `ease: 'power3.out'`) e a traseira alcança depois (~0.55s, `'power3.inOut'`) — durações de leitura aproximada.

**Copiar:** funil como barras dentro de trilhos; heatmap de coorte; luz ambiente atrás do conteúdo em vez de
gradiente nos cards.

---

## 5. App de orçamento familiar — `DfkNvnePItL` (@_code_and_chill_)
**Tema:** dark verde musgo. Sidebar `~#162218`, fundo com manchas verdes desfocadas `~#2c3a2c`, acento menta `~#8af1b6`
(item ativo, CTA, barras, anel).

**Telas**
- **Home "Good morning, Ines":** **cartão de crédito 3D verde** como hero (com sombra e leve perspectiva); saldo
  `$24,627.72` grande com mini-KPIs e área; card de gastos com barras finas menta.
- **Cards:** cartão grande + painel de configurações (limites em dois campos, 4 toggles menta, slider).
- **Insights:** 4 KPIs translúcidos; barras verticais menta com sombra (gastos) + linha (tendência);
  **barras horizontais por categoria** com valores à direita e **anel** de orçamento com valor central.
- Sidebar: logo, itens com contadores, bloco de saldo ou plano no rodapé, usuário.

**Animação:** mesma `slidePill` em vertical (a pílula menta estica cobrindo dois itens e depois encolhe no destino);
o conteúdo desfoca entre páginas.

**Copiar:** objeto do domínio como hero (o cartão); barras por categoria + anel para orçamento; pílula elástica vertical.

---

## 6. Smart home — `DfrqAX9v59S` (@_code_and_chill_)
**Tema:** glass/frosted cinza grafite. Painéis `~#555756`, sidebar `~#414342`, ativo em **pílula branca** `~#dfe1e0`.
Sem cor de destaque — as fotos dão a cor.

**Telas**
- **Home "Good morning, Noor":** linha de 5 tiles de status (cômodos/dispositivos); **câmera hero** (sala) com faixa de
  miniaturas; tiles grandes `20` e `9:00`; **dial de termostato** circular (arco branco, `20.5°`) com +/-; chips de cena
  na base (ativo branco).
- **Security:** grid de câmeras 1 grande + 2x2 com rótulos sobrepostos; chips de filtro; lista de dispositivos.
- **Climate:** dois cards de cômodo com dial (`21.5°`, `18.5°`) e segmented de modo (ativo branco); **grade de agenda
  semanal** (7 linhas x ~24 horas; células brancas = aquecimento ligado) com botões de preset.

**Animação:** `slidePill` com direção detectada (`Math.abs(to.t - prev.t) > Math.abs(to.l - prev.l)` → vertical), e as
bordas do eixo cruzado também animam (~0.4s, `power2.inOut`); conteúdo some em desfoque cinza entre páginas.

**Copiar:** UI neutra quando o conteúdo é mídia; dial para controle contínuo; grade de agenda como heatmap binário.

---

## 7. Plataforma de saúde, prior authorization — `DfV39ohhwAC` (@ui.iliasmiah000)
**Tema:** dark neutro `~#0b0c0e`, cards `~#151618` com borda sutil e cantos ~16px, destaque **mint `~#2fb58f`**,
âmbar para prazos, chips de status azul-acinzentado / verde. Glow verde muito leve ao redor da moldura.
Tipografia sans geométrica, números grandes em peso leve.

**Layout**
- Sidebar larga: logo "Veyra Health", card do usuário, Overview ativo + itens com contadores, grupo de filas
  com pontos coloridos, Settings.
- Topo: busca com atalho, data/hora, ícones (notificação com badge), avatar.
- Header: "Overview" + "Good morning, Dana. 23 cases need attention today." À direita: "All payers", "Last 30 days",
  CTA mint "New authorization".
- **KPI strip sem cards** (5): Active cases 386 · Pending payer 142 (chip âmbar) · Approved 1,127 · Denied 96 (chip
  vermelho) · Median turnaround 3.4 d.
- **"Requests vs decisions"** (2/3): Submitted 1,318 / Decided 1,223 / Backlog change +95; segmented 7D/30D/90D;
  estado 1 = barras cinza-escuro com só a atual em mint; estado 2 = **duas linhas suaves com fita preenchida** e
  coluna destacada com tooltip.
- **"On time decisions"** (1/3): **gauge semicircular de ticks** (mint → âmbar) com "92%" e "1,125 of 1,223 within
  clock"; ao lado "6 h until the first clock lapses", "4 cases lapse within 24 h".
- **"Open pipeline":** **barras de ticks empilhados** (estilo equalizador) por estágio, mint, sobre trilhos de ticks cinza.
- **"Needs attention":** abas Due today / Overdue; paciente, payer, status em chip (Pending payer, Submitted, Ready for
  review), prazo + avatar; "Open queue".
- **Card "Veyra Assistant":** orbe luminoso, "4 Sunvale cases lapse within 12 hours. Follow up by 2 PM", avatares + ID,
  barra âmbar "First clock lapses in", CTA mint "Review 4 cases" + "Dismiss".

**Animação:** entrada escalonada (sidebar → header → cards); linhas desenhando; ticks do gauge acendendo;
barras de ticks subindo.

**Ideia do autor (legenda):** "Sorted by clock, not by date, so the riskiest case is always on top."

**Copiar:** saudação com o que importa; KPIs sem caixa; histórico neutro e "agora" destacado; gauge com contexto ao
lado; card de IA com uma recomendação concreta + CTA + dispensar; ordenar por risco.

---

## 8. Série glassmorphism — @code.xr
Snippet comum: `motion.div whileHover={{ y: -5 }} className="glass-card p-6 rounded-2xl"`, título
`text-sm text-white/60`, valor `text-2xl font-bold text-white`, delta `text-emerald-400` com `ArrowUpRight`
(lucide-react; também `ShoppingBag`, `Users`, `DollarSign`). Stack: React, CSS, Framer Motion.

- **Login V3 — `DeoGCPlzKOs`:** fundo preto `~#05060b` com ondas 3D escuras e faixas ciano. Card de vidro escuro
  `~#25313d` com **cantos superior-esquerdo e inferior-direito chanfrados** marcados por triângulos ciano. "Welcome
  **Back**" (email, senha com olho, Remember me, Forgot?, botão "Sign in" ciano, Google/Apple, "Sign up") e
  "Create **Account**" (Full name, email, senha + confirmar lado a lado, termos, "Create Account"). **Transição:**
  campos somem → card vazio só com o logo (quadrado ciano dividido na diagonal) → anel de luz pulsa ao redor →
  o card se reajusta à altura do outro formulário e os campos entram.
- **Dashboard V7 + CRM — `DfHrMboTVDZ`:** sobre foto de sala (madeira, TV, planta). Rail vertical escuro com tooltip,
  pílulas laranja `~#d59353` no topo. **Home:** 1º KPI em vidro âmbar, demais escuros (`$99,664`, `35`, `45,000`,
  `$59,900`); **barras verticais como pilares de luz** (gradiente branco→transparente, selecionada em laranja com
  rótulo), donut multicolor (laranja, azul, amarelo, verde), cards "98 orders", "17 ...". **Customer Intelligence:**
  perfil com avatar azul `~#94a6fa`, linhas roxa/verde, gauge verde "94%", barras horizontais coloridas, tabela.
  **Performance & Audit:** KPIs em linha. Páginas entram do desfoque.
- **Dashboard V8 — `DfKPFDwz2aA`** (no vídeo aparece "V18"): começa só com a foto; os painéis surgem do desfoque.
  Sidebar glass com marca e **títulos em serifa** ("Good Afternoon, Sarah", "Leads", "Reports", "Calendar"). Coluna
  direita **fixa entre páginas** com 3 widgets: azul `~#7488c7` com barras brancas (`2,008`→`3,241`), bronze
  (`$2,078`→`$2,450`), escuro com área (`68,048`→`95,215`) — os números contam ao trocar de página. Leads: 4 KPIs +
  tabela com avatares coloridos; Reports: barras azul-claras + donut; Calendar: grade com eventos coloridos.
- **Sidebar V5 — `DfMH6YTTcwx`:** detalhado em `glassmorphism.md`.

**Copiar:** glass só sobre fotografia ou fundo rico; um card de cor sólida para ancorar o olhar; hover com elevação
de 5px; serifa para títulos dá ar "premium"; widgets persistentes entre páginas; transição de formulário pelo logo.
