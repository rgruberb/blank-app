# Exemplos por domínio — o que cada referência faz e o que copiar

Descrições feitas a partir das folhas de contato (12 quadros por reel; 18 reels). Textos muito pequenos são citados só
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

---

## 9. Série "OS" de operações sobre foto aérea — @felvrabr (`Dfui4V5BMbz`, `DfpCOjIB1Rb`, `Dfr9S5yhlvX`)
Os três reels são **o mesmo template** com tema trocado por domínio (estúdio FELVRA; legenda genérica "Follow for more
UI & UX", áudio só música — tudo abaixo vem das imagens). Estrutura comum, quadro a quadro:
abertura com o mockup num tablet sobre fundo liso da cor do tema, nome da marca gigante em contorno atrás e
"<Marca> <tipo> OS" no canto → zoom no produto → popover de um objeto do mapa → ação → painel "Overview" (rolagem) →
close-ups desfocados/zoom em gráficos → mockup de novo → tela preta "FELVRA" ("Chame no direct · @felvrabr").

**Esqueleto (comum aos três):** a **foto aérea ocupa a tela toda e é o próprio mapa**; por cima, em vidro escuro:
logo + busca no topo esquerdo, sidebar flutuante curta (6 itens, ativo em pílula translúcida), coluna direita
"<X> Overview" (sino com ponto + avatar com iniciais na cor do acento + nome + cargo), toggles de camada empilhados à
direita do mapa (ativo em pílula do acento), e uma faixa inferior com 2 cards (anéis concêntricos + barras de 12 meses).
Tipografia sans geométrica, números grandes em peso leve com unidade pequena ao lado ("0.77 index", "27 %", "47.4 MWh").
Cards `~#182313`–`#2b3827` (Verdan), cantos ~16–20px, borda clara 1px.

### 9a. Verdan Farm OS — `Dfui4V5BMbz` (agro; principal referência de progresso e gamificação)
**Tema:** fundo de apresentação sálvia `~#7b8e72`; UI verde-oliva escuro `~#182313`/`#212d17`; acento **lima `~#c6e17a`–`#cee980`**;
âmbar/laranja só para alerta ("Dry", "Low moisture").
- **Mapa:** talhões com rótulo-pílula ("Field 01", "Field 02", "HQ"); o Field 03 é um **polígono preenchido em âmbar**
  com etiqueta "Field 03 · Dry". Camadas: **NDVI** (ativa, lima) / Moisture / Yield / Pivots.
- **Popover do talhão** (card escuro ancorado ao pin): foto do trigo, chip âmbar "Low moisture", "Field 03 · Wheat"
  + metadados, valor **18%** com comparação à direita (texto pequeno, ilegível; parece "vs target"), linha de
  NDVI/temperatura/data e **CTA lima cheio "Start irrigation"**.
- **Feedback da ação (quadros 5 → 6):** o CTA é substituído por "✓ Irrigating · 40 min" com spinner, a etiqueta do
  talhão deixa de ser "Dry" e **o polígono passa de âmbar para verde-claro translúcido**. Ação → estado visível no
  próprio objeto, sem modal.
- **Farm Overview (Ana P., Farm manager):** grade 2x2 de KPIs: **Avg. NDVI 0.77 index** (chip "Healthy", linha
  crescente); **Pivots running 2** (chip "2 running", gráfico de **pirulitos** com marcador "Max 4", o ativo em lima);
  **Soil moisture 27% → 31%** (chip "Rising", linha com ponto); **Crop health gauge semicircular de ticks
  33% → 92% "TODAY"** (o número conta e o arco enche entre os quadros 7 e 8).
- **Plano de irrigação "IR-0317 · Field 03 · Wheat · 40 min"** com avatar do agrônomo (Marcos Lima) e menu `⋮`;
  abaixo **"Zones irrigated 3/4"** como **barra segmentada em 4 células** com % à direita (0% → enchendo).
- **Recent Messages:** "Marcos Lima — Field 03 looked dry on this morning's walk" + "View all".
- **Crop Mix:** anéis concêntricos (lima, verde médio, branco) com total "1,240" no centro e legenda Soybean 48% /
  Corn 32% / Wheat 20%. **Harvest Forecast** ("Thousand tons per month, next 12", dropdown "Next 12 mo"): 12 barras em
  pílula cinza-gradiente dentro de trilhos, **só Mar em lima com tooltip-pílula "Mar · 4.2k t"**.
- **Animação aparente:** zoom/dolly da câmera do mockup, popover que entra sobre o pin, troca de estado do CTA,
  gauge e números contando, close-ups com desfoque de profundidade (quadro 9).

**Elementos de gamificação (o que há e o que não há):** não há pontos, níveis, badges, streaks nem ranking. O que
existe é a **camada de progresso/meta** que serve de base para gamificar: gauge que enche até o "hoje" (92%),
checklist segmentado "3/4" que completa célula a célula, comparação com meta no popover, chips de estado
("Healthy", "Rising", "Low moisture"), limite visível ("Max 4") e **feedback imediato da ação no mapa** (âmbar → verde).
Ver "Padrões de gamificação" em `layout-patterns.md`.

### 9b. Helion Solar plant OS — `DfpCOjIB1Rb`
**Tema:** apresentação cinza-azulado `~#878d9d`; UI ardósia `~#171b26`–`#20222f`; acento **âmbar `~#f0b048`**.
- Mapa = foto dos painéis; camadas Block A / **Block B** (ativo) / Block C / Substation; o bloco B-12 aparece
  contornado em grade âmbar com pin "B-12 · 312 kW".
- Popover "Inverter B-12" (foto, chip "Alert", 312 kW, comparação ilegível) com CTA **"Dispatch technician"** →
  vira **"Crew 3 · ETA 11:50"**.
- **Plant Overview (Laura M., Site manager):** Generation today **47.4 → 48.6 MWh** "On track"; Crews on site **2 → 3**
  "2 active" (pirulitos, "Max 4"); Irradiance **817 → 842 W/m²** "Clear"; **Performance ratio 33% → 91% TODAY**.
  Work order "WO-2214 · Inverter B-12 · fan fault", Crew 3 Rafael Costa, **"Pre-job checklist 3/4"** segmentado.
  Recent Messages: "Block D crew — Rows 1-20 washed, output up 3%".
- Energy Mix (anéis, "6.4" no centro): Grid export 62% / Battery 26% / On-site use 12%. Generation "GWh per month,
  last 12 months", **Jul em âmbar "1.42 GWh"**.

### 9c. Maren (resort de vilas de praia) — `Dfr9S5yhlvX`
**Tema:** verde-petróleo escuro `~#132622`–`#1c3132`; acento **menta `~#6cf0c9`**; reservas em **coral `~#c06860`**.
- Sidebar (aparece no quadro 5): Overview, Villas, **Reservations** (ativo), Guests, Concierge, Revenue. Topo: período
  "Dec 27 – Jan 3", sino, avatar "Lena K.".
- Foto aérea do resort com pins ("Villa 04 · $1,070/night" em menta; "V06 · Booked" escuro), chip "29° · Calm sea",
  filtros-pílula (All villas / Private pool / Garden) e popover de vila com "Check dates".
- **Card de ocupação:** anel "5/6" + **83%** (texto "1 villa left") → **95%** → **100%** no fim — a meta se completa
  à medida que a reserva entra.
- **Reservations (Gantt):** dias no topo, **hoje "31" destacado em coluna mais clara**, barras coral com nome e noites;
  hover/seleção mostra tooltip com datas e valor; legenda Booked/New + Filters + CTA menta "New booking".
- **Ocupação:** "94%" + grade de células menta (calendário-heatmap). **Revenue per night `$5,350` New Year's Eve**: área
  menta com pico e tooltip "31 Dec · $6,420".
- **Chat do hóspede** (Elena Hartley): "Hi! Any villa left for New Year's? We're 4 people" → **chip de resposta
  sugerida "Send booking · Villa 04"** → bolha menta "Villa 04 is yours: 29 Dec – 2 Jan, private pool" → "Perfect,
  thank you!". Ao mesmo tempo **uma nova barra menta "E. Hartley · 4 nights · $4,280"** aparece no Gantt.

**Copiar (série):** o objeto do domínio (fazenda, usina, resort) como canvas principal, não como foto decorativa;
**ação no popover → estado muda no mapa e no painel** (fecha o ciclo); KPIs 2x2 com chip de estado em palavra
("Healthy", "On track", "Clear"), não só seta; um card "plano/ordem de serviço" com responsável + checklist
segmentado; barras de 12 meses com **um mês destacado e rotulado**; mesmo layout, acento por domínio.

---

## 10. Glassy Dashboard V30 — `Dfj_FGsTAVB` (@code.xr)
**Tema:** glass **claro** cinza-mauve `~#585256`–`#7f7472` sobre foto de quarto (luminárias pendentes pretas, cama).
Acento azul `~#4a8fe0`/`#6888a8` (a legenda promete "Premium Purple & White"; no vídeo o que se vê é azul e branco).
- Abertura: só a foto e a moldura do app; os cards **condensam do desfoque** (quadros 1 → 3).
- **Overview:** top tabs (Overview ativo + 3), rail de ícones à esquerda; card "Team" com **pilha de avatares
  coloridos**; card com toggle azul e **dial circular** (anel azul com knob, valor **50° → 65°**); `$19.5k` → `$23.1k` com área
  suave e rótulos de mês; mini-cards (barras finas "1.2M", `$4,8..`); barras verticais com **a atual em azul** e rótulo;
  coluna direita com toggles, card de perfil com player (botão play branco).
- **Reports:** 4 KPIs (`$8.67M`, 7.4%, 3.7%, ...) e **donut azul/branco que entra girando** do desfoque.
- **Deals Pipeline:** 4 KPIs (`$342.7k`, `$74.7k`, 8%, `$8.9k`), abas, CTA branco em pílula, **kanban de 5 colunas**.
- **Customers:** 4 KPIs + tabela com avatares de contorno colorido.
- **Products:** grade de cards com **ícone 3D brilhante** (rosa, verde-limão, verde, azul, vermelho, ciano, roxo,
  laranja), preço, **barra de estoque verde** e toggle azul de ativo.
- Snippet: o mesmo `StatCard` da série (`motion.div whileHover={{ y: -5 }}`, `glass-card p-6 rounded-2xl`,
  `text-emerald-400`, `ArrowUpRight`). Legenda: React, CSS3, "Smooth Hover Animations".

**Copiar:** glass claro (não escuro) quando a foto é clara; ícone 3D colorido como placeholder de produto; dial
que anima até o valor ao entrar; o mesmo esqueleto (KPIs + conteúdo) repetido em todas as páginas.

---

## 11. Ad campaign de gravadora — `DfXoXVFPBfd` (@_code_and_chill_)
**Tema:** dark quase preto `~#131416`–`#15161b`, CTA/pílula ativa **azul `~#7088e0`**, cores de canal (azul, amarelo,
verde, vermelho) só em gráficos. Marca no canto lida como "Amplo" (pequena, incerta). Áudio só música.
- **Top nav em pílulas** (ativa preenchida azul) + ícones e CTA azul no topo direito; nada de sidebar.
- **Overview "Good morning, Imogen":** subtítulo com 3 metadados; ações à direita (secundária + CTA azul). Card de
  gasto: **`£19,076.74` → `£22,731.21` → `£23,094.80`** (conta ao entrar) com 3 mini-KPIs e um bloco com botão azul;
  **anel segmentado multicolor (azul, verde, amarelo, vermelho) com orbe azul brilhante no centro** e legenda em
  2 colunas — leitura: distribuição de verba por canal. Card largo com `75,365`, segmented de período e área azul que
  sobe no fim. Embaixo: tabela de campanhas com ícone, plataformas em pílulas e status; card lateral com 3 números
  em quadrados + **barra de progresso azul** (provável meta/pacing; rótulos ilegíveis).
- **Reports:** lista de relatórios salvos à esquerda (com botão circular), abas/segmented, **"Total 140,708"** em
  **barras horizontais coloridas** por canal (azul, amarelo, verde, vermelho, vazias) com valor à direita + tabela.
- **Campaigns:** título + descrição + CTA; faixa de **aprovações pendentes** (2 linhas com botões azuis) acima da
  tabela; toggle **List ↔ Board**: board de 5 colunas com cards que têm barra azul fina e avatares.
- **Animação:** a pílula da top nav **estica entre itens** (quadros 4 e 8 mostram a pílula alongada) — snippet
  `slidePill(pill, target)` com `gsap.to(..., { [lead]: ..., duration ~0.3, ease: 'power3.out' })` e trail
  `~0.55, 'power3.inOut'`; o conteúdo some e volta entre páginas.

**Copiar:** saudação + gasto que conta; anel de distribuição com orbe como "assinatura" visual; reports por canal em
barras horizontais; faixa de aprovações pendentes acima da lista; toggle lista/board.

---

## 12. CRM de estúdio de design de interiores — `DfeT74YvQaD` (@_code_and_chill_)
**Tema:** monocromático **marrom-sépia quente** (`~#261e13` fundo, cards `~#483c30`–`#4b3f2f`, texto creme), glow
avermelhado no topo; ativo em **pílula creme** na top nav e quadrado claro no rail de ícones. Nenhuma cor saturada.
- **Overview:** breadcrumb + título; card `$41,849.73` → `$48,490.60` (conta) com linha; card largo com
  2 valores, segmented e linha + barras fantasma; listas embaixo (projetos/tarefas com ícone e valor), barra de
  progresso fina.
- **Pipeline:** abas + busca + filtros-pílula; **4 colunas** de cards de cliente (avatar, nome, subtítulo, valor e
  botão circular de ação).
- **Schedule:** chips de pessoa com avatar (filtro por designer) + **agenda em colunas por dia** com blocos de evento
  e marcador do horário atual.
- **Growth:** 4 KPIs, barras verticais creme e **anel de progresso** com % no centro (meta; rótulo ilegível).
- **Snippet:** `slidePill(pill, target, { radius = 12 } = {})` com `clip-path: inset(... round ${radius}px)` e o comentário
  "the leading edge runs ahead, the trailing edge catches up" (leitura aproximada); durações ~0.30 / ~0.55.

**Copiar:** paleta de uma cor só em tons quentes para marcas de design/lifestyle; agenda filtrada por pessoa;
pílula elástica com raio configurável (não só 999px).

---

## 13. Admin de e-commerce (velas) — `Dfct0mNvg3f` (@_code_and_chill_)
**Tema:** dark vinho `~#1e0f12` com **sidebar magenta `~#781840`** (gradiente para preto), glows laranja e azul
`~#342b48` nos cantos; CTA/pílulas **rosa `~#bf6888`**; categorias em rosa, amarelo, azul e laranja.
- **Sidebar larga** com grupos rotulados, badges, sub-itens expansíveis (Products → 3 filhos) e **card no rodapé com
  anel** (plano/uso; texto ilegível).
- **Overview "Good morning, Noor":** `£9,318.40` com chips de filtro; **área empilhada rosa/amarelo/azul** larga;
  coluna direita com **"23"** + **3 barras de progresso coloridas** (rosa, azul, amarelo) + lista com valores + **anel**
  com texto; faixa de 4 mini-KPIs com ícone circular colorido no canto.
- **Products:** abas + busca + filtros-pílula (ativo rosa) + toggle de visualização; **grade de cards com monograma em
  fundo pastel** (SF, FL, SC, WR, ST, AD, NJ, GM — placeholders de produto) ↔ **tabela** com miniaturas e chips de status.
- **Analytics:** 4 KPIs com ícone colorido (rosa, amarelo, azul, laranja) e **área empilhada** larga com faixa de
  gradiente na base.
- **Snippet:** variante do `slidePill` que anima as bordas do eixo cruzado ("stretches like a strap"),
  `duration` ~0.30 / ~0.55 / ~0.45 (leitura aproximada).

**Copiar:** área empilhada por canal/categoria; monograma pastel como placeholder de produto; barras de progresso de
meta na coluna lateral; grid ↔ tabela no catálogo.

---

# Rodada 3 (perfis do Instagram, 18/11/2026)

Seções 14–21 vêm de leitura por frames (reels de 5–6 s, texto pequeno) e de prints únicos. Só os itens com
arquivo em `assets/visual-refs/` têm imagem; os demais são descrição apenas. Hex aproximados.

## 14. Verificação de identidade "Vigilo" — `Dfz0mLAzsjg` (@_code_and_chill_, sem imagem)
**Tema:** claro, fundo cinza `~#EDEFEE`, cartões **verde-menta `~#CFE5E0`** + **um cartão preto** como quebra; o resto
neutro. "Good morning, Ines".
- **Overview:** KPIs `94.5K` verificações, `40K`…; botão de estado "All checks passing"; **heatmap de quadrados
  arredondados** (menta/cinza, legenda Passed / Declined / Flagged) para volume por período; card preto com lista.
- **Reports:** linha suave sobre área menta + **linha preta tracejada "Compare with last period"**; card "Total checks 15,180".
- **Protection:** card de visão geral com barras pretas + **lista de regras com toggle preto e botão "Review"**.
**Copiar:** acento único + preto como segundo destaque; comparação com período anterior tracejada (não uma 2ª cor);
regras/políticas como lista de toggles.

## 15. Vendas de pequena empresa — `Dfjx6Stv3-d` (@_code_and_chill_, sem imagem)
**Tema:** dark `~#1E1E21` + **laranja `~#FF6B35`** único; item ativo da sidebar em bloco laranja.
- **Orders:** kanban New / Processing / Completed / Delivered; cards com ID, cliente, valor, selo de status.
- **Sales:** **barras-pirulito (haste + ponto) com linha de meta tracejada** — acima da meta em laranja, abaixo em
  cinza, a barra atual em branco; valor grande `£41,506` + 3 números menores; seletor de período.
- **Channels:** **barra segmentada de 1 linha em 4 cores + 4 cards de valor** abaixo; linha de vendas; lista de canais
  com barra de progresso.
- Abre com o conteúdo vazio (loading) e os blocos entram.
**Copiar:** a cor mostra **quem bate a meta**, sem eixo; partes do total em barra segmentada + cards.

## 16. Gestão de crédito privado — `Dfo0F0Pvo4Y` (@_code_and_chill_, sem imagem)
**Tema:** **terracota `~#B8664D`–`#D98A6C` + acento verde-limão `~#C8F23A`**, sidebar clara/oliva — fora do clichê azul
de finanças.
- **Imóvel "Casa Duna":** foto grande + miniaturas; gauge semicircular "63,8%" em limão; tabela curta.
- **Risk:** **matriz de risco 5x5** em escala de um tom (claro → escuro) com números nas células, **célula selecionada
  com contorno no acento**; abas Heatmap / Watchlist / Insights; painel "Top risk `$10.54m`" com 4 imóveis.
- Snippet `slidePill` com clip-path, `duration: 0.35`, `ease: "power3.inOut"`.
**Copiar:** heatmap de risco monocromático + seleção por contorno; paleta quente para fintech B2B.

## 17. Skeuomorphism Dashboard — `DfuS2Jbzsjt` (@code.xr, sem imagem)
**Tema:** **creme `~#EFE7DC` com relevo** (luz em cima, sombra embaixo), acento coral/laranja, marrom/preto e um
verde-azulado escuro para contraste. Barra superior marrom com **pílula de comando/IA** ("Can you fund $250 to
Jenny…") como ponto focal.
- **Overview:** "Total balance `$527,495.35`" + Transfer / Request; cards de valor; barras pretas com **uma laranja**.
- **Reports:** 4 KPIs, renda × despesa (renda com área laranja), donut por categoria + barras de progresso.
- **Savings & Goals:** total poupado com barra laranja, **colunas em relevo** (última laranja), toggles "Auto-save",
  **cartões de meta com anel** (74/64/63/66%) e card pontilhado "Add goal".
- Entrada: blur → nítido (framer-motion), `StatCard` no código.
**Copiar:** alternativa "tátil" ao glass para fintech pessoal; metas como anéis + card "Add goal" tracejado.

## 18. Curved Sidebar — `Dfw4gEmz87N` (@code.xr, sem imagem)
Cápsula vertical de vidro recolhida (avatar com ponto verde, 5 ícones, card com cristal, settings/sair) → expande em
**painel com laterais côncavas** ("LUMEN"), perfil, seção MENU com **submenu aninhado** (Bookings → Upcoming /
Calendar / History), cartão "NOTICE", rodapé. Vidro definido por **borda 1px ~30% branco**, sobre fundo listrado de
alto contraste. Complementa `DfMH6YTTcwx` (sidebar V5).

## 19. Ember Dashboard V29 — `DfrtgFyTmOM` (@code.xr, sem imagem)
**Tema:** branco com sidebar escura estreita; **coral `~#F26B5E` só no que pede ação**.
- **Overview:** "Good afternoon, Daniel"; card "Close the quarter stronger `$144K`" com slider; "Pipeline by stage
  `$138K`"; card coral "Hot leads"; semana; "Follow-ups"; card escuro de cliente.
- **Saved:** biblioteca de cards (alguns em gradiente coral→rosa) + painel "Collections".
- **Tasks:** **"Overdue 2" em card coral cheio + Today / Upcoming / Completed brancos**; filtros-pílula; listas com
  selos High/Medium.
- `motion.div whileHover={{ y: -2 }}`.
**Copiar:** **acento = urgência** (atrasado, lead quente), não decoração; mesmo shell para vários módulos.

## 20. Apps de investimento / trading — "Markets" `DXeeUP7FKGs_1` (@rish_designs) e Borea AI `DSIMwtvDluO_1–3` (@ramotion)

### 20a. Markets (iOS, dark `~#0B0B0D` + verde-limão `~#D4FF3A`)
Legenda do autor (resumo): não foi feito para "parecer app de trading", e sim para **o momento em que a pessoa decide
comprar, vender ou esperar**; a tela responde na hora o que está se mexendo e para onde olhar; mostra só sinais
imediatos e contexto suficiente; o bloco de IA existe para **reduzir dúvida**, não para impressionar; UX boa é tirar
atrito entre intenção, decisão e ação.
- **Lista "MARKETS":** busca "Search stocks, crypto…"; abas Stocks / Crypto / ETFs / Kits (ativa sublinhada);
  **"Today's Movers"** em cards horizontais (logo, nome, preço, pílula de variação); **"All Assets"** em linhas:
  logo + **ticker em negrito + nome completo embaixo** à esquerda, **preço + variação com sinal e cor** à direita;
  tab bar com a aba ativa em pílula limão.
- **Detalhe do ativo:** nome + tag de setor ("Tech"), preço grande + variação "(Today)"; candles verde-limão/vermelho;
  **seletor 1D · 1W · 1M · 3M · 1Y · ALL** (ativo em pílula limão); **card "AI Report"** com selo de veredito
  ("BEARISH" vermelho) + 2–3 frases + "View Full Analysis →"; **Sell (vermelho) e Buy (limão, texto preto) do mesmo
  tamanho, lado a lado, fixos no rodapé**.
- Preço em sans, dados em mono.

### 20b. Borea AI (dark quase preto, marca azul `~#3D5BF5` + laranja `~#F26B3A`)
- **Mobile:** **rosca segmentada laranja→azul com score "74" no centro**, cards de métrica, linha laranja no rodapé.
- **Web:** listas prontas em vez de feed — **"Top Traded Stocks"** (cards com logo; selecionado = fundo azul / borda),
  faixa "Activate Daily Free Predictions" + Sign Up, **"Top Traded Index ETFs"** (cards de ticker com variação verde),
  **"Top Daily Movers"** em duas colunas **Gainers (verde) / Losers (vermelho)**.
- **Kit:** chip de ticker "VOO +0.07%" com nome do fundo embaixo; set de ícones; **gráfico de linha com cursor
  vertical + ponto de leitura + seletor de período**.
- Verde/vermelho são **só** variação de preço; as cores de marca ficam em score, seleção e gráficos.
- Erro do case: ticker da Apple como "APPL" (correto AAPL) — revise dados de mockup.

**Copiar (os dois):** ver `layout-patterns.md` §8 (momento de decisão e anatomia do card de ticker).

## 21. Fluxos completos de app — @ui.pixel (reposts; sem imagem)

### 21a. Lavanderia "Qwash" — `DX_bA4rCWf0` (design @oshioke.ui)
Cabeçalho em gradiente roxo `~#4B3FA0 → #7B6FD6` e botões-pílula em gradiente; corpo branco com cards arredondados.
Fluxo em 10 telas: **My Offer** (cupons) → **Profile** (anel "90% Complete", endereços, cartões salvos) → **Home**
("Hi J.Snow", 2 cards de serviço com preço, **"Active Orders" com progresso em 4 etapas: Picked → Washing → Out for
delivery → Delivered**, oferta) → **Explore Services** (grade 2x2 com ilustração, preço e selo verde de desconto) →
**Services Overview** (abas, lista de preços com stepper − 0 +, **rodapé fixo "Delivery Fee $5 / Estimated Total $21"
+ "Schedule A Collection"**) → **Order Details** (chip "On Process", o mesmo stepper de 4 etapas, mapa com rota
Pick-Up → Delivery, chat de suporte, "Cancel order") → **Collection & Delivery** (data/hora, frequência, endereço) →
**Review Order** (checkout detalhado + "PAY NOW"). Tab bar de 5 abas com **botão central circular** para a ação principal.
Atenção: o exemplo mostra subtotal $26 e botão "$43" — inconsistência, não copie.

### 21b. Viagens "WayLoo" — `DVv7OOECewR` (design @webdesign.uiux)
Preto + **laranja `~#FF6A1A` só em botões, selos e aba ativa**, brilho laranja difuso no fundo. Splash em malha de
gradiente; home "Hello, Denis! *You want to book something?*" (2ª frase em cinza) com cards Plane / Train / House e
selos de contagem; detalhe de carro com **cards de vidro escuro de borda fina** (consumo, aceleração, câmbio) e botão
360°; login com social; **tab bar flutuante em pílula** com aba ativa laranja.

### 21c. Dashboard de RH — `DYJwy9aCSYP` (design @webdesignssphere)
Fundo azul-gelo `~#EAF1F7`, cards brancos/azul-claro muito arredondados, verde `~#8FD694` na aba ativa e verde-petróleo
`~#2F6B73` num card de destaque. "Good morning Jhon"; card de pessoa (foto, cargo, "4+ years experience", ligar/e-mail);
**"46,5 avg hours" com gráfico de pontos (altura = nº de pontos)**; donut de equipe; hiring com fotos + barras verdes;
salários em lista. Fotos de pessoas humanizam o painel. Apresentado em 3 versões (plano, close inclinado, notebook).

**Copiar (21):** progresso do pedido em 4 etapas **repetido** na home e no detalhe; rodapé fixo com total + 1 CTA;
uma ação principal destacada na tab bar; acento só em ativo/CTA/selo.

---

# Rodadas 2, 5, 6 e 7 (Instagram e Facebook, 18/11/2026)

Prints com arquivo em `assets/visual-refs/` estão marcados; o resto é só descrição. Hex aproximados, lidos de print.
Os mockups desta leva têm **vários dados inconsistentes** (listados em cada item): revise números de exemplo antes de
mostrar a cliente.

## 22. Fintech web escuro do Orbix Studio (@shohan.designs)

### 22a. Vaulto — `DfcdrhgFFMR` (prints `DfcdrhgFFMR_1.jpg` plano esquerdo, `_2` plano direito, `_3` recorte inclinado)
Dark quase preto `~#0B0B0C`–`#141414`, **laranja `~#FF5A1F` só no CTA "Add Funds" e no ponto do tooltip**, vermelho
`~#E0302A` como série de gasto, verde/vermelho nos deltas. Legenda: "visual weight given to the information you'd scan first".
- Sidebar com grupos em caps cinza **GENERAL / TOOLS / INSIGHTS / OTHER**, badges ("3", "20$"), card "Upgrade to PRO" no rodapé.
- **Total Balance `$12,420.22` + chip "+24%"**, logo abaixo a composição "Cash $7,000 · Crypto $5,420.22"; ações
  "+ Add Funds" (pílula laranja cheia) / "Send" / "Convert" (contorno).
- Cards de moeda com **textura granulada** sutil (ETH 78,351 +17%, EURO −18%, YEN) e **card tracejado "+ Add another
  currency"** como estado vazio que convida à ação.
- "Balance Spendings": 2 linhas (branca e vermelha) sobre grade escura, tooltip com ponto laranja, **seletor de dias
  em pílulas numeradas**; barras semanais cinza com **só "Wed" em vermelho com gradiente**.
- **Sankey de conversão de moedas** e **"Net Cashflow −$3564" em heatmap de quadradinhos** cinza/branco.
- Barra "Search or type command" com atalho **⌘ Space** (produto de poder).
**Divergência entre rodadas:** a rodada 7 leu "Apps/Reports", "+11%", "Dribix Studio −2300" e tooltip "Debt"; o print
confirma a rodada 2 (TOOLS/INSIGHTS, +17%, Orbix Studio −2309, "Cash").

### 22b. Zentra (cripto) — `Dfr6X8qFPwC` (rodada 5, sem print)
Fundo `~#0E0E10`, cards `#17171A`; **roxo `#6D4AFF` só em item ativo e CTA**; linhas de gráfico laranja `#F7931A` (BTC)
e azul `#4C8DF6` (market cap) + 1 neutra sobre barras de volume cinza; verde `#2ECC71` / vermelho `#FF4D4F` só em variação.
- Sidebar MAIN MENU / FINANCE OPS, botão "Ask AI ⌘D", **card de onboarding "Finish Setup · 2 of 4 · Skip · Next"** com
  ilustração 3D (progresso de configuração dentro da sidebar), toggle Dark Mode no rodapé.
- Ordem: **faixa de 5 KPIs → "Market Trends" grande com tooltip multi-série → tabela de transações → coluna lateral com
  ação (Convert, borda em gradiente laranja→azul, abas Buy/Sell/Swap/Convert) e monitoramento (Watchlist)**.
- "Transaction Status" com **barra de progresso por estado** (Pending 80%, Completed 100%, On Hold 30%…).
- Card "Registration" com QR e **mensagem de erro já escrita** ("If an error occurs scanning…").
- Dados com números "didáticos" (π, e, √2, φ) como placeholder; KPIs de marketing (Traffic, CTR, CPA) num dashboard
  cripto: não faz sentido, não copie.

### 22c. CareNest (saúde) — `DfUvP_ulPC6` (print `DfUvP_ulPC6_2.jpg`)
Mesmo sistema do Vaulto em outro setor: gradiente petróleo `~#0E1A1C → #12262A`, **acento teal `~#3FB8A8`** (aba ativa,
filtro "Weekly", dia ativo) e **bege `~#D9A066` como 2ª cor só nos gráficos**.
- "Welcome back, Cecillia!"; seletor de dias horizontal (dia ativo em pílula teal); cards de médico com foto, especialidade
  e chip "Available".
- Cada KPI com subtotal de contexto ("Total Patients 86 Today · Old Patients: 12"; "Total Rooms 124 · General Rooms: 36")
  e mini-visual próprio (gauge semicircular, barras bicolores).
- Histograma de barras finas com marcos rotulados; **risco em 3 faixas com contagem (12 alto / 24 moderado / 72 baixo)**
  sobre arco radial de traços com "Ai Insight Today". Chips "Upcoming" azul / "Urgent" vermelho.

## 23. Score de crédito "CreditPros" — `DfaQe-CiBfJ` (@uiuxcenter; design Jack R. / @rondesignlab; prints `DfaQe-CiBfJ_1.jpg`, `_2`)
Claro com gradiente pastel (branco → pêssego `~#F3E3DA` → verde-claro), nav em pílulas (ativa preta), **ativo/✓ em
verde-limão `~#D4F53C`**, cards de crédito em gradiente oliva `~#8A9A3A` e rosa-terroso `~#B5796A`, alerta laranja `~#FF5A1F`.
- **Pacote mínimo de confiança do score:** número grande **730** + delta "+6 pts" + rótulo "Excellent" + "Updated 5 Days Ago".
- Score **dentro de faixas coloridas (300 / 630 / 690 / 730) com marcador triangular** na posição atual.
- Abas com contagem em badge ("Your Credits 12", "Inquiries 24", "Public Records 12").
- **Histórico de pagamentos em grade mensal ✓/✕** (✓ em círculo limão, mês perdido em ✕ cinza) + "Make a Payment".
- Painel de vidro em gradiente terroso como drawer de detalhe ("On time 63%" em anel, "$2,663 Left To Pay").
**Problemas:** "24/38 Payments on Time" = 63% em dia, mostrado sem alerta; "12,340" e "$12.340" no mesmo produto.

## 24. Perfil de atleta "Deuce" — `Dfus5sWFAov` (@orbixdashboard; print `Dfus5sWFAov_1.jpg`)
Claro cinza `~#E6E6E6`, cards brancos em 3 colunas; **um verde-oliva `~#7A9A3A` amarra navegação, seleção, gráficos e o
botão "Compare"** (a própria legenda diz isso). Perfil (foto, país, idade, mão, especialidade) ao lado dos números.
- **Forma do gráfico pela pergunta:** área (win rate no tempo), donut (participação por piso), barras horizontais
  (comparação), radar (atributos), mapa de quadra (espaço/tática).
- **Linha tracejada depois do "hoje"** separa projeção de dado real. Resultados recentes com selo W (verde) / L (vermelho).
- KPIs de temporada com delta "vs last season".
**Dados quebrados:** "Age 5"; "Win Rate 543"; Grass 56% (8W/2L) no donut vs 80% nas barras. Usa atletas reais com
estatística inventada.

## 25. Logística "Alpha." — `DftsSH-jnfs` (@webdesignssphere; print `DftsSH-jnfs_1.jpg`)
**A melhor justificativa de UX da leva** (legenda resumida):
- dark + **um laranja** para alertas, botões e pontos de status, porque é **tela de sala de controle aberta por horas**;
- **4 KPIs com variação vs mês anterior** respondem "como estamos?" antes de abrir relatório;
- **card de rastreio com timeline + courier + botões ligar/mensagem** transforma status em algo que o despachante pode agir;
- **heatmap** mostra pico e vale de uma vez, mais fácil que tabela;
- "Visits by country" com filtro de região; tabela de atividades com ID, categoria, horário e status colorido;
- **"+ Create New Request" fixo no topo** (ação mais comum ao alcance).
Visual: "Hi Jelle, Good Evening!" (segunda parte em cinza), nav em pílulas, Income Tracker com **barras hachuradas e
uma barra cheia teal-acinzentada `~#7FB5B5` com tooltip "$329"**, heatmap em tons de teal com legenda por faixa,
banner promocional com foto de contêiner.
**Falhas:** Delivered 3047 > Shipments 1200 sem período; Order ID repetido; "−45%" de distância sem dizer se é bom;
rastreio em "London, UK" num conceito para Dubai.

## 26. Saúde "MediCore" — `DfUWa0jAed7` (@uiuxsharon; print `DfUWa0jAed7_1.jpg`)
Claro `~#F4F5F7` + **azul `~#3B82F6`** (aba ativa). Hero com saudação + **resumo do dia** ("You have 8 appointments today
and 3 new patient reports"), 2 botões (preto + contorno) e ilustração 3D de corpo translúcido com tags de sinais vitais.
KPI padrão: rótulo, número grande, delta verde, mini-barras. Donut com total no centro; tabela com chips de estado
(Stable verde / Monitoring azul / Improving laranja); progresso de tratamento em barras horizontais por programa.
**Problemas:** "Critical Alerts 9 (+6%)" **em verde** (alerta subindo não é bom: a cor do delta precisa seguir o
sentido "bom/ruim", não o sinal); Adrian × Andrian; hashtags de futebol; slide final imita o sorriso da Amazon.

## 27. Code & Chill no Facebook (rodada 6, sem print) — mesmos reels já indexados
Os dois reels são cross-posts de reels do Instagram já descritos:
- **"SaaS revenue analytics dashboard"** (`facebook.com/reel/1555972142999537`) = **`DffBnb2vlUn`** (§4): Funnels em 5
  colunas (1ª azul `#2F6BFF` cheia), Campaigns em kanban Draft / Scheduled / Live / Done, barras `#2FD6A5`, Cohorts com
  heatmap triangular `#1D3FA8 → #5B8CFF` (claro = maior retenção). Fundo `#0B1428`, cards `#101C36`. Snippet `slidePill`
  com `ease: 'power3.out'` (leitura aproximada).
- **"Private credit loan management dashboard"** (`facebook.com/share/r/1A3pMvMBW2/`) = **`Dfo0F0Pvo4Y`** (§16): Casa Duna →
  Portfolio ("Total outstanding $14.18m" → "$14.97m") → Risk (grade terracota `#8A5A48`/`#A86B52`, célula com contorno
  limão `#B8F03C`, lista de imóveis com miniatura). Ordem **ativo → portfólio → risco** (micro ao macro); números
  oscilam entre frames (contagem viva).
**Divergências com §16:** aqui o gauge do imóvel é **amarelo `#E8C547` "63,4%"** (lá: limão "63,8%"); a rodada 6 leu
`power3.out`, a 3 leu `power3.inOut`. Fundo lido como marrom-oliva `#17140F` com vidro sobre foto (lá: terracota + sidebar
clara). Ambos são leituras de frame: na dúvida, prefira §16.
O link `1AE3r4BKt6` abre a página (20K seguidores), não um vídeo; o post mais recente era "Music listening app
dashboard" e não foi analisado.

## 28. Série "OS" da @felvrabr em carrossel (rodada 7, sem print) — complementa §9
Os carrosséis mostram **um componente por slide** com título e uma frase no canto ("Every number at a glance", "Data
that reads like a story", "Micro-interactions that feel native"). Úteis para estudar cada peça isolada.

### 28a. Caféra Coffee Farm OS — `Df4Shdgmafx` (novo domínio: café)
Foto aérea de cafezal verde-escuro `~#12301A`, **acento laranja `~#E8955A`** (verde + laranja, em vez de oliva + lima).
- **Ripeness map:** talhão laranja com pino "Plot 03 · Ready" e cartão com foto das cerejas ("82% ripe · Brix 21.4 ·
  Moisture 92%") + **CTA único "Start harvest"**: "One scan finds the ripe plot, one tap sends the crew".
- **Harvest overview** (2x2): Ripe cherries 71% "On target" (área); Crews in field 3 "+1 sent" (pirulitos "Max 4");
  Picked today 260 bags "Rising" (linha pontilhada); **Season progress 68% TODAY** (gauge).
- Variety Mix em anéis (Catuaí 48 / Bourbon 32 / Mundo Novo 20, centro "412 HECTARES"); Harvest Forecast com junho no acento.
- Sidebar de vidro com ponto laranja de notificação em "Ripeness"; "Harvest picker HV-0307 · Rows picked 3/4 75%".

### 28b. Verdan (carrossel `DfuhN08lTWN`) e Maren (carrossel `Dfr4RMBlaPH`)
Mesmos produtos dos reels `Dfui4V5BMbz` e `Dfr9S5yhlvX`. **Diferenças de número entre reel e carrossel** (o mockup muda
entre versões): Verdan NDVI 0.78 (reel 0.77), "Pivots running 3 · +1 started" (reel 2); Maren ocupação "94% ▲ 6 pts" com
**receita 2026 (teal) vs 2025 (cinza) na mesma curva** e linha pontilhada em 31 Dec, barras Booked terracota `~#C8664F` /
New teal `~#4FD8C0` (§9c chama de coral/menta), tooltip de arraste "Drag to extend · 4 nights · $4,280".
Também listados e **não lidos**: Vinora "Vineyard OS" (`Df11OjZFT5G`), Helion carrossel (`Dfo-Jx3FZ0L`) e landing pages
de comida (Sem Frescura, Brutto) — estas são de `design-direction`.

## 29. Apps mobile do Orbix Studio (@shohan.designs, rodada 7, sem print)

### 29a. Fitness "Workout Readiness" — `DffCenmFASU`
Preto + **teal único**, foto do corredor desfocada em teal. Home abre com **"Today's Health Score" + título "Your Body
Is Ready" + botão único "Start Workout"**; **"93%" e "89%" em fonte de matriz de pontos** dentro de arco fino (score com
identidade sem ilustração); "My Progress · Of the weekly plan completed". Treino: "Workout Progress 68%" em **barra
segmentada com marcador + "Exercises 8/12" + "Workout Time 28:42"**. Nutrição: "Nutrition Score 88 · Excellent" em arco
de pontos e **"Nutrition Achievements" em mini-anéis** (hidratação, fibra, vitaminas 9/12). Título grande bold + rótulos
pequenos cinza.

### 29b. Finanças pessoais — `DfmwyDclA0Q`
"Good morning, Itachi"; "My Balance $50,764.00" + chip verde; **duas cores de acento com papéis fixos: azul `~#1E9BFF` =
dinheiro/ação ("+ Add Money"), lima `~#C8F32B` = resultado/score** (anel "74% Excellent!"). Cashflow Daily/Weekly/Monthly
com "This week / Last week / Change +$1,650"; Income/Outcome com delta. Copiloto "Lumen AI": frase com número ("12% lower
than May"), cartão "Entertainment $1,300 · +18% over budget" e **atalhos prontos** ("Set a budget", "Save $500",
"Find subscriptions").

**Copiar (22–29):** um acento só para ação/estado (ou dois com papéis fixos e documentados); composição do total logo
abaixo do número; KPI com subtotal de contexto; delta colorido pelo sentido bom/ruim; card tracejado de "adicionar";
status → ação (rastreio com ligar/mensagem; "Start harvest"); score = número + delta + palavra + data; forma do gráfico
pela pergunta; projeção tracejada depois do "hoje".
