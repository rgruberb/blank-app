# React Bits e outras bibliotecas de componentes animados

> Outras bibliotecas (Bencho, BoardUI, Transitions.dev, Beautiful UI, Skiper UI, Animata…), o teste vazio/carregando/erro/texto longo e curadorias de ícones e skills de motion estão no fim do arquivo.

[React Bits](https://reactbits.dev) ([repo](https://github.com/DavidHDev/react-bits)) é uma biblioteca com cerca de 210 componentes React animados, divididos em 5 categorias: TextAnimations, Animations, Backgrounds, Components e Micro. **Não é uma skill.** Você instala componente por componente, e o código-fonte fica dentro do seu projeto, onde dá para editar.

Use quando o projeto for **React/Next.js** e o padrão de motion já existir pronto. Antes de instalar, ajuste o componente aos valores desta skill (durações, springs, `prefers-reduced-motion`).

Licença: MIT + Commons Clause. Pode usar em projetos, inclusive comerciais. Não pode revender a biblioteca em si.

## Instalação

Cada componente tem 4 variantes, escolhidas pelo sufixo: `JS` ou `TS`, combinado com `CSS` (CSS puro) ou `TW` (Tailwind).

```bash
# shadcn CLI (registry @react-bits)
npx shadcn@latest add @react-bits/SplitText-TS-TW

# ou jsrepo
npx jsrepo@latest add https://reactbits.dev/r/SplitText-TS-TW
```

Para o Claude Code achar e instalar componentes sozinho, registre o registry no `components.json` e conecte o MCP do shadcn:

```json
{ "registries": { "@react-bits": "https://reactbits.dev/r/{name}.json" } }
```

```bash
npx shadcn@latest mcp init --client claude
```

**Dependências:** alguns componentes puxam `gsap` + `@gsap/react` ou `motion` (Framer Motion), e alguns trazem ícones do `@hugeicons`. Os Backgrounds e os componentes de vidro usam **WebGL puro**, sem lib, mas pesam na GPU (ver regras abaixo). A CLI instala as dependências declaradas; confira o `package.json` depois.

## Quais usar, por necessidade desta skill

Na tabela, os nomes estão como aparecem no registry. Quando a dependência foi conferida no código, ela aparece entre parênteses.

| Necessidade (ver `micro-interactions.md` / `SKILL.md`) | Componentes React Bits | Observações |
|---|---|---|
| **Press/squish, toggle, checkbox** | `SquishSwitch` (motion), `SpringCheck` (motion), `HoldButton`, `RubberSegment` (motion), `JellyRadio` | Ajuste a escala do press para 0,95 e use spring sem overshoot exagerado |
| **Toasts e linhas com swipe** | `SwipeToast` (motion), `SwipeRow` (motion) | Siga as 5 regras de toast desta skill (empilhar, pausar no hover, origem fixa) |
| **Números que mudam** | `CountUp` (motion), `Counter`, `CodeSlots` | Use para KPIs e totais; a contagem roda uma vez, quando o elemento entra na tela |
| **Estado de IA, loaders e espera** | `ThoughtLine` (motion), `LatticeLoader`, `PromptBar` (motion), `ShinyText` | Spinner só para esperas < 3 s; acima disso use skeleton ou progresso (`loaders-and-refresh.md`) |
| **Status e feedback** | `StatusMark` (motion), `PulseHeart`, `BellToggle`, `WarmTooltip` (motion) | Sucesso em ~470 ms (círculo→tick) |
| **Seleção e menus** | `GlideSelect`, `PillNav`, `StaggeredMenu` (gsap), `CardNav`, `Dock`, `FlowingMenu` | Menus nascem do botão que os abre, com stagger de 70–100 ms |
| **Títulos e texto** | `SplitText` (gsap), `BlurText` (motion), `RotatingText` (motion), `TextType` (gsap), `DecryptedText` (motion), `GradientText`, `ShinyText` | Reveal ≤ 700 ms, uma vez; em app de uso diário, prefira não animar texto |
| **Reveal no scroll** | `AnimatedContent` (gsap), `FadeContent` (gsap), `ScrollReveal` (gsap), `ScrollFloat` (gsap), `ScrollStack`, `ScrollExpand` | Antes, passe pelo checklist de `scroll-and-screen-transitions.md` |
| **Cards e grids** | `SpotlightCard`, `TiltedCard`, `MagicBento`, `BorderGlow`, `AnimatedList` | Hover sutil; tilt e glow só em landing ou vitrine, nunca em tabelas de trabalho |
| **Vidro (glassmorphism)** | `GlassSurface`, `FluidGlass`, `GlassIcons` | WebGL; precisa de fundo rico por trás (ver `dashboard-ui/references/glassmorphism.md`) |
| **Fundos de hero** | `Aurora`, `SoftAurora`, `Silk`, `Grainient`, `DarkVeil`, `LightRays`, `DotGrid`, `Particles`, `Iridescence` | WebGL; **no máximo 1 por página**, só em hero ou landing |
| **Cursor e efeitos de clique** | `ClickSpark`, `Magnet`, `GlareHover`, `StarBorder`, `GradualBlur` | Decorativo; use com parcimônia e desligue em touch |

Lista completa por categoria: os nomes ficam nas pastas `src/content/<Categoria>/` do repo, e as demos em reactbits.dev.

## Regras ao usar React Bits

1. **Cada componente cumpre uma função.** Escolha pelo que o motion comunica (feedback, origem, progresso, mudança de valor), não pelo efeito. Se o componente for só "bonito", corte.
2. **Ajuste os valores aos desta skill.** Os defaults da biblioteca costumam ser mais longos e chamativos. Troque `duration`/`delay`/`stiffness`/`damping` pelos tokens da tabela do `SKILL.md`.
3. **Use `prefers-reduced-motion` sempre.** Nem todo componente trata isso. Envolva o componente ou passe props estáticas quando `matchMedia('(prefers-reduced-motion: reduce)')` for verdadeiro.
4. **WebGL tem orçamento.** Os componentes Backgrounds, Glass e os 3D usam canvas WebGL. Regras:
   - no máximo 1 canvas por página;
   - pausar quando sair da tela;
   - fallback estático (gradiente CSS) em mobile fraco;
   - medir o FPS com `ext-playwright-cli` ou com o DevTools.
5. **Não misture libs de animação à toa.** Se o projeto já usa `motion`, prefira componentes em `motion`; se usa GSAP, use os que dependem de `gsap` e siga `ext-gsap-react`.
6. **Prefira o componente da React Bits a escrever do zero** quando ele já faz o padrão. Escreva o seu (`css-recipes.md`) quando o projeto não for React ou quando precisar de controle fino dos valores.

## Outras bibliotecas de componentes e curadorias (rodadas 1 e 5)
Nomes e URLs vieram de posts de terceiros e **não foram instalados nem auditados** (licença, dependências, manutenção). Confira antes de adotar.

**Por que usar uma biblioteca** (`DfkBGDyDgqS`, @griffinwooldridge1): "pare de fazer a IA desenhar cada UI do zero; dê a ela bons componentes". O resultado fica consistente e polido. Escolha pelo tipo de produto:

| Biblioteca | Para quê (segundo o post) | O que os slides mostram |
|---|---|---|
| Bencho (bencho.dev) | Micro-interações lúdicas | Timer circular 25:00 com ticks e +5/play/reset, card 72 BPM, seletor "Playback speed" 0.5×–2× em pílulas |
| BoardUI (boardui.com) | Dashboards densos e ferramentas de agente | Donut de anéis, input de agente com abas, barras "Earned so far" com Weekly/Monthly/Yearly, seletor de intervalo com presets |
| Transitions.dev (transitions.dev) | Transições suaves entre estados | Chat estilo iMessage, "Token spend", timer "Focus time", agenda "Thursday". **É a mesma base das skills `ext-transitions-dev` / `ext-transitions-polish`**: use-as primeiro |
| Beautiful UI (beautifului.dev) | Chat de agente, aprovações e workflows | Insights com variação colorida, tabela com tags, painel "Proposed menu cleanup" com diff vermelho/verde e "Apply 3 changes" |

**Teste antes de adotar** (de um comentário no post, a regra mais útil): a biblioteca cobre os estados **vazio, carregando, erro e texto longo**? É aí que UI feita por IA quebra. **(complemento)** Monte uma página de teste com os 4 estados de cada componente escolhido (string de 80+ caracteres, lista vazia, skeleton, erro com retry) e confira também `prefers-reduced-motion`, foco por Tab e alvos ≥ 44 px (`ux-patterns`).

**Curadorias de UI animada** (@noahelhadedy, rodada 5; todas React, copiar e colar):
- `De_J0aOl9SJ`, 7 bibliotecas: **Skiper UI** (componentes incomuns para shadcn), **Kokonut UI** (cards e widgets polidos), **Cult UI** (blocos shadcn "com um twist", MIT), **SmoothUI** (micro-interações), **Animata** (150+ animações, MIT), **Eldora UI** (efeitos de landing), **Hover.dev** (botões e seções chamativos). Prints: `De_J0aOl9SJ_1.jpg` (Skiper UI: hero "UN-COMMON COMPONENTS" sobre fumaça WebGL azul-ciano, comando de instalação + "Get Started"), `_2` (Kokonut UI "Animated React components": AI Input Selector, Dynamic Dial 21.0°, AI State Loading, toast "Delete workspace" com desfazer, Shape Background, "Good vibrations"), `_3` (Animata: "Ship faster. Look better.", bento com 152 componentes, selo "MIT Licensed + free forever"). Cada slide usa a mesma moldura: rótulo "UI Libraries" no topo, gravação de tela no meio, URL embaixo.
- `Dfo__tSjk9k`, 7 componentes de motion grátis (designbookmark.com/motion): pull cord, goo menu, jelly slider, swipe deck, glass lens, parallax ticket e **hold to publish** (segurar para confirmar evita clique acidental em ação irreversível). A legenda diz que cada um vem com o código **e um botão de copiar direto para Claude ou Codex**. Prints: `Dfo__tSjk9k_1.jpg` (pull cord: luminária em palco claro, cordão com puxador), `_2` (swipe deck: card "Kalypso · Portfolio kit · 12 pages · $49" com chips Figma/Framer em pilha), `_3` (parallax ticket "Motion Night · Oct 30 · 20:00 · Lisbon · No. 0042" inclinado em 3D).
- `Df1eAHODjT9`, 8 sets de ícones: Neat Icons (do próprio autor: 1.162 ícones em 4 estilos numa grade só, 201 grátis), Doo Icons, Majesticons (line/solid/duotone numa grade 24×24, com seletor de estilo, traço e cor), Gravity UI, Pictogrammers (Material Design Icons), Humbleicons (284 ícones neutros, por categoria), Bootstrap Icons, Vectopus. Critérios do post: **mesma grade (24×24)**, estilos disponíveis, licença, arquivo Figma e volume. Prints em `design-direction/assets/visual-refs/Df1eAHODjT9_1–_3.jpg`. Para ícone animado, morph de `micro-interactions.md` §7.

**Skills de motion para agentes** (`DfKaOBqjUr4`, @craftwork.design, "Design skills Part 2", "Ten more skills… motion, 3D and the final polish"): Craftwork (fontes, ícones e referências reais em vez de defaults; antes/depois de landing), Design Engineering de Emil Kowalski (easing, durações, springs, auditoria de animações), GSAP ScrollTrigger ("official guide to pinning, scrub and cleanup"; já coberto por `ext-gsap-scrolltrigger`), Motion Design da LottieFiles (tabelas de duração e easing), Shader Dev (36 técnicas do ShaderToy, de SDFs a fluidos), Three.js Scroll Worlds (um mundo 3D guiado pelo scroll nativo), **Diagram Design** (44 tipos de diagrama editorial em HTML e SVG; faltava nesta lista), Frontend Slides, Refactoring UI e Web Interface Guidelines da Vercel. Comandos e repositórios não verificados. Print do slide GSAP (`DfKaOBqjUr4_3.jpg`): título + 1 frase, janela de navegador com o site (fita 3D em gradiente azul→rosa) e "Direct link → gsap.com/scroll" manuscrito; capa e antes/depois em `design-direction`.

Regras para todas **(complemento)**: as mesmas de React Bits acima (cada componente cumpre uma função, ajuste aos tokens, reduced-motion, 1 WebGL por página, não misture libs de animação) e a regra de **um momento animado por página** (`scroll-and-screen-transitions.md` §5). Visual: `DfkBGDyDgqS_1.jpg` (mosaico das 4) e `DfkBGDyDgqS_3.jpg` (Transitions.dev).
