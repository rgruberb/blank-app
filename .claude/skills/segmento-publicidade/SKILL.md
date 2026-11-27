---
name: segmento-publicidade
description: 'Camada de SEGMENTO publicidade (código PUB) para qualquer agência, anunciante, gestor de tráfego ou ferramenta de marketing. Duas faces — ferramenta densa e neutra (Meta #0064E0, Google #1A73E8 sobre cinzas claros) e criativo/vitrine expressiva (Awwwards #222222/#FFF083) —, especificação de anúncio da Meta (4:5, 1440×1800, título 27 caracteres), KPI com período e comparação, o que nunca animar (orçamento, publicar), anúncio identificável (CONAR art. 28, CDC art. 36), templates TPL-PUB e componentes CMP-PUB (campanha/conjunto/anúncio, orçamento, prévia por posicionamento, selo Publicidade). Use em "agência", "campanha", "anúncio", "ads manager", "gerenciador de anúncios", "criativo", "mídia paga", "tráfego pago", "gestor de tráfego", "ROAS", "CTR", "painel de campanhas", "agendador de posts", "e-mail marketing", "site de agência", "publi", "parceria paga".'
---

# Segmento: Publicidade (PUB)

Skill de **segmento**: o que muda quando o produto é de publicidade, para qualquer empresa do setor (agência,
anunciante, ferramenta de mídia, agendador, e-mail marketing). Não repete regras gerais: plataforma (`website-ui`,
`desktop-app-ui`, `mobile-app-ui`) e tema (`design-direction`, `ui-motion`, `ux-patterns`, `dashboard-ui`) continuam
valendo. Fontes: ficha PUB da rodada 10B (27/11/2026), imagens 10C/C2–C4, posts 10A. "(inferência)" = conclusão
nossa, não está na fonte.

## Código
**PUB.** Templates `TPL-PUB-NN`, componentes `CMP-PUB-NN`. Imagens podem receber `REF-PUB-NN` em
`references/visual-index.md` (coluna vazia, a preencher).

## Quando usar
- Gerenciador de anúncios, painel de campanhas/relatórios, criação de criativo com prévia, agendador de posts,
  e-mail/SMS marketing com receita atribuída, ferramenta de SEO/visibilidade.
- Site de agência/estúdio (vitrine de cases) e landing de ferramenta de marketing.
- Peça publicitária (post, reel, carrossel, banner) quando a regra é de formato ou de identificação do anúncio.
- Criador de conteúdo com publi → `segmento-marca-pessoal` (o selo vem daqui, `CMP-PUB-08/09`).

## Prioridade
skill de app específico > **segmento (esta)** > plataforma > tema > terceiros (`ext-*`). Em conflito, esta vence a
de plataforma (ex.: densidade alta numa tabela de campanhas mesmo no mobile de consulta).

## Tom e personalidade
- **Ferramenta:** funcional, analítica, neutra. O gestor quer controle de orçamento e resultado.
- **Criativo/agência:** ousado, autoral, editorial. O cliente da agência quer impacto (inferência, 10B).
- Regra-mãe (inferência): **a UI da ferramenta não compete com o criativo do cliente**; cor forte é do anúncio.

## Regras centrais
**Paleta (hex medidos com `getComputedStyle` em páginas públicas, 10B; produto logado não medido)**
- Meta Ads Manager: azul `#0064E0`; fundos `#FFFFFF` `#F1F4F7` `#F5F6F6`; texto `#1C1E21` `#1C2B33` `#465A69`.
- Google Ads: azul `#1A73E8`; fundos `#F8F9FA` `#F8FAFD` `#E8F0FE`; texto `#202124` `#3C4043` `#5F6368`.
- Awwwards (vitrine de agências): `#222222` `#F8F8F8` `#EDEDED`; destaque `#FFF083`; `#B42625`.
- Padrão: azul + neutros claros na ferramenta. **Evitar** (inferência): paleta de UI saturada que brigue com o
  criativo; vermelho/verde como único sinal de status ou de variação.

**Tipografia**
- Meta `Optimistic VF`; Google `Google Sans`/`Google Sans Text`; Awwwards `Inter Tight`. Tabular e mínimo: não
  verificados nos produtos.
- Valor de KPI: **uma linha, `tabular-nums`, `white-space: nowrap`, ~30px no máximo** em card estreito; a 48px o
  valor quebra (10A `Deq_kvJBI3g`, "One line, capped size").
- Site/peça: escala 1,25 (16/20/25/31,25≈32), linha de 45–75 caracteres (10A `DfzcornCO73`, `DgOzQOLk5m9`).

**Densidade**
- **Alta na ferramenta** (muitas campanhas, colunas, métricas); **baixa no criativo** (uma mensagem por peça). O
  gestor compara linhas; o anúncio é lido em segundos (inferência, 10B).

**Motion**
- Aceitável: prévia animada de anúncio, vídeo e carrossel (são o produto); transição de painel. A Meta recomenda
  "movimento e som" em anúncio de vídeo (Ads Guide).
- **Nunca animar** (inferência): números de gasto/orçamento enquanto o usuário edita; botão de publicar.
- Reel/carrossel: ≤ 6 palavras por tela, ~1,2 s cada (`ui-motion/references/motion-for-social-video.md`).

**Dados e números**
- Meta, imagem no Feed: JPG/PNG, **4:5, 1440×1800 px**, texto principal **50–150** caracteres, título **27**,
  máx. **30 MB**, mín. **600×750** em 4:5, tolerância de proporção **3%**. Carrossel: até **10** cards. Outros
  posicionamentos e Google: não verificados.
- Métrica isolada engana: custo por lead baixo com gancho/retenção ruins (Medium, secundária) → **qualidade ao lado
  do custo**.
