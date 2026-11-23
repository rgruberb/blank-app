# Rodada 9D — Ferramentas, bibliotecas, design systems e motion systems

Pesquisa feita em 22–23/11/2026 no Chrome, abrindo as fontes oficiais (sites, docs e repositórios GitHub oficiais). Onde a página não trouxe o dado, está escrito "não especificado" ou "não verificado".

## Resumo (principais aprendizados)

1. **shadcn/ui mudou de base**: os componentes agora vêm em 3 variantes (Base UI, React Aria, Radix UI). O Drawer trocou o Vaul pelo Base UI e ganhou swipe, snap points, drawers aninhados e um swipe handle. Isso cobre boa parte do "bottom sheet" iOS-like sem biblioteca extra.
2. **shadcn/ui ainda roda com React 18**: projetos novos nascem com Tailwind v4 + React 19, mas a doc diz que apps em Tailwind v3 + React 18 continuam funcionando.
3. **Duas bibliotecas exigem React 19**: Mantine v9 pede React 19.2+ e HeroUI v3 pede React 19+ e Tailwind v4. Com o stack atual (React 18), as duas ficam fora sem antes subir a versão do React.
4. **Motion for React**: exige React 18.2+. Por padrão usa spring em `x`/`scale` e tween em `opacity`, e a duração padrão de tween é 0,3 s. **Atenção:** o `MotionConfig reducedMotion` tem padrão `"never"`, ou seja, o Reduce Motion do sistema é ignorado até você configurar `"user"`.
5. **Material 3 Expressive aposentou o sistema de easing + duração** ("no longer maintained") em favor de springs, mas publica uma tabela de springs convertidas em cubic-bezier + duração para web. Ela serve direto para CSS e para o Tailwind.
6. **Valores concretos de motion encontrados**: Carbon (6 tokens, de 70 a 700 ms, e 6 curvas), Atlassian (interações de 50 a 150 ms, transições de 150 a 400 ms, 4 curvas) e Material 3 (16 tokens de duração, de 50 a 1000 ms, mais as curvas). A Apple não publica números: só princípios (brevidade, precisão, deixar cancelar).
7. **Ionic React** é a opção mais "nativa" (modo `ios` automático no iPhone) e é a UI recomendada pela própria Capacitor, mas traz o próprio sistema visual, que concorre com Tailwind/shadcn.
8. **Licenças**: tudo o que é open source no núcleo é MIT, exceto React Aria (Apache-2.0), HeroUI (Apache-2.0), Lighthouse (Apache-2.0) e axe-core (MPL-2.0). O GSAP é gratuito, mas sob licença própria ("Standard No Charge"), não MIT. O shadcn.io **não é o shadcn/ui oficial**: é um site comercial de terceiros.
9. **Recomendação (Parte 4)**: manter shadcn/ui + Tailwind + Motion e construir uma camada própria de padrões iOS (tab bar, navegação com título grande, sheet com snap points, swipe-back). Ionic React fica só como plano B, se o app Capacitor precisar de transições de página nativas que a camada própria não alcance.

---

## PARTE 1 — Links semente

### 22. Figma Community
- URL: https://www.figma.com/community | status: ✅ abriu (busca e páginas de arquivo públicas, sem login)
- Kits encontrados (abertos e com licença conferida na página):

| Kit | Autor | URL | Licença | Observação |
|---|---|---|---|---|
| iOS and iPadOS 27 | Apple (oficial) | https://www.figma.com/community/file/1651309003795292092/ios-and-ipados-27 | License Agreement for Apple Design Resources | Atualizado em 28/10/2026, 74,6 mil usuários. Traz Liquid Glass, layout, scroll edge effects. Exige SF Symbols instalado |
| iOS and iPadOS 26 | Apple (oficial) | https://www.figma.com/community/file/1527721578857867021/ios-and-ipados-26 | "License Agreement for Apple Design Resources" | 280 mil usuários. Componentes, text styles, color styles, materiais, layout guides |
| Material 3 Design Kit | Material Design (Google) | https://www.figma.com/community/file/1035203688168086460/material-3-design-kit | CC BY 4.0 | 1,15 milhão de usuários. Funciona com o plugin Material Theme Builder |
| Obra shadcn/ui Community Edition | Obra Studio | https://www.figma.com/community/file/1514746685758799870/shadcn-ui-kit-community-edition | CC BY 4.0 | Listado pela doc oficial do shadcn como "o kit gratuito mais completo" |
| shadcncraft Free Starter Kit | shadcncraft | https://www.figma.com/community/file/1534076420225325960/shadcn-ui-kit-shadcncraft-free-starter-kit | não verificado | Doc do shadcn: variáveis Figma para os 8 estilos e importação de temas |
| CRM UI Kit for SaaS Dashboards | SaaS Dashboard | https://www.figma.com/community/file/1463555657173424575/crm-ui-kit-for-saas-dashboards | CC BY 4.0 | 51,7 mil usuários. Referência para painel do gestor |
| DashStack – Free Admin Dashboard UI Kit | não verificado | https://www.figma.com/community/file/1324762163080748317/dashstack-free-admin-dashboard-ui-kit-admin-dashboard-ui-kit-admin-dashboard | não verificado | Só listado na busca |
| Personal Portfolio Template | não verificado | https://www.figma.com/community/file/1116316830579955404/personal-portfolio-template | não verificado | Só listado na busca; a busca por "portfolio" trouxe sobretudo templates de site genéricos |

- Lista oficial de kits shadcn (doc): https://ui.shadcn.com/docs/figma. Os arquivos são da comunidade, não do shadcn.
- Limitações: kits Apple são para mockup (a licença da Apple restringe o uso dos assets); kits de comunidade variam em qualidade e manutenção.

