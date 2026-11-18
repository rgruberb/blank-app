# Workflow: usar o Claude para web design

Fontes: @thearseniodev (Dd9nhiOyrZU, DfVlIwHISSv — legendas), @thedzianis (DfSIP2iBuFI), @mobileeditingclub (Dff1kjUiR4o). Os reels de @thearseniodev e @thedzianis promovem uma biblioteca de assets ("getlayersai"/"LAYERS"); o princípio vale independentemente da ferramenta.

## Princípio central: mostrar, não descrever

> "Stop asking Claude to 'make your website look premium.' That's way too vague." — Dd9nhiOyrZU
> "Adjectives get you an interpretation. References get you the result." — DfVlIwHISSv

- Adjetivos ("modern", "clean", "expensive", "premium") obrigam o modelo a **inventar toda a direção criativa** → resultado genérico e uma hora corrigindo o palpite.
- Em vez disso, aponte para **uma cena real, uma transição real, uma seção real que já está certa**. O modelo parte de código/visual concreto, não de adjetivos.
- Divisão de papéis: **humano decide mood, escolhe referências e controla hierarquia; Claude faz o trabalho pesado** ("Here's the vision. Here's the toolkit. Make it real.").
- O autor conecta o agente via **MCP a uma biblioteca de assets reais** (cenas 3D cinemáticas, efeitos de movimento, vídeos de fundo, seções interativas) e o Claude lê os componentes reais. Equivalentes neste projeto: `ext-extract-design` (extrai tokens de um site por URL), screenshots/imagens anexadas, trechos de código de componentes existentes.

## Passo a passo recomendado

1. **Colete referências concretas** (2–5): URLs, screenshots, um componente que já funciona. Se for URL, rode `ext-extract-design` para obter cores/fontes/espaçamento reais.
2. **Defina a direção em decisões, não adjetivos**:
   - paleta 2+1 com hex (ver `color-palettes.md`);
   - trio tipográfico (sans / serif itálico de ênfase / mono para labels) ou equivalente;
   - hierarquia: qual é o único CTA, qual o headline;
   - qual é a "terceira camada" (cor, luz, objeto/cena).
3. **Construa em camadas** sobre o mesmo layout: zero design → identidade → profundidade (luz, frosted glass) → movimento. Valide cada camada antes da próxima.
4. **Movimento: um efeito por vez**, passando visuais + cores + descrição do movimento; teste desktop e mobile.
5. **Critique** com `ext-impeccable` / `ext-taste-skill` (anti-slop) e cheque confiança (espaço, alinhamento, ritmo calmo — ver `layers-and-trust-layout.md`).

## Modelos de prompt

Ruim:
> "Make my landing page look premium and modern."

Bom (baseado nos princípios das fontes):
> "Landing page para [produto]. Mood: escuro, técnico, calmo. Paleta: base #0A0A0A + texto #E6E6E6, acento único #C7F44F usado só no CTA primário e no badge do logo. Tipografia: headline sans, segunda linha em serif itálico, labels em mono. Referência de layout: [screenshot/URL] — copie a estrutura do hero (headline à esquerda, diagrama de workflow à direita). Camada de profundidade: um feixe de luz verde atrás de cards em frosted glass. Não adicione movimento ainda."

Movimento (Dff1kjUiR4o):
> "Adicione só um headline reveal: o título entra palavra por palavra em ~600ms, sutil e legível. Cores da marca: [...]. Depois me mostre em desktop e mobile antes do próximo efeito."

## O que se vê no resultado mostrado (Dd9nhiOyrZU)

Site "Relay" dark gerado com essa abordagem, seção por seção:
- Hero: feixes de luz verde/lime fluindo, headline "The handoffs run *themselves.*", CTA pill lime, cards de vidro com diagrama de workflow.
- "Most of a process is *glue*." — texto curto + painel lateral sobre fundo de streams.
- "Approvals where people already are" — mock de app de mensagens com botão lime; gráfico de barras 3D isométrico (barra destacada em lime).
- Transição: um tile/ícone lime que cresce e preenche a tela (o acento vira transição de seção).
- "*Boring* in the ways that matter." — cards de features com ícone lime.
- "A *Tuesday*, seen from Relay." — heatmap/tabela + anel de progresso lime.
- "Numbers we did *not* have to explain away" — métricas grandes (56,703 / 9 / 73%) com medidor em barras lime.
- "You pay for runs, not *for seats*." — slider de volume + pricing $29 / $89 / $290, plano do meio destacado (badge + botão lime).
- CTA final: card de fundo lime "Pick the task you *hate* most." + footer.

Padrão: **todo título de seção usa uma palavra em serif itálico** e o lime aparece 1–2 vezes por seção (CTA, dado-chave). Útil como referência de **consistência do acento e da tipografia ao longo de várias seções**.

## Dar à IA peças reais: componentes, skills, ícones (rodadas 1 e 5)

Mesmo princípio do "mostrar, não descrever", aplicado a componentes. Resumo dos posts; os links reais não foram
conferidos (vários dependem de "comente X").

