---
name: mobile-app-ui
description: UI/UX de app mobile (iOS e Android nativo, React Native, Flutter, PWA instalável e a versão mobile de web apps) com números concretos — alvos 44pt/48dp e 8px entre alvos, zona do polegar, tab bar de 3–5 itens, stack, modal e bottom sheet, safe areas, Dynamic Type, gestos e haptics, press 95%, pull-to-refresh 35%, springs, large title 34→18, teclado e formulários, estados offline/carregando, listas e infinite scroll, rodapé fixo com total, Buy/Sell fixos, convenções HIG vs Material (sheet detents, navigation rail), PWA vs nativo, permissões e onboarding (NN/g), 60fps e dark mode. Aponta para as references e imagens de ui-motion, ux-patterns, dashboard-ui e design-direction. Use quando falarem em "app de celular", "app mobile", "iOS", "Android", "React Native", "Flutter", "PWA", "tab bar", "bottom sheet", "tela de app", "gestos", "swipe", "safe area", "notch", "Dynamic Island", "haptic", "onboarding do app", "checkout no app", "app fitness/finanças" ou "versão mobile".
---

# Mobile App UI

Skill de **plataforma**: traz só o que é específico do celular e aponta para as skills de **tema** (`ui-motion`,
`ux-patterns`, `dashboard-ui`, `design-direction`), que continuam sendo a base. Não copie de lá: abra a seção indicada.
Os números vêm dessas skills (reels e carrosséis listados nos `visual-index.md` delas). O que está marcado
**(complemento)** é conhecimento geral (WCAG, prática de mercado), não vem das fontes. Regras de Apple HIG, Material 3
e NN/g lidas nas páginas oficiais (pesquisa 9A/9B, nov/2026) vêm com a fonte citada; **[PWA]** = vale no PWA/Capacitor,
**[nativo]** = só em app nativo (SwiftUI/UIKit/Compose).

## Escopo e fronteiras
- **Esta skill:** apps de celular iOS/Android (SwiftUI, UIKit, Compose, React Native, Expo, Flutter), PWA instalável
  e a **experiência mobile de um web app** (mesmo produto aberto num celular de 360–430 px).
- **Não é esta skill:** site de marketing, landing, portfólio → `website-ui`; app desktop, web app de tela grande,
  dashboard com sidebar → `desktop-app-ui`. Tablet: comece por `desktop-app-ui` e use os gestos e alvos daqui.
- Padrões de tela detalhados (onboarding, login, feed, checkout, decisão, score…) → `references/mobile-patterns.md`.
- Quais imagens já existentes mostram app mobile → `references/visual-index.md`.

## Prioridade entre skills (quando as regras conflitam)

1. **Valores e decisões de design** (números, quantidade de animação, cor, sombra, tipografia) vêm das **skills do projeto**: `website-ui`, `desktop-app-ui`, `mobile-app-ui`, `design-direction`, `ui-motion`, `ux-patterns`, `dashboard-ui`.
2. **Skills de terceiros** (`design-taste-frontend`, `impeccable`, `transitions-*`, `gsap-*`, `playwright-cli`, `extract-design`) servem para **implementação**: código pronto, APIs, checkers e verificação no browser. Use o código delas, mas com os valores do item 1.
3. Se o checker ou a regra de uma skill de terceiros reprovar algo que segue o item 1, **siga o item 1** e diga ao usuário qual regra externa foi ignorada e por quê.
4. Na plataforma, vale a skill da plataforma (`website-ui`, `desktop-app-ui` ou `mobile-app-ui`); nos temas, vale a skill de tema que ela indicar.

| Conflito | Vale | Em vez de |
|---|---|---|
| **Quantidade de animação** | **1 momento animado por página**: a entrada do hero **ou** um momento no CTA/seção, nunca os dois. Página longa também fica com 1. Micro-feedback funcional (press, hover, foco, sucesso) não conta | `design-taste-frontend`: entrada do hero + 1 momento por página (2 em página longa) |
| **Durações** | Os tokens de `ui-motion`: press **160 ms** (feedback em 0 ms), stagger **70–100 ms**, expandir card/abrir painel **350 ms**, sucesso **470 ms**, reveal **≤ 700 ms**. Onde `ui-motion` não tem número, use o token de `transitions-dev` (micro 80 ms, quick 150 ms, fast 250 ms) | `transitions-dev`: stagger 40 ms, panel open 400 ms, success check 500 ms |
| **Sombras** | Seções e blocos se separam por **espaço ou mudança de fundo**, sem sombra (as duas fontes concordam). **Sombra tingida** (cor do fundo, blur = 2× Y, ~8%) **só em elementos que flutuam**: dropdown, popover, modal, card arrastável, toast | `design-taste-frontend` sem sombras em nada; e sombra preta genérica |

