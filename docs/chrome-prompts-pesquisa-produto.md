# Pesquisa de Product Design para o app de marca pessoal (rodadas 9A–9F)

Prompts para a extensão **Claude in Chrome**. Mande **uma rodada por vez**, com o Instagram e o Facebook logados. Ao final de cada rodada, a extensão gera `rodada-9X.md` com os prints. Cole o resultado na sessão das skills no Claude Code. Lá eu faço a síntese final: visão geral, plano em 3 fases, checklist de 40–60 itens e entregáveis.

| Rodada | Conteúdo | Links semente | Modelo |
|---|---|---|---|
| 9A | Fundações oficiais: Apple HIG, Material 3, Carbon Motion | 1–7, 31 | Sonnet 5.5 |
| 9B | UX e pesquisa: Nielsen Norman Group | 8–12 | Sonnet 5.5 |
| 9C | Inspiração e benchmarking + apps de referência | 13–21 | Sonnet 5.5 |
| 9D | Ferramentas, bibliotecas, design systems e motion systems | 22–30 + lista E | **Opus 5.5** |
| 9E | Instagram (meta: 25 perfis) | 32–44 | Sonnet 5.5 |
| 9F | Facebook (10), YouTube (15), newsletters e comunidades (15) | 45–48 | Sonnet 5.5 |

Não use Haiku. Se uma resposta cortar no meio, peça "continue de onde parou, no mesmo formato".

---

## Rodada 9A: fundações oficiais (Apple, Material, Carbon)

**Modelo:** Sonnet 5.5

```
Você é um pesquisador sênior de Product Design, UI/UX e motion design. Sua tarefa é LER e EXTRAIR, não opinar de memória.

CONTEXTO DO PRODUTO
App de gestão de marca pessoal (presença, conteúdo, agenda, portfólio, networking, propostas, contratos, mensagens, resultados). Web: painel para gestor e cliente. Mobile do cliente: PWA no piloto, depois o mesmo código React empacotado com Capacitor (iOS/Android). Stack: React 18 + TypeScript + Vite + Supabase + Tailwind + shadcn/ui + Motion for React. Público avançado, PT e EN. Direção visual: inspirada em iOS/Apple (clean, tipografia forte, hierarquia clara, gestos naturais, animações curtas), sem copiar a Apple.

LINKS DESTA RODADA (abra cada um e navegue pelas subpáginas relevantes)
1. https://developer.apple.com/design/human-interface-guidelines/
2. https://developer.apple.com/design/human-interface-guidelines/foundations/motion
3. https://developer.apple.com/design/human-interface-guidelines/accessibility
4. https://developer.apple.com/design/human-interface-guidelines/design-principles
5. https://m3.material.io/styles/motion
6. https://m3.material.io/styles/motion/overview/how-it-works
7. https://m3.material.io/foundations/adaptive-design/overview
31. https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview

O QUE EXTRAIR (priorize números e regras concretas, não resumos genéricos)
- Tipografia: tamanhos, pesos, escala, Dynamic Type / type scale do Material.
- Layout: margens, grid, breakpoints/window size classes, safe areas, alvos de toque.
- Cor e dark mode: papéis de cor, contraste.
- Navegação: tab bar/navigation bar, sheets/bottom sheets, modais, gestos.
- Motion: princípios, durações, curvas de easing (com os valores: ms, cubic-bezier, springs), tokens de motion, transições de tela, Reduce Motion.
- Acessibilidade: contraste, VoiceOver/TalkBack, tamanho de texto, foco.
- Para cada regra, diga se vale para o PWA/Capacitor do cliente, para o painel web, ou para os dois.

FORMATO: para cada link, uma ficha:
### <nome do recurso>
- URL principal | status: ✅ abriu / ❌ quebrado / 🔒 exige login
- Subpáginas relevantes visitadas (com URL de cada uma)
- Tema, nível, idioma, preço (gratuito/pago/open source/freemium)
- Tags: [oficial] [comunidade] [inspiração] [ferramenta] [curso] [artigo] [vídeo] [newsletter] [biblioteca]
- Regras e números extraídos (lista objetiva, citando a subpágina)
- Para que serve no app (telas/fluxos: onboarding, perfil, portfólio, agenda, propostas, mensagens, configurações, dashboards)
- Limitações e riscos (ex.: regra só de app nativo que não funciona em PWA)

No final, uma tabela comparando Apple × Material × Carbon em: durações de motion, easing, alvos de toque, escala tipográfica e navegação mobile.

REGRAS
- Abra cada URL antes de citar. Não invente valores: se a página não traz o número, escreva "não especificado".
- Não confunda React Native com React DOM. A base do app é React DOM + Capacitor.
- Só leia; não faça login nem preencha formulários.

AO FINAL DA RODADA, gere o arquivo `rodada-9A.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas com os principais aprendizados da rodada;
   - depois, TODAS as fichas e a tabela;
   - no fim, a seção "Fontes verificadas", com todas as URLs abertas, e a seção "Prints".
