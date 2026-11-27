# Templates JUR (direções visuais)

Base: "Direções visuais possíveis" da ficha JUR (rodada 10B, 27/11/2026). Hex medidos por `getComputedStyle` nas
páginas públicas (marketing; produto logado pode diferir). **Raio, sombra e durações não foram medidos** — os valores
dessas linhas são sugestão nossa (inferência), salvo quando a imagem mostra.

## TPL-JUR-01 — Sóbrio institucional
| token | valor |
|---|---|
| Paleta | fundo `#FFFFFF` / `#F4F8FB`, texto `#0B0C0C`, secundário `#484949`, ação `#1D70B8` (hover `#1A65A6`), sucesso `#0F7A52` (GOV.UK, medidos) |
| Par tipográfico | GDS Transport só no gov.uk → fora dele **Helvetica ou Arial**; uma família |
| Escala | corpo **19px em todas as larguras** (`govuk-body` 19/25px); `govuk-body-s` 14px com moderação (GOV.UK) |
| Raio | 0px (inferência; cantos retos do estilo GOV.UK não medidos) |
| Sombra | nenhuma; borda inferior sólida no botão (inferência) |
| Densidade | média; formulário uma pergunta por página quando longo (NN/g §5) |
| Motion | nulo (10B) |
| Quando usar | portal do cliente, formulário jurídico longo, serviço público ou quase público, público leigo/idoso |
| Fontes | https://design-system.service.gov.uk/ · /styles/typography/ |
| Imagens | nenhuma captura própria; `../../ux-patterns/assets/visual-refs/9B_formularios_slack-forca-senha_1.jpg` (rótulo fora do campo) |

## TPL-JUR-02 — Legaltech editorial
| token | valor |
|---|---|
| Paleta | marinho `#0F172A` (texto forte/segmentado ativo), fundo `#F1F5F9`, verde `#007A5F` (marca/destaque), `#00A37F` (apoio), texto `#455468` / `#5C6F8A` (Jusbrasil, medidos) |
| Par tipográfico | **Inter** em tudo (Jusbrasil) |
| Escala | corpo 16px no site; 19px em leitura longa, em todas as larguras (regra GOV.UK) |
| Raio | campo de busca e chips em pílula (observado na imagem; valor não medido) |
| Sombra | brilho verde suave ao redor da busca (observado; não medido) |
| Densidade | baixa na home; média na consulta |
| Motion | mínimo |
| Quando usar | consulta processual, jurisprudência, conteúdo para leigo, marketplace de advogados |
| Fontes | https://www.jusbrasil.com.br/ |
| Imagens | `10C_JUR_jusbrasil_home-busca-processo_1.jpg` |

## TPL-JUR-03 — Contrato digital
| token | valor |
|---|---|
| Paleta | roxo-escuro `#130032` + fundo `#F8F3F0`, violeta `#4C00FF` (ação), `#151B17` (DocuSign BR, medidos) |
| Par tipográfico | grotesca própria (`DSIndigo`); substituta: uma grotesca licenciada do projeto (inferência) |
| Escala | corpo 19px na leitura do documento em todas as larguras (GOV.UK `govuk-body`); 16px nas telas de ação fora da leitura |
| Raio | não medido (página coberta por modal de cookies na C3) |
| Sombra | não medido |
| Densidade | **baixa** no fluxo de assinatura (10B) |
| Motion | mínimo; nada no botão de assinar; confirmação final sem festa |
| Quando usar | envio e assinatura de contratos, termos, procurações |
| Fontes | https://www.docusign.com/pt-br |
| Imagens | nenhuma (captura descartada por modal de cookies) |

## TPL-JUR-04 — Gestão moderna de escritório
| token | valor |
|---|---|
| Paleta | preto `#000000` / branco, cinza `#F5F5F5`, azul `#1A56FF` (ação) e `#012587`, areia `#F5CE9B` (Clio, medidos) |
| Par tipográfico | display leve (`Facility`) + mono (`Openinto Mono`) (Clio); alternativa serifada nos KPIs como Harvey (sem hex medido) |
| Escala | números de destaque grandes em peso leve (imagem Clio); corpo 16px no app |
| Raio | botão com raio pequeno (observado; não medido) |
| Sombra | não medido |
| Densidade | média-alta (painel, faturamento) |
| Motion | funcional |
| Quando usar | gestão de escritório, faturamento por tempo, painel de prazos |
| Fontes | https://www.clio.com/ ; https://www.harvey.ai/ (sem hex) |
| Imagens | `10C_JUR_clio_home-numeros-confianca_1.jpg`, `10C_JUR_harvey_command-center-dashboard_1.jpg`, `10C_JUR_dribbble-mara-bureau_painel-prioridades-ia_1.jpg` |

## Como escolher
- Cliente leigo, formulário, público idoso → 01. Busca/consulta/conteúdo → 02. Assinatura → 03. Ferramenta do
  advogado → 04 (ou 01 em versão densa via `desktop-app-ui`).
- Site de escritório: qualquer um, desde que obedeça o Provimento 205 (sem ostentação, sem resultado, sem logo da OAB).
