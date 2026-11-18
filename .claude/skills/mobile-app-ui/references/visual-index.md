# Índice visual — imagens de app mobile nas skills de tema

Esta skill **não tem imagens próprias**: aponta para as que já existem nas skills de tema. Caminhos relativos a esta
pasta (`mobile-app-ui/references/`). **Cada imagem custa contexto**: abra no máximo 1–2, só para *ver* layout ou curva;
os números já estão em `../SKILL.md`, `mobile-patterns.md` e nas references das skills de tema.

Formato: "folha 4×3" = 12 frames do reel em ordem (esquerda → direita, cima → baixo); "print" = slide único.
Os reels do @motion_ui_interface mostram **painéis de componente com o gráfico da curva** (não a tela inteira do celular).

## Motion e micro-interações (`ui-motion`)

| Caminho | Autor | O que mostra | Quando abrir |
|---|---|---|---|
| `../../ui-motion/assets/visual-refs/De4B0UxPXIk.jpg` | @motion_ui_interface | 6 detalhes "without vs on iPhone": press 120 vs 0 ms, linear vs spring, momentum 1000px, rubber band 86px, interrupção, cantos contínuos | Justificar por que o app "parece iPhone": springs, momentum, rubber band, squircle |
| `../../ui-motion/assets/visual-refs/DfP6EoLBtgg.jpg` | @motion_ui_interface | Curvas: press 95%, pull 100% → 35%, dígitos 100ms, lift 105% + 200ms, ease-out 350ms, tick 470ms | Ver a forma da curva de press, pull-to-refresh, reorder, expand, sucesso |
| `../../ui-motion/assets/visual-refs/DfTr-mwhZT3.jpg` | @motion_ui_interface | Add to cart em arco 500ms, submit 260 → 64px, lista 70ms, swipe 12°, flip 180°, sino ±24° | Swipe-away, add to cart, submit morph, stagger de lista, badge |
| `../../ui-motion/assets/visual-refs/DfWjKQPhUbn.jpg` | @motion_ui_interface | Speed dial 45°, slider 140%, **large title 34 → 18px**, long press 400ms, page dots, side menu 86% | Large title, long press, FAB, dots de onboarding, side menu |
| `../../ui-motion/assets/visual-refs/DfZkZZ4hkuV.jpg` | @motion_ui_interface | Estrelas 100ms, **OTP 70ms**, accordion, senha em 4 segmentos, to-do 470ms, reações 1,6× | Login/OTP, cadastro com senha, rating, celebração |
| `../../ui-motion/assets/visual-refs/DfcwOHLh76I.jpg` | @motion_ui_interface | Copy button, **label flutuante 20 → 14px**, checkout steps 400ms, map pin, delete 400ms, photo viewer 1:1 | Formulário, stepper de checkout, delete em lista, galeria |
| `../../ui-motion/assets/visual-refs/DfVOGNnzR_D.jpg` | @motion_ui_interface | Ícones que morfam: play/pause 300ms, download 1,2 s, tema 600ms, search → X, send, unlock 34% overshoot | Ícones de tab bar/toolbar que mudam de estado |
| `../../ui-motion/assets/visual-refs/Dflzxq5Bqfj.jpg` | @motion_ui_interface | Polish iPhone: **blur 30px atrás da tab bar**, raio 36 − 12 = 24, centro óptico +11px, tracking −6px, ícone 2,4px, **Dynamic Island** | Acabamento "caro" de tela iOS; alerta que cresce da ilha |
| `../../ui-motion/assets/visual-refs/DXRpZTTMr9a.jpg` | @designmotionhq | Toasts: posição desktop/**mobile (topo)**/centro errado, 4s/7s/até ack, stack 180/20 máx. 3, swipe/close | Toasts e notificações in-app |
| `../../ui-motion/assets/visual-refs/DUEjWRukT_2.jpg` | @designmotionhq | Blank vs skeleton (card de post), like otimista 142 → 143, progresso 16% vs 31% | Estados de carregamento de feed; UI otimista |
| `../../ui-motion/assets/visual-refs/DfvAY82DSvD.jpg` | @ale.uiux | Grade de **mockups de celular**, 1 loader por slide: spinner, typing dots, barra, skeleton, AI shimmer, anel, pull refresh, shape morph | Escolher o loader de cada estado do app |
| `../../ui-motion/assets/visual-refs/DfwavjimeIa.jpg` | @ale.uiux | 8 formas de atualizar: pull down, elastic pull, release cue, new posts pill, live insert, auto-load, load more, refresh button | Feed/lista: refresh e infinite scroll |
| `../../ui-motion/assets/visual-refs/DbfG6fuPE9y.jpg` | @_code_and_chill_ | Tab bar "Meniscus": aba ativa vira gota líquida, cor e glow por aba, gota arrastável | Tab bar com indicador expressivo (o momento lúdico da tela) |
| `../../ui-motion/assets/visual-refs/DfwhC1riuuO.jpg` | @theglidestudio | "Tap. Cut." vs "Don't cut. Carry.": card vira a página, back volta, menu nasce do botão (demo em **site** de loja) | Transição lista → detalhe no app (o princípio vale igual) |

