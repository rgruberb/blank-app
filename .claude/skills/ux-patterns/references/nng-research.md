# Pesquisa NN/g (Nielsen Norman Group): onboarding, navegação, formulários, dashboards, confiança e métricas

Fonte: rodada **9B** (22/11/2026), 17 artigos do nngroup.com abertos e lidos na íntegra. Diferente dos reels, aqui as regras vêm de **estudos de usabilidade**, mas vários são de **2015–2019**: confira a data na tabela do fim e reavalie com teste quando a plataforma mudou. Inferências nossas estão marcadas **(complemento)**.

---

## 1. Onboarding: evite o instrucional (`mobile-app-onboarding`, 2020)
- **Evite onboarding sempre que possível**: custa interação e memória, e tutoriais em deck de cards **não melhoraram o desempenho** em estudo do NN/g.
- **Prefira**: dicas **em contexto** (no momento em que a função fica útil), **empty states** que ensinam (§4) e interface mais aprendível.
- Onboarding só se justifica quando: o app **precisa de dados do usuário para começar**, é muito personalizado, ou o fluxo é realmente novo.
- Tipos: promoção de funções (evite no 1º uso; mostre quando a função fica acionável, ex.: após 7 dias de dados) · personalização (conteúdo sim; **tema/cores no onboarding não**) · instruções (breves, opcionais).
- Se usar deck: **"Skip" bem visível**, poucos cards, **um conceito por card**. Coach marks: no momento certo, discretos; walkthrough interativo com opção de pular.
- Explique por que pede cada dado; mostre progresso; permita pular.

## 2. Navegação e tabs
**Tab bar mobile** (`mobile-navigation-patterns`, 2015): persistente, ícone **com rótulo**; **4–5 destinos** sempre visíveis; acima de 5 o alvo de toque encolhe. Hambúrguer cabe muito, mas é pouco descobrível ("longe da vista, longe da mente"); se usar, ofereça cross-links. Menu por gesto sem sinalizador quase ninguém descobre e conflita com o voltar do iOS. Hub de navegação serve a apps de uma tarefa por sessão.
Bate com a Apple HIG (≤ 5 abas, sem "More", rótulo de 1 palavra, não esconder nem desabilitar abas) e com a toolbar "3–5 tools" desta skill.

**Tabs internas** (`tabs-used-right`, 2024, rev. 2026): não misturar tabs de navegação com tabs internas; poucas tabs, rótulos de **1–2 palavras**, sem caixa-alta; **pelo menos 2 indicadores de seleção** (linha + negrito, ou fundo); tabs não selecionadas legíveis; **um nível** de tabs (dois níveis só quando são claramente filtros, ex.: mercado × período em `9B_tabs_google-finance-in-page_1.jpg`); conteúdo mais usado primeiro; **no mobile, acordeão costuma vencer tabs** em conteúdo longo; teclado (Enter/Espaço), foco de alto contraste, papéis ARIA.

**4 padrões iOS que falham em teste** (`4-ios-rules-break`, 2015): page control (pontinhos) como único acesso a conteúdo (prefira cortar parte do próximo item); botão de enviar **no topo** do formulário (ponha embaixo ou fixo no rodapé); ícone "+" ambíguo em conteúdo (use rótulo); ícone de "mover" (deixe arrastar o item inteiro; "Menu" junto do hambúrguer). Estudo antigo: não copie esses 4 padrões só porque "é iOS".

## 3. Alvos de toque físicos (`touch-target-size`, 2019)
- Mínimo **1 cm × 1 cm (0,4 in)**, medida **física**, não em pixels (estudo de 2006).
- Ponta do dedo 1,6–2 cm; área do polegar ~2,5 cm.
- Ação primária ou uso em movimento: maior (exemplo do app da Target: **~2 cm × 2 cm**, `9B_touch-targets_target-app_1.jpg`).
- Espaço entre alvos concorrentes ~**2 mm**, mas primeiro o alvo precisa ser grande.
- **View–tap asymmetry**: legível mas pequeno demais para tocar (pontinhos de carrossel).
- Mapa com marcadores pequenos: ofereça lista como alternativa (idealmente padrão).
- Conversão para pt/dp: ver `typography-and-touch.md` §1b.

## 4. Empty states (`empty-state-interface-design`, 2021)
Nunca deixe a tela totalmente vazia (dúvida: carregando? erro? filtro errado?). O empty state faz 3 coisas:
1. **Comunica o estado do sistema** ("Não há registros para o intervalo selecionado").
2. **Ensina** a função ("Favorite itens para listá-los aqui", `9B_empty-states_datadog_1.jpg`).
3. **Dá um caminho direto** (botão "Criar", "Saiba mais", dados de demonstração).
"Sem registros" exibido **durante o carregamento** é pior que vazio: mostre progresso/skeleton enquanto processa. Liga com `components-checklists.md` §11 (home com estado vazio) e `perceived-performance.md`.