## Regras específicas do celular (com números)

**1. Alvos de toque.** Mínimo **44 × 44 pt** iOS e **48 × 48 dp** Android; app web/PWA no celular segue o piso **44px** desta skill (o piso 24px/meta 44 é de site, `website-ui`). Cresça
por padding (**20 + 12 + 12 = 44**), nunca o ícone; **~8px** entre áreas de alvos pequenos (centros a 52px, não 32px).
Botão primário **48px** de altura, 24px de padding, label 17px semibold (`ux-patterns` → `typography-and-touch.md` §1,
`components-checklists.md` §1–2). Fontes oficiais (rodada 9A/9B): Apple **44×44pt padrão, 28×28pt mínimo absoluto**
(só para controle secundário denso), ~12pt de folga em controle com borda/fundo e ~24pt sem; Material **48×48dp + ≥ 8dp**
entre alvos (ícone 24dp com padding até 48); NN/g mede em **tamanho físico: ≥ 1 × 1 cm**, ~2 × 2 cm para ação primária
ou uso em movimento, e alerta da "view–tap asymmetry" (pontinhos de carrossel legíveis mas impossíveis de tocar).
[PWA] use **44px CSS de piso e 48px de padrão** (1dp ≈ 1px CSS é inferência). Mapa com pinos pequenos → ofereça lista.

**2. Zona do polegar.** Ação principal grande e perto (Fitts: 0,66 s → 0,28 s). Ações de decisão e CTA de compra
**fixos no rodapé** (Buy/Sell, "Schedule a collection", "Pay now"). Topo da tela = leitura e navegação secundária
(`ux-laws.md` Parte 1; `components-checklists.md` §9–10). Destrutivo nunca no lugar onde o polegar pousa por hábito (complemento).

**3. Tab bar.** **3–5** destinos de primeiro nível (Hick: 12 → 4 + More, 0,74 s → 0,46 s), **seções, não ações**
(complemento HIG). Ícone + rótulo; **um accent** só na aba ativa (pílula flutuante: WayLoo, Markets). Botão central
circular para ação principal só funciona por ser **visualmente distinto** (Von Restorff), não pela posição —
divergência com Serial position registrada em `components-checklists.md` §10. Indicador **viaja**, não pisca
(`ui-motion` → `micro-interactions.md` §11 Meniscus, §13 pílula). Oficial (9A/9B): NN/g — tab bar persistente e
rotulada aguenta **4–5** destinos, acima disso o alvo encolhe; hambúrguer esconde a navegação ("longe da vista") e
menu por swipe de borda sem sinal quase ninguém descobre (e briga com o voltar do iOS). Apple — tab bar é navegação,
**ações vão na toolbar**; sempre visível (exceto sob modal); **evite aba "More"**; **nunca desabilite nem esconda
aba** (seção vazia explica o porquê); rótulo de 1 palavra; badge só para o crítico; ≤ 5 se for personalizável.
Material — largura **compact < 600dp → navigation bar inferior**; medium 600–839 → bar ou **navigation rail**;
expanded ≥ 840 → rail (expandida). Troque só componentes equivalentes (bar ↔ rail; bottom sheet ↔ menu).

**4. Navegação: stack, modal, sheet.** Hierarquia em **stack** com back (o edge-swipe de voltar do iOS nunca é
bloqueado; Android respeita o back do sistema — complemento). Tarefa autocontida em **modal/sheet**. Bottom sheet
**segue o dedo e faz snap** (146px com overshoot de 7px), página atrás escurece (`components-checklists.md` §8;
backdrop 17,4:1 → 2,5:1, `ux-laws.md` Figure-ground). Card → detalhe: **o card vira a página e volta para onde estava**
(`page-transitions-and-timing.md`). Side menu: página encolhe para **86%** e desliza **150px** ("push, don't cover").
**Sheet (Apple HIG, 9A):** tarefa curta e contextual; **uma sheet por vez**; detents **medium (~½ da altura)** e
**large (altura total)**; **grabber** visível em sheet redimensionável; swipe para baixo fecha e, com alteração não
salva, confirma antes; botões Cancel (início) + Done (fim) ou Back em fluxo de etapas — **nunca os três juntos**;
fluxo longo vai para tela cheia. [nativo] `presentationDetents`/`UISheetPresentationController`; [PWA] snap points
(Drawer do shadcn/Base UI ou Motion `drag="y"` — ver `references/component-libraries.md`).

