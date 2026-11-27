# Componentes CRM

Origem: 10B §14 (CMP-CRM-01 a 09) e galeria 10C/C2/C4/10A (CMP-CRM-10 a 16). Nomes entre crases (`deal-card`) são
os nomes sugeridos nas fichas da galeria. **(inferência)** = regra desta skill, não da fonte.
Regras transversais: `tabular-nums` em valores, contagens e datas; status com texto + ícone + cor; foco visível e
ação por teclado em tudo; alvo mínimo 24px na web (44pt/48dp no mobile).

---

## CMP-CRM-01 — Tabela densa com visões salvas
- **Anatomia:** abas de visão salva (Todos / Favoritos / Novos / Atribuídos a mim) → barra de filtros (CMP-CRM-07) →
  ações da lista (Importar, Exportar, Adicionar) → tabela: checkbox, nome + e-mail, empresa, origem, pontuação, estado,
  criado em, responsável.
- **Estados:** linha hover, selecionada, multi-seleção com barra de ações em massa, editando inline, carregando, vazia.
- **Regras:** cabeçalho fixo e semântico; números à direita; linha 13–14px, com modo compacto opcional de 12px (piso); filtro e ordenação **persistem** ao navegar
  (inferência); ação em massa com desfazer. Detalhe em `desktop-app-ui/references/desktop-patterns.md` §3.
- **Plataformas:** desktop. **Referências:** `10C_CRM_dribbble-conceptzilla_crm-leads-tabela_1.jpg` (`list-tabs`,
  `list-actions`), `10A_DgAT3fVBJ8B_1.jpg` (tabela de usuários com plano, status, uso 30d);
  `ux-patterns` `9B_tabelas_painel-lateral-crm_1.jpg`.

## CMP-CRM-02 — Cartão de negócio
- **Anatomia:** etiquetas de cor (opcional, com texto acessível) → nome do negócio → empresa → avatar/iniciais do
  responsável → **valor** → botão circular de próxima ação/estado da atividade.
- **Estados:** normal, arrastando (lift), atrasado (ícone + texto), sem atividade agendada, ganho/perdido.
- **Regras:** valor com moeda e `tabular-nums`; prazo/data prevista visível (10B §14: valor, responsável, prazo);
  arrastar tem alternativa por menu/teclado (inferência).
- **Referências:** `10C_CRM_pipedrive_deals-kanban-app_1.jpg` (`deal-card`).

## CMP-CRM-03 — Coluna de pipeline com soma
- **Anatomia:** cabeçalho com nome da etapa + **soma dos valores** + **nº de negócios** → pilha de cartões → "+" para
  adicionar. Topo da tela: total do funil ("$51,300 · 10 deals") + seletor de funil.
- **Regras:** soma recalcula sem animação de contagem (inferência); cabeçalho em forma de seta mostra progressão
  (Pipedrive); colunas com a mesma largura; fade no fim indica rolagem.
- **Referências:** `10C_CRM_pipedrive_deals-kanban-app_1.jpg` (`stage-column`), `10C_CRM_rd-station-crm_home-funil-kanban_1.jpg`
  (`pipeline-kanban`); `dashboard-ui` §12 (pipeline de 4 colunas).

## CMP-CRM-04 — Linha do tempo do contato
- **Anatomia:** filtro por tipo (nota, e-mail, ligação, reunião, tarefa, alteração de campo) → itens em ordem
  cronológica com autor, data relativa + data completa no hover, conteúdo resumido e link para o original.
- **Regras:** inclui alterações de propriedade (quem/quando) para auditoria; entrada de consentimento LGPD com origem e
  texto (CMP-CRM-09). "Ver histórico de propriedade/associação" aparece no menu do card HubSpot.
- **Referências:** 10B §6 e §14; `10C_CRM_hubspot_home-card-contato_1.jpg` (`context-menu`).

## CMP-CRM-05 — Painel lateral de detalhes
- **Anatomia:** abre à direita sem cobrir a lista; cabeçalho com nome e ações; abas (Visão geral, Atividade, Negócios);
  campos editáveis; Cancelar/Salvar.
- **Regras:** não modal; Esc fecha; setas mudam de registro mantendo o painel aberto (inferência); 350 ms para abrir
  (`ui-motion`).
- **Referências:** `ux-patterns` `9B_tabelas_painel-lateral-crm_1.jpg`; `desktop-app-ui/references/desktop-patterns.md` §7.

## CMP-CRM-06 — Badge de etapa/estado
- **Anatomia:** ponto ou ícone + texto (Ativo, Trial · 9d left, Inativo, Convidado; To do, In progress, On review).
- **Regras:** nunca só cor; cores semânticas fixas (verde = ganho/ativo, vermelho = risco/perdido) e acento de marca
  fora dos estados (inferência).
- **Referências:** `10A_DgAT3fVBJ8B_1.jpg` (status), `10C_CRM_dribbble-ronas-it_bizlink-tarefas-mobile_1.jpg` (`status-tabs`).

## CMP-CRM-07 — Barra de filtros combináveis
- **Anatomia:** chips de filtro ativos (campo · operador · valor) com "×" → "+ Filtro" → ordenar → salvar como visão.
- **Regras:** filtros persistem e aparecem na URL (inferência); contagem de resultados ao lado ("248"); limpar tudo.
- **Referências:** `10C_CRM_dribbble-conceptzilla_…` (filtro e ordenar no cabeçalho); `10A_DfkL5N_H4GK` usa chips de filtro
  (ver `segmento-financeiro`).

