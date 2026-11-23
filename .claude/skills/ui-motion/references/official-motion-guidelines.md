# Diretrizes oficiais de motion: Apple HIG, Material 3, Carbon, Atlassian e Motion for React

Fontes: rodadas **9A** (Apple HIG, Material 3, Carbon; lidas em 22/11/2026) e **9D** (Material 3, Carbon, Atlassian, Motion for React, LottieFiles, GSAP; 22–23/11/2026), páginas oficiais abertas no navegador. Inferências nossas estão marcadas **(complemento)**.

> **Prioridade:** os **tokens de `SKILL.md` continuam valendo** (ver "Prioridade entre skills"). Esta reference serve para justificar, calibrar o que a skill não cobre e explicar divergências. Ela **não** substitui nenhum token.

---

## 1. Apple HIG: princípios, sem números

Página Motion (`developer.apple.com/design/human-interface-guidelines/motion`):
- **Propósito.** Não adicione motion "por adicionar"; motion excessivo distrai e pode causar desconforto.
- **Opcional.** Motion nunca é o único canal de algo importante. Some háptico e áudio (no web: texto, ícone e cor).
- **Breve e preciso.** Feedback curto. Evite motion em interações muito frequentes.
- **Cancelável.** A pessoa não espera a animação acabar para agir (bate com a regra 4 da skill, interrupção).
- **Realista e ligado ao gesto.** Se a view entrou deslizando de cima, não sai para o lado (bate com a regra 11: "nada aparece do nada").
- Liquid Glass reage com mais ênfase ao toque direto do que ao trackpad (só nativo).

**A Apple NÃO publica durações em ms, curvas de easing nem parâmetros de spring** (nem na página Motion, nem em Accessibility). Os números iOS da skill (damping ~0.8, overshoot ~1.5%, rubber band 200→86 px, momentum ~1000 px) vêm de reels que medem o iOS (`De4B0UxPXIk`), **não** da HIG. Não cite "a Apple recomenda X ms".

### 1.1 Reduce Motion (página Accessibility da HIG)
Com Reduce Motion ativo, a Apple pede:
1. Reduzir animações automáticas e repetitivas (zoom, scale, movimento periférico).
2. **Apertar os springs** (mais rígidos, mais amortecidos) para **reduzir o bounce**.
3. **Seguir o gesto direto**: a animação acompanha o dedo, sem continuar sozinha.
4. **Evitar animar profundidade** (camadas no eixo z: zoom de fundo, cartas empilhadas que afundam).
5. **Trocar transições em x/y/z por fade.**
6. **Evitar entrar ou sair de blur** (blur animado).

Também da Accessibility (úteis para motion): evitar elementos com tempo limite que se auto-dispensam, evitar autoplay sem controle, oferecer alternativa a todo gesto (swipe para dispensar + botão).

Equivalente web **(complemento)**: `@media (prefers-reduced-motion: reduce)` em CSS, `useReducedMotion()` / `<MotionConfig reducedMotion="user">` no Motion for React (§5), `gsap.matchMedia()` no GSAP. Snippets em `css-recipes.md` §0 e §13.

---

## 2. Material 3: springs desde o M3 Expressive (maio/2025)

- O **M3 Expressive (maio/2025)** trocou o sistema de easing + duração por **física de springs** (stiffness + damping + velocidade inicial). O sistema antigo "ainda serve para transições", mas **"não é mais mantido"**.
- Dois esquemas, escolhidos **no nível do produto**: **expressive** (overshoot/bounce, momentos de destaque) e **standard** (bounce mínimo, produtos utilitários).
- Tokens `md.sys.motion.spring.{fast|default|slow}.{spatial|effects}`.
  - **Spatial** (posição, rotação, tamanho, cantos) pode ultrapassar o valor final. **Effects** (cor, opacidade) **sem overshoot**.
  - **fast** = componentes pequenos (switch, botão); **default** = parte da tela (bottom sheet); **slow** = tela inteira.
- Valores numéricos de stiffness/damping: **não especificado** no texto (ficam num módulo recolhido).
- Recomendação oficial: **spring quando há gesto ou interrupção**; curva + duração só em animação sem interrupção.

### 2.1 Tabela oficial: springs convertidas para web (cubic-bezier + duração)

