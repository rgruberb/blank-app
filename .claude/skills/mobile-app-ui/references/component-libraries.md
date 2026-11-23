# Bibliotecas de componentes para app mobile web (PWA, opcionalmente empacotado com Capacitor)

Fonte: pesquisa 9D (docs e repositórios oficiais lidos em 22–23/11/2026; dado bruto em `docs/achados/rodada-9D.md`).
"(inferido)" = a doc não diz; uma lib React DOM roda no WebView do Capacitor por ser web. Versões mudam: confira antes de instalar.

## Compatibilidade

| Biblioteca | Licença | React DOM | React 18? | PWA / Capacitor | Visual iOS-like | Nota |
|---|---|---|---|---|---|---|
| **shadcn/ui** | MIT | sim | **sim** (novos projetos nascem Tailwind v4 + React 19; Tailwind v3 + React 18 segue funcionando) | sim (inferido) | parcial | 3 variantes por componente: **Base UI / React Aria / Radix UI** — escolha uma e fique nela (`asChild` → `render`, Vaul → Base UI) |
| shadcn **Drawer** (Base UI) | MIT | sim | sim | sim (inferido) | **sim** para sheet | `swipeDirection`, `snapPoints` (fração, px, rem), `showSwipeHandle`, drawers aninhados, `modal={false}`; altura máx. `calc(100dvh - 6rem)`; **iOS Safari exige `body { position: relative }`** |
| Radix Primitives | MIT | sim | sim | sim (inferido) | indireto | WAI-ARIA maduro; sem gestos mobile |
| React Aria | Apache-2.0 | sim | sim | sim (inferido) | indireto | a11y e i18n fortes (date picker PT/EN); verboso |
| Headless UI | MIT (v2.2) | sim | sim | sim (inferido) | pouco | catálogo pequeno, **sem sheet/drawer** |
| Mantine v9 | MIT | sim | **não — exige React 19.2+** | sim (inferido) | não | CSS Modules, não Tailwind |
| HeroUI v3 | Apache-2.0 | sim | **não — exige React 19+ e Tailwind v4** | sim (inferido) | parcial | base React Aria |
| **Ionic React** | MIT | sim | sim ("versões recentes"; política não lida) | **sim, oficial**: UI recomendada pela Capacitor | **alto**: modo `ios` automático no iPhone, `md` no Android | nav stack, swipe-back, sheet modal, tab bar prontos; **sistema visual e roteamento próprios** que concorrem com Tailwind/shadcn |
| Framework7 (React) | MIT (v9.3) | sim | — | PWA citado; Capacitor não verificado | **alto** ("iOS 26 styles") | sheet, swipeout, pull-to-refresh, navbar; router e estilo próprios |
| Ant Design Mobile | MIT (v5.43) | sim (H5) | — | PWA (inferido); Capacitor não verificado | não (estética Ant/Alipay) | tem guia de Reduce Motion (experimental) |
| Vant | MIT | **não**: oficial só Vue; versões React são da comunidade | — | — | não | fora para app React |
| Motion for React | MIT (núcleo) | sim | **sim (18.2+)** | sim | gestos, springs, layout | `reducedMotion` padrão **"never"** → use `<MotionConfig reducedMotion="user">` |

## Critérios (gerais; Parte 4 da 9D)
A 9D avaliou um cenário de exemplo (PWA → Capacitor, visual iOS-like, Tailwind, React 18, web e mobile no mesmo
código). Para qualquer projeto, pese: **compatível com a versão de React do projeto** (eliminatório) · visual
plataforma-like pedido · gestos nativos · acessibilidade · peso do bundle (não medido) · casa com o sistema de estilo já
adotado · maturidade · licença. Componente 100% próprio = acessibilidade toda por sua conta.

## Recomendação condicionada ao stack
- **Se o stack for React DOM + Tailwind + PWA (com ou sem Capacitor) e um só sistema com o web app:** shadcn/ui (uma
  variante, ex. Base UI) + Motion for React + uma camada própria fina de padrões iOS (abaixo).
- **Se estiver em React 18:** Mantine v9 e HeroUI v3 ficam fora (exigem React 19+); em React 19+ voltam à disputa.
- **Se transições de página nativas forem requisito e o app for empacotado (Capacitor):** Ionic React — custo: dois
  sistemas visuais se houver web app separado.
- **Se o app for nativo (SwiftUI/Compose) ou RN/Flutter:** esta tabela não se aplica; use os componentes da plataforma.

### Camada iOS própria (o que o shadcn não tem)
| Padrão | Como construir | Regra de UX (SKILL.md) |
|---|---|---|
| **Tab bar inferior** | componente próprio, `env(safe-area-inset-bottom)`, indicador com `layoutId` | regra 3; `mobile-patterns.md` §4 |
| **Navigation bar com título grande** que colapsa no scroll | `useScroll` + `useTransform` (34 → 18px) | regra 6; `ui-motion` `micro-interactions.md` §4 |
| **Sheet com snap points** | Drawer Base UI (`snapPoints`, handle) | regra 4; `mobile-patterns.md` §6 |
| **Push/pop com swipe-back** | Motion `drag="x"` + `AnimatePresence`; não bloquear o voltar do navegador | regra 4 |
| Swipe actions em lista, segmented control, pull-to-refresh, action sheet | Motion `drag` + `onDragEnd` (`info.velocity`); Toggle Group adaptado; Drawer adaptado | regras 7, 11; `mobile-patterns.md` §16 |
| Haptics | Se empacotado com Capacitor: Capacitor Haptics (sem equivalente no Safari) | regra 7 |

### Dia 1 (se adotar esse stack)
`<MotionConfig reducedMotion="user">` na raiz · tokens de duração/easing no Tailwind com os valores de `ui-motion` ·
animar só `transform`/`opacity` · `body { position: relative }` (Drawer no iOS Safari) · testar em **iOS 16.4+**
(Tailwind v4 exige Safari 16.4+/Chrome 111+) · Lighthouse no CI, axe-core nos testes · Storybook quando a camada passar
de ~10 componentes.

Kits Figma e blocks de referência: `benchmark-sources.md`.
