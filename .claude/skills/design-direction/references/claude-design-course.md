# Claude Design — curso completo (Nate Herk)

Fonte: "Claude Design 2 HOUR COURSE (Beginner to Pro)" — Nate Herk (@nateherk), https://youtu.be/ovabeVoWrA0 (30/04/2026). Destilado da transcrição completa. Citações verbatim entre aspas (em inglês). Inferências minhas marcadas como **(complemento)**. Propaganda/patrocínio (ferramenta de voz, comunidade, PDF gratuito) omitidos.

Projeto-exemplo do curso: marca fictícia **Tally** (app de finanças pessoais, "money on the level", paleta bone + navy + acento verde, logo de 4 tally marks cortados + ponto verde). Na parte final, um segundo projeto do zero: **Lull** (bebida noturna de magnésio), levado até deploy.

## Sumário rápido

| Tempo | Capítulo | Essência |
|---|---|---|
| 0:00 | What Is Claude Design | App separado (Anthropic Labs), Opus 4.7, **limite próprio** de uso |
| 5:24 | Why Design Systems Matter | Design system é a 1ª coisa a fazer; vira o `design.md` de tudo |
| 8:55 | Ideating the Tally Brand | Brainstorm no **Claude chat**, nunca no Claude Design |
| 11:33 | Creating the Design System | Input enxuto (logo PNG + markdown); revisar card a card; logo costuma sair errado |
| 19:50 | Pitch Deck Build | Outline/pesquisa feita no chat → cola no Design; Edit, Draw, Tweaks |
| 34:01 | Landing Page Wireframes | Wireframe gera 3 conceitos — mas ele considera que foi desperdício para landing simples |
| 40:45 | High-Fidelity Website Build | Sketch + vídeo de fundo (Kling) + brand doc → landing em ~1 shot; tweaks |
| 57:51 | Mobile App Prototype | Spec de 804 linhas feito no chat → canvas com todas as telas em frames iOS, interativo |
| 1:09:00 | Launch Video with HyperFrames | Template Animation + skill HyperFrames (.md) → vídeo HTML animado |
| 1:22:05 | Final Live Build | Site Lull do zero: chat → prompts de imagem/vídeo → Design; comments/edit/draw/tweaks |
| 1:42:01 | GitHub & Vercel Deploy | Zip → Claude Code → GitHub privado → Vercel; erro 404 resolvido com `index.html` |
| 1:49:26 | Stretching Your Session Limit | Model por etapa, 1 mudança por prompt, negativos, referências reais, sessão nova |
| 1:57:00 | Final Thoughts | Acabou o limite? Exporta e continua no Claude Code |

---

## 0:00 — What Is Claude Design

**O que é**
- Produto separado dentro do ecossistema Anthropic (ao lado de Chat, Cowork, Claude Code), lançado em 17/04/2026 como produto da Anthropic Labs, em **research preview**. Cria designs, protótipos, slides, one-pagers, animações e vídeos.
- Roda por padrão em **Claude Opus 4.7** (melhor visão). Usa a visão para **verificar** o que gerou ("verify agent") e corrige sozinho.
- Exporta para Claude Code, Canva, ZIP, HTML, PDF, PowerPoint, Figma; design systems podem ser compartilhados com o time (plano Team).
- Só em plano pago (Pro, Max, Team, Enterprise). Acessa pelo botão **Design** na barra lateral do claude.ai.

**Ponto crítico:** o Claude Design tem **limite de uso separado** (aparece em Usage ao lado de "current session", "all models", "Sonnet only"). Ele acredita que o reset é semanal; dá para comprar extra usage. Opus 4.7 gasta tokens mais rápido.

**Interface inicial**
- Esquerda: novo projeto → **Prototype** (Wireframe ou High fidelity), **Slide deck**, **From template** (ex.: Animation), **Other**.
- Direita: designs anteriores, design systems e **exemplos** (organic loaders, text streaming, globe, shaders) cujos prompts podem ser reaproveitados.

## 5:24 — Why Design Systems Matter

