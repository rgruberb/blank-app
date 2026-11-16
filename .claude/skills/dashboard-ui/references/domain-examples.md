# Exemplos por domínio — o que cada referência faz e o que copiar

Descrições feitas a partir das folhas de contato (resolução baixa; textos pequenos muitas vezes ilegíveis —
quando um rótulo não pôde ser lido, isso está dito). Hex aproximados. Itens marcados "(complemento)" não
aparecem na referência; são sugestões para completar o padrão.

---

## 1. Vendas de varejo — `De12lc1vUmr` (@_code_and_chill_)
**Tema:** claro monocromático. Fundo `~#eceeed`, cards `~#f7f8f7`/branco, texto quase preto `~#111`,
KPI destacado e rail em `~#0f1110`.

**Layout**
- Header de app: logo quadrado preto + nome da loja à esquerda; **top nav em pílulas** centralizada (6–8 itens,
  alguns com contador; o ativo é pílula preta com texto branco); ícones à direita.
- **Rail de ícones vertical flutuante** à esquerda: pílula preta alongada, ~7 ícones brancos, separada da borda.
- Título "Analytics" grande; abaixo, segmented controls de período (pílulas pequenas, ativa branca) e, à direita,
  um toggle (provavelmente comparação) + botão "Export".
- Linha de **5 KPI cards** iguais em largura: rótulo pequeno, valor grande (`$37,163`, `532`, `$69.87`, `4.53%`,
  `38.7%`), delta verde, sparkline fina embaixo. **O primeiro é invertido (preto)** — é o KPI-mestre.
- Abaixo: gráfico de área/linha largo (~2/3) com o valor-mestre repetido em destaque, duas séries
  (linha escura + área cinza clara, curvas suaves), legenda no canto superior direito.
- Coluna direita (~1/3): breakdown com dois percentuais, **barra empilhada horizontal** preta/cinza e lista de
  dois itens (bullet, nome, valor à direita, delta verde).

**Animação:** troca de tema com `document.startViewTransition` + `clipPath: circle()` expandindo a partir do
botão de tema, `duration: 620` (leitura aproximada), `pseudoElement: '::view-transition-new(root)'`.

**Copiar:** KPI-mestre invertido; sparkline em todo KPI; disciplina de cor (só o verde dos deltas tem cor);
rail flutuante + top nav em pílulas.

---

## 2. Gestão de projetos em equipe — `Deoi1WhP83h` (@_code_and_chill_)
**Tema:** escuro neutro. Fundo `~#141517`, superfícies `~#1b1c1e`–`#25262b`, bordas sutis, cantos ~16–20px;
cards parecem levemente translúcidos (o próprio app oferece Glass "Clear/Tinted").

**Telas vistas**
- **Tasks:** rail de ícones com logo azul no topo e avatar no rodapé; ilha superior central "Focus 24:56" (timer em pílula
  preta, estilo dynamic island); toolbar de ícones à direita. Título "Tasks" + subtítulo "31 open across 5 projects"
  (leitura aproximada). **Faixa de stats sem cards**: Open 31 · Due this week 11 · Overdue 0 · Done this week 26.
  Filtros em pílulas (All projects, Mine only, Any priority) + campo de busca. Botões "Board"/"List" e CTA azul "New task".
- **Kanban** In progress / In review / Done: cabeçalho com ponto colorido + contagem; cards com **tag de projeto**
  (pílula com ponto: verde, azul, roxo, rosa) + tag de prioridade (laranja "High", vermelho "Urgent"), título,
  **barra de progresso fina** na cor do projeto, data, comentários, avatar. Em "Done" aparece check azul.
- **By project:** donut em segmentos separados (roxo, azul, verde, rosa, teal) com total central "333 finished";
  legenda em lista: bullet, nome do projeto, contagem, percentual alinhado à direita.
- **Focus:** "807 hours — about 63h a week" (número grande + unidade pequena).
- **Settings:** sub-navegação em lista com ícones coloridos quadrados (Profile, Notifications, Appearance, Focus, Data);
  seções em cards: Theme (Light/Dark/Auto segmented), Wallpaper (grade de miniaturas coloridas), Accent (6 swatches:
  azul, roxo, magenta `~#d12777`, laranja, verde, cinza), Glass Clear/Tinted, **Reduce transparency** (toggle),
  Focus (steppers 25 min / 5 min), Data (Export tasks as CSV, ação destrutiva em vermelho).

**Animação:** primeiro quadro mostra transição com forte motion blur entre listas.

**Copiar:** faixa de stats compacta sem caixa; anatomia do card de kanban; tela de Appearance com
"Reduce transparency" (acessibilidade para glass); donut com legenda tabular.

---

