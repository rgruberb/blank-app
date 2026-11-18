# Rodada 1: design visual, UI/motion e componentes

*Coletado em 18/11/2026, só leitura: nenhuma curtida, comentário ou follow. Dos 8 links, 7 foram lidos. O `DfkSCaRNfa0` está indisponível (veja o fim do documento).*

## Resumo da rodada

1. **Paleta como rampa de 6 tons:** os carrosséis de @uiuxaadi usam sempre 6 cápsulas, do mais escuro ao mais claro, e às vezes um acento contrastante no fim (laranja, rosa, âmbar). O formato já entrega fundo, superfície, borda, texto e acento.
2. **Os hex desses posts precisam de conferência:** no slide Ruby, o rótulo `#243A66` (um azul) está sobre um swatch rosa, e um comentário apontou isso. Além disso, a legenda promete 8 paletas e o carrossel tem 7 (falta "Plum"). Nunca copie hex de post sem conferir no conta-gotas.
3. **Regras de sistema da @gg.designhub:**
   - espaçamento em múltiplos de 8 (4 px só para micro);
   - cor em 60/30/10;
   - escala tipográfica Major Third de 1,25 (16→20→25→31→39);
   - sombra tingida com a cor do fundo, blur = 2× o Y e opacidade baixa (~8%);
   - linha de 45–75 caracteres, entrelinha de 140–160% no corpo e 110–120% em títulos.
4. **Font pairing (@gfx.om):** 12 pares de display + corpo (Playfair + Montserrat, Lora + Open Sans, Fraunces + Inter…). Dicas: 2–3 fontes, contraste entre display e corpo, hierarquia por pesos, e o mesmo par em tudo.
5. **Motion web (@mobileeditingclub):** cinco padrões (headline reveal, micro-interações, portfolio showcase, galeria animada e scroll reveal). O fluxo recomendado é passar visuais, cores da marca e uma descrição clara do movimento, fazer um efeito por vez e testar no desktop e no mobile.
6. **Skills de design para Claude Code (@matheustilli):** 42 skills organizadas em 6 camadas: UI, imagem/vídeo, produto/interação, conteúdo, qualidade/avaliação. Segundo a legenda, são 18 repositórios, e um deles traz 16 das 42. Os links só saem pelo "comente".
7. **Bibliotecas de componentes para IA (@griffinwooldridge1):** Bencho, BoardUI, Transitions.dev e Beautiful UI, todas com estética dark e cards arredondados. Um comentário dá o teste certo antes de adotar: estados vazio, carregando, erro e texto longo.
8. **Padrão de CTA:** 4 dos 7 posts pedem "comente X para receber". O valor real fica fora do post, e a informação útil é o que está visível nos slides.

---

## Blocos

### DfEmKLLFEDi — @uiuxaadi
- Link: https://www.instagram.com/p/DfEmKLLFEDi/ · 29/10/2026 (selo "AI content"; colab. com @figma.tutors)
- Tipo: carrossel (9 slides)
- Tema: design visual
- Legenda: anuncia 9 paletas premium para projetos de UI e lista uma por linha, com emoji e dois adjetivos de clima: 💜 Purple Haze (futurista e elegante), 🌿 Forest Glow (fresca e terrosa), 🧡 Sunset Fusion (vibrante e enérgica), 🌸 Rose Blush (ousada e divertida), 🌊 Arctic Blue (fria e profissional), 🩵 Ocean Teal (calma e moderna), 💗 Neon Pop (vibrante e chamativa), 🫒 Olive Luxe (natural e sofisticada), 🤎 Mocha Earth (quente e atemporal). Pede para salvar, pergunta qual paleta a pessoa escolheria e manda seguir @uiuxaadi. Hashtags: #uidesign #uxdesign #colorpalette #figmadesign #designinspiration. (O autor fixou um comentário oferecendo "100+ paletas" para quem comentar "Colours".)
- Slide a slide (layout igual em todos: 6 cápsulas arredondadas empilhadas e sobrepostas, da mais escura no topo à mais clara, com o hex em sans pequena dentro de cada uma; fundo escuro com dois brilhos difusos laterais na cor de acento; `@uiuxaadi` em cinza com fio embaixo, no rodapé. Os nomes das paletas **não aparecem** nos slides; a correspondência abaixo é inferida pelas cores):
  1. Mocha Earth — `#1A120E` `#3A2418` `#6B4A2E` `#A88462` `#D5C4AE` `#4A4A46` (brilho laranja-âmbar)
  2. Purple Haze — `#0E0B1D` `#2A1E4D` `#5A3B8C` `#8B7CC7` `#C9C2E3` `#3A3A52` (brilho violeta)
  3. Forest Glow — `#0F1F17` `#1E3A2E` `#3E5A3F` `#6B7F67` `#C7CBB8` `#3D4337` (brilho verde-lima)
  4. Arctic Blue — `#0B132B` `#1C2541` `#3A506B` `#5BC0DE` `#F4D6B0` `#D97706` (brilhos laranja à esquerda e azul à direita)
  5. Neon Pop — `#121212` `#1F2937` `#334155` `#64748B` `#F1F5F9` `#EC4899` (brilhos magenta e ciano)
  6. Ocean Teal — `#0A0F14` `#0F3D3E` `#2E6F73` `#7FB3B8` `#EADCC8` `#C6601F` (brilhos laranja e teal)
  7. Rose Blush — `#1A0F2E` `#3B1B4F` `#7A2E6F` `#D6598F` `#F4D7D4` `#FF6B6B` (brilhos vermelho e azul)
  8. Sunset Fusion — `#1A1A1F` `#2D2B55` `#6A5ACD` `#A678B9` `#F0D9B5` `#F4A62A` (brilhos âmbar e violeta)
  9. Olive Luxe — `#0B0F0D` `#1F2A1F` `#3E5A3F` `#8CA98C` `#D9C7A3` `#B08D57` (brilhos âmbar e verde)
