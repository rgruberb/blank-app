# React Bits: componentes animados prontos

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
