# Rodada 9B: UX e pesquisa (Nielsen Norman Group)

Data da pesquisa: 22/11/2026. Todas as URLs abaixo foram abertas no navegador antes de serem citadas. Quando algo não pôde ser lido, está marcado como "não verificado" ou 🔒.

## Resumo (principais aprendizados)

1. **Onboarding:** o NN/g recomenda evitar onboarding instrucional sempre que possível. Prefere dicas em contexto, empty states úteis e interface mais aprendível. Só vale onboarding quando o app precisa de dados para começar, é muito personalizado ou tem fluxos realmente novos.
2. **Tabs:** o tab bar mobile funciona bem com até 4–5 destinos. Acima de 5 o alvo de toque encolhe e o menu hambúrguer esconde a navegação. Inferência para o app do cliente (PWA/Capacitor): tab bar inferior com rótulos e no máximo 5 destinos (isto é leitura minha, não afirmação do NN/g).
3. **Alvos de toque:** mínimo físico de 1 cm × 1 cm (0,4 in). Ações principais ou uso em movimento pedem mais (o NN/g cita ~2 cm × 2 cm em exemplo). O NN/g mede em tamanho físico, não em pixels.
4. **Empty states** devem ser projetados: dizer o estado do sistema, ensinar a função e oferecer um caminho direto (botão) para a primeira tarefa. Estado totalmente vazio gera dúvida ("está carregando? deu erro?").
5. **Formulários:** 4 princípios (estrutura, transparência, clareza, suporte), coluna única, sem placeholder no lugar de rótulo, validação inline só depois que o campo é concluído, erro ao lado do campo.
6. **Dashboards:** use comprimento e posição 2D (barras, linhas) para valores. Evite pizza, donut, gauge e treemap em painéis de leitura rápida. Cor nunca deve ser o único sinal.
7. **Confiança:** o NN/g descreve 5 níveis de compromisso. Não peça dados pessoais, cadastro ou contas conectadas antes de entregar valor e credibilidade. Para o app, isso vale para login, convite do cliente e pedido de permissões.
8. **Permissões:** pedir no contexto, explicar o benefício em linguagem simples, permitir reverter. Estudo citado: dar um motivo aumentou em 12% a chance de aceite, e o texto mais convincente chegou a +81% sobre o menos convincente.
9. **Métricas:** HEART é para produtos de consumo. CASTLE (Cognitive load, Advanced features, Satisfaction, Task efficiency, Learnability, Errors) serve melhor para o painel do gestor, que é uma ferramenta de trabalho.
10. **Lacunas:** o NN/g quase não cobre motion/microinterações, PWA vs. Capacitor, creator economy, CRM/propostas/contratos, nem conteúdo em PT-BR. Vários estudos são antigos (2015–2019); a Apple já mudou padrões que eles criticam.

---

## Parte A: Páginas semente (links 8–12)

### Link 8 — Artigos (índice geral)
- https://www.nngroup.com/articles/ | status: ✅ abriu | data: página dinâmica (mostra itens de nov/2026)
- Tema: índice de artigos e vídeos | nível: misto | gratuito
- Conteúdo extraído: lista de "Popular Articles" (10 Usability Heuristics, Journey Mapping 101, Usability Testing 101 etc.) e itens recentes, como "6 Tips for Better Tabs" (vídeo, 10/nov/2026) e "Complex vs. Complicated" (vídeo, 2/nov/2026).
- Aplica-se a: ponto de partida e monitoramento contínuo.
- Limitações: a busca interna (`/search/?q=...`) não carregou resultados no navegador; a descoberta foi feita por study guides e páginas de tópico.

### Link 9 — Mobile UX: Study Guide
- https://www.nngroup.com/articles/mobile-ux-study-guide/ | status: ✅ | 12/jan/2023 (Raluca Budiu)
- Tema: guia de leitura em ordem recomendada | nível: iniciante a avançado | gratuito
- Seções: Considerações gerais, Interação, **Navegação**, Conteúdo, **Experiência inicial (login/onboarding)**, Gestos, Recursos específicos (permissões, push, microsessões), Multitarefa, Web responsivo, Diferenças culturais, Outros dispositivos, E-commerce, Teste de usabilidade mobile, Histórico, Relatórios.
- Artigos do guia mais úteis para o app (slug após `/articles/`):
  - Interação: `touch-target-size`, `mobile-accordions`, `mobile-input-checklist`, `4-ios-rules-break`, `accidental-overlay-dismissal`, `infinite-scrolling-tips`.
  - Navegação: `mobile-navigation-patterns`, `support-mobile-navigation`, `mobile-subnavigation`, `image-vs-list-mobile-navigation`.
  - Conteúdo: `defer-secondary-content-for-mobile`, `utilize-available-screen-space`, `mobile-tables`, `mobile-list-thumbnail`, `mini-ia-structuring-information`.
  - Experiência inicial: `checklist-registration-login`, `login-walls`, `mobile-app-onboarding`, `mobile-tutorials`, `mobile-instructional-overlay`.
  - Gestos: `iphone-x`, `contextual-swipe`.
  - Recursos mobile: `permission-requests`, `push-notification`, `mobile-microsessions`.
  - Web/responsivo: `mobile-native-apps` (nativo, web app e híbrido).
