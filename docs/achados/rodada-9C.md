# Rodada 9C — Inspiração e benchmarking (verificado em 22/11/2026)

## Resumo
- **Mobbin 🔒**: só a home é pública; toda a biblioteca (`/browse/ios/apps` → redireciona para login) exige conta. Não foi possível listar apps/categorias de referência sem login. A home informa 600 mil+ telas, seções Apps / Sites / Screens / Flows / Animations / UI Elements e MCP em planos Pro/Team.
- **Dribbble ⚠️**: tags e buscas abrem sem login, mas após ~20 aberturas seguidas de shots o site exibiu "Let's confirm you are human". Não contornei. Por isso só 4 shots (dashboard de criador) têm autor verificado; nas demais categorias há título + URL, com autor "não verificado".
- **Behance ✅**: busca "creator app ui ux" funciona sem login e traz projetos úteis (marketplaces criador × marca, monetização). Limite: "Log in to view more projects".
- **Awwwards / Land-book / SiteInspire ✅**: bons para landing e portfólio pessoal. Não servem para telas de app.
- **Coolors / Typewolf ✅**: Coolors tem contrast checker com regras WCAG; Typewolf tem lista "40 Best Google Fonts" (open source) e guia de pares. Os pares em si **não foram extraídos** (ver ficha).
- Lacuna: nenhuma referência de **telas mobile iOS** de agenda/CRM/mensagens foi verificada via Mobbin. Sugestão: o usuário abrir o Mobbin logado numa rodada à parte.
- Nenhum print foi salvo (ver seção Prints).

---

## Fichas dos sites

### Mobbin
- https://mobbin.com | status: 🔒 (home ✅; biblioteca exige login)
- O que é: biblioteca de referência de UI/UX com 600 mil+ telas de apps e sites; conteúdo organizado em Apps, Sites, Screens, Flows, Animations, UI Elements. Há plano Finance+ (60+ apps de finanças) em Team/Enterprise.
- Gratuito/pago: "Join for free" + planos (Pro/Team). Preços e limites do plano gratuito: não verificado. Integração MCP: apenas Pro e Team.
- Melhor uso: estudar fluxos de onboarding, agenda, mensagens, paywall e perfil em apps iOS reais; seção Animations para motion.
- Limitações: sem login não dá para listar apps por categoria. **Categorias pedidas (creator economy, portfólio, agenda, CRM, networking, mensagens, propostas, dashboards): não verificado.**

### Dribbble — tags
- https://dribbble.com/tags/ui-ux-inspiration | ✅ — "127 inspirational designs" (texto da página).
- https://dribbble.com/tags/ui-ux-design | ✅ — página abriu; a contagem de shots não ficou legível.
- O que é: portfólio de shots de designers; mistura apps, landing pages, anúncios (há cards "Advertise").
- Gratuito: navegação livre; banner de cookies não foi aceito. Login só para curtir/contato.
- Melhor uso: tendência visual de telas mobile e dashboards.
- Limitações: shots são imagens editadas, não telas reais; qualidade irregular; verificação anti-bot após muitas requisições.

### Behance
- https://www.behance.net | ✅ (home e busca sem login; "Log in or sign up to view more projects")
- O que é: plataforma Adobe de portfólios criativos (Projects, People, Assets, Images; filtro UI/UX).
- Melhor uso: estudos de caso completos (processo, várias telas) em vez de shots soltos.
- Limitações: muitos cases de estudantes com 1–10 apreciações; filtre por apreciações; há itens "PROMOTED".

### Awwwards
- https://www.awwwards.com | ✅ — Site of the Day em 22/11/2026: Artemii Lebedev (score 7.27/10). Seções: Websites, Directory, Academy, Jobs, Market.
- Melhor uso: landing e portfólio de serviço pessoal; motion e tipografia.
- Limitações: premia sites experimentais pesados, nem sempre aplicáveis a produto; várias áreas Pro/pagas (Academy, Creative Pass).

### Land-book
- https://land-book.com | ✅ — galeria curada diária de sites; filtros: Landing, Portfolio, Blog, Ecommerce, Other; abas Websites / Sections / Mobile / Motion / OG Images / Headlines.
- Melhor uso: padrões de seção (hero, pricing, case) para landing de serviço pessoal.
- Limitações: só web/landing; alguns itens são templates pagos.