- "This is the first thing that I want you guys to do when you get into Claude Design." Construir design system é caro em tokens, mas compensa: tudo depois sai com logo, tipografia, cores, espaçamento e componentes da marca.
- "You don't want to go crazy building like five different design systems. You just want to start with one and then iterate from there."
- O design system gerado contém: **typography** (quando usar primária/secundária), **colors** (acentos, gradientes, neutros, primárias), **spacing** (inclusive glows atrás de botões, raios/formas), **components** (badges, tags, botões, cards, inputs, ícones).
- Marca já existente: ele deu logo + **GitHub repo** do site + **URL** do site, e o Design extraiu tudo.
- O design system é o seu `design.md`: dá para baixar como ZIP/PDF/HTML e levar para Claude Code, Canva ou outro modelo de imagem.

## 8:55 — Ideating the Tally Brand

- Brainstorm da marca feito no **Claude chat** comum: "Hey, I need to create a brand… help me figure out a good brand concept that I can use so it feels consistent."
- Depois: "Okay, let's run with Tally. I want you to build a brand around this. What's the product we're selling? Who does it appeal to? What's the mission? What's the offer?"
- Resultado: brand concept com produto, público, avatares (ex.: "Sam", "freelance Frankie"), missão, posicionamento, pilares, voz/tom, promessa e **identidade visual**: paleta de **4 cores**, fonte primária + secundária, hierarquia do hero.
- Logo iterado no chat; ele fez um híbrido de duas opções (tally marks + ponto verde no fim da palavra) e pediu uma mini brand guideline tipográfica.
- **Regra:** "Don't ever brainstorm in Claude Design. There's just no point. You get way more usage over here." Use o Design só quando tiver ideia e plano prontos.
- Alternativa citada: ChatGPT image model ("image two") para explorar logos; ele preferiu o logo do Claude.

## 11:33 — Creating the Design System

**Passo a passo**
1. Design systems → **Create new design system**.
2. **Company name and blurb**: "Tally" + a missão copiada do brand concept.
3. Sem GitHub/código. **Assets**: logo PNG + brand concept exportado como **markdown**. (Também aceita pastas, arquivos, repos e import de Figma.)
4. **Any other notes**: como ainda não havia site, descreveu botões: "I want the buttons to feel very modern. I want them to have sort of a like a slight glow behind them. And I just want it to feel very polished." (Ele mesmo admite que é vago.)
5. **Continue to generation** (~5 min; outro trecho cita 10–15 min).

**Revisão (não pule)**
- Dá para dar feedback enquanto ainda gera: cada card tem aprovar/feedback. "Definitely spend some time here because… this is going to be your design.md, your spec for everything that you build in the future."
- Fontes da marca ausentes são OK — pode subir os arquivos ou ele busca.
- O Design gera ainda um **mock de landing page**, preview de app mobile, UI kit (botões com hover/click, sombra com glow, inputs, ícones).
- Ao final: **Publish**; opcionalmente **make default**. Aba **Design files** mostra assets enviados, previews e docs (é o que se exporta).

**Erro e correção — logo deformado**
- "Claude Design has been historically bad with logos." Ele alterou o tally mark (o traço não cruzava os 4). Feedback usado: "The logo is not appearing as it should. I dropped in a PNG of a logo, and you should just keep it exactly as is… Everything else though looks good. The colors and the font is fine. But the icon logo is not correct." Em outro card: "The logo has been changed. The colors look good, but the logo cannot be changed from the original PNG that I gave you."
- Problema reaparece no deck e no vídeo; logos tipográficos simples (ex.: "AIS") não sofrem. Corrigir funciona, mas gasta tokens.

**Custo medido:** 4% → 10% do limite do Design no plano Max 20x (US$ 200/mês) ≈ **6%**. "Be selective about what you give your Claude Design" — só cores, logo, tipografia e componentes; não dê um repo inteiro sem necessidade.

## 19:50 — Pitch Deck Build

**Setup:** novo **Slide deck**, design system Tally, nome "Tally pitch deck". Interface tipo Lovable: chat/comentários à esquerda, preview/arquivos/sketches à direita.