- Relatórios listados no guia: *User Experience for Mobile Applications and Websites* (pago), *Tablet Website and Application UX* (gratuito), *iPad App and Website Usability* (gratuito).
- Limitações: a lista de "Histórico" é de interesse apenas histórico; vários artigos do guia são de 2015–2019.

### Link 10 — Web UX: Study Guide
- https://www.nngroup.com/articles/web-ux-study-guide/ | status: ✅ | 18/dez/2025 (Huei-Hsin Wang)
- Tema: guia de leitura de web UX | nível: iniciante a avançado | gratuito
- Seções: Uso da web, **Comportamento de leitura**, Eyetracking, **Interação** (tabs, acordeões, modais, skeleton/spinners, animação), Conteúdo, **Formulários**, Usabilidade de links, **Navegação**, **Busca**, **Multiplataforma (breakpoints, responsivo)**, Design visual (grids, contraste, dark mode, glassmorphism), Tendências, E-commerce.
- Artigos do guia mais úteis (slug):
  - Interação: `tabs-used-right`, `card-view-vs-list-view`, `modal-nonmodal-dialog`, `skeleton-screens-vs-progress-bars-vs-spinners`, `animation-usability`, `distracting-animations`.
  - Formulários: `web-form-design`, `eas-framework-simplify-forms`, `4-principles-reduce-cognitive-load`, `wizards`, `errors-forms-design-guidelines`, `placeholders-form-fields`, `required-fields`.
  - Navegação/IA: `menu-design`, `breadcrumb-navigation-useful`, `flat-vs-deep-hierarchies`, `3-ia-mistakes`, `3-click-rule`.
  - Multiplataforma (listados por título; slugs não anotados): "Breakpoints in Responsive Design", "Large Devices Preferred for Important Tasks", "The Negative Impact of Mobile-First Web Design on Desktop".
  - Visual: `visual-treatments-accessibility`; por título (slugs não anotados): "Low-Contrast Text Is Not the Answer", "The Aesthetic-Usability Effect", "Dark Mode vs. Light Mode", "Dark Mode: How Users Think About It", "Glassmorphism".
- Total de itens indexados na tabela do guia: 181 links.
- Relatórios listados: *Usability Guidelines for Accessible Web Design* (gratuito), *How to Conduct Eyetracking Studies* (gratuito); pagos: *How People Read Online*, *B2B Website Usability*.
- Limitações: vários vídeos do guia não exibem texto sem aceitar cookies (ver ficha do vídeo de skeleton).

### Link 11 — Tópicos
- https://www.nngroup.com/topics/ | status: ✅ | gratuito
- Estrutura: Design Process, Research, Audiences, Web UX, Management & Strategy, User Psychology, Devices & Applications.
- Páginas de tópico encontradas e abertas por mim: `/topic/applications/` (Application Design, 5 páginas). URLs de tópico existentes (vistas na página): visual-design, analytics-and-metrics, research-methods, user-testing, accessibility, information-architecture, navigation, persuasive-design, search, writing-web, behavior-patterns, applications, mobile-and-tablet-design.
- Observação: tentei `/topic/application-design/` e deu 404; o slug correto é `/topic/applications/`.
- Itens recentes em Application Design (página 1, aberta): "Complex vs. Complicated" (vídeo, 2/nov/2026), "Are You Supporting Legacy Users?" (vídeo, 28/set/2026), "Why So Many Info Tips Are Bad" (23/jan/2026), "Designing Effective Contextual Menus: 10 Guidelines" (28/nov/2025), "Overflow Menu Icons" (vídeo), "UX Strategies for Complex-Application Design" (25/jul/2025), "Supporting Power Users Isn't Enough: 3 Complex-App User Types" (27/jun/2025), "Bulk Actions: 3 Design Guidelines" (vídeo, 17/mar/2025), "How to Increase the Visibility of Error Messages" (vídeo, 17/jun/2024), "Power Law of Learning" (vídeo, 31/jan/2024). **Não abertos individualmente.**

### Link 12 — Relatórios
- https://www.nngroup.com/reports/ | status: ✅
- Páginas abertas: `/reports/`, `/reports/topic/mobile-and-tablet-design/`, `/reports/topic/applications/`, `/reports/free/`, `/reports/mobile-website-and-application-usability/`, `/reports/make-decisions/`.

