---
name: design-direction
description: Direção de arte e identidade visual para sites, landing pages, apps e marcas — paleta 2 cores base + 1 acento (catálogo com hex, 60/30/10, rampas de tons), camadas identidade → profundidade (luz, vidro, sombra tingida) → movimento, layout que transmite confiança, par tipográfico (12 pares), branding (logo, embalagem × preço, brand book) e workflow com o Claude e o Claude Design mostrando referências e componentes reais em vez de adjetivos. Use quando pedirem "escolhe uma paleta", "que cores usar", "60/30/10", "font pairing", "par de fontes", "sombra", "cara premium", "site genérico/sem personalidade", "parece pouco confiável", "como pedir pro Claude fazer um site bonito", "Claude Design", "branding", "identidade visual", "criar logo", "brand book", "embalagem", "parece barato", "biblioteca de componentes para IA", "onde aprender design", "quem seguir no Instagram/YouTube", "Behance/Dribbble/Mobbin", "checar contraste" ou antes de começar a UI de uma landing page nova.
---

# Design Direction

Destilado de 11 reels sobre direção de arte web (paletas 2+1, camadas, layout de confiança, workflow com Claude) da rodada 3 de perfis (branding, logo, embalagem, sistemas de marca da Ramotion, antes/depois de paleta), das rodadas 1 e 5 (rampas de paleta, 60/30/10 e sombra da @gg.designhub, font pairing, bibliotecas de componentes/skills/ícones para IA, apresentação em mockup) e das rodadas 9C/9E/9F (benchmarking e fontes contínuas de aprendizado). Use para **decidir** a direção antes de codar e para **corrigir** UIs genéricas.

## Gatilhos adicionais
Também use para: "cara de startup", "melhora a direção de arte", "adiciona animação/movimento no site" (direção; valores
em `ui-motion`), "como usar o Claude Design", "design system / pitch deck / landing / protótipo de app / vídeo de
lançamento no Claude Design", "limite do Claude Design acabou", "o logo está ruim", "animar o logo", "caro demais",
"combinação de fontes", "que fonte usar", "proporção de cores", "rampa de cores", "escala de tons", "sombra tingida",
"box-shadow feio", "skills de design para Claude", "biblioteca de ícones", "apresentar o design em mockup".

## Quando usar

- Início de landing page/site/app sem direção visual definida.
- UI "funciona mas é esquecível", "cara de template", "fria", "corporativa".
- Página que precisa parecer segura (fintech, B2B, saúde, onboarding).
- Pedido de movimento/animação num site existente.
- Usuário descrevendo o visual só com adjetivos ("premium", "moderno", "clean").
- Criar/revisar **identidade visual**: logo, paleta e tipografia de marca, embalagem, perfil social, brand book.

## Regras centrais