**Preparação fora do Design (chave do capítulo)**
- No mesmo chat do Claude onde nasceu a marca, pediu estrutura + pesquisa de mercado: "I want to create a pitch deck for an investor presentation… explain what Tally is and why I believe in it and also look at the market… build on top of that with a pitch deck sort of structure and also do any research about the market and the strategy…"
- O Claude quis construir o deck; ele interrompeu: "You don't need to build the deck. Just give me markdown outline so that I can put this research into Claude design."
- Mentalidade: "Thinking about AI as a specialized tool… a separate chat for each individual type of request." Chat faz pesquisa/outline; Design faz o design.

**Prompt no Design:** anexou `Tally-Brand-Concept.md` + colou o outline (372 linhas) e explicou: "You don't have to follow it to a T, but there's a lot of important research and information in there that I want you to use in this pitch deck as if we're trying to convince investors…" Esclareceu que o bloco colado era a estrutura do deck.

**Modelo:** seletor no rodapé (Opus 4.7 padrão, Opus 4.6, Sonnet, Haiku…). Opus 4.7 no planejamento inicial; Sonnet/Haiku para ajustes; quando o fluxo e o design system estão maduros, dá para ficar só no Sonnet.

**Resultado:** o verify agent revisou slide a slide e corrigiu os slides 6 e 10 sozinho. Deck coerente com fontes/cores/logo; slides de mercado vieram da pesquisa do chat. Ele avisa que não validou os números.

**Ferramentas de iteração**
- **Edit**: clicar no elemento e mudar texto, tamanho, cor diretamente. "It helps you actually be more specific on your changes and it will save you… tokens in the long run."
- **Draw**: circular algo e escrever o pedido; injeta um screenshot no chat. Falhou uma vez ("couldn't capture it") — bug de research preview. Melhor para coisas **sem elemento próprio** (ex.: região de gradiente escura demais); para um elemento real, edite direto.
- **Sem undo/reset** no modo edit: para desfazer uma cor teve de copiar o valor original manualmente.
- **Tweaks**: "Could you give me a couple different tweaks that I could play around with for this whole slide deck?" Gera um painel com toggles: cover (default / bold mark / wordmark only), textura (dot grid, hairline, **warm haze** — o favorito), accent (vivid green, warm), slide chrome (default/minimal/emphasized). "You can let Claude design be the creative one."
- Saídas: Present, convidar time, duplicar, virar template, exportar, mandar para Claude Code.

**Custo:** acumulado 32% depois do design system + deck.

## 34:01 — Landing Page Wireframes

- Novo Prototype → **Wireframe**, design system Tally, "landing page mockups". Anexou o brand concept e pediu: "The point of this project is a wireframe project. I want you to give me a bunch of different concepts… hero section… specs… pricing… testimonials. You can fill all of this in with mock data… help me figure out the theme, the style… dark mode or light mode…"
- O Design faz **perguntas de múltipla escolha** antes de construir: quantos conceitos (3), fidelidade (sketchy / clean / **mid-fi** / mix), vibes ("decide for me"), light/dark ("mostly light with one dark concept"), imagery, seções extras (FAQ, founder note, comparison table, sample do weekly).
- Saída: board pan/zoom (tipo Figma/Stitch) com 3 conceitos ("honest mirror", "receipt ledger", "quiet night") + tabela comparando modo, voz, imagery, extensão, público-alvo (mapeia os avatares) e riscos ("could feel preachy / cold / generic"). Abrir em tela cheia é melhor que o canvas ("a little bit wonky").
- **Veredito dele:** "For this specific use case, I think that was probably a waste of my session limit" (~7%). Wireframe vale mais para **funil multi-página**, **app desktop/mobile**, logos/packaging. Para landing simples: vá direto ao high-fidelity. Conceitos de mockup também dá para pedir no chat comum, que é mais barato.
- Exportou o board como HTML.
- Contraponto (1:49): ele viu gente no X dizendo que wireframe antes converte melhor para hi-fi com menos iteração; acha plausível pelo princípio "planejamento primeiro".

## 40:45 — High-Fidelity Website Build

**Asset de movimento feito fora:** no **Kling**, vídeo com start frame = fundo bone vazio e end frame = logo; resultado: logo "desenhado à mão" e o traço cruzando. Ideia: loop infinito no lado direito do hero. Subiu `tally animation.mp4` + brand concept (posicionamento e preço).