### SiteInspire
- https://www.siteinspire.com | ✅ — filtros por Categories/Styles/Types/Subjects/Platforms. Categorias visíveis em 22/11/2026: Portfolio 1.449, Typographic 2.108, Minimal 861, Grid Layout 675 etc.
- Melhor uso: layouts editoriais e tipografia forte para portfólio.
- Limitações: acervo de sites, não de apps; muito conteúdo de agências.

### Coolors
- https://coolors.co | ✅ — gerador de paletas (10M+ paletas), extração de cores de imagem, preview em designs, Tailwind Colors, contrast checker. Pro/Sign in no topo; limites do plano grátis: não verificado.
- https://coolors.co/contrast-checker | ✅ — descreve WCAG: AA = 4,5:1 texto normal e 3:1 texto grande (≥18pt) ou negrito; AAA = 7:1 normal e 4,5:1 grande.
- Melhor uso: validar contraste de tokens de cor claro/escuro; gerar escala para Tailwind.
- Limitações: paleta bonita ≠ papéis semânticos de cor; exportar tokens exige conferência manual.

### Typewolf
- https://www.typewolf.com | ✅ — "What's Trending in Type": sites com as fontes usadas (ex.: Neue Montreal, Suisse Int'l, DM Sans, Switzer); listas "Top 40 Google Fonts", "Top 40 Adobe Fonts"; guias "Flawless Typography Checklist" e "The Definitive Guide to Free Fonts".
- https://www.typewolf.com/google-fonts | ✅ — "40 Best Google Fonts", atualizado em 12/01/2026; todas open source e livres para uso comercial, focadas em famílias com vários pesos.
- Tentei `/free-font-combinations` → **404** (URL inventada por mim; o guia correto é "The Definitive Guide to Free Fonts", URL não capturada). **Pares tipográficos recomendados: não extraídos.**
- Melhor uso: escolher fonte open source com vários pesos para PT/EN (verificar suporte a acentos na página de cada fonte: não verificado).
- Limitações: muitas fontes citadas na home são pagas (Neue Haas, Suisse, Canela, etc.); licença de app (embed em Capacitor) precisa ser lida em cada foundry.

---

## Referências concretas

### Dashboard de criador (Dribbble — autores verificados)
### Kreya – Content Creator Dashboard — Chandra Mudha Mahendra (VanguardCX)
- https://dribbble.com/shots/25294910-Kreya-Content-Creator-Dashboard | ✅ | Plataforma: web app
- Observar: hierarquia de métricas e cards. Telas: visão geral de conteúdo.
- Adaptar: usar como padrão de "Resultados" do painel do gestor, com seus próprios tokens.
- Riscos: shot estático; sem estados vazios/erro; não copiar layout nem identidade.

### Blenz | Influencer Analytics Dashboard UI — Wolfpixel UI/UX (Wolfpixel Agency)
- https://dribbble.com/shots/26534678-Blenz-Influencer-Analytics-Dashboard-UI | ✅ | web app
- Observar: organização de analytics por criador. Adaptar: aba de resultados por rede.
- Riscos: padrão de agência de influência, não de marca pessoal individual.

### Invoice / Proposal Creator — Amir Baqian (Ace Design)
- https://dribbble.com/shots/25532738-Invoice-Proposal-Creator | ✅ | web app
- Observar: fluxo de criação de proposta/fatura. Adaptar: módulo Propostas e Contratos.
- Riscos: conteúdo visto só pelo título e autor; detalhes de telas não analisados.

### Creator Brand & Content Management Mobile App — Erudite07
- https://dribbble.com/shots/27744939-Creator-Brand-Content-Management-Mobile-App | ✅ | iOS/Android (conceito)
- Observar: gestão de marca e conteúdo no mobile. Adaptar: home mobile do cliente.
- Riscos: conceito sem prova de uso; autor é perfil individual.

### Outros shots de dashboard (apareceram na busca "creator dashboard"; autor não verificado)
- Creator Analytics Dashboard — https://dribbble.com/shots/27669622-Creator-Analytics-Dashboard
- Creatora – Creator Management SaaS Dashboard — https://dribbble.com/shots/27784384-Creatora-Creator-Management-SaaS-Dashboard
- BLOOMIO Creator Analytics Mobile App UI — https://dribbble.com/shots/27669776-BLOOMIO-Creator-Analytics-Mobile-App-UI