- Regras/lições práticas:
  - Monte a paleta como rampa: 3–4 tons de fundo/superfície + 1 claro (texto/superfície clara) + 1 acento ou neutro.
  - Um acento quente sobre uma base fria (azul/teal + laranja) cria hierarquia de CTA sem acrescentar cores.
  - Repetir o mesmo template em todos os slides deixa a comparação direta e fortalece a identidade do perfil.
  - Ressalva: o post não mostra contraste (WCAG) nem estados como erro e sucesso. Um comentário lembra que, em produto, o que decide a paleta é o contraste dos neutros e o comportamento nos estados.

### DfUnwyQGCTA — @uiuxaadi
- Link: https://www.instagram.com/p/DfUnwyQGCTA/ · 04/11/2026 · ~2,5 mil compartilhamentos
- Tipo: carrossel (7 slides)
- Tema: design visual
- Legenda: anuncia "8 paletas incríveis" para UI, cada uma com dois adjetivos: Ruby (ousada e romântica), Aqua (fresca e futurista), Forest (calma e natural), Plum (elegante e luxuosa), Violet (criativa e moderna), Monochrome (atemporal e minimalista), Slate (elegante e profissional), Serenity (suave e relaxante). Pede para salvar e seguir. Hashtags: #uiuxdesign #colorpalette #uidesign #designinspiration #figma webdesign colortheory.
- Slide a slide (mesmo template do post anterior: 6 cápsulas empilhadas com hex em sans, fundo com brilho na cor da paleta e `@uiuxaadi` entre fios no rodapé):
  1. Ruby — `#800021` `#881144` `#243A66` ⚠️ `#C24366` `#FF69B4` `#FFE4D8`. **O terceiro rótulo está errado:** `#243A66` é azul-marinho, mas o swatch é magenta.
  2. Monochrome — `#0B0B0B` `#1A1A1A` `#333333` `#6B6B6B` `#D9D9D9` `#FFFFFF` (brilho branco)
  3. Violet — `#0B0720` `#25134D` `#6A2FC8` `#9D71E8` `#D1B8FF` `#F2E9FF`
  4. Aqua — `#05161A` `#072E33` `#0C7075` `#0F969C` `#6DA5C0` `#294D61` (brilho ciano)
  5. Forest — `#051F20` `#0B2B26` `#163832` `#235347` `#8EB69B` `#DAF1DE`
  6. Serenity — `#F7CBCA` `#DDD3D3` `#F1F7F7` `#D5E5E5` `#BDD7D8` `#5D6B6B`. É a única com fundo claro: degradê rosa/azul-acinzentado e ordem invertida (clara em cima).
  7. Slate — `#06141B` `#11212D` `#253745` `#4A5C6A` `#9BA8AB` `#CCD0CF`
  - **A paleta "Plum" da legenda não existe no carrossel** (7 slides para 8 nomes).
