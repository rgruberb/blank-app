# Padrões de app desktop

Cada padrão traz regras, números das fontes (com ID/autor) e o ponteiro para o arquivo da skill de tema que tem o
detalhe. Conhecimento geral (Apple HIG macOS, Fluent/Windows, WCAG, prática de mercado) está marcado
**(complemento)**. Não repete os textos longos das skills de tema: abra o ponteiro quando precisar do detalhe.

---

## 1. App shell

**Fontes:** `dashboard-ui` `layout-patterns.md` §1A/§1B, `SKILL.md` padrões 1–2 e 15; `DfMH6YTTcwx`, `DfKPFDwz2aA`,
`DfcdrhgFFMR_1`, `DftsSH-jnfs_1`.

```
┌────────┬─────────────────────────────────────────────────┬──────────┐
│ logo ▾ │ Título da página          [filtros] [7D|30D] [CTA]│          │
│ ⌕ ⌘K   │ subtítulo de contexto                           │ inspector│
│ MAIN   ├─────────────────────────────────────────────────┤ 320–400  │
│ ▣ item │ conteúdo (KPIs → gráfico 2/3 + coluna 1/3 →     │ (compl.) │
│ ○ item │ tabela / lista)                                 │          │
│ WORK…  │                                                 │          │
│ 👤 user│                                                 │          │
└────────┴─────────────────────────────────────────────────┴──────────┘
 220–260px (rail 56–64px recolhido)
```
- **Sidebar larga 220–260px** ou **rail 56–64px**. Na sidebar: logo + workspace (+ botão recolher), busca com `⌘K`,
  grupos rotulados em caps pequenas cinza, ícone 16–18px + label + badge de contagem, card de usuário/tema no rodapé.