### Criador × marca, monetização (Behance — autor da listagem)
- **Cook (Creator–Brand Deals App)** — Suhani Barai — https://www.behance.net/gallery/258614563/Cook-%28-CreatorBrand-Deals-App-%29 | ✅ | app. Observar: fluxo de propostas entre criador e marca. 23 apreciações; baixo validado.
- **Nomey — Creator Monetization Platform** — "Multiple Owners" — https://www.behance.net/gallery/254485187/Nomey-Creator-Monetization-Platform | ✅ | plataforma. Observar: monetização e pagamentos. 227 apreciações.
- **Reelful — AI Powered Social Video Creator App | UI/UX** — "Multiple Owners" — https://www.behance.net/gallery/253975015/Reelful-AI-Powered-Social-Video-Creator-App-UIUX | ✅ | app mobile. 405 apreciações. Observar: fluxo de criação de conteúdo.
- Riscos comuns: cases individuais não analisados tela a tela; copiar fluxo de marketplace não serve a um app de gestão.

### Portfólio / landing de serviço pessoal (sites)
- **Awwwards — Portfolio**: https://www.awwwards.com/websites/portfolio/ | ✅. Entradas vistas na URL (autor = nome no slug, não confirmado): `luis-bizarro-1`, `saho-birkar`, `anna-kurilets`, `daniel-neath-product-design-portfolio` (https://www.awwwards.com/sites/daniel-neath-product-design-portfolio). Observar: tipografia e hero; riscos: peso/animação excessiva para PWA.
- **Land-book** (listados na home em 22/11/2026): "Mayo — Fearless brand & product design" (Portfolio by Aron Mayo) e "Damian Fejdasz — AI-Native Product Designer" (Portfolio). URLs individuais não capturadas; ver https://land-book.com.
- **SiteInspire — categoria Portfolio**: https://www.siteinspire.com/websites?categories=5 | ✅ (confirmei "Portfolio 1.449" no filtro; a URL com `categories=5` abriu como listagem geral, então não garanto que o filtro tenha sido aplicado).

### Outras categorias no Dribbble (título e URL abertos na listagem de busca; **autor não verificado**, página do shot não aberta por bloqueio anti-bot)
| Categoria | Shot | URL |
|---|---|---|
| Portfólio | Personal Portfolio Website Design UIUX | https://dribbble.com/shots/25067767-Personal-Portfolio-Website-Design-UIUX |
| Portfólio | Personal Portfolio Landing Page | https://dribbble.com/shots/23742257-Personal-Portfolio-Landing-Page |
| Agenda | Calendar Booking App | https://dribbble.com/shots/26029349-Calendar-Booking-App |
| Agenda | Booking Calendar App | https://dribbble.com/shots/27286173-Booking-Calendar-App |
| CRM pessoal | CRM Mobile App | https://dribbble.com/shots/24243315-CRM-Mobile-App |
| CRM pessoal | CRM Mobile Design BizForce | https://dribbble.com/shots/27609091-CRM-Mobile-Design-BizForce |
| Mensagens | Mobile Chat UI | https://dribbble.com/shots/20762095-Mobile-Chat-UI |
| Mensagens | Customer Messaging Mobile App UI Talk Sense | https://dribbble.com/shots/27580119-Customer-Messaging-Mobile-App-UI-Talk-Sense |
| Onboarding | WanderWise Full Onboarding Flow | https://dribbble.com/shots/26343181-WanderWise-Full-Onboarding-Flow |
| Onboarding | Mobile Onboard | https://dribbble.com/shots/25197917-Mobile-Onboard |
| Perfil | Profile Page Freelance Marketplace UI Design | https://dribbble.com/shots/26673918-Profile-Page-Freelance-Marketplace-UI-Design |
| Perfil | Mobile App Design Freelance Platform for Busy People | https://dribbble.com/shots/26112146-Mobile-App-Design-Freelance-Platform-for-Busy-People-UX-UI |

Para todos: "o que observar / como adaptar" não foi analisado visualmente; tratar como lista de candidatos para revisão manual. Risco geral: shots de conceito, sem prova de uso real.

---

## Tabela: categoria × melhores referências verificadas

