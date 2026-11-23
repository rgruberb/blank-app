---
name: website-ui
description: UI/UX específico de WEBSITE — sites institucionais, landing pages, páginas de vendas, portfólios, e-commerce/loja, blogs e páginas de produto/SaaS marketing. Traz regras com números para layout e grid, largura de conteúdo, breakpoints mobile-first, hero e acima da dobra, navbar/footer, CTA, tipografia fluida (Major Third 1,25), imagens e Core Web Vitals, motion de site (um momento animado por página, scroll reveal, reduced motion), SEO/semântica e acessibilidade (alvos 24/44px, contraste), formulários e confiança (NN/g), fontes de benchmark (Awwwards, Land-book, SiteInspire, Coolors, Typewolf), com workflow de verificação em 375/768/1280/1440 e ponteiros para as skills de tema. Use ao "criar site", "landing page", "página de vendas", "portfólio", "e-commerce", "loja online", "home do site", "site responsivo", "hero", "navbar", "footer", "pricing", "página de produto", "checkout", "blog" ou ao revisar um site existente. Web app de uso diário (dashboard SaaS) fica em desktop-app-ui.
---

# Website UI

Skill de **plataforma**: o que muda quando a tela é um **site** (visita curta, chega por busca/anúncio/link, rola,
decide e sai). As skills de **tema** continuam sendo a base: `design-direction` (direção, cor, tipo, marca),
`ui-motion` (valores de motion), `ux-patterns` (leis, números de UX) e `dashboard-ui`. Aqui fica só o que é
específico de site e o mapa para o resto. Padrões por seção/página: `references/website-patterns.md`. Imagens:
`references/visual-index.md`. Itens marcados **(complemento)** são conhecimento geral de plataforma (WCAG, Core Web
Vitals, convenções web), não vêm das fontes. Regras do NN/g e das galerias de benchmark lidas na pesquisa 9B/9C
(nov/2026) vêm com a fonte citada. Onde buscar referência visual: `references/benchmark-sources.md`.

## Escopo e fronteira
- **Esta skill:** site institucional, landing page/página de vendas, portfólio, loja (vitrine, produto, carrinho,
  checkout), blog/conteúdo, página de produto e marketing de SaaS, 404.
- **`desktop-app-ui`:** web app de uso diário (dashboard SaaS, painel admin, CRM, kanban, settings, ⌘K). Admin de loja
  é app, não site. Regra prática: se a pessoa **volta todo dia para trabalhar** na tela, é app; se **visita para
  entender/comprar**, é site.
- **`mobile-app-ui`:** app nativo/PWA instalado (tab bar, gestos, 44pt/48dp). O site **responsivo** em celular continua
  aqui.
- Fronteira cinzenta: área logada simples de loja (pedidos, endereço) segue esta skill; se virar painel com dados,
  passe para `desktop-app-ui`.

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

## Regras de website (com números)

**1. Layout e grid**
- Uma borda de alinhamento por coluna, margens generosas, nada flutuando; "a page that looks cared for gets believed"
  (`design-direction` → `layers-and-trust-layout.md` §2).
- Espaçamento em grade de **8** (8, 16, 24, 32, 48, 64; 4 só micro). Espaço entre seções = **2–3×** o espaço interno
  dos cards (complemento da fonte). Em site, seção grande usa os degraus altos: **64–128px** desktop, **48–64px**
  mobile (complemento).
- Grid de **12 colunas** desktop, **8** tablet, **4** mobile; gutter 24px (16px no mobile); margem lateral mínima
  **16–24px** no mobile (complemento).
- Alterne fundo escuro/claro (ou base/superfície) para marcar troca de capítulo (`DYpD5C7zwx6`; Tally no
  `claude-design-course.md`).

**2. Largura máxima de conteúdo** (complemento, salvo a medida)
- Container **1200–1280px** (frame de design em 1440); hero e mídia podem ir full-bleed.
- Texto corrido: token `--measure: 50ch` (≈ 66–71 caracteres); regra em caracteres: **45–75** (teto ~75) e
  **45–60** em formulários; conte na sua fonte — das fontes (`ux-patterns` →
  `typography-and-touch.md` §2/§2b). Nunca parágrafo na largura total do container.

**3. Breakpoints mobile-first** (complemento)
- CSS base = **375px**; `min-width` em **768**, **1024**, **1280**, **1440**. Teste também 320 (sem scroll horizontal).
- No mobile: 1 coluna, CTA visível sem rolar, navegação em menu; nada de hover como única forma de revelar conteúdo.

**4. Hero e "acima da dobra"**
- Headline curto + 1 subtítulo + **1 CTA primário** (secundário vira link). Nada de widgets competindo (chat, banner)
  acima da dobra (`layers-and-trust-layout.md` §2).