**Sketch antes do prompt:** "New sketch" → retângulo 16:9 (página), quadrado ~1:1 marcado "Tally animation.mp4" (para não ficar coberto por texto), caixas "hero text"/"hero subtext", navbar com logo à esquerda, nav sections e CTA à direita. "I want to align with Claude on the way that this is going to work before it actually starts trying to build."

**Prompt (resumo verbatim):** "I've given you a sketch attached in this chat… I'm imagining a navbar up the top… hero text and hero subtext on the left side… the tally animation.mp4 on the right side of the hero section. But, what's important is that the tally animation, the color is the bone color. So, I want the whole background of the site to be bone, at least for the hero section, so it looks like it naturally and seamlessly fits in… as we scroll down, I want you to design the other sections of the site using our Tally design system and… brand concept… You can fill all of this in with mock data… if you have any questions, feel free to ask."

**Resultado e ajustes**
- Seguiu o sketch; adicionou sozinho faixa deslizante de trust (Plaid, 256-bit, read-only…), 4 passos com tempo de setup, "sample weekly" com elemento sticky enquanto o resto rola, acentos verdes, CTA final com logo.
- Fundo do site ≠ fundo do vídeo por pouco → corrigir com **hex exato** do vídeo.
- Sugestão dele: alternar seções navy/bone para dar estrutura.
- Tweaks pedidos ("Give me a bunch of tweaks"): tone (warm/dark), texture (noise, dot grid, **ledger lines**, graph paper, paper fiber) + **texture strength**, vignette, hero layout (split/stacked/video left), fonte/tamanho/texto do headline, frame do vídeo (flush/hairline/corner ticks/card plate), ornament dot, accent + intensidade, **tally mark watermark** de fundo (só nas seções bone), ledger numerals, ligar/desligar seções.
- Em Present notou um gap ("should probably be more flush") — fácil de corrigir com Edit/Draw. "For basically a one-shot prompt, maybe… two or three iterations, we're already at a spot where this is really good."
- Publicar: export para Claude Code → GitHub → Vercel, ou HTML/ZIP (detalhado em 1:42).

**Fontes de inspiração (copiar prompt e colar no Design)**
- **Motion Sites** (motionsites.ai): backgrounds e sites animados com prompt pronto; "copy this prompt… 'build me this website, but use our Tally design spec'".
- **godly.website**, **Awwwards**: inspiração em scroll infinito.
- **21st.dev**: componentes individuais (announcements, backgrounds animados, borders, buttons) com prompt copiável.
- Efeito de **parallax com vídeo controlado pelo scroll**: "I want to have this video be on the background. I want it to be parallax scrolling… As the user scrolls down or scrolls up, the video should play in that order." Mais cards 3D glassmorphism.

**Brand guidelines one-pager**
- No projeto do site (já "treinado" na marca): "Can you please output just a text-based version of these brand guidelines? … logo and the spacing and the font and the colors and the typography… as specific as you can about the way that the buttons are, about the way that the accents work…"
- Colou o texto + logo ícone + wordmark no ChatGPT (create image): "create me basically a one-pager for the Tally brand guidelines". Saiu vertical, com do's/don'ts do logo, cores, tipografia (pequeno erro de fonte), spacing, UI/ícones.
- Mais barato: exportar ZIP/HTML e fazer a análise fora do Design. Modelos de imagem às vezes erram fontes específicas (Roboto Mono/Montserrat) → finalize no **Canva**.
- Uso: doc interno de referência ou para enviar a fornecedor/designer.

**Custo:** 51% acumulado.

## 57:51 — Mobile App Prototype

