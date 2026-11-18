---
name: dashboard-ui
description: Galeria de referências e padrões visuais para dashboards e web apps — SaaS, varejo, kanban, CRM, saúde, logística, fintech/crédito, investimento/trading, apps de score (fitness, finanças pessoais), fluxos de pedido em etapas e "OS" operacionais sobre foto aérea — com folhas de contato e prints em assets/visual-refs, receita de glassmorphism e padrões de gamificação (progresso, metas, níveis, ranking) para painel de gestor e de cliente. Use ao "criar dashboard", "painel admin", "tela de analytics", "KPI cards", "sidebar de app", "kanban", "glassmorphism", "dashboard fintech", "dashboard de saúde", "app fitness", "score de crédito", "app de investimento/trading", "card de ticker", "gamificação", "painel com metas", "acompanhamento de pedido" ou ao revisar hierarquia, paleta e densidade de um painel existente.
---

# dashboard-ui

Padrões de layout, KPI, gráficos, paleta e glassmorphism para dashboards, tirados de referências reais
(@_code_and_chill_, @ui.iliasmiah000, @code.xr, @felvrabr; na rodada 3 @rish_designs, @ramotion, @ui.pixel; nas rodadas
2, 5–7 @shohan.designs/Orbix Studio, @webdesignssphere, @uiuxcenter, @orbixdashboard, @uiuxsharon). As imagens estão em `assets/visual-refs/<ID>.jpg`;
o índice com autor, URL e quando abrir cada uma está em `references/visual-index.md`.

## Gatilhos adicionais
Também use para: "tela de login com vidro", "dashboard gamificado", "painel do gestor/cliente com metas", "corretora",
"carteira de ações", "tela de compra/venda", "skeuomorfismo", "dashboard cripto", "saldo e gastos", "health score",
"workout progress", "dashboard logístico/rastreio", "perfil de atleta", "Sankey", "heatmap de cashflow",
"estado vazio de card", "apresentar dashboard em mockup".

## Quando usar
- Montar do zero um dashboard, painel admin, tela de analytics, kanban ou portal B2B.
- Escolher entre tema escuro, claro ou glass para um app de dados.
- Fazer cards, sidebar ou formulário de login em glassmorphism.
- Prototipar um painel **gamificado** (progresso, metas, níveis, ranking) para gestor e/ou cliente —
  `references/layout-patterns.md` §7.
- Montar **app de investimento/trading** (lista de ativos, detalhe com gráfico, Buy/Sell) — `references/layout-patterns.md` §8.
- Montar fluxo de app de serviço com **pedido em etapas** e checkout — `layout-patterns.md` §9.
- Montar **dashboard fintech web** (saldo, moedas, transações, watchlist) ou **app de score** (crédito, finanças
  pessoais, fitness) — `layout-patterns.md` §10 e `domain-examples.md` §22–29.
- Revisar um painel que parece genérico ("AI slop"): KPIs sem hierarquia, gradiente roxo aleatório, cards iguais.

## Padrões recorrentes (o que as referências têm em comum)
1. **Estrutura fixa: navegação + header + canvas de cards.** Duas variantes:
   - *Rail de ícones* estreito à esquerda (varejo: pílula preta flutuante; tasks; SaaS) + **top nav em pílulas**
     com o item ativo preenchido (preto no claro, teal/verde no escuro).
   - *Sidebar larga* com logo + workspace no topo, busca, grupos rotulados (MAIN / WORKSPACE) em caps pequenas,
     badges de contagem à direita, card de usuário no rodapé (saúde, smart home, orçamento, sidebar V5).
2. **Header de página = título grande + subtítulo de contexto + ações à direita** (filtros em pílula,
   período 7D/30D/90D em segmented control, CTA primário preenchido com a cor de destaque).
   A home quase sempre é uma **saudação pelo nome** ("Good morning, Dana/Lin/Noa/Ines/Noor", "Good Afternoon, Sarah",
   "Hello, ...") seguida de um resumo do dia ("23 cases need attention today").
