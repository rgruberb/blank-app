---
name: ui-motion
description: Projeta e implementa micro-interações e motion de UI com valores concretos de reels de motion design: press de botão (95%), pull-to-refresh com resistência (35%), números rolando, ícones que morfam, toasts, drag-and-drop/upload, 8 loaders, 8 formas de atualizar, transição card→página, durações, easing e springs, detalhes que fazem apps premium parecerem caros, e motion para redes: texto de reel (≤6 palavras, 1,2 s), logo animado (~1 s) e título primeiro. Use quando o pedido falar em "animar", "micro-interação", "app mais fluido/premium", "feedback ao tocar", "spring", "easing", "quanto tempo deve durar a animação", "loader/skeleton", "pull to refresh", "toast", "drag and drop", "transição de página", "animação no scroll", "scroll reveal", "parallax", "dar vida aos componentes", "componente animado pronto", "ícone animado", "polish de motion", "React Bits", "vídeo de produto", "reel", "texto no vídeo", "animar logo" ou "por que o iPhone parece tão suave".
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
10. **Morph, não swap.** Ícones e botões mudam de forma (play→pause 300 ms; botão 260→64 px virando spinner em 270 ms; Dynamic Island cresce da pílula). Nada "pisca" para outro desenho.
11. **Nada aparece do nada.** Card vira a página e volta exatamente para onde estava; menus nascem do botão que os abriu.
12. **Percepção > velocidade real.** Skeleton em vez de tela vazia, UI otimista (mostre sucesso já), barra de progresso que começa rápida e desacelera.
13. **Respeite `prefers-reduced-motion`.** Troque deslocamentos/escala/bounce por fade curto (≤150 ms) ou corte; mantenha o feedback de estado (cor, ícone, texto). (complemento)
14. **Título primeiro.** Nunca deixe a tela em branco: "2 s em branco parecem uma hora". O título aparece no primeiro paint e o resto entra em cascata (theglidestudio, Dfy7ig_B-FL).
15. **Texto de reel: ≤ 6 palavras, grande, 1,2 s na tela**; se não dá para ler duas vezes, está rápido. **Logo: ~1 s**, e o tipo de movimento é a personalidade (linha lenta = calmo, encaixe rápido = rápido, crescer de um ponto = amigável) (theglidestudio, DfxpIbfP-SB, Dfzkwu3hSj5).
16. Anime só `transform` e `opacity` sempre que possível; evite animar `width/height/top` em listas grandes. (complemento)

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

Curvas CSS equivalentes (complemento): ease-out `cubic-bezier(0.22, 1, 0.36, 1)`; ease-in-out para flips `cubic-bezier(0.65, 0, 0.35, 1)`; spring com overshoot leve `cubic-bezier(0.34, 1.56, 0.64, 1)` ou `linear()` gerado (ver `references/css-recipes.md`).

## Workflow
1. **Inventarie os momentos**: toque, mudança de estado, entrada/saída, espera, navegação, erro/sucesso.
2. **Para cada um, escolha o padrão** em `references/micro-interactions.md` (ou loaders/refresh/transições) e **copie os valores** — não invente durações.
3. **Defina tokens** (`:root` CSS vars ou objeto JS) e use-os em todo lugar.
4. **Implemente** com os snippets de `references/css-recipes.md`; para coreografia complexa use GSAP.
5. **Garanta interrupção** (transitions CSS ou springs que partem do valor atual) e **reduced-motion**.
6. **Verifique no browser** a 1× e em câmera lenta (DevTools → Animations a 25%, como os reels mostram "¼ speed").

## Quando abrir cada reference
- `references/micro-interactions.md` — catálogo completo (~45 interações: botões, listas, ícones, formulários, toasts, drag/upload, detalhes iOS, tab bar líquida, foco em dashboard) com valores e porquê. Abra ao implementar qualquer componente específico.
- `references/loaders-and-refresh.md` — 8 loaders, 3 truques de percepção, 8 formas de atualizar página, regras de upload. Abra para estados de espera/feed.
- `references/page-transitions-and-timing.md` — durações, easing vs spring, shared element card→página, menus, side menu, large title. Abra para navegação ou dúvidas de "quanto tempo".
- `references/scroll-and-screen-transitions.md` — **diretriz do usuário**: scroll e transição de telas para dar vida aos componentes, *avaliando onde faz sentido*. Tem tabela onde sim/onde não, checklist de decisão e implementação (CSS `animation-timeline`, View Transitions, ScrollTrigger). Abra sempre que o pedido envolver scroll, reveal, parallax, header que encolhe ou troca de tela.
- `references/motion-for-social-video.md` — texto de reel, logo animado, título primeiro em vídeo de site, scroll-storytelling (RWB Porsche), template de carrossel educativo, formato de reel de "fixes". Abra para qualquer motion de marketing/redes sociais.
- `references/css-recipes.md` — snippets CSS/JS prontos (press, spring `linear()`, pull-to-refresh, stagger, rolling number, View Transitions, FLIP, toast stack, reduced-motion).
- `references/react-bits.md` — componentes React animados prontos (React Bits) mapeados para cada padrão desta skill, com comando de instalação, dependências e regras (ajustar valores, WebGL ≤ 1 por página). Abra quando o projeto for React/Next.js e o padrão já existir pronto.
- `references/visual-index.md` — qual imagem mostra o quê, e no fim a tabela **Perfis avaliados** (ativo?, nota, o que aproveitar).

## Imagens (`assets/visual-refs/*.jpg`)
Folhas de contato 4×3 dos reels, mais 3 prints únicos (`<ID>_<n>.jpg`: scroll-storytelling e carrossel). **Custam contexto: abra só quando precisar de exemplo visual** (ex.: ver o formato da curva de uma interação, o layout de um toast stack, o antes/depois de um detalhe iOS). Consulte `references/visual-index.md` para escolher **uma** imagem.

## Skills complementares
- `ext-transitions-dev` / `ext-transitions-polish` — CSS transitions prontas e polish.
- `ext-gsap-core`, `ext-gsap-scrolltrigger`, `ext-gsap-react` — timelines, scroll-linked (large title encolhendo, reveals), React.
- `design-direction` — personalidade de marca, paleta e logo estático antes de animar o logo.
- `ux-patterns` — alvos de toque e escala tipográfica (os componentes que você anima precisam ter ≥ 44px de toque).
- `ext-playwright-cli` — abrir no browser, gravar/capturar e checar estados e `prefers-reduced-motion` (emulação).

## Skills externas (dependências)
Esta skill pode delegar para: `ext-transitions-dev`, `ext-transitions-polish`, `ext-gsap-core`, `ext-gsap-scrolltrigger`, `ext-gsap-react`, `ext-playwright-cli`. Elas **não** fazem parte da repo; são instaladas por `scripts/install-external-skills.sh`.
1. Antes de delegar, confira se a pasta existe em `.claude/skills/<nome>/` ou `~/.claude/skills/<nome>/`.
2. Se faltar, **pergunte ao usuário** antes de instalar e, com o ok, rode `./scripts/install-external-skills.sh` (ou `--global`). Depois da instalação, o Claude Code normalmente já enxerga as skills novas; se alguma não aparecer, leia o `SKILL.md` instalado com Read e siga as instruções dele.
3. Se o usuário não quiser instalar, siga sem elas usando as references desta skill.