- Spec feito no Claude chat: "Give me a full spec for mobile app. I want this to be a requirement doc, and I want to turn this text-based request into a live high-fidelity breakdown of how the app should look and feel." → 804 linhas.
- Justificativa: "Those input tokens are not as expensive as Claude outputting tokens and going down the wrong path."
- Pulou wireframe; High fidelity "Tally app design", design system Tally, deixando claro que é **mobile, não desktop**. Prompt: "I just dropped you in 804 lines of a mobile app spec, and you already have access to our Tally design system. Go ahead and build this out. If there's any questions… feel free to shoot."
- Perguntas do Design: escopo (all screens), formato (**design canvas com todas as telas lado a lado em frames iOS**), interatividade (sim), variações (light/dark toggle, 2–3 layouts), "ask sheet" ligada ao Claude ou respostas hardcoded (hardcoded por ora), realismo dos dados fake, nº de insights.
- Resultado: board com home, flow, weekly, onboarding (connect bank, 3 perguntas, notificação), dark mode, variações de hero, notificações iOS; telas clicáveis (inputs, expandir despesas, marcar como cash).
- Problema: "very bland… basically the bone color all the way throughout." Prompt: "Could you just upgrade this a little bit? … make some polished changes, give it some more texture, and give me a bunch of things that we can tweak…" Tweaks: accent color (green/terra/amber/indigo/rose), uso do acento (quiet/medium/loud), textura (paper/grain), hero scale, tally mark, card style (flat/lifted/paper), subscriptions (plain/bar).
- Draw usado onde não há elemento editável: status bar do iPhone (hora/bateria) cobrindo UI; watermark saindo da borda. Ambos corrigidos. Bug: a nota digitada no draw fica escondida.
- Bugs restantes: ícone de settings errado (devia ser engrenagem), toggles e textos fora dos limites. "Iteration is the name of the game." Ele seguiria com a versão dark, que achou melhor.
- **Custo:** 85% acumulado.
- Exemplo paralelo (marca AIS): design system → site → landing de promoção no mesmo estilo → vídeo de release animado só em HTML, sem HyperFrames.

## 1:09:00 — Launch Video with HyperFrames

- **HyperFrames** (da HeyGen): framework/skill para o modelo escrever HTML animado e renderizar como vídeo. Baixou o raw `.md` da skill "Claude Design HyperFrames" (link na descrição do vídeo).
- Novo projeto → **From template → Animation**, "Tally Launch Video", design system Tally. Anexou a skill `.md` + brand concept.
- Prompt: "…make a launch video for Tally. You have Tally Design System… Tally Brand Concept… and then you have the Claude Design Hyperframes markdown file, which is going to teach you how to actually create the motion graphics and render out this… animated video… We're targeting a landscape video… maybe 20 to 30 seconds of fast-paced information. The ultimate goal is to announce Tally, announce what it does, and… at the end, a big call to action for people to sign up and start their free trial."
- 1ª versão (25 s): lógica boa, CTA bom, mas "very bland… not very engaging".
- Iteração emocional, como falaria com um editor humano: "Let's make this more fast-paced. Let's keep our audience's attention… more animations, more motion graphics. There should be more going on on screen than just a couple bullet points coming up. That's boring. Tell a story here. Make this exciting… it's a big day. We're launching an app, and we are inviting people to be a part of the journey." → "much better". Restou ritmo rápido demais em partes e **logo errado de novo**.
- **Catálogo HyperFrames**: notificações, transições (chromatic radial split, cross warp morph, glitch), "app showcase" (3 celulares). Ele passou só a **URL** da página do catálogo; o Design buscou a página e o repo no GitHub e adicionou uma cena (vídeo foi de 25 para 30 s; precisou de 1 prompt extra de ajuste). "Claude Design can fetch pages, can search the web."
- **Exportar vídeo:** não há render MP4 nativo. Opções: handoff para Claude Code renderizar, ZIP/HTML, ou tela cheia + gravação de tela.
- Aviso da própria UI: "Start a new chat to save 110,000 tokens of context. This uses your rate limits more effectively." → exporte o HTML e continue num projeto novo quando o thread estiver longo.
- **Custo:** os 4 builds + design system ≈ **95%** do limite (Max 20x).

**Recap "four moves that compound"** (~1:18)
1. **Reference, don't describe** — screenshots reais, destacar elementos, editar você mesmo, draw, tweaks; planejar no chat e trazer o plano refinado.
2. **Don't use defaults** — default gera "AI slop"; dê sua copy e seu design system.
3. **Design system first** — um, bem feito, compartilhado; atualize-o quando trocar botão/logo/cores.
4. **Iterate in chunks** — com ~5 mudanças num prompt "it kind of loses track"; uma feature por vez.