- **Título primeiro:** título e CTA no primeiro paint; "2 s em branco parecem uma hora" (`ux-patterns` →
  `ux-laws.md`, Doherty; `ui-motion` → `page-transitions-and-timing.md`).
- Identidade em camadas: cor + tipo → luz/vidro → movimento; trio sans + 1 palavra em serif itálico + mono em labels
  (`layers-and-trust-layout.md` §1). Detalhes em `website-patterns.md` §1.

**5. Navegação, header e footer**
- Navbar mínima: logo à esquerda, **3–5 links**, **1 CTA** colorido à direita (RWB Porsche `DYpD5C7zwx6`; glide:
  "nav reduzida a logo + Sign in"). Hick: menos opções, decisão mais rápida.
- Menu (mobile/fullscreen) **nasce do botão** que o abriu, fundo escurece; abre em **~0,7 s**, press em **0,16 s**
  (`ui-motion` → `page-transitions-and-timing.md`). Header sticky com altura ≤ 64–72px (complemento).
- Footer **sempre alcançável**: infinite scroll enterra contato e termos → "Load more, then stop" (`ux-patterns` →
  `components-checklists.md` §4).

**6. CTAs**
- **Verbo + objeto** ("Começar teste grátis", "Add to cart"), nunca "Enviar/OK". Altura **≥ 44px (alvo 48)**, padding
  lateral **24px**, label ≥ **4,5:1**, borda ≥ **3:1**, latência de resposta **≤ 100ms** (`components-checklists.md` §1–2).
- O **acento só no CTA** e em 1 dado/palavra; ≤ **10%** da área (60/30/10). `Dfc-Q-0yy0W` é a melhor referência
  (`design-direction` → `color-palettes.md`).
- Mesmo CTA primário repetido no hero e no CTA final, com o mesmo texto (complemento).

**7. Tipografia fluida — use Major Third 1,25 em site**
- `ux-patterns` registra a divergência **1,2** (`DfjxqzkCrUI`) vs **1,25** (`DfRucYFjrac`, `De_FtT3k-tT`). **Em site,
  use 1,25**: (a) as duas fontes de 1,25 tratam de hierarquia de site/editorial (`De_FtT3k-tT` rotula 39px como
  "Hero/H1"); (b) site tem poucos níveis por tela e precisa de **contraste forte** entre headline e corpo, enquanto 1,2
  serve a produto denso (app/dashboard). Escala: **12,8 · 16 · 20 · 25 · 31 · 39 · 49** (+61 só no hero desktop,
  complemento).
- Fluida (complemento): `clamp()` por degrau, ex. h1 `clamp(2.441rem, 1.6rem + 3.5vw, 3.815rem)` (39→61px), corpo
  **16px** mobile → **18px** desktop no máximo. Nunca `vw` puro (quebra zoom).
- Line-height **1,5** corpo → **1,1** display; tracking **−0,02em** títulos ≥ 39px, **+0,05em** caps; 2–3 famílias, o
  mesmo par no site inteiro (`design-direction` → `typography-pairing.md`). Carregue a fonte de verdade
  (`display=swap`, self-host, ≤ 2–3 pesos) — `ux-patterns` → `dark-patterns.md` §C; `perceived-performance.md` item 29.
- Escolher fonte livre: **Typewolf "40 Best Google Fonts"** (9C, atualizada 12/01/2026; open source, uso comercial,
  famílias com vários pesos). Confira acentos PT na página de cada fonte; as fontes da home do Typewolf (Neue Montreal,
  Suisse, Canela…) costumam ser **pagas**. Pares: `design-direction` → `typography-pairing.md`.

**8. Imagens e performance / Core Web Vitals**
- Das fontes (`perceived-performance.md`): WebP/AVIF (02), CDN (06), Brotli (09), lazy loading fora da tela (15), SSR
  ou build estático (20), scripts de terceiros depois (21), code splitting (22), cache (27), fontes próprias com
  poucos pesos (29), testar no celular em rede lenta (31).
- Metas (complemento): **LCP ≤ 2,5 s**, **INP ≤ 200 ms**, **CLS ≤ 0,1** (p75, mobile). Imagem do hero **sem lazy**,
  com `fetchpriority="high"`; toda imagem com `width`/`height` ou `aspect-ratio` (reserve espaço, como na paginação:
  shift de 68px = toque errado); `srcset`/`sizes`; hero ≤ ~200 KB.
- WebGL/vídeo de fundo: **≤ 1 por página**, pausar fora da tela, fallback estático no mobile (`ui-motion` →
  `react-bits.md`).

**9. Motion de site**
- **Um momento animado por página: hero OU CTA**, não os dois; "se tudo mexe, nada é especial". Feedback funcional
  (press, hover, foco) não conta (`ui-motion` → `scroll-and-screen-transitions.md` §5).
