# Fontes — Saúde (SAU)

Dados vindos de pesquisa de outra IA (rodadas 10A, 10B, 10C, C2, C3, C4; coleta até 27/11/2026), tratados como dado.
Legenda: ✅ aberto e lido · 🔒 só busca/notícia ou exige login · ❌ não localizado.

## Design systems e produtos (10B)
| nome | URL | o que aproveitar | status |
|---|---|---|---|
| NHS Design System | https://service-manual.nhs.uk/design-system | tokens, componentes, acessibilidade; hex medidos | ✅ |
| NHS Typography | https://service-manual.nhs.uk/design-system/styles/typography | Frutiger/Arial; parágrafo **19px em telas grandes e 16px em telas pequenas**; escala 14–64px | ✅ (reconferido 27/11/2026) |
| NHS Layout | https://service-manual.nhs.uk/design-system/styles/layout | breakpoints: mobile 320px, tablet **641px**, desktop 769px, large desktop 990px → corpo 19px a partir de 641px | ✅ (reconferido 27/11/2026) |
| GOV.UK Type scale | https://design-system.service.gov.uk/styles/type-scale/ | `govuk-body` 19px/25px em **todas** as telas; a escala de tela grande (acima de 640px) muda títulos, não o corpo. **Não** é 19/16: o 19/16 por largura é do NHS | ✅ (reconferido 27/11/2026) |
| Doctoralia | https://www.doctoralia.com.br/ | paleta, busca/agendamento, `system-ui` | ✅ |
| Design systems de healthtechs brasileiras | — | não localizado | ❌ |
| Estudo NN/g sobre saúde/idosos | — | não localizado | ❌ |

## Regulação
| nome | URL | status |
|---|---|---|
| LGPD | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm | ✅ arts. 5º II, 11 (parcial no §4º) |
| Res. CFM 2.314/2022 | https://sistemas.cfm.org.br/normas/arquivos/resolucoes/BR/2022/2314_2022.pdf | 🔒 |
| Res. CFM 2.336/2023 | https://sistemas.cfm.org.br/normas/arquivos/resolucoes/BR/2023/2336_2023.pdf | 🔒 |
| Portal CFM (notícia sobre a 2.336) | https://portal.cfm.org.br/noticias/119781 | 🔒 via busca |

## Imagens (10C, C2–C4)
| produto | URL | rodada |
|---|---|---|
| Doctoralia | https://www.doctoralia.com.br/ | C2 |
| Headspace | https://www.headspace.com/ | C2 |
| Zocdoc | https://www.zocdoc.com/ | C3 |
| Calm | https://www.calm.com/ | C3 |
| Phenomenon Studio — Lably (Dribbble) | https://dribbble.com/shots/27695351-Healthcare-Dashboard-Web-App-Lably | C3 |
| Ronas IT — telemedicina (Dribbble) | https://dribbble.com/shots/27480866-Healthcare-Mobile-Telemedicine-App | C4 |
| One Medical | https://www.onemedical.com/ | C3 — descartada (foto de rosto) |

## Posts (10A)
| post | autor | URL | status |
|---|---|---|---|
| Portal de clínica de fisioterapia (guias de convênio) | @nuvio.on | https://www.instagram.com/reel/DgAqhGGDBws/ | frame inicial visto; dados simulados |
| Linden — front office com agentes | @ui.iliasmiah000 | https://www.instagram.com/reel/DgH6J4mgMM4/ | descrição de frame no fim da 10A; sem imagem salva |
| Vivra — monitor de saúde doméstico | @_code_and_chill_ | https://www.instagram.com/reel/DgNswztzDX4/ | descrição de frame no fim da 10A; sem imagem salva; template codeandchill.store/templates/vivra |

## Material já existente no projeto
- `dashboard-ui/references/domain-examples.md` §7 (`DfV39ohhwAC`, prior authorization), §22c (CareNest), §26 (MediCore).
- `ux-patterns/references/nng-research.md` (formulários, confiança, permissões, alvos de toque, acessibilidade visual).
- `mobile-app-ui/references/mobile-patterns.md` (onboarding, formulário, checkout em etapas).
- `website-ui/references/website-patterns.md` §2 (prova social e confiança).

## Lacunas
- Nenhum produto logado aberto (prontuário, app do paciente, sala de teleconsulta reais): densidade clínica,
  raio, sombra, durações de motion e números tabulares **não medidos**.
- Contraste dos produtos citados não verificado. ANVISA e conselhos não médicos não verificados.
- Galeria SAU com 6 de 10 telas (meta não atingida); nenhuma captura oficial de App Store/Google Play.