**5. Safe areas.** Nada interativo sob notch, Dynamic Island, home indicator ou cantos arredondados; rodapé fixo soma
`env(safe-area-inset-bottom)` / `WindowInsets` / `SafeAreaView` (complemento). Status bar não cobre conteúdo — bug real
no protótipo do Claude Design (`design-direction` → `claude-design-course.md` "Mobile App Prototype").

**6. Tipografia mobile.** Escala **16 × 1,2^n** (16, 19, 23, 28, 33, 40, 48) é a recomendada para produto denso em tela
pequena; line-height 1,5 no corpo → 1,1 no display; tracking −0,02em em títulos (`typography-and-touch.md` §2, §2b).
Se seguir a escala nativa iOS (corpo **17pt**), mantenha a nativa e não misture. **Dynamic Type / font scale do
Android:** use estilos de texto do sistema, teste em 200% e deixe linhas quebrarem (complemento HIG/Material; piso 11pt).
Large title **34 → 18px ligado ao scroll** (`micro-interactions.md` §4). Número-herói enorme (20 → 76px no app de clima, §5).
Oficial (9A): Apple iOS corpo **17pt padrão / 11pt mínimo**; texto ampliável a **≥ 200%**; **evite pesos Ultralight,
Thin e Light** (prefira Regular/Medium/Semibold/Bold; fonte fina pede tamanho maior); não trunque em área rolável,
empilhe o layout em tamanhos grandes; poucas famílias. Material: escala **Major Second 1,125, base 14**, 15 estilos
baseline + 15 emphasized, `rem` na web — divergência com a 1,2 acima: em app Android puro siga a do Material; não
misture escalas. [PWA] `font: -apple-system-body`/`system-ui` ou fonte própria em `rem`, nunca `px` fixo no corpo.

**7. Gestos e haptics.** Todo gesto tem alternativa visível (botão/menu) (complemento). Swipe-away segue o dedo,
inclina **12°** e sai com velocidade; photo viewer segue **1:1** e volta com spring; long press = **400ms** de hold,
sobe 5%, fundo escurece; drag-to-reorder sobe a **105%**, os outros deslizam 200ms (`micro-interactions.md` §2–6).
Haptic leve em snap, toggle, sucesso e no ponto de soltar do pull (complemento: `UIImpactFeedbackGenerator`,
`HapticFeedbackConstants`); nunca em scroll contínuo. "Segurar para confirmar" para ação irreversível (`react-bits.md`, `Dfo__tSjk9k`).

**8. Micro-interações (valores de `ui-motion`).** Feedback no **touchdown, 0 ms** (não no release, 120 ms); press
**0,95** → spring; spring iOS **damping 0.8 (~1,5% overshoot)**; toasts **stiffness 180 / damping 20**, máx. 3,
**no topo no mobile**, swipe para dispensar; pull-to-refresh **dedo 100% → lista 35%**; rubber band **200 → 86px**;
momentum ~1000px; stagger 70/100ms; expand **ease-out 350ms**; sucesso **470ms**. Tudo **interrompível**.
**Um momento lúdico por tela.** Tokens em `ui-motion/SKILL.md`; receitas em `css-recipes.md`.