- Scroll reveal: **≤ 700 ms** ease-out, deslocamento ~24px, stagger **70–100 ms**, **uma vez só**, nunca no conteúdo já
  visível no load; sem scroll-jacking; sem parallax decorativo no mobile (§1–§4).
- 5 padrões de site (headline reveal, micro-interactions, portfolio showcase, animated gallery, scroll reveal): escolha
  **1 expressivo**, um efeito por vez, teste desktop e mobile (§6).
- `prefers-reduced-motion`: troque deslocamento por fade ≤ 150 ms ou corte; mantenha estados.

**10. SEO e semântica** (complemento)
- Um `<h1>` por página; hierarquia h2/h3 sem pular; landmarks `header`/`nav`/`main`/`footer`; `<a>` para navegar,
  `<button>` para agir; `lang="pt-BR"`.
- `<title>` ≤ ~60 caracteres, meta description ~150, Open Graph/Twitter card, canonical; `alt` descritivo (vazio em
  decorativa); JSON-LD por tipo (Organization, Product, Article, FAQPage, BreadcrumbList).
- Conteúdo principal no HTML servido (SSR/SSG), URLs legíveis, estado de filtro/página na URL (`?page=&sort=`).

**11. Acessibilidade**
- Alvos web: piso **24×24px** (WCAG 2.2 AA 2.5.8), **meta 44** (AAA); cresça por padding; **~8px** entre alvos
  (`ux-patterns` → `typography-and-touch.md` §1). Links inline no texto são isentos do piso (complemento).
- Contraste: texto **4,5:1**, texto grande (24px / 19px bold), ícones e bordas **3:1**; texto sobre foto com scrim
  medido **no ponto mais claro** (§3). Focus ring visível; skip link "Pular para o conteúdo" (complemento).
- Dark mode: sem `#000` (ex. `#0C1424`), texto ~87% (§4). Formulários: label visível, erro em texto, não só cor.
- Medir contraste: **Coolors contrast checker** (coolors.co/contrast-checker, 9C) — AA **4,5:1** texto normal e **3:1**
  texto grande (≥ 18pt ou negrito); AAA **7:1** e **4,5:1**. Teste cada par de token claro **e** escuro; paleta bonita
  não define papel semântico (texto, borda, estado). NN/g (9B): teste também em escala de cinza e com foco visível espesso.

**12. Formulários e confiança (NN/g web, 9B)**
- **Não peça antes de entregar valor.** Hierarquia de confiança em 5 níveis: relevância → preferência → dado pessoal
  → dado sensível/financeiro → relação contínua. Não pule degraus: cadastro/login obrigatório para ver conteúdo,
  "agende uma demo" antes de mostrar preço, ou conta social conectada (nível 5) na primeira visita espantam. Mostre
  conteúdo, preço e prova antes do formulário; deixe explorar.
- Formulário: **coluna única**, grupos nomeados, poucos campos (só o necessário), "(opcional)" marcado, tempo estimado
  em formulário longo; **rótulo visível, nunca placeholder como rótulo**; exemplo de formato; validação **depois** que
  o campo termina, erro **ao lado do campo** com cor + ícone e texto que diz como corrigir; ajuda extra após **3 erros**;
  resumo no topo nunca sozinho; erro nunca em tooltip. Botão de enviar **abaixo dos campos**.