2. Prints: tire print só do que tiver valor visual (tabelas de duração/easing, diagramas de curva, exemplos de layout ou navegação), no máximo 3 por link. Nomeie cada um como `9A_<recurso>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-9A.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-9A.md` num ÚNICO bloco de código Markdown. Na seção "Prints", ponha uma linha por print: nome | URL | o que mostra.
```

---

## Rodada 9B: UX e pesquisa (Nielsen Norman Group)

**Modelo:** Sonnet 5.5

```
Você é um pesquisador sênior de UX. Sua tarefa é LER e EXTRAIR, não opinar de memória.

CONTEXTO DO PRODUTO
App de gestão de marca pessoal (presença, conteúdo, agenda, portfólio, networking, propostas, contratos, mensagens, resultados). Web: painel para gestor e cliente. Mobile do cliente: PWA, depois Capacitor (iOS/Android). React 18 + TypeScript + Tailwind + shadcn/ui + Motion for React. Público avançado, PT e EN.

LINKS DESTA RODADA
8. https://www.nngroup.com/articles/
9. https://www.nngroup.com/articles/mobile-ux-study-guide/
10. https://www.nngroup.com/articles/web-ux-study-guide/
11. https://www.nngroup.com/topics/
12. https://www.nngroup.com/reports/

O QUE FAZER
1. Abra os dois study guides (9 e 10) e liste os artigos de cada um. Abra os que tratam dos temas abaixo e extraia as recomendações concretas.
2. Nos tópicos (11), encontre os artigos mais relevantes para: arquitetura de informação, navegação mobile, formulários, onboarding, empty states, mensagens de erro, loading/skeletons, dashboards, microcopy, acessibilidade (inclusive cognitiva), testes com usuários, métricas de UX, retenção, design responsivo, agenda/agendamento, perfis e confiança/credibilidade.
3. Nos relatórios (12), liste os que se aplicam ao app, com preço e se há versão gratuita.

FORMATO: para cada artigo ou relatório relevante:
### <título>
- URL | status: ✅ / ❌ / 🔒 | data de publicação
- Tema, nível, gratuito/pago
- Recomendações extraídas (lista objetiva; inclua números quando houver, ex.: tempos de resposta, tamanhos, percentuais)
- Telas/fluxos do app em que se aplica
- Limitações (ex.: estudo antigo, desktop-only)

No final:
- Top 15 artigos para este produto, em ordem de prioridade, com 1 linha de justificativa cada.
- Lista de lacunas: temas do app que o NN/g NÃO cobre bem.

REGRAS
- Abra cada URL antes de citar. Não invente títulos nem datas.
- Respeite o conteúdo pago: só descreva o que é público.
- Só leia; não faça login nem compre nada.

