# Rodada 6 — Facebook (3 links analisados; Drama Reels excluído a pedido)

## Resumo dos principais aprendizados

- **Só 2 dos links eram vídeos de design utilizáveis** (1 e 3, ambos @Code & Chill). O link 2 abre o perfil da página, não um vídeo. O link 4 (Drama Reels) foi excluído da pesquisa a pedido.
- **Formato dos reels da Code & Chill:** vídeo de ~5 s em loop, vertical 9:16, com título em pêssego no topo, gravação de tela do dashboard no centro, handle `@_code_and_chill_` e um painel de código (editor escuro) embaixo. O painel de código mostra o código da animação (função `slidePill` com GSAP), vendendo "como fazer".
- **Dashboards escuros com 1 cor de acento:** azul-marinho + azul elétrico (SaaS/funnels) e oliva-escuro + verde-limão (crédito privado). Cada tela troca por navegação (pílula ativa que desliza na sidebar), mostrando 4 telas em 5 s.
- **Padrões de componentes vistos:** funil de conversão em colunas, kanban de campanhas (Draft/Scheduled/Live/Done), heatmap de coortes, gauge semicircular (63%), mapa de risco em grade, lista de ativos com thumbnails.
- **Animação como assinatura:** a pílula de navegação desliza entre itens (curva de saída suave), e as telas fazem transição curta; o cursor aparece clicando — o movimento é a demonstração.
- **Limitação:** não consigo ouvir áudio. Os reels 1 e 3 têm "Original audio"/música e nenhuma fala ou legenda na tela, então não há narração a resumir.
- **Pendente:** confirmar qual era o vídeo do link 2.

---

### 1CTThcky5H (reel/1555972142999537) — Code & Chill
- Tipo: reel (5,3 s, em loop)
- Tema: dashboard (UI/motion)
- Legenda: "SaaS revenue analytics dashboard 📈 #dashboard #dataviz #analytics #uidesign #frontend"
- Narração/fala: não há fala nem legenda na tela; o áudio é "Original audio" (não consigo ouvi-lo). Nada a resumir além do texto visível.
- Cena a cena:
  - Layout 9:16 com fundo preto: topo vazio (ou título), gravação de tela do dashboard ocupando ~30% da altura, "@_code_and_chill_" em branco pequeno abaixo, e um editor de código escuro (barra com 3 bolinhas, arquivo `src/ui/action.ts`) embaixo. Código aproximado: `export function slidePill(pill, target) { const box = pill.parentElement; … gsap.to(…, { duration, ease: 'power3.out' … }) }` (leitura aproximada).
  - **0–1 s — Funnels:** UI azul-marinho `#0B1428` com cards `#101C36`; título "Funnels"; sidebar com lista de funis; área principal com 5 colunas verticais (funil por etapa) — a 1ª coluna preenchida em azul `#2F6BFF`, as outras vazias/contorno; KPIs no topo (42k, 5.6k, 1.9k, 2.8k, 1.1k, aproximado); cursor sobre as colunas. Pílula ativa na sidebar.
  - **~2,2 s — Campaigns (kanban):** título "Campaigns"; 4 colunas Draft / Scheduled / Live / Done com cards de campanha e mini-barras de progresso verdes/azuis; cursor sobre um card Live.
  - **~3,4 s — Campaigns (receita):** cards com métricas e barras verde-azuladas `#2FD6A5`; cartão "$10,822" à direita; abaixo bloco "Recently…" (lista).
  - **~5 s — Cohorts:** título "Cohorts"; 3–4 KPIs no topo (ex.: "$2.9k", "63%", "78.0%", data "May 2026"); heatmap triangular de retenção por coorte × mês em tons de azul `#1D3FA8` → `#5B8CFF` (mais claro = maior retenção).
  - Transição: a pílula ativa desliza na sidebar e a tela troca; o cursor clica no item de navegação.
- Regras/lições práticas:
  - Mostrar 4 telas-chave de um SaaS (funil, campanhas, receita, coortes) em 5 s resume o produto.
  - Um único hue (azul) em 3–4 tons para dados; claro = valor alto no heatmap; tipografia sans neutra.
  - Navegação com pílula deslizante (GSAP, `power3.out`) dá continuidade entre telas.
  - Colocar o código ao lado da demo aumenta o valor percebido (ensina e vende).

---