## CMP-CRM-08 — Paleta de comandos
- **Anatomia:** ⌘K abre busca global + ações (criar negócio, ir para contato, registrar ligação); atalhos exibidos à direita.
- **Regras:** 6 decisões em `ux-patterns/references/components-checklists.md` §6; "Quick Actions ⌘K" na sidebar (Attio).
- **Referências:** `10C_CRM_attio_home-workspace-ia_1.jpg` (`quick-actions-bar`); Linear (10B).

## CMP-CRM-09 — Gerenciador de consentimento LGPD
- **Anatomia (no registro do contato):** finalidade → status (concedido/revogado) → **origem** (formulário, evento,
  importação) → **data** → **texto exato aceito** → ações: exportar dados, eliminar/anonimizar.
- **Na captura:** checkbox **desmarcado** para marketing, link para aviso de privacidade, campos opcionais marcados.
- **Regras:** LGPD arts. 6º, 8º, 9º, 18 (`regulacao.md`).
- **Referências:** 10B §9. Sem imagem própria.

## CMP-CRM-10 — Card de contato com ações rápidas
- **Anatomia:** avatar → nome → cargo e empresa → e-mail e telefone (com copiar) → linha de ações com ícone + rótulo:
  Nota, E-mail, Ligação, Tarefa, Reunião → menu "…" (seguir, ver propriedades, histórico, resumir com IA, exportar).
- **Regras:** rótulo sob cada ícone; telefone/e-mail acionáveis no mobile; "exportar" e "opt out" no menu servem à LGPD.
- **Referências:** `10C_CRM_hubspot_home-card-contato_1.jpg` (`contact-card`, `quick-actions`, `context-menu`).

## CMP-CRM-11 — Pontuação de lead
- **Anatomia:** barra segmentada compacta (0–10) + valor "7/10" em texto, ao lado da coluna de origem (Website, LinkedIn).
- **Regras:** número sempre visível; cor por faixa com texto (inferência); explicar o critério no hover.
- **Referências:** `10C_CRM_dribbble-conceptzilla_crm-leads-tabela_1.jpg` (`lead-score-bar`).

## CMP-CRM-12 — Caixa de IA (pergunta, resumo, checklist)
- **Anatomia:** saudação + campo de pergunta ("How do I win…") com modo e enviar; ou item "Resumir com IA" no menu; ou
  checklist pós-reunião (preencher CRM, enviar resumo, analisar concorrentes) com transcrição ao lado.
- **Regras:** IA cita a fonte (ligação, e-mail, atividade) e pede confirmação antes de gravar no registro (inferência;
  ver Wayline/Threshold em `fontes.md`: "o agente propõe, a pessoa aprova uma vez").
- **Referências:** `10C_CRM_attio_home-workspace-ia_1.jpg` (`ai-prompt-box`), `10C_CRM_hubspot_…` ("Summarize with AI"),
  `10C_CRM_rd-station-crm_…` (`ai-checklist`, `call-transcript`).

## CMP-CRM-13 — Trilho de integrações
- **Anatomia:** coluna vertical de ícones de canais (WhatsApp, Google Agenda, Meet/Zoom, Teams) ao lado do conteúdo.
- **Regras:** mostrar só integrações reais; estado conectado/desconectado em texto (inferência).
- **Referências:** `10C_CRM_rd-station-crm_home-funil-kanban_1.jpg` (`integration-rail`).

## CMP-CRM-14 — Cartão de tarefa (mobile)
- **Anatomia:** título → descrição curta → prazo → prioridade (chip) → avatares → barra de progresso com %.
  Acima: abas de status (To do / In progress / On review), ordenar, filtro "Me", intervalo de datas.
- **Regras:** tab bar flutuante em pílula com ativo destacado; métricas do dia (tarefas, atrasadas em vermelho com
  texto "+1 yesterday", tempo por tarefa, taxa de conclusão "39 of 50").
- **Plataformas:** mobile. **Referências:** `10C_CRM_dribbble-ronas-it_bizlink-tarefas-mobile_1.jpg` (`task-card`,
  `floating-tabbar`, `metric-card`); `mobile-app-ui` regras 3 e 11.

## CMP-CRM-15 — Alternância de visão
- **Anatomia:** segmented de ícones kanban / lista / gráfico (Pipedrive) ou Tabela / Cards (`10A_DgAT3fVBJ8B`).
- **Regras:** mesma seleção e filtros nas duas visões; lembrar a última escolha (inferência). Card hero com contador
  + fração ("2.184 · +8,2% vs Oct · 77% of 2.847 seats") acima da tabela.
- **Referências:** `10C_CRM_pipedrive_deals-kanban-app_1.jpg` (`view-switcher`), `10A_DgAT3fVBJ8B_1.jpg`.

## CMP-CRM-16 — Linha de confiança (site)
- **Anatomia:** 3 itens pequenos sob os CTAs: nota em plataforma de avaliação · "sem cartão de crédito" · conformidade
  (ex.: SOC 2 & GDPR). Variante: selo de prêmio ao lado do mock.
- **Regras:** só certificações que o produto tem; adapte à LGPD no Brasil (inferência).
- **Plataformas:** website. **Referências:** `10C_CRM_pipedrive_home-hero-confianca_1.jpg` (`trust-line`),
  `10C_CRM_hubspot_home-card-contato_1.jpg` (`award-badge`); `website-ui/references/website-patterns.md` §2.
