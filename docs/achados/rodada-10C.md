# Rodada 10C — Galeria de referências visuais + APIs e integrações

Data da pesquisa: 27/11/2026. Parte 3 de 3. Somente leitura: nenhuma conta, plano ou chave de API foi criado.

## 1. Resumo

**Entrega parcial.** A meta de 60 telas NÃO foi atingida. Foram capturadas 12 telas em tamanho grande (1471 px de largura, texto legível): FIN 8 e CRM 4. PUB, MPE, SAU e JUR estão com 0 telas. Faltam 48 telas (FIN 2, CRM 6, e 10 em cada um dos outros quatro segmentos).
- Todas as capturas são de **website** (páginas públicas de produtos). Não há app desktop nem mobile ainda.
- As capturas são o viewport inteiro (não recortadas só na interface). Banners de cookies aparecem em algumas.
- Os dados de pessoas que aparecem (ex.: "John Ronan" no HubSpot) são exemplos fictícios das páginas de marketing. Nenhum dado real de terceiros foi capturado.
- Data de publicação: "não verificado" em todas (páginas de produto não trazem data).

**APIs (Parte 3.2):** as 13 fontes pedidas foram cobertas, mas com níveis de verificação diferentes (coluna "verificação" na tabela). Principais achados:
1. **Mobbin** tem MCP, mas só a partir do plano Pro (US$ 10/mês, cobrança anual). Neste ambiente o conector Mobbin já está instalado, mas as buscas retornaram "Mobbin MCP requires a paid plan". Não fiz upgrade.
2. **Refero** tem MCP remoto oficial (`https://api.refero.design/mcp`), exige plano pago (Pro, Team ou Lifetime).
3. **Behance** fechou a API pública para novos clientes.
4. **Dribbble** tem API v2 com OAuth, mas nos docs só apareceram `/user` e `/user/shots` (sem busca por palavra-chave).
5. **Land-book** e **SiteInspire** têm feed RSS (sem busca por segmento).
6. **Pinterest** tem API v5 gratuita, com acesso Trial (1.000 req/dia) e aprovação necessária.

**O que não foi possível verificar** (marcado "não verificado"): Screenlane (página não abriu), Godly e UI Sources (a ferramenta de leitura bloqueou a inspeção das páginas; ambos redirecionam para outros domínios, ver nota), termos de uso de vários sites, e preços de Page Flows e Land-book além do que a página mostrou.

---

## 2. Galeria por segmento

Convenção: arquivos em `10C/<SEG>/10C_<SEG>_<produto>_<tela>_<n>.png`. Os arquivos são PNG convertidos de capturas JPEG do navegador.

### FIN — Financeiro (8 de 10)

