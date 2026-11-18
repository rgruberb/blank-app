---
name: dashboard-ui
description: Galeria de referências e padrões visuais para dashboards e web apps (vendas de varejo, e-commerce, kanban, seguros marítimos, analytics SaaS, campanhas de anúncio, CRM de estúdio, orçamento familiar, smart home, saúde, e "OS" operacionais sobre foto aérea — fazenda, usina solar, resort) e para a série glassmorphism (login, dashboards V7/V8/V30, sidebar V5), destilados de 18 reels com folhas de contato em assets/visual-refs, mais padrões de gamificação (progresso, metas, checklist, níveis, ranking) para painel de gestor e de cliente. Use ao "criar dashboard", "painel admin", "tela de analytics", "glassmorphism", "admin panel", "KPI cards", "sidebar de app", "kanban", "tela de login com vidro", "gamificação", "dashboard gamificado", "painel do gestor/cliente com metas" ou ao revisar a hierarquia, a paleta e a densidade de um painel existente.
---

# dashboard-ui

Padrões de layout, KPI, gráficos, paleta e glassmorphism para dashboards, tirados de referências reais
(@_code_and_chill_, @ui.iliasmiah000, @code.xr, @felvrabr). As imagens estão em `assets/visual-refs/<ID>.jpg`;
o índice com autor, URL e quando abrir cada uma está em `references/visual-index.md`.

## Quando usar
- Montar do zero um dashboard, painel admin, tela de analytics, kanban ou portal B2B.
- Escolher entre tema escuro, claro ou glass para um app de dados.
- Fazer cards, sidebar ou formulário de login em glassmorphism.
- Prototipar um painel **gamificado** (progresso, metas, níveis, ranking) para gestor e/ou cliente —
  `references/layout-patterns.md` §7.
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
- Esquecer estados: vazio, carregando (skeleton), "nenhum resultado" (complemento).

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
sidebar recolhível → `DfMH6YTTcwx`; login glass → `DeoGCPlzKOs`; **protótipo gamificado / mapa operacional com
ação → estado → `Dfui4V5BMbz`** (variações `DfpCOjIB1Rb` solar, `Dfr9S5yhlvX` reservas com Gantt e meta de ocupação);
campanhas de mídia → `DfXoXVFPBfd`; e-commerce → `Dfct0mNvg3f`; CRM de serviços quente → `DfeT74YvQaD`;
glass claro sobre foto → `Dfj_FGsTAVB`.

## Arquivos
- `references/visual-index.md` — tabela das 18 referências (autor, URL, domínio, estilo, quando abrir).
- `references/domain-examples.md` — descrição de cada dashboard e o que copiar dele.
- `references/layout-patterns.md` — estruturas, KPI cards, gráficos, densidade, animações com código e
  §7 padrões de gamificação (gestor vs. cliente).
- `references/glassmorphism.md` — receita CSS completa da série glass.

## Skills externas (dependências)
Esta skill pode delegar para: `ext-taste-skill`, `ext-impeccable`. Elas **não** fazem parte da repo; são instaladas por `scripts/install-external-skills.sh`.
1. Antes de delegar, confira se a pasta existe em `.claude/skills/<nome>/` ou `~/.claude/skills/<nome>/`.
2. Se faltar, **pergunte ao usuário** antes de instalar e, com o ok, rode `./scripts/install-external-skills.sh` (ou `--global`). Depois da instalação, o Claude Code normalmente já enxerga as skills novas; se alguma não aparecer, leia o `SKILL.md` instalado com Read e siga as instruções dele.
3. Se o usuário não quiser instalar, siga sem elas usando as references desta skill.

