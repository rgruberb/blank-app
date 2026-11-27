---
name: desktop-app-ui
description: 'UI/UX específica de app desktop — tela grande, mouse e teclado: web apps SaaS, dashboards, painel admin, CRM e sistemas internos no navegador do desktop, e apps nativos/Electron/Tauri para macOS e Windows. Traz app shell (sidebar, topbar, conteúdo, painel lateral) com larguras e colapso, densidade (escala 1,2), tabela de dados, hover/foco/estados, atalhos e ⌘K, breakpoints de app 1024/1280/1440/1920, breakpoints Material 3 (compact→extra-large) e navigation rail, tabela e dashboard pelo NN/g, métricas CASTLE, menu de contexto, drag-and-drop, multi-seleção, convenções macOS vs Windows, motion contido e acento só em alerta e ação, apontando para as references e imagens de dashboard-ui, ux-patterns, ui-motion e design-direction. Use quando falarem em "app desktop", "web app", "SaaS", "painel admin", "sistema interno", "back-office", "Electron", "Tauri", "app para Mac/Windows", "tela com sidebar", "atalhos de teclado", "tabela de dados", "data grid", "split view" ou "menu de contexto".'
---

# desktop-app-ui

Skill de **plataforma**: o que muda quando a interface é usada horas por dia, em tela ≥ 1024px, com mouse, trackpad e
teclado. As skills de **tema** continuam sendo a base (`dashboard-ui`, `ux-patterns`, `ui-motion`, `design-direction`);
aqui ficam só as regras específicas de desktop e os ponteiros para o resto. Não copie conteúdo delas: abra o arquivo
indicado na tabela "Onde está o resto".

## Escopo e fronteiras
- **Entra:** web apps SaaS, dashboards, admin, CRM, ERP, ferramentas internas e back-office usados no navegador do
  desktop; apps nativos ou Electron/Tauri para macOS e Windows; editores e ferramentas de produtividade.
- **Não entra:** site de marketing, landing page, portfólio e blog → **`website-ui`**. App de celular (iOS/Android,
  PWA mobile) → **`mobile-app-ui`**. Se o mesmo produto tem as três frentes, use a skill de cada superfície.
- Regra de origem: números com autor/ID vêm das fontes das skills de tema; Material 3, Carbon e NN/g lidos nas páginas
  oficiais (pesquisa 9A/9B, nov/2026) vêm com a fonte citada; o que for conhecimento geral (Apple HIG macOS,
  Fluent/Windows, WCAG, prática de mercado) está marcado **(complemento)**.

## Prioridade entre skills (quando as regras conflitam)

Ordem completa, da mais forte para a mais fraca: **skill de app específico** (ex.: `projetos/marca-pessoal-app/`, copiada para `.claude/skills/` na repo do app) > **skill de SEGMENTO** (`segmento-financeiro`, `segmento-crm`, `segmento-publicidade`, `segmento-marca-pessoal`, `segmento-saude`, `segmento-juridico`) > **plataforma** (`website-ui`, `desktop-app-ui`, `mobile-app-ui`) > **tema** (`design-direction`, `ui-motion`, `ux-patterns`, `dashboard-ui`) > **terceiros** (`ext-*`).
Se o projeto é de um setor, abra primeiro a skill `segmento-*` correspondente.