| Relatório | Preço / acesso | Escopo | Serve ao app? |
|---|---|---|---|
| **User Experience for Mobile Applications and Websites** (5ª ed.) | **Pago: US$ 298 individual, US$ 598 grupo** (arquivos digitais) | 713 páginas, **374 guidelines**, mais de 1000 screenshots; 19 estudos presenciais e 2 remotos em 8 países. Cobre tab bar, touch targets, formulários, login/passkeys, skeleton screens, PWA, permissões, gestos, onboarding | Alta (PWA/Capacitor do cliente) |
| **Helping Users Make Decisions** | Pago: US$ 49 individual, US$ 99 grupo | 70 páginas; psicologia da escolha, sobrecarga de opções | Média (propostas, planos, escolha de pacotes) |
| **Tablet Website and Application UX** | **Gratuito** (listado em /reports/free/) | 126 guidelines para tablets | Média (painel em iPad) |
| **Usability Guidelines for Accessible Web Design** | **Gratuito** | 75 guidelines, 150 páginas, leitores de tela, lupas | Alta (acessibilidade) |
| **How to Conduct Usability Studies for Accessibility** | **Gratuito** | 40 recomendações | Média (teste com usuários) |
| **How to Recruit Participants for Usability Studies** | **Gratuito** | 234 dicas | Média (testes do piloto) |
| **Mobile Intranets and Enterprise Apps** | **Gratuito** (aparece na lista de gratuitos; também em Application Design e Mobile) | 237 páginas, casos de apps corporativos | Média (painel do gestor) |
| **Presenting Company Information on Corporate Websites** (About Us) | **Gratuito** | 85 guidelines | Média (perfil/portfólio e credibilidade) |
| **Marketing Email and Newsletter Design** | **Gratuito** | 199 guidelines | Baixa a média (e-mails de proposta/relatório) |
| **Strategic Design for FAQs** | **Gratuito** | FAQ | Baixa |
| **Site Map Usability** | **Gratuito** | 47 dicas | Baixa |
| **iPad App and Website Usability** | **Gratuito** | Estudos antigos de iPad | Baixa (antigo) |
| Intranet Usability Guidelines (300 guidelines, 4 volumes), Intranet Design Annual | Pagos (os anuários antigos aparecem como gratuitos) | Intranets | Baixa |
| Architecting a Journey Management Practice | Pago (preço não aberto) | Jornada | Baixa |

- Não verificado: preço de *Ecommerce UX Vol. 09 – Trust and Credibility* (a página só apareceu em busca, não foi aberta) e dos demais relatórios pagos não listados acima.
- Limitações: a lista "gratuita" mistura relatórios antigos; confira a data antes de usar.

---

## Parte B: Fichas dos artigos lidos (17 abertos e lidos na íntegra)

### Touch Targets on Touchscreens
- https://www.nngroup.com/articles/touch-target-size/ | ✅ | 5/mai/2019 | Tema: alvos de toque | nível: iniciante | gratuito
- Recomendações:
  - Alvo mínimo **1 cm × 1 cm (0,4 in)**, medida física, não em pixels (estudo de Parhi, Karlson e Bederson).
  - Ponta do dedo: 1,6–2 cm de largura (MIT Touch Lab); área de impacto do polegar: ~2,5 cm.
  - Espaçamento mínimo citado entre alvos concorrentes: ~2 mm; mas o alvo precisa ser grande primeiro e depois bem espaçado.
  - "View–tap asymmetry": elementos legíveis, mas pequenos demais para tocar (ex.: pontinhos de carrossel).
  - Ações primárias ou uso em movimento: maiores (exemplo do app da Target: ~2 cm × 2 cm).
  - Idosos e crianças se beneficiam de alvos maiores. Reduzir elementos na tela permite alvos maiores.
  - Mapas com marcadores pequenos erram toques: ofereça lista como alternativa (idealmente padrão).
- Telas do app: tab bar, agenda (slots de horário), listas de mensagens, ações em cards, calendário do cliente.
- Limitações: estudo de 2006 + artigo de 2019. Os valores em pt/dp equivalentes saem de HIG/Material (rodada 9A), não do NN/g.

### Basic Patterns for Mobile Navigation: A Primer
- https://www.nngroup.com/articles/mobile-navigation-patterns/ | ✅ | 15/nov/2015 | navegação mobile | gratuito
- Recomendações:
  - Priorizar conteúdo sobre "chrome", mas manter navegação descobrível.
  - **Tab bar:** persistente, rótulos nos ícones; bom quando há poucas opções. Mais de 5 opções ficam difíceis de caber com alvo de toque adequado. 4–5 destinos principais podem ficar sempre visíveis.
  - **Hambúrguer/menu:** cabe muitas opções, mas é pouco descobrível ("longe da vista, longe da mente"); adequado a apps de navegação/consumo de conteúdo. Se usar, ofereça navegação cruzada (cross-links).
  - **Hub de navegação:** serve a apps orientados a tarefa em que o usuário usa uma tarefa por sessão.
  - Menu por gesto sem sinalizador (swipe na borda) quase ninguém descobre e conflita com o gesto de voltar do iOS.