- Regras/lições práticas:
  - Paletas monocromáticas de 6 passos servem como escala de superfícies (bg → card → borda → texto secundário → texto).
  - Paletas claras (Serenity) pedem ordem invertida e fundo claro; o template se adapta.
  - Sempre confira os hex: este post tem um rótulo errado e uma paleta faltando.

### Dff1uulGoxb — @mobileeditingclub (com @adrianabubori)
- Link: https://www.instagram.com/p/Dff1uulGoxb/ · 08/11/2026 (selo "AI content")
- Tipo: carrossel (7 slides: 1 imagem + 5 vídeos de 6–17 s + 1 imagem)
- Tema: UI/motion
- Legenda: CTA "comente WEBSITE" para receber o fluxo completo. A ideia é usar o Claude para dar movimento a um site, de uma revelação de título até uma galeria que muda conforme o visitante explora. Lista cinco formas:
  - headline reveal: animação curta de abertura, legível e sutil;
  - micro-interações: hover, deslocamento de imagem e transições entre detalhes do produto;
  - portfolio showcase: transições que guiam pelos projetos e dão contexto;
  - galeria animada: imagens reveladas uma após a outra;
  - scroll reveal: imagens, detalhes e texto entrando conforme o scroll.

  Recomenda dar ao Claude os visuais, as cores da marca e uma descrição clara do movimento, construir um efeito por vez e checar no desktop e no mobile. Hashtags: #ai #claude #webdesign #websiteanimation #contentcreation.
- Slide a slide:
  1. **Capa (imagem):** retrato editorial de uma mulher com luvas de tule vinho e chapéu bordô, fundo amarelo-pálido (~`#E8E3A6`). Texto branco em grotesk pesada: "How to animate / **Websites** / with / **Claude**". Etiquetas tipo cursor do Figma: "Animation" (rosa ~`#F06BA8`), "Interaction" (laranja ~`#F08A1C`), "Motion" (azul ~`#4FA8E8`). Botão laranja em pílula "OUR WORKFLOW →". Logo "MOBILE EDITING CLUB" no canto.
  2. **/headline-reveal (vídeo 14,7 s):** fundo creme (~`#F4EEE6`). Instrução no topo em sans preta com trecho realçado em marrom-claro: dê ao Claude imagem do produto, headline e cores da marca, e peça um hero com revelação suave da imagem e texto em sequência, com movimento sutil. Mockup de navegador mostra o splash "MEC", depois um hero escuro ("…mornings you actually have"), uma seção de stats (60 / 40 / 0, "Two ingredients on the label. That is the whole list.") e "Start with one bottle." Título grande "/headline-reveal", barra de progresso e etiqueta "Motion".
  3. **/micro-interactions (vídeo 16,5 s):** fundo marrom-café (~`#2E1F1C`), texto branco com realce rosado. Pede um leve deslocamento da imagem no hover, resposta clara do botão ou transição suave entre detalhes do produto, um efeito de cada vez. Mockup de site de cosméticos: lábios em close, depois "your own flush." com lista de tons e swatches de blush. Etiqueta "Interaction" azul.
  4. **/portfolio-showcase (vídeo 15,1 s):** creme. Pede um showcase com transições de imagem suaves e navegação simples entre projetos, deixando o trabalho em destaque com pouco texto. Mockup "MFC Films" (serif itálica dourada sobre foto) e depois "FW'26" com retrato editorial. Etiqueta "Transition" rosa.
  5. **/animated-gallery (vídeo 14,8 s):** marrom-café. Pede imagens reveladas uma após a outra com movimento sutil, espaçamento consistente e layout limpo. Mockup "FILMS IN / Maison Véra" (serif) e depois uma faixa de fotos em sequência. Etiqueta "Animation" mostarda.
  6. **/scroll-reveal (vídeo 6,3 s):** creme. Pede que produto, imagens e texto entrem conforme o scroll, com sequência clara, transições suaves e próxima ação fácil de achar. Mockup com mãos segurando um produto e "MEC" gigante. Etiqueta "Flow" azul.
  7. **CTA (imagem):** marrom-café, "Comment [WEBSITE em pílula laranja] and we'll send you the full workflow for free", P.S. para seguir e checar as DMs, e o wordmark "MOBILE EDITING CLUB" no rodapé.
  - Sistema visual: dois fundos alternados (creme ~`#F4EEE6` / café ~`#2E1F1C`), grotesk preta pesada nos títulos com prefixo "/" (estilo comando), etiquetas de cursor coloridas por tipo de movimento e mockup de navegador centralizado numa moldura bege.