| Categoria | Referências (URL) | Confiança |
|---|---|---|
| Perfil | Dribbble Profile Page Freelance Marketplace (link acima) | baixa (autor/telas não verificados) |
| Portfólio | Awwwards Portfolio; SiteInspire (Portfolio); Land-book (Aron Mayo, Damian Fejdasz) | média |
| Agenda | Dribbble Calendar Booking App; Booking Calendar App | baixa |
| Propostas/contratos | Dribbble Invoice / Proposal Creator (Amir Baqian); Behance Cook (Suhani Barai) | média |
| Mensagens | Dribbble Mobile Chat UI; Talk Sense | baixa |
| Dashboard | Dribbble Kreya (Chandra Mudha Mahendra); Blenz (Wolfpixel); Behance Nomey | média |
| Onboarding | Dribbble WanderWise; Mobile Onboard | baixa |
| CRM / networking | Dribbble CRM Mobile App; BizForce; Behance Cocraft / Collabr (apareceram na busca, não abertos) | baixa |

---

## Fontes verificadas (URLs abertas)
- https://mobbin.com e https://mobbin.com/browse/ios/apps (redireciona a login)
- https://dribbble.com/tags/ui-ux-inspiration, https://dribbble.com/tags/ui-ux-design
- Buscas Dribbble: /search/creator-dashboard, personal-portfolio-app, booking-calendar-app, crm-mobile-app, messaging-app-ui, onboarding-mobile, freelancer-profile-app
- Shots abertos com autor: Kreya, Blenz, Invoice/Proposal Creator, Creator Brand & Content Management
- https://www.behance.net e a busca `creator app ui ux` (field ui/ux)
- https://www.awwwards.com e /websites/portfolio/
- https://land-book.com
- https://www.siteinspire.com e /websites?categories=5
- https://coolors.co e /contrast-checker
- https://www.typewolf.com, /google-fonts, /free-font-combinations (404)

## Prints
Capturados em 23/11/2026 (arquivos `.jpg`, pasta `prints-9C`). Os shots do Dribbble (Kreya, Blenz, Invoice/Proposal) **não têm print**: o site bloqueou com verificação humana e não contornei.

| nome | URL | o que mostra |
|---|---|---|
| 9C_coolors_contrast-checker_1.jpg | https://coolors.co/contrast-checker/112a46-acc8e5 | ferramenta de contraste: campos de cor, razão 8.42, nota por tamanho de texto |
| 9C_typewolf_google-fonts_1.jpg | https://www.typewolf.com/google-fonts | lista "40 Best Google Fonts" (open source, uso comercial) e nota de fontes boas para texto corrido |
| 9C_perfil-criador_nomey_1.jpg | https://www.behance.net/gallery/254485187/Nomey-Creator-Monetization-Platform | capa do case: tipografia grande, gradiente azul, tela mobile de perfil |
| 9C_perfil-criador_nomey_2.jpg | idem | card de perfil do criador (avatar, handle, 78 Reels, botão de assinatura) sobre grade de conteúdo |
| 9C_perfil-criador_nomey_3.jpg | idem | grade de vídeos com tab bar flutuante de 4 ícones e barra de navegador |
| 9C_propostas_cook_1.jpg | https://www.behance.net/gallery/258614563/Cook-%28-CreatorBrand-Deals-App-%29 | telas de onboarding e cards de campanha (valor, prazo) |
| 9C_propostas_cook_2.jpg | idem | tela "Brand Deals, Sorted" com cards de oferta |
| 9C_portfolio_awwwards-daniel-neath_1.jpg | https://www.awwwards.com/sites/daniel-neath-product-design-portfolio | portfólio de product design: título grande, navegação e hero |
| 9C_landing_land-book_1.jpg | https://land-book.com | abas (Websites, Sections, Mobile, Motion) e filtros por tipo de página; banner de cookies cobre parte |
| 9C_portfolio_siteinspire_1.jpg | https://www.siteinspire.com/websites | galeria e filtros por categoria (Portfolio, Typographic, Minimal etc.) |

Observações: o filtro `?categories=5` do SiteInspire redireciona para `/websites` sem filtro, então a ficha de SiteInspire deve usar essa URL. Os prints do Nomey e do Cook são de telas conceituais (Behance), não de apps em produção.
