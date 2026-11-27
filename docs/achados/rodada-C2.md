# Rodada C2 — continuação da galeria e das APIs

Data: 27/11/2026. Continua a `rodada-10C.md` (as fichas das 12 primeiras telas estão lá). Somente leitura: nenhuma conta, plano ou chave foi criado.

## 1. Resumo

- **Galeria: 23 de 60 telas** (12 da rodada anterior + 11 novas). Todas são de website (páginas públicas), com 1427–1471 px de largura. Ainda NÃO há app desktop nem mobile.
- Situação por segmento: FIN 9, CRM 5, PUB 4, MPE 1, SAU 2, JUR 2. Faltam 37 telas (meta mínima: 10 por segmento).
- **APIs:** dois "não verificado" da rodada anterior foram resolvidos:
  - **UI Sources** hoje é o **ScreensDesign** (`screensdesign.com`) e tem **MCP oficial**, incluído no plano Pro. Entra no ranking.
  - **Godly** redireciona para **recent.design**, uma galeria de inspiração. Não vi API, MCP ou feed na página (só olhei a tela, não li a documentação).
- Por que a galeria avança devagar: a captura de tela do navegador é a única forma de obter imagens neste ambiente (o shell não tem rede), e páginas de marketing mostram pouca interface. O caminho mais eficiente para fechar as 37 restantes é um MCP de referências (ScreensDesign, Refero ou Mobbin), que devolvem telas reais de apps.

## 2. Galeria — novas telas

Pasta: `10C/<SEG>/`. Data de publicação: "não verificado" em todas (páginas de produto não trazem data).

### FIN (+1 → 9 de 10)

| arquivo | nome sugerido | segmento | plataforma | produto/autor | URL exata | tipo de tela | componentes (nome sugerido) | o que observar | como adaptar sem copiar |
|---|---|---|---|---|---|---|---|---|---|
| 10C_FIN_stripe-invoicing_fatura-pagamento-moeda_1.png | Fatura com escolha de moeda e método | FIN | website | Stripe Invoicing | https://stripe.com/invoicing | detalhe de fatura / pagamento (mock) + faixa de benefícios | seletor de moeda lado a lado (`currency-toggle`), botões de método Card/Bank/SEPA (`payment-method-buttons`), 4 cards de benefício com ícone e link âncora (`benefit-cards`), faixa de logos de clientes | moeda original e convertida lado a lado; links em seta para baixo levam à seção | oferecer duas moedas e métodos de pagamento em linha, com ícones próprios |

### CRM (+1 → 5 de 10)

| arquivo | nome sugerido | segmento | plataforma | produto/autor | URL exata | tipo de tela | componentes (nome sugerido) | o que observar | como adaptar sem copiar |
|---|---|---|---|---|---|---|---|---|---|
| 10C_CRM_pipedrive_deals-kanban-app_1.png | Funil de negócios em kanban com sidebar | CRM | website (mock de app desktop) | Pipedrive | https://www.pipedrive.com/en | lista / funil | moldura de navegador (`browser-frame`), sidebar de ícones escura (`icon-sidebar`), colunas de etapa com total e nº de negócios (`stage-column`), cartões de negócio com valor (`deal-card`), alternância kanban/lista/gráfico (`view-switcher`) | cabeçalho de coluna em formato de seta mostra progressão; total da etapa visível; cartões com fade no fim | funil com cabeçalho de etapa mostrando valor somado e contagem, com formas e cores próprias |

### PUB (+4 → 4 de 10)

| arquivo | nome sugerido | segmento | plataforma | produto/autor | URL exata | tipo de tela | componentes (nome sugerido) | o que observar | como adaptar sem copiar |
|---|---|---|---|---|---|---|---|---|---|
| 10C_PUB_buffer_agendamento-ideias-boards_1.png | Compositor de post + quadro de ideias | PUB | website (mocks de app) | Buffer | https://buffer.com/ | agenda / criação | calendário mensal (`month-calendar`), seletor de canais por avatar (`channel-picker`), quadro de ideias em colunas Ideias/To do/Review (`idea-board`), prova social "375.227 criadores" (`social-proof-count`), faixa de ícones de integração | dois mocks lado a lado, cada um sobre fundo de cor diferente; contagem de usuários exata como prova | mostrar duas funções-chave em cards de cor distinta, com o contador de usuários real do produto |
| 10C_PUB_klaviyo_dashboard-receita-atribuida_1.png | Dashboard de receita atribuída por canal | PUB | website (mock de app em tablet) | Klaviyo | https://www.klaviyo.com/ | dashboard | tabela de receita por canal: campanhas, fluxos, e-mail, SMS, WhatsApp (`attributed-revenue-table`), card de recomendação com CTA (`ai-recommendation`), faixa de logos laranja (`logo-strip`), banner de cookies | números pequenos e densos dentro de moldura de dispositivo; recomendação de IA acima da lista de fluxos | tabela de receita por canal + recomendação acionável, com hierarquia própria |
| 10C_PUB_semrush_home-busca-insights_1.png | Campo de busca de domínio + cards de módulo | PUB | website | Semrush | https://www.semrush.com/ | home | campo de busca com seletor de país (`domain-search-field`), card roxo "Get found in search and AI answers" e card claro "Ask AI" (`module-cards`), banner de cookies com 3 opções | campo de busca é a ação principal da home; cards com listras diagonais como textura | busca única como CTA e cards de módulo com textura gráfica própria |
| 10C_PUB_mailchimp_home-selos-avaliacao_1.png | Hero com nota agregada de reviews | PUB | website | Mailchimp | https://www.mailchimp.com/ | home | estrelas + "33.000+ reviews" (`rating-summary`), selos Capterra/TrustRadius/G2 (`review-badges`), CTA amarelo + CTA secundário "Find the right plan", cards "Recommended for your business" | nota e origem dos reviews juntas; segundo CTA ajuda quem não decidiu | agregar avaliações de fontes reais com número e origem, e um CTA de ajuda para escolha de plano |

