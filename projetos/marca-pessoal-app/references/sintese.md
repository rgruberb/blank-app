# Síntese final: pesquisa de Product Design do app de marca pessoal

Data: 23/11/2026. Base: rodadas `docs/achados/rodada-9A.md` (fundações oficiais), `9B` (NN/g), `9C` (inspiração), `9D` (ferramentas, design systems e critérios), `9E` (Instagram), `9F` (Facebook, YouTube, newsletters) e as skills do projeto em `.claude/skills/` (`mobile-app-ui`, `desktop-app-ui`, `website-ui`, `ux-patterns`, `ui-motion`, `design-direction`, `dashboard-ui`).

**Produto:** gestão de marca pessoal (presença, conteúdo, agenda, portfólio, networking, propostas, contratos, mensagens, resultados). Painel web para gestor e cliente; app mobile do cliente como PWA no piloto e depois o mesmo React empacotado com Capacitor. Stack: React 18, TypeScript, Vite, Supabase, Tailwind, shadcn/ui, Motion for React. Público avançado, PT e EN. React Native fica fora como base.

**Como ler este documento.** As seções 2 a 12 resumem as rodadas e apontam para o arquivo de origem. A seção 13 traz as decisões. A 14 é o checklist de auditoria e a 15 reúne os entregáveis. A seção 16 lista as lacunas e a 17, as fontes. Cada número citado vem de uma rodada ou de uma skill, com a fonte entre parênteses. Quando uma decisão é inferência minha, ela aparece marcada como **(inferência)**. As decisões aprovadas pelo usuário aparecem como **D1–D8** (lista no início da seção 13).

---

## 1. Visão geral: como usar a biblioteca de recursos e as skills

1. **As skills mandam nos números e as rodadas dão o embasamento.** Pela regra de prioridade das skills (`mobile-app-ui`, `ui-motion`, `desktop-app-ui`), os valores de design (durações, alvos, escala, sombra, quantidade de animação) vêm das skills do projeto. As rodadas 9A–9F confirmam esses valores, preenchem lacunas e mostram as limitações. Quando uma fonte oficial diverge de uma skill, a divergência está registrada aqui.
2. **Cada skill tem a sua superfície.** O PWA e o Capacitor do cliente seguem `mobile-app-ui`. O painel web em tela de 1024 px ou mais segue `desktop-app-ui`, com `dashboard-ui` para Resultados. O perfil público e o portfólio seguem `website-ui`. Identidade visual fica com `design-direction`. Motion fica com `ui-motion` e qualquer revisão passa por `ux-patterns`.
3. **Os tokens vêm antes das telas.** Primeiro se fecham tipografia, espaço, alvo, cor e motion em CSS vars e no Tailwind. Só depois se desenham as telas (seção 13, fase 1).
4. **Fica mantido o stack shadcn/ui (Base UI) + Motion, com uma camada própria de padrões iOS.** Essa é a decisão final da 9D. Mantine v9 e HeroUI v3 exigem React 19 e saem. Ionic React fica como plano B do Capacitor (seção 15h).
5. **As fontes oficiais servem para regra e os perfis sociais servem para ideia.** Apple, Material, Carbon, Atlassian e NN/g dão regras verificáveis. Instagram, Dribbble e Behance dão inspiração visual, e boa parte disso é isca de lead ou conceito sem uso real (9C, 9E).
6. **Toda tela passa pelo teste dos 4 estados**: vazio, carregando, erro e texto longo, mais offline no mobile (`design-direction` regra 17, `mobile-app-ui` §10, NN/g empty states em 9B).
7. **Para auditar, use o checklist da seção 14** antes de cada release e reporte o antes e o depois com números (workflow de `ux-patterns`).
8. **Mantenha um radar semanal leve:** Smashing Magazine, Frontend Focus, React Status, Ionic Forum e os 5 primeiros perfis do top 15 do Instagram (seção 15c). O resto é consulta pontual, não feed.
9. **Verifique no browser.** Use `ext-playwright-cli` em 360×800, 375×812 e 390×844 no mobile e em 768, 1024, 1280 e 1440 na web. Meça alvos com `getBoundingClientRect()`. Emule reduced motion, dark mode e rede lenta (`mobile-app-ui` workflow 6, `website-ui`).
10. **Seja crítico com as fontes:** Mobbin está 🔒, quase não há conteúdo em PT-BR, parte do NN/g é de 2015–2019 e a Apple não publica números de motion. A seção 16 reúne tudo o que falta.

---

## 2. Fundações (resumo de 9A e das skills)

Detalhes: `docs/achados/rodada-9A.md` (fichas 1–7 e a tabela comparativa).

| Tema | O que adotar | Fonte |
|---|---|---|
| Alvo de toque | Piso de 44 px no PWA e padrão confortável de 48 px, com ≥ 8 px entre alvos. Na web com mouse o piso é 24 px e a meta 44 | 9A (Apple 44×44 pt / Material 48×48 dp, 8 dp), `ux-patterns`, `desktop-app-ui` §3 |
| Escala tipográfica | Produto denso: 16 × 1,2ⁿ = 16, 19, 23, 28, 33, 40, 48. Site e portfólio público: Major Third 16 × 1,25ⁿ = 12,8, 16, 20, 25, 31, 39, 49. Não misturar as duas na mesma superfície | `ux-patterns`, `mobile-app-ui` §6, `website-ui` |
| Texto | Line-height de 1,5 no corpo caindo até 1,1 nos títulos grandes. Tracking de −0,02em em títulos e +0,05–0,06em em caixa-alta. Medida de 45–75 caracteres (45–60 em formulários), com o token `--measure: 50ch` ≈ 66–71 caracteres (D8); o Material pede 40–60. Mínimo de 11 pt (iOS). Pesos Regular a Bold, sem Ultralight, Thin ou Light | `ux-patterns`, 9A (Apple Typography, M3) |
| Texto ampliável | Funcionar com 200% de texto, sem truncar em áreas roláveis | 9A (Apple Accessibility) |
| Contraste | 4,5:1 no texto, 3:1 em texto grande, ícones e bordas. Buscar 7:1 em texto pequeno no dark mode | 9A, 9B, 9C (Coolors), `ux-patterns` |
| Espaçamento | Grade de 8 (8, 16, 24, 32, 48, 64); o 4 só em micro | `ux-patterns` |
| Layout adaptativo | Material: compact < 600, medium 600–839, expanded 840–1199, large 1200–1599, extra-large ≥ 1600 dp. Barra inferior ↔ rail, e bottom sheet ↔ menu. Apple decide por size class, não por dispositivo | 9A (M3 breakpoints, Apple Layout) |
| Breakpoints do projeto | Mobile base de 375 px. Web em 768, 1024, 1280 e 1440, mais 1920 no painel. 1024 é o mínimo do desktop (sidebar vira rail) | `website-ui`, `desktop-app-ui` §2 |
| Cor | Papéis semânticos com variantes claro, escuro e alto contraste. Nunca depender só de cor | 9A (Apple Color), 9B |
| Dark mode | Sem `#000` (ex.: `#0C1424`), texto a 87%, acento clareado, elevação por luminosidade. Seguir `prefers-color-scheme` | `ux-patterns`, `mobile-app-ui` §14, 9A |
| Acessibilidade web | Landmarks ARIA, um único H1 e headings sem pular nível | 9A (M3 Accessibility designing) |

**Ponto crítico:** a tabela de tipografia iOS capturada na 9A corresponde ao tamanho "xSmall", não ao padrão "Large", então não serve como escala. O único dado confirmado é o corpo padrão de 17 pt. A escala do projeto é 16 × 1,2 com corpo 16, igual no app e no painel (D1); o corpo 17 pt do iOS fica só como referência do nativo (`mobile-app-ui` §6).

---

## 3. UI mobile (PWA e depois Capacitor)

Detalhes: `9A` (tab bars, sheets), `9B` (navegação, alvos, 4 iOS rules to break), `9D` (Drawer do shadcn, Ionic), skill `mobile-app-ui`.

- **Tab bar:** 3–5 seções, nunca ações, com ícone e rótulo de uma palavra, um acento só na aba ativa e sem desabilitar nem esconder abas. A Apple pede para evitar a aba "More" (`mobile-app-ui` §3, 9A, 9B).
- **Navegação:** stack com back e edge-swipe preservado. Tarefa curta fica em sheet. O card vira página e volta ao lugar de onde saiu (`mobile-app-ui` §4).
- **Sheets:** detents médio (cerca de metade da tela) e grande, com grabber, swipe para dispensar e confirmação se houver mudança não salva. Uma sheet por vez. Fluxo longo vai para tela cheia (9A Sheets). Implementação: Drawer do shadcn (Base UI) com `snapPoints`, `showSwipeHandle` e `body { position: relative }` no iOS Safari (9D).
- **Safe areas:** nada interativo sob notch ou home indicator. O rodapé fixo soma `env(safe-area-inset-bottom)` (`mobile-app-ui` §5).
- **Zona do polegar:** a ação principal e as decisões ficam fixas no rodapé, como o botão de pagamento fixo do exemplo NN/g/Hotel Tonight (9B, `mobile-app-ui` §2).
- **Teclado:** `inputmode` e `autocomplete` corretos, e o campo focado e o CTA sempre acima do teclado (`mobile-app-ui` §9).
- **Gestos:** todo gesto tem uma alternativa visível (9A Accessibility, `mobile-app-ui` §7). Long press dura 400 ms e reordenar levanta o item a 105%.
- **Haptics:** no Capacitor, via plugin de Haptics (9D), só em snap, toggle, sucesso e soltar do pull. Nunca em scroll.
- **Cuidado com o "iOS-like":** a NN/g mostra que page control (pontinhos), botão de envio no topo e "+" ambíguo falham em teste (9B, 4 iOS rules to break). O Liquid Glass, o Dynamic Type e os SF Symbols são nativos e no PWA valem só como referência visual (9A).

---

## 4. UX avançado

Detalhes: `9B` (17 artigos NN/g, top 15 e lacunas), `ux-patterns` (leis e checklists).

- **Onboarding:** evitar o instrucional. Usar dica em contexto e empty state que ensina. Onboarding só quando faltam dados para começar, com "Pular" visível, um conceito por card e sem escolha de tema (9B).
- **Empty states:** dizem o estado do sistema, ensinam a função e trazem um botão para a primeira tarefa. Nunca mostrar "Sem registros" enquanto carrega (9B).
- **Formulários:** coluna única, sem placeholder no lugar de rótulo, marcação "(opcional)", tempo estimado e progresso. Validar só depois que o campo for concluído, com o erro ao lado do campo e cor mais ícone. Oferecer ajuda extra depois de 3 erros repetidos (9B). Rótulo a 8 px do campo e a 24 px do próximo (`ux-patterns`, Proximity).
- **Permissões:** pedir no contexto, dar o motivo ("…para que você possa [benefício]") e permitir reverter com um link para os ajustes. Dar um motivo aumentou o aceite em 12%, e o melhor texto rendeu 81% a mais que o pior (9B).
- **Confiança:** seguir a hierarquia de 5 níveis de compromisso. Não pedir dado sensível nem conta conectada antes de entregar valor (9B).
- **Agenda e fuso:** detectar o fuso automaticamente, buscar por cidade e ordenar alfabeticamente por cidade com o offset ao lado. 73% conhecem o próprio fuso e só 34% sabem o offset em UTC (9B).
- **Tabelas no painel:** primeira coluna identificável, cabeçalho fixo, edição em painel lateral não modal e ações em lote (9B, `desktop-app-ui` §4). Linha de 32–36 px compacta ou 44–48 px confortável.
- **Dashboards:** barras e linhas. Evitar pizza, donut, gauge e treemap em painel de leitura rápida, e nunca usar só a cor como sinal (9B). **Conflito:** o `dashboard-ui` usa gauge e anel como "progresso como linguagem". **Decisão (D4):** no painel operacional do gestor, sem gauge nem anel (barras e linhas); no painel e no app do cliente, só anel de meta com o número visível, no máximo 1–2 por tela, pelo critério do `dashboard-ui` padrão 17.
- **Tabs:** separar navegação de abas internas, usar pelo menos 2 indicadores de seleção e preferir acordeão a tabs no mobile para conteúdo longo (9B).
- **Métricas de UX:** CASTLE para o painel do gestor (ferramenta de trabalho) e HEART para o app do cliente (9B).
- **Leis com número** (`ux-patterns`): Doherty ≤ 400 ms de feedback. Hick: poucos itens visíveis e o resto em "Mais". Von Restorff: um destaque, nunca três. Goal gradient: o progresso não começa do zero.

