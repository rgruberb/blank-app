# Regulação que afeta a interface — Saúde (SAU)

> **Aviso:** isto não é aconselhamento jurídico nem médico. É um resumo de pesquisa de design (rodada 10B, 27/11/2026)
> para orientar telas. **Confira a norma vigente** e valide com o jurídico/DPO e o responsável técnico do projeto
> antes de publicar. Legenda: ✅ texto oficial lido · 🔒 não verificado (só visto em busca/notícia; PDF não aberto) ·
> "(inferência)" = aplicação nossa.

## LGPD — Lei 13.709/2018
Fonte: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm

| Artigo | O que diz (resumo) | Status | O que muda na tela |
|---|---|---|---|
| Art. 5º, II | dado pessoal "referente à saúde" é **dado pessoal sensível** | ✅ | Tratar toda informação clínica (queixa, exame, receita, histórico, sintoma digitado) como sensível. |
| Art. 11, I | tratamento com consentimento "de forma específica e destacada, para finalidades específicas" | ✅ | Caixa própria por finalidade, não embutida nos termos gerais, nunca pré-marcada (CMP-SAU-05). |
| Art. 11, §4º | vedada comunicação ou uso compartilhado entre controladores de dados sensíveis referentes à saúde — **o texto tem ressalvas que não foram lidas** | ✅ parcial | Não oferecer "compartilhar com parceiros" por padrão; compartilhamento visível no histórico (inferência). |
| Arts. 6º, 8º, 9º, 18 | princípios, consentimento, informação ao titular, direitos do titular (lidos na ficha CRM) | ✅ | Política acessível, revogar consentimento em Configurações, acesso/correção de dados (inferência de aplicação). |

## Conselho Federal de Medicina (CFM)
| Norma | O que se sabe | Status | O que muda na tela |
|---|---|---|---|
| Res. CFM 2.314/2022 (telemedicina) — https://sistemas.cfm.org.br/normas/arquivos/resolucoes/BR/2022/2314_2022.pdf | Segundo notícias do CFM e do CREMERS: paciente ou representante autoriza o atendimento e a transmissão de imagens e dados (termo de consentimento); atendimento registrado em prontuário. Registro em conselho para quem faz telemedicina: resumo do Portal da Indústria (fonte secundária). | 🔒 PDF não aberto; artigos exatos não verificados | Termo de consentimento na sala de espera (CMP-SAU-06); CRM/UF visível (CMP-SAU-01). |
| Res. CFM 2.336/2023 (publicidade médica), em vigor desde março/2024 — https://sistemas.cfm.org.br/normas/arquivos/resolucoes/BR/2023/2336_2023.pdf | Segundo notícia do CFM (https://portal.cfm.org.br/noticias/119781) e CREMERS: permite "antes e depois" com finalidade educativa e condições (indicações, evoluções satisfatórias e insatisfatórias, complicações); permite divulgar preço de consulta; exige autorização do paciente e privacidade. Menciona Manual de Publicidade Médica. | 🔒 artigos exatos não verificados | Galeria "antes e depois" só educativa, com complicações e autorização; preço pode aparecer no cartão do profissional. |
| Selo de qualidade que induza garantia de resultado | Proibido na publicidade médica segundo apresentação do CRM-PR vista em busca | 🔒 | Não usar selos/garantias de resultado. |

## Outras
- **ANVISA:** não verificado (nenhuma norma aplicável à interface localizada neste escopo).
- **CDC e CONAR** (identificação de publicidade): ver `segmento-publicidade`; não detalhado aqui.
- Conselhos de outras profissões (odontologia, psicologia, fisioterapia, nutrição): **não verificados**. Não presuma que
  as regras do CFM valem para eles.
- Receita digital/atestado eletrônico: norma específica **não verificada**; para tipos de assinatura eletrônica ver
  `segmento-juridico/references/regulacao.md` (Lei 14.063/2020).

## Checklist de tela (inferência sobre o que foi lido)
- [ ] Consentimento de dado de saúde separado, por finalidade, não marcado, com recusar de mesmo peso.
- [ ] Caminho para revogar consentimento e ver/baixar dados.
- [ ] Nenhum compartilhamento com terceiros ligado por padrão.
- [ ] Teleconsulta com termo de consentimento antes de entrar.
- [ ] CRM e UF do profissional visíveis.
- [ ] Sem promessa de resultado, selo de garantia ou urgência falsa.
