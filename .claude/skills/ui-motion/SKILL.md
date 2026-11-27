---
name: ui-motion
description: 'Projeta e implementa micro-interações e motion de UI com valores concretos: press (95%), pull-to-refresh (35%), números rolando, ícones que morfam, toasts, drag-and-drop, loaders, card→página, pílula de navegação, durações, easing, springs, um momento animado por página, motion de site e de redes (reel, logo, carrossel), bibliotecas animadas e comparação com Apple HIG, Material 3, Carbon e Atlassian. Use quando o pedido falar em "animar", "micro-interação", "app mais fluido/premium", "spring", "easing", "quanto tempo deve durar a animação", "loader/skeleton", "pull to refresh", "toast", "drag and drop", "transição de página", "scroll reveal", "um momento animado", "biblioteca de componentes", "ícone animado", "polish de motion", "React Bits", "reel", "carrossel", "animar logo", "Material 3 motion", "Carbon", "Apple HIG motion", "Reduce Motion", "MotionConfig" ou "por que o iPhone parece tão suave".'
---

# UI Motion

Motion é metade de como uma interface "parece". Apps premium não são mais rápidos — **se movem melhor**: respondem no toque, usam springs, nunca cortam, e tudo vem de algum lugar.

## Quando usar
- Adicionar ou revisar animações/estados de componentes (botões, listas, ícones, toasts, uploads, loaders).
- Escolher duração, easing ou parâmetros de spring.
- Transições entre telas/rotas, menus, modais.
- "Polish pass" final de um app ou site.
- Reels, vídeo de produto/demo de site, logo animado e carrossel educativo (`references/motion-for-social-video.md`).

## Regras centrais (com números das fontes)
1. **Responda no touchdown, 0 ms.** Feedback no `pointerdown`, nunca no release (o "sem" do reel tinha 120 ms de atraso).
2. **Press = afundar para 95% e voltar com spring.** Escala `0.95` → `1` com leve overshoot.
3. **Anime com springs, não timers.** Referência iOS: damping ~0.8, **overshoot ~1.5%**, depois assenta. Para pilhas de toasts: **damping 20, stiffness 180**.
4. **Toda animação é interrompível.** Se o usuário fecha um painel no meio da abertura, ele inverte de onde está — nunca espere 180 ms terminar.
5. **Resistência na borda.** Pull-to-refresh: dedo 100%, lista **35%**. Rubber band iOS: puxão de **200 px estica 86 px** e volta com spring.
6. **Momentum.** Flick continua deslizando (~**1000 px**, decaimento 0.998/ms) depois que o dedo sai.
7. **Durações** (theglidestudio): **press ≈ 160 ms** ("um piscar"), **reveal < 1 s (~700 ms)**, **cena completa ≈ 1,2 s**. 2,4 s = lento demais; 0,1 s = rápido demais, você não vê de onde veio.
8. **Ease-out para entradas/expansões**: rápido no começo, devagar no fim. Card expand = **ease-out 350 ms**.
9. **Cascade, não dump.** Stagger de **70 ms** (linhas de lista, dígitos OTP, emojis) ou **100 ms** (dígitos rolando, estrelas, ações de speed dial).
10. **Morph, não swap.** Ícones e botões mudam de forma (play→pause 300 ms; botão 260→64 px virando spinner em 270 ms; Dynamic Island cresce da pílula). Nada "pisca" para outro desenho. Quando não dá para morfar, troque o ícone com **desfoque curto + fade** (@fabianocarvalhojr `Df5pCOhmYuP`, rodada 10A).
11. **Nada aparece do nada.** Card vira a página e volta exatamente para onde estava; menus nascem do botão que os abriu.
12. **Percepção > velocidade real.** Skeleton em vez de tela vazia, UI otimista (mostre sucesso já), barra de progresso que começa rápida e desacelera.
13. **Respeite `prefers-reduced-motion`.** Troque deslocamentos/escala/bounce por fade curto (≤150 ms) ou corte; mantenha o feedback de estado (cor, ícone, texto) (complemento). Regras da Apple HIG: springs mais firmes (menos bounce), animação segue o gesto, nada de profundidade (z), x/y/z vira fade, sem blur entrando/saindo. Com Motion for React, **`<MotionConfig reducedMotion="user">` na raiz é obrigatório** (o padrão é `"never"`). Ver `references/official-motion-guidelines.md` §1.1 e §5.
14. **Título primeiro.** Nunca deixe a tela em branco: "2 s em branco parecem uma hora". O título aparece no primeiro paint e o resto entra em cascata (theglidestudio, Dfy7ig_B-FL).
15. **Texto de reel: ≤ 6 palavras, grande, 1,2 s na tela**; se não dá para ler duas vezes, está rápido. **Logo: ~1 s**, e o tipo de movimento é a personalidade (linha lenta = calmo, encaixe rápido = rápido, crescer de um ponto = amigável) (theglidestudio, DfxpIbfP-SB, Dfzkwu3hSj5).
16. Anime só `transform` e `opacity` sempre que possível; evite animar `width/height/top` em listas grandes. (complemento)
17. **Um momento animado por página/tela.** Hero **ou** CTA, não os dois; "se tudo mexe, nada é especial" (@noahelhadedy, 2 posts). Feedback funcional (press, hover, sucesso) não conta (complemento). Ao pedir motion de site ao Claude: visuais + cores da marca + descrição do movimento, **um efeito por vez**, testar em desktop e mobile (@mobileeditingclub). Detalhes em `references/scroll-and-screen-transitions.md` §5–6.
18. **Indicador viaja, não pisca.** A pílula do item ativo desliza até o item clicado (GSAP `power3.out`, Code & Chill) e a tela troca com transição curta (`references/micro-interactions.md` §13).
19. **Faixa e frequência** (rodada 10A, @samro_ai `DgI3UF_k_-G`, "19 regras de animação"): a maior parte do motion de componente fica em **100–500 ms** (NN/g) e a resposta chega em **≤ 400 ms** (Doherty); ação repetida **~100×/dia não anima** (Emil Kowalski), só muda de estado. Os tokens desta skill já caem na faixa; `--dur-reveal` (700 ms) e `--dur-scene` (1,2 s) ficam acima porque são de reveal de site e troca de cena, não de componente: **valem os tokens** (heurística × token da skill). Detalhes em `micro-interactions.md` §14.
20. **Motion segue o visitante** (@theglidestudio `DgEyy8nRybB`, "Follow, don't lead"): o efeito ligado ao scroll avança com o polegar e **para quando ele para**. Reforça "sem scroll-jacking" (`scroll-and-screen-transitions.md` §2).
21. **Texto animado < 1 s** (@ale.uiux `DgQYY6OpZMB`): typewriter (notas, busca), word stream (resposta de IA), scramble (senha, código), retype (hero), typing dots (chat), letter rise (boas-vindas). Escolha 1 pelo contexto (`micro-interactions.md` §17).