## UX, componentes e leis (`ux-patterns`)

| Caminho | Autor | O que mostra | Quando abrir |
|---|---|---|---|
| `../../ux-patterns/assets/visual-refs/DXeeUP7FKGs_1.jpg` | @rish_designs (collab @ultimateuiux) | Print: app de trading **iOS** "Markets" (lista + detalhe), pílulas +/−, tab bar com pílula limão, **Sell/Buy iguais fixos no rodapé** | Tela de decisão, card de ticker, rodapé com 2 ações. Mesmo arquivo em `../../dashboard-ui/assets/visual-refs/DXeeUP7FKGs_1.jpg` |
| `../../ux-patterns/assets/visual-refs/DfgcqeMBPCU.jpg` | @motion_ui_interface | Painéis slow-mo: **bottom sheet "Choose a ride" snap 146px + 7px**, tooltip da seta, typing dots, toast 64px/92%, file drop, "Paid" com confetti 460ms | Bottom sheet, toast, sucesso de pagamento (curvas) |
| `../../ux-patterns/assets/visual-refs/Ddy5RJOha1U.jpg` | @motion_ui_interface | Botão "Add to cart" com medidas: 44px de alvo, 48 de altura, 24 de padding, 17px semibold, pill 24 | Botão primário de rodapé/CTA do app |
| `../../ux-patterns/assets/visual-refs/Dd25eCoBJGr.jpg` | @motion_ui_interface | Leis parte 1 em painéis: Fitts (card de produto 0,66 vs 0,28 s), Hick ("Share to" 12 vs 4 + More), Chunking, Doherty, Proximity (formulário 1:3), Von Restorff | Share sheet, formulário com espaçamento de label, CTA perto do conteúdo |
| `../../ux-patterns/assets/visual-refs/Dd4UtBDBsIS.jpg` | @motion_ui_interface | Parte 2: cartão de carimbos 19% vs 34%, telefone tolerante, endereço 31 vs 16 teclas, chevrons em settings, **curva serial position (tab bar)**, peak-end | Onboarding com progresso, formulário tolerante, posição da ação na tab bar |
| `../../ux-patterns/assets/visual-refs/Del7XTgsuwI.jpg` | @motion_ui_interface | Parte 4: **carrossel com 32% espiando**, dialog com backdrop 17,4 → 2,5:1, aviso no feed, postcode 30 vs 7 teclas, checkout conectado, 24 vs 6 opções | Carrossel horizontal, modal/sheet, stepper de checkout |
| `../../ux-patterns/assets/visual-refs/DerGbJAhUTm.jpg` | @motion_ui_interface | Thread de chat (Maya Chen): lados, 4/18px, accent nas suas bolhas, 1 divisor de horário, "Read" na última, typing | Tela de chat ou assistente de IA |
| `../../ux-patterns/assets/visual-refs/DfreUkyBNQg.jpg` | @designmotionhq | Toolbar de editor de fotos: 12 ícones → 4 com label + More; **sheet "More tools"** agrupada | Toolbar inferior / barra de ícones de app; sheet de "More" |
| `../../ux-patterns/assets/visual-refs/DdtzWoMhLtW.jpg` | @motion_ui_interface | Paginação: total visível, espaço reservado (68px), load more e parar, estado na URL, "End of results", back volta à linha | Lista longa / infinite scroll no app ou web mobile |

## Telas de app (`dashboard-ui`, `design-direction`)