Outras ideias do trecho: relatos de "80% of my weekly Pro budget on one webpage" e "95% of my quota… after a single design system iteration"; quando o limite acaba, leve o spec ao Claude Code (outro medidor); ajustes triviais (trocar logo num pôster/PDF) são mais rápidos no **Canva/PowerPoint/Figma** do que brigando com o modelo.

## 1:22:05 — Final Live Build (Lull)

**Demonstração inicial:** sites dele (AIS e pessoal) transformados em ~20 min cada em experiências de scroll com cards 3D e cena de fundo, mantendo copy, cores e marca. Ele já tinha gasto mais de US$ 200 em extra usage testando.

**Dois pontos de partida:** (1) site existente → dê o repo do GitHub ou a pasta ao Design; (2) do zero → comece no chat.

**Pipeline do zero**
1. Chat: "I want to build a website using Claude design and I'm looking for some inspiration… What is the product or service…? And what should the hero section and actual copy be like? Help me basically build a brand… give me the spec for this." → **Lull** (magnesium glycinate noturno), posicionamento, voz, identidade visual, seções, footer.
2. Chat: "I want to create a video that will play in the background of the hero section… endless loop… wow factor… There should not be any text, but it should also have room where we could insert a block for the hero text and the subtext." → pede **image prompt** + **video prompt**.
3. Imagem 16:9 com Nano Banana 2 (caneca cerâmica escura com líquido quente, espaço vazio para o texto). Vídeo com SeeDance 2.0 usando a imagem como **first e last frame** (loop perfeito); câmera parada, só vapor animado.
4. Claude Design → Prototype High fidelity, **sem design system** (marca nova), "Lull website".
5. Sketch: vídeo de fundo do hero, caixa hero text + subtext à esquerda, navbar (logo, shop).
6. Upload do MP4 (8 s). **Limite de upload ~30–40 MB**; 15 s e 20 s funcionaram.
7. Colou o spec da marca (23 linhas) + prompt: "I've got a sketch, which is just my basically idea for the hero section. There's going to be a lot of little sections beneath, which you will be on your own to figure out… I've given you the sleep background.mp4… playing on an endless loop in the background… hero text will be on the left side… I pasted in 23 lines of text, which is kind of the brand identity… and how you should write the copy. And just go ahead and write all the copy for now."
8. **Observe o que ele faz e interrompa se desviar**: "Go ahead and stop it if it's going down the wrong path, because if it's going down the wrong path, it's going to build stuff, and that's going to use a lot of your session limit." Ele cria to-do e um mini design system (paleta, texto) por conta própria.

**Iteração no canvas (mais barato que conversar)**
- **Comment** num elemento: "Go ahead and make this button the color of the comma in the hero text. Make it a gold accent." → "Send to Claude" leva o comentário preso ao elemento exato.
- **Edit inline**: apagou um travessão ("That looks very AI"), mudou tamanho de fonte em tempo real.
- **Draw**: "I don't like how this ends so abruptly. Add a transition overlay or gradient, so it feels smoother." Veio só uma linha → iterar de novo, mas acertou o lugar.
- **Tweaks**: "I want to see what else is possible… just add a bunch of things that I can tweak… different colors, different sliders, different panels." Painel: palette, accent hue, fonte, tamanho do headline, case (lowercase), hero layout, overlay, **video dim**, **section rhythm** (gap entre seções), ritual card style (flat/bordered/big numerals), **Reset**.
- Por que tweaks economizam: no Claude Code, testar "e se o fundo fosse azul?" custa 1 prompt + 1 revert; aqui é um toggle. Não há botão de **revert** de versões como no Lovable.
- Scroll-scrub de vídeo: "Instead of just playing it, I want you to only associate each frame with like a scroll position, so that as I scroll down or up, the video goes forward or reverses."
- **Seção por seção**: quebre o site em seções; para cada uma peça ao chat ideia de elemento/vídeo + prompts, gere fora, traga de volta.
- Motion Sites: copiar o prompt de um site e pedir "replace the background video with this background video… update all of the copy and the brand colors and feel to my brand" + design system.

## 1:42:01 — GitHub & Vercel Deploy

