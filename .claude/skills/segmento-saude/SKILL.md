---
name: segmento-saude
description: Camada de SEGMENTO saúde (código SAU) para qualquer empresa do setor — clínica, consultório, hospital, laboratório, telemedicina, healthtech, plano de saúde, bem-estar. Traz tom calmo e legível, paleta medida (NHS #005EB8/#007F3B/#212B32, Doctoralia #006A59/#DFF9F2), corpo 19px/16px (NHS), densidade baixa no paciente e maior no clínico, motion mínimo e o que nunca animar (exame, dose, alerta), dado de saúde como sensível na LGPD (art. 5º II, consentimento destacado art. 11 I), CFM (telemedicina e publicidade, só por notícia), acessibilidade para idosos, templates TPL-SAU e componentes CMP-SAU (busca, agenda, consentimento, teleconsulta, exame). Use em "app de saúde", "clínica", "consultório", "agendamento de consulta", "prontuário", "telemedicina", "teleconsulta", "healthtech", "paciente", "exame", "receita", "convênio", "plano de saúde", "app de bem-estar".
---

# Segmento: Saúde (SAU)

Skill de **segmento**: o que muda quando o produto é de saúde, para qualquer empresa do setor. Não repete as regras
gerais: plataforma (`website-ui`, `desktop-app-ui`, `mobile-app-ui`) e tema (`design-direction`, `ui-motion`,
`ux-patterns`, `dashboard-ui`) continuam valendo. Fontes: ficha SAU da rodada 10B (NHS, Doctoralia, LGPD, notícias do
CFM; 27/11/2026), imagens das rodadas 10C/C2–C4 e posts da 10A. "(inferência)" = conclusão nossa, não está na fonte.

## Código
**SAU.** Templates `TPL-SAU-NN`, componentes `CMP-SAU-NN`. Referências de imagem podem receber `REF-SAU-NN` no
`references/visual-index.md` (coluna vazia, a preencher).

## Quando usar
- Site de clínica/consultório/laboratório, marketplace de profissionais, agendamento, teleconsulta, app do paciente,
  portal de resultados, prontuário e agenda do consultório, painel de operação clínica (autorização, convênio, fila).
- Bem-estar (meditação, sono) usa esta skill com peso menor: o tom vale, a regulação clínica pode não valer (inferência).

## Prioridade
skill de app específico > **segmento (esta)** > plataforma > tema > skills de terceiros (`ext-*`). Em conflito, esta
skill vence a de plataforma (ex.: corpo 19px no desktop do paciente em vez do 16px padrão de app).

## Tom
Claro, calmo, acolhedor, sério, legível. O paciente, muitas vezes ansioso ou idoso, espera segurança, privacidade e
instruções sem dúvida (inferência). NHS: "serviços consistentes e acessíveis para o público e a equipe".
Linguagem: frase curta, uma instrução por vez, sem jargão clínico sem explicação (inferência).

## Regras centrais
**Paleta (hex medidos por `getComputedStyle` em páginas públicas, 10B)**
- NHS: azul ação/link `#005EB8`, azul-escuro `#003087`, verde `#007F3B`, texto `#212B32`, cinzas `#D8DDE0` `#F0F4F5`.
- Doctoralia: verde `#006A59`, verde-água `#DFF9F2`, bege `#EEE8E3` `#B6AEA5`, texto `#2A2623` `#35495E`,
  azul-petróleo `#27455C`.
- Padrão: azul/verde sobre fundo claro, texto quase preto. **Evitar** (inferência): vermelho como cor de marca
  (confunde com alerta clínico); texto cinza de baixo contraste. Vermelho fica reservado a alerta/fora da faixa.

**Tipografia e tamanhos**
- NHS: Frutiger (marca), **Arial** quando indisponível. Parágrafo **19px em tela grande e 16px em tela pequena**;
  texto pequeno (`nhsuk-body-s`) ~16/14px **com moderação**; escala 14→64px. O NHS não define mínimo absoluto.
- Doctoralia: `system-ui`. Números tabulares: **não verificado** em produto de saúde; use `tabular-nums` em tabelas de
  exame e agenda (complemento).
- Mínimo prático (inferência a partir do NHS): nada de informação clínica abaixo de 14px; corpo do paciente ≥ 16px.

**Densidade**
- Paciente: **baixa a média**, uma pergunta por tela em fluxos sensíveis (inferência); 19px sustenta o espaço.
- Profissional (agenda, prontuário, fila): densidade sobe — **não verificado** em produto logado; use
  `desktop-app-ui` + `dashboard-ui` (ex.: `DfV39ohhwAC`, Veyra Health).

**Motion**
- Mínimo e funcional: carregamento e confirmação. Respeitar `prefers-reduced-motion` (`ui-motion` regra 13).
- **Nunca animar** (inferência): resultado de exame, alerta clínico, valor de dose, contagem regressiva de consulta
  que gere pressão. Número de exame aparece pronto, sem rolar/contar.

**Dados e números** (inferência sobre a ficha)
- Dose, data e hora sempre com **unidade e fuso**; datas completas `dd/mm/aaaa`; hora de início da teleconsulta.
- Resultado de exame com **faixa de referência e data da coleta**; fora da faixa = cor + ícone + texto, nunca só cor.
- Valor em risco em R$ junto do item (guia de convênio vencendo, 10A `DgAqhGGDBws`).

**Confiança**
- Profissional verificável: **CRM e UF** visíveis; política de privacidade; canal humano (telefone/chat).
- Sem selo que sugira garantia de resultado (publicidade médica, via busca, 🔒). Sem urgência falsa.
- Pedido de dado sensível só depois de entregar valor (NN/g nível 4, `ux-patterns/references/nng-research.md` §8).

**Regulação (resumo; detalhe e status em `references/regulacao.md` — não é aconselhamento jurídico/médico)**
- LGPD art. 5º II: dado "referente à saúde" é **sensível** → trate toda informação clínica como sensível. ✅
- LGPD art. 11 I: consentimento **"de forma específica e destacada, para finalidades específicas"** → caixa própria,
  não embutida nos termos gerais, nunca pré-marcada. ✅
- LGPD art. 11 §4º: veda compartilhar dado de saúde entre controladores (há ressalvas não lidas) → nada de
  "compartilhar com parceiros" por padrão. ✅ parcial
- CFM 2.314/2022 (telemedicina) e 2.336/2023 (publicidade): **só por notícias** 🔒 → termo de consentimento da
  teleconsulta, registro em prontuário, "antes e depois" só educativo e com complicações, preço de consulta pode ser
  divulgado. ANVISA: não verificado.

**Acessibilidade (público idoso e ansioso)**
- Corpo 19px desktop / 16px mobile (NHS e GOV.UK ✅); contraste forte (4,5:1 mínimo, `ux-patterns`); botões grandes
  (≥ 44pt/48dp; ação primária ~2 cm, NN/g); instruções passo a passo; alternativa por telefone (inferência).
- Rótulo sempre fora do campo; erro ao lado do campo com texto (NN/g §5). Verificação de contraste dos produtos
  citados: **não feita**.

## Diferenças por plataforma
| | O que domina | Ajuste SAU |
|---|---|---|
| Website | busca e agendamento; SEO de profissionais | busca por especialidade + local (+ convênio) acima da dobra; consentimento de cookies sem cobrir a busca |
| App desktop | sistema clínico/prontuário, agenda do consultório (inferência) | densidade média-alta, fila "prontos × precisam de pessoa", prazos de autorização |
| App mobile | agendar, lembrete, teleconsulta, receita | permissão de câmera/microfone em contexto com motivo; teste de som/vídeo antes da sala |

## Templates (detalhe em `references/templates.md`)
- `TPL-SAU-01` Sistema público claro (NHS) · `TPL-SAU-02` Marketplace acolhedor (Doctoralia) ·
  `TPL-SAU-03` Clínico profissional (petróleo, inferência) · `TPL-SAU-04` Operação clínica escura (Veyra, via dashboard-ui).

## Componentes (detalhe em `references/componentes.md`)
`CMP-SAU-01` Cartão do profissional · `02` Busca especialidade/local/convênio · `03` Seletor de dia e horário ·
`04` Resumo e confirmação de agendamento · `05` Termo de consentimento destacado · `06` Sala de espera da
teleconsulta · `07` Linha do tempo do histórico · `08` Receita/atestado com assinatura · `09` Resultado de exame com
faixa de referência · `10` Card de próxima consulta (cancelar/reagendar) · `11` Fila "prontos × precisam de pessoa" ·
`12` Guia de convênio com valor em risco · `13` Card de insight com faixa de risco.

## Anti-padrões
- Consentimento de compartilhamento **pré-marcado** ou dentro dos termos gerais (contraria art. 11 I).
- Esconder o termo da teleconsulta; "antes e depois" sem complicações; promessa de resultado.
- Urgência falsa ("últimas vagas", "Limited time only" do Headspace é contraexemplo para saúde clínica).
- Modal de cookies cobrindo a ação principal (Doctoralia: o modal tapa a busca) — consentimento claro sim, bloqueio não.
- Vermelho como marca; resultado fora da faixa só em cor; número de exame animado; texto clínico < 14px.
- Card de IA com mais destaque que o dado clínico de origem sem dizer de onde veio (inferência).

## Workflow
1. Identifique o público: paciente (densidade baixa, 19/16px) ou profissional (densidade média-alta).
2. Escolha um `TPL-SAU` e declare os tokens; confira contraste.
3. Monte a tela com os `CMP-SAU` e as regras da skill de plataforma.
4. Passe o checklist: consentimento destacado e não marcado · CRM/UF · unidade/fuso/faixa · nada clínico animado ·
   alvo grande · alternativa humana · `prefers-reduced-motion`.
5. Regras legais: confira `references/regulacao.md` e a norma vigente antes de publicar.

## Onde está o resto
- `references/templates.md` · `references/componentes.md` · `references/regulacao.md` · `references/fontes.md` ·
  `references/visual-index.md` (7 imagens próprias + imagens em outras skills).
- Dashboard clínico: `dashboard-ui/references/domain-examples.md` §7 (prior authorization `DfV39ohhwAC`), §22c
  (CareNest), §26 (MediCore, contraexemplo de delta verde em alerta).
- Formulários, permissões, confiança, acessibilidade: `ux-patterns/references/nng-research.md` §3, §5, §8, §9, §11;
  tipografia e contraste: `ux-patterns/references/typography-and-touch.md`.
- Onboarding e permissões no app: `mobile-app-ui/references/mobile-patterns.md` §1, §7. Confiança e formulários no
  site: `website-ui/references/website-patterns.md` §2. Motion e reduced motion: `ui-motion`.