- Microcopy (3 I's: informar, influenciar, interagir): < 3 frases; o botão diz **o que acontece** ("Receber o orçamento"),
  explique por que pede cada dado ao lado do campo.

## Checklist de entrega
- [ ] 1 h1, 1 CTA primário por seção, acento ≤ 10% e só em CTA/dado-chave.
- [ ] Escala 1,25 em tokens, corpo 16–18px, parágrafos ≤ `--measure` (50ch; 45–75 caracteres), line-height caindo com o tamanho.
- [ ] Grade de 8; container ≤ 1280px; sem scroll horizontal em 320/375.
- [ ] Título + CTA no primeiro paint; nada competindo acima da dobra.
- [ ] Um momento animado; reveal ≤ 700 ms, uma vez; `prefers-reduced-motion` testado.
- [ ] LCP ≤ 2,5 s, CLS ≤ 0,1 em mobile throttled; imagens com dimensões, WebP/AVIF, lazy abaixo da dobra.
- [ ] Alvos ≥ 24px (meta 44), contraste 4,5/3:1, foco visível em todo link/botão, navegação por Tab completa.
- [ ] Title/description/OG, landmarks, alt, JSON-LD do tipo de página.
- [ ] Sem dark pattern: prova social real, sem plano-isca, trial com aviso (`ux-patterns` → `dark-patterns.md` §A).
- [ ] Estados desenhados: vazio, carregando, erro, texto longo; 404 dentro do sistema de marca.
- [ ] Nenhum cadastro/dado pessoal pedido antes de o visitante ver valor (conteúdo, preço, prova).
- [ ] Formulário em 1 coluna, rótulo visível, validação após o campo, erro ao lado com texto e ícone.
- [ ] Pares de cor medidos (Coolors/DevTools) em claro e escuro, não estimados.

## Workflow
1. **Brief:** tipo de site, público, objetivo da página (1 ação), faixa de preço/posicionamento (visual comunica
   preço: `design-direction` → `branding-identity.md` §3), conteúdo real disponível.
2. **Direção:** siga `design-direction` (2+1 com hex, par tipográfico, terceira camada). Peça 2–5 referências; URL →
   `ext-extract-design`. Anti-genérico: `ext-taste-skill`. Onde achar referências (Awwwards, Land-book, SiteInspire)
   e como usar sem copiar: `references/benchmark-sources.md`.
3. **Estrutura de seções:** monte a ordem com `references/website-patterns.md` (ex. landing: hero → prova social →
   problema/benefícios → features → como funciona → pricing → FAQ → CTA final → footer). Escreva o copy antes do
   visual; uma ideia por seção.
4. **Build:** tokens primeiro (cor, escala 1,25, espaço, motion de `ui-motion`), HTML semântico mobile-first, depois
   camadas (identidade → profundidade → movimento, um efeito por vez).
5. **Verificar** com `ext-playwright-cli`: screenshots em **375, 768, 1280 e 1440** (página inteira); conferir scroll
   horizontal, CTA acima da dobra em cada largura, tamanho dos alvos (`getBoundingClientRect`), Tab/foco, emulação de
   `prefers-reduced-motion`, fonte carregada em browser limpo, rede lenta. Crítica final: `ext-impeccable`
   (audit/polish), `design:accessibility-review`.

## Onde está o resto
| Preciso de… | Abra |
|---|---|
| Paleta 2+1, hex, 60/30/10, rampas | `design-direction/references/color-palettes.md` |
| Camadas, layout de confiança, 5 tipos de movimento, sombra tingida | `design-direction/references/layers-and-trust-layout.md` §1–4 |
| Par de fontes (12 pares por tom) | `design-direction/references/typography-pairing.md` §2 |
| Marca, logo, visual × preço, páginas de marca, 404 | `design-direction/references/branding-identity.md` §3, §5, §7 |
| Prompts de web design, site "Relay" seção a seção, bibliotecas | `design-direction/references/claude-web-design-workflow.md` |
| Landing no Claude Design (sketch, hi-fi, deploy) | `design-direction/references/claude-design-course.md` (40:45, 1:42) |
| Onde scroll/reveal faz sentido, 1 momento, 5 padrões de site | `ui-motion/references/scroll-and-screen-transitions.md` §1–6 |
| Durações (press/reveal/cena), card→página, menu | `ui-motion/references/page-transitions-and-timing.md` |
| Snippets (stagger, View Transitions, reduced motion) | `ui-motion/references/css-recipes.md` |
| Componentes animados prontos, orçamento WebGL | `ui-motion/references/react-bits.md` |
| Vídeo do site, scroll-storytelling | `ui-motion/references/motion-for-social-video.md` §3–4 |
| Escala 1,2 vs 1,25, alvos, contraste, grade de 8 | `ux-patterns/references/typography-and-touch.md` §1–3, §6 |
| Botão, paginação, decisão, fluxo de pedido | `ux-patterns/references/components-checklists.md` §1–2, §4, §9–10 |
| Leis (Fitts, Von Restorff no pricing, Closure, checkout) | `ux-patterns/references/ux-laws.md` |
| Dark patterns, fonte genérica | `ux-patterns/references/dark-patterns.md` §A, §C |
| Performance (31 itens) | `ux-patterns/references/perceived-performance.md` |
| Glassmorphism (vidro sobre foto) | `dashboard-ui/references/glassmorphism.md` |
| Web app/dashboard | skill `desktop-app-ui` (e `dashboard-ui`) |
| Pesquisa NN/g completa (formulários, confiança, microcopy) | `ux-patterns/references/nng-research.md` |
| Galerias de benchmark (Awwwards, Land-book, SiteInspire, Coolors, Typewolf) e prints da pesquisa 9 | `references/benchmark-sources.md` |
| Kits Figma (Obra shadcn) e blocks prontos de login/conta (shadcn, Supabase Library) | `desktop-app-ui/references/component-libraries.md` §"Referências prontas" |
| Implementação de motion | `ext-gsap-scrolltrigger`, `ext-transitions-dev` (accordion, tabs, toast) |