AO FINAL DA RODADA, gere o arquivo `rodada-9B.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas;
   - depois, TODAS as fichas, o Top 15 e as lacunas;
   - no fim, "Fontes verificadas" e "Prints".
2. Prints: no máximo 10 na rodada, só de diagramas ou exemplos visuais úteis. Nomeie como `9B_<artigo>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-9B.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-9B.md` num ÚNICO bloco de código Markdown, com a lista de prints: nome | URL | o que mostra.
```

---

## Rodada 9C: inspiração e benchmarking

**Modelo:** Sonnet 5.5

```
Você é um pesquisador sênior de Product Design fazendo benchmarking. Sua tarefa é LER e EXTRAIR, não opinar de memória.

CONTEXTO DO PRODUTO
App de gestão de marca pessoal (presença, conteúdo, agenda, portfólio, networking, propostas, contratos, mensagens, resultados). Web: painel para gestor e cliente. Mobile do cliente: PWA, depois Capacitor (iOS/Android). Direção visual inspirada em iOS/Apple (clean, tipografia forte, gestos naturais, animações curtas), sem copiar.

LINKS DESTA RODADA
13. https://mobbin.com
14. https://dribbble.com/tags/ui-ux-inspiration
15. https://dribbble.com/tags/ui-ux-design
16. https://www.behance.net
17. https://www.awwwards.com
18. https://land-book.com
19. https://www.siteinspire.com
20. https://coolors.co
21. https://www.typewolf.com

O QUE FAZER
1. Para cada site, uma ficha: URL | status ✅/❌/🔒 | o que é | gratuito/pago (o que fica atrás de login ou paywall) | melhor uso para este app | limitações.
2. No Mobbin, mesmo sem login, liste os apps e categorias visíveis que servem de referência para: creator economy, portfólio, agenda/agendamento, CRM, networking, mensagens, propostas/contratos e dashboards. Se pedir login, marque 🔒 e siga com o que é público.
3. Em Dribbble, Behance, Awwwards, Land-book e SiteInspire, encontre de 3 a 5 exemplos concretos por categoria: perfil/portfólio, agenda, dashboard de criador, CRM pessoal, mensagens, onboarding e landing de serviço pessoal.
4. Em Coolors e Typewolf, extraia como usar: paletas, contraste, pares tipográficos e fontes recomendadas para produto (com licença).

FORMATO: para cada referência concreta:
### <nome do app/projeto> — <autor/estúdio>
- URL | status
- Plataforma: iOS | Android | web app | site
- O que observar (layout, hierarquia, tipografia, cor, motion)
- Quais telas estudar
- Como adaptar ao app de marca pessoal sem copiar
- Riscos de copiar diretamente (marca, direitos, padrão que não serve)

No final, uma tabela: categoria do app (perfil, portfólio, agenda, propostas, mensagens, dashboard, onboarding) × 2–3 melhores referências com URL.

REGRAS
- Abra cada URL antes de citar. Não invente nomes de apps nem de autores.
- Só leia: não curta, não siga, não salve em coleções, não crie conta.

AO FINAL DA RODADA, gere o arquivo `rodada-9C.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas;
   - depois, TODAS as fichas e a tabela;
   - no fim, "Fontes verificadas" e "Prints".
2. Prints: tire print das telas de referência mais úteis, no máximo 3 por categoria. Nomeie como `9C_<categoria>_<app>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-9C.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-9C.md` num ÚNICO bloco de código Markdown, com a lista de prints: nome | URL | o que mostra.
```

---

## Rodada 9D: ferramentas, bibliotecas, design systems e motion systems

**Modelo:** Opus 5.5 (compara licenças, compatibilidade e trade-offs)

```
Você é um pesquisador sênior de front-end mobile e design systems. Sua tarefa é VERIFICAR nas fontes oficiais, não responder de memória.

