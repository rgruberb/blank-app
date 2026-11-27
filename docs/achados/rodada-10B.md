# Rodada 10B — Camada de skills por segmento (Parte 2 de 3)

> Status: **COMPLETO (3 de 3):** 6 fichas, tabela comparativa e fontes verificadas.
> Data da coleta: 27/11/2026. Método: cada site foi aberto no Chrome; os hex abaixo são cores computadas (`getComputedStyle`) das páginas abertas, contadas por número de elementos. Hex de marca mostrados em páginas de marketing podem diferir do produto logado (não medido: exige conta).
> Legenda: ✅ aberto e lido · 🔒 aberto, mas o conteúdo útil não renderizou/exige login · ❌ URL não existe ou foi descartada · "(inferência)" = conclusão minha, não está no texto da fonte.
> Limite assumido: não abri nenhum produto logado (regra "não crie conta"), então telas internas de apps (saldo, extrato, pipeline) vêm de páginas públicas, design systems e, quando indicado, de resultados de busca.

## Resumo

- **FIN**: confiança vem de precisão e transparência de custo. Cor de marca só em ação; texto quase preto sobre branco. Regra-chave: CET (Res. CMN 4.881/2020) e LGPD.
- **CRM**: trabalho diário, densidade alta, neutros frios, cor só para estado e ação. Referência de densidade: Linear (escuro) e Attio (claro). Regra-chave: LGPD.
- **PUB**: ferramenta densa e neutra; criativo expressivo. Regra-chave: anúncio identificável (CONAR art. 28, CDC art. 36). Especificações da Meta verificadas.
- **MPE**: o único segmento em que a personalidade da pessoa manda; densidade baixa, motion tolerante. Bento e Read.cv indisponíveis.
- **SAU**: calma e legibilidade (corpo 19px/16px no NHS). Dado de saúde é sensível (LGPD art. 5º II) e exige consentimento destacado (art. 11, I). CFM lido só por notícias.
- **JUR**: sobriedade e clareza (GOV.UK). Provimento 205/2021 restringe preço, promessa de resultado, logotipo da OAB e ostentação. Tipos de assinatura: Lei 14.063/2020.
- **Limites:** nenhum produto logado foi aberto; vários textos de norma só foram vistos em busca (marcados 🔒).

---

## Segmento: Financeiro (código: FIN)

### 1. Tom e personalidade visual
- Adjetivos: preciso, calmo, transparente, confiável; fintechs de varejo somam "acessível" e "amigável" (Nubank, Wise).
- O usuário espera sentir que o número está certo, que o dinheiro está seguro e que nada será cobrado sem aviso. (inferência, apoiada no tom das páginas abertas e na NN/g abaixo)
- NN/g (via busca, página não aberta por completo): "Trustworthiness in Web Design: 4 Credibility Factors" parte de 1999 de Nielsen e afirma que os fatores de confiança são estáveis ao longo dos anos; o primeiro passo é parecer legítimo e profissional.

### 2. Paleta típica (hex medidos)
| Produto | Cores medidas (hex, nº de elementos) | URL medida |
|---|---|---|
| Nubank | fundo/ação `#8D0DE3` (48 fundos), `#5D0599`, `#1E002F`; bege `#F3EFE6`; texto `#000000`; lilás claro `#ECDFFF` | https://nubank.com.br |
| Stripe | ação/links `#533AFD`; texto `#061B31`, `#50617A`, `#64748D`; superfícies `#E5EDF5`, `#F8FAFD`; `#7F7DFC` | https://stripe.com/br |
| Wise | verde `#9FE870` (38 fundos); verde-escuro `#163300`; texto `#0E0F0C`, `#454745`; superfície `#E8EBE6` | https://wise.com/br/ |
| Revolut | texto `#1F1F1F`; escuros `#191C1F`, `#000000`; cinzas `#C9C9CD`, `#717173`; `#F7F7F7` | https://www.revolut.com/en-BR/ |
| Inter | laranja `#FF7A00` (e `#EA7100`); texto `#161616`; cinzas `#E6E4E4`, `#747684` | https://inter.co/ |
| Itaú | laranja `#FF6200`; preto `#000000`; azul-marinho `#000066`; cinzas `#3B3B3B`, `#F1F2F4`, `#CFD1D3` | https://www.itau.com.br/ |

- Padrão observado: fundo branco ou quase branco, texto quase preto, **uma** cor de marca para ação.
- Cores a evitar (inferência): vermelho e verde puros como único sinal de perda/ganho (daltonismo; ver item 10); cores de marca saturadas como fundo de áreas com muito número.

### 3. Tipografia típica
- Famílias medidas: Nubank `nuSansText`/`nuSansDisplay`; Stripe `sohne-var`; Wise `Inter` (corpo) + `Wise Sans`; Revolut `Inter` + `Aeonik Pro`; Inter `Inter` + `Citrina`; Itaú `Itau Text`/`Itau Display`.
- Padrão: sans-serif geométrica/neutra, com família própria para títulos (display) e uma neutra para texto.
- Números tabulares (`font-variant-numeric: tabular-nums`) e tamanhos mínimos: **não verificado** nas páginas abertas. Recomendação (inferência): tabular em todo valor alinhado em coluna; corpo mínimo 16px no mobile.

