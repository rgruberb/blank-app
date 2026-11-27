---
name: segmento-juridico
description: 'Camada de SEGMENTO jurídico (código JUR) para qualquer empresa do setor — escritório de advocacia, departamento jurídico, legaltech, consulta processual, gestão de processos e prazos, contratos e assinatura eletrônica. Traz tom sóbrio e claro, paleta medida (GOV.UK #1D70B8/#0B0C0C, Jusbrasil #0F172A/#007A5F, DocuSign, Clio), corpo 19px/16px (GOV.UK), leitura longa em coluna estreita, motion mínimo e nunca em prazo/valor/assinar, Provimento OAB 205/2021 (sem preço como gancho, sem promessa de resultado, sem logo da OAB), tipos de assinatura da Lei 14.063/2020, linguagem simples, templates TPL-JUR e componentes CMP-JUR. Use em "escritório de advocacia", "site de advogado", "jurídico", "advogado", "processos", "prazos", "consulta processual", "contratos", "assinatura eletrônica", "legaltech", "OAB", "petição".'
---

# Segmento: Jurídico (JUR)

Skill de **segmento**: o que muda quando o produto é jurídico, para qualquer empresa do setor. Não repete as regras
gerais: plataforma (`website-ui`, `desktop-app-ui`, `mobile-app-ui`) e tema (`design-direction`, `ui-motion`,
`ux-patterns`, `dashboard-ui`) continuam valendo. Fontes: ficha JUR da rodada 10B (GOV.UK, Jusbrasil, DocuSign, Clio,
Provimento OAB 205/2021, Lei 14.063/2020; 27/11/2026) e imagens das rodadas C2–C4. "(inferência)" = conclusão nossa.

## Código
**JUR.** Templates `TPL-JUR-NN`, componentes `CMP-JUR-NN`. Referências de imagem podem receber `REF-JUR-NN` no
`references/visual-index.md` (coluna vazia, a preencher).

## Quando usar
- Site de escritório/advogado (sob o Provimento 205), consulta processual/jurisprudência, gestão de processos, prazos
  e faturamento, leitor de peças/contratos, fluxo de assinatura eletrônica, portal do cliente do escritório.

## Prioridade
skill de app específico > **segmento (esta)** > plataforma > tema > skills de terceiros (`ext-*`). Em conflito, esta
skill vence (ex.: "um momento animado por página" do `website-ui` não vale em botão de assinar nem em prazo).

## Tom
Sóbrio, claro, rigoroso, discreto, confiável. O usuário espera precisão e ausência de ambiguidade. Para advogado, a
norma pede publicidade **"sóbria, discreta e informativa"** (Provimento 205/2021, art. 3º §1º ✅). Cliente leigo:
"sem juridiquês" (Jusbrasil, imagem C2).

## Regras centrais
**Paleta (hex medidos por `getComputedStyle` em páginas públicas, 10B)**
- GOV.UK: azul `#1D70B8` `#1A65A6`, verde `#0F7A52`, texto `#0B0C0C` `#484949`, fundo `#F4F8FB`.
- Jusbrasil: marinho `#0F172A`, verde `#007A5F` `#00A37F`, fundo `#F1F5F9`, texto `#455468` `#5C6F8A`.
- DocuSign (BR): roxo-escuro `#130032`, violeta `#4C00FF`, fundo `#F8F3F0`, `#151B17`.
- Clio: preto `#000000`, azul `#1A56FF` `#012587`, areia `#F5CE9B`, `#F5F5F5`.
- Padrão: marinho/azul/verde/preto sobre fundo claro. **Evitar** (inferência): dourado e sinais de luxo — o art. 6º
  parágrafo único proíbe **ostentação** (regra de conteúdo, não de cor).

**Tipografia e tamanhos**
- GOV.UK: `GDS Transport` só no gov.uk; fora dele **Helvetica ou Arial**. Parágrafo **19px (tela grande) / 16px
  (pequena)**; menor classe `govuk-body-s` 14px, com moderação. Números tabulares: a página não menciona.
- Jusbrasil `Inter`; DocuSign `DSIndigo` (própria); Clio `Facility` + mono. Harvey usa serifa em títulos e KPIs
  (imagem C3). Use `tabular-nums` em prazos e valores (complemento).

**Densidade**
- **Média, com blocos de texto longo**: coluna estreita para peça/contrato; gestão (processos, prazos) densa
  (inferência). Leitura: medida 45–75 caracteres, `max-width: 60ch` (`ux-patterns/references/typography-and-touch.md`).

**Motion**
- Mínimo; GOV.UK como referência de motion nulo. **Nunca animar** (inferência): prazos, valores, cláusulas, botão de
  assinar; nada se mexe em documento aberto para leitura. `prefers-reduced-motion` sempre.

**Dados e números**
- Número CNJ e datas completas; prazo com **data final explícita + dias restantes**; valores em R$ com centavos; fonte
  e data de atualização do dado (inferência). Formato do nº de processo: regra **não verificada**.