CONTEXTO DO PRODUTO
App de gestão de marca pessoal. Web: painel para gestor e cliente. Mobile do cliente: PWA no piloto, depois o MESMO código React empacotado com Capacitor (iOS/Android). Stack: React 18 + TypeScript + Vite + Supabase + Tailwind + shadcn/ui + Motion for React. Visual iOS-like. NÃO usar React Native como base: a base é React DOM + Capacitor.

PARTE 1: LINKS SEMENTE (abra e extraia)
22. https://www.figma.com/community
23. https://ui.shadcn.com/docs/components
24. https://www.shadcn.io/ui
25. https://www.shadcn.io/awesome/components
26. https://motion.dev/docs/react
27. https://motion.dev/docs/framer
28. https://lottiefiles.com/motion-system
29. https://docs.lottiefiles.com/en/creator/15_motion-system
30. https://docs.lottiefiles.com/en/creator/07_animation/easing
- No shadcn/ui, liste quais componentes servem às telas do app (drawer/sheet, dialog, tabs, calendar, form, data table, toast/sonner, command) e o que falta para um app iOS-like.
- No Motion, extraia: springs vs tween, layout animations, AnimatePresence, gestos (drag, swipe), useReducedMotion, performance.
- No Figma Community, encontre kits relevantes (iOS UI kit oficial, Material 3 kit, shadcn kit, kits de dashboard/portfólio), com link e licença.

PARTE 2: FERRAMENTAS (abra o site oficial de cada uma e verifique)
shadcn/ui, Radix UI, Tailwind CSS, Headless UI, React Aria, Mantine, HeroUI, Ionic React, Framework7, Ant Design Mobile, Vant, Motion for React, GSAP, Lottie, Rive, Figma, Tokens Studio, Storybook, Chromatic, Lighthouse, axe DevTools, Stark, Capacitor, Supabase UI.

Para cada uma, uma linha numa tabela:
| Ferramenta | URL oficial | Categoria | Licença/preço | React DOM? | PWA? | Capacitor? | Serve para app iOS-like? | Prós | Contras | Alternativas | Quando usar | Quando evitar |
ATENÇÃO: confira na documentação oficial se a biblioteca é para React DOM ou React Native (ex.: Vant tem versão React? Ant Design Mobile funciona no Capacitor?). Se não encontrar, escreva "não verificado".

PARTE 3: DESIGN SYSTEMS E MOTION SYSTEMS (mínimo 10)
Ex.: Apple HIG, Material 3, IBM Carbon, Atlassian, Shopify Polaris, GitHub Primer, Microsoft Fluent 2, Salesforce Lightning, Radix Themes, Ant Design. Confira cada um no site oficial.
Para cada um:
### <nome> — <empresa/comunidade>
- URL | status
- O que aprender
- Tokens disponíveis (cor, tipografia, espaço, motion), com link
- Padrões de animação (durações e easing, se publicados)
- Documentação de acessibilidade (link)
- Aplicabilidade para um app de marca pessoal (alta/média/baixa e por quê)

PARTE 4: CRITÉRIOS DE ESCOLHA
Compare shadcn/ui × Ionic React × Mantine × HeroUI × componentes próprios para ESTE app (PWA → Capacitor, visual iOS-like, Tailwind já em uso): uma tabela de critérios (visual iOS-like, gestos nativos, acessibilidade, peso do bundle, customização com Tailwind, maturidade, licença) e uma recomendação justificada.

REGRAS
- Abra o site oficial de cada ferramenta antes de citar licença, preço ou compatibilidade. Não invente.
- Seja crítico: diga limitações reais.
- Só leia; não crie conta.

AO FINAL DA RODADA, gere o arquivo `rodada-9D.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas;
   - depois, as partes 1 a 4 completas;
   - no fim, "Fontes verificadas" e "Prints".
2. Prints: no máximo 12 na rodada (ex.: páginas de motion tokens, tabelas de easing, componentes-chave). Nomeie como `9D_<recurso>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-9D.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-9D.md` num ÚNICO bloco de código Markdown, com a lista de prints: nome | URL | o que mostra.
```