**9. Teclado e formulários.** Tipo de teclado certo por campo (`inputmode`/`keyboardType`: email, tel, numeric,
`autocomplete="one-time-code"`) e `autocomplete` em tudo (complemento). O campo focado e o botão de enviar **sobem
acima do teclado** (`KeyboardAvoidingView`, `visualViewport`, `adjustResize` — complemento). Label a **8px** do campo e
**24px** do próximo; label flutuante 20 → 14px; OTP com dígitos caindo **70ms**; medidor de senha em 4 segmentos;
Postel (1/4 → 4/4 formatos aceitos), Tesler/Parkinson (31 → 16 e 30 → 7 teclas: CEP primeiro). `ux-laws.md`, `micro-interactions.md` §5–6.
NN/g (9B): **coluna única**, **sem placeholder no lugar de rótulo**, "(opcional)" marcado, validar **só depois que o
campo termina**, erro **ao lado do campo** com cor + ícone, ajuda extra após **3 erros** repetidos; botão de enviar
**abaixo dos campos** (nunca no topo, padrão iOS que falha em teste) ou **fixo no rodapé**; senha: mostrar/ocultar,
regras antes, sem campo de confirmação duplicado; digitar senha no celular leva ~2× mais tempo → login social/biometria/código.

**10. Estados: carregando, vazio, erro, offline.** Feedback ≤ **400ms** (Doherty); título primeiro, nunca 2 s em
branco. Skeleton para conteúdo, barra/anel com % quando se sabe, spinner só < 3 s, loader **dentro do botão** para ação
do usuário (`loaders-and-refresh.md`). UI otimista (like 142 → 143) com reversão clara. Teste os 4 estados: **vazio,
carregando, erro, texto longo**; não abra a home com estado vazio. **Offline** (complemento): banner discreto
persistente, conteúdo em cache visível, ações enfileiradas com estado "pendente", retry inline como no upload que retoma de 90%.

**11. Listas, refresh e infinite scroll.** Pull-to-refresh em listas mobile (release cue, "new posts pill" para não
perder o lugar); **espaço reservado** (sem shift de 68px que faz o toque cair no item errado); infinite scroll só em
feed — em resultados use **"Load more, then stop"** e "End of results"; **back restaura o scroll e a linha** (400 linhas).
Virtualize listas longas. Próximo card **espia 32%** em carrossel horizontal (Closure). `components-checklists.md` §4,
`loaders-and-refresh.md`, `perceived-performance.md` item 23.

**12. iOS vs Android (complemento).** iOS (HIG): tab bar embaixo, large title, back com chevron + edge-swipe, sheets
com detents, SF Pro, cantos contínuos (squircle, `micro-interactions.md` §1). Android (Material 3): navigation bar
embaixo (3–5), top app bar, back do sistema/predictive back, FAB para a ação principal, bottom sheet com handle,
Roboto/fonte da marca, ripple. Cross-platform (RN/Flutter): siga a plataforma em navegação, back e controles nativos
(switch, picker, date); a marca entra em cor, tipo, ilustração e motion. Detalhes em `ext-impeccable` (`reference/ios.md`, `reference/android.md`). **Web/PWA com cara de iOS:** shadcn (Base UI) + Tailwind + Motion e uma camada própria de **tab bar, título grande que colapsa, sheet com snap points e push/pop com swipe-back**; Ionic React como plano B no Capacitor (`references/component-libraries.md`, pesquisa 9D).

**13. Performance e 60fps.** Anime só `transform`/`opacity`; nada de animar `width/height/top` em lista; parallax
decorativo em mobile não (`scroll-and-screen-transitions.md` §2–3). Imagens WebP/AVIF com lazy load, listas
virtualizadas, sem re-render desnecessário, **teste em celular médio e rede lenta** (`perceived-performance.md` itens 02,
15, 23, 26, 31). Orçamento de 16,7ms por frame; gestos na thread de UI (Reanimated/worklets, Flutter) (complemento).