---

## 5. Motion

Detalhes: `9A` (Apple, Material, Carbon), `9D` (Motion for React, Atlassian, Fluent, tabela comparativa), `9E` (@motion_ui_interface, @theglidestudio), skill `ui-motion`.

- **A Apple não dá números**, só princípios: propósito, motion opcional, seguir o gesto, ser breve e deixar cancelar. O Reduce Motion pede springs mais firmes, fade no lugar de x/y/z e nada de blur animado (9A).
- **Os números do projeto vêm do `ui-motion`:** press em 0,95 com feedback em 0 ms e 160 ms de duração; stagger de 70/100 ms; expandir em 350 ms ease-out; sucesso em 470 ms; reveal ≤ 700 ms; spring de UI com damping ratio 0,8; toast com stiffness 180 e damping 20; pull-to-refresh a 0,35.
- **Referências externas para calibrar:** Carbon tem 70, 110, 150, 240, 400 e 700 ms, com microinteração de 90–120 ms. A Atlassian põe abaixo de 150 ms o que dispara dezenas de vezes por dia e entre 150 e 400 ms as transições. O Material converte springs para a web (Expressive default spatial `cubic-bezier(0.38, 1.21, 0.22, 1.00)` em 500 ms; effects em 150, 200 e 300 ms) (9A, 9D).
- **Motion for React:** exige React 18.2+. Por padrão usa spring em x/scale e tween de 0,3 s em opacity. **`MotionConfig reducedMotion` tem padrão `"never"` e precisa ser configurado como `"user"`** (9D).
- **Regras de quantidade:** um momento animado por tela; o feedback funcional não conta (`ui-motion` regra 17). O que o usuário nota com frequência é candidato a remoção (Carbon, 9A).
- **Performance:** animar só `transform` e `opacity`. O orçamento é de 16,7 ms por quadro a 60 fps e 8 ms a 120 fps (9D). Animar variável CSS não tem aceleração de hardware.

---

## 6. Inspiração e benchmarking (e como adaptar sem copiar)

Detalhes: `docs/achados/rodada-9C.md`.

| Fonte | Status | Para quê |
|---|---|---|
| Mobbin | 🔒 só a home é pública | Teria fluxos iOS reais (agenda, mensagens, onboarding). **Lacuna principal** |
| Dribbble | ⚠️ anti-bot depois de ~20 shots | Dashboard de criador (Kreya, Blenz), proposta (Invoice/Proposal Creator), app de marca (Erudite07) |
| Behance | ✅ | Cases completos: Nomey (monetização, 227 apreciações), Reelful (405), Cook (23, pouco validado) |
| Awwwards, Land-book, SiteInspire | ✅ | Perfil público e portfólio (hero, tipografia), não telas de app |
| Coolors | ✅ | Contraste WCAG nos tokens claro e escuro |
| Typewolf | ✅ | "40 Best Google Fonts" (open source, uso comercial). Os pares não foram extraídos |

**Como adaptar sem copiar** (regras para o time):
1. **Extraia o padrão, não o pixel.** Anote o que o shot resolve (hierarquia de KPIs, ordem do fluxo, posição do CTA) e redesenhe com os tokens próprios (seção 13). Layout, ilustração e paleta do autor nunca entram.
2. **Valide contra uma regra.** Toda ideia tirada de um shot precisa passar no checklist da seção 14. Shots não mostram estados de vazio, erro ou carregamento (9C, "Riscos").
3. **Junte 3 referências por padrão**, de autores diferentes, e fique só com o que se repete.
4. **Prefira telas reais a conceitos.** Mobbin (quando houver acesso) e apps em produção valem mais que Dribbble e Behance, que são conceito sem prova de uso (9C).
5. **Inspiração iOS sem copiar a Apple:** pegue o comportamento (sheet com detents, tab bar sempre visível, large title que colapsa) e coloque cor, tipografia e ícones próprios. Não use SF Symbols nem assets do kit da Apple no produto: a licença restringe esses assets a mockup (9D, kits Figma).
6. **Registre a origem** de cada referência numa planilha (URL, data, padrão extraído) para auditar a originalidade depois.

---

## 7. Instagram: top 15 (resumo)

Detalhes: `docs/achados/rodada-9E.md`. São 29 perfis ativos verificados; 10 dos 13 iniciais estavam inativos ou indisponíveis. A lista completa com motivo está na seção 15c.

- Os mais úteis ensinam **regras numéricas em Reels curtos**: @motion_ui_interface, @theglidestudio e @designmotionhq.
- Os grandes perfis (@dailywebdesign, @uidesignpatterns, @showcase_ui) são só curadoria visual.
- **Risco recorrente:** isca de lead ("comente X") e promoção de curso, plugin ou template. Vários efeitos de motion vêm de vídeo ou After Effects e não se traduzem para React DOM com boa performance (9E).
- Em PT, o @felvrabr está ativo, mas a amostra trouxe só legendas comerciais.

---

## 8. Facebook: top 5 (resumo)

Detalhes: `docs/achados/rodada-9F.md`, Parte 1. Os grupos são grandes e dominados por autopromoção. Vale filtrar ("Featured", busca interna) em vez de rolar o feed. O top 5 está na seção 15d. Atenção: a página "NN" no Facebook é uma seguradora, não o Nielsen Norman Group.

---

## 9. YouTube: top 10 (resumo)

Detalhes: `9F`, Parte 2. São 15 canais ativos (último vídeo há no máximo 4 meses). O canal oficial do Ionic está parado há 2 anos; a fonte viva de Ionic é o Ionic Forum. Em PT, o único canal ativo de UX/UI encontrado é o Hericky Alencar. Os links de vídeos individuais **não foram capturados**: use a aba /videos de cada canal. O top 10 está na seção 15e.

---

## 10. Newsletters e comunidades (resumo)

Detalhes: `9F`, Parte 3. Foram verificadas 10 de uma meta de 15.

| # | Nome | Tipo | Uso |
|---|---|---|---|
| 1 | Smashing Magazine | blog + newsletter | Acessibilidade, UX, CSS, React |
| 2 | Figma Forum | comunidade | Figma e design systems |
| 3 | Ionic Forum | comunidade | Capacitor: safe area, iOS, edge-to-edge |
| 4 | Frontend Focus | newsletter semanal | Radar de CSS e browsers |
| 5 | React Status | newsletter semanal | Radar de React (filtrar React Native) |
| 6 | Josh W. Comeau | blog + cursos | CSS, React, animação |
| 7 | Codrops | blog | Motion na web |
| 8 | Accessibility Weekly | newsletter | A11y (data da última edição não verificada) |
| 9 | Reactiflux | Discord | React (75.181 membros, segundo o site) |
| 10 | WebAIM Discussion List | lista de e-mail | A11y (atividade atual não verificada) |

**Lacunas:** faltam uma newsletter de UX verificada (a página de newsletters do NN/g deu 404), uma comunidade de motion de UI e qualquer newsletter ou comunidade de UX em PT-BR.

---

## 11. Ferramentas (resumo de 9D, Parte 2)

Detalhes: `docs/achados/rodada-9D.md`, Partes 1 e 2. "Capacitor = inferido" quer dizer que a lib web em React DOM roda no WebView, mas a doc não confirma.

