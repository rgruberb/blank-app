# Padrões de website por seção e por página

Cada bloco traz: regras, números das fontes (com ID do reel/post) e o ponteiro para a reference de tema que tem o
detalhe. **(complemento)** = convenção web geral, não vem das fontes. Caminhos relativos a `.claude/skills/`.

Ordem típica de uma landing (complemento, compatível com o site "Relay" `Dd9nhiOyrZU` e o site Tally do
`claude-design-course.md`): **navbar → hero → faixa de confiança → problema/benefício → features → como funciona →
prova (números/depoimentos) → pricing → FAQ → CTA final → footer**. Corte seções que não têm conteúdo real.

---

## 0. Navbar
- Logo à esquerda, **3–5 links**, **1 CTA** colorido à direita; o resto neutro (`DYpD5C7zwx6`, @rish_designs).
  Versão "segura" do glide: nav reduzida a logo + "Sign in" (`DfyFShTounu`).
- Menu mobile/fullscreen nasce do botão hambúrguer, fundo escurece (`DfwhC1riuuO`); abertura **~0,7 s**, press
  **0,16 s**; 2,4 s = lento, 0,1 s = "pisca" (`Dfvja0XCyIi`).
- (complemento) Sticky com fundo sólido ou vidro após o primeiro scroll; altura 56–72px; item ativo com
  `aria-current="page"`; menu com foco preso e `Esc` fecha; alvo do hambúrguer ≥ 44px.
- Tema: `ui-motion/references/page-transitions-and-timing.md`; `design-direction/references/layers-and-trust-layout.md` §2.

## 1. Hero
- **Estrutura:** headline curto (sem gritar) + subtítulo de 1–2 linhas + **1 CTA primário** + link secundário opcional
  + 1 visual (produto real, objeto 3D, luz, vídeo). Layout split (texto à esquerda, visual à direita) ou empilhado.
- **Acento só no CTA** (e no máximo 1 palavra/badge): "get along = the whole page / doesn't = the button"
  (`Dfc-Q-0yy0W`). Sequências base → base → acento em `DfIaULMIRC-`, `DfKxflroHj3`.