## Tokens de motion recomendados

| Token | Valor | Origem |
|---|---|---|
| `--press-scale` | 0.95 | DfP6EoLBtgg |
| `--lift-scale` (drag/long press) | 1.05 | DfP6EoLBtgg, DfWjKQPhUbn |
| `--dur-press` | 160 ms (início do feedback: 0 ms) | Dfvja0XCyIi, De4B0UxPXIk |
| `--dur-reorder` (outros abrem espaço) | 200 ms | DfP6EoLBtgg (tela) |
| `--dur-morph-icon` | 300–400 ms | DfVOGNnzR_D |
| `--dur-expand` | 350 ms ease-out | DfP6EoLBtgg |
| `--dur-success` (círculo → tick) | 470 ms | DfP6EoLBtgg, DfZkZZ4hkuV |
| `--dur-reveal` | ~700 ms (sempre < 1 s) | Dfvja0XCyIi |
| `--dur-scene` | ~1,2 s | Dfvja0XCyIi |
| `--stagger-tight` / `--stagger` | 70 ms / 100 ms | DfTr-mwhZT3, DfZkZZ4hkuV, DfP6EoLBtgg |
| `--pull-resistance` | 0.35 | DfP6EoLBtgg |
| spring "UI" | damping ratio 0.8 (~1.5% overshoot) | De4B0UxPXIk |
| spring "stack/toast" | stiffness 180, damping 20 | DXRpZTTMr9a |
| toast timeout | info 4 s · warning 7 s · erro até ack | DXRpZTTMr9a |
| `--dur-reel-text` | 1,2 s por tela de texto (≤ 6 palavras) | DfxpIbfP-SB |
| `--dur-logo` | ~1,0 s | Dfzkwu3hSj5 |

Esses tokens têm prioridade sobre os de sistemas oficiais; a comparação com Material 3, Carbon e Atlassian (quase todos caem dentro das faixas oficiais; press e reveal divergem) está em `references/official-motion-guidelines.md` §7.

Curvas CSS equivalentes (complemento): ease-out `cubic-bezier(0.22, 1, 0.36, 1)`; ease-in-out para flips `cubic-bezier(0.65, 0, 0.35, 1)`; spring com overshoot leve `cubic-bezier(0.34, 1.56, 0.64, 1)` ou `linear()` gerado (ver `references/css-recipes.md`).