- Telas: navegação principal do app do cliente (Início, Agenda, Conteúdo, Mensagens, Perfil) e do painel.
- Limitações: 2015. Regras de design iOS/Material evoluíram; o princípio de 4–5 destinos permanece.

### iOS Design Rules to Break (4 iOS Rules to Break)
- https://www.nngroup.com/articles/4-ios-rules-break/ | ✅ | 19/jul/2015 | padrões iOS | gratuito
- Recomendações (contra padrões do iOS que falham em teste):
  1. **Page control (pontinhos):** sutis demais; não use como único acesso a conteúdo. Alternativas: cortar parte do próximo item para sugerir swipe; ou usar navegação/links de texto. Se usar, alto contraste e centralizados abaixo do conteúdo.
  2. **Botão de enviar no topo do formulário:** vai contra o fluxo de cima para baixo. Coloque o botão sob os campos; se precisar estar sempre acessível, use botão fixo no rodapé.
  3. **Ícone "+":** ambíguo (adicionar, expandir, seguir). Na barra de navegação é relativamente seguro; em conteúdo, use rótulo de texto ou seta/caret.
  4. **Ícone "mover" (três linhas):** deixe arrastar o item inteiro; mostre "Menu" junto do hambúrguer.
- Telas: formulários de proposta/contrato, listas reordenáveis (pauta de conteúdo), cards em carrossel.
- Limitações: 2015; a Apple mudou componentes depois. **Atenção:** o direcionamento "inspirado em iOS" do app não deve copiar esses 4 padrões sem teste.

### Mobile-App Onboarding: An Analysis of Components and Techniques
- https://www.nngroup.com/articles/mobile-app-onboarding/ | ✅ | 21/jun/2020 | onboarding | gratuito
- Recomendações:
  - **Evite onboarding sempre que possível** (custo de interação, carga de memória, benefício duvidoso; tutoriais em deck de cards não melhoraram desempenho em estudo do NN/g).
  - Onboarding se justifica quando: precisa de dados do usuário para começar, o app depende de contexto/preferências, ou o fluxo é realmente novo.
  - Tipos: promoção de funções (evitar no primeiro uso; fica melhor na loja de apps ou quando a função fica acionável, ex.: após 7 dias de dados), personalização (conteúdo sim; **tema/cores no onboarding não**), instruções (breves, opcionais, só o necessário).
  - Deck de cards: se usar, "Skip" bem visível, poucos cards, um conceito por card.
  - Overlays/coach marks: no momento certo e discretos; walkthrough interativo para fluxos novos, com opção de pular.
  - Explique por que pede cada dado; mostre progresso e permita pular.
- Telas: onboarding do cliente (convite → perfil mínimo), primeira vez no portfólio, agenda e propostas.
- Limitações: foco em apps de consumo; para o painel do gestor, combine com empty states.

### Designing Empty States in Complex Applications: 3 Guidelines
- https://www.nngroup.com/articles/empty-state-interface-design/ | ✅ | 19/set/2021 (Kate Kaplan) | empty states | gratuito
- Recomendações:
  - Não deixe estados totalmente vazios (causam dúvida: carregando? erro? filtro errado?).
  - Use empty state para: (1) **comunicar o estado do sistema** (ex.: "Não há registros para o intervalo de datas selecionado"); (2) **ensinar** ("Favorite itens para listá-los aqui"); (3) **dar caminho direto** (botão "Criar", link "Saiba mais", dados de demonstração).
  - Mensagem "Sem registros" exibida durante carregamento é pior que vazio: corrói confiança. Use indicador de progresso enquanto processa.
- Telas: dashboard sem dados, agenda vazia, portfólio sem projetos, caixa de mensagens, resultados sem período.
- Limitações: exemplos de apps corporativos complexos; adapte o tom para o cliente final.

### 10 Design Guidelines for Reporting Errors in Forms
- https://www.nngroup.com/articles/errors-forms-design-guidelines/ | ✅ | 3/fev/2019, revisado 12/dez/2024 | erros em formulários | gratuito
- Recomendações: validação inline quando possível; indicar sucesso em campos complexos (ex.: senha com medidor); mensagem ao lado do campo; cor + ícone (não só cor); animação sutil no ícone (nunca no texto); modais só com parcimônia; **não validar antes de terminar o campo**; resumo de validação nunca como única indicação; não usar tooltip para erro; ajuda extra após **3 ou mais** erros repetidos no mesmo preenchimento.
- Mensagens: explícitas, legíveis, educadas, precisas, com conselho construtivo.
- Telas: formulários de proposta, contrato, cadastro de cliente, configurações.
- Limitações: foco em web; no mobile, cuidado com teclado cobrindo mensagens.