## 5. Formulários
**4 princípios** (`4-principles-reduce-cognitive-load`, 2025):
- **Estrutura**: agrupar, ordem lógica, **coluna única**, divulgação progressiva, "uma coisa por página" quando longo.
- **Transparência**: tempo estimado, o que vai precisar, salvar progresso, marcar obrigatórios e "(opcional)", indicador de progresso.
- **Clareza**: linguagem simples (nível de 6º a 8º ano), exemplos de formato, largura do campo coerente com a resposta.
- **Suporte**: **rótulo fora do campo, nunca só placeholder**; restrições úteis; erro **depois que o campo é concluído**, **ao lado do campo**.

**Erros** (`errors-forms-design-guidelines`, 2019, rev. 2024): validação inline; **não validar antes de terminar o campo** (no `blur`, não a cada tecla; exceção: medidor de senha que mostra sucesso em tempo real, `9B_formularios_slack-forca-senha_1.jpg`); mensagem ao lado do campo; **cor + ícone**, nunca só cor; animação sutil no ícone, nunca no texto; resumo de erros nunca como única indicação; **sem tooltip para erro**; modal com parcimônia; ajuda extra depois de **3 ou mais** erros no mesmo campo. Mensagem explícita, educada, precisa, com conselho.

**Login/cadastro mobile** (`checklist-registration-login`, 2017): login opcional sempre que possível; pedir o mínimo; **sem campo duplicado** de senha (use "mostrar senha"); revelar as regras de senha antes; medidor de força; "Esqueci a senha"; biometria. Senha no mobile leva quase o dobro do tempo.

**Microcopy** (`3-is-of-microcopy`, 2025): < 3 frases; objetivo principal informar, influenciar ou apoiar a interação; botão diz o que acontece (bate com "verbo + objeto").

**Fuso horário** (`time-zone-selectors`, 2022): 73% sabem o nome do fuso, só 34% o offset UTC; detecte automaticamente e deixe mudar; busca visível; ordene **por cidade** com país e offset.

## 6. Dashboards (`dashboards-preattentive`, 2017)
- Dashboard = uma tela para ação rápida. Separe **operacional** (decisão imediata) de **analítico**.
- Valores em **comprimento (barras)** e **posição 2D (linhas, dispersão)**. **Evite pizza, donut, gauge e treemap** em painel de leitura rápida; evite 3D (`9B_dashboards_linha-e-barras_1.jpg`).
- **Cor não é o único sinal**: cor marca categoria, não magnitude. Até ~4,5% da população tem daltonismo (~8% dos homens, ~0,5% das mulheres); use forma, posição, rótulo e agrupamento.

### DIVERGÊNCIA com `dashboard-ui` (registrar, não apagar)
`dashboard-ui` usa **donut, gauge e anéis** (apps de score, fitness, crédito, cards de KPI com anel) como referência visual. O NN/g diz para evitá-los em painéis de leitura rápida. **Critério (complemento):**
| Situação | Use |
|---|---|
| Comparar valores, ver tendência, ranking, várias categorias, painel operacional/analítico | **Barras ou linhas** (NN/g) |
| **Um único** número contra uma meta clara (score 0–100, % da meta, progresso do anel de atividade), com o **número escrito** no centro | Anel/gauge aceito como **moldura** do número, não como forma de leitura |
| Parte de um todo com **2–3 fatias** e rótulo com % | Donut aceito; com 4+ fatias, troque por barra empilhada ou barras horizontais |
| Pizza/donut/gauge lado a lado para comparar | **Nunca**: troque por barras |
Em todos os casos: valor numérico visível, cor + rótulo/forma, sem 3D. Vale para cliente e gestor; em painel operacional de uso diário (ferramenta de trabalho), sem gauge/anel: só barras/linhas (`dashboard-ui` padrão 17).

## 7. Tabelas de dados (`data-tables`, 2022)
Tabela vence cards em comparação e escala. 4 tarefas: achar, comparar, ver/editar linha, agir. 1ª coluna com identificador legível; cabeçalho e 1ª coluna fixos; ocultar/reordenar colunas com estado visível; **edição em painel lateral não modal** (modal cobre os registros vizinhos, `9B_tabelas_painel-lateral-crm_1.jpg`); ações em lote com "selecionar todos" e barra contextual.