- Regras/lições práticas:
  - Para pedir animação a uma IA, entregue os assets, as cores da marca e uma descrição verbal do movimento (o quê, em que ordem, com que intensidade).
  - Construa e valide **um efeito por vez**, no desktop e no mobile.
  - Movimento sutil, com o texto sempre legível; o movimento serve para guiar até a próxima ação.
  - Os cinco padrões cobrem o ciclo da página: entrada (hero), resposta (hover), navegação (showcase), descoberta (galeria) e progressão (scroll).

### De_FtT3k-tT — @gg.designhub
- Link: https://www.instagram.com/p/De_FtT3k-tT/ · 27/10/2026
- Tipo: carrossel (8 slides)
- Tema: design visual (sistema de design)
- Legenda: "Bom design não é adivinhação, é sistema." Diz que 5 "cheat codes" (espaçamento, proporção de cor, tipografia, sombras e legibilidade) ajudam a decidir com mais consistência. Pede para salvar antes do próximo sprint e se apresenta: Guhan Gnanakrishnan, fundador e diretor criativo do estúdio GG Design Hub. Hashtags: #GGDesignHub #GuhanGnanakrishnan #GraphicDesignTips #BrandIdentity #designfundamentals.
- Slide a slide (fundo branco/cinza-claro ~`#F4F4F5`, grotesk bold preta no título com a segunda linha em cinza ~`#6B6B6B`, render 3D à direita e caixa "Takeaway" cinza no rodapé):
  1. **Capa:** "6 Design Cheat Codes / That Feel Illegal to Know." Subtítulo: "Stop guessing layout math, color contrast, and font scales." Botão contornado "Swipe for the vault →". Cofre de metal 3D com pastas Spacing / Color / Typography / Shadows / Readability. **Inconsistência:** a capa diz 6 e o conteúdo tem 5.
  2. **#01 The Universal Spacing Scale Rule – Multiples of 8:** pílula "8, 16, 24, 32, 48, 64 px" e fita métrica amarela marcada 8…64. Sub-rule: 4 px só para padding de ícone compacto e micro-badges. Why it matters: "elimina 90% da inconsistência entre breakpoints" (afirmação sem fonte). Pro-tip: nunca ajuste à mão com valores como 13 px ou 27 px.
  3. **#02 The Perfect Palette Ratio:**
     - 60% Dominant: canvas neutro (branco, dark slate, cinza suave);
     - 30% Secondary: cards, superfícies, subtítulos, molduras;
     - 10% Accent/Pop: CTAs, estados interativos, destaques de dado.

     Placas 3D empilhadas (branco 60%, lavanda ~`#D9D6F5` 30%, roxo ~`#6D4AE8` 10%). Takeaway: se o design parece poluído, o acento de 10% está cobrindo 30% da tela.
  4. **#03 Fail-Safe Type Hierarchy:** tabela 39 px Hero/H1 (31×1,25), 31 px H2 (25×1,25), 25 px H3 (20×1,25), 20 px Subhead (16×1,25), 16 px Base Body. Pedra entalhada com amostras ("Build a Stronger Brand", "Design Systems That Work"…). Takeaway: use a escala Major Third (1,250).
  5. **#04 Kill Pure Black Shadows:** erro de iniciante é usar `rgba(0,0,0,0.25)`, que fica sujo e artificial. O certo é pegar o matiz do fundo, baixar o brilho e usar opacidade baixa ("Color-Tinted Shadow", ex.: navy profundo para cards azuis). Fórmula: **blur = 2× o Y-offset**, ex. Y 8 px · Blur 16 px · Opacity 8%. Placas azuis 3D (~`#DCE6F8` → `#4A6FB5`).
  6. **#05 Line Length & Legibility:** largura ideal de 45–75 caracteres por linha (com espaços). Entrelinha de ouro: corpo 140–160%, títulos 110–120%. Laptop com exemplo "Within 45–75 characters" (✓ verde) vs "Too long" (✗ vermelho). Takeaway: linha longa cansa o olho; linha curta quebra o ritmo.
  7. **The Speed Run – 5 Second Recap:** Spacing (múltiplos estritos de 8 px) · Color (60% base / 30% surface / 10% pop) · Scale (multiplique por 1,25) · Shadows (tingidas, nunca preto chapado) · Reading (máx. 75 caracteres por linha). Cards flutuantes ilustram cada regra.
  8. **CTA:** "Level up your design fundamentals." Ícones 3D Save (branco) + Follow (preto), "Follow @gg.designhub" e a fileira Like / Comment / Share / Save for later.