### 4. Densidade
- **Média-baixa no varejo** (Nubank, Wise, Revolut: uma ação por tela, muito espaço); **média-alta em painel de negócios** (Stripe Dashboard: tabelas e filtros). Motivo: no varejo o medo é errar uma transferência; no B2B o usuário compara muitas linhas. (inferência)
- Stripe Apps limita de propósito a personalização visual para manter consistência e contraste de acessibilidade (https://docs.stripe.com/stripe-apps/design ✅).

### 5. Motion
- Aceitável: transições curtas de estado, confirmação de sucesso, carregamento de saldo.
- Nunca animar (inferência): valores monetários em contagem decrescente/crescente em telas de confirmação, botão de confirmar pagamento que se move, avisos de custo/risco.
- Não verificado: durações medidas nos produtos.

### 6. Padrões de tela essenciais
- Conta/saldo com extrato; transferência/Pix com tela de **confirmação com resumo**; simulação de crédito com CET; carteira/rentabilidade; cartão (fatura, limite); segurança (https://nubank.com.br abre com bloco "Segurança é prioridade" com "Me roubaram" e "Canal de Denúncias" ✅).
- Stripe Dashboard: superfícies Home, páginas de lista (Pagamentos, Clientes) e páginas de detalhe de objeto (https://docs.stripe.com/stripe-apps/design ✅).
- Revolut: poupança com rendimento atrelado ao CDI, "paga diariamente", com aviso "taxa variável" na mesma seção (https://www.revolut.com/en-BR/ ✅).

### 7. Dados e números
- Valor em R$ com separador brasileiro, sempre 2 casas; taxas em % a.a. **e** a.m. quando for crédito; moeda estrangeira com a moeda explícita.
- **CET**: percentual anual que inclui todos os encargos; norma vigente Res. CMN 4.881/2020 (ver item 9).
- **Rentabilidade**: o exemplo real da Sicredi traz "rentabilidade passada não representa garantia de rentabilidade futura", período mínimo de 12 meses para avaliação, e diz que a rentabilidade é líquida de taxas mas não de impostos; mostra a **data da cota** (ex.: 29/07/2026) junto aos números (https://www.sicredi.com.br/site/previdencia/individual/tabela-de-rentabilidade-pf/, texto lido em resultado de busca).
- Regra de produto (inferência): todo número com data e fonte; variação com sinal (+/−) além da cor; "taxa variável" sempre rotulada.

### 8. Confiança e credibilidade
- NN/g, "Hierarchy of Trust": 5 níveis de comprometimento; o site precisa atender necessidades básicas de confiança antes de pedir dados (https://www.nngroup.com/articles/commitment-levels/ — texto lido via busca).
- NN/g, "Prominence-Interpretation Theory": pedir demais cedo perde confiança (https://www.nngroup.com/articles/prominence-interpretation-theory/ — via busca).
- Sinais na tela: aviso de segurança/proteção visível (Nubank), "proativo" contra fraude (Revolut Secure, citado na home), número de clientes (Nubank "130 milhões", Revolut "80+ milhões"), regulador e garantia (FGC) onde couber. (a parte FGC: apenas inferência)

### 9. Regulação e conformidade que afetam a interface
| Regra | Órgão | URL | O que muda na tela |
|---|---|---|---|
| Res. CMN 4.881, de 23/12/2020: cálculo e informação do CET em operações de crédito e arrendamento mercantil financeiro. Art. 9º: não se aplica a repasses de recursos externos e crédito rural. | CMN/Banco Central | https://www.bcb.gov.br/content/estabilidadefinanceira/especialnor/Resolu%C3%A7%C3%A3o4881.pdf (texto visto em resultado de busca) | Mostrar o CET em % ao ano na oferta/contratação (inferência de aplicação). |
| Res. CMN 3.517/2007: **REVOGADA** a partir de 1/2/2021 pela 4.881/2020 | Banco Central | https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o&numero=3517 ✅ | Não usar como base; só histórica. |
| Res. CVM 175/2022 (fundos): contém seção "Material de Divulgação" | CVM | https://conteudo.cvm.gov.br/legislacao/resolucoes/resol175.html (visto em busca; **texto do artigo não lido**) | Conteúdo exato sobre rentabilidade em material de divulgação: **não verificado**. |
| Lei 13.709/2018 (LGPD), art. 6º (princípios: finalidade, adequação, necessidade…), art. 8º (consentimento por escrito deve constar de cláusula destacada; ônus da prova é do controlador), art. 9º (acesso facilitado, informação clara, adequada e ostensiva), art. 18 (direitos do titular: confirmação, acesso, correção, eliminação, portabilidade…) | Congresso/ANPD | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm ✅ | Aviso de privacidade claro, consentimento destacado, tela para o titular exercer direitos. |
- Anbima: citada no briefing; **não consegui abrir norma específica de exibição de rentabilidade**: não verificado.
- Procon/CDC art. 54-B (CET sintetizado em % ao ano): citado por artigo do Conjur (https://www.conjur.com.br/2025-jun-18/a-protecao-dos-consumidores-na-regulacao-bancaria/), fonte secundária; texto do CDC não aberto.

### 10. Acessibilidade específica do público
- Público amplo, inclui idosos e baixa literacia financeira (inferência). Contraste alto em valores; não depender só de cor para ganho/perda; alvos de toque grandes em confirmação; linguagem simples para taxas e siglas (CET, CDI, a.a.).
- Evidência verificada: Stripe limita cores justamente por contraste (item 4). Medições de contraste dos produtos: **não verificado**.

### 11. Anti-padrões e dark patterns
- Apenas o que as fontes sustentam: NN/g (Prominence-Interpretation): pedir informação demais cedo. UXDA tem artigo "Dark Patterns in Banking UX and the Erosion of Financial Brand Trust" (título visto em busca; não lido).
- Inferência: esconder tarifa/CET após o botão principal; pré-selecionar seguro/upsell; "rentabilidade" sem data nem período; botão de cancelar escondido; contagem regressiva falsa; cor vermelha do CTA igual a de alerta.

### 12. Diferenças por plataforma
| | Website | App desktop | App mobile |
|---|---|---|---|
| FIN | institucional + captação (CPF no topo, Nubank) | painel de negócio, tabela e exportação (Stripe Dashboard) | fluxo curto, uma decisão por tela, biometria (inferência) |

### 13. Direções visuais possíveis
1. **"Sóbrio institucional"** — fundo branco/`#F1F2F4`, texto `#000`/`#3B3B3B`, acento único `#FF6200` ou azul `#000066` (Itaú); tipografia de família própria + neutra; densidade média; motion mínimo. Fontes: itau.com.br.
2. **"Fintech moderna"** — branco + cor de marca saturada em CTA (`#8D0DE3` Nubank, `#533AFD` Stripe); sans geométrica; densidade baixa; motion suave de estado. Fontes: nubank.com.br, stripe.com/br.
3. **"Verde confiança"** — `#9FE870` sobre `#163300`, texto `#0E0F0C`; Inter; transparência de taxa como mensagem central. Fonte: wise.com/br.
4. **"Preto premium"** — `#191C1F`/`#1F1F1F` com cinzas `#C9C9CD`; Inter + display; densidade média. Fonte: revolut.com.

### 14. Componentes característicos
- Card de saldo com variação · Linha do extrato com data e status · Resumo de confirmação de transferência · Quadro de custo (CET, taxa a.m./a.a., total a pagar) · Selo de rentabilidade com data da cota e aviso · Alerta de segurança/fraude · Seletor de período (12/24/36 meses) · Gerenciador de consentimento e direitos LGPD.

### 15. Referências verificadas
| nome | URL | tipo | o que aproveitar | status |
|---|---|---|---|---|
| Stripe Apps — Design | https://docs.stripe.com/stripe-apps/design | design system (docs) | superfícies, anatomia, limite de cor por contraste | ✅ |
| Stripe Brasil | https://stripe.com/br | produto | paleta/tipografia | ✅ |
| Wise (site BR) | https://wise.com/br/ | produto | paleta/tipografia | ✅ |
| Wise Design | https://wise.design | design system/portfólio | página só com menu (sem conteúdo útil) | 🔒 |
| Nubank | https://nubank.com.br | produto | paleta, bloco de segurança | ✅ |
| Revolut BR | https://www.revolut.com/en-BR/ | produto | poupança/CDI com aviso, paleta | ✅ |
| Inter | https://inter.co/ | produto | paleta/tipografia | ✅ |
| Itaú | https://www.itau.com.br/ | produto | paleta/tipografia | ✅ |
| Res. CMN 3.517 (revogada) | link no item 9 | regulação | prova de revogação | ✅ |
| Res. CMN 4.881 (PDF BCB) | link no item 9 | regulação | CET | 🔒 (texto visto só em busca) |
| LGPD | link no item 9 | regulação | arts. 6, 8, 9, 18 | ✅ |
| Res. CVM 175 | link no item 9 | regulação | seção de material de divulgação | 🔒 |
| NN/g Trustworthiness | https://www.nngroup.com/articles/trustworthy-design/ | pesquisa | 4 fatores de credibilidade | 🔒 (via busca) |
| NN/g Hierarchy of Trust | https://www.nngroup.com/articles/commitment-levels/ | pesquisa | 5 níveis | 🔒 (via busca) |
| NN/g (URLs que chutei) /articles/trustworthiness/ e /trust-web-design/ | — | — | 404 | ❌ |
| Sicredi tabela de rentabilidade | https://www.sicredi.com.br/site/previdencia/individual/tabela-de-rentabilidade-pf/ | produto | aviso de rentabilidade passada | 🔒 (via busca) |
| Anbima (norma de rentabilidade) | — | regulação | não localizada | ❌ |
| Design system público Nubank/Itaú/Inter | — | design system | não localizei página pública; **não verificado** | ❌ |

---

## Segmento: CRM (código: CRM)

### 1. Tom e personalidade visual
- Adjetivos: eficiente, denso, neutro, rápido, previsível. O usuário espera sentir controle e velocidade em trabalho repetitivo. (inferência, baseada nas páginas abertas)
- Linear apresenta tema escuro por padrão (fundo `#0F1011`/`#08090A`, texto `#F7F8F8`).

### 2. Paleta típica (hex medidos)
| Produto | Cores medidas | URL |
|---|---|---|
| HubSpot | laranja `#FF4800`; verde-escuro `#061C1D`, `#124548`; texto `#1F1F1F`; fundos `#FCFCFA`, `#F8F5EE` | https://www.hubspot.com/ |
| Pipedrive | roxo `#6861F2`; amarelo `#FFDE00`; azul-petróleo `#27455C`; texto `#192435`; verde `#017737`, `#D7F9D3`, `#F3FCF2` | https://www.pipedrive.com/ |
| Attio | azul `#266DF0`; roxo `#9B69FF`; verde `#007D53`, `#E0FCED`; neutros `#242629`, `#101112`, `#505155`, `#75777C`, `#CDCED2`, `#ECECED` | https://attio.com/ |
| Linear | fundos `#0F1011`, `#08090A`; texto `#F7F8F8`, `#D0D6E0`, `#8A8F98`, `#62666D`; verde `#27A644`; vermelho `#F34E52` | https://linear.app/ |
- Padrão: neutros frios em quase todo o espaço; cor reservada a ação e estado (verde/vermelho). Cores a evitar (inferência): fundos saturados em tabelas; vermelho/verde como único diferenciador de status.
- Medidas são da página de marketing, não do produto logado.

### 3. Tipografia típica
- HubSpot `HubSpot Sans` + `HubSpot Serif`; Pipedrive `Inter` + `Haffer`; Attio `Inter`/`Inter Display` + `JetBrains Mono`; Linear `Inter Variable` + `Berkeley Mono`.
- Padrão: **Inter** domina; monoespaçada para IDs/códigos. Números tabulares e tamanho mínimo: **não verificado**; recomendação (inferência): 12–13px para linhas de tabela densa, 14px para corpo.

### 4. Densidade
- **Alta.** Motivo: o usuário lida com muitos registros por sessão; trocar de contexto custa. (inferência) Salesforce SLDS 2 posiciona-se como estrutura de UI flexível com temas avançados e prepara terreno para modo escuro (https://www.lightningdesignsystem.com/ ✅ — versão "Fall '26 v3.7").

### 5. Motion
- Aceitável: arrastar cartão de kanban, transição de painel lateral, destaque de linha atualizada.
- Nunca animar (inferência): troca de ordem de linhas em tabelas enquanto o usuário lê; contadores de pipeline ao filtrar; qualquer coisa que atrase atalho de teclado.
- Não verificado: durações.

### 6. Padrões de tela essenciais
- Lista/tabela de registros com filtros e visões salvas · Pipeline kanban por etapa · Perfil do contato com **linha do tempo de atividades** · Painel lateral de detalhes · Paleta de comandos/atalhos (Linear) · Relatórios e metas.
- Referências abertas: Salesforce SLDS 2 (documentação de componentes) ✅; Linear, Attio, Pipedrive e HubSpot (páginas de marketing) ✅. Telas internas: não abertas (exigem conta).

### 7. Dados e números
- Valores de negócio em moeda local, soma por etapa do funil, probabilidade % e data prevista de fechamento; datas relativas ("há 3 dias") com data completa no hover (inferência); abreviação (R$ 1,2 mi) só com valor exato acessível.
- Fonte e data: toda métrica de relatório com período e "atualizado em". (inferência)

### 8. Confiança e credibilidade
- Para CRM, confiança = dados corretos e histórico auditável: quem alterou, quando. (inferência) Salesforce destaca "Trust" no rodapé da página do design system ✅ (link "Trust").

### 9. Regulação e conformidade que afetam a interface
| Regra | Órgão | URL | O que muda na tela |
|---|---|---|---|
| LGPD art. 8º: consentimento escrito em cláusula destacada; ônus da prova do controlador | Congresso/ANPD | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm ✅ | Registrar origem, data e texto do consentimento no contato. |
| LGPD art. 9º: acesso facilitado e informação clara, adequada e ostensiva | idem | idem | Aviso de privacidade acessível no formulário de captura. |
| LGPD art. 18: direitos do titular (acesso, correção, eliminação, portabilidade etc.) | idem | idem | Funções "exportar dados do contato" e "eliminar/anonimizar". |
| LGPD art. 6º: finalidade e necessidade | idem | idem | Campos opcionais claramente marcados; não coletar além do necessário. |
- Marketing por e-mail/WhatsApp: regra específica (ex.: CDC, Marco Civil): **não verificado**.

### 10. Acessibilidade específica do público
- Usuário profissional em uso prolongado: contraste confortável, foco visível e **navegação por teclado completa** (atalhos). Tabelas com cabeçalho semântico. (inferência)
- Verificação nos produtos: **não feita**.

### 11. Anti-padrões e dark patterns
- Inferência: campos obrigatórios demais; perder o contexto ao abrir registro; filtro que reseta ao navegar; exclusão em massa sem desfazer; pré-marcar consentimento de marketing (contraria art. 8º, em termos de ônus da prova — interpretação minha).

### 12. Diferenças por plataforma
| | Website | App desktop | App mobile |
|---|---|---|---|
| CRM | marketing + onboarding | **superfície principal**: tabela, kanban, atalhos, painéis | consulta rápida, registrar atividade, ligação/WhatsApp (inferência) |

### 13. Direções visuais possíveis
1. **"Produtividade escura"** — `#0F1011`, texto `#F7F8F8`/`#D0D6E0`, acento verde `#27A644`, Inter Variable + mono; densidade alta; motion mínimo. Fonte: linear.app.
2. **"Clara e fluida"** — branco/`#ECECED`, texto `#242629`, azul `#266DF0`, roxo `#9B69FF`; Inter + mono; densidade alta-média. Fonte: attio.com.
3. **"Funil amigável"** — branco, texto `#192435`, roxo `#6861F2` e verde `#017737`; Inter; densidade média; kanban em destaque. Fonte: pipedrive.com.
4. **"Plataforma corporativa"** — neutros + laranja `#FF4800` ou azul Salesforce (hex **não medido**); densidade alta; muitos módulos. Fontes: hubspot.com, lightningdesignsystem.com.

### 14. Componentes característicos
- Tabela densa com visões salvas · Cartão de negócio (valor, responsável, prazo) · Coluna de pipeline com soma · Linha do tempo do contato · Painel lateral de detalhes · Badge de etapa/estado · Barra de filtros combináveis · Paleta de comandos · Gerenciador de consentimento LGPD.

### 15. Referências verificadas
| nome | URL | tipo | o que aproveitar | status |
|---|---|---|---|---|
| Salesforce Lightning Design System 2 | https://www.lightningdesignsystem.com/ | design system público | arquitetura de tokens (CSS custom properties), caminho para dark mode, padrões agênticos | ✅ |
| HubSpot (site) | https://www.hubspot.com/ | produto | paleta/tipografia | ✅ |
| HubSpot Canvas | https://canvas.hubspot.com/ | design system | redirecionou para um blog sobre design systems; **design system público não confirmado** | ❌ |
| Pipedrive | https://www.pipedrive.com/ | produto | paleta/tipografia | ✅ |
| Attio | https://attio.com/ | produto | paleta/tipografia | ✅ |
| Linear | https://linear.app/ | produto | densidade e tema escuro | ✅ |
| LGPD | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm | regulação | arts. 6, 8, 9, 18 | ✅ |
| NN/g/Baymard sobre CRM | — | pesquisa | não localizei estudo específico; **não verificado** | ❌ |

---

## Segmento: Publicidade (código: PUB)

### 1. Tom e personalidade visual
- Duas faces: **ferramenta** (Ads Manager, Google Ads: funcional, neutra, orientada a dados) e **criativo/agência** (expressivo, editorial). Adjetivos: funcional/analítico (ferramenta); ousado/autoral (agência). (inferência, apoiada nas páginas medidas)
- O usuário da ferramenta espera controle sobre orçamento e resultado; o do criativo espera impacto.
- Awwwards lista agências em categoria própria (https://www.awwwards.com/websites/advertising-agencies/ ✅): referência de vitrine criativa.

### 2. Paleta típica (hex medidos)
| Produto | Cores medidas | URL |
|---|---|---|
| Meta Ads Manager (página) | azul `#0064E0`; fundos `#FFFFFF`, `#F1F4F7`, `#F5F6F6`; texto `#1C1E21`, `#1C2B33`, `#465A69` | https://www.facebook.com/business/tools/ads-manager |
| Google Ads (página, redireciona para business.google.com/br/google-ads/) | azul `#1A73E8`; fundos `#F8F9FA`, `#F8FAFD`, `#E8F0FE`; texto `#202124`, `#3C4043`, `#5F6368` | https://ads.google.com/intl/pt-BR_br/home/ |
| Awwwards (vitrine de agências) | texto/fundo `#222222`, `#F8F8F8`, `#EDEDED`; destaque `#FFF083`; `#B42625` | https://www.awwwards.com/websites/advertising-agencies/ |
- Ferramentas usam azul + neutros claros; cor forte fica para o criativo do anunciante. Cores a evitar (inferência): UI com paleta que compete com o criativo do cliente.

### 3. Tipografia típica
- Meta `Optimistic VF`; Google `Google Sans` / `Google Sans Text`; Awwwards `Inter Tight`. Números tabulares e tamanho mínimo: **não verificado**.

### 4. Densidade
- **Alta na ferramenta** (muitas campanhas, métricas e colunas); **baixa no criativo** (uma mensagem por peça). Motivo: gestor compara muitas linhas; o anúncio precisa ser lido em segundos. (inferência)

### 5. Motion
- Aceitável: prévia de anúncio animada, vídeo e carrossel (são o produto); transições de painel.
- Nunca animar (inferência): números de gasto/orçamento enquanto o usuário edita; botão de publicar.
- Meta Ads Guide: a página de vídeo recomenda "movimento e som" em anúncios (https://www.facebook.com/business/ads-guide/update/image ✅, texto do formato Feed).

### 6. Padrões de tela essenciais
- Estrutura campanha → conjunto → anúncio; escolha de objetivo; público; orçamento (diário ou vitalício, descrito na página do Ads Manager ✅); upload de criativo com **prévia por posicionamento** e por dispositivo; tabela de desempenho com colunas configuráveis. App Ads Manager existe para iOS e Android ✅.
- Meta Ads Guide: formatos Imagem, Vídeo, Carrossel (até 10 imagens/vídeos) e Coleção ✅.

### 7. Dados e números
- Especificação verificada (Meta, imagem, Feed do Facebook): JPG ou PNG; proporção 4:5; 1440 × 1800 px; texto principal 50–150 caracteres; título 27 caracteres; arquivo máx. 30 MB; largura mín. 600 px; altura mín. 750 px em 4:5; tolerância de proporção 3% (https://www.facebook.com/business/ads-guide/update/image ✅). Outros posicionamentos e Google: **não verificado**.
- Métrica isolada engana: um artigo (Medium, via busca) mostra campanha com custo por lead baixo e taxas de gancho/retenção ruins; lição de design: mostrar qualidade ao lado de custo (https://medium.com/@olumiladedavid/most-real-estate-marketers-dont-know-how-to-read-a-meta-ads-dashboard-here-s-how-to-fix-it-aa7051a9b1ca, fonte secundária).
- Regra de produto (inferência): moeda e período explícitos; variação vs. período anterior; atribuição e janela rotuladas.

### 8. Confiança e credibilidade
- Para o anunciante: transparência de gasto e de atribuição. Para o público: anúncio identificável como tal (itens 9 e 11).

### 9. Regulação e conformidade que afetam a interface
| Regra | Órgão | URL | O que muda na tela |
|---|---|---|---|
| Código CONAR, art. 28: o anúncio deve ser claramente distinguido como tal, seja qual for a forma ou meio | CONAR (autorregulação) | https://www.conar.org.br/codigos ✅ | Rótulo "Publicidade/Patrocinado" visível em qualquer formato. |
| Código CONAR, art. 27: apresentação verdadeira do produto; parágrafos tratam de alegações, preços e testemunhais | CONAR | idem ✅ | Preço, condições e depoimentos fiéis ao real. |
| Código CONAR, art. 37: nenhum anúncio dirigirá apelo imperativo de consumo diretamente à criança | CONAR | idem ✅ | Sem CTA imperativo em peças para crianças. |
| CDC (Lei 8.078/90), art. 36: a publicidade deve ser veiculada de modo que o consumidor a identifique fácil e imediatamente; art. 37 §1º e §2º: enganosa e abusiva | Congresso | https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm ✅ | Idem; sem omissão de dado essencial. |
| Guia CONAR de Marketing e Publicidade por Influenciadores Digitais (maio/2026) | CONAR | https://conar.wpenginepowered.com/wp-content/uploads/2026/05/260525_GUIA_INFLUENCIADORES_CONAR_v6.pdf | **Não lido**: a leitura do PDF foi bloqueada (robots). Termos exigidos, posição e duração do aviso: não verificado. |
- A home do CONAR (https://www.conar.org.br/ ✅) lista decisões recentes, muitas sobre anúncios de apostas ("ODDs"); e noticia "ferramenta gratuita para identificar a publicidade de influenciadores". O conteúdo dessas decisões não foi lido.
- Rótulo de plataforma: resultados de busca descrevem o rótulo "Parceria paga" do Instagram para conteúdo de marca (fontes secundárias, ex.: https://www.creatorsjet.com/pt-BR/blog/adicionar-parceria-paga-instagram); a regra oficial na Central de Ajuda da Meta não foi aberta.
- Políticas de anúncios das plataformas (Meta/Google): **não verificado**.

### 10. Acessibilidade específica do público
- Anúncios: contraste do texto sobre imagem, legenda em vídeo (muito consumo sem som; fonte: Kontentino via busca, secundária), texto alternativo. Medições: **não verificado**.

### 11. Anti-padrões e dark patterns
- Anúncio disfarçado de conteúdo editorial (contraria CONAR art. 28 e CDC art. 36, ambos lidos); preço "a partir de" sem condição (art. 37 §1º, enganosa por omissão, leitura resumida); depoimento falso. Na ferramenta (inferência): recomendações automáticas pré-aplicadas que aumentam gasto; orçamento padrão alto.

### 12. Diferenças por plataforma
| | Website | App desktop | App mobile |
|---|---|---|---|
| PUB | Ads Manager na web (principal para criação) | painel de relatórios e criação em massa (inferência) | app Ads Manager: monitorar, pausar, ajustar orçamento ✅ |

### 13. Direções visuais possíveis
1. **"Painel de mídia"** — fundo `#F8F9FA`/`#FFFFFF`, texto `#202124`, azul `#1A73E8`; Google Sans-like/Inter; densidade alta; motion mínimo. Fonte: Google Ads.
2. **"Social ads claro"** — `#F1F4F7`, `#1C1E21`, azul `#0064E0`; sans humanista; densidade média-alta; prévias grandes. Fonte: Meta.
3. **"Vitrine de agência"** — `#222222` + `#F8F8F8`, destaque `#FFF083`; grotesca (Inter Tight); densidade baixa; motion expressivo só na vitrine. Fonte: Awwwards.

### 14. Componentes característicos
- Hierarquia campanha/conjunto/anúncio · Prévia por posicionamento · Seletor de objetivo · Barra de orçamento (diário/vitalício) · Tabela de desempenho com colunas configuráveis · Checagem de especificação (formato, proporção, caracteres) · Selo "Publicidade" · Rótulo de parceria paga.

### 15. Referências verificadas
| nome | URL | tipo | o que aproveitar | status |
|---|---|---|---|---|
| Meta Ads Manager | https://www.facebook.com/business/tools/ads-manager | produto | funções, app mobile, paleta | ✅ |
| Meta Ads Guide (Feed, imagem) | https://www.facebook.com/business/ads-guide/update/image | especificação | tamanhos e limites de texto | ✅ |
| Google Ads | https://ads.google.com/intl/pt-BR_br/home/ | produto | paleta/tipografia | ✅ |
| CONAR (home) | https://www.conar.org.br/ | regulação | estrutura, guias | ✅ |
| Código CONAR | https://www.conar.org.br/codigos | regulação | arts. 27, 28, 37 (lidos via ferramenta de leitura de página; página tem 176 mil caracteres e só os primeiros 100 mil foram cobertos) | ✅ |
| Guia de influenciadores CONAR | link no item 9 | regulação | — | 🔒 |
| CDC | https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm | regulação | arts. 36 e 37 | ✅ |
| Awwwards — agências | https://www.awwwards.com/websites/advertising-agencies/ | vitrine | paleta e tipografia | ✅ |
| ClickCease (Behance) | https://www.behance.net/gallery/100475361/ClickCease-Case-Study-SaaS-dashboards-UXUI-design | estudo de caso | redesign de dashboards de cliques do Google Ads; só título/tags lidos | 🔒 |
| Medium: dashboard de campanhas | https://nikhilprasad01.medium.com/creating-a-dashboard-to-help-streamline-campaign-management-processes-a-case-study-fac74a9de3a6 | estudo de caso | painel interno para gestores; trecho via busca | 🔒 |
| Awwwards Hall/Prêmios de campanhas | — | — | não verificado | ❌ |
| Especificações Google Ads (criativos) | — | — | não aberta | ❌ |

---

## Segmento: Marca pessoal (código: MPE)

### 1. Tom e personalidade visual
- Adjetivos: autoral, expressivo, direto, humano, memorável. O usuário (dono do perfil) espera sentir identidade própria; o visitante espera entender quem é a pessoa em segundos.
- Behance, caso "Self Branding & Portfolio": o conceito mistura "ilustradora peculiar" com "designer organizada"; logo em letra manuscrita porque queria ser lembrada pelo nome (https://www.behance.net/gallery/29277083/Self-Branding-Portfolio, trecho via busca).
- Behance, "Portfolio 2017": defende o portfólio simples e limpo, que comunica o que faz e mostra o processo (https://www.behance.net/gallery/47094559/Portfolio-2017, trecho via busca). Há duas escolas: personalidade forte e minimalismo.

### 2. Paleta típica (hex medidos)
| Produto | Cores medidas | URL |
|---|---|---|
| Linktree | `#FFFFFF`, `#1E2330` (texto principal), `#E9C0E9` (lilás), `#D2E823` (lima), `#ECFEF2`, `#676B5F` | https://linktr.ee/ |
| Framer Marketplace (templates) | fundos `#1F1F1F`, `#111111`, `#FFFFFF`; texto `#FFFFFF`, `#999999`; `#0099FF` | https://www.framer.com/marketplace/templates/ |
- A paleta de marca pessoal é a da pessoa; as plataformas oferecem moldura neutra (Framer escuro) ou cores vivas de marca (Linktree). Cores a evitar (inferência): moldura colorida que compita com a identidade do perfil.

### 3. Tipografia típica
- Linktree `Linksans` (própria); Framer `Inter` (+ `walsheim`). Behance cita "sofia pro" em um portfólio (tag do caso 2017). Números tabulares: não se aplica/não verificado; tamanhos mínimos: não verificado.

### 4. Densidade
- **Baixa.** Motivo: uma pessoa, uma mensagem, poucos blocos; o visitante decide em segundos. (inferência) Behance (blog): o trabalho deve ser o foco e a formatação simples para navegar e contatar (https://www.behance.net/blog/how-to-make-design-portfolio, via busca).

### 5. Motion
- É o segmento mais tolerante: microinterações, transições de portfólio, hover. Limites (inferência): nunca animar o botão de contato/CTA principal; respeitar `prefers-reduced-motion`; nada que atrase o carregamento do link na bio.

### 6. Padrões de tela essenciais
- Perfil com foto, nome e uma linha de posicionamento · lista de links/botões (Linktree) · grade de portfólio com estudo de caso · agenda pública (shows, aulas, palestras) · prova social (logos de clientes, depoimentos, números) · contato/agendamento · página de produto/venda.
- Linktree: "um link para todo o conteúdo", vender produtos, coletar pagamentos, analytics de cliques e receita, QR code ✅ (https://linktr.ee/).
- Estrutura de estudo de caso (Behance 2017, via busca): introdução, problema, processo e exemplos anotados.
- **Bento** (bento.me): ao abrir, a navegação terminou em linktr.ee; o motivo **não foi verificado**. Tratar como não disponível.
- **Read.cv**: página mostra "Deployment Paused" (🔒).

### 7. Dados e números
- Prova social: "70M+" no Linktree ✅. Números públicos de seguidores/clientes com data (inferência). Template de portfólio Framer: preços de Free a US$ 129 na listagem aberta ✅ (só como exemplo de mercado).

### 8. Confiança e credibilidade
- Logos de clientes, depoimentos reais, trabalho recente com data, contato visível. NN/g (via busca): "Trustworthiness in Web Design: 4 Credibility Factors" e prominência/interpretação (links no item 8 de FIN) aplicam-se; estudo específico de marca pessoal: **não verificado**.

### 9. Regulação e conformidade que afetam a interface
| Regra | Órgão | URL | O que muda na tela |
|---|---|---|---|
| LGPD arts. 6, 8, 9, 18 | Congresso/ANPD | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm ✅ | Formulário de contato/newsletter e analytics com aviso claro e consentimento destacado. |
| CONAR art. 28 e CDC art. 36 (identificação publicitária) | CONAR / Congresso | links em PUB ✅ | Posts e links patrocinados devem ser identificados como publicidade (inferência de aplicação ao criador). |
| CDC art. 37 §1º (publicidade enganosa) | Congresso | link em PUB ✅ | Depoimentos e números de prova social devem ser reais (inferência). |
| Guia CONAR de influenciadores | CONAR | link em PUB | 🔒 não lido. |

### 10. Acessibilidade específica do público
- Público amplo e mobile-first (inferência). Contraste do texto sobre foto/cor viva (lilás `#E9C0E9` e lima `#D2E823` exigem texto escuro `#1E2330`; contraste não calculado); alvo de toque grande nos botões de link; texto alternativo em imagens de portfólio.

### 11. Anti-padrões e dark patterns
- Link na bio com dezenas de botões sem hierarquia; CTA escondido atrás de animação; contador de escassez falso; depoimentos inventados (CDC art. 37 §1º); publi sem rótulo (CONAR art. 28); capturar e-mail sem aviso (LGPD art. 9º). Os dois últimos são aplicações minhas de textos lidos.

### 12. Diferenças por plataforma
| | Website | App desktop | App mobile |
|---|---|---|---|
| MPE | portfólio completo, estudos de caso (Framer/Behance) | editor/painel de criador | **principal consumo**: link na bio aberto do Instagram/TikTok; uma coluna (inferência) |

### 13. Direções visuais possíveis
1. **"Link-hub vibrante"** — fundo branco, texto `#1E2330`, acentos `#E9C0E9` e `#D2E823`; sans própria; densidade baixa; motion de hover. Fonte: linktr.ee.
2. **"Portfólio escuro editorial"** — `#1F1F1F`/`#111111`, texto branco e `#999999`, destaque `#0099FF`; Inter/grotesca; densidade baixa; motion suave de entrada. Fonte: framer.com/marketplace.
3. **"Minimalista de processo"** — branco, texto escuro, estudo de caso em 4 blocos (intro, problema, processo, telas); sem logo; motion nulo. Fonte: Behance Portfolio 2017.
4. **"Vitrine autoral"** — expressivo, neutros `#222222`/`#F8F8F8` com 1 cor de destaque (`#FFF083`); grotesca; motion editorial. Fonte: Awwwards.

### 14. Componentes característicos
- Cartão de perfil (foto, nome, posicionamento) · Botão de link com ícone · Grade de portfólio · Estudo de caso em 4 blocos · Agenda pública · Faixa de prova social (logos + números) · Depoimento com origem · Botão de agendamento · Selo "publi/parceria".

### 15. Referências verificadas
| nome | URL | tipo | o que aproveitar | status |
|---|---|---|---|---|
| Linktree | https://linktr.ee/ | produto | funções, paleta, "70M+" | ✅ |
| Framer Marketplace | https://www.framer.com/marketplace/templates/ | templates | categorias, paleta, preços | ✅ |
| Bento | https://bento.me/ | produto | redirecionou para linktr.ee | ❌ |
| Read.cv | https://read.cv/ | produto | "Deployment Paused" | 🔒 |
| Behance — Self Branding & Portfolio | https://www.behance.net/gallery/29277083/Self-Branding-Portfolio | estudo de caso | conceito de marca pessoal | 🔒 (via busca) |
| Behance — Portfolio 2017 | https://www.behance.net/gallery/47094559/Portfolio-2017 | estudo de caso | estrutura de caso | 🔒 (via busca) |
| Behance — How to make a portfolio | https://www.behance.net/blog/how-to-make-design-portfolio | guia | foco no trabalho | 🔒 (via busca) |
| Awwwards | https://www.awwwards.com/websites/advertising-agencies/ | vitrine | referência autoral | ✅ |
| LGPD / CONAR / CDC | links acima | regulação | — | ✅ |
| Notion como portfólio | — | — | não aberto | ❌ |

---

## Segmento: Saúde (código: SAU)

### 1. Tom e personalidade visual
- Adjetivos: claro, calmo, acolhedor, sério, legível. O usuário (paciente, muitas vezes ansioso ou idoso) espera sentir segurança, privacidade e instruções que não deixam dúvida. (inferência)
- NHS Design System: "construir serviços do NHS consistentes e acessíveis para o público e a equipe" (https://service-manual.nhs.uk/design-system ✅).

### 2. Paleta típica (hex medidos)
| Produto | Cores medidas | URL |
|---|---|---|
| NHS Design System | azul `#005EB8` (links/ação), azul-escuro `#003087`; verde `#007F3B`; texto `#212B32`; cinzas `#D8DDE0`, `#F0F4F5` | https://service-manual.nhs.uk/design-system |
| Doctoralia (BR) | verde-água claro `#DFF9F2`; bege `#EEE8E3`, `#B6AEA5`; verde `#006A59`; texto `#2A2623`, `#35495E`; azul-petróleo `#27455C` | https://www.doctoralia.com.br/ |
- Padrão: azul/verde sobre fundos claros, texto quase preto. Cores a evitar (inferência): vermelho como cor de marca (confunde com alerta clínico); contraste baixo em texto cinza.

### 3. Tipografia típica
- NHS: `Frutiger W01` medida; o manual diz que Frutiger é a fonte da marca e que se deve usar Arial quando ela não estiver disponível. Parágrafo padrão **19px em telas grandes e 16px em telas pequenas**; texto pequeno (`nhsuk-body-s`) com moderação, cerca de 16px/14px; a escala completa vai de 14px a 64px (https://service-manual.nhs.uk/design-system/styles/typography ✅, lido por ferramenta de leitura de página). O manual não define um mínimo absoluto.
- Doctoralia: `system-ui`. Números tabulares: **não verificado**.

### 4. Densidade
- **Baixa a média.** Motivo: público diverso e tarefa sensível; uma pergunta por tela reduz erro. (inferência) O corpo de 19px do NHS e do GOV.UK sustenta o espaço generoso.
- Em prontuário/sistema clínico, a densidade sobe (profissional): **não verificado** em produto real (exige login).

### 5. Motion
- Mínimo e funcional (carregamento, confirmação). Nunca animar (inferência): resultados de exame, alertas clínicos, valores de dose, contagem de tempo de consulta que gere pressão.

### 6. Padrões de tela essenciais
- Busca de profissional por especialidade/local · agendamento com data e horário · confirmação com resumo e lembrete · teleconsulta (sala de espera, vídeo, chat) · prontuário/histórico · receitas e atestados · termo de consentimento. O Doctoralia abre com "Encontre um profissional da saúde — solicite um agendamento online" (título da página ✅).
- NHS: componentes e padrões prontos, com código (https://service-manual.nhs.uk/design-system ✅).

### 7. Dados e números
- Dose, data e hora sempre com unidade e fuso (inferência); datas completas (dd/mm/aaaa) e hora de início da teleconsulta; resultados com faixa de referência e data da coleta (inferência). Preço de consulta pode ser divulgado pelo médico segundo notícia do CFM (item 9).

### 8. Confiança e credibilidade
- Dados do profissional verificáveis (CRM e UF), política de privacidade, canal humano. A exigência de registro em conselho para quem faz telemedicina vem de resumo da Portal da Indústria sobre a Res. 2.314 (fonte secundária). Selo de qualidade em produto induzindo garantia de resultado é proibido pela publicidade médica (apresentação do CRM-PR via busca, item 9).

### 9. Regulação e conformidade que afetam a interface
| Regra | Órgão | URL | O que muda na tela |
|---|---|---|---|
| LGPD art. 5º, II: dado "referente à saúde" é dado pessoal sensível | Congresso/ANPD | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm ✅ | Tratar toda informação clínica como sensível. |
| LGPD art. 11, I: consentimento "de forma específica e destacada, para finalidades específicas" | idem | idem ✅ | Caixa de consentimento própria, não embutida em termos gerais. |
| LGPD art. 11, §4º: vedada comunicação ou uso compartilhado entre controladores de dados sensíveis referentes à saúde (o texto tem ressalvas que **não li**) | idem | idem ✅ (parcial) | Não oferecer "compartilhar com parceiros" por padrão. |
| Res. CFM 2.314/2022 (telemedicina) | CFM | https://sistemas.cfm.org.br/normas/arquivos/resolucoes/BR/2022/2314_2022.pdf (visto em busca; **PDF não aberto**) | Segundo notícias do CFM e do CREMERS: paciente ou representante deve autorizar o atendimento e a transmissão de imagens e dados (termo de consentimento); atendimento registrado em prontuário. Texto exato dos artigos: não verificado. |
| Res. CFM 2.336/2023 (publicidade médica), em vigor desde março/2024 | CFM | https://sistemas.cfm.org.br/normas/arquivos/resolucoes/BR/2023/2336_2023.pdf (visto em busca; **PDF não aberto**) | Segundo notícia do CFM e do CREMERS: permite "antes e depois" com finalidade educativa e condições (indicações, evoluções satisfatórias e insatisfatórias, complicações) e divulgar preços de consultas; exige autorização do paciente e privacidade. Artigos exatos: não verificado. |
- ANVISA: **não verificado** (não localizei norma que se aplique a interface neste escopo).
- CDC e CONAR (identificação de publicidade): ver PUB.

### 10. Acessibilidade específica do público
- Público idoso e ansioso: texto de 19px no desktop e 16px no mobile como base (NHS e GOV.UK ✅); contraste forte; botões grandes; instruções passo a passo; alternativa por telefone (inferência). Verificação de contraste dos produtos: **não feita**.

### 11. Anti-padrões e dark patterns
- Pré-marcar consentimento de compartilhamento (contraria o art. 11, I, lido); esconder o termo de teleconsulta; "antes e depois" sem complicações (condição relatada pelo CFM); promessa de resultado; urgência falsa ("últimas vagas"). A lista é majoritariamente minha (inferência) sobre textos lidos.

### 12. Diferenças por plataforma
| | Website | App desktop | App mobile |
|---|---|---|---|
| SAU | busca e agendamento; SEO de profissionais | sistema clínico/prontuário e agenda do consultório (inferência) | agendar, lembrete, teleconsulta, receita; câmera/microfone |

### 13. Direções visuais possíveis
1. **"Sistema público claro"** — branco, texto `#212B32`, azul `#005EB8`, verde `#007F3B`; Frutiger/Arial; corpo 19px/16px; densidade baixa; motion mínimo. Fonte: NHS.
2. **"Marketplace acolhedor"** — fundos `#DFF9F2`/`#EEE8E3`, verde `#006A59`, texto `#2A2623`; sans de sistema; densidade média; motion leve. Fonte: Doctoralia.
3. **"Clínico profissional"** — neutros frios, azul-petróleo `#27455C`, densidade média-alta para agenda/prontuário (inferência; sem fonte de produto logado).

### 14. Componentes característicos
- Cartão do profissional (foto, CRM/UF, especialidade, preço) · Seletor de horário · Resumo de agendamento · Termo de consentimento destacado · Sala de espera da teleconsulta · Linha do tempo do histórico · Receita/atestado com assinatura · Faixa de referência de exame.

### 15. Referências verificadas
| nome | URL | tipo | o que aproveitar | status |
|---|---|---|---|---|
| NHS Design System | https://service-manual.nhs.uk/design-system | design system público | tokens, componentes, acessibilidade | ✅ |
| NHS Typography | https://service-manual.nhs.uk/design-system/styles/typography | design system | fontes e tamanhos | ✅ |
| Doctoralia | https://www.doctoralia.com.br/ | produto | paleta, busca/agendamento | ✅ |
| LGPD | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm | regulação | arts. 5º II e 11 | ✅ |
| Res. CFM 2.314/2022 | link no item 9 | regulação | telemedicina | 🔒 |
| Res. CFM 2.336/2023 | link no item 9 | regulação | publicidade médica | 🔒 |
| Portal CFM (notícias) | https://portal.cfm.org.br/noticias/119781 | oficial | resumo da 2.336; menciona Manual de Publicidade Médica | 🔒 (via busca) |
| Design systems de healthtechs brasileiras | — | design system | não localizado | ❌ |
| Estudo NN/g sobre saúde/idosos | — | pesquisa | não localizado | ❌ |

---

## Segmento: Jurídico (código: JUR)

### 1. Tom e personalidade visual
- Adjetivos: sóbrio, claro, rigoroso, discreto, confiável. O usuário espera sentir precisão e ausência de ambiguidade; no caso de advogado, a norma pede publicidade "sóbria, discreta e informativa" (Provimento 205/2021, art. 3º, §1º, lido via ferramenta de leitura de página).
- GOV.UK é a referência de clareza: design system público para "serviços consistentes com GOV.UK", com estilos, componentes e padrões (https://design-system.service.gov.uk/ ✅).

### 2. Paleta típica (hex medidos)
| Produto | Cores medidas | URL |
|---|---|---|
| GOV.UK Design System | azul `#1D70B8`, `#1A65A6`; verde `#0F7A52`; texto `#0B0C0C`, `#484949`; fundo `#F4F8FB` | https://design-system.service.gov.uk/ |
| Jusbrasil | marinho `#0F172A`; verde `#007A5F`, `#00A37F`; fundo `#F1F5F9`; texto `#455468`, `#5C6F8A` | https://www.jusbrasil.com.br/ |
| DocuSign (BR) | roxo-escuro `#130032`; violeta `#4C00FF`; fundo `#F8F3F0`; `#151B17` | https://www.docusign.com/pt-br |
| Clio | preto `#000000`; azul `#1A56FF`, `#012587`; areia `#F5CE9B`; `#F5F5F5` | https://www.clio.com/ |
- Padrão: azul-marinho/verde/preto, fundos claros. Cores a evitar (inferência): dourado/“ostentação” (art. 6º, parágrafo único do Provimento proíbe ostentação de bens, no texto lido; é regra de conteúdo, não de cor).

### 3. Tipografia típica
- GOV.UK `GDS Transport` (obrigatória no subdomínio gov.uk; fora dele, Helvetica ou Arial); parágrafo 19px (grande) / 16px (pequeno); menor classe `govuk-body-s` com 14px, com moderação (https://design-system.service.gov.uk/styles/typography/ ✅). Números tabulares: a página não menciona.
- Jusbrasil `Inter`; DocuSign `DSIndigo`; Clio `Facility` + mono (`Openinto Mono`).

### 4. Densidade
- **Média, com blocos de texto longo.** Motivo: leitura de peças e contratos exige coluna estreita e hierarquia; telas de gestão (processos, prazos) são densas. (inferência)

### 5. Motion
- Mínimo. Nunca animar (inferência): prazos, valores, cláusulas contratuais, botão de assinar; evitar movimento em documento aberto para leitura.

### 6. Padrões de tela essenciais
- Consulta processual/jurisprudência com busca e filtros (Jusbrasil abre com "Mais facilidade na sua Consulta Judicial", título ✅) · lista de processos e prazos · linha do tempo do processo · leitura de documento com anotações · fluxo de assinatura eletrônica (enviar, assinar, concluir) · formulário passo a passo (padrões de GOV.UK) · faturamento por tempo (gestão de escritório; Clio, ver nota).
- GOV.UK: padrões para "entrar nomes e endereços, preencher formulários e criar contas" ✅.

### 7. Dados e números
- Número CNJ e datas completas; prazos com contagem e data final explícitas (inferência); valores com R$ e centavos; sempre fonte e data de atualização do dado (inferência). Não há regra lida sobre formato do número de processo (não verificado).

### 8. Confiança e credibilidade
- Para advogado: títulos "verdadeiros e comprováveis" (Provimento 205, art. 4º, §1º, lido). Para produto de assinatura: tipo de assinatura e trilha de auditoria visíveis (inferência), apoiado na Lei 14.063/2020.

### 9. Regulação e conformidade que afetam a interface
| Regra | Órgão | URL | O que muda na tela |
|---|---|---|---|
| Provimento 205/2021 (publicidade e informação da advocacia), de 15/07/2021: art. 3º caput (não pode configurar captação de clientela ou mercantilização), art. 3º I (vedada referência a honorários para captar), art. 3º §1º (sóbria, discreta e informativa), art. 4º §1º (títulos verdadeiros e comprováveis), art. 4º §2º (vedada menção a decisões judiciais e resultados), art. 5º §2º (vedado logotipo e símbolos oficiais da OAB), art. 5º §3º (vedados casos concretos e resultados em vídeos/palestras), art. 6º (vedada promessa de resultados; parágrafo único: ostentação) | CFOAB | https://www.oab.org.br/leisnormas/legislacao/provimentos/205-2021 ✅ | Sem preço/desconto como gancho, sem "resultados garantidos", sem logotipo da OAB, sem depoimento de caso, sem sinais de luxo. Depoimentos: o texto lido não os menciona expressamente (as regras próximas são os arts. 4º §2º e 5º §3º). |
| Lei 14.063/2020, art. 4º: assinatura **simples** (identifica o signatário), **avançada** (certificados não ICP-Brasil, vinculada ao signatário e que detecta alteração) e **qualificada** (certificado digital ICP-Brasil, nível mais alto). Ementa: uso de assinaturas eletrônicas em interações com entes públicos | Congresso | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14063.htm ✅ | Mostrar qual tipo de assinatura será aplicado e o que ele significa. (inferência de aplicação; a lei trata de entes públicos) |
| MP 2.200-2/2001 (ICP-Brasil) | — | não aberta | **não verificado** |
| LGPD (dados em processos/clientes) | Congresso/ANPD | link em SAU ✅ | Aviso e consentimento onde houver dado pessoal. |
- Linguagem simples: página de diretrizes de escrita do GOV.UK redirecionou em duas etapas e **não li o texto das regras**; usei só a existência do design system. Plain language: não verificado.

### 10. Acessibilidade específica do público
- Leitura longa e uso prolongado: corpo 19px/16px (GOV.UK ✅), coluna estreita, contraste forte, foco visível, formulários com erro descrito em texto (padrão de GOV.UK, inferência). Cliente leigo e idoso: linguagem simples e glossário de termos (inferência).

### 11. Anti-padrões e dark patterns
- Juridiquês sem explicação; assinatura em que o tipo e o efeito não são mostrados; botão "assinar" sem revisão do documento; contagem regressiva falsa; promessa de resultado e preço como gancho (contraria os arts. 3º I e 6º lidos); uso do logo da OAB (art. 5º §2º).

### 12. Diferenças por plataforma
| | Website | App desktop | App mobile |
|---|---|---|---|
| JUR | captação (sob o Provimento) e consulta pública | gestão de processos, peças, faturamento (inferência; Clio e Jusbrasil se descrevem como plataformas) | consulta de andamento, notificações de prazo, assinar documento |

### 13. Direções visuais possíveis
1. **"Sóbrio institucional"** — fundo branco/`#F4F8FB`, texto `#0B0C0C`, azul `#1D70B8`; GDS Transport/Arial, corpo 19px; densidade média; motion nulo. Fonte: GOV.UK.
2. **"Legaltech editorial"** — `#0F172A` + `#F1F5F9`, verde `#007A5F`; Inter; densidade média; motion mínimo. Fonte: Jusbrasil.
3. **"Contrato digital"** — `#130032` + `#F8F3F0`, violeta `#4C00FF`; grotesca própria; densidade baixa em fluxo de assinatura. Fonte: DocuSign.
4. **"Gestão moderna de escritório"** — preto/branco, azul `#1A56FF`, areia `#F5CE9B`; display + mono; densidade média-alta. Fonte: Clio.

### 14. Componentes característicos
- Linha do tempo do processo · Cartão de prazo (data final, dias restantes) · Leitor de peça com anotações · Seletor do tipo de assinatura com explicação · Fluxo "revisar → assinar → concluir" · Trilha de auditoria do documento · Busca jurídica com filtros · Aviso ético de publicidade (rodapé de escritório).

### 15. Referências verificadas
| nome | URL | tipo | o que aproveitar | status |
|---|---|---|---|---|
| GOV.UK Design System | https://design-system.service.gov.uk/ | design system público | estilos, componentes, padrões; v6.6.0 de 15/10/2026 | ✅ |
| GOV.UK Typography | https://design-system.service.gov.uk/styles/typography/ | design system | fonte, 19px/16px | ✅ |
| Jusbrasil | https://www.jusbrasil.com.br/ | produto | paleta, Inter, consulta judicial | ✅ |
| DocuSign | https://www.docusign.com/pt-br | produto | paleta, assinatura eletrônica | ✅ |
| Clio | https://www.clio.com/ | produto | paleta, tipografia | ✅ |
| Provimento 205/2021 | https://www.oab.org.br/leisnormas/legislacao/provimentos/205-2021 | regulação | arts. 3º a 6º | ✅ |
| Lei 14.063/2020 | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14063.htm | regulação | tipos de assinatura | ✅ |
| GOV.UK escrita (plain language) | https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/tone-of-voice/ | guia | redirecionou; texto não lido | 🔒 |
| Projuris | https://www.projuris.com.br/provimento-205-2021/ | produto/blog | resumo do Provimento (só trecho em busca) | 🔒 |
| Design system de legaltech brasileira | — | design system | não localizado | ❌ |

---

## Tabela comparativa (6 segmentos)

| Segmento | Tom | Paleta (medida) | Densidade | Motion | Tipografia | Regulação-chave |
|---|---|---|---|---|---|---|
| FIN | preciso, calmo, transparente | branco + 1 cor de marca (`#8D0DE3` Nubank, `#533AFD` Stripe, `#9FE870` Wise, `#FF6200` Itaú) | média-baixa (varejo); média-alta (painel) | mínimo; nunca animar valores nem confirmação | famílias próprias + Inter; tabular não verificado | Res. CMN 4.881/2020 (CET); LGPD |
| CRM | eficiente, denso, neutro | neutros frios; ação/estado em cor (`#266DF0` Attio, `#27A644` Linear; escuro `#0F1011`) | alta | funcional; nunca reordenar linhas lidas | Inter + mono | LGPD (arts. 6, 8, 9, 18) |
| PUB | funcional (ferramenta) / ousado (criativo) | azul + neutros claros (`#0064E0` Meta, `#1A73E8` Google) | alta na ferramenta; baixa no criativo | alto só no criativo; nunca em orçamento/publicar | Optimistic VF, Google Sans, Inter Tight | CONAR art. 28; CDC art. 36 |
| MPE | autoral, expressivo, humano | paleta da pessoa; moldura neutra (`#1F1F1F`) ou viva (`#E9C0E9`, `#D2E823`) | baixa | o mais tolerante; nunca no CTA | Linksans, Inter | LGPD; CONAR art. 28 |
| SAU | claro, calmo, acolhedor | azul/verde claros (`#005EB8`, `#007F3B`, `#006A59`) | baixa-média | mínimo; nunca em resultados/doses | Frutiger/Arial; 19px/16px | LGPD arts. 5º II e 11; CFM 2.314 e 2.336 (resumos) |
| JUR | sóbrio, rigoroso, discreto | marinho/azul/verde (`#0F172A`, `#1D70B8`, `#007A5F`) | média (leitura longa) | mínimo; nunca em prazos/assinar | GDS Transport/Arial 19px; Inter | Provimento OAB 205/2021; Lei 14.063/2020 |

---

## Fontes verificadas (consolidado)

**Abertas e lidas no navegador (hex/fonte medidos ou texto lido):** stripe.com/br e docs.stripe.com/stripe-apps/design; wise.com/br; nubank.com.br; revolut.com/en-BR; inter.co; itau.com.br; hubspot.com; pipedrive.com; attio.com; linear.app; lightningdesignsystem.com; facebook.com/business/tools/ads-manager e /ads-guide/update/image; ads.google.com (business.google.com/br/google-ads); conar.org.br; awwwards.com (agências); linktr.ee; framer.com/marketplace/templates; service-manual.nhs.uk/design-system; design-system.service.gov.uk; doctoralia.com.br; jusbrasil.com.br; docusign.com/pt-br; clio.com.

**Normas lidas via ferramenta de leitura de página (oficiais):** LGPD (planalto.gov.br, arts. 5º, 6º, 8º, 9º, 11, 18); CDC (planalto.gov.br, arts. 36–37); Código CONAR (conar.org.br/codigos, arts. 27, 28, 37; só os primeiros 100 mil de 176 mil caracteres); Provimento OAB 205/2021 (oab.org.br); Lei 14.063/2020 (planalto.gov.br); Res. CMN 3.517 (página BCB, revogação); NHS e GOV.UK (tipografia).

**Vistas só em resultado de busca (não abertas):** Res. CMN 4.881/2020 (PDF BCB); Res. CVM 175; Res. CFM 2.314/2022 e 2.336/2023; artigos NN/g; casos do Behance; páginas de ajuda sobre "parceria paga".

**Descartadas/falharam:** NN/g (2 URLs que chutei), HubSpot Canvas, bento.me, read.cv, guia de influenciadores do CONAR (PDF bloqueado), página de escrita do GOV.UK (só redirecionamentos).

**Lacunas assumidas:** nenhuma tela interna de produto logado foi vista; hex são de páginas públicas. Design systems públicos de Nubank, Itaú, Inter, healthtechs e legaltechs brasileiras não localizados. Números tabulares e durações de motion não verificados em nenhum produto. ANVISA, Anbima, políticas de anúncios Meta/Google e MP 2.200-2 não verificados.

FIM