1. **Valores e decisões de design** (números, quantidade de animação, cor, sombra, tipografia) vêm das **skills do projeto** (app específico → segmento → plataforma → tema, nessa ordem): `website-ui`, `desktop-app-ui`, `mobile-app-ui`, `design-direction`, `ui-motion`, `ux-patterns`, `dashboard-ui`.
2. **Skills de terceiros** (`design-taste-frontend`, `impeccable`, `transitions-*`, `gsap-*`, `playwright-cli`, `extract-design`) servem para **implementação**: código pronto, APIs, checkers e verificação no browser. Use o código delas, mas com os valores do item 1. Vale o mesmo para qualquer skill de terceiros instalada depois (ex.: `expo/skills`, ECC `motion-*`/`frontend-*`, `karpathy-guidelines`, `mattpocock/skills`). Regras de **código** de terceiros ("mínimo que resolve", "sem feature não pedida", mudança cirúrgica) valem para a estrutura do código; os estados (vazio, carregando, erro), a acessibilidade e o `prefers-reduced-motion` que as skills do projeto exigem **fazem parte do pedido de UI**, não são feature extra.
3. Se o checker ou a regra de uma skill de terceiros reprovar algo que segue o item 1, **siga o item 1** e diga ao usuário qual regra externa foi ignorada e por quê.
4. Na plataforma, vale a skill da plataforma (`website-ui`, `desktop-app-ui` ou `mobile-app-ui`); nos temas, vale a skill de tema que ela indicar. A skill de segmento ou de app específico só sobrepõe o que ela disser explicitamente (paleta do setor, tom, compliance, telas obrigatórias); no resto valem plataforma e tema.

| Conflito | Vale | Em vez de |
|---|---|---|
| **Quantidade de animação** | **1 momento animado por página**: a entrada do hero **ou** um momento no CTA/seção, nunca os dois. Página longa também fica com 1. Micro-feedback funcional (press, hover, foco, sucesso) não conta | `design-taste-frontend`: entrada do hero + 1 momento por página (2 em página longa) |
| **Durações** | Os tokens de `ui-motion`: press **160 ms** (feedback em 0 ms), stagger **70–100 ms**, expandir card/abrir painel **350 ms**, sucesso **470 ms**, reveal **≤ 700 ms**. Onde `ui-motion` não tem número, use o token de `transitions-dev` (micro 80 ms, quick 150 ms, fast 250 ms) | `transitions-dev`: stagger 40 ms, panel open 400 ms, success check 500 ms |
| **Sombras** | Seções e blocos se separam por **espaço ou mudança de fundo**, sem sombra (as duas fontes concordam). **Sombra tingida** (cor do fundo, blur = 2× Y, ~8%) **só em elementos que flutuam**: dropdown, popover, modal, card arrastável, toast | `design-taste-frontend` sem sombras em nada; e sombra preta genérica |
| **Motion em app nativo/RN** | Os mesmos tokens de `ui-motion` (press **0,95 em 160 ms**, painel **350 ms**, sucesso **470 ms**); `expo-animation` e ECC `motion-*` entram só com a implementação (Reanimated na thread de UI, springs, haptics) | `expo-animation`: press 0,97 em 100–150 ms e tudo < 300 ms; ECC `motion-foundations`: fast 180 / normal 350 / slow 600 ms |
| **Stack de app mobile** | A escolha sai do passo 1 do workflow de `mobile-app-ui` e da skill de app específico (ex.: `marca-pessoal-app` proíbe React Native). `expo/skills` só se aplica depois de o projeto ser Expo/RN; não migre um web app para Expo por iniciativa própria | `expo-web-to-native`: "transformar site em app" = migrar para Expo/RN |
| **Violeta/lilás** | Permitido quando vem da marca, do segmento (lilás Linktree em `segmento-marca-pessoal`, roxo Attio/Pipedrive em `segmento-crm`) ou de paleta escolhida em `design-direction`; nunca como cor padrão sem motivo nem em gradiente roxo→azul (`ux-patterns` `dark-patterns.md`) | `design-taste-frontend`: nunca violeta ou lilás na página |

## Regras específicas de desktop

**1. App shell: navegação + topbar + conteúdo (+ painel lateral)**
- Duas variantes vistas nas referências (`dashboard-ui` `layout-patterns.md` §1A/§1B):
  - *Rail de ícones* **56–64px** + top nav em pílulas (varejo `De12lc1vUmr`, SaaS `DffBnb2vlUn`).
  - *Sidebar larga* **220–260px**: logo + workspace, busca com `⌘K`, grupos em caps pequenas, ícone 16–18px + label +
    badge, usuário no rodapé (saúde `DfV39ohhwAC`, Vaulto `DfcdrhgFFMR_1`).
- **Colapso**: sidebar larga ↔ rail com tooltip em cada ícone e badges preservados (`DfMH6YTTcwx`). Lembre a escolha
  do usuário entre sessões **(complemento)**.