- Regras/lições práticas:
  - Grid de 8 px para todo espaçamento; 4 px só em micro-elementos.
  - Distribuição de cor 60/30/10, com o acento restrito a CTA, estados e dados-chave.
  - Escala tipográfica modular 1,25 a partir de 16 px: 16 / 20 / 25 / 31 / 39.
  - Sombra com o matiz do fundo, opacidade em torno de 8% e blur = 2× o Y.
  - Linha de 45–75 caracteres; entrelinha de 1,4–1,6 no corpo e 1,1–1,2 em títulos.
  - Dúvida levantada nos comentários: o 60/30/10 é proporção de **área**, não de opacidade.

### DescJ2zTeSf — @gfx.om
- Link: https://www.instagram.com/p/DescJ2zTeSf/ · 19/10/2026 (selo "AI content")
- Tipo: imagem única (infográfico)
- Tema: design visual (tipografia)
- Legenda: "Font Pairing 😀" (é a legenda inteira).
- Slide a slide (imagem única):
  - **Cabeçalho:** sobrelinha "BETTER FONTS = BETTER DESIGNS", título "**Font** Pairing" (bold + regular) e subtítulo "The perfect combination of fonts can make your design look more professional, clean and memorable." À direita, "DIFFERENT FONTS. BETTER TOGETHER." com um texto curto e três ícones: Headings (Bold/Display), Subheadings (Medium/Semibold), Body Text (Regular/Light).
  - **Grade 3×4 de cards brancos com borda fina.** Cada card tem número em badge preto, categoria, o nome das duas fontes renderizado nelas mesmas, uma frase-exemplo e três bolinhas de cor (cores aproximadas):
    1. Modern & Clean — Playfair Display + Montserrat (preto, cinza, cinza-claro)
    2. Bold & Minimal — Montserrat + Lato (preto, azul ~`#2F6FD6`, cinza)
    3. Elegant & Classic — Bodoni Moda + Poppins (navy, navy, cinza)
    4. Creative & Stylish — Pacifico + Montserrat (coral ~`#F26B6B`, laranja ~`#F5A142`, pêssego)
    5. Strong & Modern — Lora + Open Sans (verde-escuro ~`#1F4D3A`, verde-médio, verde-claro)
    6. Minimal & Stylish — Helvetica Neue + Source Sans Pro (preto, cinza, cinza-claro)
    7. Vintage & Classic — Abril Fatface + Raleway (marrom ~`#7A4A2B`, caramelo, bege)
    8. Tech & Modern — Rajdhani + Roboto (roxo ~`#7B3FD1`, azul, lavanda)
    9. Soft & Friendly — Quicksand + Nunito (teal ~`#1E9A9A`, teal-claro, menta)
    10. Luxury & Premium — Cormorant Garamond + Lato (dourado ~`#B8955A`, areia, bege)
    11. Edgy & Bold — Anton + Muli (preto, vermelho ~`#E02424`, cinza)
    12. Fresh & Modern — Fraunces + Inter (verde-oliva ~`#4E6B3A`, sálvia, verde-claro)
  - **Faixa "Quick Tips for better font pairing":** Keep it simple (2–3 fontes por design) · Create contrast (display + fonte limpa) · Think hierarchy (pesos diferentes para estrutura clara) · Be consistent (o mesmo par no projeto todo). Rodapé: `@gfx.om`.
- Regras/lições práticas:
  - Combine uma fonte de personalidade (serif, display ou script) nos títulos com uma sans neutra no corpo.
  - Use no máximo 2–3 famílias e construa a hierarquia com pesos (Bold / Semibold / Regular), não com mais fontes.
  - Escolha o par pelo tom da marca (luxo, tech, amigável) e mantenha o mesmo par em todas as peças.
  - Todas as fontes listadas existem no Google Fonts, exceto Helvetica Neue, que é comercial (pergunta que apareceu nos comentários).