---

## Rodada 9E: Instagram (meta: 25 perfis)

**Modelo:** Sonnet 5.5

```
Você é um pesquisador sênior de UI/UX e motion design avaliando perfis do Instagram como fonte de aprendizado. Sua tarefa é ABRIR cada perfil e verificar, não citar de memória.

CONTEXTO DO PRODUTO
App de gestão de marca pessoal (perfil, portfólio, agenda, propostas, mensagens, dashboards). Web: painel para gestor e cliente. Mobile do cliente: PWA, depois Capacitor. Visual inspirado em iOS, com motion curto.

PERFIS INICIAIS (abra cada um)
32. https://www.instagram.com/ui.designs/
33. https://www.instagram.com/uitrends/
34. https://www.instagram.com/uidesignpatterns/ (já avaliado antes: ativo, ~413 mil seguidores, curadoria só de inspiração, sem texto didático; só confirme se ainda está ativo)
35. https://www.instagram.com/ux_ui_wireframes/
36. https://www.instagram.com/humble_ux/
37. https://www.instagram.com/uxigers/
38. https://www.instagram.com/uigarage/
39. https://www.instagram.com/gifux/ (já avaliado antes: INATIVO, 0 posts; só confirme)
40. https://www.instagram.com/uiuxgifs/
41. https://www.instagram.com/uxdesignmastery/ (já avaliado antes: INATIVO; só confirme)
42. https://www.instagram.com/showcase_ui/
43. https://www.instagram.com/zanderwhitehurst/
44. https://www.instagram.com/iamjesseshow/

PERFIS JÁ CONHECIDOS COMO BONS (não precisa analisar; só inclua na lista final se ainda estiverem ativos)
@motion_ui_interface, @designmotionhq, @theglidestudio, @felvrabr, @shohan.designs, @_code_and_chill_, @code.xr, @ui.iliasmiah000, @ramotion, @dailywebdesign, @ui.pixel, @noahelhadedy

O QUE FAZER
1. Para cada perfil inicial, confira se existe e se está ativo (seguidores e data do último post). Se não existir ou não postar há mais de 6 meses, escreva "INATIVO: <motivo>" e passe para o próximo.
2. Para os ativos, analise os destaques, o link da bio e os 10 posts mais recentes. Escolha os 2 melhores posts ou Reels para este produto (mobile iOS-like, motion, perfil, portfólio, agenda, dashboards) e descreva cada um: link, o que mostra, regras ou números ensinados.
3. Para chegar a pelo menos 25 perfis ativos e relevantes, descubra novos pelas "Contas sugeridas" dos melhores perfis e por hashtags como #uidesign #uxdesign #motiondesign #iosdesign #appdesign #mobileui #productdesign. Descarte quem só reposta sem crédito, vende curso sem conteúdo ou não posta há mais de 6 meses.

FORMATO: para cada perfil:
### <nome> — @handle
- URL | tipo: perfil pessoal / página de marca / agência | ativo? | seguidores | último post
- Foco
- Tipo de conteúdo (carrossel didático, Reels de motion, showcase, repost)
- Nível (iniciante / intermediário / avançado)
- Por que seguir
- Risco de conteúdo raso ou só visual
- 2 melhores posts (link + o que ensina)

No final:
- Top 15 perfis para este produto, em ordem, com 1 linha de justificativa cada.
- Lista dos perfis descartados, com o motivo.

REGRAS
- Abra cada perfil antes de citar. Não invente handles nem números de seguidores.
- Só leia: não curta, não comente, não siga, não mande mensagem.

AO FINAL DA RODADA, gere o arquivo `rodada-9E.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas;
   - depois, TODAS as fichas, o Top 15 e os descartados;
   - no fim, "Fontes verificadas" e "Prints".