- Topbar: título da página + subtítulo de contexto à esquerda; filtros, período e **um** CTA à direita; busca/comando
  com atalho visível ("Search or type command ⌘ Space" no Vaulto).
- Painel lateral de detalhe (inspector/drawer) à direita, **320–400px** **(complemento)**; coluna direita fixa que
  persiste entre páginas aparece no CRM V8 `DfKPFDwz2aA`.
- A ação mais comum fica fixa no topo ("+ Create New Request", logística `DftsSH-jnfs_1`).
- **Navigation rail (Material 3, 9A)** é o equivalente oficial do rail de ícones: a barra inferior do celular **vira
  rail** a partir de 600dp e **rail expandida** (≈ sidebar) a partir de 840dp. Troque só componentes equivalentes
  (bar ↔ rail ↔ sidebar; bottom sheet ↔ menu; nunca botão ↔ chip). Apple faz o mesmo por size class: tab bar → sidebar
  no espaço regular.

**2. Breakpoints de app (complemento)**
- **1024** mínimo útil: sidebar vira rail, painel lateral vira overlay. **1280** padrão de notebook: sidebar larga +
  conteúdo. **1440** cabe painel lateral fixo. **1920+**: limite a largura de texto e formulários (`max-width` por
  bloco, linha de 45–75 caracteres de `ux-patterns`), deixe tabelas e gráficos crescerem.
- Abaixo de 1024 não é desktop: aplique `mobile-app-ui` ou uma visão reduzida, sem espremer a tabela.
- **Mapeamento com os breakpoints do Material 3 (9A, largura da janela em dp ≈ px CSS — equivalência é inferência):**

| Material 3 | Faixa | Navegação M3 | Painéis M3 | Nesta skill |
|---|---|---|---|---|
| compact | < 600 | navigation bar inferior | 1 | não é desktop → `mobile-app-ui` |
| medium | 600–839 | bar ou rail | 1 (2 só se pouco denso) | tablet / janela estreita → `mobile-app-ui` + alvos daqui |
| expanded | 840–1199 | rail expandida | 1–2 (recom. 2) | **1024** cai aqui: rail, painel lateral em overlay |
| large | 1200–1599 | rail expandida/sidebar | 1–2 (recom. 2) | **1280** e **1440**: sidebar larga; painel fixo a partir de 1440 |
| extra-large | ≥ 1600 | sidebar | 1–3 | **1920**: até 3 painéis; limitar texto e formulários |

  **Divergência registrada:** o Material corta em 840 e 1200, esta skill em 1024 e 1280. Mantenha **1024/1280/1440/1920**
  como pontos de **teste** (larguras reais de notebook/monitor) e use os cortes do Material para decidir **quantos
  painéis e qual navegação**: entre 840 e 1023 a janela já é "expanded" — não quebre para layout de celular, use rail
  + 1 painel. Linha de texto: Material pede **40–60 caracteres**; regra das skills: 45–75 no texto corrido e **45–60
  em formulários**, token `--measure: 50ch` (`ux-patterns` `typography-and-touch.md` §2b).

**3. Densidade**
- Escala tipográfica **16 × 1,2^n** (16, 19, 23, 28, 33, 40, 48) para produto denso; 1,25 fica para site/editorial
  (`ux-patterns` `typography-and-touch.md` §2). Labels e células podem usar **13–14px** **(complemento)**.
- Painel operacional: padding de card **16–20px**, gap **12–16px**, 5 KPIs + 2 gráficos + tabela na 1ª dobra;
  executivo: padding ~24px (`dashboard-ui` `layout-patterns.md` §4). Espaçamento na grade de 8, 4 só em micro.
- Ofereça densidade *compacta/confortável* em tabelas e listas **(complemento)**.
- Alvo com mouse: piso WCAG **24px**, meta **44px** para ações principais (`typography-and-touch.md` §1); ícones de
  toolbar crescem por padding (20 + 12 + 12).

**4. Tabelas e listas grandes**
- Cabeçalho fixo, dígitos tabulares e números alinhados à direita, chips de status com texto e não só cor
  **(complemento)**. Altura de linha 32–36px compacta / 44–48px confortável **(complemento)**.
