# Padrões de tela de app mobile

Cada padrão: regras curtas, números das fontes (com ID do reel/post) e **ponteiro** para o texto completo na skill
de tema. "(complemento)" = Apple HIG, Material 3, WCAG ou inferência nossa; não vem das fontes.
Imagens: escolha em `visual-index.md` antes de abrir qualquer uma.

---

## 1. Onboarding
- **Título primeiro**: nada de tela em branco; "2 s em branco parecem uma hora" (`Dfy7ig_B-FL`). Splash com loader de
  marca (shape morph, "Preparing your space", `DfvAY82DSvD`) só enquanto carrega de verdade.
- **Progresso nunca começa do zero** (Goal gradient 19% → 34%, `Dd4UtBDBsIS`). Passos visíveis: "Finish Setup · 2 of 4 ·
  Skip · Next" (Zentra `Dfr6X8qFPwC`); perfil "90% Complete" em anel (Qwash `DX_bA4rCWf0`).
- **Pouco por passo** (Hick, Choice overload 3% → 30%); peça só o necessário e preencha o resto (Tesler 31 → 16 teclas).
- Pedido de permissão (notificação, localização) **no momento em que faz sentido**, com tela explicando o ganho antes
  do diálogo do sistema; "Agora não" respeitado (complemento; nagging em `dark-patterns.md` §A).
- Carrossel de boas-vindas: próximo slide espiando, paginação com dots elásticos (borda da frente sai 130ms antes, `DfWjKQPhUbn`); "Pular" sempre visível (complemento).
- Ponteiros: `ux-patterns/references/ux-laws.md` Partes 2 e 4; `ui-motion/references/micro-interactions.md` §4;
  `design-direction/references/claude-design-course.md` "Mobile App Prototype" (onboarding com connect bank, 3 perguntas, notificação).

## 2. Login e cadastro
- Social login (Apple, Google…) + e-mail; "Forgot password" perto do campo; "Not a member? Create an account" no fim
  (WayLoo `DVv7OOECewR`). No iOS, oferecer Sign in with Apple quando há outros sociais (complemento, App Store).
- Campos: label a **8px** do campo e **24px** do próximo (Proximity 1:3); label flutuante **20 → 14px**; teclado
  `email`, `autocomplete="username"/"current-password"`, `one-time-code` para OTP (complemento).
- OTP: dígitos caem **70ms** separados e as caixas acendem em onda; senha com medidor de **4 segmentos** vermelho → azul
  (`DfZkZZ4hkuV`). Erro com shake curto + texto, não só cor (complemento; `ext-transitions-dev` "error state shake").
- Botão "Sign in" ≥ 48px, loading **mantém a largura** e ignora o 2º toque (`DfemaTCBncA`).
- Login de vidro e transição login ↔ cadastro: `dashboard-ui/references/glassmorphism.md` (`DeoGCPlzKOs`; é web, adapte).
- Ponteiros: `ux-patterns/references/components-checklists.md` §2; `ui-motion/references/micro-interactions.md` §5–6.