1. **Use exatamente 2 cores base + 1 acento.** "The first two colors set the mood. The accent gives it personality." Não adicione uma 4ª cor de marca; "you don't need more colors, you need one that surprises people".
2. **As bases se dão bem; o acento não.** Bases da mesma família ou neutro + cor; acento com matiz oposto/complementar e alta saturação (azul→laranja, violeta→lime/mint, rosa→amarelo, navy→hot pink).
3. **O acento vai só no que deve ser clicado ou lembrado:** CTA primário, badge, 1 palavra de ênfase, indicador-chave. "A little", "a touch", "a hint" — nunca em fundos grandes.
4. **Empilhe camadas sobre o mesmo layout, nesta ordem:** (1) identidade = cor + tipografia → "personality"; (2) profundidade = luz atrás de frosted glass → "looks expensive"; (3) movimento → "people stop scrolling". "Same layout in all four — the layers are what people remember."
5. **Tipografia de identidade em trio:** sans no headline, serif itálico em 1 palavra/linha de ênfase ("The handoffs run *themselves.*"), mono em labels/metadados.
6. **Confiança = espaço + alinhamento + ritmo calmo.** Mesmo texto, layout diferente muda a credibilidade: 1 CTA primário por tela, uma borda de alinhamento por coluna, margens generosas, nada de widgets competindo acima da dobra. "A page that looks cared for gets believed."
7. **Mostre, não descreva.** Nunca peça "make it look premium". Dê referências reais (URL, screenshot, componente) e decisões concretas (hex, fontes, hierarquia). "Adjectives get you an interpretation. References get you the result."
8. **Marca é julgada em ~3 s, antes do produto**: fachada/site, logo, cores, perfil social e embalagem precisam contar a mesma história. 2–3 cores e consistência valem mais que parecer caro.
9. **Sistema de marca = 1 cor saturada + escuro + 1–2 de apoio**, display larga **só em títulos** + Inter (sans neutra) no corpo; documente hex **e** RGB; 1 palavra do título na cor de marca (padrão dos 3 cases da Ramotion). É o 2+1 da regra 1 em escala de sistema: a cor de apoio extra fica para ícones/ilustração/páginas secundárias, nunca compete com o acento na mesma tela.
10. **Logo**: 1 ideia, funciona pequeno (ícone de app) e em preto e branco chapado, sem depender de degradê/tendência. O movimento faz parte do logo: traço lento = calmo, encaixe rápido = ágil, crescer de um ponto = amigável.
11. **Visual comunica preço**: budget = cores altas + ofertas; mid = azul/bege + selo de valor; premium = preto + dourado, serifa discreta, muito espaço. Defina preço/posicionamento antes; design desalinhado do valor perde vendas.
12. **Movimento: um efeito por vez**, sutil e legível, testado em desktop e mobile. Tipos: headline reveal, micro-interactions, portfolio showcase, animated gallery, scroll reveal. Em página: **um momento animado** (hero ou CTA, não os dois). Valores: `ui-motion`.
13. **60/30/10 por área**: base dominante ~60%, superfícies ~30%, acento ≤10% (CTA, estado interativo, dado-chave). É o 2+1 com número; 10% é teto, não meta. Se o produto deixar o cliente/tenant usar a cor da marca, troque **só o acento** e valide contraste ≥ 4,5:1 nos dois temas antes de salvar. "Se parece poluído, o acento está cobrindo 30% da tela." (`color-palettes.md`)
14. **Paleta de produto = rampa de tons + 1 acento**: 5–6 tons de uma base (fundo → superfície → borda → texto 2 → texto 1) e o acento de matiz oposto no fim. **Confira todo hex de post no conta-gotas** (@uiuxaadi tem rótulo errado).
15. **Sombra tingida, nunca preta chapada**: matiz do fundo escurecido, opacidade ~8%, **blur = 2× o Y** (Y 8 · blur 16). Em tema escuro, profundidade vem de luz/glow atrás de vidro. (`layers-and-trust-layout.md` §4)
16. **Par tipográfico: 2–3 famílias, contraste display × corpo, hierarquia por peso, o mesmo par em tudo.** O trio sans + serif itálico + mono já cabe nesse limite. 12 pares prontos em `references/typography-pairing.md`; escala/line-height/8 pt em `ux-patterns`.
17. **Dê à IA peças reais** (biblioteca de componentes, ícones de uma grade só, skills de avaliação), não "desenhe do zero", e exija os 4 estados: **vazio, carregando, erro e texto longo**. (`claude-web-design-workflow.md`)
18. **Audite antes de refazer e peça conteúdo real antes do layout** (hallmark e 5 prompts de auditoria, rodada 10A): hierarquia → tipo → espaço → cor → "por que parece barato?", uma correção de maior efeito por vez. Degradê, se houver, interpolado em OKLCH (`color-palettes.md`, "Ajustes finos").

## Workflow

1. **Contexto**: produto, público, mood desejado (1 frase) e se precisa transmitir confiança.
2. **Referências**: peça 2–5 sites/imagens ao usuário. Se houver URL, rode `ext-extract-design` para extrair tokens reais. Sem referência, proponha 2–3 combinações do catálogo (`references/color-palettes.md`) e deixe o usuário escolher.
3. **Defina a direção por escrito** (curto): `--base-1`, `--base-2`, `--accent` com hex (e a rampa de tons das bases); onde o acento aparece (≤10% da área); par/trio tipográfico (`typography-pairing.md`); sombra tingida ou glow; o único CTA; qual é a "terceira camada" (cor, luz ou objeto/cena).
4. **Layout primeiro, sem enfeite**: estrutura com espaço, alinhamento e 1 CTA (checklist em `references/layers-and-trust-layout.md` §2).
5. **Camada 1 – identidade** (cores + tipografia). Valide.
6. **Camada 2 – profundidade** (luz/glow, frosted glass, sombras). Valide.
7. **Camada 3 – movimento**, um efeito por vez (implementação: `ui-motion`, `ext-gsap-scrolltrigger`, `ext-gsap-*`). Respeite `prefers-reduced-motion`.
8. **Se o pedido for marca/identidade**: siga o workflow de `references/branding-identity.md` §8 (pesquisa e faixa de preço → paleta → par tipográfico → logo testado pequeno e em P&B → 5 pontos de contato).
9. **Crítica final** com `ext-impeccable` (design system/critique) e `ext-taste-skill` (anti-slop); cheque contraste do acento (AA 4.5:1; texto grande e bordas 3:1) no Coolors contrast checker (`color-palettes.md`, fim).

## Referências — quando abrir