### 23. shadcn/ui — componentes
- URL: https://ui.shadcn.com/docs/components | status: ✅ | MIT (repositório shadcn-ui/ui, 129 mil estrelas) | gratuito
- Subpáginas: /docs/components/drawer, /docs/components/toast, /docs/installation/vite, /docs/tailwind-v4, /docs/react-19, /docs/figma
- **Mudanças estruturais**: cada componente tem as variantes **Base UI | React Aria | Radix UI**. Há componentes novos voltados a apps (Bubble, Message, Message Scroller, Attachment, Empty, Item, Field, Input Group, Spinner, Kbd, Native Select) e um bloco "AI Elements".
- **Componentes que servem às telas do app**:

| Necessidade | Componente shadcn | Telas |
|---|---|---|
| Bottom sheet iOS | **Drawer** (Base UI): `swipeDirection` up/right/down/left, `snapPoints` (fração do viewport, px ou rem), `showSwipeHandle`, drawers aninhados, `modal={false}`, `data-swiping` / `data-expanded`. Altura máxima padrão `calc(100dvh - 6rem)`; lateral com 75% da largura ou 24rem. No iOS Safari exige `body { position: relative }` | ações rápidas, filtros, detalhes de proposta e agenda |
| Painel lateral | Sheet | painel web |
| Confirmações | Dialog, Alert Dialog | contratos, exclusões |
| Abas | Tabs, Toggle Group | perfil, portfólio, resultados |
| Agenda | Calendar, Date Picker | agenda |
| Formulários | Field, Input, Input OTP, Select, Native Select, Combobox, Checkbox, Radio Group, Switch, Textarea (+ guias de React Hook Form e TanStack Form) | onboarding, propostas, configurações |
| Tabelas | Data Table, Table, Pagination | painel do gestor, CRM |
| Toast | **Toast** (Base UI) com tipos success/info/warning/error/loading, `toast.promise` e ação "Undo". A doc da migração para Tailwind v4 dizia que o toast antigo seria descontinuado em favor do Sonner | feedback global |
| Busca / atalhos | Command, Kbd | painel web |
| Mensagens | Bubble, Message, Message Scroller, Attachment | mensagens |
| Estados vazios / loading | Empty, Skeleton, Spinner, Progress | todas |
| Navegação web | Sidebar, Navigation Menu, Breadcrumb, Menubar | painel web |

- **O que falta para um app iOS-like** (não existe na lista de componentes): tab bar inferior, navigation bar com título grande que colapsa no scroll, transição de página em pilha (push/pop) com swipe-back, segmented control iOS (dá para adaptar o Toggle Group), pull-to-refresh, action sheet no estilo iOS (dá para adaptar o Drawer), list rows com swipe actions e haptics. Tudo isso precisa ser construído (Motion + Capacitor Haptics).
- Compatibilidade: projetos novos usam Tailwind v4 + React 19; "apps existentes com Tailwind v3 e React 18 continuam funcionando" e novos componentes adicionados a eles continuam em v3/React 18 (página /docs/tailwind-v4).
- Limitações: as APIs mudam entre as bases (ex.: `asChild` → `render`, Vaul → Base UI), então escolha uma base e fique nela.

### 24. shadcn.io/ui
- URL: https://www.shadcn.io/ui | status: ✅ | **site comercial de terceiros, não o shadcn/ui oficial** (a própria FAQ pergunta "Are these the official shadcn/ui components?")
- 175 componentes para React, Vue, Svelte e Solid, "grátis com uma conta". O plano Pro traz 6.231 blocks, 14 templates, servidor MCP e 500 arquivos DESIGN.md de marcas. Preços de tabela: Individual US$ 49/mês, Team US$ 99/mês, Organization US$ 199/mês, com promoção de 66% até 30/11/2026. O Individual é "Personal & open source only": uso comercial só a partir do Team.
- Uso no app: inspiração para efeitos e blocks. Risco: licença comercial restrita no plano Individual e dependência de conta.

### 25. shadcn.io/awesome/components
- URL: https://www.shadcn.io/awesome/components | status: ✅ | diretório gratuito com 216 recursos
- Relevantes para o app (só descrição do diretório, sem abrir cada repositório): **Credenza** e **DropDrawer** (padrão dialog no desktop e drawer no mobile), **Tour Kit** (onboarding headless, diz cumprir WCAG 2.1 AA), **Shadcn Event Calendar / Full Calendar / Planner / CalendarCN** (agenda), **shadcn-chat / Message components** (mensagens), **Niko Table / tablecn** (tabelas), **Shadcn Kanban Board** (pipeline de propostas), **React Wheel Picker** (picker em roda, estilo iOS), **Componentry** (animações com Motion, MIT), **Supabase + shadcn/ui + TanStack Table**, **Vaul** (o drawer antigo).
- Limitações: qualidade e manutenção variam; confira licença e atividade no repositório antes de usar.

### 26. Motion for React — docs
- URL: https://motion.dev/docs/react | status: ✅ | MIT (repositório motiondivision/motion, 35,5 mil estrelas) | núcleo gratuito; Motion+ pago (exemplos, Motion UI, AI Kit)
- Subpáginas: /docs/react-installation, /docs/react-transitions, /docs/react-drag, /docs/react-use-reduced-motion, /docs/react-motion-config, /docs/react-accessibility, /docs/performance
- **Requisito**: "compatível apenas com React 18.2 ou superior". Funciona no Vite sem configuração. Import: `motion/react`.
- **Motor híbrido**: roda via Web Animations API e ScrollTimeline, e cai para JS quando precisa de spring, keyframes interrompíveis ou rastreamento de gesto.
- **Spring × tween**:
  - Padrão: propriedades físicas (`x`, `scale`) usam spring; visuais (`opacity`) usam tween.
  - Tween: `duration` padrão de 0,3 s (0,8 s com vários keyframes). Easings nomeados: linear, easeIn/Out/InOut, circIn/Out/InOut, backIn/Out/InOut, anticipate. Aceita cubic-bezier em array `[x1,y1,x2,y2]`.
  - Spring por duração: `duration` + `bounce` (padrão de 0,25, faixa de −1 a 1; 0 = criticamente amortecido). Não incorpora velocidade, mas pode ser gerado como CSS puro.
  - `visualDuration`: incorpora a velocidade do gesto interrompido. É a melhor opção para coordenar com animações por tempo.
  - Spring físico: `stiffness`, `damping` (padrão 10), `mass` (padrão 1; `"auto"` em layout), `restSpeed` 0,1, `restDelta` 0,01. A página lista `stiffness` com padrão "1", o que parece erro de documentação; conferir no código antes de usar como referência.
  - Inércia (usada no drag): `power` 0,8, `timeConstant` 700, `bounceStiffness` 500, `bounceDamping` 10, `modifyTarget` para snap.
  - `MotionConfig transition={…}` define o padrão global; `inherit: true` herda valores.