## 3. Home e feed
- **Saudação em duas camadas**: nome em branco/preto + pergunta ou resumo em cinza ("Hello, Denis! *You want to book
  something?*"; "Good morning, Itachi") — `DVv7OOECewR`, `DfmwyDclA0Q`.
- **Uma ação clara** no topo da home: score do dia + "Start Workout" (`DffCenmFASU`); "+ Add Money" (`DfmwyDclA0Q`);
  "Start a new trip" (`DVv7OOECewR`).
- **Não abra com estado vazio**; mostre conteúdo útil (cartões com foto grande, preço, selo, nota), filtros em pílula
  com **um ativo cheio**, banner com **um CTA** — antes/depois imobiliário `DfzgxEKlx8z`.
- **Um accent** só para ativo/CTA/selo; resto neutro (Von Restorff). Layout seguro: margens generosas, uma borda
  esquerda, 1 CTA (`DfyFShTounu`).
- Feed: skeleton sem layout shift; "new posts pill" para não perder o lugar; live insert para tempo real; pull-to-refresh
  com resistência **35%** (`DfwavjimeIa`, `DfP6EoLBtgg`). Carrossel horizontal com **32%** do próximo card visível (`Del7XTgsuwI`).
- Ponteiros: `ux-patterns/references/components-checklists.md` §11; `ui-motion/references/loaders-and-refresh.md`;
  `design-direction/references/layers-and-trust-layout.md` §2; `dashboard-ui/references/layout-patterns.md` §9.

## 4. Tab bar
- **3–5 destinos** (seções, não ações — complemento HIG/Material); ícone + **rótulo** ("glance, don't guess", `DfreUkyBNQg`).
- Aba ativa com **um accent**: pílula flutuante (WayLoo `DVv7OOECewR`, Markets `DXeeUP7FKGs_1`), gota líquida "Meniscus"
  com cor por aba (`DbfG6fuPE9y`). Indicador viaja (`power3.out`, 250–350ms — complemento) e nunca pisca.
- **Vidro fosco**: 30px de blur atrás da tab bar (`Dflzxq5Bqfj`); só sobre conteúdo que rola.
- **Botão central circular** para a ação principal (Qwash `DX_bA4rCWf0`) contradiz Serial position (`Dd4UtBDBsIS`: ação-chave
  no início ou no fim); funciona por ser distinto (Von Restorff). Se a ação é uma tarefa, prefira FAB (Android) ou
  botão no conteúdo (complemento).
- Esconder ao rolar para baixo e mostrar ao subir só em leitura longa (complemento, `scroll-and-screen-transitions.md` §1).
- Altura + `safe-area-inset-bottom`; alvos ≥ 44pt/48dp (complemento: iOS ~49pt + inset, Material navigation bar 80dp).
- Ponteiros: `ux-patterns/references/components-checklists.md` §10; `ui-motion/references/micro-interactions.md` §8, §11, §13.

## 5. Detalhe (produto, ativo, pedido)
- **Card → página**: a imagem do card cresce até o hero e o back volta à posição de origem ("Don't cut. Carry.",
  `DfwhC1riuuO`); reveal ~350–700ms; View Transitions/FLIP na web, shared element nativo (complemento).
- Large title **34 → 18px ligado ao scroll** em telas de topo; detalhe profundo com título inline (complemento HIG).
- CTA fixo no rodapé acima da safe area ("Add to bag", "Book"); Add to cart voa em **arco 500ms** e o badge faz +1 (`DfTr-mwhZT3`).
- Photo viewer: segue o dedo **1:1** e encolhe; ao soltar volta com spring para a thumbnail (`DfcwOHLh76I`).
- Cards de spec em vidro escuro com borda fina (consumo, aceleração), botão 360° (WayLoo `DVv7OOECewR`).
- Ponteiros: `ui-motion/references/page-transitions-and-timing.md`; `ui-motion/references/css-recipes.md` §6.

## 6. Bottom sheet e modais
- Sheet **segue o dedo e faz snap em 146px com overshoot de 7px**; a página escurece (`DfgcqeMBPCU`, "Choose a ride").
- Backdrop baixa o contraste do fundo **17,4:1 → 2,5:1** (Figure-ground, `Del7XTgsuwI`).
- "More" em sheet agrupada por tarefa (Edit / Adjust) para tools raros (`DfreUkyBNQg`, Hick 12 → 4 + More).
- Detents (médio/grande), handle visível, fecha por swipe para baixo, tap no backdrop e botão; conteúdo rolável dentro
  sem brigar com o gesto de fechar (complemento HIG/Material).
- Modal só para tarefa autocontida ou confirmação destrutiva; menu/popover **nasce do botão** que o abriu (`DfwhC1riuuO`).
- Tooltip cresce **50% → 100% a partir da seta** (`DfgcqeMBPCU`). Dynamic Island/alertas: morph da pílula, não pop (`Dflzxq5Bqfj`).
- Ponteiros: `ux-patterns/references/components-checklists.md` §8; `ui-motion/references/micro-interactions.md` §8.

## 7. Formulário e teclado
- Teclado certo por campo (`inputmode`/`keyboardType`), `autocomplete`/`textContentType`, `enterkeyhint="next"` e
  "Next" avançando o foco (complemento).
- **Campo focado e CTA acima do teclado**: `KeyboardAvoidingView`/`adjustResize`/`visualViewport`; CTA de rodapé
  sobe junto com o teclado (complemento).
- Postel: aceite qualquer formato e normalize (telefone **1/4 → 4/4**); Chunking: `415 555 0123`; Tesler/Parkinson:
  CEP/postcode primeiro (**31 → 16**, **30 → 7 teclas**) — `Dd25eCoBJGr`, `Dd4UtBDBsIS`, `Del7XTgsuwI`.
- Validação inline depois de sair do campo, erro com texto + ícone (complemento); disabled diz o porquê
  ("Name your workspace first", `DfemaTCBncA`).
- Slider: thumb cresce **140%** ao agarrar, bolha de valor segue (`DfWjKQPhUbn`); arraste que muda valor mostra o
  resultado antes de soltar ("Drag to extend · 4 nights", `Dfr4RMBlaPH`).
- Ponteiros: `ux-patterns/references/ux-laws.md`; `components-checklists.md` §2, §8; `ui-motion/references/micro-interactions.md` §4–6.

## 8. Checkout e fluxo em etapas com rodapé fixo
- **Progresso em 4 etapas nomeadas** (Picked → Washing → Out for delivery → Delivered), **a mesma barra na home e no
  detalhe**, com chip de estado ("On Process") e mapa de rota (Qwash `DX_bA4rCWf0`; Uniform connectedness 4 grupos → 1, `Del7XTgsuwI`).
- **Rodapé fixo com total + 1 primário**: "Delivery Fee $5 / Estimated Total $21" + "Schedule A Collection"; stepper
  − 0 + na lista de preços.
- **Revisão antes de pagar** (itens, horários, endereço, subtotal) e o botão diz o valor — **confira que bate com o
  total** (o exemplo mostra $43 vs $26: não copie).
- Checkout steps: check desenha, linha enche em **400ms**, próximo dot pulsa (`DfcwOHLh76I`).
- Pagamento: "Pay" vira "Paid" com confetti de **18 peças, pico em 460ms** (`DfgcqeMBPCU`); final caloroso
  ("You're all set!", Peak-end 4,5 → 8/10). Apple Pay / Google Pay como primário quando disponível (complemento).
- Pedido ativo: cancelar visível; suporte por chat no detalhe.
- Ponteiros: `ux-patterns/references/components-checklists.md` §10; `dashboard-ui/references/layout-patterns.md` §9;
  `dashboard-ui/references/domain-examples.md` §21a.

## 9. Tela de decisão (Buy/Sell, aceitar/recusar)
- Desenhe para o instante da decisão: responda **o que se mexe, o preço e para onde olhar** ("Today's Movers"); só
  sinais imediatos + contexto mínimo (Hick) — Markets `DXeeUP7FKGs_1`.
- Linha de ticker: logo 32–40px · ticker bold + nome cinza · preço (tabular) + **variação com sinal e cor em pílula**.
- Detalhe: preço grande + variação → gráfico → seletor **1D · 1W · 1M · 3M · 1Y · ALL** → card de IA com veredito
  (BEARISH) + 2–3 frases → **Sell e Buy do mesmo tamanho, lado a lado, fixos no rodapé** (zona do polegar).
- **Divergência registrada**: "um primário por tela" vs dois primários; vale quando as duas ações são opostas e legítimas.
- Verde/vermelho só para variação de preço; um accent para ativo/CTA positivo.
- Score/resumo mobile em rosca segmentada com número no centro (Borea `DSIMwtvDluO_1`).
- Ponteiros: `ux-patterns/references/components-checklists.md` §9; `dashboard-ui/references/layout-patterns.md` §8;
  `dashboard-ui/references/domain-examples.md` §20.

## 10. Notificações, toasts e badges
- Toast **no topo no mobile**, nunca centralizado; info **4 s**, warning **7 s**, erro até reconhecer; máx. **3** com
  spring **180/20**; dispensável por **swipe**; ícone + **borda esquerda colorida** (6% não distinguem só pela cor) — `DXRpZTTMr9a`.
- Toast novo sobe **64px** e o anterior recua para **92%** (`DfgcqeMBPCU`).
- Sino balança **±24°** e assenta em **760ms**, badge entra com pop (`DfTr-mwhZT3`); use só para algo novo de verdade.
- Ilha de estado para modo ativo (foco, gravação, sync): pílula que expande + toast "notifications are held"
  (`Deoi1WhP83h`, web; no iOS = Live Activity/Dynamic Island — complemento).
- Push (complemento): pedir opt-in depois de o usuário ver valor; categorias controláveis nas settings; deep link para
  a tela certa; nada de push como nagging.
- Ponteiros: `ui-motion/references/micro-interactions.md` §3, §9; `ux-patterns/references/dark-patterns.md` §A.

## 11. Estados (carregando, vazio, erro, offline, sucesso)
- Escolha o loader pelo que se sabe: spinner **< 3 s**; barra/anel com **%** (21 → 100%); skeleton para feed; typing
  dots/AI shimmer para chat e IA; loader no botão para ação do usuário (`DfvAY82DSvD`, `Dfw7678GcQ2`).
- Optimistic UI (like **142 → 143**) e progresso psicológico (Linear 16% vs 31% no mesmo instante) — `DUEjWRukT_2`.
- Vazio que convida: card tracejado "adicionar" (Vaulto `DfcdrhgFFMR_2`), nunca "No properties found" na primeira dobra.
- Erro com retry inline que **retoma** (upload "Resuming from 90%", `DZ2Dp5wt0pJ`); timeout em APIs externas (item 12).
- Offline (complemento): banner persistente e discreto, dados em cache com "atualizado há X", ações na fila com selo
  "pendente", sincroniza sozinho ao voltar e avisa conflito.
- Sucesso: círculo e depois tick **470ms**; download seta → anel → tick **1,2 s**.
- Ponteiros: `ui-motion/references/loaders-and-refresh.md`; `ux-patterns/references/perceived-performance.md`;
  `design-direction/references/claude-web-design-workflow.md` (teste dos 4 estados).

## 12. Settings
- Confirmar o save na linha ("Saved") · **escopo em cada linha** (pessoal / workspace / todos) · busca e seções ·
  1 linha de consequência · marcar o que não é default + reset · dizer quando vale (agora, próximo login, restart) — `DdRneVWhBSY` (painéis não mobile).
- **Chevron** nas linhas que abrem algo (Similarity: 3 escondidas → 0, `Dd4UtBDBsIS`).
- Aparência: tema Light/Dark/Auto, accent, **Reduce transparency** (`Deoi1WhP83h`, §2 de domain-examples). Ação
  destrutiva em vermelho e no fim.
- Mobile (complemento): grupos em lista inset (iOS) ou lista com subtítulos (Material); toggle aplica na hora; links para
  as permissões do sistema (notificação, localização) quando negadas.
- Ponteiros: `ux-patterns/references/components-checklists.md` §3; `dashboard-ui/references/domain-examples.md` §2.

## 13. Apps de score (fitness, finanças pessoais, crédito)
- **Score = número + delta + palavra + data**, dentro de faixas/arco, + **1 botão de próximo passo**:
  "93% · Your Body Is Ready · Start Workout" (`DffCenmFASU`); "74% Excellent!" (`DfmwyDclA0Q`); "730 +6 pts Excellent ·
  Updated 5 days ago" (`DfaQe-CiBfJ`, web).
- Número-herói em **fonte de matriz de pontos** dentro de arco fino, 1 por tela, dígitos de largura fixa
  (`typography-and-touch.md` §7).
- Meta curta e concreta: barra segmentada com marcador + "Exercises 8/12" + "Workout Time 28:42".
- Cor do delta pelo sentido **bom/ruim**, não pelo sinal; faixas com rótulo de texto (daltonismo, complemento).
- Finanças: saldo + chip de variação → "+ Add Money" (accent) e "Send Money" → score → gastos; copiloto de IA com
  **atalhos prontos** ("Set a budget", "Save $500"). **Dois accents** só com papéis fixos (azul = ação, lima = score).
- Um accent sobre preto (teal no fitness); título bold grande + rótulos pequenos cinza.
- Ponteiros: `dashboard-ui/references/layout-patterns.md` §10; `dashboard-ui/references/domain-examples.md` §23, §29;
  `ux-patterns/references/typography-and-touch.md` §5 (app de clima: número 20 → 76px).

## 14. Gamificação mobile
- O que as fontes mostram é **progresso e meta**, não pontos/badges: gauge que enche, anel **N/M** (Tasks 3/8),
  checklist segmentado **3/4**, mini-anéis de conquista ("Vitamins 9/12"), grade ✓/✕ de meses (base de streak).
- Goal gradient: comece com progresso dado (cartão 8 vazios → 10 com 2 dados: **19% → 34%**).
- Streak (complemento): 7 pontos (dias) no topo da home, preenchidos no accent; nunca "quebra" para pressionar compra.
- Celebração = 1 animação curta, uma vez (estrelas **100ms** separadas com pop; confetti 18 peças), reduced motion
  respeitado; nunca bloqueia a tela. No cliente, sem ranking contra outros; no máximo "você vs sua média".
- Gamifique o que o usuário controla (concluir treino, pagar em dia), não o que ele não move.
- Ponteiros: `dashboard-ui/references/layout-patterns.md` §7 (7.1–7.4, gestor vs cliente); `ux-patterns/references/ux-laws.md` Parte 2;
  `ui-motion/references/micro-interactions.md` §5.

## 15. Chat e assistente de IA
- Suas mensagens à direita com accent (texto **8,3:1**); **4px** dentro da sequência e **18px** entre pessoas (num
  sistema de 8, 16–24px); 1 timestamp no intervalo; "Read" só na última; nova mensagem desliza **240ms** (`DerGbJAhUTm`).
- Campo de texto fixo acima do teclado e da safe area; sugestões em chips acima do campo (complemento; atalhos do Lumen AI `DfmwyDclA0Q`).
- IA: typing dots / AI shimmer "Thinking…", streaming token a token (`perceived-performance.md` item 13).
- Ponteiros: `ux-patterns/references/components-checklists.md` §5; `ui-motion/references/loaders-and-refresh.md`.

## 16. Listas com ações (swipe, long press, reorder)
- Swipe para ação: segue o dedo, inclina **12°**, sai com velocidade; delete voa para a lixeira em **400ms** e a lista
  fecha o vão (`DfTr-mwhZT3`, `DfcwOHLh76I`). Sempre com undo (toast) e alternativa visível (menu) (complemento).
- Long press: **400ms** de hold, linha sobe **5%**, resto escurece (`DfWjKQPhUbn`); reorder sobe **105%**, outros
  deslizam **200ms** (`DfP6EoLBtgg`). To-do: check + risco + afunda para o fim em **470ms** (`DfZkZZ4hkuV`).
- Linhas de lista grandes podem encostar; ícones pequenos vizinhos precisam de **8px** (`typography-and-touch.md` §1).
- Ponteiros: `ui-motion/references/micro-interactions.md` §2–6; `ui-motion/references/css-recipes.md` §10.
