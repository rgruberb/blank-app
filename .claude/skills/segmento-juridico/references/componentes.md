# Componentes JUR

Lista-base da ficha JUR (10B §14) + componentes vistos nas imagens (C2–C4). "Regras" sem fonte explícita são
(inferência). Plataformas: W = website, D = app desktop, M = app mobile.

## CMP-JUR-01 — Busca jurídica única
- **Anatomia:** um campo para nome, CPF, CNPJ ou nº do processo; ícone de busca; atalhos de intenção em pílula ("Acompanhar meu processo", "Conferir uma pessoa ou empresa", "Resolver um problema"); filtros (tribunal, data, tipo) na página de resultado.
- **Estados:** vazio · digitando (detectar formato CNJ/CPF/CNPJ) · sem resultado · erro de formato descrito em texto.
- **Regras:** placeholder diz os 4 tipos aceitos, mas rótulo acessível existe; buscar pessoa por CPF envolve dado pessoal — mostrar finalidade/aviso LGPD (inferência).
- **Plataformas:** W, D, M. **Refs:** `10C_JUR_jusbrasil_home-busca-processo_1.jpg`.

## CMP-JUR-02 — Linha do tempo do processo
- **Anatomia:** nº CNJ no topo, partes, tribunal/vara, eventos (movimentações) em ordem com data completa, tipo e texto original + resumo em linguagem simples.
- **Estados:** atualizado em [data] · sem movimentação · segredo de justiça (conteúdo oculto, explicar).
- **Regras:** sempre fonte e data de atualização; resumo nunca substitui o texto original (inferência).
- **Plataformas:** W, D, M. **Refs:** ficha 10B §6, §14.

## CMP-JUR-03 — Cartão de prazo
- **Anatomia:** ato/prazo, processo, **data final** (`dd/mm/aaaa`), **dias restantes** (úteis ou corridos, dito explicitamente), responsável, status.
- **Estados:** no prazo · vence amanhã · vencido · cumprido · bloqueado (motivo).
- **Regras:** data final sempre escrita; status em cor + texto; nada piscando ou contando segundos (10B §5).
- **Plataformas:** D, M. **Refs:** `10C_JUR_dribbble-mara-bureau_painel-prioridades-ia_1.jpg` ("Due Tomorrow — Filing deadline approaching", "Blocked — Signature page still missing").

## CMP-JUR-04 — Leitor de peça com anotações
- **Anatomia:** documento em coluna estreita, índice/cláusulas à esquerda, anotações e comentários à direita, busca no documento, versão.
- **Estados:** leitura · anotando · comparando versões (redlines) · somente leitura.
- **Regras:** corpo 19px em desktop (GOV.UK); nada se move durante a leitura (10B §5); comparação de versões explícita.
- **Plataformas:** D (M só leitura). **Refs:** ficha 10B §14; "New redlines" no Mara Bureau.

## CMP-JUR-05 — Seletor do tipo de assinatura
- **Anatomia:** opções **simples**, **avançada**, **qualificada (ICP-Brasil)**, cada uma com uma frase do que significa e o que exige (certificado digital, etc.).
- **Estados:** disponível · indisponível (motivo, ex.: sem certificado) · selecionada.
- **Regras:** definições da Lei 14.063/2020 art. 4º ✅; a lei trata de interações com entes públicos — dizer qual tipo vale para o caso é responsabilidade do jurídico do projeto (inferência).
- **Plataformas:** W, D, M. **Refs:** ficha 10B §9.

## CMP-JUR-06 — Fluxo revisar → assinar → concluir
- **Anatomia:** etapa 1 documento completo (rolagem/índice), etapa 2 identificação + tipo de assinatura + botão "Assinar contrato", etapa 3 confirmação com cópia, hash/ID e trilha.
- **Estados:** não revisado (botão desabilitado com motivo) · assinando · assinado · recusado · expirado.
- **Regras:** nunca "Assinar" sem acesso ao documento inteiro; botão com verbo + objeto; sem animação no botão (10B §5, §11).
- **Plataformas:** W, M, D. **Refs:** padrão de etapas em `mobile-app-ui/references/mobile-patterns.md` §8.