- **Layout animations**: prop `layout` (corrige distorção de escala) e `layoutId` (shared element). Uso: troca de abas com sublinhado, card que expande para tela cheia no portfólio.
- **AnimatePresence**: animações de saída (`exit`) ao remover do DOM. Uso: toasts, sheets, troca de telas.
- **Gestos**: hover, tap, focus, drag. A doc afirma que `:hover` em CSS é pouco confiável no toque e que os reconhecedores do Motion funcionam entre dispositivos. Drag: `drag="x"`, `dragConstraints` (px ou ref), `dragElastic` (0–1), `dragMomentum`, `dragDirectionLock`, `useDragControls` (arrastar por um handle), `info.velocity` e `offset` no `onDragEnd` (base para swipe-to-dismiss e swipe actions). O Motion **não tem dropzone** (para isso, usar o drag-and-drop nativo ou outra lib). Imagens precisam de `draggable={false}`.
- **Reduced Motion**: `useReducedMotion()` devolve true/false e re-renderiza quando a preferência muda. `MotionConfig reducedMotion`: `"user"` | `"always"` | `"never"`, **padrão `"never"`**. Quando ativo, desliga animações de transform e de layout e mantém opacity e backgroundColor. Recomendação da doc: trocar transform em elementos grandes por opacity, desligar autoplay de vídeo e parallax.
- **Performance** (/docs/performance): orçamento de 16,7 ms por frame a 60 fps e 8 ms a 120 fps. `transform` e `opacity` são os valores mais seguros. Prefira `filter: drop-shadow` a `boxShadow` e `clipPath: inset(0 round Npx)` a `borderRadius`. Animar variável CSS **não** tem aceleração de hardware. `willChange: transform` com moderação.
- Vale para: os dois (PWA/Capacitor e painel web).
- Limitações: o pacote tem tree-shaking, mas o peso não foi medido nesta rodada; o drag dentro de pai com transform exige `correctParentTransform`.

### 27. Motion — Framer
- URL: https://motion.dev/docs/framer | status: ✅
- Sites feitos no Framer já usam Motion. Em code components e overrides, importar de `"framer-motion"` no lugar de `"motion/react"`.
- Para que serve no app: só se a landing de marketing for feita no Framer. **Não se aplica** ao código React + Vite do app.

### 28. LottieFiles — Motion System
- URL: https://lottiefiles.com/motion-system | status: ✅ | **pago**: só nos planos Team+ e Enterprise (não entra em Free, Individual nem Team)
- O que é: biblioteca governada de primitivas de motion (curvas de easing, durações, presets, cores, fontes, assets), criada no Lottie Creator e aplicada pelos plugins de Figma e After Effects. Pode gerar um rascunho a partir de um PDF de brand guide, com IA. A ponte para o código está marcada como "roadmap".
- Uso no app: só se houver ilustrações animadas (onboarding, estados vazios, celebrações) feitas por um motion designer. Para o motion da UI, tokens no código (Tailwind + Motion) bastam.

### 29. LottieFiles docs — Motion System
- URL: https://docs.lottiefiles.com/en/creator/15_motion-system | status: ✅ | atualizada em 10/11/2026
- Seções possíveis: Colors, Easings, Fonts, Motion Presets, Assets (imagens e Lottie) e Documentation. Presets só podem ser criados no Creator, pelo plugin Motion Presets. O sistema é publicado para o time.

### 30. LottieFiles docs — Easing
- URL: https://docs.lottiefiles.com/en/creator/07_animation/easing | status: ✅
- Tangentes de entrada e saída independentes (Linear ou Smooth/Bezier), editor de curva com notação `cubic-bezier(x1, y1, x2, y2)`. Exemplos da página: ease-in-out `cubic-bezier(0.42, 0, 0.58, 1)`, linear `cubic-bezier(0, 0, 1, 1)`, back in-out `cubic-bezier(0.68, -0.55, 0.265, 1.55)`.
- Uso: alinhar as curvas das animações Lottie com os tokens de easing do app.

---

## PARTE 2 — Ferramentas

Legenda: **React DOM?** = confirmado na doc ou repositório oficial. **PWA? / Capacitor?** = bibliotecas web em React DOM rodam no WebView do Capacitor; isso é inferência, salvo onde a doc confirma.