- **Terceira camada** do hero: uma cor, uma **luz** atrás de frosted glass, ou **um objeto/cena** ("every site here is
  just three layers", `DfVlIwHISSv`; camadas em `DfSIP2iBuFI`).
- **Tipografia:** sans no headline, **1 palavra em serif itálico** ("The handoffs run *themselves.*"), mono em
  eyebrow/labels. Display condensado + serif itálico também funciona (`DfKxflroHj3`). Outline + sólido para hierarquia
  sem trocar de fonte (`DYpD5C7zwx6`).
- **Primeiro paint:** título e CTA visíveis já no load ("2 s em branco parecem uma hora", `Dfy7ig_B-FL`); se o hero for
  o "momento animado", headline reveal palavra por palavra em **~600 ms** (prompt em `claude-web-design-workflow.md`),
  total < 1 s.
- **Acima da dobra:** nada competindo (chat flutuante, banner de cookie colado, 2 CTAs de mesmo peso) — `DfyFShTounu`.
- Mídia de fundo: fundo do site com o **hex exato** do vídeo/imagem para "encaixar" (Tally, `claude-design-course.md`
  40:45); vídeo de fundo conta como o momento animado da página.
- (complemento) Imagem do hero = provável LCP: sem `loading="lazy"`, `fetchpriority="high"`, AVIF/WebP com `srcset`.
  Texto sobre foto com scrim medido no ponto mais claro (`ux-patterns/references/typography-and-touch.md` §3).
- Tema: `design-direction/references/layers-and-trust-layout.md` §1, `color-palettes.md`, `typography-pairing.md`.

## 2. Prova social e confiança
- **Faixa de confiança** logo abaixo do hero (logos de clientes, selos: "Plaid, 256-bit, read-only" no site Tally,
  `claude-design-course.md` 40:45). Logos em monocromático para não competir com o acento (complemento).
- **Números grandes** como prova ("56,703 / 9 / 73%" com medidor no acento, `Dd9nhiOyrZU`); o número é o herói, sem
  tiles pastel (`ux-patterns/references/dark-patterns.md` §B).
- **Só dados reais**: contador de visitantes aleatório e os mesmos compradores repetidos são dark pattern ("fake social
  proof", `dark-patterns.md` §A). Depoimento com nome, cargo e foto real ou não use (complemento).
- Banner chamativo é ignorado (Banner blindness: **0 vs 2 olhadas**, `ux-laws.md` parte 4): coloque a prova com estilo
  de conteúdo.
- Confiança também é layout: espaço, alinhamento, ritmo calmo (`DfyFShTounu`); marca julgada em ~3 s
  (`branding-identity.md` §1).

## 3. Features / benefícios
- **Uma ideia por seção**, título de seção com 1 palavra em serif itálico, acento **1–2 vezes por seção** (padrão do
  "Relay", `Dd9nhiOyrZU`, `claude-web-design-workflow.md`).
- Cards de feature com ícone no acento, **um set de ícones de grade única (24×24)** e mesmo traço
  (`claude-web-design-workflow.md`, ícones).
- Mostre o produto real (screenshot/mock de app) em vez de ilustração genérica (`Dfc-Q-0yy0W`; anti-slop em
  `ext-taste-skill`).
- Grade: 3 colunas desktop → 2 tablet → 1 mobile; cards de altura igual numa borda de alinhamento (complemento +
  `layers-and-trust-layout.md` §2).
- Carrossel de features/depoimentos: deixe **32%** do próximo card espiar (Closure, **0% vs 32%**, `ux-laws.md` parte 4).
- "Como funciona": passos numerados ligados por uma linha (Uniform connectedness) e tempo de setup por passo (Tally).
- Scroll reveal discreto aqui (≤ 700 ms, stagger 70–100 ms, uma vez) se o momento animado estiver em outro lugar
  (`ui-motion/references/scroll-and-screen-transitions.md` §1, §5).

## 4. Pricing
- **Um plano destacado** (elevado + acento), os outros neutros: Von Restorff, "um destaque, nunca três" ($9 / $19 /
  $49, `Dd25eCoBJGr`). No "Relay": $29 / **$89** / $290, plano do meio com badge + botão no acento e **slider de
  volume** (`Dd9nhiOyrZU`).
- **2–4 planos** (Choice overload: 24 → 6 geleias, **3% vs 30%** compraram, `ux-laws.md` parte 4; Hick).
- **Sem plano-isca** ("the decoy": Medium existe para o Large parecer $0.50 mais caro) e **trial com aviso** de data e
  valor (trap de $79.99 no dia 8) — versão honesta em `ux-patterns/references/dark-patterns.md` §A.
- Visual condiz com o preço (budget / mid / premium, `design-direction/references/branding-identity.md` §3).
- (complemento) Toggle mensal/anual com a economia em texto; preço com dígitos tabulares; lista de features
  comparável linha a linha; tabela de comparação completa abaixo, colapsável no mobile.

## 5. FAQ
- (complemento) 5–8 perguntas reais (objeções de compra: preço, cancelamento, segurança, prazo); accordion com
  `<button aria-expanded>` ou `<details>/<summary>`; várias abertas ao mesmo tempo; JSON-LD `FAQPage`.
- Motion do accordion: seta gira **180°** e o painel abre (**62px** no exemplo) — `DfZkZZ4hkuV`
  (`ui-motion/references/micro-interactions.md` §5); receita pronta em `ext-transitions-dev` (21-accordion).
- Seção FAQ é sugestão do próprio Claude Design no wireframe de landing (`claude-design-course.md` 34:01).

## 6. CTA final
- Repita **a mesma ação** do hero com o mesmo texto do botão (complemento). Bloco com fundo no acento/cor de marca é
  aceitável **uma vez** na página: card lime "Pick the task you *hate* most." (`Dd9nhiOyrZU`); CTA final com logo
  (Tally).
- Se o momento animado da página estiver aqui, o hero fica sem efeito expressivo (hero **ou** CTA,
  `scroll-and-screen-transitions.md` §5).
- Peak-end: o fim da página e a tela pós-conversão são desenhados de propósito (memória **4.5/10 vs 8/10**,
  `ux-laws.md` parte 2).

## 7. Footer
- **Alcançável** (sem infinite scroll que o enterre, `components-checklists.md` §4).
- (complemento) Colunas de links agrupados (Produto, Empresa, Recursos, Legal), contato, redes, idioma; política de
  privacidade/termos; newsletter com 1 campo + botão; alvos ≥ 24px (links de footer costumam falhar); `<footer>` com
  `<nav aria-label="Rodapé">`.

## 8. Página de produto (loja e SaaS)
- **Card → página sem corte:** a imagem do card cresce até virar o hero do produto e o "voltar" retorna à posição no
  grid ("Don't cut. Carry.", `DfwhC1riuuO`); View Transitions/FLIP em `ui-motion/references/css-recipes.md`.
- **CTA de compra grande e perto** do preço/imagem (Fitts: **0.66s vs 0.28s**, card "Aurora Speaker $249",
  `Dd25eCoBJGr`).
- **Botão "Add to cart"** com as 6 decisões: **48px** altura, **24px** padding, label **17px semibold**, borda 4:1 /
  label 14:1, pill radius 24, 1 ícone a 10px, estado "Added ✓" (`Ddy5RJOha1U`; estados loading/foco/disabled em
  `DfemaTCBncA`; `components-checklists.md` §1–2). Em escala 1,25 arredonde o label para 16 ou 20.
- Motion: add to cart em **arco 500 ms + badge +1** (`DfTr-mwhZT3`, `micro-interactions.md` §3).
- Galeria: imagens reveladas uma após a outra, espaçamento consistente (`animated-gallery`,
  `scroll-and-screen-transitions.md` §6); hover com leve deslocamento da imagem (`micro-interactions` do mesmo §).
- Página de produto de marca/dev: CTA no acento + link secundário, linguagem técnica com mono e `//`
  (`Dak9nkTFpYI_3`, `branding-identity.md` §5). Produto premium com storytelling: 1 palavra-título + 1 ângulo 3D por
  seção, oclusão (`DYpD5C7zwx6`, `motion-for-social-video.md` §4).
- (complemento) Preço, variação (tamanho/cor) e disponibilidade acima da dobra no mobile; variações como botões, não
  dropdown escondido; prazo e frete antes do carrinho; JSON-LD `Product` com `offers`.

## 9. Vitrine / listagem e checkout de loja
**Listagem**
- Total e posição visíveis ("Page 3 of 48 · 1,187 results"), espaço reservado (sem shift de **68px**), página e
  ordenação na URL (`?page=3&sort=price`), "End of results", back restaura scroll e linha (`DdtzWoMhLtW`,
  `components-checklists.md` §4).
- Filtros em pílula com **um estado ativo cheio** (`components-checklists.md` §11); não abra com estado vazio.

**Checkout**
- **Etapas ligadas por uma linha** (Cart → Ship → Pay → Done: **4 grupos vs 1**, Uniform connectedness, `Del7XTgsuwI`).
- **Menos digitação:** CEP/ZIP primeiro e autopreenche (Tesler **31 vs 16** teclas; Parkinson **30 vs 7**), campos
  tolerantes a formato (Postel **1 de 4 vs 4 de 4**) — `Dd4UtBDBsIS`, `Del7XTgsuwI`, `ux-laws.md`.
- **Rodapé/resumo fixo com total + primário**; revisão antes de pagar; **o valor no botão bate com o total** (erro real
  do exemplo: botão $43 vs subtotal $26) — `components-checklists.md` §10.
- Proximity em formulários: label a **8px** do campo e **24px** do próximo (`ux-laws.md` parte 1).
- Botão de pagar: feedback < **400ms** (Doherty), largura fixa no loading, **ignora o 2º clique** (`DfemaTCBncA`).
- Sucesso: "Pay" → check "Paid" com confetti de **18 peças, pico em 460ms** (`DfgcqeMBPCU`, `components-checklists.md`
  §8); tela final calorosa (Peak-end).
- (complemento) Checkout como convidado; sem distrações (navbar reduzida, sem footer completo); `autocomplete`
  correto (`postal-code`, `cc-number`); teclado numérico (`inputmode="numeric"`); erros inline em texto. Animação de
  scroll **não** entra no checkout (`scroll-and-screen-transitions.md` §2).

## 10. Blog / conteúdo
- Corpo **16–18px**, line-height **1,5**, medida **50–60ch** (45–75 caracteres), escala **1,25** com line-height por
  degrau (`DfRucYFjrac_1/_2`, `ux-patterns/references/typography-and-touch.md` §2b).
- Par editorial: Lora + Open Sans (blog/educação), Playfair Display + Montserrat (editorial), Fraunces + Inter
  (`typography-pairing.md` §2). Tom editorial: serifa fina grande + menu mono caixa-alta pequeno
  (`branding-identity.md` §7).
- Índice de posts: paginação com total, `?page=` na URL, "Load more, then stop" para o footer existir
  (`components-checklists.md` §4).
- Nada de reveal atrasando o texto que a pessoa veio ler (`scroll-and-screen-transitions.md` §2).
- (complemento) Data, autor e tempo de leitura; sumário com âncoras em post longo; imagens com `figure/figcaption`;
  JSON-LD `Article`/`BreadcrumbList`; links inline sublinhados.

## 11. Portfólio
- Motion como guia: `portfolio-showcase` (transições suaves entre projetos, pouco texto) e `animated-gallery` ("each
  project gets its moment") — `scroll-and-screen-transitions.md` §6; um deles é o momento da página.
- O movimento pode ser a identidade (colagem de miniaturas que se reorganiza, @uidesignpatterns, `branding-identity.md`
  §7); foto PB + 1 ponto de cor como foco.
- Apresente cada case em device → plano → recorte 3D desfocado (`claude-web-design-workflow.md`, mockup); revise os
  dados dos mockups.

## 12. 404 e estados
- 404 como peça de marca: foto em tela cheia, "404" grande, frase em serif itálico, **CTA de volta visível**
  (`branding-identity.md` §5, §7).
- Todo componente com vazio, carregando, erro e texto longo (`claude-web-design-workflow.md`); formulário de contato
  com sucesso e erro desenhados.