3. **Faixa de KPIs logo abaixo do header**, 3 a 6 itens: rótulo minúsculo em caps → número grande em peso
   regular/medium → delta em chip colorido (verde ▲, vermelho ▼, âmbar "overdue"). Varejo destaca o
   **KPI principal invertido** (card preto num tema claro) e põe sparkline em cada card.
4. **Grid assimétrico abaixo dos KPIs**: um gráfico largo (~2/3) + coluna estreita (~1/3) com breakdown,
   gauge ou lista. Depois uma linha de tabela/lista + card de insight (assistente de IA, na saúde).
5. **Uma cor de destaque só**, aplicada a: item ativo, CTA, série principal do gráfico, chips positivos.
   Barras/séries secundárias em tons neutros do próprio fundo (barras cinza-escuro com a barra atual em mint).
   Exceção consciente: KPI cards **tingidos cada um com um tom terroso** (seguros: teal, marrom, azul-acinzentado, ferrugem).
6. **Kanban é o layout dominante em apps de trabalho** (tasks, campanha "Spring Launch" do varejo, pipeline de seguros):
   colunas com cabeçalho (ponto colorido + nome + contagem), cards com tag de projeto colorida, título,
   barra de progresso fina, avatar e data.
7. **Gráficos com "personalidade" sóbria**: gauge de ticks (saúde), barras de ticks empilhados estilo equalizador,
   heatmap de coorte em triângulo (SaaS), funil em barras, anéis de atividade (tasks), dial de termostato e grade de
   agenda (smart home). Sempre um destaque, o resto neutro.
8. **Movimento funcional, não decorativo**: troca de tema com `startViewTransition` + clip-path em círculo
   a partir do botão; pílula ativa que desliza com borda dianteira rápida e traseira atrasada (GSAP);
   **troca de página com o conteúdo desfocando e voltando** (SaaS, orçamento, smart home, V7/V8);
   barco que percorre a rota no stepper; números que contam até o valor; entrada escalonada dos cards (saúde).
   Detalhes em `references/layout-patterns.md`.
9. **Objeto do domínio como canvas operacional** (série @felvrabr: fazenda, usina, resort): foto aérea em tela cheia
   com polígonos/pins que carregam estado, popover com 1 número + 1 CTA, e **a ação muda o estado no próprio objeto**
   ("Start irrigation" → "✓ Irrigating · 40 min", talhão âmbar → verde). Coluna "Overview" de vidro escuro com KPIs 2x2,
   chips de estado em palavra ("Healthy", "On track"), gauge "TODAY" e checklist segmentado "3/4". Mesmo layout,
   acento trocado por domínio.
10. **Progresso como linguagem** (base para gamificação): gauges que enchem, anéis N/M, checklists segmentados,
    números que contam. Nenhuma referência tem pontos/badges/ranking explícitos — esses blocos estão em
    `layout-patterns.md` §7 marcados como complemento.
11. **O acento marca o que pede ação ou bate a meta**, não o maior número: KPI "Overdue" cheio de coral contra 3 neutros
    (Ember V29), barras acima da linha de meta tracejada em laranja e abaixo em cinza (vendas), célula de risco
    selecionada só com contorno no acento. Período anterior = linha **tracejada** neutra, não uma 2ª cor.
12. **Design para o momento de decisão** (investimento/trading): a tela responde de cara o que se mexe, o preço e para
    onde olhar; card de ticker = logo + ticker em negrito + nome embaixo | preço + variação com **sinal e cor** em pílula;
    detalhe com seletor 1D…ALL, card de IA com veredito curto e **Buy/Sell do mesmo tamanho fixos no rodapé**.
    Verde/vermelho só para variação de preço. Detalhes em `layout-patterns.md` §8.
13. **Fluxo de pedido em etapas**: progresso em 4 passos com rótulos curtos repetido na home e no detalhe; rodapé fixo
    com total + 1 CTA (o valor do botão bate com o total); tab bar com a ação principal destacada. `layout-patterns.md` §9.
14. **Fintech web: peso visual na ordem de leitura** — saldo gigante + delta → **composição do total logo abaixo** →
    1 CTA cheio no acento + 2 em contorno → cards por ativo + **card tracejado "adicionar"** → gráfico com tooltip →
    atividade/transações; coluna lateral com 1 ação (Convert) e 1 monitor (Watchlist). Vaulto `DfcdrhgFFMR_1`, Zentra. §10.