## 3. Portal de corretora de seguros marítimos — `DfCWtPgPcfP` (@_code_and_chill_)
**Tema:** par dark/light do mesmo produto ("Moorly"). Destaque teal `~#4fb1a2`.
- Dark: fundo `~#04121a` com **ondas teal escuras** no terço inferior (ilustração de mar), colunas `~#062a2a`.
- Light: fundo branco com **névoa teal/pêssego** (`~#e6f7f8`, toque quente no canto superior direito), cards `~#d8f3f6`.

**Layout**
- Top nav em pílulas com ativo teal preenchido + badges numéricos; segunda linha de abas/breadcrumbs.
- **Pipeline (dark):** kanban de ~6 colunas de estágio; cards com tipo de seguro, nome da empresa, valor (`$85,750`…),
  avatar e ações. CTA teal "New submission" (aparente) no canto superior direito.
- **Detalhe da conta (light):** título "Pell Harbor Ferry Co." + metadados; **stepper horizontal em forma de rota**
  (nós circulares teal ligados por linha curva; etapa atual com marcador escuro); grid de campos (rótulo pequeno + valor)
  no card principal; card lateral "Indicated premium $66,500" com lista chave/valor.

**Animação (GSAP):** um barco percorre o path da rota até a próxima estação — `getPointAtLength`, rotação por
`Math.atan2`, `strokeDashoffset` para revelar a linha, `ease: 'power3.inOut'`.

**Copiar:** metáfora do domínio aplicada a um componente funcional (o stepper vira rota marítima), sem poluir o resto;
oferecer os dois temas com a mesma estrutura.

---

## 4. Analytics de receita SaaS — `DffBnb2vlUn` (@_code_and_chill_)
**Tema:** dark azul profundo. Fundo `~#061a2a`→`#0b1640`, **glow radial azul `~#1d3aa8` e teal** atrás das colunas,
colunas/cards `~#122670` translúcidos com borda azul clara sutil, CTA azul `~#4e6ad1`.

**Layout:** rail de ícones à esquerda (ativo em quadrado azul claro), breadcrumbs + busca no topo, título "Campaigns",
um seletor com cursor circular (ação sendo demonstrada), board de 4 colunas; cards com nome da campanha, descrição,
**dois pares rótulo + barra de progresso** (teal e azul) com valor à direita, avatar.

**Animação (GSAP `slidePill`):** a pílula ativa é recortada com `clip-path: inset()`; a borda na direção do movimento
anda primeiro (`ease: 'power3.out'`, ~0.3s) e a traseira alcança depois (`'power3.inOut'`, ~0.5s) — efeito elástico
(durações com leitura incerta).

**Copiar:** luz ambiente atrás do conteúdo em vez de gradiente nos cards; barras de progresso duplas para
"meta vs realizado" (complemento: rotular claramente qual barra é qual).

---

## 5. App de orçamento familiar — `DfkNvnePItL` (@_code_and_chill_)
**Tema:** dark verde musgo (`~#162218` sidebar, conteúdo `~#374534` desfocado), ativo verde-menta `~#8af1b6`.
Só um quadro, em plena transição: a **pílula ativa da sidebar está esticada** cobrindo dois itens (efeito do
`slidePill` vertical) e o conteúdo está borrado. Rodapé da sidebar com bloco de saldo e card do usuário; topo com
busca e botão verde circular.

**Copiar:** a animação de item ativo em navegação vertical. Layout em si não é legível o bastante para copiar.

---

## 6. Smart home — `DfrqAX9v59S` (@_code_and_chill_)
**Tema:** glass/frosted cinza grafite. Painéis `~#555756`, sidebar `~#414342`, item ativo em **pílula branca**
`~#dfe1e0` com texto escuro. Sem cor de destaque — as fotos das câmeras dão a cor.

**Layout:** sidebar larga (logo circular + nome, grupos, ~10 itens, card no rodapé), barra de busca no topo e ícones;
breadcrumb + título "Security" + subtítulo; botão branco em pílula à direita; abas; **grid de câmeras**: 1 grande
(sala) + 2x2 menores (fachadas, interiores), com rótulo sobreposto no canto; abaixo, chips de filtro (ativo branco)
e linha de dispositivos com miniaturas.

**Copiar:** quando o conteúdo é mídia, deixe a UI neutra e acinzentada; grid "1 grande + 4 pequenos".

---

## 7. Plataforma de saúde, prior authorization — `DfV39ohhwAC` (@ui.iliasmiah000)
**Tema:** dark neutro `~#0b0c0e`, cards `~#151618` com borda sutil e cantos ~16px, destaque **mint `~#2fb58f`**,
âmbar para alertas de prazo, chips de status em azul-acinzentado / verde. Glow verde muito leve ao redor da moldura.
Tipografia sans geométrica, números grandes em peso leve/regular.

