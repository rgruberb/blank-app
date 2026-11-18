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

### 9a. Verdan Farm OS — `Dfui4V5BMbz` (agro; referência pedida para o protótipo gamificado)
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