2. Prints: dos 2 melhores posts de cada perfil do Top 15, no máximo 2 prints por perfil. Nomeie como `9E_<handle>_<IDdopost>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-9E.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-9E.md` num ÚNICO bloco de código Markdown, com a lista de prints: nome | link do post | o que mostra.
```

---

## Rodada 9F: Facebook, YouTube, newsletters e comunidades

**Modelo:** Sonnet 5.5

```
Você é um pesquisador sênior de Product Design montando uma lista de fontes contínuas de aprendizado. Sua tarefa é ABRIR e VERIFICAR cada fonte, não citar de memória.

CONTEXTO DO PRODUTO
App de gestão de marca pessoal. Web: painel para gestor e cliente. Mobile do cliente: PWA, depois Capacitor (iOS/Android). Stack React 18 + TypeScript + Tailwind + shadcn/ui + Motion for React. Visual iOS-like. Público avançado, PT e EN.

PARTE 1: FACEBOOK (meta: 10 itens)
Comece por estes grupos:
45. https://www.facebook.com/groups/uxdesignercommunity/
46. https://www.facebook.com/groups/226816094176688/
47. https://www.facebook.com/groups/973224974974520/
48. https://www.facebook.com/groups/bestUXDesigners/
Depois, busque mais grupos e páginas de UI/UX, Figma, motion design, React e acessibilidade até chegar a 10 relevantes. NÃO peça para entrar em grupos: avalie só o que é visível publicamente (nome, descrição, tamanho, atividade, se é público ou privado).
Ficha: nome | URL | tipo (página / perfil / grupo público / grupo privado) | foco | tamanho | atividade recente | por que acompanhar | como usar sem perder tempo | risco (spam, autopromoção).

PARTE 2: YOUTUBE (meta: 15 canais ou playlists)
Busque canais de UI/UX, product design, motion design, Figma, design systems, React/Tailwind/shadcn e animação para front-end, em PT e EN. Confira cada canal: inscritos, data do último vídeo, playlists.
Ficha: nome | URL | foco | idioma | nível | inscritos | último vídeo | 2–3 melhores vídeos ou playlists (com link) | por que vale acompanhar.

PARTE 3: NEWSLETTERS, BLOGS E COMUNIDADES (meta: 15)
Inclua pelo menos 1 de cada: blog de design, newsletter de UX, newsletter de front-end, comunidade de design, comunidade de React, comunidade de Capacitor/Ionic, comunidade de acessibilidade e comunidade de motion design.
Ficha: nome | URL | tipo | frequência | gratuito/pago | foco | por que acompanhar.

No final:
- Top 5 grupos ou páginas do Facebook.
- Top 10 canais do YouTube.
- Top 10 newsletters ou comunidades.

REGRAS
- Abra cada URL antes de citar. Não invente nomes, números de inscritos nem vídeos.
- Para o Facebook, distinga claramente página, perfil e grupo.
- Não inclua fontes inativas há mais de 6 meses.
- Só leia: não entre em grupos, não siga, não se inscreva, não assine newsletters.

AO FINAL DA RODADA, gere o arquivo `rodada-9F.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas;
   - depois, as partes 1 a 3 e os tops;
   - no fim, "Fontes verificadas".
2. Prints: não são necessários nesta rodada, salvo algo excepcional (no máximo 5).
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-9F.md`.
   - Se não conseguir, entregue o conteúdo completo num ÚNICO bloco de código Markdown.
```

---

## Depois das rodadas

Cole os 6 arquivos `rodada-9A.md` a `rodada-9F.md` (e os prints) na sessão das skills no Claude Code. Lá eu monto o restante do pedido original:
- **1:** visão geral.
- **13:** plano em 3 fases.
- **14:** checklist de auditoria com 40–60 itens.
- **15:** entregáveis — tabela mestre, top 20 recursos, plano de estudo de 30 dias, plano de implementação de 90 dias e critérios de escolha da biblioteca.

Os achados também entram nas skills `mobile-app-ui`, `desktop-app-ui`, `ui-motion`, `ux-patterns` e `design-direction`.