1. **Share → Download project as ZIP**. Alternativa: **Hand off to Claude Code** (copia um comando); naquela manhã dava **404**, por isso usou o ZIP.
2. Extraiu numa pasta, abriu no VS Code com Claude Code. Conteúdo: vídeo de fundo, `scraps` (sketch), `uploads`, o HTML.
3. Prompt: "This is a website project for our brand called Lull. All I want you to do is push this to a GitHub repository, push it to a private repository, and call it whatever you want." (Primeira vez: o Claude Code abre a autorização do GitHub.)
4. Faltou testar antes do push: "Make sure that the website actually works as expected and open it up in a local host for me to view." `localhost` só funciona na sua máquina — não mande esse link para ninguém.
5. **Vercel** (cadastro com a conta GitHub) → Add new → Project → Import do repo → Deploy (~60 s) → domínio `*.vercel.app` (no vídeo, `lol-website.vercel.app` — a pasta/repo saiu como "lol website").
6. **Erro 404 NOT_FOUND**: perguntou ao Claude Code "…when I opened it up, it gave me this error message. What does this mean? How do I fix this?" Causa: a Vercel serve a raiz do repo e o HTML tinha outro nome → renomear para **`index.html`** e push. A Vercel redeployou sozinha.
7. Fluxo contínuo: localhost = ambiente de teste; "push all of these changes to GitHub" → Vercel publica em ~30 s.
8. **Mobile não vem otimizado**: DevTools (F12) → toggle de device mostrou o site quebrado. "Claude design and Claude code don't automatically optimize for mobile, but if you tell it… it will certainly help you." Peça otimização mobile sem afetar o desktop.
9. Domínio próprio: ~5 min, peça ajuda ao Claude.

## 1:49:26 — Stretching Your Session Limit

- **Dois medidores**: limite semanal do Claude Design separado do resto.
- **Burn rate relatado**: Pro (US$ 20) → um site grande + um design system e quase acabou; Max 5x → "four to five serious prompts"; Max 20x → alguns projetos de vídeo e sites antes de chegar perto do fim.
- **O que mais drena**: tudo em Opus 4.7; pular o planejamento (contexto pobre → muita iteração); **design system sem URL**/com muito material (ingestão de 10–15 min); **threads muito longas** (context rot, tokens descacheados reprocessados).
- **Truque do design system**: baixe-o como ZIP e use no Claude Code ("This is the design system for AI Automation Society. Help me build some other stuff") — sem gastar o limite do Design.
- `/clear` existe no chat do Design ("cleared, ready for the next instruction"), mas ele não confirmou se de fato limpa o contexto. Mais seguro: exportar e abrir projeto novo, iterando sobre o já construído.
- **Model by stage**: Opus 4.7 para planejar ou mudanças pesadas; **Sonnet 4.6** fez vídeo, animações e decks "just fine" quando o pedido é claro.
- **One visual dimension per prompt**: com várias mudanças grandes juntas, "it only actually does like one or two of them well and the rest… get disregarded".
- **Negativos**: diga o que você não quer (fontes, esquemas de cor) para não ter de corrigir depois.
- **Referências reais**: "linear 2023 with higher density" em vez de "make this clean/minimalistic".
- Apontar/comentar/desenhar; pedir protótipos, flows, demos.
- **Exportar** (HTML, Figma, Canva, PowerPoint) para ajustes manuais triviais.
- **Uploads**: MP4 funciona, com teto (~30–40 MB; vídeo de 5 min não). Quanto mais assets relevantes no início, menos repetição e correção.

## 1:57:00 — Final Thoughts

- Acabou o limite do Design no meio do trabalho? "Export your Claude Design project, get it into Claude Code, and now you can just keep working on Claude Code because you have more usage. And then just wait till your usage resets on design and then take it back into design."
- Para começar: escolha um artefato real que você quer entregar, escreva seu `design.md`/guidelines, itere no Design e depois leve para Claude Code/Figma/etc.

---

## Workflow recomendado (brand → deploy)