| Ferramenta | URL oficial | Categoria | Licença/preço | React DOM? | PWA? | Capacitor? | Serve para app iOS-like? | Prós | Contras | Alternativas | Quando usar | Quando evitar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| shadcn/ui | ui.shadcn.com | Componentes (código copiado) | MIT, grátis | Sim | Sim (inferido) | Sim (inferido) | Parcial: Drawer com swipe e snap; falta tab bar e nav stack | Código é seu; 3 bases; Tailwind nativo; 129 mil estrelas | Sem padrões iOS prontos; APIs mudam entre bases | Radix Themes, HeroUI | Base do app (já em uso) | Se quiser um kit iOS pronto |
| Radix UI (Primitives) | radix-ui.com/primitives | Primitivas headless | MIT ("Made by WorkOS") | Sim | Sim (inferido) | Sim (inferido) | Indireto | Segue padrões WAI-ARIA; maduro | Sem estilo nem gestos mobile | Base UI, React Aria | Se ficar na variante Radix do shadcn | Gestos e sheets mobile (o Drawer do shadcn agora usa Base UI) |
| Tailwind CSS | tailwindcss.com | CSS utilitário | MIT; v4.3; Tailwind Plus é pago | n/a (CSS) | Sim | Sim | Sim (tokens próprios) | Já no stack; tokens via CSS vars | **v4 exige Safari 16.4+ / Chrome 111+** (limita iPhones antigos) | CSS Modules | Sempre | — |
| Headless UI | headlessui.com | Componentes headless | MIT; v2.2.10 (React) | Sim (React e Vue) | Sim (inferido) | Sim (inferido) | Pouco | Integra com Tailwind; simples | Catálogo pequeno; sem sheet/drawer | Radix, Base UI | Projetos só com Tailwind | Já usando shadcn (redundante) |
| React Aria | react-aria.adobe.com | Hooks e componentes acessíveis | Apache-2.0 (adobe/react-spectrum) | Sim | Sim (inferido) | Sim (inferido) | Indireto | Acessibilidade e i18n de ponta; "interações adaptativas"; 50+ componentes | Mais verboso; sem estilo | Radix, Base UI | Variante React Aria do shadcn; date pickers e i18n PT/EN | Se o time quer menos código |
| Mantine | mantine.dev | Kit completo | MIT; v9.8.2 | Sim | Sim (inferido) | Sim (inferido) | Não (visual próprio) | Muito completo, hooks | **v9 exige React 19.2+**; estilo em CSS Modules, não Tailwind | shadcn | Painel admin rápido em React 19 | **Stack atual (React 18 + Tailwind)** |
| HeroUI | heroui.com | Kit estilizado | Apache-2.0 (no GitHub); v3.2.8 | Sim (também tem "Native") | Sim (inferido) | Sim (inferido) | Parcial | Bonito, Tailwind v4, base React Aria | **v3 exige React 19+ e Tailwind v4**; removeu Framer Motion | shadcn | Projeto novo em React 19 | Stack atual (React 18) |
| Ionic React | ionicframework.com/docs/react | Kit mobile | MIT (ionic-framework, 52,8 mil estrelas) | Sim | Sim | **Sim, oficial** (Capacitor é o runtime oficial; a Capacitor recomenda Ionic) | **Sim**: modo `ios` automático no iPhone, `md` no Android | Visual e transições nativas; mesma empresa da Capacitor | Visual próprio que briga com shadcn/Tailwind; roteamento próprio | Framework7, Konsta UI (não verificado) | App 100% mobile que precisa de look nativo | App com painel web + design próprio |
| Framework7 | framework7.io | Kit mobile | MIT; v9.3.0 (30/10/2026) | Sim (Framework7 React) | Sim (site cita PWA) | Não verificado na doc (provável) | **Sim**: "Now with iOS 26 styles" | Tem sheet, swipeout, pull-to-refresh e navbar prontos | Ecossistema menor; router próprio; estilo próprio | Ionic | Protótipo iOS-like rápido | Integração com shadcn/Tailwind |
| Ant Design Mobile | mobile.ant.design | Kit mobile (H5) | MIT; v5.43.0 | Sim (`antd-mobile`, web H5) | Sim (inferido) | Não verificado | Não (estética Ant) | Leve; tem guias de Reduce Motion (experimental) e React 19 | Visual "Alipay"; doc pensada para o mercado chinês | Vant | Apps H5 no estilo Ant | Visual iOS-like |
| Vant | github.com/youzan/vant | Kit mobile | MIT | **Oficial só para Vue**. Versões React são **comunidade** (3lang3/react-vant, @antmjs/vantui) | — | — | Não | Kit mobile maduro (Vue) | Não é React oficial | Ant Design Mobile | Projetos Vue | **Este app** |
| Motion for React | motion.dev | Animação | MIT; núcleo grátis, Motion+ pago | Sim (React 18.2+) | Sim | Sim (inferido) | **Sim**: springs, drag, layout | Declarativo, gestos, WAAPI | `reducedMotion` padrão `"never"` | GSAP | Todo o motion de UI | — |
| GSAP | gsap.com | Animação | **Grátis, licença própria "Standard No Charge"** (não MIT); proíbe uso em ferramentas no-code que concorram com o Webflow | Sim (via @gsap/react; a página de React não pôde ser lida) | Sim | Sim (inferido) | Parcial | Timelines complexas, ScrollTrigger | Imperativo; a doc do Motion o chama de "messy" com React (opinião do concorrente) | Motion | Animações narrativas de marketing | Microinterações de UI em React |
| Lottie (lottie-web / dotLottie) | github.com/airbnb/lottie-web; github.com/LottieFiles/dotlottie-web | Player de animação | MIT (os dois) | Sim (`@lottiefiles/dotlottie-react`) | Sim | Sim (inferido) | Para ilustração | Animações de designer em JSON/.lottie | Arquivos pesados se mal otimizados; não é UI interativa | Rive | Onboarding, estados vazios, sucesso | Microinterações (use Motion) |
| Rive | rive.app | Animação interativa | Editor freemium: US$ 0, 9, 32 e 120 por assento/mês. **Runtimes MIT**; exportação grátis exibe splash da Rive | Sim (runtime web; detalhe do pacote React não verificado) | Sim | Sim (inferido) | Para ilustração interativa | State machines, arquivos leves | Curva de aprendizado; splash no plano grátis | Lottie | Mascotes e ícones animados com estado | UI comum |
| Figma | figma.com | Design | Starter grátis; Professional US$ 16 (full), 12 (dev), 3 (collab) por mês; Organization US$ 55, 25, 5 | n/a | n/a | n/a | Sim (kit iOS 27 oficial) | Padrão de mercado | Custo por assento | Penpot (não verificado) | Sempre | — |
| Tokens Studio | tokens.studio | Design tokens | Studio grátis (1 projeto, 1 editor); Team €39/mês por editor extra; plano de €499 (detalhe cortado na leitura) | n/a | n/a | n/a | Indireto | Git-sync e temas multidimensionais no Figma | Recursos pagos; complexidade | Figma Variables | Quando houver tokens multi-marca ou multi-tema | Time pequeno com 1 tema |
| Storybook | storybook.js.org (repositório storybookjs/storybook) | Workshop de componentes | MIT (91,7 mil estrelas) | Sim | n/a | n/a | Indireto | Documenta estados; teste visual | Manutenção extra | Ladle (não verificado) | Quando a camada iOS própria crescer | MVP muito inicial |
| Chromatic | chromatic.com | Teste visual (nuvem) | Free US$ 0 (5.000 snapshots); Starter US$ 179; Pro US$ 399/mês | n/a | n/a | n/a | Indireto | Regressão visual do Storybook | Custo por snapshot | Playwright screenshots | Time com Storybook | Sem Storybook |
| Lighthouse | github.com/GoogleChrome/lighthouse | Auditoria | Apache-2.0, grátis | n/a | **Sim** (audita PWA e performance) | n/a | Indireto | Performance, a11y, boas práticas | Score de laboratório, não dados reais | WebPageTest | CI de cada release do PWA | — |
| axe DevTools / axe-core | deque.com/axe/devtools; github.com/dequelabs/axe-core | Teste de acessibilidade | axe-core MPL-2.0; extensão Free; Pro e Bundle pagos (com trial) | n/a | Sim | Sim | Indireto | Padrão de mercado; integra com testes | Pro pago | Lighthouse a11y | Testes automáticos de a11y | — |
| Stark | getstark.co | Acessibilidade (Figma e código) | Planos de US$ 198, 2.500, 8.000 e 21.000 (período não ficou claro no trecho lido) | n/a | n/a | n/a | Indireto | Checa contraste no Figma | Caro para time pequeno | plugins grátis de contraste | Auditoria no design | Orçamento curto |
| Capacitor | capacitorjs.com | Runtime nativo | MIT (ionic-team/capacitor); v8; "An OutSystems Company" | Sim (qualquer web app) | Sim (tem guia de PWA e PWA Elements) | — | Sim (empacota o PWA) | Mesmo código React; plugins nativos | A UI nativa fica por sua conta, ou Ionic | — | Fase 2 do mobile | — |
| Supabase UI → **Supabase Library** | supabase.com/ui (redireciona para /library) | Blocks de backend e UI | Open source (licença exata não verificada) | Sim (registry shadcn) | Sim (inferido) | Sim (inferido) | Indireto | Auth, upload, realtime e chat prontos sobre shadcn | Starters focados em Next.js | blocks próprios | Login, upload de portfólio, realtime de mensagens | — |