| Token | Curva | Duração |
|---|---|---|
| Expressive fast spatial | `cubic-bezier(0.42, 1.67, 0.21, 0.90)` | 350 ms |
| Expressive default spatial | `cubic-bezier(0.38, 1.21, 0.22, 1.00)` | 500 ms |
| Expressive slow spatial | `cubic-bezier(0.39, 1.29, 0.35, 0.98)` | 650 ms |
| Expressive/Standard fast effects | `cubic-bezier(0.31, 0.94, 0.34, 1.00)` | 150 ms |
| Expressive/Standard default effects | `cubic-bezier(0.34, 0.80, 0.34, 1.00)` | 200 ms |
| Expressive/Standard slow effects | `cubic-bezier(0.34, 0.88, 0.34, 1.00)` | 300 ms |
| Standard fast / default / slow spatial | `cubic-bezier(0.27, 1.06, 0.18, 1.00)` | 350 / 500 / 750 ms |

y > 1 na curva = overshoot em CSS. Standard spatial (y 1,06) ≈ overshoot leve; expressive fast (y 1,67) = bounce visível.

### 2.2 Sistema legado (não mantido; útil para comparar)
- Easing: standard `cubic-bezier(0.2, 0, 0, 1)`; standard decelerate `(0, 0, 0, 1)`; standard accelerate `(0.3, 0, 1, 1)`; emphasized decelerate `(0.05, 0.7, 0.1, 1)`; emphasized accelerate `(0.3, 0, 0.8, 0.15)`; "emphasized" puro sem equivalente CSS (use standard).
- Duração (16 tokens): short1–4 **50/100/150/200** · medium1–4 **250/300/350/400** · long1–4 **450/500/550/600** · extra-long1–4 **700/800/900/1000 ms**.
- Exemplos oficiais: seleção 200 ms standard; FAB → sheet 400 ms emphasized; card → tela cheia 500 ms emphasized; carrossel ambiente 1000 ms.
- Reduced motion: **não especificado** nas páginas lidas.

---

## 3. Carbon (IBM): o sistema mais completo em tokens

- **Productive** (tarefas, sutil, eficiente) × **expressive** (momentos importantes e ocasionais: nova página, ação primária, alerta). Reserve expressive para o raro.
- **Easing:**

| Uso | Productive | Expressive |
|---|---|---|
| Standard (visível do início ao fim) | `cubic-bezier(0.2, 0, 0.38, 0.9)` | `cubic-bezier(0.4, 0.14, 0.3, 1)` |
| Entrance (aparece) | `cubic-bezier(0, 0, 0.38, 0.9)` | `cubic-bezier(0, 0, 0.3, 1)` |
| Exit (sai de vez) | `cubic-bezier(0.2, 0, 1, 0.9)` | `cubic-bezier(0.4, 0.14, 1, 1)` |

  Elemento que sai mas fica "por perto" (painel lateral recolhido) usa **standard**, não exit.
- **Durações:** `fast-01` **70 ms** (botão, toggle) · `fast-02` **110 ms** (fade) · `moderate-01` **150 ms** (pequenas expansões) · `moderate-02` **240 ms** (expansão, toast) · `slow-01` **400 ms** (grandes expansões, notificação importante) · `slow-02` **700 ms** (escurecer o fundo).
- **Regras de uso:** duração cresce com distância/tamanho (Motion Generator; "dynamic duration" em breve); feedback imediato; **microinteração com ease-out e 90–120 ms**; em tela pequena movimento sutil passa despercebido; **se o usuário nota o motion com frequência, considere remover**; sempre ter alternativa reduzida/estática que comunique o mesmo.
- Visual das duas curvas (distância × tempo): `assets/visual-refs/9A_carbon-easing-curves_1.jpg`.

---

## 4. Atlassian Design System (rodada 9D)

- Cada evento = duração + easing + propriedade, empacotados em token (ex.: `motion.popup.enter`).
- **Regra de frequência:** o que dispara dezenas de vezes por dia fica **abaixo de 150 ms**; o que aparece uma vez por sessão pode ser mais expressivo.
- **Durações:** interações **50–150 ms** (hover de item de lista 50 ms); transições **150–400 ms** (dropdown 150 ms, modal 250 ms).
- **4 curvas:** ease-out bold `cubic-bezier(0, 0.4, 0, 1)` (Panel/Flag entrando) · ease-in-out bold `cubic-bezier(0.4, 0, 0, 1)` (escalar modal) · ease-in practical `cubic-bezier(0.6, 0, 0.8, 0.6)` (saídas) · ease-out practical `cubic-bezier(0.4, 1, 0.6, 1)` (popup e fade de hover).
- Reduced motion: com a preferência ativa, motion **desligado e instantâneo**.

