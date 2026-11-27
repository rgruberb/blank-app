# Templates — Publicidade (TPL-PUB)

Cada template é uma **direção** com tokens. Hex medidos vêm da rodada 10B (`getComputedStyle` em páginas públicas,
27/11/2026); `~#` = aproximado (amostrado de JPEG, `dashboard-ui`). Onde a fonte não mediu, está escrito "não medido":
use a paleta da marca do cliente. "(inferência)" = conclusão nossa. Imagens em `../assets/visual-refs/` (ver
`visual-index.md`).

---

## TPL-PUB-01 — Painel de mídia claro
- **Paleta:** fundo `#FFFFFF` / `#F8F9FA`, superfície `#F8FAFD`, seleção `#E8F0FE`; texto `#202124`, secundário
  `#3C4043`, terciário `#5F6368`; ação `#1A73E8` (Google Ads, 10B).
- **Par tipográfico:** `Google Sans` (títulos) + `Google Sans Text` (texto) na fonte; equivalente livre: Inter
  (inferência). Números `tabular-nums`.
- **Escala:** app 1,2 (`desktop-app-ui`); linhas de tabela 13–14px, KPI ≤ ~30px numa linha (10A `Deq_kvJBI3g`).
- **Raio / sombra:** não medidos; separar por fundo e borda, sombra só no que flutua (`design-direction`).
- **Densidade:** alta (tabela de campanhas com colunas configuráveis).
- **Motion:** mínimo; nada se mexe em orçamento ou no botão de publicar.
- **Quando usar:** gerenciador de anúncios, relatório de mídia, painel interno de agência.
- **Fontes:** 10B PUB §2, §13 direção 1 (https://ads.google.com/intl/pt-BR_br/home/).
- **Imagens:** `10C_PUB_dribbble-vektora_nebula-analytics-campanhas_1.jpg` (estrutura KPIs → gráfico → tabela),
  `10A_Deq_kvJBI3g_1.jpg` (KPI numa linha).

## TPL-PUB-02 — Social ads claro
- **Paleta:** fundos `#F1F4F7` / `#F5F6F6` / `#FFFFFF`; texto `#1C1E21`, `#1C2B33`, `#465A69`; ação `#0064E0`
  (Meta Ads Manager, 10B).
- **Par tipográfico:** `Optimistic VF` na fonte; sans humanista equivalente (inferência).
- **Escala:** 1,2 no app; prévias de criativo em tamanho real do posicionamento.
- **Raio / sombra:** não medidos.
- **Densidade:** média-alta; **prévias grandes** ao lado do formulário.
- **Motion:** só a prévia (vídeo/carrossel) se move; transição de painel curta.
- **Quando usar:** criação de anúncio para redes sociais, fluxo objetivo → público → orçamento → criativo.
- **Fontes:** 10B PUB §2, §6, §13 direção 2 (https://www.facebook.com/business/tools/ads-manager;
  https://www.facebook.com/business/ads-guide/update/image).
- **Imagens:** nenhuma tela interna da Meta capturada (lacuna); estrutura de prévia: `CMP-PUB-06`.

## TPL-PUB-03 — Vitrine de agência
- **Paleta:** `#222222` + `#F8F8F8`, apoio `#EDEDED`, destaque `#FFF083`; vermelho `#B42625` pontual (Awwwards, 10B).
- **Par tipográfico:** grotesca — `Inter Tight` na fonte; display grande para o nome da agência/case.
- **Escala:** site 1,25 (16/20/25/32; 10A `DfzcornCO73`), título de case em corpo muito grande.
- **Raio / sombra:** não medidos.
- **Densidade:** baixa (um case por dobra).
- **Motion:** expressivo **só na vitrine** (showreel em tela cheia, rodapé que sobe — 10A `DgNTvDZCMNX`); cada
  interação tem custo em mobile, contraste e performance; respeitar `prefers-reduced-motion`.
- **Quando usar:** site de agência/estúdio, página de case, portfólio de campanhas.
- **Fontes:** 10B PUB §13 direção 3 (https://www.awwwards.com/websites/advertising-agencies/); SiteInspire
  categoria "Agencies & Consultancies" (9C).
- **Imagens:** `10C_PUB_dribbble-talha-sarwar_adexa-case-dashboard-anuncios_1.jpg` (capa de case: marca gigante ao
  fundo + dispositivo), `9C_portfolio_siteinspire_1.jpg`.

## TPL-PUB-04 — Painel de campanhas escuro
- **Paleta:** fundo `~#131416`–`#15161b`, pílula/CTA azul `~#7088e0`; cores de canal (azul, amarelo, verde,
  vermelho) **só em gráficos** (aproximado, `dashboard-ui` §11).
- **Par tipográfico:** não identificado na fonte; sans neutra + `tabular-nums` (inferência).
- **Escala:** 1,2; gasto como número herói no topo.
- **Raio / sombra:** pílulas totalmente arredondadas na top nav; resto não medido.
- **Densidade:** média-alta (Overview, Reports, Campaigns).
- **Motion:** pílula da top nav estica entre itens (`slidePill`, ~0,3 s `power3.out`, trail ~0,55 s); gasto conta
  ao **entrar** na página — nunca durante edição.
- **Quando usar:** painel de agência/anunciante com várias campanhas e canais; quando o cliente pede tema escuro.
- **Fontes:** `dashboard-ui/references/domain-examples.md` §11 (`DfXoXVFPBfd`, @_code_and_chill_).
- **Imagens:** `../../dashboard-ui/assets/visual-refs/DfXoXVFPBfd.jpg`.

## TPL-PUB-05 — Home de ferramenta de marketing
- **Paleta:** não medida (Semrush, Mailchimp, Buffer, Klaviyo só em print). Observado nos prints: CTA de cor
  própria e saturada sobre fundo claro (amarelo Mailchimp, verde-claro Buffer, lilás Semrush), faixa de logos sobre
  bloco de cor (Klaviyo) — use a paleta da marca.
- **Par tipográfico:** não medido; Mailchimp usa serifada em título de seção ("Recommended for your business").
- **Escala:** site 1,25 (`website-ui`).
- **Raio / sombra:** CTA em pílula em todos os prints (observação).
- **Densidade:** baixa no hero; média nas seções de módulos.
- **Motion:** um momento por página (`website-ui`); a home do Framer/Semrush demonstra o produto no hero.
- **Estrutura:** (1) **uma ação principal** — campo de busca/e-mail com CTA (Semrush "Get insights", Buffer "Get
  started for free" com aviso de e-mail logo abaixo); (2) **prova social com número e origem** (Mailchimp 33.000+
  reviews + selos; Buffer 375.227); (3) cards de módulo com mock do produto; (4) segundo CTA para quem não decidiu
  ("Find the right plan").
- **Quando usar:** landing/site de SaaS de marketing, agendador, e-mail marketing, SEO.
- **Fontes:** 10C/C2 (https://www.semrush.com/, https://www.mailchimp.com/, https://buffer.com/,
  https://www.klaviyo.com/).
- **Imagens:** `10C_PUB_semrush_home-busca-insights_1.jpg`, `10C_PUB_mailchimp_home-selos-avaliacao_1.jpg`,
  `10C_PUB_buffer_agendamento-ideias-boards_1.jpg`, `10C_PUB_klaviyo_dashboard-receita-atribuida_1.jpg`.