### MPE (+1 → 1 de 10)

| arquivo | nome sugerido | segmento | plataforma | produto/autor | URL exata | tipo de tela | componentes (nome sugerido) | o que observar | como adaptar sem copiar |
|---|---|---|---|---|---|---|---|---|---|
| 10C_MPE_beacons_perfil-link-bio-mock_1.png | Perfil de criador em link-in-bio (mock mobile) | MPE | website (mocks de app mobile) | Beacons | https://beacons.ai/ | perfil / portfólio | campo "beacons.ai/seunome" com CTA (`claim-handle-field`), perfil com ícones sociais e bio curta (`profile-header`), botões grandes de ação (`link-buttons`), carrossel de produtos (`product-strip`), card flutuante de produto (`floating-card`), painel de métricas (`stats-panel`) | três celulares em profundidade mostram perfil, métricas e feed; o campo de handle é a conversão principal | reservar o endereço pessoal como primeira ação e mostrar o perfil em mock mobile com persona fictícia |

### SAU (+2 → 2 de 10)

| arquivo | nome sugerido | segmento | plataforma | produto/autor | URL exata | tipo de tela | componentes (nome sugerido) | o que observar | como adaptar sem copiar |
|---|---|---|---|---|---|---|---|---|---|
| 10C_SAU_doctoralia_home-busca-especialista_1.png | Busca de profissional com modal de privacidade | SAU | website | Doctoralia | https://www.doctoralia.com.br/ | home + consentimento | abas "No local / Telecon…" (`visit-type-tabs`), campo de busca por especialidade (`specialty-search`), modal de consentimento com Recusar/Aceitar (`consent-modal`), listas de especialidades e convênios (`specialty-chips`), menu "Segurança de dados" | modal de privacidade bloqueia o hero (exemplo de consentimento destacado, em PT-BR); fundo verde-escuro transmite sobriedade | busca por especialidade como ação principal e consentimento claro, sem cobrir o campo de busca |
| 10C_SAU_headspace_cards-objetivos_1.png | Escolha de objetivo em cards | SAU | website | Headspace | https://www.headspace.com/ | home (seleção de objetivo) | cards "Stress less / Sleep soundly / Manage anxiety / Start therapy" com ícone (`goal-cards`), selo de oferta "50% off" (`offer-tag`), nota legal de renovação automática sob o CTA (`billing-disclosure`), banner de cookies | pergunta aberta + 5–6 cards de objetivo reduz a escolha; aviso de cobrança logo abaixo do CTA | oferecer objetivos em cards com ícone próprio e declarar condições de cobrança junto ao CTA |

### JUR (+2 → 2 de 10)

| arquivo | nome sugerido | segmento | plataforma | produto/autor | URL exata | tipo de tela | componentes (nome sugerido) | o que observar | como adaptar sem copiar |
|---|---|---|---|---|---|---|---|---|---|
| 10C_JUR_clio_home-numeros-confianca_1.png | Hero escuro com grade de números de confiança | JUR | website | Clio | https://www.clio.com/ | home | título em fonte leve de grande corpo, CTAs "Start a free trial / Book a demo" (`cta-pair`), grade de estatísticas: 400K+ profissionais, 130+ países, 50 ordens estaduais aprovam (`trust-stats`) | aprovação por ordens profissionais como prova de confiança, tipografia fina e sóbria | grade de 3–5 números verificáveis (incluindo aprovação de entidade de classe) com tipografia sóbria |
| 10C_JUR_jusbrasil_home-busca-processo_1.png | Busca única por processo, pessoa ou empresa | JUR | website | Jusbrasil | https://www.jusbrasil.com.br/ | home | alternância "Para todos / Para Advogados" (`audience-toggle`), campo de busca por nome/CPF/CNPJ/nº do processo (`process-search`), 3 atalhos em pílula (`intent-chips`) | linguagem simples ("sem juridiquês"); um campo cobre quatro tipos de entrada | busca única com atalhos de intenção e alternância de público, em linguagem acessível |