## Workflow
1. **Inventarie os momentos**: toque, mudança de estado, entrada/saída, espera, navegação, erro/sucesso.
2. **Para cada um, escolha o padrão** em `references/micro-interactions.md` (ou loaders/refresh/transições) e **copie os valores** — não invente durações.
3. **Defina tokens** (`:root` CSS vars ou objeto JS) e use-os em todo lugar.
4. **Implemente** com os snippets de `references/css-recipes.md`; para coreografia complexa use GSAP.
5. **Garanta interrupção** (transitions CSS ou springs que partem do valor atual) e **reduced-motion** (React + Motion: `<MotionConfig reducedMotion="user">`; `css-recipes.md` §13).
6. **Verifique no browser** a 1× e em câmera lenta (DevTools → Animations a 25%, como os reels mostram "¼ speed").

## Quando abrir cada reference
- `references/micro-interactions.md` — catálogo completo (~45 interações: botões, listas, ícones, formulários, toasts, drag/upload, detalhes iOS, tab bar líquida, foco em dashboard) com valores e porquê; §14–18 (rodada 10A): 19 regras de animação, os **42 nomes do "ABC of UI"** como checklist de inventário, linhas arrastáveis, texto animado e componentes "com física" (The Kitchen). Abra ao implementar qualquer componente específico.
- `references/loaders-and-refresh.md` — 8 loaders, 3 truques de percepção, 8 formas de atualizar página, regras de upload. Abra para estados de espera/feed.
- `references/page-transitions-and-timing.md` — durações, easing vs spring, shared element card→página, menus, side menu, large title. Abra para navegação ou dúvidas de "quanto tempo".
- `references/scroll-and-screen-transitions.md` — **diretriz do usuário**: scroll e transição de telas para dar vida aos componentes, *avaliando onde faz sentido*. Tem tabela onde sim/onde não, checklist de decisão, implementação (CSS `animation-timeline`, View Transitions, ScrollTrigger), a regra de **um momento animado por página** (§5) e os **5 padrões de motion de site** com o fluxo para pedir ao Claude (§6). Abra sempre que o pedido envolver scroll, reveal, parallax, header que encolhe, troca de tela ou "animar o site".
- `references/motion-for-social-video.md` — texto de reel, logo animado, título primeiro em vídeo de site, scroll-storytelling (RWB Porsche), carrossel educativo (capa com promessa numerada, 1 ideia por slide, CTA), reel de "fixes" e reel de demo com cursor e código. Abra para qualquer motion de marketing/redes sociais.
- `references/css-recipes.md` — snippets CSS/JS prontos (press, spring `linear()`, pull-to-refresh, stagger, rolling number, View Transitions, FLIP, toast stack, reduced-motion).
- `references/react-bits.md` — componentes React animados prontos (React Bits) mapeados para cada padrão desta skill, com comando de instalação, dependências e regras (ajustar valores, WebGL ≤ 1 por página); no fim, **outras bibliotecas** (Bencho, BoardUI, Transitions.dev, Beautiful UI, Skiper UI, Kokonut UI, Cult UI, Animata…), o teste **vazio/carregando/erro/texto longo** antes de adotar e curadorias de ícones e skills de motion. Abra quando o padrão já existir pronto ou o pedido for "qual biblioteca de componentes usar".
- `references/official-motion-guidelines.md` — **Apple HIG** (princípios; não publica ms/curvas; regras de Reduce Motion), **Material 3 Expressive** (springs desde maio/2025, tabela web cubic-bezier + duração, legado não mantido), **Carbon** (70–700 ms, productive/expressive), **Atlassian** (50–150/150–400 ms), **Motion for React** (React 18.2+, defaults, `reducedMotion` padrão `"never"`), GSAP/Lottie, e tabela **tokens da skill × oficiais** (onde batem e divergem, sem mudar os tokens). Abra quando pedirem "o que o Material/Carbon/Apple diz", para calibrar algo que a skill não cobre (saídas, hover) ou para justificar um valor.
- `references/visual-index.md` — qual imagem mostra o quê, e no fim a tabela **Perfis avaliados** (ativo?, nota, o que aproveitar).

## Imagens (`assets/visual-refs/*.jpg`)
Folhas de contato 4×3 dos reels, mais 6 prints únicos (`<ID>_<n>.jpg`: scroll-storytelling, carrossel, motion de site e bibliotecas). **Custam contexto: abra só quando precisar de exemplo visual** (ex.: ver o formato da curva de uma interação, o layout de um toast stack, o antes/depois de um detalhe iOS). Consulte `references/visual-index.md` para escolher **uma** imagem.