- Paginação contada ("Page 3 of 48 · 1,187 results"), estado em `?page=&sort=` e back que restaura scroll e linha
  (`ux-patterns` `components-checklists.md` §4). Acima de alguns milhares de linhas: **virtualização** (item 23 de
  `perceived-performance.md`). Detalhes e escolha paginação × virtualização em `references/desktop-patterns.md` §3.

- **NN/g, Data Tables (9B):** tabela vence cards para **comparar e escalar**; desenhe para as **4 tarefas**: achar
  registro, comparar, ver/editar linha, agir. **1ª coluna = identificador legível**; cabeçalho **e** 1ª coluna fixos;
  ocultar/reordenar colunas com estado visível; editar em **painel lateral não modal** (modal cobre as linhas
  vizinhas que a pessoa quer consultar — print `../ux-patterns/assets/visual-refs/9B_tabelas_painel-lateral-crm_1.jpg`); ações em lote com "selecionar
  todos" + barra contextual.

**5. Hover, foco e estados**
- Hover é sinal de clicável e lugar de ações secundárias da linha, **nunca o único caminho** para uma ação
  **(complemento)**. Tooltips em ícones sem label.
- **Focus ring sempre visível**, nunca `outline: none` (`components-checklists.md` §2); use `:focus-visible`
  **(complemento)**. Disabled explica o porquê.
- Todo componente com estados vazio, carregando (skeleton), erro, texto longo e "nenhum resultado"
  (`dashboard-ui`, anti-padrões).

**6. Teclado**
- **⌘K / Ctrl+K**: input 44 → **68px**, grupos Actions/Pages/Recent, letras destacadas, 1º resultado selecionado,
  atalho na linha, abre em **150ms** (`components-checklists.md` §6).
- Atalhos para experts nas ações frequentes, mostrados no tooltip e no menu ("clicks teach the keys") — `§6–7`.
- Tab order segue a ordem visual; `Esc` fecha o que estiver por cima; `Enter` confirma; setas navegam listas e
  menus; `?` abre a lista de atalhos **(complemento)**. Não roube atalhos do sistema/navegador (⌘W, ⌘T, Ctrl+F)
  **(complemento)**.

**7. Menus de contexto, drag-and-drop, multi-seleção**
- Clique direito replica ações que já existem em outro lugar (botão `⋯` na linha) **(complemento)**.
- Drag-and-drop: drop zone reage antes do drop (borda, glow, "Release to upload"), progresso honesto com % e tempo,
  fila independente, retry inline (`ui-motion` `micro-interactions.md` §10). Arraste que muda valor mostra o
  resultado em tempo real ("Drag to extend · 4 nights") (`components-checklists.md` §8). Sempre com alternativa por
  teclado/menu **(complemento)**.
- Multi-seleção: checkbox na linha, Shift+clique para intervalo, ⌘/Ctrl+clique para alternar, barra de ações em
  massa com contagem ("3 selected") e desfazer **(complemento)**.

**8. macOS vs Windows (complemento)**
- Modificador: ⌘ no Mac, Ctrl no Windows; mostre o símbolo certo por SO. Botões de janela: semáforo à esquerda no Mac,
  minimizar/maximizar/fechar à direita no Windows; em Electron/Tauri com barra customizada, reserve essa área e
  mantenha a região arrastável.
- Ordem de botões em diálogo: Mac = primário à direita; Windows = primário à esquerda do Cancelar. Menu do app na
  barra global (Mac) vs menu na janela/hambúrguer (Windows). Preferências: ⌘, no Mac; "Settings" no Windows.
- Respeite tema, acento e `prefers-reduced-motion` do SO; fontes do sistema (SF Pro / Segoe UI Variable) só se não
  houver fonte de marca (`ux-patterns` `dark-patterns.md` §C pede fonte do mundo do produto).

**9. Motion contido em tela aberta por horas**
- Anime troca de página, item ativo, troca de tema e o elemento-assunto; **nunca loops decorativos**
  (`dashboard-ui` anti-padrões). Pílula ativa que desliza **250–350ms** ease-out (`micro-interactions.md` §13).