---

## PARTE 3 — Design systems e motion systems (11)

### Apple Human Interface Guidelines — Apple
- URL: https://developer.apple.com/design/human-interface-guidelines/motion | ✅
- O que aprender: motion com propósito ("não adicione motion por adicionar"); motion opcional, nunca o único canal de informação (somar haptics e áudio); feedback realista que segue o gesto (se abriu deslizando de cima, não feche para o lado); "brevidade e precisão" nas animações de feedback; deixar a pessoa cancelar o motion. O Liquid Glass responde ao toque com mais ênfase do que ao trackpad.
- Tokens: não publica tokens de motion. Os kits Figma oficiais (iOS 26/27) trazem text styles, color styles e materiais.
- Durações/easing: **não especificado**.
- Acessibilidade: https://developer.apple.com/design/human-interface-guidelines/accessibility. Permitir aumentar o texto em pelo menos 200%; Dynamic Type; contraste por WCAG ou APCA.
- Aplicabilidade: **alta** (direção visual do app).

### Material Design 3 — Google
- URLs: https://m3.material.io/styles/motion/easing-and-duration/tokens-specs | https://m3.material.io/styles/motion/overview/specs | ✅
- O que aprender: o M3 Expressive migrou para um "motion physics system" baseado em springs; o sistema de easing e duração "não é mais mantido", mas ainda serve para transições.
- **Tokens de duração (legado)**: short1–4 = 50/100/150/200 ms; medium1–4 = 250/300/350/400 ms; long1–4 = 450/500/550/600 ms; extra-long1–4 = 700/800/900/1000 ms. Exemplos da página: selection controls em 200 ms com Standard; FAB → Sheet em 400 ms com Emphasized.
- **Easing (legado)**: standard `cubic-bezier(0.2, 0, 0, 1)`; standard.decelerate `(0, 0, 0, 1)`; standard.accelerate `(0.3, 0, 1, 1)`; emphasized.decelerate `(0.05, 0.7, 0.1, 1)`; emphasized.accelerate `(0.3, 0, 0.8, 0.15)`; emphasized: "N/A, use Standard como fallback" em CSS.
- **Springs convertidas para web (curva + duração)**:
  - Expressive: fast spatial `0.42, 1.67, 0.21, 0.90` em 350 ms; default spatial `0.38, 1.21, 0.22, 1.00` em 500 ms; slow spatial `0.39, 1.29, 0.35, 0.98` em 650 ms; fast effects `0.31, 0.94, 0.34, 1.00` em 150 ms; default effects `0.34, 0.80, 0.34, 1.00` em 200 ms; slow effects `0.34, 0.88, 0.34, 1.00` em 300 ms.
  - Standard: spatial `0.27, 1.06, 0.18, 1.00` em 350, 500 e 750 ms (fast, default, slow); effects iguais aos do Expressive.
  - Os tokens de spring (stiffness e damping) existem, mas os valores não foram extraídos: ficam numa árvore recolhida na página.