### DfFBFpXDZLv — @matheustilli
- Link: https://www.instagram.com/p/DfFBFpXDZLv/ · 29/10/2026 · ~1,9 mil comentários
- Tipo: carrossel (7 slides)
- Tema: outro (ferramentas de IA para design / UX)
- Legenda: pede para comentar "9T36N" para receber o link de cada uma das 42 skills. Explica que o carrossel só traz os nomes das 42 skills de design para o Claude Code, e nome sem link não instala nada. O guia traz, para cada uma, o repositório, o caminho do SKILL.md, a licença e a data do último commit. Destaca que não são 42 instalações, e sim 18 repositórios, e que um deles traz 16 das 42. Hashtags: #claudecode #uiux #designdeproduto #inteligenciaartificial #github.
- Slide a slide (fundo papel creme ~`#F3ECDF` com marcas de corte e mira nos cantos, display condensada preta (estilo Anton/Bebas), rótulos em monospace, acentos azul ~`#1E9BE9`, vermelho ~`#F0443A` e verde ~`#3DDC5A`, mascote 3D de pelúcia laranja, paginação "0X / 07" e "ARRASTA →"):
  1. **Capa:** "O CLAUDE CODE É [RUIM em caixa vermelha] EM [DESIGN. em faixa azul]" / "ESSAS 42 SKILLS [CORRIGEM em verde] ISSO." Selo "42 / 42 COM FONTE PÚBLICA", ícones de asterisco (Claude) e GitHub, mascote cortando uma interface com tesoura.
  2. **Camada 1 · Construção visual – FRONTEND E UI** (selo "02 / 42 · fontes confirmadas"):
     01 frontend-design (interface com direção visual forte) · 02 impeccable (audita e lapida a interface) · 03 taste-skill (direção estética com intenção) · 04 make-interfaces-better (microinteração e acabamento) · 05 color-expert (cor em OKLCH e contraste) · 06 design-tokens-skill (tokens consistentes e escaláveis) · 07 design-system-governance (governa o design system) · 08 brandkit (identidade visual numa rodada) · 09 format-storybook (Storybook pronto pro handoff) · 10 mobile-app-design (interface móvel no padrão nativo).
  3. **Camada 2 · Criação visual – IMAGEM, GRÁFICOS E VÍDEO:**
     11 canvas-design (arte visual e vetor editável) · 12 algorithmic-art (arte generativa com p5.js) · 13 p5js-hermes (experimento criativo em código) · 14 shader-dev (shader e gráfico em tempo real) · 15 animate-skill (animação guiada por intenção) · 16 css-animation-skill (movimento direto em CSS) · 17 wiggle-claude-skill (SVG pra Lottie, GIF e MP4) · 18 remotion-best-practices (vídeo em React com boas práticas).
  4. **Camadas 3 e 4 · Experiência – PRODUTO E INTERAÇÃO:**
     19 work-with-design-systems (reutiliza componentes e tokens reais) · 20 extract-design-md (extrai regras do design existente) · 21 taste-design-stitch (refina telas geradas no Stitch) · 22 design-html (transforma direção em HTML visual) · 23 information-architecture-and-navigation (arquitetura e navegação claras) · 24 interfaces-that-feel (interações com sensação intencional) · 25 search-ux (busca que ajuda o usuário) · 26 neo-user-journey (mapeia jornadas e fricções) · 27 design-auditor (encontra inconsistências visuais) · 28 fixing-accessibility (corrige acessibilidade na interface).
  5. **Camada 5 · Direção e contexto – COMPORTAMENTO E CONTEÚDO:**
     29 design-brief (briefing que elimina ambiguidade) · 30 design-consultation (decisões de design com critério) · 31 ux-writing-skill (microcopy clara e útil) · 32 content-strategy (conteúdo com estrutura e propósito) · 33 copywriting-skill (texto que orienta a ação) · 34 product-position (posicionamento antes do visual) · 35 user-research-cookiy (pesquisa com usuários ponta a ponta) · 36 software-ux-research (pesquisa de UX para software).
  6. **Camada 6 · Confiança – QUALIDADE E AVALIAÇÃO:**
     37 plan-design-review (dá nota e detecta "AI slop") · 38 design-review-garrytan (critica o visual antes de construir) · 39 design-debt-audit (mapeia dívida de design) · 40 design-impact-reporting (liga design a métricas reais) · 41 cloudflare-web-perf (audita desempenho da experiência) · 42 dark-pattern-audit (detecta padrões manipulativos).
  7. **CTA:** "QUER AS 42 SKILLS? COMENTA ["9T36N" em faixa vermelha]", "EU TE ENVIO O MAPA COMPLETO" e o selo "42 / 42 · SKILL.MD PÚBLICO CONFIRMADO". Mascote lendo um mapa ao lado de uma pasta azul e um balão de fala.