### Dashboards: Making Charts and Graphs Easier to Understand
- https://www.nngroup.com/articles/dashboards-preattentive/ | ✅ | 18/jun/2017 | dashboards | gratuito
- Recomendações:
  - Dashboard = visão de uma tela, para ação rápida. Diferencie **operacional** (decisão imediata) de **analítico**.
  - Use **comprimento (barras)** e **posição 2D (linhas, dispersão)** para valores; evite pizza, donut, gauge e treemap em painéis de leitura rápida; evite 3D.
  - Cor serve para categoria, não para magnitude; até 4,5% da população tem daltonismo (~8% homens, ~0,5% mulheres); use forma e agrupamento como sinal principal.
- Telas: Resultados (alcance, engajamento, leads), painel do gestor com visão de múltiplos clientes.
- Limitações: 2017; não cobre mobile nem gráficos interativos.

### 3 Design Considerations for Effective Mobile-App Permission Requests
- https://www.nngroup.com/articles/permission-requests/ | ✅ | 28/abr/2019 | permissões | gratuito
- Recomendações e números:
  - Dar um motivo **aumentou em 12%** a chance de aceite (estudo de Tan et al., 2014, 15 apps); o motivo mais convincente gerou **+81%** de aceite versus o menos convincente.
  - Fórmula: "[app] gostaria de acessar [recurso] para que você possa [benefício]". Evite "para melhorar a experiência".
  - Pedir **no contexto** (quando o usuário toca no recurso), não tudo no primeiro uso; só permissões essenciais na primeira abertura.
  - Permitir reverter: explicar por que a função não funciona e ligar direto às configurações do dispositivo.
  - Evitar dark patterns.
  - No iOS há "purpose string"; no Android é preciso uma tela explicativa antes do diálogo do sistema.
- Telas: notificações push, câmera/fotos para portfólio, contatos para networking, calendário.
- Limitações: 2019. Em **PWA** as permissões são do navegador; em **Capacitor** são as do SO (ver plugins), então o texto do pré-aviso é responsabilidade do app.

### 5 Visual Treatments that Improve Accessibility
- https://www.nngroup.com/articles/visual-treatments-accessibility/ | ✅ | 30/out/2022 | acessibilidade visual | gratuito
- Recomendações:
  - Contraste de texto ≥ **4,5:1**; para texto ≥ 18 pt (ou 14 pt em negrito), **3:1** (WCAG).
  - Não depender só de cor (teste em escala de cinza); estado de foco visível (contorno espesso); alt text conciso e sem repetir legenda; imagens decorativas sem alt.
  - Testar com usuários reais: 5 usuários já rendem feedback valioso; inclua pessoas com baixa visão e dificuldade motora.
- Telas: todo o app, especialmente texto sobre imagens do portfólio e estados de formulário.
- Limitações: não cobre acessibilidade cognitiva em profundidade, nem VoiceOver/TalkBack em apps nativos.

### CASTLE Framework for Productivity/Workplace Applications
- https://www.nngroup.com/articles/castle-framework/ | ✅ | 29/jan/2023 | métricas de UX | gratuito
- Recomendações:
  - HEART (Happiness, Engagement, Adoption, Retention, Task success) funciona para produtos de consumo; **CASTLE** é para software de trabalho: Cognitive load, Advanced feature usage, Satisfaction, Task efficiency, Learnability, Errors.
  - Cada dimensão deve ser quebrada em metas, sinais e medidas (ex.: NASA-TLX para carga cognitiva, SEQ para satisfação, tempo em tarefa em teste quantitativo, erros de validação via analytics).
  - Métricas dizem se algo melhora, não por quê: pareie com pesquisa qualitativa.
- Telas: painel do gestor (CASTLE), app do cliente (HEART: retenção, adoção).
- Limitações: sem valores de referência de mercado.

### Few Guesses, More Success: 4 Principles to Reduce Cognitive Load in Forms
- https://www.nngroup.com/articles/4-principles-reduce-cognitive-load/ | ✅ | 18/jul/2025 | formulários | gratuito
- Recomendações: **Estrutura** (agrupar campos, hierarquia visual, ordem lógica, **coluna única**, divulgação progressiva, "uma coisa por página"); **Transparência** (tempo estimado, materiais necessários, salvar progresso, marcar obrigatórios e "(opcional)", indicador de progresso); **Clareza** (linguagem simples em nível de 6º a 8º ano, texto positivo, exemplos de formato, convenções de elementos, largura do campo coerente); **Suporte** (**evitar placeholders**, restrições úteis, erro depois que o campo for concluído e ao lado do campo, sugestões construtivas).
- Telas: onboarding, propostas, contratos, configurações de perfil.
- Limitações: exemplos de web desktop; alguns exemplos usam wheel picker, que o próprio artigo desaconselha.