- Acessibilidade: https://m3.material.io/foundations/overview/principles (título "Accessibility overview")
- Aplicabilidade: **alta** como referência de números para web, mesmo com visual iOS. "Spatial" (posição e tamanho) × "effects" (cor e opacidade) é uma divisão útil para o app.

### IBM Carbon — IBM
- URL: https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview | ✅
- O que aprender: dois estilos, **productive** (eficiência, microinterações) e **expressive** (momentos importantes e raros). Duração dinâmica conforme a distância (Motion Generator).
- **Tokens de duração**: fast-01 70 ms (botão, toggle); fast-02 110 ms (fade); moderate-01 150 ms (pequenas expansões); moderate-02 240 ms (expansão, toast); slow-01 400 ms (grandes expansões); slow-02 700 ms (escurecer o fundo). Microinterações entre 90 e 120 ms (checklist da página).
- **Easing** (productive / expressive): standard `(0.2, 0, 0.38, 0.9)` / `(0.4, 0.14, 0.3, 1)`; entrance `(0, 0, 0.38, 0.9)` / `(0, 0, 0.3, 1)`; exit `(0.2, 0, 1, 0.9)` / `(0.4, 0.14, 1, 1)`. Regra: elemento que sai mas fica "por perto" (painel lateral) usa standard, não exit.
- Acessibilidade: https://www.carbondesignsystem.com/building-blocks/foundations/accessibility/overview
- Aplicabilidade: **alta** para o painel web (produtivo, denso em dados).

### Atlassian Design System — Atlassian
- URL: https://atlassian.design/foundations/motion | ✅
- O que aprender: cada evento de motion = duração + easing + propriedade, empacotados em tokens (ex.: `motion.popup.enter`). **Regra de frequência**: o que é disparado dezenas de vezes por dia fica abaixo de 150 ms; o que aparece uma vez por sessão pode ser mais expressivo.
- **Durações**: interações de 50 a 150 ms (hover de item de lista em 50 ms); transições de 150 a 400 ms (dropdown em 150 ms, modal em 250 ms).
- **Easing**: ease-out bold `(0, 0.4, 0, 1)` para Panel/Flag entrando; ease-in-out bold `(0.4, 0, 0, 1)` para escalar modais; ease-in practical `(0.6, 0, 0.8, 0.6)` para saídas; ease-out practical `(0.4, 1, 0.6, 1)` para Popup e fades de hover.
- Reduced motion: hoje, com a preferência ativa, o motion fica desligado e instantâneo.
- Tokens: https://atlassian.design/foundations/tokens/design-tokens | Acessibilidade: https://atlassian.design/foundations/accessibility
- Aplicabilidade: **alta** (a regra de frequência resolve debates de duração).

### Microsoft Fluent 2 — Microsoft
- URL: https://fluent2.microsoft.design/motion | ✅
- O que aprender: princípios Functional, Natural (inércia, gravidade, peso) e Consistent; seção "Accessible motion design" (ter um modo "sem motion", como recomenda a WCAG; durações curtas; nada de flashes; motion contido no elemento).
- Tokens: página de design tokens em https://fluent2.microsoft.design/design-tokens. Valores de duração e curva **não especificados** nas páginas lidas.
- Acessibilidade: https://fluent2.microsoft.design/accessibility
- Aplicabilidade: **média** (bons princípios, sem números nas páginas abertas).

### Shopify Polaris — Shopify
- URL tentada: https://polaris-react.shopify.com/design/motion → **redireciona** para https://shopify.dev/docs/api/polaris | ⚠️ a página de motion não existe mais
- O que aprender: o Polaris agora é "o framework de UI unificado da Shopify, construído sobre web components", voltado a apps dentro do admin da Shopify.
- Tokens e motion: não encontrados após o redirect.
- Aplicabilidade: **baixa** (específico do ecossistema Shopify).