1. **Brainstorm da marca no Claude chat** (não no Design): conceito, produto, público/avatares, missão, voz, identidade visual (paleta de ~4 cores, fonte primária/secundária), logo. Peça um **brand concept em markdown**.
2. **Logo**: itere no chat ou num modelo de imagem; finalize como **PNG** limpo (ícone + wordmark).
3. **Design system no Claude Design** (um só): nome + blurb (missão), logo PNG, brand concept `.md`; marca existente → URL + repo. Notas curtas sobre botões/estilo. Revise **cada card**; exija o logo idêntico ao PNG; publique (e torne default se for a marca principal).
4. Para cada artefato, **prepare o conteúdo no chat** (outline do deck com pesquisa, spec do app, copy do site) e peça **só markdown**, não o artefato.
5. **Assets de mídia fora**: prompts de imagem/vídeo pelo chat → gere (Kling, Nano Banana, SeeDance…), com espaço vazio para o texto e first frame = last frame para loop.
6. **Sketch** do layout-chave (hero) no Design antes do prompt.
7. **Prompt único e rico** (Opus 4.7): anexos + spec + sketch + restrições (ex.: "fundo do site = cor do vídeo"); peça perguntas. Responda o questionário; use "decide for me" onde não tiver opinião.
8. **Acompanhe e interrompa** se desviar.
9. **Itere barato**: Edit direto → Comment no elemento → Draw para regiões sem elemento → peça um **painel de Tweaks** e explore → uma mudança grande por prompt (troque para Sonnet aqui).
10. Wireframe só para funis multi-página/apps; landing simples vai direto para hi-fi.
11. **Vídeo**: template Animation + skill HyperFrames `.md` + brand concept; itere pedindo história/ritmo; aproveite o catálogo HyperFrames por URL; render via Claude Code ou gravação de tela.
12. **Derivados**: brand guidelines em texto → modelo de imagem para one-pager; ajustes finos no Canva.
13. **Deploy**: Share → ZIP (ou Hand off to Claude Code) → Claude Code: testar em localhost → repo privado no GitHub → Vercel import/deploy → se 404, garantir `index.html` na raiz → otimizar para mobile → domínio próprio.
14. Daí em diante, continue no Claude Code e volte ao Design quando o limite resetar ou para algo muito visual.

## Como economizar o limite de sessão

- **Nunca faça brainstorm, pesquisa ou outline no Design** — faça no Claude chat ("you get way more usage over here") e traga markdown pronto.
- **Contexto rico de entrada > iteração**: input tokens (spec longo) são mais baratos que o modelo gerando saída na direção errada.
- **Um design system só**, com input enxuto (logo, cores, tipografia, componentes); nada de repo inteiro sem necessidade. Custo medido: ~6% no Max 20x.
- **Reuse o design system fora**: ZIP → Claude Code.
- **Model by stage**: Opus 4.7 para o build inicial/plano; Sonnet 4.6 (ou Haiku) para ajustes — com design system maduro, Sonnet resolve quase tudo.
- **Edite você mesmo** (Edit inline, tamanho, cor) em vez de descrever em linguagem natural.
- **Comment/Draw** prendem o pedido ao elemento/região exata → menos erro de interpretação.
- **Tweaks** em vez de prompt + revert para experimentar cor, fonte, textura, espaçamento.
- **Uma dimensão visual por prompt.**
- **Diga os negativos** de antemão.
- **Referências concretas** ("Linear 2023, mais denso", screenshot, prompt do Motion Sites/21st.dev) em vez de adjetivos.
- **Sketch antes** para acertar o layout em 1 shot.
- **Pule wireframe** em landing simples (~7% desperdiçado no curso).
- **Observe e pare** o agente quando ele sair do rumo.
- **Threads longas → projeto novo**: siga o aviso "Start a new chat to save 110,000 tokens"; exporte HTML/ZIP e continue; `/clear` existe mas não está confirmado.
- **Ajustes triviais à mão** (Canva, PowerPoint, Figma) — trocar logo num pôster leva 5 s manualmente.
- **Logo complexo** custa tokens extras para corrigir; subir o PNG e mandar "keep it exactly as is" logo no início evita retrabalho **(complemento)**.
- **Acabou o limite**: exporte e continue no Claude Code (medidor separado).
- Referência de consumo do curso (Max 20x): design system 6% → +deck 32% → +wireframe 41% → +landing/guidelines 51% → +app 85% → +vídeo ~95%. Em Pro/Max 5x, o mesmo roteiro estoura bem antes **(complemento: priorize um artefato por semana nesses planos)**.