- Regras/lições práticas:
  - Organize o uso de IA em design por camadas: construção visual → criação visual → produto/interação → conteúdo → qualidade.
  - Inclua skills de **avaliação** (review, dívida, acessibilidade, dark patterns, performance), não só de geração.
  - Antes de instalar, confira repositório, licença e último commit: muitas skills vêm do mesmo repositório.
  - O post é um índice de nomes; sem os links (que dependem do comentário) é preciso buscar cada repositório.
  - Layout que vale estudar: estética "papel técnico" com marcas de corte, listas numeradas em monospace e uma cor de acento por palavra-chave.

### DfkSCaRNfa0 — autor não identificado (redireciona para @aiwithknox)
- Link: https://www.instagram.com/reel/DfkSCaRNfa0/
- Tipo: reel (presumido pela URL)
- Tema: —
- Legenda: indisponível
- Slide a slide: o Instagram mostra "Sorry, this page isn't available". O link redireciona para o perfil @aiwithknox, que também está indisponível. Testei como `/reel/` e como `/p/`, com o mesmo resultado. O post pode ter sido apagado, o perfil pode estar privado ou ter mudado de nome.
- Regras/lições práticas: —

### DfkBGDyDgqS — @griffinwooldridge1
- Link: https://www.instagram.com/p/DfkBGDyDgqS/ · 10/11/2026
- Tipo: carrossel (5 slides)
- Tema: UI/motion (bibliotecas de componentes / dashboard)
- Legenda: "Pare de fazer a IA desenhar cada UI do zero; dê a ela bons componentes." Lista quatro bibliotecas:
  - Bencho: micro-interações divertidas;
  - BoardUI: dashboards e ferramentas de agente;
  - Transitions.dev: mudanças de estado suaves;
  - Beautiful UI: fluxos de agente polidos.

  Pede para salvar e pergunta qual a pessoa testaria primeiro.
- Slide a slide (fundo preto ~`#0B0B0C`, título branco em grotesk (Inter/SF Display), subtítulo cinza, cards de componentes em cinza-grafite ~`#1C1C1E` com cantos ~16–20 px e a URL da biblioteca com "↗" no rodapé):
  1. **Capa – "Top 4 UI Libraries / Stop making AI design from scratch":** mosaico de componentes: comparador de imagem antes/depois com slider, widget de clima (San Francisco 24°, card azul), fluxo de automação, anéis de atividade multicoloridos, input de chat com IA ("Redesign the pricing page hero and tighten the CTA copy"), calendário "Thursday" com eventos coloridos, controle de velocidade (0.5×–2×, 1× selecionado), gráfico "Token spend" de barras empilhadas, card financeiro com linhas, timer "Focus time 25" magenta e "72 BPM".
  2. **Bencho – Playful micro-interactions:** leque de cartas coloridas com arte floral psicodélica, timer circular "25:00" com marcações de tick e botões +5 / play / reset, card de batimentos "72 BPM" (peak 87, min 51) com mini-barras e seletor "Playback speed" 0.5× / 1× (pílula branca) / 1.25× / 1.5× / 2×. URL: bencho.dev.
  3. **BoardUI – Data-rich dashboards and agent tools:** donut de anéis (laranja, amarelo, azul, roxo, verde) com total 325, input de agente com tabs "Get answer / Get spec / Stats / Infinity", gráfico de barras verde-lima ~`#A6E22E` "Earned so far $7,462 (+14.8%)" com abas Weekly / Monthly / Yearly e meses Jan–Dec, e seletor de intervalo de datas com presets (Today, Yesterday, Last week, This month, Last month, This year, Last year, All time), calendários Novembro e Dezembro 2026 e botões Cancel / Apply. URL: boardui.com.
  4. **Transitions.dev – Smooth transitions between UI states:** conversa estilo iMessage (Maya Chen, bolhas azuis ~`#0A84FF` e cinza, "Read"), card "Token spend 1.7M" com barras empilhadas e legenda de modelos, card "Focus time / 25 min" em degradê magenta-vinho com régua de seleção e botão "Start focus", e agenda "Thursday, March 14 · 3 meetings" com dias Mon–Fri e eventos Standup (azul), Product review (roxo), 1:1 with Maya (verde). URL: transitions.dev.
  5. **Beautiful UI – Agent chat, approvals, and workflows:** card "Insights" com métricas −4.41% (vermelho) e +1.15% (verde) e linha temporal, tabela Company / Category com tags coloridas (B2B, Retail, Catering, Seasonal…), lista de tarefas com status To do / In Progress / Completed e painel "Proposed menu cleanup" com linhas em vermelho/verde e botão azul "Apply 3 changes". URL: beautifului.dev.