## 8. Confiança: 5 níveis de compromisso (`commitment-levels`, 2016)
1. Relevância e confiança básica → 2. preferência sobre alternativas → 3. confiança com dados pessoais → 4. confiança com dados sensíveis/financeiros → 5. disposição para relação contínua.
- **Não faça pedido de nível alto antes de resolver os de baixo.** Login obrigatório logo de início pula direto ao nível 3; pedir conta social conectada é pedido de nível 5.
- **Entregue valor antes de pedir dados**: deixe explorar, dê controle. Vale para login, convite, cadastro, pagamento e permissões. Liga com `dark-patterns.md` (nagging, trial que cobra).

## 9. Permissões em contexto (`permission-requests`, 2019)
- Dar um motivo **aumentou o aceite em 12%** (Tan et al., 2014, 15 apps); o motivo mais convincente teve **+81%** sobre o menos convincente.
- Fórmula: "[app] quer acessar [recurso] **para que você possa [benefício]**". Evite "para melhorar sua experiência".
- **Peça no contexto** (quando a pessoa toca no recurso); na 1ª abertura, só o essencial.
- **Permita reverter**: se negou, explique por que a função não funciona e leve direto às configurações (`9B_permissoes_venmo-camera-negada_1.jpg`: "No Camera Access" + motivo + "Open Settings").
- iOS tem "purpose string"; no Android, tela explicativa antes do diálogo do sistema. No PWA as permissões são do navegador: o pré-aviso é responsabilidade do app **(complemento)**.

## 10. Métricas: HEART × CASTLE (`castle-framework`, 2023)
- **HEART** (Happiness, Engagement, Adoption, Retention, Task success): produto de **consumo** (app do cliente).
- **CASTLE** (Cognitive load, Advanced feature usage, Satisfaction, Task efficiency, Learnability, Errors): **ferramenta de trabalho** (painel do gestor, back-office, SaaS interno), onde uso é obrigatório e "engajamento" não mede sucesso.
- Quebre cada dimensão em metas → sinais → medidas (NASA-TLX para carga cognitiva, SEQ para satisfação, tempo em tarefa, erros de validação via analytics). Métrica diz **se** melhorou, não **por quê**: pareie com pesquisa qualitativa.

## 11. Acessibilidade visual (`visual-treatments-accessibility`, 2022)
Contraste 4,5:1 (3:1 para texto ≥ 18pt ou 14pt bold); não depender só de cor (teste em escala de cinza); foco visível com contorno espesso; alt text conciso. **5 usuários** já rendem feedback valioso; inclua baixa visão e dificuldade motora. Bate com `typography-and-touch.md` §3.

---

## Lacunas do NN/g (o que buscar em outra fonte)
- **Motion e microinterações** (durações, easing, springs): sem números → `ui-motion` (`official-motion-guidelines.md`).
- **PWA vs. Capacitor/nativo**: só no relatório pago.
- **Gestos e componentes iOS atuais** (sheets, menus contextuais, Dynamic Island): artigos de 2017–2018.
- **Dark mode**, **mobile tables**, **push e microsessões**, **skeleton vs spinner** (vídeo bloqueado sem cookies): não lidos.
- **Domínio do produto** (CRM, propostas, contratos, agenda de conteúdo, cobrança) e **PT-BR**: não cobertos.
- **Dados antigos**: muitos estudos mobile de 2015–2019; reavalie com teste no seu produto.
- Acessibilidade cognitiva/neurodivergência: sem guia aprofundado.

## Artigos usados (todos em `https://www.nngroup.com/articles/<slug>/`)
| Slug | Ano | Seção |
|---|---|---|
| `mobile-app-onboarding` | 2020 | §1 |
| `mobile-navigation-patterns` | 2015 | §2 |
| `tabs-used-right` | 2024 (rev. 2026) | §2 |
| `4-ios-rules-break` | 2015 | §2 |
| `touch-target-size` | 2019 | §3 |
| `empty-state-interface-design` | 2021 | §4 |
| `4-principles-reduce-cognitive-load` | 2025 | §5 |
| `errors-forms-design-guidelines` | 2019 (rev. 2024) | §5 |
| `checklist-registration-login` | 2017 | §5 |
| `3-is-of-microcopy` | 2025 | §5 |
| `time-zone-selectors` | 2022 | §5 |
| `dashboards-preattentive` | 2017 | §6 |
| `data-tables` | 2022 | §7 |
| `commitment-levels` | 2016 | §8 |
| `permission-requests` | 2019 | §9 |
| `castle-framework` | 2023 | §10 |
| `visual-treatments-accessibility` | 2022 | §11 |
Relatórios gratuitos úteis: *Usability Guidelines for Accessible Web Design*, *Tablet Website and Application UX*, *Mobile Intranets and Enterprise Apps*. O relatório *UX for Mobile Applications and Websites* (5ª ed., 374 guidelines) é pago (US$ 298).