- **Colapso** (`DfMH6YTTcwx`, Glassy SideBar V5): rail com tooltip em cada ícone e badges; expande para a sidebar
  completa com sub-itens e linha-guia vertical. **(complemento)**: atalho `⌘\` / `Ctrl+\` (ou `⌘B`) para alternar,
  estado salvo por usuário, abaixo de 1024px recolhe sozinho.
- **Item ativo em pílula** que desliza entre itens (`ui-motion` `micro-interactions.md` §13; código `slidePill` em
  `layout-patterns.md` §6). A navegação fica nítida enquanto o conteúdo troca.
- **Topbar**: título grande + subtítulo de contexto; à direita filtros em pílula, segmented 7D/30D/90D e **um** CTA
  cheio. Barra de comando com atalho ("Search or type command ⌘ Space", Vaulto).
- **Ação mais comum fixa no topo** ("+ Create New Request", `DftsSH-jnfs_1`).
- **Coluna direita persistente** entre páginas, com números contando até o novo valor (CRM V8 `DfKPFDwz2aA`): bom
  para um monitor/watchlist ou para o inspector de detalhe.
- Larguras do inspector 320–400px, conteúdo mínimo ~640px entre sidebar e painel, painel vira overlay < 1440px
  **(complemento)**.

## 2. Navegação

**Fontes:** `dashboard-ui` padrões 1–2; `ux-patterns` `components-checklists.md` §4 e §7; `ux-laws.md` (Hick, Serial
position).
- Até ~7 itens de primeiro nível por grupo; o resto em grupos rotulados ou "More" (Hick: 12 → 4 itens, 0.74s → 0.46s,
  `ux-laws.md`).
- Top nav em pílulas para 3–6 seções irmãs (varejo `De12lc1vUmr`, ad campaign `DfXoXVFPBfd`); sidebar quando há
  hierarquia ou muitos módulos.
- **URL é estado** (complemento derivado da regra de paginação `?page=&sort=`): rota, filtros, aba e item aberto no
  inspector entram na URL, para refresh, compartilhar e back funcionarem.
- Breadcrumb em hierarquias com 3+ níveis; título da janela/aba = página atual + produto **(complemento)**.
- Back/forward do navegador (e ⌘[ / ⌘] no nativo) restauram scroll e seleção (`components-checklists.md` §4.6).

## 3. Tabela de dados

**Fontes:** `ux-patterns` `components-checklists.md` §4 (`DdtzWoMhLtW`), `perceived-performance.md` itens 04, 05, 23,
24; `dashboard-ui` padrões 11 e 16, `domain-examples.md` §25 e §26 (tabelas com chips).
- **Ordenação**: clique no cabeçalho alterna asc/desc com seta visível; ordem padrão = a pergunta da tela (saúde
  ordena por prazo, não por data — `dashboard-ui` Workflow §1). Ordenação na URL (`?sort=price`).
- **Filtros**: em pílula acima da tabela com **um** estado ativo cheio (`components-checklists.md` §11); filtros
  ativos sempre visíveis como chips removíveis + "Limpar" **(complemento)**; busca com **debounce** (item 04).
- **Paginação vs virtualização**:
  - Paginação quando a pessoa precisa de posição e referência ("Page 3 of 48 · 1,187 results"), compartilhar link ou
    voltar à mesma linha. Reserve a altura (sem shift de 68px) e diga "End of results".
  - "Load more, then stop" quando o footer precisa ficar alcançável.
  - **Virtualização** ("só desenha o que aparece", item 23) para listas longas na mesma página: log, feed de eventos,
    grade de milhares de linhas. Peça só as colunas necessárias (item 24) e pagine a API (item 05).
  - **(complemento)**: virtualizar a partir de ~500–1.000 linhas no DOM; com virtualização, mantenha contagem total,
    `Ctrl+F` deixa de achar linhas fora da tela — ofereça busca própria.
- **Célula**: dígitos tabulares, números à direita, texto à esquerda, status em chip com **texto** (Stable /
  Monitoring), delta com sinal e cor pelo sentido bom/ruim (`dashboard-ui` padrão 16; contraexemplo MediCore
  `DfUWa0jAed7_1` com alerta subindo em verde).
- **(complemento)**: cabeçalho fixo e 1ª coluna fixa em tabelas largas; scroll horizontal só dentro da tabela;
  colunas redimensionáveis e ocultáveis com preferência salva; densidade compacta 32–36px / confortável 44–48px;
  linha inteira clicável abre o inspector, ações da linha em `⋯` + hover; edição inline com `Enter` salva, `Esc`
  cancela; seleção por checkbox com barra de ações em massa.
- **Estados**: skeleton das linhas na carga, "nenhum resultado" com o filtro que causou e botão de limpar, erro com
  retry na própria tabela.

## 4. Formulários longos

**Fontes:** `ux-patterns` `ux-laws.md` (Proximity, Tesler, Postel, Chunking, Goal gradient) e
`components-checklists.md` §1–2; `dashboard-ui` `layout-patterns.md` §1D (detalhe com stepper).
- Label a **8px** do campo e **24px** do próximo (Proximity, `Dd25eCoBJGr`).
- Sistema preenche o que sabe (endereço 31 → 16 teclas); aceita qualquer formato e normaliza (Postel).
- Agrupe em seções nomeadas; formulário muito longo vira etapas com stepper e progresso que não começa do zero.
- Página de detalhe: título da entidade + metadados → stepper → grid de 3 colunas (rótulo 11px cinza, valor
  13–14px) → card lateral com o número que importa (`layout-patterns.md` §1D).
- Botão: verbo + objeto, **um** primário, loading que mantém a largura e ignora o 2º clique, disabled diz o porquê.
- **(complemento)**: em desktop, 1 coluna para dados sequenciais e 2 colunas só para pares curtos (cidade/UF);
  largura de campo proporcional ao conteúdo esperado; `max-width` ~640–720px para o bloco; barra de ações fixa no
  rodapé ou no topo em telas longas; `⌘/Ctrl+Enter` envia, `⌘/Ctrl+S` salva; aviso ao sair com alterações não salvas;
  autosave com "Saved" visível.

## 5. Settings / Preferências

**Fontes:** `ux-patterns` `components-checklists.md` §3 (`DdRneVWhBSY`).
- Confirmar o save (estado "Saved" na linha ou save explícito com linhas "dirty").
- **Escopo em cada linha** (pessoal, workspace, todos) — o erro mais caro.
- Busca + seções reais + link direto para cada linha; uma linha de consequência sob o label.
- Marcar o que não é default e oferecer reset por linha; dizer antes quando vale (agora, próximo login, restart).
- **(complemento)**: layout desktop em 2 colunas (lista de seções à esquerda ~200–240px, conteúdo à direita); no Mac
  nativo abre em janela própria com `⌘,` e aplica na hora; no Windows a convenção é página "Settings" dentro do app.

## 6. Command palette (⌘K)

**Fontes:** `ux-patterns` `components-checklists.md` §6 (`DeUr5-AhdvQ`); barra de comando do Vaulto (`domain-examples.md`
§22a, "⌘ Space", "⌘D Ask AI").
- Input é o maior elemento: **44 → 68px**, texto **26px**, detalhes **14px**.
- **3 grupos** (Actions, Pages, Recent) com ícone por tipo; letras digitadas destacadas.
- Painel elevado, **1º resultado pré-selecionado**; atalho na linha (`⌘N`) e `↑↓ ↵ esc` no footer.
- Abre em **150ms**, refiltra a cada tecla, Enter mostra spinner e abre.
- **(complemento)**: `⌘K` no Mac e `Ctrl+K` no Windows/Linux; abre de qualquer tela, inclusive com foco num input;
  busca fuzzy por nome e sinônimo; ações contextuais da tela atual no topo; mesma palette lista os atalhos.

## 7. Painéis divididos (split view, master-detail)

**Fontes:** `dashboard-ui` `layout-patterns.md` §1 (lista de funis à esquerda + detalhe, SaaS `DffBnb2vlUn`), §1E
(coluna Overview à direita), V8 `DfKPFDwz2aA`; `ui-motion` `micro-interactions.md` §12 (painel que cresce e escurece o
resto, `De1j52PFdpL`).
- Lista à esquerda, detalhe no centro ou à direita; a seleção da lista fica marcada e sobrevive ao refresh (URL).
- Foco num gráfico/painel: cresce com spring e o resto escurece; volta ao grid (`De1j52PFdpL`).
- **(complemento)**: divisores arrastáveis com largura mínima por painel (lista ≥ 240px, detalhe ≥ 480px), duplo
  clique no divisor volta ao padrão, tamanhos salvos; painéis recolhíveis por atalho; setas ↑↓ trocam o item da lista
  sem sair do detalhe.

## 8. Notificações e toasts

**Fontes:** `ui-motion` `micro-interactions.md` §9 (`DXRpZTTMr9a`), `css-recipes.md` §9; `ux-patterns`
`components-checklists.md` §8; `dashboard-ui` `layout-patterns.md` §6 ("ação → estado no objeto", ilha de estado).
- Desktop: **canto inferior direito**, nunca centralizado. Info **4s**, warning **7s**, erro **até reconhecer**.
- Máx. **3 visíveis**, novos empurram com spring damping 20 / stiffness 180; o anterior recua a 92%.
- Sempre dispensável, **pausa no hover**; ícone + borda esquerda colorida por tipo (não só fundo tingido).
- Quando a ação muda algo visível, prefira **mudar o estado no próprio objeto** ("✓ Irrigating · 40 min") em vez de
  toast (`layout-patterns.md` §6, série @felvrabr).
- Modo ativo global (foco, gravação, sync) → **ilha de estado** fixa no topo (tasks `Deoi1WhP83h`).
- **(complemento)**: toast de ação destrutiva com "Desfazer" em vez de diálogo de confirmação; centro de notificações
  com badge para o que precisa de histórico; em app nativo, notificação do SO só para eventos com a janela fora de
  foco e com opção de desligar; `aria-live="polite"` para toasts.

## 9. Estados vazio, carregando e erro

**Fontes:** `dashboard-ui` anti-padrões e padrão 14 (card tracejado "Add another currency", `DfcdrhgFFMR_2`);
`ux-patterns` `components-checklists.md` §11 e `perceived-performance.md`; `ui-motion` `loaders-and-refresh.md`.
- **Vazio** que convida: card tracejado "adicionar" no fim da fileira; nunca abrir a home com estado vazio na 1ª dobra
  (`components-checklists.md` §11).
- **Carregando**: skeleton para conteúdo estruturado; barra/anel com % quando o progresso é conhecido; spinner só
  para espera curta (< 3s); loader dentro do botão para ação do usuário (`loaders-and-refresh.md`). Feedback em até
  **400ms** (Doherty); título no primeiro paint.
- **Erro**: no lugar do conteúdo que falhou, com retry inline e o resto da tela funcionando (upload retoma de 90%,
  `micro-interactions.md` §10).
- Teste os 4 estados (vazio, carregando, erro, texto longo) antes de adotar qualquer componente pronto (`ui-motion`
  `react-bits.md`, @griffinwooldridge1).
- **(complemento)**: offline/reconectando como faixa discreta no topo; erro de permissão diz quem pode liberar.

## 10. Onboarding

**Fontes:** `ux-patterns` `ux-laws.md` (Goal gradient, Peak-end), `components-checklists.md` §11; `dashboard-ui`
Vaulto (card de onboarding no rodapé da sidebar, `layout-patterns.md` §10), home com saudação + resumo do dia
(padrão 2), card de IA com frase acionável (`layout-patterns.md` §5).
- Progresso nunca começa do zero; checklist segmentado "3/4" (padrão 10 de `dashboard-ui`).
- Card de onboarding ou upgrade no rodapé da sidebar, não modal bloqueante.
- Home com saudação + **resumo acionável** ("23 cases need attention today"), não "Welcome back 👋" genérico
  (`dark-patterns.md` §B).
- **(complemento)**: dados de exemplo em vez de tela vazia; dicas contextuais ancoradas no elemento, dispensáveis e
  que não voltam; apresentar ⌘K e 2–3 atalhos depois da primeira tarefa concluída, não antes.

## 11. Multi-janela e app nativo (Electron/Tauri)

**Fontes:** nenhuma das skills de tema cobre janelas; tudo aqui é **(complemento)** com base em Apple HIG macOS e
Fluent/Windows.
- **Janela**: tamanho mínimo ~1024×640; lembrar tamanho, posição e monitor; reabrir no estado anterior; suportar
  tela cheia e Split View (Mac) / Snap Layouts (Windows) sem quebrar o layout.
- **Barra de título customizada**: reservar a área dos botões de janela (semáforo à esquerda no Mac, ~78px; controles
  à direita no Windows, ~138px), região arrastável (`-webkit-app-region: drag`) fora de botões e inputs, duplo clique
  maximiza.
- **Menus**: Mac com menu global (App, File, Edit, View, Window, Help) e atalhos padrão (⌘Q, ⌘W, ⌘,, ⌘Z/⇧⌘Z); Windows
  com Ctrl e Alt para menus, Ctrl+Y para refazer, F11 tela cheia.
- **Multi-janela**: abrir item em nova janela (⌘/Ctrl+clique ou menu de contexto), estado sincronizado entre janelas,
  ⌘+crase para alternar janelas no Mac; aba-por-documento quando o app edita arquivos.
- **Integração com o SO**: tema claro/escuro e acento do sistema, `prefers-reduced-motion`, notificações nativas,
  arrastar arquivos do Finder/Explorer para a janela (mesmas regras de drop zone de `ui-motion`
  `micro-interactions.md` §10), atalhos globais só com opt-in.
- **Performance**: janela já aparece com o shell (sem flash branco — cor de fundo da janela = cor do tema), conteúdo
  com skeleton; sem bundle gigante na 1ª janela (code splitting, item 22 de `perceived-performance.md`).
- **Web no navegador**: não dependa de clique direito nem de atalhos que o navegador captura; ofereça PWA instalável
  só se houver uso diário **(complemento)**.