| arquivo | nome sugerido | segmento | plataforma | produto/autor | URL exata | tipo de tela | componentes (nome sugerido) | o que observar | como adaptar sem copiar | data de publicação |
|---|---|---|---|---|---|---|---|---|---|---|
| 10C_FIN_wise_home-hero_1.png | Hero tipográfico com prova social de lojas | FIN | website | Wise | https://wise.com/br/ | home | selos de nota das lojas (`store-rating-badges`), título gigante condensado, CTA pílula | contraste verde-lima sobre verde-escuro; promessa numérica (1,1% IOF) logo no subtítulo | usar tipografia de impacto + um número verificável no subtítulo, com a paleta do projeto | não verificado |
| 10C_FIN_wise_selos-confianca-regulacao_1.png | Faixa de 3 selos de confiança | FIN | website | Wise | https://wise.com/br/ | home (seção de confiança) | cartão com chip (`card-visual`), pílula de conversão de moedas (`currency-pill`), faixa de 3 selos: volume, regulação (Banco Central), suporte 24/7 (`trust-strip`) | regulação citada com link para o órgão; ícones de linha simples; 3 colunas | faixa de 3 provas (volume, regulação, suporte) com ícones próprios e linguagem do segmento | não verificado |
| 10C_FIN_stripe_checkout-pagamento_1.png | Checkout com plano e resumo | FIN | website | Stripe | https://stripe.com/payments | formulário de pagamento (mock) | seletor de plano radio (`plan-radio`), abas de método de pagamento (`payment-method-tabs`), campos de cartão com bandeiras, resumo do plano com checklist e total (`order-summary`) | duas colunas: escolha à esquerda, resumo à direita; botão desabilitado até preencher | manter a estrutura escolha+resumo, mudar grid, cores e rótulos | não verificado |
| 10C_FIN_mercury_home-aviso-regulatorio_1.png | Aviso regulatório fixo no rodapé do viewport | FIN | website | Mercury | https://mercury.com/ | home | faixa de aviso regulatório "não é banco" (`regulatory-notice`), banner de consentimento (`cookie-consent`), campo de e-mail + CTA (`email-cta`) | o aviso legal é visível sem rolagem, em texto curto, acima do cookie | posicionar aviso regulatório obrigatório de forma fixa e legível, adaptado à regulação local | não verificado |
| 10C_FIN_ramp_home-dashboard-ia_1.png | Home com contadores ao vivo e mock de produto | FIN | website | Ramp | https://ramp.com/ | home | contador ao vivo no topo (`live-counter`), barra inferior de métricas em tempo real (`agent-ticker`), mock de recibo + cartão (`product-mock`) | números rolando dão sensação de produto "vivo"; fundo pontilhado discreto | métricas ao vivo/estimadas do próprio produto em uma faixa inferior | não verificado |
| 10C_FIN_stripe-billing_planos-precos-cards_1.png | Cards de planos com selo "melhor valor" | FIN | website | Stripe Billing | https://stripe.com/billing | preços / planos (mock em janela de navegador) | janela de navegador falsa (`browser-frame`), 3 cards de plano, etiqueta "Best value" (`value-badge`), checklist por plano | destaque do plano do meio por barra superior colorida + etiqueta | destacar um plano com barra e etiqueta, sem copiar nomes/layout | não verificado |
| 10C_FIN_wise_precos-transparentes_1.png | Página de preços por serviço | FIN | website | Wise | https://wise.com/br/pricing/ | preços | título de promessa, cartão branco arredondado por serviço (`service-price-card`) com seta de ação | preço por uso, sem planos; cartão grande com raio alto sobre fundo cheio | lista de preços por serviço em cartões largos com CTA circular | não verificado |
| 10C_FIN_monzo_home-selos-protecao_1.png | Hero com selos de proteção e prêmio | FIN | website | Monzo | https://monzo.com/ | home | selo de prêmio "Which? Recommended" (`award-seal`), selo de proteção FSCS (`protection-seal`), banner de cookies (`cookie-consent`), foto com cartão no celular | selos no canto inferior direito do hero; cookie com 3 opções (aceitar/rejeitar/personalizar) | posicionar selos reais e verificáveis no hero; só usar selo que o projeto tenha direito | selo marcado "November 2026" |

### CRM (4 de 10)

| arquivo | nome sugerido | segmento | plataforma | produto/autor | URL exata | tipo de tela | componentes (nome sugerido) | o que observar | como adaptar sem copiar | data de publicação |
|---|---|---|---|---|---|---|---|---|---|---|
| 10C_CRM_hubspot_home-card-contato_1.png | Card de contato com ações rápidas e menu | CRM | website | HubSpot | https://www.hubspot.com/products/crm | home de produto | card de contato (`contact-card`), botões de ação Nota/E-mail/Ligação/Tarefa (`quick-actions`), menu de contexto com "Summarize with AI" (`context-menu`), selo G2 Leader (`award-badge`) | fundo escuro, ações em ícones com rótulo; IA integrada ao menu | card de contato com ações rápidas em linha | selo "Summer 2026" |
| 10C_CRM_pipedrive_home-hero-confianca_1.png | Hero com linha de confiança | CRM | website | Pipedrive | https://www.pipedrive.com/en | home | título central, 2 CTAs (primário amarelo / secundário claro), linha de confiança: nota Capterra, "sem cartão", SOC 2 & GDPR (`trust-line`), banner de cookies | selos de conformidade em linha pequena sob os CTAs | linha de confiança de 3 itens sob o CTA principal | não verificado |
| 10C_CRM_attio_home-workspace-ia_1.png | Mock de app com prompt de IA | CRM | website (mock de app desktop) | Attio | https://attio.com/ | home / produto | janela de app com sidebar (`app-sidebar`), saudação + caixa de prompt (`ai-prompt-box`), atalho de ações rápidas (`quick-actions-bar`) | mock de app desktop dentro do site mostra o produto real na primeira dobra | mostrar o app com a pergunta de IA como centro, adaptando sidebar e conteúdo | não verificado |
| 10C_CRM_rd-station-crm_home-funil-kanban_1.png | Funil kanban com checklist de IA | CRM | website | RD Station CRM | https://www.rdstation.com/crm/ | home de produto | funil em colunas/kanban (`pipeline-kanban`), cartão de vídeo com transcrição (`call-transcript`), ícones de integrações em coluna (`integration-rail`), checklist de IA (`ai-checklist`) | integrações (WhatsApp, Meet, Teams) mostradas como coluna de ícones; PT-BR | trilho de integrações + funil, com linguagem e cores próprias | não verificado |

