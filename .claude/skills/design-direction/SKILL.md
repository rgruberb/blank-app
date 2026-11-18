---
name: design-direction
description: Direção de arte e identidade visual para sites, landing pages, apps e marcas — escolhe paleta de 2 cores base + 1 acento (com catálogo de combinações e hex), empilha "camadas" visuais (identidade → profundidade → movimento), aplica layout que transmite confiança (espaço, alinhamento, ritmo calmo) e guia o workflow de usar o Claude para web design mostrando referências em vez de descrever com adjetivos, inclusive para adicionar movimento; cobre também branding (logo, embalagem que comunica preço, sistema de marca com paleta e par tipográfico, movimento do logo). Use quando o usuário pedir "escolhe uma paleta", "que cores usar no site", "deixa com cara premium/cara de startup", "o site está genérico/sem personalidade", "melhora a direção de arte", "parece pouco confiável", "como pedir pro Claude fazer um site bonito", "adiciona animação/movimento no site", "Claude Design", "como usar o Claude Design", "design system no Claude Design", "pitch deck/landing/protótipo de app/vídeo de lançamento no Claude Design", "limite do Claude Design acabou", "branding", "identidade visual", "criar marca/logo", "brand book", "embalagem/packaging", "o logo está ruim", "animar o logo", "parece barato/caro demais", ou antes de começar a UI de uma landing page nova.
---

# Design Direction

Destilado de 11 reels sobre direção de arte web (paletas 2+1, camadas, layout de confiança, workflow com Claude) e da rodada 3 de perfis (branding, logo, embalagem, sistemas de marca da Ramotion, antes/depois de paleta). Use para **decidir** a direção antes de codar e para **corrigir** UIs genéricas.

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
12. **Movimento: um efeito por vez**, sutil e legível, testado em desktop e mobile. Tipos: headline reveal, micro-interactions, portfolio showcase, animated gallery, scroll reveal.

## Workflow

1. **Contexto**: produto, público, mood desejado (1 frase) e se precisa transmitir confiança.
2. **Referências**: peça 2–5 sites/imagens ao usuário. Se houver URL, rode `ext-extract-design` para extrair tokens reais. Sem referência, proponha 2–3 combinações do catálogo (`references/color-palettes.md`) e deixe o usuário escolher.
3. **Defina a direção por escrito** (curto): `--base-1`, `--base-2`, `--accent` com hex; onde o acento aparece; trio tipográfico; o único CTA; qual é a "terceira camada" (cor, luz ou objeto/cena).
4. **Layout primeiro, sem enfeite**: estrutura com espaço, alinhamento e 1 CTA (checklist em `references/layers-and-trust-layout.md` §2).
5. **Camada 1 – identidade** (cores + tipografia). Valide.
6. **Camada 2 – profundidade** (luz/glow, frosted glass, sombras). Valide.
7. **Camada 3 – movimento**, um efeito por vez (implementação: `ui-motion`, `ext-gsap-scrolltrigger`, `ext-gsap-*`). Respeite `prefers-reduced-motion`.
8. **Se o pedido for marca/identidade**: siga o workflow de `references/branding-identity.md` §8 (pesquisa e faixa de preço → paleta → par tipográfico → logo testado pequeno e em P&B → 5 pontos de contato).
9. **Crítica final** com `ext-impeccable` (design system/critique) e `ext-taste-skill` (anti-slop); cheque contraste do acento (AA 4.5:1).

## Referências — quando abrir

| Arquivo | Abra quando |
|---|---|
| `references/color-palettes.md` | For escolher/propor paleta; precisar de hex; quiser os padrões base→acento (16 combinações citadas). |
| `references/layers-and-trust-layout.md` | For montar camadas (identidade/profundidade/movimento), revisar layout por confiança, ou listar os 5 tipos de movimento. |
| `references/branding-identity.md` | For criar/revisar **marca**: logo (6 erros), embalagem × faixa de preço, os 5 pontos de contato julgados em 3 s, movimento do logo, sistemas de marca da Ramotion (paleta + par tipográfico + ordem do brand book), antes/depois de paleta e direção de arte de páginas de marca (scroll-storytelling 3D, foto PB com 1 cor, 404). |
| `references/claude-web-design-workflow.md` | For escrever prompts de web design, orientar o usuário a dar referências, ou planejar o processo com o Claude. |
| `references/claude-design-course.md` | For usar o **Claude Design** (app da Anthropic): criar design system/brand, pitch deck, wireframe vs. high-fidelity de landing, protótipo de app mobile, vídeo de lançamento com HyperFrames, levar para Claude Code → GitHub → Vercel, ou economizar o limite de sessão do Design. |
| `references/visual-index.md` | Precisar saber qual imagem mostra qual exemplo antes de abrir uma; ou consultar a tabela **"Perfis avaliados"** (quais contas valem como fonte, inclusive as inativas). |

## Imagens (`assets/visual-refs/*.jpg`)

Folhas de contato 4x3 dos reels (`<ID>.jpg`) e prints únicos da rodada 3 (`<ID>_<n>.jpg`). **Só abra quando precisar de exemplo visual concreto** (mostrar ao usuário, conferir composição) — custam contexto e os hex já estão nas references. Melhores apostas:
- `Dfc-Q-0yy0W.jpg` — acento só no botão em landings SaaS (antes/depois).
- `DfSIP2iBuFI.jpg` — mesma página nas 4 camadas.
- `DfyFShTounu.jpg` — layout inseguro vs. seguro (mobile).
- `DfVlIwHISSv.jpg` — terceira camada como luz/objeto 3D.

- `Dak9nkTFpYI_1.jpg` / `_2.jpg` — paleta de marca documentada (hex+RGB) e par Funnel Display + Inter (Ramotion).
- `DYpD5C7zwx6_1.jpg` — página de produto com 3D, título outline + sólido.

`De9oszIIQ4V.jpg` e `Dfm0NTiIfyd.jpg` são fora do tema (hype de ferramentas de IA); não abra.

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