15. **Status vira ação**: card de rastreio com timeline + responsável + ligar/mensagem; talhão "Ready" + "Start harvest";
    a ação mais comum ("Create New Request") fixa no topo. Em tela aberta por horas, o acento só marca alerta/botão/status
    (logística `DftsSH-jnfs_1`, a melhor justificativa escrita).
16. **Score = número + delta + palavra + data**, dentro de faixas/arco, com 1 botão de próximo passo ("730 +6 pts
    Excellent · Updated 5 days ago"; "93% · Your Body Is Ready · Start Workout"). Cor do delta pelo sentido **bom/ruim**,
    não pelo sinal (alerta subindo nunca em verde).

## Paleta: escuro vs claro
- **Escuro neutro-quente** (saúde, tasks): fundo `#0b0c0e`, cards `#151618`–`#1b1c1e`, borda 1px `rgba(255,255,255,.06)`,
  destaque único (mint `~#2fb58f`, azul `#3b82f6` ou magenta `#d12777`). Texto secundário ~55% de opacidade.
- **Escuro com glow ambiente** (SaaS azul `#0a1530`→`#1d3aa8`, seguros teal `#04161a` com ondas e brilho âmbar,
  orçamento verde musgo `#1c2a1e` com acento menta `#8af1b6`):
  um radial-gradient grande e desfocado atrás do conteúdo; cards translúcidos por cima.
- **Claro monocromático** (varejo): fundo `#eceeed`, cards brancos e cinza-claro `#e2e4e3`, cards-destaque pretos
  `#111`, sombra mínima; a única cor são os deltas verdes. Seguros (detalhe) usa claro com névoa teal `#e6f7f8`.
- **Monocromático quente** (CRM de interiores `DfeT74YvQaD`): só tons de café/sépia `#261e13`–`#4b3f2f`, ativo em pílula creme.
- **Vinho/magenta com glows** (e-commerce `Dfct0mNvg3f`): sidebar magenta `#781840`, CTA rosa `#bf6888`, glows laranja e azul.
- **Vidro escuro tingido pela foto** (@felvrabr): oliva + lima `#c6e17a`, ardósia + âmbar `#f0b048`, petróleo + menta `#6cf0c9`.
- **Glass neutro** (smart home): tudo em cinza grafite translúcido `#505251`, ativo em pílula branca; a cor vem das fotos.
- **Claro menta + preto** (verificação `Dfz0mLAzsjg`): cinza `#EDEFEE`, cards menta `#CFE5E0`, 1 card preto de quebra.
- **Terracota + lima** (crédito privado `Dfo0F0Pvo4Y`): escala terracota `#B8664D`–`#D98A6C`, acento `#C8F23A` — fintech sem azul.
- **Skeuomórfico creme** (`DfuS2Jbzsjt`): creme `#EFE7DC` em relevo, acento coral/laranja, marrom/preto de contraste.
- **Branco + coral de urgência** (Ember V29 `DfrtgFyTmOM`): sidebar escura, coral `#F26B5E` só em atrasados/leads quentes.
- **Trading dark + limão** (`DXeeUP7FKGs_1`): `#0B0B0D` + `#D4FF3A` em ativo/CTA positivo; vermelho `#E0352B` só para queda/Sell.
- **Fintech preto + 1 acento** (Orbix Studio): Vaulto `#0B0B0C` + laranja `#FF5A1F`; Zentra `#0E0E10` + roxo `#6D4AFF`;
  CareNest petróleo + teal `#3FB8A8` com bege só nos gráficos. Séries de gráfico podem ter cor própria (vermelho de gasto,
  laranja BTC/azul ETH). **Divergência:** finanças pessoais `DfmwyDclA0Q` usa 2 acentos com papel fixo (azul = ação,
  lima = score) — só aceite com papéis documentados.
- **Claro pastel com gradiente** (CreditPros `DfaQe-CiBfJ_1`): branco → pêssego → verde-claro, ✓ em limão `#D4F53C`.
- **Claro + 1 acento** (Deuce `Dfus5sWFAov_1` verde-oliva `#7A9A3A`; MediCore `DfUWa0jAed7_1` azul `#3B82F6`).
- Ofereça os dois temas quando o painel for uso diário (varejo e seguros mostram dark + light do mesmo produto,
  com a troca animada).

## Receita de glassmorphism (série @code.xr + smart home)
Funciona **só sobre um fundo com conteúdo** (foto de interior, ondas 3D, gradiente vivo). Sobre fundo liso vira cinza.
```css
.glass {
  background: rgba(255,255,255,.08);          /* escuro: .06–.12 | tingido quente: rgba(60,45,38,.45) */
  backdrop-filter: blur(20px) saturate(140%);
  -webkit-backdrop-filter: blur(20px) saturate(140%);
  border: 1px solid rgba(255,255,255,.14);    /* aresta de luz */
  border-radius: 20px;                        /* cards 16–24px, sidebar flutuante 28px+ */
  box-shadow: 0 8px 32px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.12);
}
```
Versão completa (login com cantos chanfrados, botão neon, item ativo em pílula, fallback de
`prefers-reduced-transparency`) em `references/glassmorphism.md`.

## Anti-padrões
- Todos os KPIs com o mesmo peso e a mesma cor → escolha 1 principal (invertido ou maior).
- Várias cores de destaque competindo; gradiente roxo-azul genérico sem motivo de marca.
- Gráfico 100% saturado em todas as barras: as referências deixam o histórico neutro e destacam só o "agora".
- Glass sobre fundo chapado, blur > 40px, texto pequeno sobre vidro claro sem contraste (WCAG AA).
- Cards todos do mesmo tamanho num grid 3x3 — as referências usam grid assimétrico.
- Animação em tudo; nas referências anima-se troca de tema, item ativo, troca de página e o elemento-assunto
  (rota, gauge, contagem de números) — nunca loops decorativos permanentes.
- Esquecer estados: vazio, carregando (skeleton), erro, texto longo, "nenhum resultado". O card tracejado "Add another
  currency" do Vaulto é o estado vazio bem feito; ao usar biblioteca de componentes, teste os 4 estados (vem de `design-direction`).
- Mockup com dado impossível (Delivered > Shipments, "Win Rate 543", "Age 5", "24/38" sem alerta): a leva das rodadas 2–7
  está cheia deles; revise antes de mostrar.
- Em app financeiro: variação só por cor (sem +/−), Buy maior que Sell, card de IA com parágrafo genérico sem veredito,
  ticker/total errado no mockup (os cases mostram "APPL" e botão "$43" com subtotal "$26").

## Workflow
1. Defina domínio e a **pergunta principal** do painel (ex.: "quais casos vencem primeiro?" → ordenar por prazo, não por data, como na saúde).
2. Escolha a referência mais próxima pela tabela de `references/visual-index.md` e leia o trecho dela em
   `references/domain-examples.md`.
3. Escolha estrutura (rail + top nav ou sidebar larga) e tema (claro / escuro / glass) — `references/layout-patterns.md`.
4. Defina tokens: fundo, superfície, borda, texto 1/2/3, **uma** cor de destaque, verde/vermelho/âmbar semânticos.
5. Monte: header → faixa de KPIs → gráfico principal + coluna lateral → tabela/lista → card de insight.
6. Cores e marcas de gráfico: carregue a skill **`dataviz`** antes de escrever o código dos gráficos.
7. Revise contra os anti-padrões acima e, para AI slop em dashboards, contra **`ux-patterns`** (do projeto).
   Para acabamento visual geral use **`ext-impeccable`** (audit/polish) e **`ext-taste-skill`** (anti-slop).

## Quando abrir as imagens
Cada imagem custa contexto. Não abra todas: escolha 1–2 pela coluna "quando abrir" do índice.
Cada folha tem 12 quadros em ordem cronológica (4 colunas x 3 linhas), cobrindo o vídeo inteiro: dá para ver
várias telas do mesmo produto e os estados intermediários das animações. Nos reels de @_code_and_chill_ e @code.xr
cada quadro traz a UI em cima e um snippet de código embaixo; nos de @felvrabr são close-ups da UI num tablet.

Atalhos: dashboard escuro completo e bem hierarquizado → `DfV39ohhwAC`; claro minimalista com KPI invertido e
troca de tema → `De12lc1vUmr`; home pessoal + kanban + settings → `Deoi1WhP83h`; funil/coorte → `DffBnb2vlUn`;
fintech pessoal → `DfkNvnePItL`; IoT/mídia → `DfrqAX9v59S`; glass sobre foto → `DfKPFDwz2aA` / `DfHrMboTVDZ`;
sidebar recolhível → `DfMH6YTTcwx`; login glass → `DeoGCPlzKOs`; **gamificação / mapa operacional com
ação → estado → `Dfui4V5BMbz`** (variações `DfpCOjIB1Rb` solar, `Dfr9S5yhlvX` reservas com Gantt e meta de ocupação);
campanhas de mídia → `DfXoXVFPBfd`; e-commerce → `Dfct0mNvg3f`; CRM de serviços quente → `DfeT74YvQaD`;
glass claro sobre foto → `Dfj_FGsTAVB`; **app de trading / investimento → `DXeeUP7FKGs_1`** (Borea AI:
`DSIMwtvDluO_1` score mobile, `_2` home web com Gainers/Losers, `_3` chip de ticker e gráfico com cursor).
**Fintech web → `DfcdrhgFFMR_1`/`_2`**; logística/status → ação → `DftsSH-jnfs_1`; score de crédito → `DfaQe-CiBfJ_1`/`_2`;
saúde escura → `DfUvP_ulPC6_2`; perfil de atleta claro → `Dfus5sWFAov_1`; saúde clara → `DfUWa0jAed7_1`; recorte 3D de
apresentação → `DfcdrhgFFMR_3`. Fitness, finanças pessoais, Zentra e Caféra só têm descrição (§22b, §28–29).
Os reels da rodada 3 sem imagem (vendas com meta, crédito privado, skeuomorfismo, Ember, fluxos @ui.pixel) estão só
descritos em `domain-examples.md` §14–21.

## Arquivos
- `references/visual-index.md` — tabela das 18 folhas + 4 prints da rodada 3 + 9 prints da rodada 2 (autor, URL, domínio, estilo, quando abrir)
  e **"Perfis avaliados"** (quais contas valem como fonte, nota 1–5, inclusive inativas/inexistentes).
- `references/domain-examples.md` — descrição de cada dashboard e o que copiar dele (§14–21: rodada 3 — verificação,
  vendas com meta, crédito privado, skeuomorfismo, sidebar curva, Ember coral, trading/Borea, fluxos de app @ui.pixel;
  §22–29: fintech Orbix, CreditPros, Deuce, logística, MediCore, Code & Chill no Facebook, Caféra/Verdan/Maren em carrossel,
  apps fitness e finanças pessoais).
- `references/layout-patterns.md` — estruturas, KPI cards, gráficos, densidade, animações com código e
  §7 padrões de gamificação (gestor vs. cliente), §8 momento de decisão / card de ticker (investimento), §9 fluxos de
  pedido em etapas, §10 dashboard fintech web e apps de score.
- `references/glassmorphism.md` — receita CSS completa da série glass.

## Skills externas (dependências)
Esta skill pode delegar para: `ext-taste-skill`, `ext-impeccable`. Elas **não** fazem parte da repo; são instaladas por `scripts/install-external-skills.sh`.
1. Antes de delegar, confira se a pasta existe em `.claude/skills/<nome>/` ou `~/.claude/skills/<nome>/`.
2. Se faltar, **pergunte ao usuário** antes de instalar e, com o ok, rode `./scripts/install-external-skills.sh` (ou `--global`). Depois da instalação, o Claude Code normalmente já enxerga as skills novas; se alguma não aparecer, leia o `SKILL.md` instalado com Read e siga as instruções dele.
3. Se o usuário não quiser instalar, siga sem elas usando as references desta skill.