### PUB — Publicidade (0 de 10)
Não capturado nesta rodada. Alvos sugeridos: páginas públicas de Google Ads, Meta Ads e TikTok Ads, estudos de caso no Behance/Dribbble.

### MPE — Marca pessoal (0 de 10)
Não capturado. Alvos sugeridos: Linktree, Beacons, about.me, portfólios no Behance/Awwwards.

### SAU — Saúde (0 de 10)
Não capturado. Alvos sugeridos: Doctoralia, Headspace, One Medical, capturas oficiais de App Store/Google Play.

### JUR — Jurídico (0 de 10)
Não capturado. Alvos sugeridos: Clio, Jusbrasil, Rocket Lawyer, DocuSign.

**Limitação da ferramenta:** o shell do ambiente não tem acesso à rede. As imagens só puderam ser obtidas por captura de tela do navegador (viewport), então não foi possível baixar imagens originais de lojas ou de sites de galeria.

---

## 3. APIs e integrações dos sites de referência

Legenda da coluna "verificação": **doc** = li a documentação oficial; **página** = li só a página pública; **terceiros** = a informação vem de fontes não oficiais (tratar como inferência); **não verificado**.

| site | bloqueio encontrado | tem API pública? | tem MCP / conector para IA? | tem RSS ou feed? | tem export ou embed? | autenticação | preço / plano necessário | o que dá para BUSCAR | limites e termos relevantes | serve por segmento? | verificação |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Mobbin** | Buscas via MCP retornaram "requires a paid plan" neste ambiente | Sim, só em Team e Enterprise (página de preços) | Sim (MCP oficial, plano Pro ou acima); conector já instalado aqui | não verificado | Export ("Copy & download") limitado no Free, incluído nos pagos | conector OAuth (via claude.ai) | Free sem MCP/API; Pro US$ 10/mês (anual); Team US$ 16/membro/mês (anual); Enterprise sob consulta | telas, fluxos e seções por linguagem natural, plataforma ios/web (descrição das ferramentas) | URLs de imagem expiram em 30 dias (descrição da ferramenta); termos não verificado | **sim** (com plano pago) | doc (https://mobbin.com/pricing) + resposta da ferramenta |
| **Dribbble** | não verificado (não testei navegação anônima) | Sim, API v2 em `api.dribbble.com/v2/` | não verificado | não verificado | não verificado | OAuth 2 (Bearer ou `access_token`) | não verificado | só `/user` e `/user/shots` apareceram na doc; busca por palavra-chave: não encontrado | 60 req/min e 1.440 req/dia por usuário; 429 ao exceder; "Terms & Guidelines" citados, conteúdo não verificado | **não** (não busca shots públicos) | doc (https://developer.dribbble.com/v2/) |
| **Behance** | Programa de API fechado | **Não** para novos clientes ("no longer accepting new clients") | não verificado | não verificado | não verificado | não verificado | — | — | — | **não** | doc (https://www.behance.net/dev) |
| **Awwwards** | Nenhum bloqueio visto na home | não encontrado | não verificado | não encontrado no `<head>` da home | não encontrado | — | não verificado | navegação manual (Latest, Nominees, Collections, Directory) | termos em https://www.awwwards.com/terms/ (conteúdo não lido) | **parcial** (só manual) | página |
| **Land-book** | A leitura automática por WebFetch falhou; no Chrome abriu normalmente | não encontrado | não verificado | **Sim**: `https://land-book.com/rss.xml` e `https://land-book.com/feed/` | não verificado | nenhuma | Banner na home: PRO US$ 72 → US$ 50/ano (promoção "Black Weeks"); o que o PRO libera: não verificado | itens recentes do feed (sites), não por segmento | termos em https://land-book.com/terms-of-service (conteúdo não lido) | **parcial** (feed de novidades) | página (Chrome) |
| **SiteInspire** | Nenhum bloqueio visto; há login/"Subscribe" | não encontrado | não verificado | **Sim**: `https://www.siteinspire.com/websites/feed` | não encontrado | nenhuma (feed) | não verificado | novos sites publicados (feed) | não verificado | **parcial** | página (Chrome) |
| **Pinterest** | Aprovação do app necessária; novos apps começam em Trial | **Sim**, API v5 (`https://developers.pinterest.com/docs/api/v5/`) | não verificado | não verificado | não verificado | OAuth 2 | Gratuita (Trial e Standard) | busca de pins por palavra-chave existe segundo documentação de terceiros (`GET /v5/search/pins`); não confirmada na doc oficial que consegui abrir; uma discussão da comunidade cita o endpoint `search/partner/pins` com acesso restrito | Trial: 1.000 req/dia; Standard: 100 req/s por usuário por app (doc de rate limits); limites mudam sem aviso | **parcial** (inferência: pins de inspiração, sem garantia de telas de UI) | doc (https://developers.pinterest.com/docs/reference/ratelimits/) + terceiros |
| **Figma Community** | — | REST API oficial (https://developers.figma.com/docs/rest-api/); busca de arquivos da Community por palavra-chave: não encontrado | **Sim**: servidor MCP oficial (remoto `https://mcp.figma.com/mcp`) | não verificado | não verificado | token de acesso pessoal ou OAuth 2 | MCP depende de plano/assento: Enterprise Full/Dev até 600 chamadas/dia; Pro/Org Full/Dev até 200/dia; View/Collab até 6/mês (docs de MCP) | ler arquivos/frames que você indicar por link; não busca a Community | limites por minuto (10–20/min conforme plano, segundo terceiros); Developer Terms | **parcial** (lê o que você já escolheu) | doc (https://developers.figma.com/docs/figma-mcp-server/plans-access-and-permissions) |
| **Refero** | Plano pago para MCP | MCP; API REST: não verificado | **Sim**, MCP remoto oficial `https://api.refero.design/mcp` | não verificado | não verificado | OAuth ou Bearer token (conforme ferramenta) | Pro, Team ou Lifetime (preços: não verificado) | telas e fluxos (125.000+ telas e 8.000+ fluxos, segundo o post de lançamento no Product Hunt, não confirmado em doc) | não verificado | **sim** | doc (https://doc.refero.design/mcp/getting-started.md) |
| **Screenlane** | A página não abriu na leitura automática; no Chrome a navegação não pôde ser confirmada | não verificado | não verificado | não verificado | não verificado | — | não verificado | — | — | não verificado | não verificado |
| **Page Flows** | Assinatura (botão "Try 3 Days"); fluxos em vídeo | não encontrado | não encontrado (nem no registro oficial de MCP, segundo comparação de terceiros) | não encontrado | "Importing & Exporting" aparece só como categoria de fluxos | login | https://pageflows.com/pricing/ (valores não lidos) | fluxos iOS, Android, web e e-mails (navegação manual) | https://pageflows.com/terms/ (não lido) | **parcial** (manual, pago) | página (Chrome) |
| **Godly** | `godly.website` redireciona para `recent.design`; a ferramenta bloqueou a inspeção da página | não verificado | não verificado | não verificado | não verificado | — | não verificado | — | — | não verificado | não verificado |
| **UI Sources** | `uisources.com` redireciona para `screensdesign.com`; inspeção bloqueada | não verificado | não verificado | não verificado | não verificado | — | não verificado | — | — | não verificado | não verificado |

Nota: Godly e UI Sources apontam para outros domínios. Não confirmei se são o mesmo produto renomeado ou outro serviço. A inspeção em `recent.design` e `screensdesign.com` ficou pendente.

### Ranking: 5 melhores opções para buscar referências por programa a partir do Claude Code

1. **Refero MCP.** É a única opção oficial pensada para agentes, com busca de telas e fluxos em linguagem natural e suporte declarado ao Claude Code. Passo mínimo: assinar um plano pago (Pro, Team ou Lifetime), e depois rodar o comando da doc: `claude mcp add --transport http refero https://api.refero.design/mcp --header "Authorization: Bearer <token>"` (token obtido na conta Refero). Nada disso foi feito aqui.
2. **Mobbin MCP.** Maior acervo de telas e fluxos de apps reais, com busca por plataforma. Já está instalado como conector neste ambiente. Passo mínimo: ativar o plano Pro (US$ 10/mês, cobrança anual) na conta usada no conector. Sem isso, as buscas falham (confirmado aqui).
3. **Pinterest API v5.** Gratuita, mas exige criar um app e aguardar aprovação em Trial (1.000 req/dia). Passo mínimo: criar o app no portal de desenvolvedores, solicitar acesso e gerar o token OAuth. Serve para inspiração visual geral. Para telas de UI por segmento a utilidade é incerta (inferência).
4. **Land-book via RSS.** Sem conta nem chave. Passo mínimo: ler `https://land-book.com/rss.xml` por script. Só traz novidades, sem filtro por segmento (inferência: dá para filtrar por palavras-chave nos títulos).
5. **SiteInspire via RSS.** Mesmo caso: ler `https://www.siteinspire.com/websites/feed`, sem autenticação. Só traz novidades.

Complemento fora do ranking: **Figma MCP** não busca na Community, mas lê qualquer arquivo ou frame que você apontar por link. Passo mínimo: conectar `https://mcp.figma.com/mcp` (requer assento Dev/Full em plano pago para uso confortável).

### Sites sem integração oficial encontrada e melhor acesso manual

- **Behance:** API fechada para novos clientes. Acesso manual mais eficiente: abrir páginas de projeto/"Moodboards" no Chrome e capturar telas em tamanho grande.
- **Dribbble:** API existe mas não busca shots públicos (conforme a doc lida). Acesso manual: busca por termo no site, abrindo cada shot em tamanho grande.
- **Awwwards:** sem API/feed encontrado. Acesso manual: coleções e "Nominees" no site.
- **Page Flows:** sem API/MCP encontrado. Acesso manual: assinar o teste de 3 dias e explorar por categoria (inferência).
- **Screenlane, Godly, UI Sources:** não verificado. Acesso manual: navegar no site.

---

## 4. Fontes verificadas

Abertas e lidas nesta rodada:
- https://mobbin.com/pricing (preços e inclusão de MCP/API)
- https://developer.dribbble.com/v2/ (API v2, limites)
- https://www.behance.net/dev (API fechada a novos clientes)
- https://developers.figma.com/docs/rest-api/ (autenticação)
- https://developers.figma.com/docs/figma-mcp-server/plans-access-and-permissions (limites do MCP)
- https://developers.pinterest.com/docs/reference/ratelimits/ e https://developers.pinterest.com/docs/key-concepts/access-tiers/ (Trial/Standard)
- https://doc.refero.design/mcp/getting-started.md (MCP, plano pago, URL do servidor)
- Páginas abertas no Chrome: land-book.com (RSS), siteinspire.com (feed), awwwards.com (termos), pageflows.com (preços/termos)
- Páginas de produto das capturas: wise.com/br/, wise.com/br/pricing/, stripe.com/payments, stripe.com/billing, mercury.com, ramp.com, monzo.com, hubspot.com/products/crm, pipedrive.com/en, attio.com, rdstation.com/crm/

Fontes de terceiros (tratar como inferência): Product Hunt (Refero MCP, volume de telas), descrição de `GET /v5/search/pins` (jentic.com), comunidade Pinterest, comparação Page Flows × Screenlane.

Não verificado: termos de uso completos de todos os sites; preços de Refero, Page Flows; Screenlane, Godly, UI Sources.