| Ferramenta | Licença / preço | React 18? | Papel no app | Decisão |
|---|---|---|---|---|
| [shadcn/ui](https://ui.shadcn.com/docs/components) | MIT | Sim (Tailwind v3 + React 18 seguem funcionando) | Base de componentes: Drawer com snap, Toast com Undo, Field, Calendar, Data Table, Bubble/Message, Empty, Skeleton | **Usar** (variante Base UI) |
| [Motion for React](https://motion.dev/docs/react) | MIT; Motion+ pago | Sim (18.2+) | Springs, drag, `layoutId`, `AnimatePresence` | **Usar** com `reducedMotion="user"` |
| [Tailwind CSS](https://tailwindcss.com) | MIT | n/a | Tokens via CSS vars | **Usar**. Se migrar para v4, o piso é Safari 16.4+ e Chrome 111+ |
| [Radix Primitives](https://www.radix-ui.com/primitives/docs/overview/introduction) | MIT | Sim | Variante Radix do shadcn | Só se ficar na variante Radix |
| [React Aria](https://react-aria.adobe.com) | Apache-2.0 | Sim | i18n PT/EN, date pickers | Opcional para datas e i18n |
| [Headless UI](https://headlessui.com) | MIT | Sim | — | Redundante com shadcn |
| [Mantine](https://mantine.dev/getting-started/) | MIT | **Não** (v9 exige 19.2+) | — | Fora |
| [HeroUI](https://www.heroui.com/docs/guide/installation) | Apache-2.0 | **Não** (v3 exige 19+ e Tailwind v4) | — | Fora |
| [Ionic React](https://ionicframework.com/docs/react) | MIT | Sim (política de suporte não lida) | Modo `ios` automático, transições nativas | **Plano B** do Capacitor |
| [Framework7](https://framework7.io/react/) | MIT | Sim | Estilo iOS 26 pronto | Só referência ou protótipo |
| [Ant Design Mobile](https://mobile.ant.design) | MIT | Sim | — | Estética distante do iOS |
| Vant | MIT | React só de comunidade | — | Fora |
| [GSAP](https://gsap.com/licensing/) | Grátis com licença própria (não MIT) | Sim | Narrativa de marketing | Só na landing, se precisar |
| Lottie (lottie-web / dotLottie) | MIT | Sim | Ilustração de onboarding, vazio, sucesso | Opcional (fase 3) |
| [Rive](https://rive.app/pricing) | Editor freemium; runtimes MIT; o plano grátis exporta com splash | Sim (pacote React não verificado) | Ilustração interativa | Opcional |
| [Capacitor](https://capacitorjs.com/docs) | MIT (v8) | Sim | Runtime nativo, Haptics | Fase 2 do mobile |
| [Supabase Library](https://supabase.com/library/docs/getting-started/introduction) | Open source (licença exata não verificada) | Sim (registry shadcn) | Auth, upload, realtime, chat | Avaliar blocks (focados em Next.js) |
| [Figma](https://www.figma.com/pricing/) | Starter grátis; Professional US$ 16 full | n/a | Design | Usar com os kits iOS 27, M3 e Obra shadcn |
| [Tokens Studio](https://tokens.studio/pricing) | Grátis para 1 projeto | n/a | Tokens multi-tema | Só se houver tema por cliente em escala |
| Storybook | MIT | Sim | Documentar a camada iOS | A partir de ~10 componentes próprios |
| [Chromatic](https://www.chromatic.com/pricing) | Free: 5.000 snapshots | n/a | Regressão visual | Opcional |
| Lighthouse | Apache-2.0 | n/a | Auditoria de PWA e performance | **CI do PWA** |
| axe-core / [axe DevTools](https://www.deque.com/axe/devtools/pricing/) | MPL-2.0; extensão grátis | n/a | A11y automatizada | **Testes** |
| [Stark](https://www.getstark.co/pricing/) | Pago | n/a | Contraste no Figma | Só depois de plugin grátis |
| [shadcn.io](https://www.shadcn.io/ui) | **Terceiro comercial, não oficial**; o Individual é só para uso pessoal | — | Inspiração | Não depender dele |
| [LottieFiles Motion System](https://lottiefiles.com/motion-system) | Pago (Team+/Enterprise) | n/a | Governança de motion de ilustração | Não agora |

**Do diretório [shadcn.io/awesome](https://www.shadcn.io/awesome/components)** (só a descrição foi lida; confira licença e atividade antes): Credenza/DropDrawer (dialog no desktop e drawer no mobile), Tour Kit (onboarding), Event Calendar/Planner (agenda), shadcn-chat (mensagens), Kanban Board (pipeline de propostas), React Wheel Picker.

---

## 12. Design systems e motion systems (resumo de 9D, Parte 3)

São 11 sistemas avaliados. As durações aparecem só onde a página trouxe número.

| Sistema | Durações | Easing de referência | Reduced motion | Para o app |
|---|---|---|---|---|
| [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/motion) | não especificado | não especificado | Detalhado (9A) | **Alta**: comportamento e acessibilidade |
| [Material 3](https://m3.material.io/styles/motion/easing-and-duration/tokens-specs) | Legado com 16 tokens de 50 a 1000 ms; springs na web de 150 a 750 ms | standard `0.2, 0, 0, 1`; Expressive default spatial `0.38, 1.21, 0.22, 1.00` em 500 ms | não lido | **Alta**: números para web e divisão spatial × effects |
| [IBM Carbon](https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview) | 70, 110, 150, 240, 400, 700 ms | productive `0.2, 0, 0.38, 0.9`; expressive `0.4, 0.14, 0.3, 1` | alternativas estáticas | **Alta**: painel web |
| [Atlassian](https://atlassian.design/foundations/motion) | 50–150 ms (interação); 150–400 ms (transição); modal em 250 ms | ease-out bold `0, 0.4, 0, 1`; saída `0.6, 0, 0.8, 0.6` | motion desligado | **Alta**: regra de frequência |
| [Fluent 2](https://fluent2.microsoft.design/motion) | não especificado | não especificado | modo "sem motion" | Média: princípios |
| [Primer](https://primer.style/product/primitives/) | sem página de motion | — | — | Média: nomes de tokens e dark mode |
| [Lightning DS 2](https://www.lightningdesignsystem.com/) | sem motion | — | — | Média/baixa: doc de a11y por componente |
| [Radix Themes](https://www.radix-ui.com/themes/docs/overview/getting-started) | não especificado | — | — | Média: escala de cor e radius |
| [Ant Design](https://ant.design/docs/spec/motion) | tokens sem valores padrão | nomes de curvas | — | Baixa/média |
| Shopify Polaris | página de motion não existe mais (redirect) | — | — | Baixa |
| LottieFiles Motion System | — | curvas Lottie | — | Baixa agora |
| Motion (lib) | tween de 300 ms padrão; spring com bounce de 0,25 | spring em x/scale | **padrão "never"** | Implementação |

**Leitura:** a Apple dá o comportamento, o `ui-motion` dá os números principais, Carbon e Atlassian definem o painel web produtivo e a regra de frequência, e o Material dá as curvas de spring para CSS.

---

## 13. Recomendação em 3 fases

**Decisões do usuário (D1–D8), aprovadas em 23/11/2026:**
- **D1 Tipografia do app:** escala 16 × 1,2ⁿ com corpo 16, igual ao painel; botões em 16 ou 19 px. O corpo 17 pt do iOS fica só como referência do nativo (1.5).
- **D2 Latência × animação:** "feedback em 100 ms, concluído em 300 ms" é prazo de resposta do sistema, não duração de animação; a animação do press segue o `ui-motion` (feedback visual em 0 ms, press 160 ms) (Loading).
- **D3 Motion do painel web:** os mesmos tokens do `ui-motion`; onde ele não define, micro = 80 ms (`transitions-dev`). Carbon productive só como referência comparativa (1.3–1.4).
- **D4 Gauges e anéis:** proibidos no painel operacional do gestor (barras e linhas); no painel/app do cliente, só anel de meta com o número visível, no máximo 1–2 por tela (`dashboard-ui` padrão 17) (seção 4).
- **D5 Tab bar:** 5 abas como hipótese a validar em teste de usuários antes de fechar (1.12).
- **D6 Tema:** app do cliente segue o tema do sistema, sem seletor; painel web com seletor Claro/Escuro/Sistema (1.10).
- **D7 Personalização por cliente:** nenhuma no piloto; depois, só a cor de acento, com contraste ≥ 4,5:1 validado automaticamente (Fase 3).
- **D8 Medida de linha:** token `--measure: 50ch` (≈ 66–71 caracteres); regra em caracteres: 45–75, e 45–60 em formulários (seção 2, item 7).

### Fase 1: Fundações (tokens, shell, acessibilidade de base)

| # | Decisão concreta | Números | Fonte |
|---|---|---|---|
| 1.1 | Stack de UI: shadcn/ui com **uma** base (Base UI), Motion e uma camada `ios/` própria | React 18; Mantine e HeroUI fora | 9D Parte 4 |
| 1.2 | `<MotionConfig reducedMotion="user" transition={…}>` na raiz | sobrescreve o tween padrão de 0,3 s | 9D |
| 1.3 | Tokens de motion em CSS vars e Tailwind: `--press-scale .95`, `--dur-press 160ms` (feedback em 0 ms), micro de **80 ms** (`transitions-dev`) onde o `ui-motion` não define (D3), `--dur-expand 350ms` ease-out, `--dur-success 470ms`, `--dur-reveal ≤700ms`, `--stagger 70/100ms`; spring UI com damping ratio 0,8; toast com stiffness 180 / damping 20; saída mais curta que a entrada | ver à esquerda | `ui-motion`; 9D (Atlassian < 150 ms para o frequente; saídas mais curtas) |
| 1.4 | Curvas: ease-out `cubic-bezier(0.22, 1, 0.36, 1)` (`ui-motion`) no app **e** no painel web, com os mesmos tokens (D3). Carbon productive `0.2, 0, 0.38, 0.9` fica só como referência comparativa. Spring em CSS: M3 Expressive default spatial `0.38, 1.21, 0.22, 1.00` em 500 ms só sem interrupção | — | `ui-motion`, 9A, 9D |
| 1.5 | Tipografia: escala 16 × 1,2ⁿ no app e no painel; corpo 16; labels do painel 13–14; botão primário em 16 ou 19 semibold (D1; o corpo 17 pt do iOS é só referência do nativo); perfil público em Major Third 1,25 | lh 1,5 → 1,1; tracking −0,02em | `ux-patterns`, `desktop-app-ui` §3, `website-ui` |
| 1.6 | Fonte: 1 família com 2 pesos (no máximo 2–3 famílias), open source, com acentos PT verificados | Typewolf "40 Best Google Fonts" | `design-direction` regra 16, `ux-patterns` (anti AI slop), 9C |
| 1.7 | Alvos: `--tap: 44px` como piso no PWA e 48 no botão primário; `--tap-gap: 8px`; crescer por padding (20 + 12 + 12) | web desktop: piso de 24 e meta de 44 | 9A, `ux-patterns`, `mobile-app-ui` §1 |
| 1.8 | Breakpoints do Tailwind: base 375; 768 (tablet: rail); 1024 (desktop: sidebar vira rail, inspector em overlay); 1280 (sidebar larga de 220–260); 1440 (inspector fixo de 320–400); 1920 (limitar a medida do texto) | M3: barra < 600 e rail a partir de 840 | `desktop-app-ui` §1–2, `website-ui`, 9A |
| 1.9 | Cor: 2 bases + 1 acento em 60/30/10 (acento ≤ 10%); rampa de 5–6 tons por base; papéis semânticos claro, escuro e alto contraste | texto 4,5:1; UI 3:1 | `design-direction` 1, 13, 14; 9A |
| 1.10 | Dark mode: `#0C1424` em vez de `#000`, texto a 87%, segue o sistema. **Conflito (resolvido):** a Apple pede para não ter seletor próprio no app nativo; versões anteriores de `mobile-app-ui`/`desktop-app-ui` sugeriam troca manual, e hoje as duas já seguem esta regra (§14 e §11). **Decisão (D6):** o app do cliente segue o tema do sistema, sem seletor; o painel web tem seletor Claro/Escuro/Sistema | — | 9A, `mobile-app-ui` §14, `desktop-app-ui` §11 |
| 1.11 | Sombras: separar blocos por espaço ou fundo; sombra tingida só no que flutua (Y 8, blur 16, ~8%) | — | `design-direction` 15, regra de prioridade |
| 1.12 | Shell do app: tab bar com 5 abas como **hipótese a validar em teste** de usuários (árvore/primeiro clique) antes de fechar (D5): Início, Agenda, Conteúdo, Mensagens, Perfil (propostas, contratos, portfólio e networking entram em Perfil ou na Início). Sem aba "More" | 3–5 abas | 9A, 9B (hipótese a validar em teste), `mobile-app-ui` §3 |
| 1.13 | Shell web: sidebar larga 220–260 ↔ rail 56–64 com tooltip; topbar com 1 CTA e ⌘K | ⌘K abre em 150 ms | `desktop-app-ui` §1, §6 |
| 1.14 | Safe areas e Drawer no iOS: `env(safe-area-inset-bottom)` no rodapé fixo; `body { position: relative }` | — | `mobile-app-ui` §5, 9D |
| 1.15 | Qualidade no CI: Lighthouse (PWA e performance) e axe-core nos testes; Playwright nas viewports 360, 375, 390, 768, 1280 e 1440 | LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 (complemento da skill) | 9D, `website-ui`, `mobile-app-ui` |
| 1.16 | i18n PT/EN desde os tokens: rótulos que aguentam texto mais longo; teste de "texto longo" | — | `design-direction` 17 |

### Fase 2: Fluxos críticos

| Fluxo | Decisão concreta | Números | Fonte |
|---|---|---|---|
| **Onboarding** | Convite → perfil mínimo (só os dados necessários, explicando o porquê, com progresso e "Pular"). Sem tour em cards e sem escolha de tema. Dicas em contexto depois. Login com "mostrar senha", sem campo duplicado e com OTP (`autocomplete="one-time-code"`) | progresso que não começa do zero | 9B (onboarding, login, hierarquia de confiança), `ux-patterns` Goal gradient, `mobile-app-ui` §9 |
| **Perfil** | Seções em acordeão no mobile e tabs internas no web, com 2 indicadores de seleção. Large title de 34 → 18 px ligado ao scroll | 34 → 18 px | 9B Tabs, `mobile-app-ui` §6 |
| **Portfólio** | Grade de cards no estilo feed canônico do M3 com filtros em chips. Card → detalhe com `layoutId` (o card vira a página). Upload que retoma de onde parou. Permissão de câmera e fotos só no toque | expand em 350 ms | 9A (prints canônicos), 9D (`layoutId`), `ui-motion` regra 11, 9B |
| **Agenda** | Calendar/Date Picker do shadcn, fuso detectado com busca por cidade, escolha de horário no Drawer com CTA fixo, slots com alvo de ≥ 44 px | 44 px; ordenar por cidade | 9D (print do Drawer), 9B Time-zone, 9A |
| **Propostas e contratos** | Formulário em coluna única com rodapé fixo (total + primário, valor do botão = total), verbo + objeto ("Enviar proposta"). Confirmação dupla em ação irreversível (assinar ou cancelar). No painel web: tabela com inspector lateral não modal e Kanban de pipeline | botão de 48 px | 9B (formulários, tabelas, 4 iOS rules), `ux-patterns` (fluxo de pedido), 9A (Assistive Access) |
| **Mensagens** | Bubble/Message/Message Scroller do shadcn. Suas mensagens de um lado; 4 px dentro de uma sequência e 18 px entre pessoas; "Lido" só na última; typing em 240 ms | 4/18 px, 240 ms | 9D, `ux-patterns` Chat |
| **Configurações** | Escopo em cada linha, uma linha de consequência, confirmação do save, reset do que não é padrão e "quando vale" | — | `ux-patterns` Settings |
| **Empty states** | Estado do sistema + o que fazer + botão para a 1ª tarefa (componente Empty). A home nunca abre vazia | — | 9B, 9D, `mobile-app-ui` §10 |
| **Erros** | Inline depois do blur, ao lado do campo, com cor e ícone; ajuda depois de 3 erros. Toast de erro fica até ser reconhecido. Offline: banner persistente e ações "pendentes" | erro até reconhecer | 9B, `ui-motion` (toast), `mobile-app-ui` §10 |
| **Loading** | Título no 1º paint; skeleton para conteúdo sem layout shift; spinner só abaixo de 3 s; loader dentro do botão (mantém a largura e ignora o 2º clique); UI otimista com reversão | feedback ≤ 400 ms; latência do botão: resposta ≤ 100 ms e estado final ou spinner ≤ 300 ms (D2); a animação do press segue os tokens (feedback em 0 ms, 160 ms) | `mobile-app-ui` §10, `ux-patterns` |
| **Resultados (dashboard)** | 1 KPI principal + 3 secundários, período nomeado, dígitos tabulares, barra e linha; cor do delta pelo sentido bom ou ruim | 3–6 KPIs na faixa | `ux-patterns` anti-slop, `dashboard-ui` 3 e 11, 9B |

### Fase 3: Diferenciação

| Tema | Decisão concreta | Números | Fonte |
|---|---|---|---|
| **Identidade** | Acento só no CTA, no indicador-chave e na aba ativa. Cantos concêntricos (raio interno = externo − padding, ex.: 36 − 12 = 24). Traço de ícone casado com o peso do texto. Uma grade de ícones só | acento ≤ 10% | `design-direction`, 9E (@motion_ui_interface) |
| **Motion system** | Documentar os tokens da fase 1 por evento (duração + easing + propriedade, como `motion.sheet.enter`). Regra de frequência: o frequente fica abaixo de 150 ms e o de uma vez por sessão pode ser expressivo | < 150 ms para o frequente | 9D (Atlassian), `ui-motion` |
| **Microinterações** | Press a 0,95 no touchdown; botão copiar → check; ícone que morfa (300–400 ms); sucesso em 470 ms; segurar para confirmar em ações irreversíveis | ver à esquerda | `ui-motion`, 9E |
| **Transições** | Push/pop com swipe-back (Motion `drag="x"` + `AnimatePresence`); card → página; pílula ativa desliza em 250–350 ms; sheet com snap | 250–350 ms | 9D Parte 4, `ui-motion`, `desktop-app-ui` §9 |
| **Gestos** | Swipe actions em listas (`onDragEnd` com `info.velocity`), pull-to-refresh com dedo 100% e lista 35%, rubber band de 200 → 86 px, sempre com alternativa visível | 0,35; 200 → 86 | 9D, `ui-motion`, 9A |
| **Animação de dados** | Animar só a mudança (números rolando, barra que redimensiona), não o card inteiro; stagger de 100 ms em dígitos | 100 ms | 9E (@noahelhadedy), `ui-motion` |
| **Personalização** | **Decisão (D7):** nenhum tema por cliente no piloto. Na fase seguinte, só a cor de acento (CSS var), validada automaticamente em contraste ≥ 4,5:1 nos dois temas antes de salvar. Personalização de conteúdo sim; de tema no onboarding não | 4,5:1 | 9B, 9C (Coolors), `design-direction` |
| **Vidro** | Só sobre conteúdo (blur de 30 px atrás da tab bar), com fallback em `prefers-reduced-transparency` | blur 30 px | `mobile-app-ui` §14, `dashboard-ui` |
| **Performance** | Só `transform` e `opacity`; `filter: drop-shadow` em vez de animar `boxShadow`; listas virtualizadas; imagens WebP/AVIF; teste em celular médio e rede lenta | 16,7 ms por quadro | 9D, `mobile-app-ui` §13 |
| **Acessibilidade** | Reduced motion troca deslocamento por fade ≤ 150 ms; texto a 200%; foco visível; labels em botões de ícone; teste com 5 usuários, incluindo baixa visão e motora | ≤ 150 ms; 200% | `ui-motion` 13, 9A, 9B |

---

## 14. Checklist de auditoria (56 itens, sim/não)

**UI (5)**
1. [ ] Há uma escala tipográfica só por superfície (16 × 1,2 no app e no painel; 1,25 no site)?
2. [ ] Nenhum texto usa Ultralight, Thin ou Light, nem fica abaixo de 11 px?
3. [ ] O acento ocupa ≤ 10% da tela e aparece só no CTA, no indicador-chave ou na aba ativa?
4. [ ] Há um único botão primário por tela, com label verbo + objeto?
5. [ ] A sombra fica só em elementos que flutuam (tingida, blur = 2× Y)?

**Layout (5)**
6. [ ] O espaçamento segue a grade de 8 (4 só em micro), sem valores como 13 ou 27 px?
7. [ ] O texto corrido fica em 45–75 caracteres (45–60 em formulários), com `--measure: 50ch` (D8)?
8. [ ] Não há scroll horizontal em 320/375 px?
9. [ ] Em ≥ 1024 px o shell usa sidebar 220–260 ou rail 56–64; entre 840 e 1023 px, rail + 1 painel (`desktop-app-ui` §2); abaixo de 840 px, `mobile-app-ui`?
10. [ ] O conteúdo nunca fica sob notch, Dynamic Island ou home indicator?

**UX (5)**
11. [ ] O feedback de toda ação aparece em ≤ 400 ms?
12. [ ] Formulários em coluna única, com rótulo visível (sem placeholder no lugar) e "(opcional)" marcado?
13. [ ] A validação acontece só depois que o campo é concluído, com o erro ao lado do campo?
14. [ ] As tabs de navegação não se misturam com as tabs internas, e a seleção tem 2 indicadores?
15. [ ] O back restaura o scroll e a linha onde o usuário estava?

**Acessibilidade (5)**
16. [ ] O contraste de texto é ≥ 4,5:1, e o de ícones, bordas e texto grande ≥ 3:1, nos dois temas?
17. [ ] O layout funciona com texto a 200% sem truncar?
18. [ ] O foco fica visível em todo controle (sem `outline: none`)?
19. [ ] A cor nunca é o único sinal (sempre há ícone, forma ou texto)?
20. [ ] Há landmarks, um só H1 e botões de ícone com label acessível?

**Mobile (5)**
21. [ ] Todo alvo mede ≥ 44 px (medido com `getBoundingClientRect`) e tem ≥ 8 px entre alvos?
22. [ ] A tab bar tem 3–5 seções, ícone + rótulo, nunca ações e nenhuma aba desabilitada?
23. [ ] A ação principal fica no rodapé, acima da safe area e do teclado?
24. [ ] Cada campo tem o `inputmode` e o `autocomplete` corretos?
25. [ ] Todo gesto (swipe, long press, pull) tem uma alternativa visível?

**Performance (4)**
26. [ ] LCP ≤ 2,5 s, INP ≤ 200 ms e CLS ≤ 0,1 em mobile com throttling?
27. [ ] O Lighthouse roda no CI do PWA sem regressão?
28. [ ] Listas longas são virtualizadas e as imagens são WebP/AVIF com lazy abaixo da dobra?
29. [ ] O app foi testado em celular médio com rede lenta?

**Animações (6)**
30. [ ] `<MotionConfig reducedMotion="user">` está na raiz?
31. [ ] Com reduced motion ativo, deslocamento e escala viram fade ≤ 150 ms, sem blur animado?
32. [ ] Só se animam `transform` e `opacity` (sem width, height ou top em listas)?
33. [ ] As durações vêm dos tokens (press 160, expand 350, sucesso 470, reveal ≤ 700), sem número solto no código?
34. [ ] Toda animação é interrompível e inverte a partir do estado atual?
35. [ ] Há no máximo 1 momento animado por tela, sem contar o feedback funcional?

**Consistência (4)**
36. [ ] Os componentes vêm de uma só base do shadcn (Base UI), sem misturar com Radix ou React Aria?
37. [ ] Cores, espaços e motion saem só de tokens (CSS vars e Tailwind)?
38. [ ] O mesmo componente se comporta igual no PWA e no painel (sheet ↔ menu e barra ↔ rail são equivalentes funcionais)?
39. [ ] A camada iOS própria está documentada (Storybook a partir de ~10 componentes)?

**Estados de interface (5)**
40. [ ] Cada tela tem os estados vazio, carregando, erro, texto longo e offline desenhados?
41. [ ] O empty state diz o estado, ensina e oferece um botão para a 1ª tarefa?
42. [ ] O skeleton não causa layout shift e o spinner só aparece em esperas abaixo de 3 s?
43. [ ] O loading do botão mantém a largura e ignora o 2º clique?
44. [ ] Toasts: no máximo 3, no topo no mobile e embaixo à direita no desktop, com info 4 s, warning 7 s e erro até reconhecer?

**Onboarding (4)**
45. [ ] Não há tutorial em cards obrigatório, e "Pular" fica visível onde houver passos?
46. [ ] Só se pedem os dados necessários para começar, cada um com o motivo?
47. [ ] Cada permissão é pedida no contexto, com o benefício explicado e um caminho para reverter?
48. [ ] O fuso é detectado automaticamente e editável, com busca por cidade?

**Conversão (4)**
49. [ ] O CTA de proposta ou contrato fica fixo no rodapé, e o valor do botão bate com o total?
50. [ ] As ações opostas de uma decisão (aceitar/recusar) têm o mesmo peso visual?
51. [ ] O progresso das etapas aparece nomeado e é igual na lista e no detalhe?
52. [ ] Não há dark patterns (X falso, nagging sem "não", cobrança sem aviso, social proof falso)?

**Confiança e credibilidade (4)**
53. [ ] Nenhum dado sensível (financeiro, documento, conta conectada) é pedido antes de o usuário ver valor?
54. [ ] Ações irreversíveis (assinar, excluir, cancelar contrato) têm confirmação dupla ou "segurar para confirmar"?
55. [ ] Os números do dashboard são reais (sem placeholders "bonitos") e mostram o período?
56. [ ] Existe desfazer (Undo no toast) para ações destrutivas reversíveis?

---

## 15. Entregáveis

### (a) Tabela mestre de recursos

Prioridade: **A** = usar já (fases 1–2), **B** = consulta ou fase 3, **C** = marginal. Só entram recursos ✅ nas rodadas. O status ⚠️ aparece onde a rodada marcou ressalva.

| Categoria | Recurso | URL | Para quê | Prioridade |
|---|---|---|---|---|
| Fundação | Apple HIG (índice) | https://developer.apple.com/design/human-interface-guidelines/ | Ponto de entrada | B |
| Fundação | Apple HIG Motion | https://developer.apple.com/design/human-interface-guidelines/motion | Princípios de motion | A |
| Fundação | Apple HIG Accessibility | https://developer.apple.com/design/human-interface-guidelines/accessibility | Alvos, 200%, contraste, Reduce Motion | A |
| Fundação | Apple HIG Design principles | https://developer.apple.com/design/human-interface-guidelines/design-principles | Critérios de revisão | B |
| Fundação | Apple HIG Layout | https://developer.apple.com/design/human-interface-guidelines/layout | Size classes, safe areas | B |
| Fundação | Apple HIG Typography | https://developer.apple.com/design/human-interface-guidelines/typography | Pesos, tracking SF Pro | B |
| Fundação | Apple HIG Color | https://developer.apple.com/design/human-interface-guidelines/color | Papéis semânticos | B |
| Fundação | Apple HIG Dark Mode | https://developer.apple.com/design/human-interface-guidelines/dark-mode | 4,5:1 / 7:1, base × elevated | A |
| Fundação | Apple HIG Tab bars | https://developer.apple.com/design/human-interface-guidelines/tab-bars | Regras de tab bar | A |
| Fundação | Apple HIG Sheets | https://developer.apple.com/design/human-interface-guidelines/sheets | Detents, grabber | A |
| Fundação | M3 Motion how it works | https://m3.material.io/styles/motion/overview/how-it-works | Springs expressive × standard | B |
| Fundação | M3 Motion specs | https://m3.material.io/styles/motion/overview/specs | Springs → cubic-bezier para web | A |
| Fundação | M3 Easing/duration tokens | https://m3.material.io/styles/motion/easing-and-duration/tokens-specs | 16 tokens e curvas | A |
| Fundação | M3 Layout overview | https://m3.material.io/foundations/layout/layout-overview/overview | Adaptive design | B |
| Fundação | M3 Breakpoints | https://m3.material.io/foundations/layout/breakpoints/overview | 600/840/1200/1600 | A |
| Fundação | M3 Spacing | https://m3.material.io/foundations/layout/grids-spacing/spacing | Princípios de espaço | C |
| Fundação | M3 Type scale tokens | https://m3.material.io/styles/typography/type-scale-tokens | Major Second, base 14 | C |
| Fundação | M3 Accessibility designing | https://m3.material.io/foundations/designing/structure | Alvos de 48 dp, landmarks | B |
| Fundação | M3 Accessibility overview | https://m3.material.io/foundations/overview/principles | A11y | C |
| Fundação | M3 Canonical layouts | https://m3.material.io/foundations/layout/canonical-examples/overview | List-detail e feed (prints 9A) | B |
| Fundação | Carbon Motion | https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview | 6 durações e 6 curvas | A |
| Fundação | Carbon Accessibility | https://www.carbondesignsystem.com/building-blocks/foundations/accessibility/overview | A11y | C |
| Design system | Atlassian Motion | https://atlassian.design/foundations/motion | Regra de frequência | A |
| Design system | Atlassian Design tokens | https://atlassian.design/foundations/tokens/design-tokens | Nomes de tokens | B |
| Design system | Atlassian Accessibility | https://atlassian.design/foundations/accessibility | A11y | C |
| Design system | Fluent 2 Motion | https://fluent2.microsoft.design/motion | Acessible motion | B |
| Design system | Fluent 2 Design tokens | https://fluent2.microsoft.design/design-tokens | Tokens | C |
| Design system | Fluent 2 Accessibility | https://fluent2.microsoft.design/accessibility | A11y | C |
| Design system | Primer primitives | https://primer.style/product/primitives/ | Nomes de tokens, dark mode | B |
| Design system | Lightning DS 2 | https://www.lightningdesignsystem.com/ | A11y por componente | C |
| Design system | Radix Themes | https://www.radix-ui.com/themes/docs/overview/getting-started | Escala de cor e radius | C |
| Design system | Ant Design Motion | https://ant.design/docs/spec/motion | Nomes de tokens de motion | C |
| Design system | Ant Design theme | https://ant.design/docs/react/customize-theme | Tokens de tema | C |
| Design system | Shopify Polaris ⚠️ (redirect) | https://shopify.dev/docs/api/polaris | Fora de escopo | C |
| UX | NN/g Articles | https://www.nngroup.com/articles/ | Radar | B |
| UX | NN/g Mobile UX Study Guide | https://www.nngroup.com/articles/mobile-ux-study-guide/ | Trilha mobile | A |
| UX | NN/g Web UX Study Guide | https://www.nngroup.com/articles/web-ux-study-guide/ | Trilha web | B |
| UX | NN/g Topics | https://www.nngroup.com/topics/ | Índice | C |
| UX | NN/g Application Design | https://www.nngroup.com/topic/applications/ | Apps complexos | B |
| UX | NN/g Reports | https://www.nngroup.com/reports/ | Relatórios | C |
| UX | NN/g Reports grátis | https://www.nngroup.com/reports/free/ | Accessible Web Design (75 guidelines) | B |
| UX | NN/g Reports mobile/tablet | https://www.nngroup.com/reports/topic/mobile-and-tablet-design/ | Índice | C |
| UX | NN/g Reports applications | https://www.nngroup.com/reports/topic/applications/ | Índice | C |
| UX | NN/g Mobile UX report (US$ 298) | https://www.nngroup.com/reports/mobile-website-and-application-usability/ | 374 guidelines, PWA, skeleton | B |
| UX | NN/g Helping Users Make Decisions (US$ 49) | https://www.nngroup.com/reports/make-decisions/ | Escolha de pacotes | C |
| UX | NN/g Touch targets | https://www.nngroup.com/articles/touch-target-size/ | 1 cm × 1 cm | A |
| UX | NN/g Mobile navigation | https://www.nngroup.com/articles/mobile-navigation-patterns/ | Tab bar 4–5 | A |
| UX | NN/g 4 iOS rules to break | https://www.nngroup.com/articles/4-ios-rules-break/ | Limites do "iOS-like" | A |
| UX | NN/g Mobile onboarding | https://www.nngroup.com/articles/mobile-app-onboarding/ | Onboarding | A |
| UX | NN/g Empty states | https://www.nngroup.com/articles/empty-state-interface-design/ | Empty states | A |
| UX | NN/g Errors in forms | https://www.nngroup.com/articles/errors-forms-design-guidelines/ | Erros | A |
| UX | NN/g Dashboards | https://www.nngroup.com/articles/dashboards-preattentive/ | Gráficos | A |
| UX | NN/g Permission requests | https://www.nngroup.com/articles/permission-requests/ | Permissões (+12% / +81%) | A |
| UX | NN/g Visual treatments a11y | https://www.nngroup.com/articles/visual-treatments-accessibility/ | Contraste e foco | A |
| UX | NN/g CASTLE | https://www.nngroup.com/articles/castle-framework/ | Métricas do gestor | B |
| UX | NN/g 4 principles forms | https://www.nngroup.com/articles/4-principles-reduce-cognitive-load/ | Formulários | A |
| UX | NN/g Time-zone selectors | https://www.nngroup.com/articles/time-zone-selectors/ | Agenda | A |
| UX | NN/g Commitment levels | https://www.nngroup.com/articles/commitment-levels/ | Confiança | A |
| UX | NN/g 3 I's of microcopy | https://www.nngroup.com/articles/3-is-of-microcopy/ | Microcopy | B |
| UX | NN/g Data tables | https://www.nngroup.com/articles/data-tables/ | Tabelas do painel | A |
| UX | NN/g Registration/login checklist | https://www.nngroup.com/articles/checklist-registration-login/ | Login | B |
| UX | NN/g Tabs used right | https://www.nngroup.com/articles/tabs-used-right/ | Tabs | A |
| UX | NN/g Skeleton vs spinners 🔒 | https://www.nngroup.com/videos/skeleton-screens-vs-progress-bars-vs-spinners/ | Só o resumo público | C |
| Ferramenta | shadcn/ui componentes | https://ui.shadcn.com/docs/components | Base de UI | A |
| Ferramenta | shadcn/ui Drawer | https://ui.shadcn.com/docs/components/drawer | Bottom sheet com snap | A |
| Ferramenta | shadcn/ui Toast | https://ui.shadcn.com/docs/components/toast | Feedback e Undo | A |
| Ferramenta | shadcn/ui Vite | https://ui.shadcn.com/docs/installation/vite | Instalação | A |
| Ferramenta | shadcn/ui Tailwind v4 | https://ui.shadcn.com/docs/tailwind-v4 | Compatibilidade v3/React 18 | A |
| Ferramenta | shadcn/ui React 19 | https://ui.shadcn.com/docs/react-19 | Migração futura | B |
| Ferramenta | shadcn/ui Figma | https://ui.shadcn.com/docs/figma | Kits oficiais listados | B |
| Ferramenta | shadcn.io/ui ⚠️ (terceiro comercial) | https://www.shadcn.io/ui | Inspiração | C |
| Ferramenta | shadcn.io awesome | https://www.shadcn.io/awesome/components | Diretório (Credenza, Tour Kit…) | B |
| Ferramenta | Motion for React | https://motion.dev/docs/react | Motion | A |
| Ferramenta | Motion instalação | https://motion.dev/docs/react-installation | React 18.2+ | A |
| Ferramenta | Motion transitions | https://motion.dev/docs/react-transitions | Spring × tween | A |
| Ferramenta | Motion drag | https://motion.dev/docs/react-drag | Swipe e sheets | A |
| Ferramenta | Motion useReducedMotion | https://motion.dev/docs/react-use-reduced-motion | Reduced motion | A |
| Ferramenta | Motion MotionConfig | https://motion.dev/docs/react-motion-config | `reducedMotion="user"` | A |
| Ferramenta | Motion accessibility | https://motion.dev/docs/react-accessibility | A11y | A |
| Ferramenta | Motion performance | https://motion.dev/docs/performance | 16,7 ms / 8 ms | A |
| Ferramenta | Motion Framer | https://motion.dev/docs/framer | Só para landing em Framer | C |
| Ferramenta | Radix Primitives | https://www.radix-ui.com/primitives/docs/overview/introduction | Variante Radix | C |
| Ferramenta | Tailwind CSS | https://tailwindcss.com | Tokens | A |
| Ferramenta | Tailwind compatibilidade | https://tailwindcss.com/docs/compatibility | Safari 16.4+ na v4 | A |
| Ferramenta | Headless UI | https://headlessui.com | Redundante | C |
| Ferramenta | React Aria | https://react-aria.adobe.com | i18n e datas | B |
| Ferramenta | Mantine | https://mantine.dev/getting-started/ | Fora (React 19) | C |
| Ferramenta | Mantine 9.0 changelog | https://mantine.dev/changelog/9-0-0/ | Prova do requisito React 19.2 | C |
| Ferramenta | Mantine CSS Modules | https://mantine.dev/styles/css-modules/ | Estilo fora do Tailwind | C |
| Ferramenta | HeroUI | https://www.heroui.com/docs/guide/installation | Fora (React 19) | C |
| Ferramenta | Ionic React | https://ionicframework.com/docs/react | Plano B | B |
| Ferramenta | Ionic platform styles | https://ionicframework.com/docs/theming/platform-styles | Modo ios/md | B |
| Ferramenta | Framework7 | https://framework7.io | Referência iOS 26 | C |
| Ferramenta | Framework7 React | https://framework7.io/react/ | Referência | C |
| Ferramenta | Ant Design Mobile | https://mobile.ant.design | Fora | C |
| Ferramenta | Ant Design Mobile quick start | https://mobile.ant.design/guide/quick-start | Fora | C |
| Ferramenta | GSAP pricing | https://gsap.com/pricing/ | Licença | C |
| Ferramenta | GSAP licensing | https://gsap.com/licensing/ | "Standard No Charge" | C |
| Ferramenta | Rive pricing | https://rive.app/pricing | Ilustração interativa | C |
| Ferramenta | Figma pricing | https://www.figma.com/pricing/ | Custo | B |
| Ferramenta | Tokens Studio pricing | https://tokens.studio/pricing | Multi-tema | C |
| Ferramenta | Chromatic pricing | https://www.chromatic.com/pricing | Regressão visual | C |
| Ferramenta | Stark pricing | https://www.getstark.co/pricing/ | Contraste no Figma | C |
| Ferramenta | axe DevTools pricing | https://www.deque.com/axe/devtools/pricing/ | A11y | A |
| Ferramenta | Capacitor docs | https://capacitorjs.com/docs | Runtime | A |
| Ferramenta | Capacitor UI | https://capacitorjs.com/docs/getting-started/ui | Escolha de UI | A |
| Ferramenta | Supabase Library | https://supabase.com/library/docs/getting-started/introduction | Blocks de auth, upload, chat | B |
| Ferramenta | LottieFiles Motion System | https://lottiefiles.com/motion-system | Governança (pago) | C |
| Ferramenta | Lottie docs Motion System | https://docs.lottiefiles.com/en/creator/15_motion-system | Doc | C |
| Ferramenta | Lottie docs Easing | https://docs.lottiefiles.com/en/creator/07_animation/easing | Curvas | C |
| Ferramenta (repo) | shadcn-ui/ui | https://github.com/shadcn-ui/ui | MIT, 129 mil estrelas | B |
| Ferramenta (repo) | motiondivision/motion | https://github.com/motiondivision/motion | MIT | B |
| Ferramenta (repo) | ionic-team/capacitor | https://github.com/ionic-team/capacitor | MIT | B |
| Ferramenta (repo) | GoogleChrome/lighthouse | https://github.com/GoogleChrome/lighthouse | CI | A |
| Ferramenta (repo) | dequelabs/axe-core | https://github.com/dequelabs/axe-core | Testes de a11y | A |
| Ferramenta (repo) | storybookjs/storybook | https://github.com/storybookjs/storybook | Documentar componentes | B |
| Ferramenta (repo) | LottieFiles/dotlottie-web | https://github.com/LottieFiles/dotlottie-web | Player | C |
| Ferramenta (repo) | airbnb/lottie-web | https://github.com/airbnb/lottie-web | Player | C |
| Kit Figma | Apple iOS and iPadOS 27 | https://www.figma.com/community/file/1651309003795292092/ios-and-ipados-27 | Layout guides e safe areas (só mockup) | A |
| Kit Figma | Apple iOS and iPadOS 26 | https://www.figma.com/community/file/1527721578857867021/ios-and-ipados-26 | Componentes (só mockup) | B |
| Kit Figma | Material 3 Design Kit | https://www.figma.com/community/file/1035203688168086460/material-3-design-kit | Android, CC BY 4.0 | B |
| Kit Figma | Obra shadcn/ui Community Edition | https://www.figma.com/community/file/1514746685758799870/shadcn-ui-kit-community-edition | Kit da base, CC BY 4.0 | A |
| Kit Figma | CRM UI Kit for SaaS Dashboards | https://www.figma.com/community/file/1463555657173424575/crm-ui-kit-for-saas-dashboards | Painel do gestor, CC BY 4.0 | B |
| Inspiração | Mobbin 🔒 | https://mobbin.com | Fluxos iOS reais (exige login) | B |
| Inspiração | Dribbble tag UI/UX inspiration | https://dribbble.com/tags/ui-ux-inspiration | Tendência | C |
| Inspiração | Dribbble tag UI/UX design | https://dribbble.com/tags/ui-ux-design | Tendência | C |
| Inspiração | Dribbble Kreya | https://dribbble.com/shots/25294910-Kreya-Content-Creator-Dashboard | Resultados | B |
| Inspiração | Dribbble Blenz | https://dribbble.com/shots/26534678-Blenz-Influencer-Analytics-Dashboard-UI | Analytics por rede | B |
| Inspiração | Dribbble Invoice/Proposal Creator | https://dribbble.com/shots/25532738-Invoice-Proposal-Creator | Propostas | B |
| Inspiração | Dribbble Creator Brand & Content App | https://dribbble.com/shots/27744939-Creator-Brand-Content-Management-Mobile-App | Home mobile | B |
| Inspiração | Behance | https://www.behance.net | Cases completos | B |
| Inspiração | Behance Nomey | https://www.behance.net/gallery/254485187/Nomey-Creator-Monetization-Platform | Perfil do criador | B |
| Inspiração | Behance Cook | https://www.behance.net/gallery/258614563/Cook-%28-CreatorBrand-Deals-App-%29 | Propostas | C |
| Inspiração | Behance Reelful | https://www.behance.net/gallery/253975015/Reelful-AI-Powered-Social-Video-Creator-App-UIUX | Fluxo de conteúdo | C |
| Inspiração | Awwwards | https://www.awwwards.com | Portfólio público | B |
| Inspiração | Awwwards Portfolio | https://www.awwwards.com/websites/portfolio/ | Portfólio público | B |
| Inspiração | Awwwards Daniel Neath | https://www.awwwards.com/sites/daniel-neath-product-design-portfolio | Hero de portfólio | C |
| Inspiração | Land-book | https://land-book.com | Seções de landing | B |
| Inspiração | SiteInspire | https://www.siteinspire.com/websites | Tipografia editorial | C |
| Cor e tipo | Coolors | https://coolors.co | Paletas | B |
| Cor e tipo | Coolors contrast checker | https://coolors.co/contrast-checker | WCAG | A |
| Cor e tipo | Typewolf | https://www.typewolf.com | Tendência de tipo | B |
| Cor e tipo | Typewolf Google Fonts | https://www.typewolf.com/google-fonts | 40 fontes open source | A |
| Newsletter | Smashing Magazine | https://www.smashingmagazine.com/ | Blog e newsletter | A |
| Newsletter | Frontend Focus | https://frontendfoc.us/ | Radar de front-end | A |
| Newsletter | React Status | https://react.statuscode.com/ | Radar de React | A |
| Newsletter | Accessibility Weekly | https://a11yweekly.com/ | A11y | B |
| Comunidade | Ionic Forum | https://forum.ionicframework.com/ | Capacitor | A |
| Blog | Codrops | https://tympanus.net/codrops/ | Motion web | B |
| Blog | Josh W. Comeau | https://www.joshwcomeau.com/ | CSS, React, animação | A |
| Comunidade | Figma Forum | https://forum.figma.com/ | Figma | B |
| Comunidade | WebAIM Discussion List | https://webaim.org/discussion/ | A11y | C |
| Comunidade | Reactiflux | https://www.reactiflux.com/ | React | B |
| Instagram, Facebook, YouTube | ver itens (c), (d), (e) e seção 17 | — | — | — |

### (b) Top 20 recursos

| # | Recurso | Por quê |
|---|---|---|
| 1 | [shadcn/ui Drawer](https://ui.shadcn.com/docs/components/drawer) + [componentes](https://ui.shadcn.com/docs/components) | Base da UI; sheet iOS com snap sem lib extra |
| 2 | [Motion MotionConfig](https://motion.dev/docs/react-motion-config) + [transitions](https://motion.dev/docs/react-transitions) | Reduced motion e tokens globais |
| 3 | [Motion drag](https://motion.dev/docs/react-drag) | Swipe-back, swipe actions, sheets |
| 4 | [Apple HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) | Alvos, 200%, Reduce Motion |
| 5 | [Apple HIG Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) | Comportamento de sheet |
| 6 | [Apple HIG Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) | Navegação do PWA |
| 7 | [M3 Motion specs](https://m3.material.io/styles/motion/overview/specs) | Springs → CSS |
| 8 | [M3 Breakpoints](https://m3.material.io/foundations/layout/breakpoints/overview) | Barra ↔ rail |
| 9 | [Carbon Motion](https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview) | Durações do painel web |
| 10 | [Atlassian Motion](https://atlassian.design/foundations/motion) | Regra de frequência |
| 11 | [NN/g Mobile onboarding](https://www.nngroup.com/articles/mobile-app-onboarding/) | Onboarding |
| 12 | [NN/g Empty states](https://www.nngroup.com/articles/empty-state-interface-design/) | Estados vazios |
| 13 | [NN/g 4 principles forms](https://www.nngroup.com/articles/4-principles-reduce-cognitive-load/) | Propostas e contratos |
| 14 | [NN/g Errors in forms](https://www.nngroup.com/articles/errors-forms-design-guidelines/) | Erros |
| 15 | [NN/g Permission requests](https://www.nngroup.com/articles/permission-requests/) | Capacitor e PWA |
| 16 | [NN/g Data tables](https://www.nngroup.com/articles/data-tables/) | Painel do gestor |
| 17 | [Capacitor UI](https://capacitorjs.com/docs/getting-started/ui) | Fase Capacitor |
| 18 | [Figma Obra shadcn kit](https://www.figma.com/community/file/1514746685758799870/shadcn-ui-kit-community-edition) + [iOS 27](https://www.figma.com/community/file/1651309003795292092/ios-and-ipados-27) | Design alinhado ao código e às safe areas |
| 19 | [Coolors contrast checker](https://coolors.co/contrast-checker) | Validar tokens e tema por cliente |
| 20 | [Lighthouse](https://github.com/GoogleChrome/lighthouse) + [axe-core](https://github.com/dequelabs/axe-core) | Qualidade no CI |

### (c) Top 15 Instagram

Fonte: 9E. Todos estavam ativos em 22–23/11/2026.

| # | Perfil | Por quê | Risco |
|---|---|---|---|
| 1 | [@motion_ui_interface](https://www.instagram.com/motion_ui_interface/) | Regras numéricas de estilo iPhone (blur de 30 px, raio concêntrico, 200–400 ms) | Conta pequena; vende templates |
| 2 | [@theglidestudio](https://www.instagram.com/theglidestudio/) | Motion como continuidade (card → página, pull-to-refresh) | Conselhos criticados nos comentários; testar |
| 3 | [@designmotionhq](https://www.instagram.com/designmotionhq/) | Inputs: 44 px, 16 px, borda 3:1, erro depois do blur | Promove plugin; marcado como "AI content" |
| 4 | [@zanderwhitehurst](https://www.instagram.com/zanderwhitehurst/) | Raio, espaçamento de formulário, Liquid Glass | Regra completa atrás de DM |
| 5 | [@memorisely](https://www.instagram.com/memorisely/) | Princípios de UI em 1 minuto | Simplificado; vende bootcamp |
| 6 | [@noahelhadedy](https://www.instagram.com/noahelhadedy/) | Componentes de motion com código; "anime a mudança" | Alterna com listas genéricas |
| 7 | [@_code_and_chill_](https://www.instagram.com/_code_and_chill_/) | Dashboards de agenda e CRM em código | Código vendido |
| 8 | [@ux.robin](https://www.instagram.com/ux.robin/) | Microinterações open source | Lead-gen; exagero visual |
| 9 | [@lay.the.designer](https://www.instagram.com/lay.the.designer/) | Identidade aplicada a um fluxo | Animação feita em AE/IA |
| 10 | [@uxbrainy](https://www.instagram.com/uxbrainy/) | "Your AI screens look junior" | Promoção de agência |
| 11 | [@ui.iliasmiah000](https://www.instagram.com/ui.iliasmiah000/) | Papéis e permissões (gestor/cliente) | Série repetitiva |
| 12 | [@shohan.designs](https://www.instagram.com/shohan.designs/) | Dashboards fintech para Resultados | Só visual |
| 13 | [@showcase_ui](https://www.instagram.com/showcase_ui/) | Volume diário de dashboards e apps | Só visual |
| 14 | [@code.xr](https://www.instagram.com/code.xr/) | Sidebar e dashboard em React | Glassmorphism chamativo |
| 15 | [@uidesignpatterns](https://www.instagram.com/uidesignpatterns/) | Curadoria de portfólio | Cadência baixa |

### (d) Top 5 Facebook

Fonte: 9F.

| # | Nome | URL | Uso |
|---|---|---|---|
| 1 | Figma \| UI UX Community (62,1 mil) | https://www.facebook.com/groups/973224974974520/ | Notificações só dos admins |
| 2 | Smashing Magazine (página, 263 mil) | https://www.facebook.com/smashmag | Seguir em vez de grupos |
| 3 | React.js Developers (331 mil) | https://www.facebook.com/groups/ReactJsDevelopersGroup/ | Dúvidas pontuais |
| 4 | UI UX Brasil (15,6 mil) | https://www.facebook.com/groups/1774083115968143/ | Mercado BR em PT |
| 5 | Ionic Brasil ⚠️ (2,8 mil; visto só no cartão de busca) | https://www.facebook.com/groups/794233283942540/ | Buscar "capacitor" |

### (e) Top 10 YouTube

Fonte: 9F. Use a aba /videos, porque os links de vídeos individuais não foram capturados.

| # | Canal | URL | Idioma | Foco |
|---|---|---|---|---|
| 1 | Figma | https://www.youtube.com/@Figma/videos | EN | Figma e motion |
| 2 | Kevin Powell | https://www.youtube.com/@KevinPowell/videos | EN | CSS moderno |
| 3 | Hyperplexed | https://www.youtube.com/@Hyperplexed/videos | EN | UI animada |
| 4 | NN/g | https://www.youtube.com/@NNgroup/videos | EN | UX ("6 Tips for Better Tabs") |
| 5 | Juxtopposed | https://www.youtube.com/@juxtopposed/videos | EN | Redesign |
| 6 | Hericky Alencar | https://www.youtube.com/@herickyalencar/videos | **PT** | UX/UI e Figma |
| 7 | Into Design Systems | https://www.youtube.com/@IntoDesignSystems/videos | EN | Tokens e DS |
| 8 | Net Ninja | https://www.youtube.com/@NetNinja/videos | EN | React e Tailwind |
| 9 | Apple Developer | https://www.youtube.com/@AppleDeveloper/videos | EN | Fonte iOS (nativo) |
| 10 | Android Developers | https://www.youtube.com/@AndroidDevelopers/videos | EN | Só para a fase Android |

### (f) Plano de estudo de 30 dias

| Semana | Tema | Recursos concretos | Saída |
|---|---|---|---|
| **1 (dias 1–7)** | Fundações e acessibilidade | Apple HIG Accessibility, Typography, Dark Mode; M3 Breakpoints e Accessibility designing; NN/g Touch targets e Visual treatments; Coolors contrast checker; skill `ux-patterns` (`typography-and-touch.md`) | Rascunho dos tokens de tipo, espaço, alvo e cor com contraste validado |
| **2 (dias 8–14)** | Navegação mobile e componentes | Apple HIG Tab bars e Sheets; NN/g Mobile navigation e 4 iOS rules to break; shadcn/ui Drawer, Toast e Vite; Capacitor UI; skill `mobile-app-ui`; Kit Figma iOS 27 (layout guides) e Obra shadcn | Protótipo do shell do PWA (tab bar + sheet) com safe areas |
| **3 (dias 15–21)** | Motion | Motion docs (transitions, drag, MotionConfig, reduced motion, performance); M3 Motion specs; Carbon Motion; Atlassian Motion; skill `ui-motion` (tokens e `css-recipes.md`); @motion_ui_interface e @theglidestudio; canal Hyperplexed; Josh W. Comeau | Arquivo de tokens de motion + demo de press, sheet e card → página com reduced motion |
| **4 (dias 22–28)** | UX de fluxos | NN/g Onboarding, Empty states, 4 principles forms, Errors in forms, Permission requests, Time-zone, Commitment levels, Data tables, Dashboards, CASTLE; skills `desktop-app-ui` e `dashboard-ui` | Wireframes de onboarding, propostas, agenda e Resultados com os 4 estados |
| **Dias 29–30** | Revisão e radar | Checklist da seção 14 nos protótipos; assinar Smashing, Frontend Focus e React Status; salvar Ionic Forum e Figma Forum | Relatório antes → depois e lista de dúvidas para teste com 5 usuários |

### (g) Plano de implementação de 90 dias

**Sprint 1 (dias 1–30): Fundações**
- **Entregáveis:** tokens (tipo 16 × 1,2; grade de 8; tap 44/48 e gap 8; cores 2+1 com rampa e dark; motion conforme a seção 13, 1.3–1.4) no Tailwind e em CSS vars; `<MotionConfig reducedMotion="user">`; shell do PWA (tab bar de 5 como hipótese validada em teste (D5), stack, Drawer com snap, safe areas, `body { position: relative }`); shell web (sidebar 220–260 ↔ rail 56–64, topbar, ⌘K); breakpoints 375/768/1024/1280/1440/1920; CI com Lighthouse, axe-core e Playwright em 6 viewports; decisão sobre Tailwind v3 × v4 (o v4 exige Safari 16.4+).
- **Critérios de pronto:** checklist itens 1–10, 16–25, 30–33 e 36–37 = sim; nenhum alvo abaixo de 44 px no PWA; contraste AA nos dois temas; Lighthouse sem regressão; reduced motion comprovado por emulação.

**Sprint 2 (dias 31–60): Fluxos críticos**
- **Entregáveis:** onboarding por convite (perfil mínimo, permissões em contexto, OTP); perfil; portfólio (grade + card → detalhe, upload que retoma); agenda (calendar, fuso por cidade, slots no Drawer); propostas e contratos (formulário em coluna única, rodapé com total, confirmação dupla; tabela + inspector + kanban no web); mensagens (Bubble/Message); configurações; os estados vazio, carregando, erro, texto longo e offline em todas as telas; Resultados com 1 + 3 KPIs.
- **Critérios de pronto:** itens 11–15, 26–29 e 40–56 = sim; teste de usabilidade com 5 usuários (incluindo baixa visão ou dificuldade motora) sem bloqueio crítico; métricas definidas (CASTLE no gestor, HEART no cliente); LCP ≤ 2,5 s, INP ≤ 200 ms e CLS ≤ 0,1 em mobile com throttling.

**Sprint 3 (dias 61–90): Diferenciação**
- **Entregáveis:** identidade aplicada (acento ≤ 10%, raios concêntricos, ícones de uma grade só); motion system documentado por evento; microinterações (press, copiar → check, sucesso em 470 ms, segurar para confirmar); transições (push/pop com swipe-back, pílula de 250–350 ms); gestos (swipe actions, pull de 0,35); animação de dados (números rolando, stagger de 100 ms); tema por cliente só via token de acento com contraste ≥ 4,5:1 validado automaticamente (D7: fora do piloto); vidro só na tab bar com fallback; Storybook da camada iOS; empacotamento Capacitor com Haptics e teste em iOS e Android reais.
- **Critérios de pronto:** itens 34–35, 38–39 = sim, e a auditoria completa da seção 14 com 56/56 ou exceções justificadas; 60 fps em celular médio (sem quadros acima de 16,7 ms nas transições principais); revisão com `ext-impeccable` e `design:accessibility-review` sem achado grave; decisão registrada sobre o plano B do Ionic (acionar só se as transições da camada própria não passarem no teste em dispositivo).

### (h) Critérios de escolha e recomendação FINAL: shadcn/ui × Ionic React × Mantine × HeroUI × componentes próprios

**Critérios** (peso por ordem de importância para este produto; a ordenação é minha):
1. **Compatível com React 18 hoje** (eliminatório, porque o stack é React 18).
2. **Mesmo código no painel web e no PWA/Capacitor**, sem dois sistemas visuais.
3. **Customização com Tailwind**, que já está no stack, e tokens próprios.
4. **Padrões iOS-like** (sheet, tab bar, stack com swipe-back, large title).
5. **Acessibilidade de base** (primitivas WAI-ARIA).
6. **Gestos e motion** integrados ao Motion for React.
7. **Peso do bundle** (nenhum foi medido na 9D: tratar como risco).
8. **Licença** (MIT ou Apache-2.0 servem) e **maturidade** (estrelas, manutenção).

| Critério | shadcn/ui | Ionic React | Mantine | HeroUI | Próprios |
|---|---|---|---|---|---|
| React 18 hoje | **Sim** | Sim (política não lida) | **Não** (v9 pede 19.2+) | **Não** (v3 pede 19+ e TW v4) | Sim |
| Um sistema web + mobile | Sim | Não (sistema visual próprio) | Sim | Sim | Sim |
| Tailwind | Total | Baixa | Baixa (CSS Modules) | Alta (v4) | Total |
| iOS-like | Médio (Drawer com snap) | **Alto** (modo `ios`) | Baixo | Médio | Alto se bem feito |
| A11y | Alta (Base UI/Radix/Aria) | Alta (não auditada) | Alta (não auditada) | Alta (React Aria) | **Risco** |
| Gestos | Médio + Motion | Alto | Baixo | Médio | Depende do Motion |
| Licença / estrelas | MIT / 129 mil | MIT / 52,8 mil | MIT / 32 mil | Apache-2.0 / 31,3 mil | — |

**Recomendação FINAL (coerente com a 9D):** **shadcn/ui na variante Base UI + Motion for React + uma camada própria fina de padrões iOS** (tab bar inferior, navigation bar com large title, push/pop com swipe-back, swipe actions, segmented control a partir do Toggle Group, pull-to-refresh). Haptics vêm do Capacitor.
- **Mantine e HeroUI estão fora** enquanto o projeto estiver em React 18. Reavaliar só se houver migração para React 19.
- **Ionic React é plano B**, restrito ao app Capacitor, se as transições de página nativas virarem requisito e a camada própria não chegar lá. O custo é manter dois sistemas visuais.
- **A camada própria** fica pequena, com acessibilidade herdada das primitivas do Base UI sempre que possível, e vai para o Storybook a partir de uns 10 componentes.
- **Obrigatórios desde o dia 1:** `<MotionConfig reducedMotion="user">`; tokens de duração e easing no Tailwind; animar só `transform`/`opacity`; `body { position: relative }` para o Drawer no iOS Safari; uma base do shadcn só (as APIs mudam entre bases, por exemplo `asChild` → `render`); teste no iOS 16.4+ se adotar o Tailwind v4.
- **Riscos que continuam abertos:** peso do bundle não medido; acessibilidade da camada própria; política de suporte do Ionic React a React 18 não lida.

---

## 16. Limitações e lacunas (leitura crítica)

- **Mobbin 🔒:** nenhuma tela real de app iOS de agenda, CRM ou mensagens foi verificada. Recomendo uma rodada logada à parte (9C).
- **Dribbble anti-bot:** só 4 shots têm autor verificado. Os demais são candidatos sem análise visual (9C). Todos os shots e cases do Behance são conceituais, sem prova de uso.
- **Quase nada em PT-BR:** 1 canal de YouTube (Hericky Alencar), 1 grupo grande (UI UX Brasil), 1 grupo pequeno de Ionic e nenhuma newsletter de UX em PT. A NN/g não tem conteúdo nem estudos em PT-BR (9B, 9F). Microcopy e tom de voz em PT ficam por conta do time.
- **NN/g antigo:** navegação (2015), 4 iOS rules (2015), commitment (2016), dashboards (2017), login (2017) e touch targets (2019). Os princípios valem, mas os componentes iOS mudaram. O vídeo de skeleton está 🔒 e o relatório mobile 5ª edição (com PWA e passkeys) é pago (US$ 298) e não foi lido.
- **Apple sem números de motion:** nem durações, nem curvas, nem springs (9A, 9D). Os números do projeto vêm do `ui-motion`, com calibragem por Carbon, Atlassian e Material. Na 9A, a tabela de tipo iOS capturada é a do tamanho "xSmall".
- **Material:** os valores de stiffness e damping das springs não foram extraídos (ficam em módulo recolhido). Só a tabela de conversão para web está disponível.
- **Motion for React:** a doc lista `stiffness` com padrão "1", o que parece erro. É preciso conferir no código antes de usar (9D).
- **Bundle:** nenhuma lib teve o peso medido (9D).
- **Instagram:** os vídeos não foram assistidos quadro a quadro. Vários números estão só no vídeo ou atrás de DM, e muito conteúdo é lead-gen (9E).
- **YouTube:** não há links de vídeos individuais (9F).
- **Newsletters:** foram verificadas 10 de 15. Falta newsletter de UX e comunidade de motion de UI (9F).
- **Facebook:** Ionic Brasil, Motion Designers (privado) e WCAG A11y (privado) foram vistos só no cartão de busca (9F).
- **Conflitos entre fontes** registrados neste documento: escala 1,2 × 1,25 (`ux-patterns`); gauge e anel × NN/g (seção 4, D4); seletor de tema próprio × Apple (1.10, D6); duração de press de 160 ms (`ui-motion`) × microinteração de 90–120 ms (Carbon) e < 150 ms para o frequente (Atlassian) (D2, D3). Pela regra de prioridade valem os tokens das skills, com o feedback começando em 0 ms. Toast que some sozinho × Apple ("evitar elementos que se auto-dispensam"): o erro fica até ser reconhecido, e info e warning precisam de pausa no hover.
- **Prints:** as rodadas citam pastas `prints-9A`…`prints-9E`, mas elas **não estão em `docs/achados/`** neste checkout.

---

## 17. Fontes verificadas

Só entram URLs marcadas como ✅ (abertas) nas rodadas. As ressalvas estão indicadas. Nenhuma URL foi criada para este documento. Os repositórios GitHub aparecem como `owner/repo`, citados na 9D como fonte de licença e estrelas.

### 9A: Fundações oficiais
- https://developer.apple.com/design/human-interface-guidelines/
- https://developer.apple.com/design/human-interface-guidelines/foundations/motion (redireciona para /motion)
- https://developer.apple.com/design/human-interface-guidelines/motion
- https://developer.apple.com/design/human-interface-guidelines/accessibility
- https://developer.apple.com/design/human-interface-guidelines/design-principles
- https://developer.apple.com/design/human-interface-guidelines/layout
- https://developer.apple.com/design/human-interface-guidelines/typography
- https://developer.apple.com/design/human-interface-guidelines/color
- https://developer.apple.com/design/human-interface-guidelines/dark-mode
- https://developer.apple.com/design/human-interface-guidelines/tab-bars
- https://developer.apple.com/design/human-interface-guidelines/sheets
- https://m3.material.io/styles/motion (redireciona para /styles/motion/overview/how-it-works)
- https://m3.material.io/styles/motion/overview/how-it-works
- https://m3.material.io/styles/motion/overview/specs
- https://m3.material.io/styles/motion/easing-and-duration/tokens-specs
- https://m3.material.io/foundations/adaptive-design/overview (redireciona para /foundations/layout/layout-overview/overview)
- https://m3.material.io/foundations/layout/applying-layout/window-size-classes (redireciona para /foundations/layout/breakpoints/overview)
- https://m3.material.io/foundations/layout/understanding-layout/spacing (redireciona para /foundations/layout/grids-spacing/spacing)
- https://m3.material.io/styles/typography/type-scale-tokens
- https://m3.material.io/foundations/designing/structure
- https://m3.material.io/foundations/layout/canonical-examples/overview (página dos prints)
- https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview

### 9B: Nielsen Norman Group
- https://www.nngroup.com/articles/
- https://www.nngroup.com/articles/mobile-ux-study-guide/
- https://www.nngroup.com/articles/web-ux-study-guide/
- https://www.nngroup.com/topics/
- https://www.nngroup.com/topic/applications/
- https://www.nngroup.com/reports/
- https://www.nngroup.com/reports/topic/mobile-and-tablet-design/
- https://www.nngroup.com/reports/topic/applications/
- https://www.nngroup.com/reports/free/
- https://www.nngroup.com/reports/mobile-website-and-application-usability/
- https://www.nngroup.com/reports/make-decisions/
- https://www.nngroup.com/articles/touch-target-size/
- https://www.nngroup.com/articles/mobile-navigation-patterns/
- https://www.nngroup.com/articles/4-ios-rules-break/
- https://www.nngroup.com/articles/mobile-app-onboarding/
- https://www.nngroup.com/articles/empty-state-interface-design/
- https://www.nngroup.com/articles/errors-forms-design-guidelines/
- https://www.nngroup.com/articles/dashboards-preattentive/
- https://www.nngroup.com/articles/permission-requests/
- https://www.nngroup.com/articles/visual-treatments-accessibility/
- https://www.nngroup.com/articles/castle-framework/
- https://www.nngroup.com/articles/4-principles-reduce-cognitive-load/
- https://www.nngroup.com/articles/time-zone-selectors/
- https://www.nngroup.com/articles/commitment-levels/
- https://www.nngroup.com/articles/3-is-of-microcopy/
- https://www.nngroup.com/articles/data-tables/
- https://www.nngroup.com/articles/checklist-registration-login/
- https://www.nngroup.com/articles/tabs-used-right/
- https://www.nngroup.com/videos/skeleton-screens-vs-progress-bars-vs-spinners/ (🔒 o vídeo não carrega)

### 9C: Inspiração
- https://mobbin.com (🔒 só a home; https://mobbin.com/browse/ios/apps redireciona para o login)
- https://dribbble.com/tags/ui-ux-inspiration
- https://dribbble.com/tags/ui-ux-design
- Buscas no Dribbble: https://dribbble.com/search/creator-dashboard, /search/personal-portfolio-app, /search/booking-calendar-app, /search/crm-mobile-app, /search/messaging-app-ui, /search/onboarding-mobile, /search/freelancer-profile-app
- https://dribbble.com/shots/25294910-Kreya-Content-Creator-Dashboard
- https://dribbble.com/shots/26534678-Blenz-Influencer-Analytics-Dashboard-UI
- https://dribbble.com/shots/25532738-Invoice-Proposal-Creator
- https://dribbble.com/shots/27744939-Creator-Brand-Content-Management-Mobile-App
- https://www.behance.net
- https://www.behance.net/gallery/258614563/Cook-%28-CreatorBrand-Deals-App-%29
- https://www.behance.net/gallery/254485187/Nomey-Creator-Monetization-Platform
- https://www.behance.net/gallery/253975015/Reelful-AI-Powered-Social-Video-Creator-App-UIUX
- https://www.awwwards.com
- https://www.awwwards.com/websites/portfolio/
- https://www.awwwards.com/sites/daniel-neath-product-design-portfolio
- https://land-book.com
- https://www.siteinspire.com/websites (o filtro `?categories=5` redireciona para cá)
- https://coolors.co
- https://coolors.co/contrast-checker
- https://www.typewolf.com
- https://www.typewolf.com/google-fonts
- ⚠️ Shots do Dribbble vistos só na listagem (o shot não foi aberto e o autor não foi verificado): 25067767, 23742257, 26029349, 27286173, 24243315, 27609091, 20762095, 27580119, 26343181, 25197917, 26673918, 26112146, 27669622, 27784384, 27669776. As URLs completas estão em `rodada-9C.md`.

### 9D: Ferramentas e design systems
- https://www.figma.com/community
- https://www.figma.com/community/file/1651309003795292092/ios-and-ipados-27
- https://www.figma.com/community/file/1527721578857867021/ios-and-ipados-26
- https://www.figma.com/community/file/1035203688168086460/material-3-design-kit
- https://www.figma.com/community/file/1514746685758799870/shadcn-ui-kit-community-edition
- https://www.figma.com/community/file/1463555657173424575/crm-ui-kit-for-saas-dashboards
- ⚠️ https://www.figma.com/community/file/1534076420225325960/shadcn-ui-kit-shadcncraft-free-starter-kit (licença não verificada)
- https://ui.shadcn.com/docs/components
- https://ui.shadcn.com/docs/components/drawer
- https://ui.shadcn.com/docs/components/toast
- https://ui.shadcn.com/docs/installation/vite
- https://ui.shadcn.com/docs/tailwind-v4
- https://ui.shadcn.com/docs/react-19
- https://ui.shadcn.com/docs/figma
- https://www.shadcn.io/ui (terceiro comercial)
- https://www.shadcn.io/awesome/components
- https://motion.dev/docs/react
- https://motion.dev/docs/react-installation
- https://motion.dev/docs/react-transitions
- https://motion.dev/docs/react-drag
- https://motion.dev/docs/react-use-reduced-motion
- https://motion.dev/docs/react-motion-config
- https://motion.dev/docs/react-accessibility
- https://motion.dev/docs/performance
- https://motion.dev/docs/framer
- https://lottiefiles.com/motion-system
- https://docs.lottiefiles.com/en/creator/15_motion-system
- https://docs.lottiefiles.com/en/creator/07_animation/easing
- https://www.radix-ui.com/primitives/docs/overview/introduction
- https://tailwindcss.com
- https://tailwindcss.com/docs/compatibility
- https://headlessui.com
- https://react-aria.adobe.com
- https://mantine.dev/getting-started/
- https://mantine.dev/changelog/9-0-0/
- https://mantine.dev/styles/css-modules/
- https://www.heroui.com/docs/guide/installation
- https://ionicframework.com/docs/react
- https://ionicframework.com/docs/theming/platform-styles
- https://framework7.io
- https://framework7.io/react/
- https://mobile.ant.design
- https://mobile.ant.design/guide/quick-start
- https://gsap.com/pricing/
- https://gsap.com/licensing/
- https://rive.app/pricing
- https://www.figma.com/pricing/
- https://tokens.studio/pricing
- https://www.chromatic.com/pricing
- https://www.getstark.co/pricing/
- https://www.deque.com/axe/devtools/pricing/
- https://capacitorjs.com/docs
- https://capacitorjs.com/docs/getting-started/ui
- https://supabase.com/ui (redireciona para https://supabase.com/library/docs/getting-started/introduction)
- GitHub: shadcn-ui/ui · radix-ui/primitives · tailwindlabs/tailwindcss · tailwindlabs/headlessui · adobe/react-spectrum · mantinedev/mantine · heroui-inc/heroui · ionic-team/ionic-framework · framework7io/framework7 · ant-design/ant-design-mobile · youzan/vant · motiondivision/motion · ionic-team/capacitor · storybookjs/storybook · GoogleChrome/lighthouse · dequelabs/axe-core · airbnb/lottie-web · LottieFiles/dotlottie-web
- https://developer.apple.com/design/human-interface-guidelines/motion · https://developer.apple.com/design/human-interface-guidelines/accessibility
- https://m3.material.io/styles/motion/easing-and-duration/tokens-specs · https://m3.material.io/styles/motion/overview/specs · https://m3.material.io/foundations/overview/principles
- https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview · https://www.carbondesignsystem.com/building-blocks/foundations/accessibility/overview
- https://atlassian.design/foundations/motion · https://atlassian.design/foundations/accessibility · https://atlassian.design/foundations/tokens/design-tokens
- https://fluent2.microsoft.design/motion · https://fluent2.microsoft.design/design-tokens · https://fluent2.microsoft.design/accessibility
- ⚠️ https://polaris-react.shopify.com/design/motion → https://shopify.dev/docs/api/polaris (a página de motion não existe mais)
- https://primer.style/product/primitives/ · https://primer.style/product/primitives/token-names/ · https://primer.style/accessibility/
- https://www.lightningdesignsystem.com/ · https://www.lightningdesignsystem.com/2e1ef8501/p/777f5a-global-styling-hooks · https://www.lightningdesignsystem.com/2e1ef8501/p/641741-accessibility
- https://www.radix-ui.com/themes/docs/overview/getting-started
- https://ant.design/docs/spec/motion · https://ant.design/docs/react/customize-theme
- Páginas dos prints: https://ui.shadcn.com/blocks · https://ionicframework.com/docs/api/modal · https://ionicframework.com/docs/api/tabs · https://framework7.io/react/kitchen-sink.html · https://supabase.com/library · https://motion.dev/examples?platform=react&search=swipe

### 9E: Instagram
Perfis ativos (https://www.instagram.com/<handle>/): motion_ui_interface, designmotionhq, theglidestudio, zanderwhitehurst, memorisely, noahelhadedy, _code_and_chill_, ux.robin, lay.the.designer, uxbrainy, ui.iliasmiah000, shohan.designs, showcase_ui, code.xr, uidesignpatterns, felvrabr, ramotion, dailywebdesign, ui.pixel, humbleteam.agency, untitledui, osmo.supply, arounda.agency, ui8net, craftwork.design, filllodesign, memento___studios, framer.

Perfis abertos e descartados como inativos, indisponíveis ou fora do foco: ui.designs, uitrends, ux_ui_wireframes, humble_ux, uxigers, uigarage, gifux, uiuxgifs, uxdesignmastery, iamjesseshow, uxbucket, kenny.kenray, afternow.co.

Posts abertos:
- https://www.instagram.com/reel/Dflzxq5Bqfj/ · https://www.instagram.com/reel/DfcwOHLh76I/ (@motion_ui_interface)
- https://www.instagram.com/reel/Df4WVGIBO2k/ · https://www.instagram.com/reel/DgCqEFtBmnz/ (@designmotionhq)
- https://www.instagram.com/reel/DfwhC1riuuO/ · https://www.instagram.com/reel/DgDE8_5hBOe/ (@theglidestudio)
- https://www.instagram.com/reel/DfFFnkBOllG/ · https://www.instagram.com/reel/DRuEeIPCH7M/ (@zanderwhitehurst)
- https://www.instagram.com/reel/Df7SmUBO5x5/ · https://www.instagram.com/reel/DfzRnlsuvfG/ (@memorisely)
- https://www.instagram.com/p/DgCpGgjjokC/ · https://www.instagram.com/p/Df_5RWiDmkc/ (@noahelhadedy)
- https://www.instagram.com/reel/Df7dwtMPccu/ · https://www.instagram.com/reel/DbfG6fuPE9y/ (@_code_and_chill_)
- https://www.instagram.com/p/Df4JJADCPVa/ · https://www.instagram.com/p/DgCbnhtiCzI/ (@ux.robin)
- https://www.instagram.com/p/DfjoEHGgLcg/ · https://www.instagram.com/reel/DfsGursgrjI/ (@lay.the.designer)
- https://www.instagram.com/p/DgDSue_Ftd-/ · https://www.instagram.com/reel/DeJcMSpxqZS/ (@uxbrainy)
- https://www.instagram.com/reel/DgDuN_3h3AU/ · https://www.instagram.com/reel/DgD79jFhsIf/ (@ui.iliasmiah000)
- https://www.instagram.com/p/DgDFfyBFIZN/ · https://www.instagram.com/p/Df978CFlMsF/ (@shohan.designs)
- https://www.instagram.com/reel/DgBw1OjO9zO/ · https://www.instagram.com/p/DgBR6h4olO7/ (@showcase_ui)
- https://www.instagram.com/reel/DgC6ruhT2NZ/ · https://www.instagram.com/reel/DgCXLXMTSW7/ (@code.xr)
- https://www.instagram.com/reel/DcyWWw-hCTz/ · https://www.instagram.com/reel/DavD2o5oge0/ (@uidesignpatterns)
- https://www.instagram.com/p/Df-LDBmF5_R/ (@untitledui)

### 9F: Facebook, YouTube, newsletters
- Facebook (abertos): https://www.facebook.com/groups/uxdesignercommunity/ · https://www.facebook.com/groups/226816094176688/ · https://www.facebook.com/groups/973224974974520/ · https://www.facebook.com/groups/bestUXDesigners/ · https://www.facebook.com/groups/uxdjcommunity/ · https://www.facebook.com/groups/1774083115968143/ · https://www.facebook.com/groups/ReactJsDevelopersGroup/ · https://www.facebook.com/smashmag
- ⚠️ Facebook visto só no cartão de busca: https://www.facebook.com/groups/794233283942540/ · https://www.facebook.com/groups/motiondesignerscommunity/ (privado) · https://www.facebook.com/groups/WCAGa11y/ (privado). A página https://www.facebook.com/nngroup/ foi descartada (é uma seguradora).
- YouTube (ativos): https://www.youtube.com/@Figma/videos · https://www.youtube.com/@KevinPowell/videos · https://www.youtube.com/@Hyperplexed/videos · https://www.youtube.com/@juxtopposed/videos · https://www.youtube.com/@NNgroup/videos · https://www.youtube.com/@herickyalencar/videos · https://www.youtube.com/@IntoDesignSystems/videos · https://www.youtube.com/@NetNinja/videos · https://www.youtube.com/@AppleDeveloper/videos · https://www.youtube.com/@AndroidDevelopers/videos · https://www.youtube.com/@rocketseat/videos · https://www.youtube.com/@ByteGrad/videos · https://www.youtube.com/@BenMarriott/videos · https://www.youtube.com/@UXPin/videos · https://www.youtube.com/@learnuxid/videos
- YouTube abertos e descartados: @DesignCourse, @googledesign, @IonicFramework, @Mizko, @mavidesign
- Newsletters e comunidades: https://www.smashingmagazine.com/ · https://frontendfoc.us/ · https://react.statuscode.com/ · https://a11yweekly.com/ · https://forum.ionicframework.com/ · https://tympanus.net/codrops/ · https://www.joshwcomeau.com/ · https://forum.figma.com/ · https://webaim.org/discussion/ · https://www.reactiflux.com/

**Excluídas por erro (não usar):** https://www.typewolf.com/free-font-combinations (404), https://www.nngroup.com/topic/application-design/ (404), https://www.nngroup.com/newsletters/ (404) e https://www.nngroup.com/search/?q=empty+states (sem resultados).