| Caminho | Autor | O que mostra | Quando abrir |
|---|---|---|---|
| `../../dashboard-ui/assets/visual-refs/DSIMwtvDluO_1.jpg` | @ramotion (case Borea AI) | Print: celular com **rosca segmentada e score "74"**, cards de métrica, linha laranja | Home de app de score/investimento |
| `../../dashboard-ui/assets/visual-refs/DSIMwtvDluO_3.jpg` | @ramotion (Borea AI) | Print: kit bento — botão-pílula, **chip de ticker "VOO +0.07%"**, ícone do app, set de ícones, gráfico com cursor + seletor de período | Componentes de app financeiro; ícone de app |
| `../../design-direction/assets/visual-refs/DfyFShTounu.jpg` | @theglidestudio | Duas **telas mobile** dark "Your invoices, handled.": insegura vs segura (grid, espaço, 1 CTA, **tab bar Send/Track/Get paid**) | Layout de confiança em tela de app (fintech, onboarding) |
| `../../dashboard-ui/assets/visual-refs/DffCenmFASU_1.jpg` | @shohan.designs | Print: app fitness preto + teal, "Your Body Is Ready" + **1 botão "Start Workout"**, 93%/89% em fonte de matriz de pontos, **tab bar flutuante** em pílula + botão circular teal à parte | Home de app de score: número + 1 ação; tab bar flutuante com FAB |
| `../../dashboard-ui/assets/visual-refs/DffCenmFASU_2.jpg` | @shohan.designs | Print: tela de treino com card-hero, "Workout Progress 68%" em barra com marcador, Exercises 8/12, tempo 28:42, lista com play | Progresso de tarefa/sessão em app (barra + N/M) |
| `../../dashboard-ui/assets/visual-refs/DffCenmFASU_4.jpg` | @shohan.designs | Print: 3 celulares (home, treino, nutrição com conquistas em mini-anéis) | Ver o sistema inteiro do app; molde de apresentação em leque |
| `../../dashboard-ui/assets/visual-refs/DfmwyDclA0Q_2.jpg` | @shohan.designs | Print: "Cashflow" com abas Daily/Weekly/Monthly, barras azuis + tooltip, This week/Last week/Change, Income/Outcome, transações, tab bar flutuante com pílula rotulada + botão lima | Tela de gráfico + lista no celular; **confira a conta** (Change não fecha) |
| `../../dashboard-ui/assets/visual-refs/DfmwyDclA0Q_4.jpg` | @shohan.designs | Print: 3 celulares — home (saldo, "+ Add Money" azul, score 74% Excellent! lima), cashflow e chat "Lumen AI" com atalhos acima do campo | Finanças pessoais; 2 acentos com papel fixo; chat de IA com chips de sugestão |
| `../../ui-motion/assets/visual-refs/Dfo__tSjk9k_2.jpg` | @noahelhadedy | Print: "Swipe deck" — card de produto em pilha (Kalypso $49, chips Figma/Framer) | Pilha de cards com swipe (o momento lúdico da tela) |

**Total: 32 imagens mapeadas** (15 `ui-motion`, 9 `ux-patterns`, 7 `dashboard-ui`, 1 `design-direction`), mais a cópia
de `DXeeUP7FKGs_1` em `dashboard-ui`.

## Atalhos por pergunta
- "Como faço o app parecer iPhone?" → `De4B0UxPXIk` (ou `Dflzxq5Bqfj` para o visual).
- Bottom sheet → `DfgcqeMBPCU`. Tab bar → `DbfG6fuPE9y` (expressiva) ou `DXeeUP7FKGs_1` (pílula simples).
- Large title / long press → `DfWjKQPhUbn`. Login/OTP → `DfZkZZ4hkuV`. Formulário → `DfcwOHLh76I` ou `Dd25eCoBJGr`.
- Loader/estado → `DfvAY82DSvD`. Refresh/feed → `DfwavjimeIa`. Toast → `DXRpZTTMr9a`.
- Tela de decisão / Buy-Sell → `DXeeUP7FKGs_1`. Score → `DSIMwtvDluO_1` ou `DffCenmFASU_1`. Confiança → `DfyFShTounu`.
- App fitness → `DffCenmFASU_1`/`_4`. Finanças pessoais / chat de IA no app → `DfmwyDclA0Q_4`. Tab bar flutuante + FAB → `DffCenmFASU_1`.

## Avaliadas e não incluídas (não são mobile)
- `../../ux-patterns/assets/visual-refs/DdRneVWhBSY.jpg` (settings): painéis em janela de desktop; as regras valem, o layout não.
- `../../dashboard-ui/assets/visual-refs/DfaQe-CiBfJ_1.jpg` / `_2` (CreditPros): dashboard web em monitor; o padrão de score está em `mobile-patterns.md` §13.
- `../../dashboard-ui/assets/visual-refs/Deoi1WhP83h.jpg` (ilha de foco): web app desktop; o conceito de ilha está em `mobile-patterns.md` §10.
- `../../ui-motion/assets/visual-refs/Dfvja0XCyIi.jpg`, `DZ2Dp5wt0pJ.jpg`, `../../ux-patterns/assets/visual-refs/DfemaTCBncA.jpg`: site, upload e botão sem contexto mobile; números já transcritos.

## Fontes mobile sem imagem (só descrição)
Qwash
`DX_bA4rCWf0` e WayLoo `DVv7OOECewR` (§21), home imobiliária `DfzgxEKlx8z` (`ux-patterns/references/components-checklists.md` §11),
alvo de toque `DfwojjrirKz`, dark mode `DfSa0GRh-gS` e app de clima `DfMN-fgIxOu` (`ux-patterns/references/typography-and-touch.md` §1, §4–5),
hold to publish (`Dfo__tSjk9k`, slide sem print; `ui-motion/references/react-bits.md`). Fitness `DffCenmFASU` e finanças
`DfmwyDclA0Q` agora têm print (tabela acima); `DfmwyDclA0Q_3` (chat no meio da transição) não foi copiado.