### It's Time We Addressed Time-Zone Selectors
- https://www.nngroup.com/articles/time-zone-selectors/ | ✅ | 11/dez/2022 | agenda/agendamento | gratuito
- Recomendações e números:
  - 73% sabiam o próprio fuso (ex.: "Central European Time"); só 34% sabiam o offset em UTC (55% em GMT).
  - Detectar o fuso automaticamente e deixar mudar; busca visível no seletor; ordenar **alfabeticamente por cidade**, com país e offset; permitir buscar por fuso ("Pacific Time"); evitar ordenar por offset (se ordenar, offset primeiro).
  - Agrupar por continente ajudou quando ordenado por offset; coloque primeiro as regiões do seu público.
  - Primeira busca mais comum: cidade (44%), depois fuso (24%).
- Telas: agenda de reuniões, publicação programada, convites (cliente em outro país: público PT e EN).
- Limitações: estudo com 13 + 83 participantes de 8 países (4 no teste não moderado); não cobre PT-BR especificamente.

### Hierarchy of Trust: The 5 Experiential Levels of Commitment
- https://www.nngroup.com/articles/commitment-levels/ | ✅ | 6/mar/2016 | confiança | gratuito
- Recomendações: 5 níveis (relevância e confiança básica → preferência sobre alternativas → confiança com dados pessoais → confiança com dados sensíveis/financeiros → disposição para relação contínua). Não faça pedidos de nível alto antes de resolver os de nível baixo. Login obrigatório logo de início pula direto ao nível 3; conta social conectada é pedido de nível 5. Dê controle e permita explorar antes de pedir dados.
- Telas: convite do cliente, landing do perfil público, contratos (dados sensíveis), cobrança recorrente.
- Limitações: 2016, foco em sites de conversão.

### The 3 I's of Microcopy: Inform, Influence, and Interact
- https://www.nngroup.com/articles/3-is-of-microcopy/ | ✅ | 1/ago/2025 | microcopy | gratuito
- Recomendações: microcopy = menos de 3 frases; três objetivos (informar, influenciar, apoiar interação); classifique cada peça pelo objetivo principal, não pelo tipo de elemento; rótulos de botão dizem o que acontece; não substitua rótulos de campo por placeholder.
- Telas: botões, empty states, notificações, tooltips, rótulos de navegação, CTAs de proposta.
- Limitações: sem diretrizes de tom em PT-BR; ver também (não aberto) `ux-copy-sizes`.

### Data Tables: Four Major User Tasks
- https://www.nngroup.com/articles/data-tables/ | ✅ | 3/abr/2022 | tabelas | gratuito
- Recomendações: tabela vence cards em comparação e escalabilidade; 4 tarefas (achar, comparar, ver/editar linha, agir); primeira coluna com identificador legível; cabeçalho e primeira coluna fixos; ocultar/reordenar colunas com estado visível; edição em **painel lateral não modal** (modal cobre registros vizinhos); ações em lote com "selecionar todos" e barra contextual.
- Telas: lista de clientes/CRM, propostas e contratos, resultados em tabela (painel web).
- Limitações: foco desktop; artigo irmão sobre tabelas no mobile (`mobile-tables`) **não aberto**.

### A Checklist for Registration and Login Forms on Mobile
- https://www.nngroup.com/articles/checklist-registration-login/ | ✅ | 4/jun/2017 | login/cadastro | gratuito
- Recomendações: digitar senha no mobile leva quase o dobro do tempo; login opcional sempre que possível; explicar benefícios; login social como alternativa; pedir só o mínimo (email e senha); mostrar senha; revelar regras de senha antes; medidor de força; **sem campo duplicado**; evitar confirmação por link de email (preferir código por SMS); biometria (TouchID); opção "mostrar senha" (mascarada por padrão no login); "Esqueci a senha".
- Telas: login, cadastro, convite do cliente.
- Limitações: 2017, não cobre passkeys (a 5ª edição do relatório pago cobre passkeys e OTP, **não verificado** o conteúdo).

### Tabs, Used Right
- https://www.nngroup.com/articles/tabs-used-right/ | ✅ | 2/ago/2024, revisado 2/set/2026 | tabs | gratuito
- Recomendações: distinguir **tabs de navegação** de **tabs internas**, não misturar; poucas tabs, rótulos de 1–2 palavras, sem caixa-alta; usar **pelo menos 2 indicadores de seleção** (linha, negrito, fundo etc.); tabs não selecionadas legíveis; um nível de tabs; lista acima do painel; conteúdo mais usado primeiro; no mobile, **acordeões costumam funcionar melhor que tabs** para conteúdo longo; acessibilidade: teclado (Enter/Espaço), foco de alto contraste, papéis ARIA.
- Telas: seções do perfil, agenda (Próximos/Passados), dashboards, configurações.
- Limitações: exemplos de web desktop.

### Skeleton Screens vs. Progress Bars vs. Spinners (vídeo)
- https://www.nngroup.com/videos/skeleton-screens-vs-progress-bars-vs-spinners/ | status: 🔒 abriu, mas o conteúdo do vídeo não carrega sem aceitar cookies | 4 min (Samhita Tankala)
- Extraído: apenas o resumo público ("indicam carregamento, mas servem a propósitos diferentes e funcionam melhor em contextos diferentes"). **Regras e números: não verificado.**
- Para loading/skeleton no app, usar o relatório mobile 5ª ed. (que inclui skeleton screens, conforme a página do relatório) ou outra fonte.