Outros sistemas lidos na 9D: Fluent 2 (princípios e modo "sem motion", sem números), Ant Design (tokens existem, valores padrão não especificados), Polaris e Primer (página de motion não existe mais). Pouco a aproveitar.

---

## 5. Motion for React (biblioteca; rodada 9D)

- **Exige React 18.2+.** Import `motion/react` (em Framer: `framer-motion`). MIT; Motion+ é pago.
- **Defaults:** propriedades físicas (`x`, `scale`) usam **spring**; visuais (`opacity`) usam **tween**. Tween padrão **0,3 s** (0,8 s com vários keyframes). Spring por duração: `bounce` padrão **0,25** (0 = criticamente amortecido). Spring físico: `damping` padrão 10, `mass` 1 (a doc lista `stiffness` padrão "1", provável erro: confira no código). `visualDuration` incorpora a velocidade de um gesto interrompido.
- **`MotionConfig reducedMotion` tem padrão `"never"`**: o Reduce Motion do sistema é **ignorado** até você configurar. **Regra obrigatória desta skill:** envolver a raiz do app em `<MotionConfig reducedMotion="user">` (snippet em `css-recipes.md` §13). Com isso ativo, o Motion desliga transform e layout e mantém opacity e backgroundColor (exatamente o "troque x/y/z por fade" da Apple).
- `useReducedMotion()` para casos que precisam de lógica própria (trocar transform de elementos grandes por opacity, desligar autoplay e parallax).
- Performance: 16,7 ms por frame a 60 fps, 8 ms a 120 fps; anime `transform` e `opacity`; `filter: drop-shadow` em vez de `boxShadow`; `clipPath: inset(0 round Npx)` em vez de `borderRadius`; variável CSS animada não tem aceleração de hardware.
- Não tem dropzone (use drag-and-drop nativo). Imagens arrastáveis: `draggable={false}`.
- **Os defaults do Motion não são os tokens da skill**: passe `transition` explícito (ou `MotionConfig transition`) com os valores de `SKILL.md` **(complemento)**.
- Exemplos oficiais (swipe actions, sheet modal, card stack): `assets/visual-refs/9D_motion-examples-swipe_1.jpg`.

## 6. GSAP e Lottie (licença e easing)

- **GSAP**: gratuito, mas sob **licença própria "Standard No Charge"**, **não MIT**; proíbe uso em ferramentas no-code que concorram com o Webflow. Confira antes de usar em produto que seja um construtor de sites. Vale para as skills `ext-gsap-*`.
- **Lottie** (lottie-web, dotLottie): players MIT. Easing no Lottie Creator usa notação `cubic-bezier`: exemplos da doc: ease-in-out `(0.42, 0, 0.58, 1)`, linear `(0, 0, 1, 1)`, back in-out `(0.68, -0.55, 0.265, 1.55)`. **(complemento)**: ao encomendar Lottie, peça as curvas dos tokens da skill (ease-out `0.22, 1, 0.36, 1`), não o ease-in-out genérico. O **LottieFiles Motion System** (biblioteca governada de curvas, durações e presets) é **pago** (Team+/Enterprise) e a ponte para código está em "roadmap": só vale com muita ilustração animada. Para motion de UI use Lottie só em ilustração (onboarding, estado vazio, celebração), nunca em microinteração.

---

## 7. Tokens da skill × sistemas oficiais (os tokens da skill NÃO mudam)