## Prioridade entre skills (quando as regras conflitam)

Ordem completa, da mais forte para a mais fraca: **skill de app específico** (ex.: `projetos/marca-pessoal-app/`, copiada para `.claude/skills/` na repo do app) > **skill de SEGMENTO** (`segmento-financeiro`, `segmento-crm`, `segmento-publicidade`, `segmento-marca-pessoal`, `segmento-saude`, `segmento-juridico`) > **plataforma** (`website-ui`, `desktop-app-ui`, `mobile-app-ui`) > **tema** (`design-direction`, `ui-motion`, `ux-patterns`, `dashboard-ui`) > **terceiros** (`ext-*`).
Se o projeto é de um setor, abra primeiro a skill `segmento-*` correspondente.

1. **Valores e decisões de design** (números, quantidade de animação, cor, sombra, tipografia) vêm das **skills do projeto** (app específico → segmento → plataforma → tema, nessa ordem): `website-ui`, `desktop-app-ui`, `mobile-app-ui`, `design-direction`, `ui-motion`, `ux-patterns`, `dashboard-ui`.
2. **Skills de terceiros** (`design-taste-frontend`, `impeccable`, `transitions-*`, `gsap-*`, `playwright-cli`, `extract-design`) servem para **implementação**: código pronto, APIs, checkers e verificação no browser. Use o código delas, mas com os valores do item 1.
3. Se o checker ou a regra de uma skill de terceiros reprovar algo que segue o item 1, **siga o item 1** e diga ao usuário qual regra externa foi ignorada e por quê.
4. Na plataforma, vale a skill da plataforma (`website-ui`, `desktop-app-ui` ou `mobile-app-ui`); nos temas, vale a skill de tema que ela indicar. A skill de segmento ou de app específico só sobrepõe o que ela disser explicitamente (paleta do setor, tom, compliance, telas obrigatórias); no resto valem plataforma e tema.

| Conflito | Vale | Em vez de |
|---|---|---|
| **Quantidade de animação** | **1 momento animado por página**: a entrada do hero **ou** um momento no CTA/seção, nunca os dois. Página longa também fica com 1. Micro-feedback funcional (press, hover, foco, sucesso) não conta | `design-taste-frontend`: entrada do hero + 1 momento por página (2 em página longa) |
| **Durações** | Os tokens de `ui-motion`: press **160 ms** (feedback em 0 ms), stagger **70–100 ms**, expandir card/abrir painel **350 ms**, sucesso **470 ms**, reveal **≤ 700 ms**. Onde `ui-motion` não tem número, use o token de `transitions-dev` (micro 80 ms, quick 150 ms, fast 250 ms) | `transitions-dev`: stagger 40 ms, panel open 400 ms, success check 500 ms |

## Skills complementares
- `ext-transitions-dev` / `ext-transitions-polish` — CSS transitions prontas e polish (é a base da biblioteca Transitions.dev citada em `react-bits.md`).
- `ext-gsap-core`, `ext-gsap-scrolltrigger`, `ext-gsap-react` — timelines, scroll-linked (large title encolhendo, reveals), React. Licença do GSAP: gratuita, mas própria ("Standard No Charge", **não MIT**); confira antes de usar em produto construtor de sites/no-code.
- `design-direction` — personalidade de marca, paleta e logo estático antes de animar o logo.
- `ux-patterns` — alvos de toque e escala tipográfica (os componentes que você anima precisam ter ≥ 44px de toque).
- `ext-playwright-cli` — abrir no browser, gravar/capturar e checar estados e `prefers-reduced-motion` (emulação).

## Skills externas (dependências)
Esta skill pode delegar para: `ext-transitions-dev`, `ext-transitions-polish`, `ext-gsap-core`, `ext-gsap-scrolltrigger`, `ext-gsap-react`, `ext-playwright-cli`. Elas **não** fazem parte da repo; são instaladas por `scripts/install-external-skills.sh`.
1. Antes de delegar, confira se a pasta existe em `.claude/skills/<nome>/` ou `~/.claude/skills/<nome>/`.
2. Se faltar, **pergunte ao usuário** antes de instalar e, com o ok, rode `./scripts/install-external-skills.sh` (ou `--global`). Depois da instalação, o Claude Code normalmente já enxerga as skills novas; se alguma não aparecer, leia o `SKILL.md` instalado com Read e siga as instruções dele.
3. Se o usuário não quiser instalar, siga sem elas usando as references desta skill.