---

## Parte C: Candidatos vistos apenas em resultados de busca (NÃO abertos)

Aparecem nos resultados de busca com o resumo do site, mas **não os abri no navegador**; confirme antes de usar.
- `reporting-ux-business-outcomes` (Stop Reporting UX Activity and Report Business Outcomes) — retenção: % de usuários da semana que seguem ativos em 7/30 dias.
- `product-ux-benchmarks` e `benchmarking-ux` — HEART e benchmarking.
- `date-input` (Date-Input Form Fields) — calendário para datas próximas (menos de um ano).
- `ux-copy-sizes` e `microcontent`-artigo — tamanhos de copy.
- `complex-application-design` (8 Design Guidelines for Complex Applications).
- `accessible-design-for-users-with-disabilities`, `inclusive-design`, e os vídeos "Neurodivergence" e "Why Disabled Buttons Hurt UX" (tópico acessibilidade).
- `tone-voice-users` (impacto do tom de voz na percepção de marca) — pode ser útil para marca pessoal.
- `about-us-information-on-websites`, `trustworthiness-in-web-design` (credibilidade).
- `saving-scroll-position`, `animation-usability` e `distracting-animations` — (motion/animação na web).
- Curso pago: "Informative Microcopy" (US$ 199, 4,5 h).

---

## Top 15 para este produto (ordem de prioridade)

1. **Mobile-App Onboarding** — define se e como fazer onboarding do cliente no piloto.
2. **Basic Patterns for Mobile Navigation** — decide tab bar inferior vs. hambúrguer (limite de 4–5 destinos).
3. **Touch Targets on Touchscreens** — regra física de 1 cm e espaçamento; vale para PWA e Capacitor.
4. **Designing Empty States** — portfólio, agenda, resultados e mensagens começam vazios.
5. **Few Guesses, More Success (formulários)** — base para propostas, contratos e cadastro.
6. **10 Design Guidelines for Reporting Errors in Forms** — erros inline, repetidos e acessíveis.
7. **Permission Requests** — push, câmera, calendário e contatos, com números de aceite.
8. **Dashboards: Making Charts and Graphs Easier to Understand** — painel de resultados do gestor.
9. **Data Tables: Four Major User Tasks** — CRM, propostas e contratos no painel web.
10. **Tabs, Used Right** — seções de perfil, agenda e dashboard.
11. **Hierarchy of Trust** — sequência de pedidos (login, dados, pagamento, conta conectada).
12. **Time-Zone Selectors** — agenda para público PT/EN e clientes em outros fusos.
13. **5 Visual Treatments that Improve Accessibility** — contraste 4,5:1, foco, não depender só de cor.
14. **CASTLE Framework** — métricas do painel do gestor; combine com HEART para o cliente.
15. **iOS Design Rules to Break** — protege o visual "inspirado em iOS" de padrões que falham em teste.

Fora do Top 15, mas úteis: Checklist for Registration and Login Forms on Mobile (login do cliente), 3 I's of Microcopy (textos de botão e estados).

---

## Lacunas: o que o NN/g NÃO cobre bem para este app

- **Motion e microinterações** (durações, easing, springs): o NN/g tem artigos genéricos sobre animação na web (não abertos), mas sem valores numéricos; use Apple HIG, Material 3 e Carbon (rodada 9A).
- **PWA vs. Capacitor**: o study guide mobile tem "Native Apps, Web Apps, and Hybrid Apps" (`mobile-native-apps`, não aberto); o relatório pago 5ª ed. menciona PWA, mas o conteúdo não é público.
- **Gestos e navegação iOS atuais**: os artigos de gestos são de 2017–2018 (iPhone X); componentes modernos (sheets, menus contextuais, Dynamic Island etc.) não estão cobertos.
- **Dark mode do app**: o Web UX Study Guide lista dois artigos sobre dark mode (não abertos).
- **Domínio do produto**: creator economy, agendamento de conteúdo, CRM pessoal, networking, propostas e contratos, assinatura digital, cobrança. O NN/g só cobre formulários, tabelas, confiança e e-commerce em geral.
- **Mobile tables e listas**: `mobile-tables` está no guia, mas não foi aberto.
- **Conteúdo em português** e adaptação cultural PT-BR: tudo é em inglês, com estudos em outros contextos.
- **Dados novos**: muitos estudos mobile são de 2015–2019; reavalie com testes no piloto.
- **Skeleton/loading**: vídeo 🔒 sem texto público.
- **Acessibilidade cognitiva e neurodivergência**: existe um vídeo recente no tópico (não aberto); falta guia aprofundado.
- **Notificações push e microsessões** estão no study guide mobile, mas não foram abertos nesta rodada.