| Token da skill | Valor | Material 3 | Carbon | Atlassian | Leitura |
|---|---|---|---|---|---|
| `--dur-press` | 160 ms (feedback em 0 ms) | fast effects 150 ms | fast-01 **70 ms**; micro **90–120 ms** | interação 50–150 ms; frequente **< 150 ms** | **Diverge**: a skill é mais longa. Os 160 ms incluem o retorno com spring; o início é 0 ms no touchdown, o que cumpre o "feedback imediato" de todos. Mantenha 160 ms (prioridade). **(complemento)** hover/feedback de cor sem spring pode usar 70–120 ms (`transitions-dev` micro 80 / quick 150) |
| `--dur-reorder` | 200 ms | short4 / default effects 200 ms | moderate-02 240 ms | transição 150–400 ms | **Bate** |
| `--dur-morph-icon` | 300–400 ms | medium2–4 300–400 ms | slow-01 400 ms | 150–400 ms | **Bate** (no teto do Atlassian) |
| `--dur-expand` | 350 ms ease-out | fast spatial 350 ms; legado medium3 350 | moderate-02 240 (expansão) / slow-01 400 (grande) | 150–400 ms | **Bate** (entre pequena e grande expansão) |
| `--dur-success` | 470 ms | long1 450 / default spatial 500 | slow-01 400 | acima de 400 | **Bate** com M3; acima de Carbon/Atlassian, aceitável por ser evento raro (regra de frequência) |
| `--dur-reveal` | ~700 ms (< 1 s) | extra-long1 700 | slow-02 700 (só escurecer fundo) | teto 400 | **Diverge em app**: 700 ms é motion de **site** (1 momento por página). **(complemento)** em painel/app de uso diário, prefira ≤ 400 ms |
| `--dur-scene` | ~1,2 s | teto 1000 (carrossel ambiente) | — | — | **Fora dos sistemas**: só marketing/vídeo |
| `--stagger` 70 / 100 ms | — | não especificado | não especificado | não especificado | **Só a skill tem** |
| ease-out `cubic-bezier(0.22, 1, 0.36, 1)` | entradas | emphasized decelerate `(0.05, 0.7, 0.1, 1)` | entrance `(0, 0, 0.38, 0.9)` / `(0, 0, 0.3, 1)` | ease-out bold `(0, 0.4, 0, 1)` | **Mesma família** (desacelera); a da skill é mais "rápida no começo" |
| ease-in-out `cubic-bezier(0.65, 0, 0.35, 1)` | flips | standard `(0.2, 0, 0, 1)` | standard expressive `(0.4, 0.14, 0.3, 1)` | ease-in-out bold `(0.4, 0, 0, 1)` | **Família próxima**; a skill é simétrica, os sistemas terminam mais suave |
| spring overshoot `cubic-bezier(0.34, 1.56, 0.64, 1)` | press, pop | expressive fast spatial `(0.42, 1.67, 0.21, 0.90)` 350 ms | sem spring | sem spring | **Bate** com M3 expressive fast |
| spring "UI" damping 0.8 (~1,5% overshoot) | geral | standard spatial (bounce mínimo, y 1,06) | — | — | **Bate** com M3 standard; Motion default `bounce` 0,25 é mais elástico: configure |
| spring toast 180/20 | pilhas | — | toast 240 ms (tween) | — | **Diverge em forma** (spring × tween); duração equivalente |
| reduced motion: fade ≤ 150 ms ou corte | — | fast effects 150 | fast-02 fade 110 | desliga (instantâneo) | **Bate** |
| Saída | (skill sem token próprio) | accelerate `(0.3, 0, 1, 1)` | exit `(0.2, 0, 1, 0.9)` | ease-in practical `(0.6, 0, 0.8, 0.6)` | **(complemento)**: saídas mais curtas que entradas e com ease-in |

Resumo: onde a skill tem número, ele cai **dentro** das faixas oficiais, exceto o press (mais longo que Carbon/Atlassian, por causa do spring) e o reveal/cena (motion de site/vídeo, fora do escopo dos sistemas de produto). Onde a skill não tem número (saída, hover, fade simples), use o token de `transitions-dev` (micro 80 ms, quick 150 ms, fast 250 ms), como manda a tabela "Prioridade entre skills" do `SKILL.md`; Carbon e Atlassian servem de checagem.

## 8. Checklist (complemento)
- [ ] App React com Motion: `<MotionConfig reducedMotion="user">` na raiz.
- [ ] Reduce Motion: springs mais firmes, gesto 1:1 sem inércia, sem z/profundidade, x/y/z → fade, sem blur animado, sem autoplay.
- [ ] Interação repetida dezenas de vezes por dia < 150 ms de percepção (feedback em 0 ms).
- [ ] Spring onde há gesto/interrupção; curva + duração só onde não há.
- [ ] Spatial pode ter overshoot; cor/opacidade nunca.
- [ ] Expressive só em momento raro (casa com "1 momento animado por página").
- [ ] Se a pessoa nota o motion toda hora, remova.