**Confiança**
- Advogado: títulos **"verdadeiros e comprováveis"** (art. 4º §1º ✅); sem resultados nem casos concretos.
- Assinatura: **tipo de assinatura e trilha de auditoria visíveis** (inferência, apoiada na Lei 14.063/2020).
- Legaltech: números de produto verificáveis (Clio "50 U.S. state bar associations have approved"); para escritório,
  números de resultado esbarram no art. 4º §2º (inferência).

**Regulação (resumo; detalhe em `references/regulacao.md` — não é aconselhamento jurídico)**
- Provimento OAB 205/2021 ✅: sem captação/mercantilização (art. 3º); sem honorários como gancho (art. 3º I); sóbria e
  informativa (§1º); sem decisões e resultados (art. 4º §2º); **sem logotipo/símbolos da OAB** (art. 5º §2º); sem casos
  concretos em vídeo/palestra (art. 5º §3º); sem promessa de resultado nem ostentação (art. 6º).
- Lei 14.063/2020 art. 4º ✅: assinatura **simples**, **avançada** e **qualificada** (ICP-Brasil); a lei trata de
  entes públicos — aplicação a contratos privados é inferência. MP 2.200-2/2001: não verificada.
- LGPD: aviso e consentimento onde houver dado pessoal de cliente/parte (✅ lida na ficha SAU/CRM).

**Linguagem simples e acessibilidade**
- Termo técnico com explicação em linha ou glossário; frase curta; verbo no botão ("Assinar contrato") (inferência;
  diretrizes de escrita do GOV.UK **não lidas** — redirecionaram 🔒). NN/g: nível 6º–8º ano em formulário (§5).
- Corpo 19px/16px, coluna estreita, contraste forte, foco visível, erro descrito em texto ao lado do campo.
- Cliente leigo e idoso: glossário, alternativa humana, nada de prazo só em cor (inferência).

## Diferenças por plataforma
| | O que domina | Ajuste JUR |
|---|---|---|
| Website | captação (sob o Provimento) e consulta pública | sem preço/resultado/logo OAB; busca única por processo; aviso ético no rodapé |
| App desktop | gestão de processos, peças, faturamento (inferência; Clio e Jusbrasil se dizem plataformas) | painel "prioridades do dia", leitor com anotações, tabela de prazos |
| App mobile | andamento, notificação de prazo, assinar documento | assinatura com revisão antes; notificação com data final, sem alarme falso |

## Templates (detalhe em `references/templates.md`)
`TPL-JUR-01` Sóbrio institucional (GOV.UK) · `TPL-JUR-02` Legaltech editorial (Jusbrasil) · `TPL-JUR-03` Contrato
digital (DocuSign) · `TPL-JUR-04` Gestão moderna de escritório (Clio).

## Componentes (detalhe em `references/componentes.md`)
`CMP-JUR-01` Busca jurídica única · `02` Linha do tempo do processo · `03` Cartão de prazo · `04` Leitor de peça com
anotações · `05` Seletor do tipo de assinatura · `06` Fluxo revisar → assinar → concluir · `07` Trilha de auditoria ·
`08` Aviso ético de publicidade · `09` Painel de prioridades do dia · `10` Assistente jurídico lateral · `11` Grade de
números de confiança · `12` Alternância de público · `13` Termo explicado (glossário inline).

## Anti-padrões
- Juridiquês sem explicação; prazo só em cor; contagem regressiva falsa.
- Botão "Assinar" sem revisão do documento; tipo e efeito da assinatura escondidos.
- Site de escritório com preço/desconto como gancho, "resultados garantidos", vitórias e casos, logo da OAB, luxo.
- Animação em documento aberto, em prazo ou no botão de assinar.
- Assistente de IA no lugar do trabalho (Mara Bureau o põe **ao lado**, não por cima).

## Workflow
1. Identifique: site de escritório (Provimento manda), produto para cliente leigo (linguagem simples) ou ferramenta
   do advogado (densidade, prazos).
2. Escolha um `TPL-JUR`, declare tokens, confira contraste.
3. Monte com `CMP-JUR` + skill de plataforma.
4. Checklist: Provimento (site) · tipo de assinatura + auditoria · prazo com data final · nada animado em
   prazo/valor/assinar · glossário · 19/16px.
5. Confira `references/regulacao.md` e a norma vigente antes de publicar.

## Onde está o resto
- `references/templates.md` · `references/componentes.md` · `references/regulacao.md` · `references/fontes.md` ·
  `references/visual-index.md` (4 imagens próprias + imagens em outras skills).
- Tabelas, painel lateral, ⌘K, atalhos: `desktop-app-ui`; KPIs e "needs attention": `dashboard-ui`
  (`references/layout-patterns.md`).
- Formulários, erros, confiança, linguagem simples: `ux-patterns/references/nng-research.md` §5, §8, §11;
  dark patterns: `ux-patterns/references/dark-patterns.md`.
- Confiança e footer de site: `website-ui/references/website-patterns.md` §2, §7. Assinatura no celular:
  `mobile-app-ui/references/mobile-patterns.md` §8–9. Dado sensível de saúde em processo: `segmento-saude`.