**14. Dark mode.** Sem `#000` (ex.: `#0C1424`), texto a **87%**, accent clareado (2,9:1 → 8,6:1), elevação por
luminosidade, glow com parcimônia (`typography-and-touch.md` §4). Siga o tema do sistema por padrão. Seletor de tema próprio: a Apple HIG pede para **evitar** no app ("Avoid offering an
app-specific appearance setting", developer.apple.com/design/human-interface-guidelines/dark-mode); ofereça só com motivo de produto. Vidro **só** sobre conteúdo: blur 30px atrás da tab bar (`micro-interactions.md` §8);
"Reduce transparency" nas settings (`dashboard-ui` → `domain-examples.md` §2).

**15. Acessibilidade e motion reduzido.** Contraste 4,5:1 texto/placeholder, 3:1 ícones/bordas; variação sempre com
**sinal + cor**; `prefers-reduced-motion`/Reduce Motion troca deslocamento por fade ≤150ms. Labels para VoiceOver/TalkBack
em botões de ícone, ordem de foco lógica (complemento). **Reduce Motion (Apple HIG, 9A):** springs mais firmes (menos
bounce), animação presa ao gesto, nada de animar profundidade (z), troque x/y/z por **fade**, sem entrar/sair com blur.
Motion nunca é o único canal (some haptic/texto) e é sempre cancelável. Contraste Apple: 4,5:1, **buscar 7:1 em texto
pequeno no dark**. [PWA] com Motion for React, `<MotionConfig reducedMotion="user">` na raiz (o padrão é `"never"`).

**16. Primeiro uso, permissões e confiança (NN/g, 9B).**
- **Evite onboarding instrucional** (deck de cards não melhorou desempenho em estudo): prefira dica em contexto,
  empty state que ensina e UI aprendível. Só vale quando o app **precisa de dados para começar**, é muito
  personalizado ou o fluxo é realmente novo; aí: poucos cards, 1 ideia por card, **"Pular" visível**, progresso,
  explicar por que pede cada dado; **tema/cor não se escolhe no onboarding**; promoção de função só quando ela fica acionável.
- **Confiança em degraus** (5 níveis): não peça cadastro, dado pessoal ou conta conectada antes de entregar valor;
  login obrigatório na 1ª tela pula para o nível 3; conectar conta social é nível 5. Login opcional quando possível.
- **Permissões no contexto** (ao tocar no recurso), só as essenciais na 1ª abertura; frase "[app] quer acessar
  [recurso] para que você possa [benefício]" — dar motivo subiu o aceite em **12%** e o melhor texto rendeu **+81%**
  sobre o pior; nunca "para melhorar sua experiência". Se negar: tela explica o que não funciona + botão para os
  Ajustes. [nativo] iOS usa purpose string, Android pede tela explicativa antes do diálogo; [PWA] a permissão é do
  navegador (pré-aviso é seu, e não há "abrir Ajustes" — explique o caminho). Detalhes: `references/mobile-patterns.md` §1–2, §7.

## PWA vs nativo — o que dá para aproximar
| Recurso | [nativo] | [PWA] / Capacitor (aproximação) |
|---|---|---|
| **Liquid Glass** (material de vidro do iOS 26+) | só em UIKit/SwiftUI | `backdrop-filter: blur()` + fundo translúcido **só sobre conteúdo** (tab bar, sheet), com fallback opaco e "Reduce transparency"; nunca em texto longo (`dashboard-ui/references/glassmorphism.md`) |
| **Dynamic Type** | estilos de texto do sistema | `font: -apple-system-body` no Safari ou tamanhos em `rem` + zoom do navegador; teste 200%; sem altura fixa em linha de texto |
| **SF Symbols** | `Image(systemName:)` | não embutir (licença Apple); use biblioteca de ícones própria (Lucide/Phosphor) no mesmo peso do texto |
| **SF Pro** | fonte do sistema | `font-family: system-ui, -apple-system` (cai em Roboto no Android); não empacotar SF Pro |
| **Sheet detents / grabber** | `presentationDetents` | Drawer com `snapPoints` + handle; `body{position:relative}` no iOS Safari |
| **Swipe-back / stack** | grátis no `UINavigationController` | Ionic (nativo) ou camada própria com Motion `drag="x"` + `AnimatePresence`; nunca bloquear o gesto do navegador |
| **Haptics** | `UIImpactFeedbackGenerator` | Capacitor Haptics; PWA puro: `navigator.vibrate` não existe no iOS Safari → sem haptic |
| **Safe area** | `SafeAreaView`/insets | `viewport-fit=cover` + `env(safe-area-inset-*)` |
| **Permissões** | diálogo do SO | diálogo do navegador (PWA) ou do SO via plugin (Capacitor) |
Linhas sem número de fonte são **(complemento)**; Liquid Glass, Dynamic Type, SF Symbols e detents são nativos
segundo o HIG (9A). Bibliotecas e camada iOS própria: `references/component-libraries.md`.

## Checklist mobile (copie para a auditoria)
- [ ] Todo alvo ≥ 44pt/48dp, ≥ 8px entre áreas; medido, não estimado.
- [ ] Ação principal e decisão no rodapé (zona do polegar), acima da safe area e do teclado.
- [ ] Tab bar 3–5 seções, ícone + rótulo, 1 accent na ativa; back do sistema e edge-swipe funcionando.
- [ ] Sheet com snap e backdrop; card → detalhe sem corte seco; modal só para tarefa autocontida.
- [ ] Nada sob notch/Dynamic Island/home indicator; status bar não cobre conteúdo.
- [ ] Uma escala tipográfica; Dynamic Type/font scale testados em 200% sem cortar texto.
- [ ] Feedback no touchdown (0 ms), press 0,95, springs interrompíveis, 1 momento lúdico por tela.
- [ ] Teclado certo por campo, `autocomplete`, campo focado visível acima do teclado.
- [ ] Estados vazio/carregando/erro/texto longo/offline desenhados; skeleton sem layout shift.
- [ ] Lista: pull-to-refresh, back restaura posição, "End of results", virtualização.
- [ ] Dark mode sem #000, texto 87%, contraste AA; reduced motion respeitado.
- [ ] Total do rodapé bate com o valor do botão; Buy e Sell do mesmo tamanho.
- [ ] Sem pesos Ultralight/Thin/Light no texto; corpo ≥ 17pt iOS (piso 11pt).
- [ ] Sheet: 1 por vez, detents medium/large com grabber, Cancel+Done (nunca os três), confirma ao descartar.
- [ ] Nenhum pedido de cadastro/permissão antes de entregar valor; permissão no contexto com motivo e caminho de volta.
- [ ] Cada regra marcada [PWA]/[nativo] conferida na plataforma real (Liquid Glass, Dynamic Type, SF Symbols só nativos).
- [ ] Largura ≥ 600dp (tablet/paisagem): bar → navigation rail, sheet → menu (`desktop-app-ui` breakpoints).

## Workflow
1. **Plataforma e stack**: iOS, Android, os dois (RN/Flutter) ou web mobile/PWA? Defina o que segue a plataforma
   (navegação, back, controles) e o que é marca (cor, tipo, motion).
2. **Mapa de telas e navegação**: tab bar (3–5), stacks, o que é sheet/modal. Escolha o padrão de cada tela em
   `references/mobile-patterns.md` e abra o ponteiro da skill de tema indicado lá.
3. **Direção visual**: paleta 2+1 e par tipográfico em `design-direction`; layout de confiança mobile (`DfyFShTounu`).
4. **Tokens**: `--tap: 44px` (48 Android), `--tap-gap: 8px`, espaço em grade de 8, escala tipográfica, tokens de motion
   de `ui-motion`, insets de safe area.
5. **Implementar** telas e estados (vazio, carregando, erro, texto longo, offline); micro-interações com os valores
   de `ui-motion/references/css-recipes.md` (web) ou springs nativas (Reanimated, SwiftUI `.spring`, Flutter `SpringSimulation`).
6. **Verificar no navegador em viewport mobile** com `ext-playwright-cli`, em **375×812** (iPhone X/11 Pro/13 mini),
   **390×844** (iPhone 12–15) e **360×800** (Android médio): emule toque e DPR (`--device "iPhone 13"` ou viewport +
   `isMobile`/`hasTouch`), tire screenshot de cada tela, meça alvos com `getBoundingClientRect()` (reprovar < 44),
   confira rodapé fixo + safe area, teclado virtual não cobrindo o CTA, `prefers-reduced-motion` e dark mode emulados,
   rede lenta (throttling) e rolagem sem scroll horizontal. App nativo: simulador/emulador + Accessibility Inspector /
   TalkBack e "Maior texto" (complemento).
7. **Crítica final**: `ux-patterns` (checklist central), `ext-impeccable` (audit/critique; `ios.md`, `android.md`),
   `design:accessibility-review` para WCAG. Reporte antes → depois com números.

## Onde está o resto
| Preciso de… | Abra |
|---|---|
| Valores de press, spring, pull, rubber band, momentum, interrupção, squircle | `ui-motion/references/micro-interactions.md` §1–2 |
| Large title, long press, side menu, speed dial, slider | `ui-motion/references/micro-interactions.md` §4 |
| Swipe away, add to cart, submit morph, stagger de lista | `ui-motion/references/micro-interactions.md` §3 |
| OTP, rating, senha, to-do, reações / label flutuante, map pin, photo viewer | `ui-motion/references/micro-interactions.md` §5–6 |
| Vidro na tab bar, cantos concêntricos, Dynamic Island | `ui-motion/references/micro-interactions.md` §8 |
| Toasts no mobile, upload, tab bar líquida, pílula que desliza | `ui-motion/references/micro-interactions.md` §9–11, §13 |
| Loaders, 8 formas de atualizar, pull-to-refresh | `ui-motion/references/loaders-and-refresh.md` |
| Durações, easing vs spring, card → página, reduced motion | `ui-motion/references/page-transitions-and-timing.md` |
| Onde animar scroll/troca de tela e onde não; 1 momento por tela | `ui-motion/references/scroll-and-screen-transitions.md` §1–5 |
| Snippets (press, `linear()` spring, pull, stagger, FLIP, toast stack) | `ui-motion/references/css-recipes.md` |
| Componentes prontos (hold to publish, swipe deck, PillNav) | `ui-motion/references/react-bits.md` |
| Alvos 44pt/48dp, escala, line-height, contraste, dark mode, grade de 8 | `ux-patterns/references/typography-and-touch.md` §1–6 |
| Botão, chat, toolbar + More, bottom sheet, tela de decisão, fluxo de pedido, home | `ux-patterns/references/components-checklists.md` §1–2, §5, §7–11 |
| Fitts, Hick, Doherty, Proximity, Goal gradient, Closure, Figure-ground… | `ux-patterns/references/ux-laws.md` |
| Paginação / infinite scroll / back que restaura | `ux-patterns/references/components-checklists.md` §4 |
| Performance (31 itens), testar em celular e rede lenta | `ux-patterns/references/perceived-performance.md` |
| Dark patterns (trial, nagging, X falso) | `ux-patterns/references/dark-patterns.md` §A |
| App de trading: card de ticker, detalhe, Buy/Sell | `dashboard-ui/references/layout-patterns.md` §8; `domain-examples.md` §20 |
| Pedido em 4 etapas, rodapé com total, tab bar com ação central | `dashboard-ui/references/layout-patterns.md` §9; `domain-examples.md` §21 |
| Apps de score (fitness, finanças, crédito) | `dashboard-ui/references/layout-patterns.md` §10; `domain-examples.md` §29 |
| Gamificação (progresso, streak, metas, conquistas) | `dashboard-ui/references/layout-patterns.md` §7 |
| Paleta 2+1, 60/30/10, par tipográfico, sombra tingida | `design-direction/references/color-palettes.md`, `typography-pairing.md`, `layers-and-trust-layout.md` §4 |
| Layout que parece seguro (2 telas mobile) | `design-direction/references/layers-and-trust-layout.md` §2 |
| Protótipo de app mobile no Claude Design | `design-direction/references/claude-design-course.md` "Mobile App Prototype" |
| Padrões de tela deste skill e imagens mobile | `references/mobile-patterns.md`, `references/visual-index.md` |
| Pesquisa NN/g completa (onboarding, empty state, formulários, permissões, HEART/CASTLE) | `ux-patterns/references/nng-research.md` |
| Bibliotecas (shadcn, Ionic, Framework7…) × React 18/PWA/Capacitor; camada iOS própria | `references/component-libraries.md` |
| Onde buscar inspiração (Mobbin 🔒, Dribbble, Behance, kits Figma) e prints da pesquisa 9 | `references/benchmark-sources.md` |
| Durações/easing oficiais (Apple sem números, Material springs → CSS, Carbon), Reduce Motion, `MotionConfig` | `ui-motion/references/official-motion-guidelines.md` (os tokens de `ui-motion` prevalecem) |

## Skills externas (dependências)
Esta skill pode delegar para: `ext-playwright-cli`, `ext-impeccable`, `ext-transitions-dev`. Elas **não** fazem parte
da repo; são instaladas por `scripts/install-external-skills.sh`.
1. Antes de delegar, confira se a pasta existe em `.claude/skills/<nome>/` ou `~/.claude/skills/<nome>/`.
2. Se faltar, **pergunte ao usuário** antes de instalar e, com o ok, rode `./scripts/install-external-skills.sh` (ou
   `--global`). Se alguma não aparecer depois, leia o `SKILL.md` instalado com Read e siga as instruções dele.
3. Se o usuário não quiser instalar, siga sem elas usando as references desta skill e das skills de tema.