**Layout (quadro completo no canto inferior direito da folha)**
- Sidebar larga: logo "Veyra Health", card do usuário/organização, navegação (Overview ativo + itens com contadores),
  grupo de filas/payers com pontos coloridos, rodapé com status.
- Topo: busca com atalho, data/hora, ícones (notificação com badge), avatar.
- Header: "Overview" + "Good morning, Dana. 23 cases need attention today." À direita: filtros ("All payers",
  "Last 30 days") e CTA mint "New authorization" (aparente).
- **KPI strip sem cards** (5): Active cases 386 · Pending payer 142 (chip âmbar "overdue") · Approved 1,127 ·
  Denied 96 (chip vermelho) · Median turnaround 3.4 d — rótulo caps minúsculo com ícone, número grande, chip de delta.
- Linha 2: **"Requests vs decisions"** (2/3) — mini-KPIs Submitted 1,318 / Decided 1,223 / Backlog change +95,
  segmented 7D/30D/90D; no quadro 2 são **barras cinza-escuro com só a barra atual em mint**; no quadro 3 vira
  **duas linhas suaves com faixa preenchida entre elas** e tooltip com marcador na coluna destacada.
  **"On time decisions"** (1/3) — **gauge semicircular de ticks** (mint→âmbar no fim) com "92%" central e
  "1,125 of 1,223 within clock"; ao lado, "6 h until the first clock lapses" e "4 cases lapse within 24 h".
- Linha 3: **"Open pipeline"** (barras verticais mint, última em rosa/vermelho); tabela **"Needs attention"** com
  abas (Due today / Overdue), colunas paciente/payer/status/clock, status em chip (Pending payer, Submitted,
  Ready for review), prazo + avatar; **card "Veyra Assistant"**: orbe luminoso, texto "4 Sunvale cases lapse within
  12 hours. Follow up by 2 PM", avatares, barra de progresso âmbar "First clock lapses in", CTA mint "Review 4 cases"
  + "Dismiss".

**Ideia do autor (legenda):** "Sorted by clock, not by date, so the riskiest case is always on top."

**Copiar:** saudação que já diz o que importa; KPIs sem caixa; gráfico com histórico neutro e "agora" destacado;
gauge com contexto textual ao lado; card de IA com **uma recomendação concreta + CTA + dispensar**; ordenar por risco.

---

## 8. Série glassmorphism — @code.xr
Todos com snippet React: `motion.div whileHover={{ y: -5 }} className="glass-card p-6 rounded-2xl"`,
título `text-sm text-white/60`, valor `text-2xl font-bold text-white`, delta `text-emerald-400` com `ArrowUpRight`
(lucide-react). Stack declarada: React, CSS, Framer Motion.

- **Login V3 — `DeoGCPlzKOs`:** fundo preto `~#05060b` com ondas 3D escuras e faixas de luz ciano. Card de vidro escuro
  `~#25313d` translúcido com **cantos chanfrados em ciano** (moldura tipo HUD), título "Create **Account**" com a
  segunda palavra em ciano/azul, campos Full Name / Email / Password + Confirm lado a lado (ícones à esquerda, olho à
  direita), checkbox de termos, botão largo gradiente ciano `~#4cc3f5`→`#2d8bb6` com seta, divisor, Google / Apple,
  link "Sign in".
- **Dashboard V7 + CRM — `DfHrMboTVDZ`:** "Customer Intelligence" sobre foto de sala de estar (móvel de madeira,
  TV, planta). Rail escuro vertical com ícones e tooltip, painéis âmbar/marrom translúcidos `~rgba(165,129,110,.5)`,
  card de perfil com avatar azul `~#94a6fa`, mini gráfico de linha, botões em pílula branca, KPIs pequenos ("630",
  "11.6%"), indicador circular "68%" com ponto verde, pílulas laranja `~#d59353` no topo.
- **Dashboard V8 — `DfKPFDwz2aA`** (no vídeo aparece "V18"): sidebar glass com marca em serifa, "Leads" em serifa,
  4 KPI cards escuros, tabela de leads (avatares coloridos, chips, barras). Coluna direita com 3 cards empilhados:
  **azul sólido-translúcido `~#7488c7` com barras brancas** (3,241), bronze (`$2,450`, botão circular),
  escuro com área (95,215). CTA azul `~#7098ed`.
- **Sidebar V5 — `DfMH6YTTcwx`:** detalhado em `glassmorphism.md`.

**Copiar:** glass só sobre fotografia ou fundo rico; um card de cor sólida para ancorar o olhar; hover com
elevação de 5px; serifa para títulos dá ar "premium" (V8).