- Regras/lições práticas:
  - Para UI gerada por IA, forneça uma biblioteca de componentes em vez de pedir design do zero: o resultado fica consistente e polido.
  - Escolha a biblioteca pelo tipo de produto: micro-interação (Bencho), dashboard/dados (BoardUI), transições de estado (Transitions.dev), fluxos de agente com aprovação (Beautiful UI).
  - Padrões de dashboard que se repetem: abas de período, KPI com variação percentual colorida, presets de intervalo de datas e tags de categoria coloridas.
  - Teste antes de adotar (vem de um comentário): a biblioteca cobre os estados vazio, carregando, erro e texto longo? É aí que UIs feitas por IA quebram.

---

## Prints

Arquivos na pasta `prints/`.

| Arquivo | Link direto | O que mostra / por que importa |
|---|---|---|
| DfEmKLLFEDi_1.png | https://www.instagram.com/p/DfEmKLLFEDi/?img_index=1 | Mocha Earth: template de 6 cápsulas com hex e brilho lateral |
| DfEmKLLFEDi_2.png | https://www.instagram.com/p/DfEmKLLFEDi/?img_index=2 | Purple Haze: rampa monocromática roxa |
| DfEmKLLFEDi_3.png | https://www.instagram.com/p/DfEmKLLFEDi/?img_index=5 | Neon Pop: base neutra fria + acento rosa `#EC4899` |
| DfUnwyQGCTA_1.png | https://www.instagram.com/p/DfUnwyQGCTA/?img_index=1 | Ruby, com o rótulo `#243A66` errado sobre um swatch rosa |
| DfUnwyQGCTA_2.png | https://www.instagram.com/p/DfUnwyQGCTA/?img_index=2 | Monochrome: escala de cinzas de `#0B0B0B` a `#FFFFFF` |
| DfUnwyQGCTA_3.png | https://www.instagram.com/p/DfUnwyQGCTA/?img_index=3 | Violet: rampa roxa saturada |
| Dff1uulGoxb_1.png | https://www.instagram.com/p/Dff1uulGoxb/?img_index=1 | Capa: tipografia pesada sobre retrato + etiquetas tipo cursor |
| Dff1uulGoxb_2.png | https://www.instagram.com/p/Dff1uulGoxb/?img_index=3 (vídeo, ~12 s) | /micro-interactions: layout com instrução, mockup e título-comando |
| Dff1uulGoxb_3.png | https://www.instagram.com/p/Dff1uulGoxb/?img_index=5 (vídeo, ~5 s) | /animated-gallery: mockup editorial com serif |
| De_FtT3k-tT_1.png | https://www.instagram.com/p/De_FtT3k-tT/?img_index=3 | Proporção 60/30/10 com placas 3D |
| De_FtT3k-tT_2.png | https://www.instagram.com/p/De_FtT3k-tT/?img_index=4 | Tabela da escala tipográfica 1,25 (16→39 px) |
| De_FtT3k-tT_3.png | https://www.instagram.com/p/De_FtT3k-tT/?img_index=5 | Sombra preta vs tingida e fórmula Y 8 / Blur 16 / 8% |
| DescJ2zTeSf_1.png | https://www.instagram.com/p/DescJ2zTeSf/ | Infográfico completo dos 12 pares de fontes |
| DescJ2zTeSf_2.png | https://www.instagram.com/p/DescJ2zTeSf/ | Pares 10–12 e faixa "Quick Tips" |
| DfFBFpXDZLv_1.png | https://www.instagram.com/p/DfFBFpXDZLv/?img_index=1 | Capa: estética "papel técnico", display condensada e acentos de cor |
| DfFBFpXDZLv_2.png | https://www.instagram.com/p/DfFBFpXDZLv/?img_index=2 | Camada 1 (skills 01–10): layout de lista numerada |
| DfFBFpXDZLv_3.png | https://www.instagram.com/p/DfFBFpXDZLv/?img_index=6 | Camada 6 (skills 37–42): qualidade e avaliação |
| DfkBGDyDgqS_1.png | https://www.instagram.com/p/DfkBGDyDgqS/?img_index=1 | Capa: mosaico de componentes dark |
| DfkBGDyDgqS_2.png | https://www.instagram.com/p/DfkBGDyDgqS/?img_index=3 | BoardUI: KPI, barras verde-lima e seletor de datas |
| DfkBGDyDgqS_3.png | https://www.instagram.com/p/DfkBGDyDgqS/?img_index=4 | Transitions.dev: chat, token spend, timer e agenda |