- Latência do botão: resposta em **≤ 100ms** e estado final/spinner em **≤ 300ms** (prazo do sistema, não duração
  de animação); Doherty **< 400ms** (`ux-patterns` `components-checklists.md` §1).
- Web app e ferramenta de trabalho usam **os mesmos tokens e a mesma curva de `ui-motion`** do app mobile; onde
  `ui-motion` não tem número, micro = **80 ms** de `transitions-dev`. Carbon (9A) fica só como referência
  comparativa: productive por padrão, expressive raro, microinteração 90–120 ms, painel lateral que fica "por perto"
  usa curva standard, não exit (`../ui-motion/references/official-motion-guidelines.md`).
- Telas de trabalho repetitivo (tabela, formulário, settings): só feedback de estado, sem scroll reveal
  (`ui-motion` `scroll-and-screen-transitions.md` §2, complemento). Toasts: canto **inferior direito** no desktop,
  info 4s, warning 7s, erro até reconhecer, máx. 3, pausa no hover (`micro-interactions.md` §9).

**10. Cor: acento só para alerta e ação**
- Tela de sala de controle aberta por horas: dark + **um** acento para alertas, botões e pontos de status
  (logística `DftsSH-jnfs_1`, `dashboard-ui` padrão 15). Histórico neutro, acento no "agora" ou no que pede ação
  (padrão 11). Cor do delta pelo sentido bom/ruim, não pelo sinal (padrão 16).

**11. Dark mode**
- Web app de uso diário: os dois temas com seletor **Claro / Escuro / Sistema** (padrão = Sistema). App nativo/PWA
  segue o tema do sistema, sem seletor (`mobile-app-ui` §14). Sem `#000` (ex.: `#0C1424` ou `#0b0c0e`),
  texto a **87%**, accent clareado, elevação por luminosidade, borda 1px `rgba(255,255,255,.06)`
  (`typography-and-touch.md` §4).

**12. Performance percebida**
- Skeleton no lugar de tela vazia, optimistic UI, streaming de IA token a token, debounce na busca, virtualização,
  code splitting por rota (`ux-patterns` `perceived-performance.md`). Título no primeiro paint.
- Em Electron/Tauri: janela aparece já com o shell desenhado e o conteúdo entra depois; nunca janela branca
  **(complemento)**.

**13. Dashboards e abas (NN/g, 9B)**
- Defina se o painel é **operacional** (decisão imediata, uma tela) ou **analítico** (exploração).
- Valor por **comprimento (barras)** e **posição 2D (linhas, dispersão)**; **sem gauge, pizza, donut, treemap e 3D**
  em painel operacional de uso diário (anel de meta só fora dele, critério em `dashboard-ui` padrão 17) (print `../ux-patterns/assets/visual-refs/9B_dashboards_linha-e-barras_1.jpg`). Cor para **categoria**, não magnitude; nunca o único
  sinal (~8% dos homens têm daltonismo). Gráficos com a skill `dataviz`; padrões em `dashboard-ui`.
- Abas: separe **abas de navegação** de **abas internas** e não misture; 1 nível; rótulos de 1–2 palavras, sem caixa-alta;
  **≥ 2 indicadores** de seleção (linha + negrito/fundo); não selecionadas legíveis; mais usada primeiro; teclado e ARIA.
- Empty state em app complexo: diz o estado ("nenhum registro no período"), ensina a função, dá o botão da 1ª tarefa;
  **nunca "Sem registros" enquanto carrega** (corrói confiança).

**14. Medir: CASTLE, não HEART (NN/g, 9B)**
- Para ferramenta de trabalho (admin, CRM, painel do gestor) use **CASTLE**: **C**ognitive load (NASA-TLX), **A**dvanced
  feature usage (uso de atalhos, filtros salvos, ações em lote), **S**atisfaction (SEQ por tarefa), **T**ask efficiency
  (tempo na tarefa), **L**earnability (tempo até proficiência), **E**rrors (erros de validação, desfazer). HEART fica
  para o app de consumo. Cada dimensão → meta, sinal e medida; pareie com pesquisa qualitativa (métrica diz *se*, não *por quê*).