| Arquivo | Abra quando |
|---|---|
| `references/color-palettes.md` | For escolher/propor paleta; precisar de hex; quiser os padrões base→acento (combinações citadas), a **proporção 60/30/10** ou as **rampas de 6 tons** de @uiuxaadi (com os hex errados marcados). |
| `references/layers-and-trust-layout.md` | For montar camadas (identidade/profundidade/movimento), revisar layout por confiança, listar os 5 tipos de movimento, ou definir **sombra tingida** (§4). |
| `references/branding-identity.md` | For criar/revisar **marca**: logo (6 erros), embalagem × faixa de preço, os 5 pontos de contato julgados em 3 s, movimento do logo, sistemas de marca da Ramotion (paleta + par tipográfico + ordem do brand book), antes/depois de paleta e direção de arte de páginas de marca (scroll-storytelling 3D, foto PB com 1 cor, 404). |
| `references/claude-web-design-workflow.md` | For escrever prompts de web design, orientar o usuário a dar referências, planejar o processo com o Claude, escolher **bibliotecas de componentes/skills/ícones para IA** (teste dos 4 estados), **apresentar o design em mockup** (device → plano → recorte 3D), usar os **5 prompts de auditoria** e as 5 skills de design por fase (rodada 10A), ou consultar os **16 repositórios citados (não instalados)**. |
| `references/claude-design-course.md` | For usar o **Claude Design** (app da Anthropic): criar design system/brand, pitch deck, wireframe vs. high-fidelity de landing, protótipo de app mobile, vídeo de lançamento com HyperFrames, levar para Claude Code → GitHub → Vercel, ou economizar o limite de sessão do Design. |
| `references/typography-pairing.md` | For escolher **par de fontes**: 12 pares display + corpo com tom de uso, 4 regras (2–3 famílias, contraste, pesos, consistência) e como o trio sans/serif/mono e o display + Inter da Ramotion se encaixam. |
| `references/learning-sources.md` | Perguntarem **onde continuar aprendendo** ou **quem seguir**: Top 15 do Instagram (foco/risco), inativos para não reavaliar, 15 canais de YouTube, 10 do Facebook (página × grupo, como usar), 10 newsletters/comunidades, galerias de benchmarking (Mobbin, Dribbble, Behance, Awwwards, Land-book, SiteInspire, Coolors, Typewolf) e lacunas (PT-BR, motion de UI). |
| `references/reference-apis.md` | Precisar **buscar referências por programa** (Claude chamando um MCP/API/feed): tabela de Mobbin, Refero, ScreensDesign, Figma, Pinterest, Dribbble, Behance, Land-book, SiteInspire, Awwwards, Page Flows, Godly/recent.design; ranking das 5 melhores; **o conector Mobbin exige plano pago (Pro)**. |
| `references/visual-index.md` | Precisar saber qual imagem mostra qual exemplo antes de abrir uma; ou consultar a tabela **"Perfis avaliados"** (quais contas valem como fonte, inclusive as inativas). |

## Imagens (`assets/visual-refs/*.jpg`)

Folhas de contato 4x3 dos reels (`<ID>.jpg`) e prints únicos das rodadas 1 e 3 (`<ID>_<n>.jpg`). **Só abra quando precisar de exemplo visual concreto** (mostrar ao usuário, conferir composição) — custam contexto e os hex já estão nas references. Melhores apostas:
- `Dfc-Q-0yy0W.jpg` — acento só no botão em landings SaaS (antes/depois).
- `DfSIP2iBuFI.jpg` — mesma página nas 4 camadas.
- `DfyFShTounu.jpg` — layout inseguro vs. seguro (mobile).
- `DfVlIwHISSv.jpg` — terceira camada como luz/objeto 3D.

- `Dak9nkTFpYI_1.jpg` / `Dak9nkTFpYI_2.jpg` — paleta de marca documentada (hex+RGB) e par Funnel Display + Inter (Ramotion).
- `DYpD5C7zwx6_1.jpg` — página de produto com 3D, título outline + sólido.
- `De_FtT3k-tT_1.jpg` (60/30/10) e `De_FtT3k-tT_3.jpg` (sombra tingida) — @gg.designhub.
- `DescJ2zTeSf_1.jpg` — os 12 pares de fontes renderizados (@gfx.om).
- `DfEmKLLFEDi_1.jpg` / `DfUnwyQGCTA_1.jpg` — rampa de 6 tons; o segundo mostra o hex errado.
- `DfkBGDyDgqS_1.jpg` — mosaico de bibliotecas de componentes dark para IA.

- `9C_coolors_contrast-checker_1.jpg` (razão de contraste 8.42) e `9C_typewolf_google-fonts_1.jpg` (40 Google Fonts).
- `9C_perfil-criador_nomey_1.jpg`, `9C_perfil-criador_nomey_2.jpg`, `9C_perfil-criador_nomey_3.jpg` / `9C_propostas_cook_1.jpg`, `9C_propostas_cook_2.jpg` — cases Behance (perfil com 1 CTA, tab bar flutuante, identidade ilustrada); conceitos, não apps reais.