---

## Fontes verificadas (todas abertas no navegador)

- https://www.nngroup.com/articles/
- https://www.nngroup.com/articles/mobile-ux-study-guide/
- https://www.nngroup.com/articles/web-ux-study-guide/
- https://www.nngroup.com/topics/
- https://www.nngroup.com/topic/applications/
- https://www.nngroup.com/reports/
- https://www.nngroup.com/reports/topic/mobile-and-tablet-design/
- https://www.nngroup.com/reports/topic/applications/
- https://www.nngroup.com/reports/free/
- https://www.nngroup.com/reports/mobile-website-and-application-usability/
- https://www.nngroup.com/reports/make-decisions/
- https://www.nngroup.com/articles/touch-target-size/
- https://www.nngroup.com/articles/mobile-navigation-patterns/
- https://www.nngroup.com/articles/4-ios-rules-break/
- https://www.nngroup.com/articles/mobile-app-onboarding/
- https://www.nngroup.com/articles/empty-state-interface-design/
- https://www.nngroup.com/articles/errors-forms-design-guidelines/
- https://www.nngroup.com/articles/dashboards-preattentive/
- https://www.nngroup.com/articles/permission-requests/
- https://www.nngroup.com/articles/visual-treatments-accessibility/
- https://www.nngroup.com/articles/castle-framework/
- https://www.nngroup.com/articles/4-principles-reduce-cognitive-load/
- https://www.nngroup.com/articles/time-zone-selectors/
- https://www.nngroup.com/articles/commitment-levels/
- https://www.nngroup.com/articles/3-is-of-microcopy/
- https://www.nngroup.com/articles/data-tables/
- https://www.nngroup.com/articles/checklist-registration-login/
- https://www.nngroup.com/articles/tabs-used-right/
- https://www.nngroup.com/videos/skeleton-screens-vs-progress-bars-vs-spinners/ (🔒 conteúdo do vídeo indisponível)
- Tentativas sem sucesso: https://www.nngroup.com/topic/application-design/ (404; slug correto é /topic/applications/); https://www.nngroup.com/search/?q=empty+states (sem resultados carregados).

Observação de método: as URLs dos artigos foram descobertas nos study guides e, para temas que eles não cobrem (empty states, dashboards, microcopy, métricas, confiança, agendamento), por busca web restrita a nngroup.com. Só entraram nas fichas os que abri e li no navegador.

## Prints

9 prints de layouts reais (telas de apps e painéis) extraídos das imagens dos próprios artigos do NN/g. Pasta: `prints-9B/`. As telas pertencem aos apps/empresas mostrados (Facebook, Venmo, Hotel Tonight, Slack, Datadog, Target etc.); use só como referência interna de estudo, sem copiar.

| Arquivo | URL do artigo | O que mostra / como usar de referência |
|---|---|---|
| 9B_navegacao_facebook-tabbar_1.jpg | https://www.nngroup.com/articles/mobile-navigation-patterns/ | Tab bar inferior no iOS (com rótulos) vs. tab bar no topo no Android. Referência para a navegação principal do app do cliente |
| 9B_permissoes_venmo-camera-negada_1.jpg | https://www.nngroup.com/articles/permission-requests/ | Tela após negar câmera: explica o estado e leva a "Open Settings". Modelo para reversão de permissão |
| 9B_formularios_hoteltonight-botao-fixo_1.jpg | https://www.nngroup.com/articles/4-ios-rules-break/ | Formulário de reserva com botão de pagamento fixo no rodapé. Modelo para propostas/contratos |
| 9B_formularios_slack-forca-senha_1.jpg | https://www.nngroup.com/articles/errors-forms-design-guidelines/ | Medidor de força de senha com validação em tempo real |
| 9B_empty-states_datadog_1.jpg | https://www.nngroup.com/articles/empty-state-interface-design/ | Empty state que ensina ("Star your favorites to list them here") |
| 9B_tabelas_painel-lateral-crm_1.jpg | https://www.nngroup.com/articles/data-tables/ | Tabela de oportunidades com painel lateral não modal de edição. Referência para CRM/propostas no painel web |
| 9B_tabs_google-finance-in-page_1.jpg | https://www.nngroup.com/articles/tabs-used-right/ | Dois níveis de tabs internas (mercado e período) com gráfico. Referência para a tela de Resultados |
| 9B_dashboards_linha-e-barras_1.jpg | https://www.nngroup.com/articles/dashboards-preattentive/ | Gráfico de linha + barras de uso: o formato recomendado para dashboards |
| 9B_touch-targets_target-app_1.jpg | https://www.nngroup.com/articles/touch-target-size/ | Home com botões primários grandes (~2 cm) e tab bar de 5 itens com rótulo |

Nota: dois prints (Hotel Tonight e Datadog) saíram com o aviso de cookies no canto inferior esquerdo.