- Instrumente desde o início **(complemento)**: uso de ⌘K e atalhos (A), erros de validação por campo (E), tempo das
  3 tarefas principais (T).

**15. Padrões de painel e tabela da rodada 10A** (1 frame + legenda por post)
- Tabela de usuários com **alternância Table / Cards**, seleção por linha, chip de plano e barra de uso 30d
  (`DgAT3fVBJ8B`, print em `dashboard-ui`). **Linha expansível só se revelar algo novo** (crítica nos comentários do
  mesmo post) — complemento.
- Fluxo com agente: **o agente propõe com o ganho em número, a pessoa aprova uma vez no painel lateral, o sistema
  notifica** (Wayline `Df1WDAnhbtx`); **prévia do impacto antes de aprovar** (Threshold `DfxspuNBjye`); fila como KPI
  "X de Y prontos, N precisam de você" (Linden `DgH6J4mgMM4`). Detalhes: `dashboard-ui` → `layout-patterns.md` §12.
- Lista reordenável: alça que aparece no hover, cursor `grab`, linha erguida e espaço aberto (`DgM5twdsInO`; regra 7).
- Sidebar/tabs de vidro (@code.xr V15, V20): só sobre foto/conteúdo e com "Reduce transparency"
  (`dashboard-ui/references/glassmorphism.md`); em app aberto por horas, prefira superfície sólida (complemento).

## Checklist (desktop)
- [ ] Shell definido: rail 56–64 ou sidebar 220–260, colapso com tooltip, topbar com 1 CTA e busca/⌘K.
- [ ] Testado em 1024, 1280, 1440 e 1920; nada de scroll horizontal da página (só dentro da tabela).
- [ ] Uma escala tipográfica (1,2), espaçamento na grade de 8, densidade coerente com o uso.
- [ ] Tabela: cabeçalho fixo, total visível, estado na URL, back restaura posição, virtualização se precisar.
- [ ] Tudo alcançável por Tab, foco visível, `Esc` fecha, ⌘K funciona, atalhos aparecem no tooltip.
- [ ] Ações de hover e de clique direito também existem num botão visível.
- [ ] Vazio, carregando, erro, texto longo e "nenhum resultado" desenhados.
- [ ] Um acento; alertas com cor + ícone + texto; delta pelo sentido bom/ruim.
- [ ] Motion só funcional; `prefers-reduced-motion` respeitado; toasts no canto inferior direito.
- [ ] Dark e light revisados; contraste 4,5:1 texto, 3:1 bordas e ícones.
- [ ] Nativo: atalhos ⌘/Ctrl por SO, área dos botões de janela reservada, ordem de botões de diálogo do SO.
- [ ] Entre 840 e 1023px a tela ainda é "expanded": rail + 1 painel, sem cair para layout de celular.
- [ ] Tabela: 1ª coluna identificadora fixa, edição em painel lateral não modal, ações em lote.
- [ ] Gráficos de barras/linhas (sem gauge/pizza/donut no painel operacional); abas com 2 indicadores.
- [ ] Metas CASTLE definidas (tempo de tarefa, erros, uso de recursos avançados).

## Workflow
1. **Defina o uso**: quem abre, por quanto tempo, qual a pergunta principal da tela (`dashboard-ui` Workflow §1) e se
   é web no navegador ou nativo (Electron/Tauri, macOS/Windows).
2. **Escolha o shell e a densidade** pelas regras 1–3; abra **uma** imagem de `references/visual-index.md`.
3. **Desenhe os padrões da tela** com `references/desktop-patterns.md` (tabela, formulário, settings, ⌘K, split view,
   toasts, estados, onboarding, multi-janela).
4. **Tokens e paleta**: `design-direction` (2 base + 1 acento) e `dashboard-ui` "Paleta"; gráficos com a skill
   `dataviz`.