- Moeda e período explícitos; variação vs. período anterior; atribuição e janela rotuladas (inferência).
- Confira coerência: no conceito Nebula, "Spend $12,845 of $5,000 budget" e "Raos 48.7K" (observação nossa da
  imagem) — dado de mock quebrado derruba a confiança.

**Confiança**
- Anunciante: transparência de gasto e de atribuição. Público: anúncio identificável.
- Prova social com número e origem: "33.000+ reviews" + Capterra/TrustRadius/G2 (Mailchimp); "375.227 criadores,
  marcas e agências" (Buffer).

**Regulação (resumo; detalhe em `references/regulacao.md`, não é aconselhamento jurídico)**
- CONAR art. 28 e CDC art. 36: anúncio **claramente identificável** em qualquer formato → selo "Publicidade".
- CONAR art. 27: apresentação verdadeira (preço, condição, testemunhal). CDC art. 37 §1º/§2º: enganosa/abusiva.
- CONAR art. 37: sem apelo imperativo de consumo dirigido à criança.
- Guia CONAR de influenciadores (05/2026) e políticas Meta/Google: **não lidos**.

**Acessibilidade**
- Contraste do texto sobre imagem; **legenda em vídeo** (muito consumo sem som; Kontentino, secundária); texto
  alternativo. Contraste mínimo 4,5:1 em texto (WCAG AA, 10A `DfJaRP4n8e4`). Medições nos produtos: não feitas.

## Diferenças por plataforma
| Website | App desktop | App mobile |
|---|---|---|
| Ads Manager na web é o principal para criação; site de agência = vitrine | relatórios e criação em massa (inferência) → `desktop-app-ui` | app Ads Manager (iOS/Android): monitorar, pausar, ajustar orçamento → `mobile-app-ui` |

## Templates (`references/templates.md`)
- `TPL-PUB-01` Painel de mídia claro (Google Ads)
- `TPL-PUB-02` Social ads claro (Meta)
- `TPL-PUB-03` Vitrine de agência (Awwwards)
- `TPL-PUB-04` Painel de campanhas escuro (Code & Chill `DfXoXVFPBfd`)
- `TPL-PUB-05` Home de ferramenta de marketing (Semrush, Mailchimp, Buffer, Klaviyo)

## Componentes (`references/componentes.md`)
- `CMP-PUB-01` Hierarquia campanha → conjunto → anúncio
- `CMP-PUB-02` Seletor de objetivo
- `CMP-PUB-03` Barra de orçamento (diário/vitalício)
- `CMP-PUB-04` Tabela de desempenho com colunas configuráveis
- `CMP-PUB-05` Linha de KPIs com período e variação
- `CMP-PUB-06` Prévia por posicionamento e dispositivo
- `CMP-PUB-07` Checagem de especificação do criativo
- `CMP-PUB-08` Selo "Publicidade/Patrocinado"
- `CMP-PUB-09` Rótulo de parceria paga
- `CMP-PUB-10` Receita atribuída por canal + recomendação
- `CMP-PUB-11` Calendário de publicação + quadro de ideias
- `CMP-PUB-12` Prova social com origem
- `CMP-PUB-13` Anel de distribuição de verba por canal

## Anti-padrões
- Anúncio disfarçado de conteúdo editorial (CONAR 28, CDC 36); "a partir de" sem condição (CDC 37 §1º);
  depoimento falso (CONAR 27).
- Na ferramenta (inferência): recomendação automática pré-aplicada que aumenta gasto; orçamento padrão alto; número
  de gasto que se mexe enquanto o usuário edita; publicar sem prévia por posicionamento.
- KPI sem período/moeda; custo sem métrica de qualidade ao lado; mock com números incoerentes.
- UI colorida competindo com o criativo; status só por cor.

## Workflow
1. Qual face? **Ferramenta** (TPL-PUB-01/02/04) ou **vitrine/landing** (TPL-PUB-03/05)? Qual plataforma?
2. Aplique tom, paleta e densidade acima; escolha o template e os CMP-PUB necessários.
3. Em criação de anúncio: `CMP-PUB-06` + `CMP-PUB-07` antes de publicar; `CMP-PUB-08/09` sempre que houver anúncio.
4. Em relatório: `CMP-PUB-05` com período, moeda e comparação; `CMP-PUB-04` com colunas configuráveis.
5. Revise com `references/regulacao.md` e os anti-padrões; confira contraste e legenda de vídeo.

## Onde está o resto
- Detalhe: `references/templates.md`, `references/componentes.md`, `references/regulacao.md`,
  `references/fontes.md`, `references/visual-index.md`; imagens em `assets/visual-refs/`.
- Dashboard de campanhas (Code & Chill `DfXoXVFPBfd`, Spring Launch `De12lc1vUmr`, Campaigns `DffBnb2vlUn`):
  `.claude/skills/dashboard-ui/references/domain-examples.md` §1, §4, §11 e `dashboard-ui/references/visual-index.md`.
- Paleta e tipografia: `.claude/skills/design-direction/references/color-palettes.md`, `typography-pairing.md`;
  marca: `branding-identity.md`.
- Reel, carrossel, logo animado: `.claude/skills/ui-motion/references/motion-for-social-video.md`.
- Landing/site de agência: `.claude/skills/website-ui/references/website-patterns.md` (§1 hero, §2 prova social).
- Tabela densa, atalhos: `.claude/skills/desktop-app-ui/`; app de consulta: `.claude/skills/mobile-app-ui/`.
- Dark patterns: `.claude/skills/ux-patterns/references/dark-patterns.md`.
- Criador/influenciador: `.claude/skills/segmento-marca-pessoal/`.