### 1AE3r4BKt6 — Code & Chill (página)
- Tipo: perfil/página (o link não é um vídeo nem um post)
- Tema: outro
- Legenda: não aplicável. Na hora da abertura, o post mais recente da página era "Music listening app dashboard 🎧 #dashboard #react #uianimation #webdesign #frontend" (publicado há ~8 min, áudio "Memory Reboot · VØJ"). Não é certo que seja o vídeo desejado, então **não analisei**.
- Narração/fala: —
- Cena a cena: —
- Regras/lições práticas: —
- Dados da página (visíveis): Code & Chill ✔, 20K seguidores, 10 seguindo, loja codeandchill.store, portfólio hasib.site, "Web Designer", Bangladesh.

---

### 1A3pMvMBW2 — Code & Chill
- Tipo: reel (5,6 s, em loop)
- Tema: dashboard (UI/motion)
- Legenda: "Private credit loan management dashboard 🏦 #dashboard #dataviz #uianimation #webdesign #frontend" (áudio: "XNIMXS · Let Him Cook")
- Narração/fala: sem fala nem legenda; só música. Nada a resumir.
- Cena a cena:
  - Layout igual ao reel 1: título "Management Dashboard" em pêssego `#FFB86B` (sans semibold ~20px) no topo; gravação de tela no centro; "@_code_and_chill_" abaixo; painel de código (src/ui…) embaixo.
  - Estética: fundo marrom-oliva escuro `#17140F` com vidro fosco (blur) sobre foto desfocada; acento verde-limão `#B8F03C` (botões "New", item ativo da sidebar, badges); texto bege claro.
  - **0,3 s — Property (Casa Duna):** breadcrumb, título "Casa Duna", botões ("Watch", "Download", "Record payment" em verde-limão); foto grande de casa moderna no deserto com tira de thumbnails embaixo; à direita card com gauge semicircular amarelo `#E8C547` "63,4%" (varia 62,8–63,4%) e mini-métricas.
  - **~2,8 s — Portfolio:** cards de KPI (ex.: "$8.27m", "20,6%"?, "2,1k"), gráfico de área "Total outstanding $14.18m" com botão verde "Add"; lista lateral.
  - **~4,1 s — Portfolio (atualizado):** "$14.97m", "64,6%", "1,8x"; lista "Recent activity" à direita com 4 itens.
  - **~5,5 s — Risk:** grade 5×N de células em terracota `#8A5A48`/`#A86B52` (heatmap de risco), uma célula com contorno verde-limão; à direita lista de propriedades com miniaturas (Casa Duna, Harbor Crest, "Cedar Ridge Lodge"…) e valor "…54m".
  - Sidebar de ícones vertical com item ativo em pílula verde-limão que desliza entre itens; cursor clicando a navegação superior (breadcrumb muda: Dashboard → Portfolio → Risk).
- Regras/lições práticas:
  - Para fintech de crédito/imobiliário, o tema "vidro escuro + foto do ativo" humaniza dados financeiros.
  - Acento único (verde-limão) para ação e estado ativo; amarelo reservado a métricas (gauge); terracota para risco.
  - Gauge semicircular + valor grande resume a saúde do ativo; heatmap em grade para risco.
  - Ordem de telas: ativo → portfólio → risco — fluxo de leitura do micro ao macro.
  - Os números oscilam de um frame para outro (animação de contagem) — mostrar valores vivos reforça o realismo.

---

## Prints

Arquivos enviados com este `.md` (nome | link direto / segundo do vídeo | o que mostra e por que importa).

| Arquivo | Link direto | O que mostra / por que importa |
|---|---|---|
| 1CTThcky5H_1.png | https://www.facebook.com/reel/1555972142999537 (≈1 s) | Tela "Funnels": funil em 5 colunas azuis sobre fundo azul-marinho + painel de código embaixo; mostra o enquadramento 9:16 padrão da série |
| 1CTThcky5H_2.png | https://www.facebook.com/reel/1555972142999537 (≈2 s) | Tela "Campaigns" em kanban (Draft / Scheduled / Live / Done); padrão de componente com cards e barras |
| 1CTThcky5H_3.png | https://www.facebook.com/reel/1555972142999537 (≈5 s) | Tela "Cohorts": heatmap triangular de retenção em tons de azul; exemplo de escala de cor sequencial |
| 1A3pMvMBW2_1.png | https://www.facebook.com/share/r/1A3pMvMBW2/ (≈0 s) | "Casa Duna": foto do ativo, gauge amarelo 63% e acento verde-limão sobre vidro escuro |
| 1A3pMvMBW2_2.png | https://www.facebook.com/share/r/1A3pMvMBW2/ (≈3 s) | "Portfolio": KPIs e gráfico de área "$14.18m" com botão verde; hierarquia de números grandes |
| 1A3pMvMBW2_3.png | https://www.facebook.com/share/r/1A3pMvMBW2/ (≈5 s) | "Risk": heatmap em terracota com célula destacada em verde-limão e lista de propriedades |