5. **Motion**: só o funcional, valores de `ui-motion`.
6. **Verifique** no navegador com `ext-playwright-cli` nos 4 breakpoints, navegando só por teclado; auditoria com
   `ux-patterns` (Workflow) e `design:accessibility-review`; polish com `ext-impeccable`.

## Onde está o resto
| Preciso de… | Abra |
|---|---|
| Esqueletos rail + top nav, sidebar larga, kanban, detalhe, Gantt | `../dashboard-ui/references/layout-patterns.md` §1 |
| KPI cards, gráficos, densidade, card de IA | `../dashboard-ui/references/layout-patterns.md` §2–5 |
| Movimento de dashboard (tema em círculo, pílula elástica, troca de página com blur) | `../dashboard-ui/references/layout-patterns.md` §6 |
| Paletas de painel escuro/claro/glass e anti-padrões | `../dashboard-ui/SKILL.md` "Paleta" e "Anti-padrões" |
| Exemplo por domínio (saúde, CRM, logística, fintech, RH) | `../dashboard-ui/references/domain-examples.md` §1–13, §21c, §22–26 |
| Glassmorphism (login, sidebar, cards) | `../dashboard-ui/references/glassmorphism.md` |
| Botão, settings, paginação, ⌘K, toolbar, tooltip de arraste | `../ux-patterns/references/components-checklists.md` §1–8 |
| Escala 1,2 vs 1,25, alvo 24/44, grade de 8, contraste, dark mode | `../ux-patterns/references/typography-and-touch.md` §1–6 |
| Leis (Fitts, Hick, Doherty, Proximity, Von Restorff, Tesler) | `../ux-patterns/references/ux-laws.md` |
| Dashboard com cara de IA e fonte genérica | `../ux-patterns/references/dark-patterns.md` §B–C |
| 31 itens de performance | `../ux-patterns/references/perceived-performance.md` |
| Toasts, drag/upload, pílula que desliza, foco em gráfico | `../ui-motion/references/micro-interactions.md` §9, §10, §12, §13 |
| Skeleton, loaders, progresso | `../ui-motion/references/loaders-and-refresh.md` |
| Onde motion não faz sentido; um momento animado por tela | `../ui-motion/references/scroll-and-screen-transitions.md` §2, §5 |
| Tokens CSS (toast stack, reorder, reduced-motion) | `../ui-motion/references/css-recipes.md` §0, §9–11 |
| Paleta 2 + 1, 60/30/10, rampa de tons, sombra tingida | `../design-direction/references/color-palettes.md`, `layers-and-trust-layout.md` §4 |
| Par tipográfico | `../design-direction/references/typography-pairing.md` |
| Padrões detalhados desta skill | `references/desktop-patterns.md` |
| Pesquisa NN/g completa (tabelas, dashboards, abas, empty state, CASTLE) | `../ux-patterns/references/nng-research.md` |
| Bibliotecas (shadcn, Radix, React Aria, Mantine, HeroUI…): critérios e recomendação condicionada ao stack | `references/component-libraries.md` |
| Onde buscar inspiração (Dribbble, Behance, kits Figma, shadcn blocks) e prints da pesquisa 9 | `references/benchmark-sources.md` |
| Quais imagens abrir | `references/visual-index.md` |

## Imagens
Esta skill **não tem imagens próprias**: o índice aponta para as das skills de tema. Cada uma custa contexto; abra
1–2 escolhidas pela coluna "quando abrir". Atalhos: shell com sidebar larga `DfV39ohhwAC`, rail + top nav
`De12lc1vUmr`, sidebar recolhível `DfMH6YTTcwx`, ⌘K `DeUr5-AhdvQ`, settings `DdRneVWhBSY`, paginação `DdtzWoMhLtW`,
toasts `DXRpZTTMr9a`.

## Skills externas (dependências)
Pode delegar para `ext-impeccable`, `ext-playwright-cli` e `ext-transitions-dev`. Elas **não** fazem parte da repo;
são instaladas por `scripts/install-external-skills.sh`. Confira se a pasta existe em `.claude/skills/<nome>/` ou
`~/.claude/skills/<nome>/`; se faltar, **pergunte ao usuário** antes de rodar o script. Sem elas, siga com as
references das skills de tema.