## CMP-JUR-07 — Trilha de auditoria do documento
- **Anatomia:** lista de eventos (enviado, visualizado, assinado, recusado) com quem, quando (data/hora + fuso), tipo de assinatura e identificador.
- **Estados:** em andamento · concluído · com pendência.
- **Regras:** visível e exportável (inferência apoiada na Lei 14.063/2020).
- **Plataformas:** W, D. **Refs:** ficha 10B §8.

## CMP-JUR-08 — Aviso ético de publicidade (rodapé de escritório)
- **Anatomia:** nome do escritório/advogado, nº de inscrição na OAB e seccional (texto), aviso de caráter informativo, link de privacidade.
- **Estados:** único.
- **Regras:** **sem logotipo ou símbolos oficiais da OAB** (art. 5º §2º ✅); texto sóbrio e informativo (art. 3º §1º ✅); conteúdo exato do aviso: não definido pela fonte (inferência).
- **Plataformas:** W. **Refs:** ficha 10B §14.

## CMP-JUR-09 — Painel de prioridades do dia
- **Anatomia:** título ("Prioridades de hoje"), 4 contagens (prazos da semana, ações pendentes, documentos para revisar, aguardando cliente), lista "Precisa de atenção" com status, linha do tempo do dia.
- **Estados:** sem pendências · pendências · item bloqueado.
- **Regras:** prazos e bloqueados antes de qualquer relatório (C4); contagem com rótulo por extenso.
- **Plataformas:** D. **Refs:** `10C_JUR_dribbble-mara-bureau_painel-prioridades-ia_1.jpg`.

## CMP-JUR-10 — Assistente jurídico lateral
- **Anatomia:** painel à direita, pedido do usuário, resumo de risco (cláusulas de alto risco, itens a esclarecer, cláusula ausente), barra de risco geral, campo "cole um documento ou pergunte".
- **Estados:** vazio · analisando · resultado · erro.
- **Regras:** **ao lado** do trabalho, não no lugar (C4); resumo aponta para as cláusulas; deixar claro que não substitui revisão do advogado (inferência).
- **Plataformas:** D. **Refs:** `10C_JUR_dribbble-mara-bureau_painel-prioridades-ia_1.jpg`; botão "Ask Harvey" em `10C_JUR_harvey_command-center-dashboard_1.jpg`.

## CMP-JUR-11 — Grade de números de confiança
- **Anatomia:** 3–5 números grandes em peso leve com régua e legenda (usuários, países, aprovação por entidades, nota).
- **Estados:** único.
- **Regras:** só números verificáveis; em **site de escritório** evitar números de resultados/vitórias (art. 4º §2º ✅) — vale para legaltech como empresa de software (inferência).
- **Plataformas:** W. **Refs:** `10C_JUR_clio_home-numeros-confianca_1.jpg`.

## CMP-JUR-12 — Alternância de público
- **Anatomia:** segmentado "Para todos / Para advogados" acima do título, mudando texto e busca.
- **Estados:** leigo · profissional.
- **Regras:** linguagem de cada público; mesma busca de base (C2).
- **Plataformas:** W. **Refs:** `10C_JUR_jusbrasil_home-busca-processo_1.jpg`.

## CMP-JUR-13 — Termo explicado (glossário inline)
- **Anatomia:** termo técnico sublinhado → explicação curta (popover acessível por teclado ou expansão em linha) + link para glossário.
- **Estados:** fechado · aberto.
- **Regras:** explicação em 1–2 frases; não usar tooltip só no hover (mobile e teclado) (inferência; NN/g evita tooltip para erro).
- **Plataformas:** W, D, M. **Refs:** ficha 10B §10–11 ("juridiquês sem explicação").