### Ainda sem capturas (para a próxima rodada)
MPE: 9 telas · SAU: 8 · JUR: 8 · PUB: 6 · CRM: 5 · FIN: 1. Sugestão: capturas oficiais de App Store/Google Play (app mobile), design systems públicos (tokens de cor/tipografia/motion), e portfólios no Behance/Awwwards (MPE).

Observações de conformidade: nenhuma tela mostra dados reais de terceiros (nomes como "Aliyah Brooks" e empresas de exemplo são conteúdo de demonstração das próprias páginas). Ignorei páginas cuja primeira dobra era foto de pessoa (ex.: depoimento do HubSpot, hero do Hootsuite) para evitar capturar rostos de terceiros.

## 3. APIs e integrações — atualização

Mudanças em relação à rodada anterior:

| site | bloqueio encontrado | tem API pública? | tem MCP / conector para IA? | tem RSS ou feed? | tem export ou embed? | autenticação | preço / plano necessário | o que dá para BUSCAR | limites e termos | serve por segmento? | verificação |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **UI Sources → ScreensDesign** | `uisources.com` redireciona para `screensdesign.com`; biblioteca e login | API REST: não verificado | **Sim**, MCP hospedado em `api.screensdesign.com/v1/mcp`, "incluído com o Pro"; funciona com Claude, Claude Code, Cursor, Codex, ChatGPT | não verificado | não verificado | não verificado (a página manda configurar pelo cliente) | Pro (valores: a página de preços não trouxe planos nem valores na leitura, "não verificado") | apps, telas gravadas, fluxos completos e screenshots da App Store, por significado (2.958+ apps do topo de faturamento, segundo a página); dados de receita e instalações; coleções salvas | a página cita "access secured and rate limited" sem os números; "não verificado" | **sim** (forte para app mobile; foco em apps de maior faturamento, o que cobre FIN e SAU, menos MPE/JUR — inferência) | página (https://screensdesign.com/mcp/) |
| **Godly → recent.design** | `godly.website` redireciona para `recent.design` | não verificado | não verificado | não verificado | não verificado | — | não verificado | galeria visual com filtros Web, Interface, Branding, Motion, Poster; abas Design, Launch Videos, Websites, App Screenshots, OG Images | não verificado | **parcial** (só navegação manual; vi apenas a tela inicial) | captura de tela da home |

Demais linhas da tabela: sem alteração (ver `rodada-10C.md`).

### Ranking atualizado: 5 melhores para buscar referências por programa a partir do Claude Code

1. **Refero MCP** — MCP remoto oficial, plano pago. Passo mínimo: assinar (Pro/Team/Lifetime) e adicionar `https://api.refero.design/mcp` com token.
2. **ScreensDesign MCP (novo)** — MCP hospedado, Pro. Passo mínimo: assinar o Pro e conectar `api.screensdesign.com/v1/mcp` pela página de configuração (a página diz ~2 minutos). Retorna telas reais, fluxos e receita por app.
3. **Mobbin MCP** — já instalado como conector aqui, mas exige plano Pro (US$ 10/mês, cobrança anual). Passo mínimo: ativar o plano na conta conectada.
4. **Pinterest API v5** — gratuita, Trial de 1.000 req/dia, requer aprovação. Passo mínimo: criar app no portal de desenvolvedores e gerar token OAuth. Utilidade para telas de UI: incerta (inferência).
5. **Land-book / SiteInspire (RSS)** — sem conta. Passo mínimo: ler `https://land-book.com/rss.xml` e `https://www.siteinspire.com/websites/feed`. Só novidades, sem filtro por segmento.

Recomendação (inferência): assinar UM dos três MCPs pagos por 1 mês e usar para fechar as 37 telas restantes de uma vez, em vez de continuar com capturas manuais.

### Sites sem integração oficial encontrada, e melhor acesso manual
- **Behance** (API fechada a novos clientes), **Dribbble** (API sem busca pública), **Awwwards** (sem feed na home), **Page Flows** (sem API/MCP encontrado), **recent.design** (não verificado), **Screenlane** (não verificado).
- Acesso manual mais eficiente: abrir cada página no Chrome e capturar em tela cheia; para Page Flows, o teste de 3 dias (botão "Try 3 Days" na home).

## 4. Fontes verificadas

Abertas nesta rodada: https://screensdesign.com/mcp/ (texto completo da página), https://screensdesign.com/ (home), https://recent.design/ (home, só captura de tela), https://screensdesign.com/pricing (a leitura automática retornou só metadados, sem planos), e as 11 páginas de produto das capturas (stripe.com/invoicing, pipedrive.com/en, buffer.com, klaviyo.com, semrush.com, mailchimp.com, beacons.ai, doctoralia.com.br, headspace.com, clio.com, jusbrasil.com.br). As demais fontes estão em `rodada-10C.md`.

Não verificado: preços do ScreensDesign, Refero e Page Flows; limites de uso do ScreensDesign MCP; termos de uso da maioria dos sites; API/feed do recent.design; Screenlane.