### GitHub Primer — GitHub
- URL: https://primer.style/product/primitives/ | ✅ (a URL de motion tentada redirecionou para a home)
- O que aprender: primitivas de cor, tipografia e espaçamento, com nomenclatura de tokens (https://primer.style/product/primitives/token-names/) e modos e temas de cor.
- Motion: **página não encontrada** na navegação de primitivas.
- Acessibilidade: https://primer.style/accessibility/
- Aplicabilidade: **média** (nomenclatura de tokens e dark mode para o painel web).

### Salesforce Lightning Design System 2 — Salesforce
- URL: https://www.lightningdesignsystem.com/ (redireciona para "Lightning Design System 2") | ✅
- O que aprender: tokens via "Styling Hooks" globais e por componente (https://www.lightningdesignsystem.com/2e1ef8501/p/777f5a-global-styling-hooks); acessibilidade documentada por componente; "Global Accessibility Standards".
- Motion: **nenhum link de motion** na navegação.
- Acessibilidade: https://www.lightningdesignsystem.com/2e1ef8501/p/641741-accessibility
- Aplicabilidade: **média/baixa** (bom modelo de doc de acessibilidade por componente; visual corporativo).

### Radix Themes — WorkOS
- URL: https://www.radix-ui.com/themes/docs/overview/getting-started | ✅
- O que aprender: kit pré-estilizado com tokens de Color, Dark mode, Typography, Spacing, Breakpoints, Radius, Shadows e Cursors; tem Segmented Control, Data List, Radio Cards e Checkbox Cards.
- Motion: **não especificado** (sem página de motion na navegação).
- Acessibilidade: herdada das Primitives (WAI-ARIA).
- Aplicabilidade: **média** (escala de cores e radius como referência; o app já usa shadcn).

### Ant Design — Ant Group
- URLs: https://ant.design/docs/spec/motion | https://ant.design/docs/react/customize-theme | ✅ (v6.7.1)
- O que aprender: princípios Natural, Performant, Concise. Tokens de motion no tema: `motionUnit` 0.1, `motionBase` 0, `motionDurationFast/Mid/Slow` e curvas `motionEaseInOut`, `motionEaseOut`, `motionEaseOutBack`, `motionEaseInQuint`, `motionEaseOutCirc` etc. Os valores padrão não aparecem na tabela lida (**não especificado**).
- Aplicabilidade: **baixa/média** (padrões de painel denso; estética distante do iOS).

### Motion System (LottieFiles) — LottieFiles
- Ver links 28–29. Motion system como ferramenta de governança, não como guideline. Pago (Team+/Enterprise). Aplicabilidade: **baixa** agora, **média** se houver muita ilustração animada.

### Tabela comparativa de motion publicada

| Sistema | Durações | Easing padrão (entrada) | Saída | Reduced motion |
|---|---|---|---|---|
| Apple HIG | não especificado | não especificado | não especificado | motion opcional; deixar cancelar |
| Material 3 | 50–1000 ms (16 tokens); springs para web de 150 a 750 ms | `0.2, 0, 0, 1` (standard) | `0.3, 0, 1, 1` (accelerate) | não lido nesta rodada |
| Carbon | 70 / 110 / 150 / 240 / 400 / 700 ms | `0, 0, 0.38, 0.9` (productive entrance) | `0.2, 0, 1, 0.9` | página de acessibilidade separada |
| Atlassian | 50–150 ms (interação); 150–400 ms (transição) | `0, 0.4, 0, 1` (bold) / `0.4, 1, 0.6, 1` (practical) | `0.6, 0, 0.8, 0.6` | motion desligado e instantâneo |
| Fluent 2 | não especificado | não especificado | não especificado | modo "sem motion" (WCAG) |
| Motion (lib) | tween 300 ms padrão; spring bounce 0,25 | spring em x/scale | — | `reducedMotion` padrão "never" (configurar "user") |

---

## PARTE 4 — Critérios de escolha

Cenário: PWA → Capacitor, visual iOS-like, Tailwind já em uso, React 18, painel web e mobile no mesmo código.

| Critério | shadcn/ui | Ionic React | Mantine | HeroUI | Componentes próprios |
|---|---|---|---|---|---|
| Visual iOS-like | Médio (neutro; Drawer com swipe) | **Alto** (modo `ios` automático) | Baixo | Médio | Alto (se bem feito) |
| Gestos nativos | Médio (Drawer: swipe e snap; o resto via Motion) | **Alto** (nav stack, swipe-back, sheets) | Baixo | Médio | Depende do Motion |
| Acessibilidade | Alta (Base UI, Radix ou React Aria) | Alta (não auditada nesta rodada) | Alta (não auditada) | Alta (React Aria no v3) | **Risco**: tudo por sua conta |
| Peso do bundle | Baixo (só o que você copia; não medido) | Alto (framework inteiro; não medido) | Médio/alto (não medido) | Médio (não medido) | Baixo |
| Customização com Tailwind | **Total** | Baixa (sistema de estilo próprio; integração com Tailwind não verificada) | Baixa (CSS Modules) | Alta (Tailwind v4) | Total |
| Maturidade | Alta (129 mil estrelas) | Alta (52,8 mil estrelas) | Alta (32 mil) | Média/alta (31,3 mil) | Nenhuma |
| Licença | MIT | MIT | MIT | Apache-2.0 | sua |
| **Compatível com React 18 hoje?** | **Sim** | Sim ("versões recentes"; política de suporte não lida) | **Não (v9 exige 19.2+)** | **Não (v3 exige 19+)** | Sim |

**Recomendação:** **shadcn/ui (variante Base UI) + Motion for React + uma camada própria fina de padrões iOS.**

Justificativa:
1. Já está no stack, é 100% Tailwind e roda em React 18. O Drawer novo resolve sheets com snap points e swipe, que é o padrão iOS mais usado no app (ações, filtros, detalhes).
2. A camada própria, pequena e testada, cobre só o que falta: tab bar inferior, navigation bar com título grande, transição push/pop com swipe-back (Motion `drag="x"` + `AnimatePresence`), swipe actions em listas e segmented control. Haptics vêm do Capacitor. Documente isso no Storybook quando passar de uns 10 componentes.
3. Mantine e HeroUI saem por exigirem React 19 (reavaliar se o projeto migrar). Ionic React fica como **plano B** só para o app Capacitor, caso transições de página nativas virem requisito de loja. O custo é ter dois sistemas visuais.
4. Configurações obrigatórias desde o dia 1: `<MotionConfig reducedMotion="user">` na raiz; tokens de duração e easing no Tailwind (sugestão: microinteração 100–150 ms; transições de 200–400 ms com a curva Material "standard" ou "Expressive default spatial" para spring; saídas mais curtas que entradas); animar só `transform` e `opacity`; `body { position: relative }` para o Drawer no iOS Safari; testar no iOS 16.4+ (limite do Tailwind v4).
5. Qualidade: Lighthouse no CI do PWA, axe-core nos testes e checagem de contraste no Figma (plugin gratuito antes de considerar o Stark).

---

## Fontes verificadas

Parte 1
- https://www.figma.com/community (busca) · https://www.figma.com/community/file/1651309003795292092/ios-and-ipados-27 · https://www.figma.com/community/file/1527721578857867021/ios-and-ipados-26 · https://www.figma.com/community/file/1035203688168086460/material-3-design-kit · https://www.figma.com/community/file/1463555657173424575/crm-ui-kit-for-saas-dashboards
- https://ui.shadcn.com/docs/components · https://ui.shadcn.com/docs/components/drawer · https://ui.shadcn.com/docs/components/toast · https://ui.shadcn.com/docs/installation/vite · https://ui.shadcn.com/docs/tailwind-v4 · https://ui.shadcn.com/docs/react-19 · https://ui.shadcn.com/docs/figma
- https://www.shadcn.io/ui · https://www.shadcn.io/awesome/components
- https://motion.dev/docs/react · https://motion.dev/docs/react-installation · https://motion.dev/docs/react-transitions · https://motion.dev/docs/react-drag · https://motion.dev/docs/react-use-reduced-motion · https://motion.dev/docs/react-motion-config · https://motion.dev/docs/react-accessibility · https://motion.dev/docs/performance · https://motion.dev/docs/framer
- https://lottiefiles.com/motion-system · https://docs.lottiefiles.com/en/creator/15_motion-system · https://docs.lottiefiles.com/en/creator/07_animation/easing

Parte 2
- https://www.radix-ui.com/primitives/docs/overview/introduction · https://tailwindcss.com · https://tailwindcss.com/docs/compatibility · https://headlessui.com · https://react-aria.adobe.com · https://mantine.dev/getting-started/ · https://mantine.dev/changelog/9-0-0/ · https://mantine.dev/styles/css-modules/ · https://www.heroui.com/docs/guide/installation · https://ionicframework.com/docs/react · https://ionicframework.com/docs/theming/platform-styles · https://framework7.io · https://framework7.io/react/ · https://mobile.ant.design · https://mobile.ant.design/guide/quick-start · https://gsap.com/pricing/ · https://gsap.com/licensing/ · https://rive.app/pricing · https://www.figma.com/pricing/ · https://tokens.studio/pricing · https://www.chromatic.com/pricing · https://www.getstark.co/pricing/ · https://www.deque.com/axe/devtools/pricing/ · https://capacitorjs.com/docs · https://capacitorjs.com/docs/getting-started/ui · https://supabase.com/ui → https://supabase.com/library/docs/getting-started/introduction
- GitHub (licença e estrelas): shadcn-ui/ui · radix-ui/primitives · tailwindlabs/tailwindcss · tailwindlabs/headlessui · adobe/react-spectrum · mantinedev/mantine · heroui-inc/heroui · ionic-team/ionic-framework · framework7io/framework7 · ant-design/ant-design-mobile · youzan/vant · motiondivision/motion · ionic-team/capacitor · storybookjs/storybook · GoogleChrome/lighthouse · dequelabs/axe-core · airbnb/lottie-web · LottieFiles/dotlottie-web
- Não abertos (marcados como não verificados na tabela): site do Storybook, página React do GSAP (bloqueada na leitura), política de suporte do Ionic React.

Parte 3
- https://developer.apple.com/design/human-interface-guidelines/motion · https://developer.apple.com/design/human-interface-guidelines/accessibility
- https://m3.material.io/styles/motion/easing-and-duration/tokens-specs · https://m3.material.io/styles/motion/overview/specs · https://m3.material.io/foundations/overview/principles
- https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview · https://www.carbondesignsystem.com/building-blocks/foundations/accessibility/overview
- https://atlassian.design/foundations/motion · https://atlassian.design/foundations/accessibility · https://atlassian.design/foundations/tokens/design-tokens
- https://fluent2.microsoft.design/motion · https://fluent2.microsoft.design/design-tokens · https://fluent2.microsoft.design/accessibility
- https://polaris-react.shopify.com/design/motion → https://shopify.dev/docs/api/polaris
- https://primer.style/product/primitives/
- https://www.lightningdesignsystem.com/ (LDS 2)
- https://www.radix-ui.com/themes/docs/overview/getting-started
- https://ant.design/docs/spec/motion · https://ant.design/docs/react/customize-theme

## Prints

Prints de referência visual (layouts, componentes e kits). Substituem os prints de tabelas de documentação da primeira versão.

| Arquivo | URL | O que mostra |
|---|---|---|
| 9D_figma-ios27-kit_1.png | https://www.figma.com/community/file/1651309003795292092/ios-and-ipados-27 | Kit oficial da Apple iOS 27, página "Layout Guides": safe areas e margens no iPhone, inclusive com sheet aberta |
| 9D_figma-obra-shadcn-kit_1.png | https://www.figma.com/community/file/1514746685758799870/shadcn-ui-kit-community-edition | Kit Obra shadcn/ui (CC BY 4.0): avatar, badge, charts, buttons e tooltip no estilo Nova |
| 9D_figma-crm-dashboard-kit_1.png | https://www.figma.com/community/file/1463555657173424575/crm-ui-kit-for-saas-dashboards | CRM UI Kit (CC BY 4.0): métricas, tarefas, tabelas e gráficos; referência para o painel do gestor |
| 9D_shadcn-drawer_1.png | https://ui.shadcn.com/docs/components/drawer | Drawer lateral aberto: lista de horários selecionáveis com CTA fixo; padrão para escolher horário na agenda |
| 9D_shadcn-drawer_2.png | https://ui.shadcn.com/docs/components/drawer | Drawer de baixo com swipe handle e snap points (versão "peek"); padrão de bottom sheet |
| 9D_shadcn-blocks-dashboard_1.png | https://ui.shadcn.com/blocks | Block dashboard-01 no desktop: sidebar, cards de KPI com tendência, gráfico com filtro de período |
| 9D_shadcn-blocks-dashboard_2.png | https://ui.shadcn.com/blocks | O mesmo dashboard na prévia mobile: cards de KPI empilhados |
| 9D_ionic-ios-sheet-modal_1.png | https://ionicframework.com/docs/api/modal | Sheet modal no modo iOS: handle, busca e lista de contatos sobre a tela |
| 9D_ionic-ios-tab-bar_1.png | https://ionicframework.com/docs/api/tabs | Tab bar inferior no modo iOS (4 abas com ícone e rótulo) e navigation bar |
| 9D_framework7-ios26-kitchen-sink_1.png | https://framework7.io/react/kitchen-sink.html | Framework7 React com estilo iOS 26: título grande, botões circulares e lista agrupada (inset) |
| 9D_supabase-library-blocks_1.png | https://supabase.com/library | Blocks da Supabase Library: login, painel de métricas, chat e perfil/conta |
| 9D_motion-examples-swipe_1.png | https://motion.dev/examples?platform=react&search=swipe | Exemplos do Motion para React: swipe actions, sheet modal, card stack e galerias com swipe |