- **Bibliotecas de componentes em vez de UI do zero** (@griffinwooldridge1, `DfkBGDyDgqS`, print `DfkBGDyDgqS_1.jpg`):
  "Stop making AI design from scratch". Escolha pelo tipo de produto: **Bencho** (micro-interações), **BoardUI**
  (dashboards e ferramentas de agente), **Transitions.dev** (mudança de estado; já instalada aqui como
  `ext-transitions-dev`), **Beautiful UI** (chat de agente, aprovações, workflows). Estética comum: fundo quase preto
  `~#0B0B0C`, cards grafite `~#1C1C1E`, cantos 16–20 px.
  **Teste antes de adotar** (vem de um comentário e vale como regra): a biblioteca cobre **estado vazio, carregando,
  erro e texto longo**? É aí que UI feita por IA quebra. Peça esses 4 estados no prompt.
- **Antes/depois com referências** (@craftwork.design, `DfKaOBqjUr4`, rodada 5, prints `DfKaOBqjUr4_2.jpg` e capa
  `_1`): "Same brief, two pages" — a landing do "Fieldnote.ai" (note-taker de IA para entrevistas) feita pelo agente sem
  referências (mancha verde genérica, cards de métrica) e a mesma página com os arquivos da Craftwork (foto de paisagem,
  objeto 3D, tipografia refinada), comparadas com divisor no meio; embaixo, a lista "What Craftwork added". É prova visual do princípio; o post
  também vende o marketplace. Outras skills citadas no mesmo carrossel: Design Engineering (Emil Kowalski), GSAP
  ScrollTrigger, LottieFiles motion-design, Refactoring UI (auditoria de hierarquia/espaço/profundidade com nota),
  Web Interface Guidelines (Vercel). Motion fica com `ui-motion`.
- **Mapa de skills de design para Claude Code** (@matheustilli, `DfFBFpXDZLv`, sem print copiado): 42 nomes em 6
  camadas (construção visual → criação visual → produto/interação → direção/conteúdo → qualidade/avaliação). Lições:
  inclua skills de **avaliação** (review, dívida de design, acessibilidade, dark patterns, performance), não só de
  geração; **confira repositório, licença e último commit** antes de instalar (18 repositórios, um deles com 16 das 42).
  Já cobertas aqui: `ext-impeccable`, `ext-taste-skill`, `ext-extract-design`, `ux-patterns` (dark patterns, AI slop).
  O post é só índice de nomes: sem os links, procure cada repositório.
- **Ícones** (@noahelhadedy, `Df1eAHODjT9`, rodada 5, prints `Df1eAHODjT9_1–_3.jpg`): 8 sets (Neat Icons, Doo Icons,
  Majesticons, Gravity UI, Pictogrammers/Material Design Icons, Humbleicons, Bootstrap Icons, Vectopus). Critérios para
  escolher (complemento a partir do post): **uma grade só (24×24)**, estilos disponíveis (line/solid/duotone), mesma
  espessura de traço em todo o produto, licença (open source vs. pago) e arquivo Figma. O 1º item é o produto do
  próprio autor (Neat Icons: 1.162 ícones em 4 estilos numa grade, 201 grátis). Nos prints: Humbleicons = 284 ícones
  de traço fino agrupados por categoria (Medical, Data and analytics, UI); Majesticons = "Ship a consistent UI without
  redrawing a single icon", grade 24×24 e seletor de estilo/traço/cor ao vivo.
- **Bibliotecas de UI animada** (@noahelhadedy, `De_J0aOl9SJ`): Skiper UI, Kokonut UI, Cult UI, SmoothUI, Animata,
  Eldora UI, Hover.dev. Dica do post: **um momento animado por página (hero ou CTA, não os dois)**. Implementação e
  prints (`De_J0aOl9SJ_1–_3.jpg`): `ui-motion`.

Prompt (complemento): "Use os componentes de [biblioteca] para cards, tabela e date picker. Para cada componente,
mostre os estados vazio, carregando, erro e com texto longo (nome de 60 caracteres, número de 9 dígitos)."

## Apresentar o design: mockup em device + recorte em perspectiva (rodadas 2 e 5)

Molde que os posts do @shohan.designs / Orbix Studio repetem em todo carrossel (Zentra `Dfr6X8qFPwC`, Vaulto
`DfcdrhgFFMR`, CareNest `DfUvP_ulPC6`): **(1)** tablet ou celular nas mãos sobre fundo cinza-claro `~#D8D8D8` com a
tela inteira → **(2–3)** a UI plana em close, dividida em duas metades (panorama) → **(4)** **recorte em perspectiva 3D
com desfoque forte nas bordas** (profundidade de campo) num gráfico ou tabela → **(5)** CTA de contato. Variação: o
mesmo design em monitor inclinado ou MacBook com luz dramática (@uiuxcenter, @webdesignssphere). Dá 4–5 slides de um
único design, mostra detalhe sem poluir. Prints de exemplo: `assets/visual-refs/Dfr6X8qFPwC_1.jpg` (Zentra num tablet
segurado pelas duas mãos, moldura "Designed by Orbix Studio · Save for later" em pílula branca no topo) e
`dashboard-ui/assets/visual-refs/` (`DfcdrhgFFMR_3.jpg` = recorte inclinado; `Dfr6X8qFPwC_2`/`_3` = as duas metades
planas). O mesmo molde vale para app de celular (`DffCenmFASU_1`/`_4`: 1 celular → 3 celulares em leque).
Cuidados (complemento): revise os dados do mockup (vários cases têm números impossíveis); não imite marca alheia no
slide de contato (MediCore copia o sorriso da Amazon).