`De9oszIIQ4V.jpg` e `Dfm0NTiIfyd.jpg` são fora do tema (hype de ferramentas de IA); não abra.

## Prioridade entre skills (quando as regras conflitam)

Ordem completa, da mais forte para a mais fraca: **skill de app específico** (ex.: `projetos/marca-pessoal-app/`, copiada para `.claude/skills/` na repo do app) > **skill de SEGMENTO** (`segmento-financeiro`, `segmento-crm`, `segmento-publicidade`, `segmento-marca-pessoal`, `segmento-saude`, `segmento-juridico`) > **plataforma** (`website-ui`, `desktop-app-ui`, `mobile-app-ui`) > **tema** (`design-direction`, `ui-motion`, `ux-patterns`, `dashboard-ui`) > **terceiros** (`ext-*`).
Se o projeto é de um setor, abra primeiro a skill `segmento-*` correspondente.

1. **Valores e decisões de design** (números, quantidade de animação, cor, sombra, tipografia) vêm das **skills do projeto** (app específico → segmento → plataforma → tema, nessa ordem): `website-ui`, `desktop-app-ui`, `mobile-app-ui`, `design-direction`, `ui-motion`, `ux-patterns`, `dashboard-ui`.
2. **Skills de terceiros** (`design-taste-frontend`, `impeccable`, `transitions-*`, `gsap-*`, `playwright-cli`, `extract-design`) servem para **implementação**: código pronto, APIs, checkers e verificação no browser. Use o código delas, mas com os valores do item 1. Vale o mesmo para qualquer skill de terceiros instalada depois (ex.: `expo/skills`, ECC `motion-*`/`frontend-*`, `karpathy-guidelines`, `mattpocock/skills`). Regras de **código** de terceiros ("mínimo que resolve", "sem feature não pedida", mudança cirúrgica) valem para a estrutura do código; os estados (vazio, carregando, erro), a acessibilidade e o `prefers-reduced-motion` que as skills do projeto exigem **fazem parte do pedido de UI**, não são feature extra.
3. Se o checker ou a regra de uma skill de terceiros reprovar algo que segue o item 1, **siga o item 1** e diga ao usuário qual regra externa foi ignorada e por quê.
4. Na plataforma, vale a skill da plataforma (`website-ui`, `desktop-app-ui` ou `mobile-app-ui`); nos temas, vale a skill de tema que ela indicar. A skill de segmento ou de app específico só sobrepõe o que ela disser explicitamente (paleta do setor, tom, compliance, telas obrigatórias); no resto valem plataforma e tema.

| Conflito | Vale | Em vez de |
|---|---|---|
| **Sombras** | Seções e blocos se separam por **espaço ou mudança de fundo**, sem sombra (as duas fontes concordam). **Sombra tingida** (cor do fundo, blur = 2× Y, ~8%) **só em elementos que flutuam**: dropdown, popover, modal, card arrastável, toast | `design-taste-frontend` sem sombras em nada; e sombra preta genérica |
| **Violeta/lilás** | Permitido quando vem da marca, do segmento (lilás Linktree em `segmento-marca-pessoal`, roxo Attio/Pipedrive em `segmento-crm`) ou de paleta escolhida em `design-direction`; nunca como cor padrão sem motivo nem em gradiente roxo→azul (`ux-patterns` `dark-patterns.md`) | `design-taste-frontend`: nunca violeta ou lilás na página |

## Skills complementares (já instaladas)

- `ext-taste-skill` — direção anti-slop, evitar o visual genérico de IA.
- `ext-impeccable` — design system, tokens e critique.
- `ext-extract-design` — extrair cores/fontes/espaçamento de um site por URL (ótimo para o passo "mostrar, não descrever").
- `ui-motion` e `ext-gsap-*` — implementar o movimento.

## Skills externas (dependências)
Esta skill pode delegar para: `ext-taste-skill`, `ext-impeccable`, `ext-extract-design`. Elas **não** fazem parte da repo; são instaladas por `scripts/install-external-skills.sh`.
1. Antes de delegar, confira se a pasta existe em `.claude/skills/<nome>/` ou `~/.claude/skills/<nome>/`.
2. Se faltar, **pergunte ao usuário** antes de instalar e, com o ok, rode `./scripts/install-external-skills.sh` (ou `--global`). Depois da instalação, o Claude Code normalmente já enxerga as skills novas; se alguma não aparecer, leia o `SKILL.md` instalado com Read e siga as instruções dele.
3. Se o usuário não quiser instalar, siga sem elas usando as references desta skill.

