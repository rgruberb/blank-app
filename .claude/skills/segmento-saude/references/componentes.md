# Componentes SAU

Lista-base da ficha SAU (10B §14) + componentes vistos nas imagens (10C, C2–C4, 10A). "Regras" sem fonte explícita são
(inferência). Plataformas: W = website, D = app desktop, M = app mobile.

## CMP-SAU-01 — Cartão do profissional
- **Anatomia:** foto (ou iniciais), nome, especialidade, **CRM + UF**, local/teleconsulta, convênios, preço (se divulgado), nota e nº de avaliações, botão "Agendar".
- **Estados:** padrão · sem horário disponível · só teleconsulta · indisponível.
- **Regras:** CRM/UF sempre visível (confiança, 10B §8); nota com número de avaliações, nunca estrelas soltas; preço de consulta pode ser divulgado (notícia CFM 🔒).
- **Plataformas:** W, M (D na recepção). **Refs:** Doctoralia (10B), `10C_SAU_dribbble-ronas-it_telemedicina-agenda-mobile_1.jpg` (foto + "4.9 · 355 reviews").

## CMP-SAU-02 — Busca especialidade / local / convênio
- **Anatomia:** abas tipo de atendimento ("No local" / "Teleconsulta"), campo "especialidade, doença ou nome", campo local (preenchido automaticamente), campo convênio, botão de busca; abaixo, especialidades e convênios em lista com "Mais".
- **Estados:** vazio · digitando com sugestões · sem resultado (oferecer teleconsulta/outro local) · local negado.
- **Regras:** busca é a ação principal acima da dobra; convênio entra desde o início (Zocdoc); modal de cookies não pode cobrir o campo; rótulo visível acima do campo.
- **Plataformas:** W, M. **Refs:** `10C_SAU_doctoralia_home-busca-especialista_1.jpg`, `10C_SAU_zocdoc_home-busca-seguro-saude_1.jpg`.

## CMP-SAU-03 — Seletor de dia e horário
- **Anatomia:** faixa de dias (dia da semana + número), horários em pílulas, fuso quando teleconsulta, "Ver todos".
- **Estados:** disponível · selecionado · indisponível (riscado/desabilitado com texto) · carregando.
- **Regras:** pílula ≥ 44pt/48dp; data completa no resumo; nada de "últimas vagas"; teclado/leitor de tela navegam por dia e horário.
- **Plataformas:** W, M. **Refs:** `10C_SAU_dribbble-ronas-it_telemedicina-agenda-mobile_1.jpg`.

## CMP-SAU-04 — Resumo e confirmação de agendamento
- **Anatomia:** profissional, data `dd/mm/aaaa`, hora + fuso, local ou link, preparo, valor/convênio, política de cancelamento, lembrete (e-mail/SMS/WhatsApp), botão "Confirmar".
- **Estados:** revisão · enviando · confirmado (com "adicionar à agenda") · falhou (motivo + tentar de novo).
- **Regras:** confirmação sem animação festiva; texto claro do que acontece depois (10B §6).
- **Plataformas:** W, M. **Refs:** ficha 10B; checkout em etapas em `mobile-app-ui/references/mobile-patterns.md` §8.

## CMP-SAU-05 — Termo de consentimento destacado
- **Anatomia:** título da finalidade, texto curto em linguagem simples, link para o termo completo, caixa **não marcada** por finalidade, botões de aceitar e recusar com o mesmo peso, data/hora do aceite registrada.
- **Estados:** não lido · aceito · recusado (explicar o que deixa de funcionar) · revogado (caminho em Configurações).
- **Regras:** "específica e destacada, para finalidades específicas" (LGPD art. 11 I ✅); uma caixa por finalidade; nada embutido nos termos gerais; compartilhar com terceiros nunca por padrão (art. 11 §4º, parcial).
- **Plataformas:** W, D, M. **Refs:** `10C_SAU_doctoralia_home-busca-especialista_1.jpg` ("Recusar todas" com peso igual a "Aceitar"; cookies, não dado clínico).

## CMP-SAU-06 — Sala de espera da teleconsulta
- **Anatomia:** nome do profissional, horário, status ("o profissional vai entrar"), teste de câmera/microfone/rede, termo de consentimento da teleconsulta, chat, botão sair.
- **Estados:** antes do horário · pronto · profissional atrasado · conexão ruim · permissão negada.
- **Regras:** pedir câmera/microfone **no contexto** com motivo (NN/g §9); permissão negada → explicar e levar às configurações; consentimento do paciente para atendimento e transmissão (CFM 2.314 via notícia 🔒); sem contador regressivo de pressão.
- **Plataformas:** W, M. **Refs:** `../../ux-patterns/assets/visual-refs/9B_permissoes_venmo-camera-negada_1.jpg`.

## CMP-SAU-07 — Linha do tempo do histórico
- **Anatomia:** eventos em ordem cronológica (consulta, exame, receita, compartilhamento), data, profissional, ícone por tipo, filtro.
- **Estados:** vazio (explicar como aparecerá) · carregando · item compartilhado (quem e quando).
- **Regras:** registrar e mostrar compartilhamentos ("Report shared … via patient link" no Lably); datas completas.
- **Plataformas:** W, D, M. **Refs:** `10C_SAU_dribbble-phenomenon-lably_dashboard-exames-ia_1.jpg` (feed), `10C_SAU_dribbble-ronas-it_telemedicina-agenda-mobile_1.jpg` ("Visits history").

## CMP-SAU-08 — Receita / atestado com assinatura
- **Anatomia:** dados do profissional (CRM/UF), paciente, itens com dose e unidade, data, assinatura digital e forma de verificar, baixar/compartilhar.
- **Estados:** válido · expirado · assinatura pendente.
- **Regras:** dose sempre com unidade; tipo de assinatura e verificação visíveis (inferência; ver `segmento-juridico` CMP-JUR-05 para tipos de assinatura); norma específica de receita digital **não verificada**.
- **Plataformas:** W, M (emissão em D). **Refs:** ficha 10B §14.

## CMP-SAU-09 — Resultado de exame com faixa de referência
- **Anatomia:** nome do exame, valor + unidade, **faixa de referência**, data da coleta, marcador "fora da faixa" (cor + ícone + texto), histórico em gráfico simples.
- **Estados:** dentro · acima · abaixo · aguardando · liberado pelo laboratório.
- **Regras:** valor nunca animado; não depender só de cor; orientar a procurar o profissional em vez de diagnosticar (inferência).
- **Plataformas:** W, D, M. **Refs:** `10C_SAU_dribbble-phenomenon-lably_dashboard-exames-ia_1.jpg` (LDL 168 mg/L com data; barra de faixa).

## CMP-SAU-10 — Card de próxima consulta
- **Anatomia:** profissional, especialidade, data e hora, local/sala ou link, ações **Cancelar** e **Reagendar** no próprio card.
- **Estados:** agendada · hoje · em andamento (entrar na sala) · cancelada.
- **Regras:** cancelar com confirmação e política visível; reagendar volta ao CMP-SAU-03.
- **Plataformas:** M, W. **Refs:** `10C_SAU_dribbble-ronas-it_telemedicina-agenda-mobile_1.jpg`.

## CMP-SAU-11 — Fila "prontos × precisam de pessoa"
- **Anatomia:** KPI central "X de Y prontos, N precisam de pessoa", contagem em risco, seletor Hoje/Amanhã/Semana, agenda por profissional.
- **Estados:** tudo pronto · itens pendentes · item em risco.
- **Regras:** a fila mostra o que a pessoa precisa fazer agora (10A Linden: 96 de 128 prontas, 7 precisam de pessoa).
- **Plataformas:** D. **Refs:** reel `DgH6J4mgMM4` (sem imagem salva); `../../dashboard-ui/assets/visual-refs/DfV39ohhwAC.jpg` ("Needs attention").

## CMP-SAU-12 — Guia de convênio com valor em risco
- **Anatomia:** linha por guia: paciente, sessões restantes, validade, **valor em risco (R$)**, ação sugerida (encaixe na agenda).
- **Estados:** ativa · vencendo · vencida · autorização pendente.
- **Regras:** ordenar por vencimento; ação na própria linha (10A `DgAqhGGDBws`, dados simulados na demo).
- **Plataformas:** D. **Refs:** `10A_DgAqhGGDBws_1.jpg`.

## CMP-SAU-13 — Card de insight com faixa de risco
- **Anatomia:** título do achado, paciente/origem, barra de faixa com marcador, link para o dado de origem.
- **Estados:** informativo · atenção · crítico.
- **Regras:** dizer de onde veio e quando; o card não substitui o resultado (CMP-SAU-09); destaque de cor cheia só em painel do profissional (inferência).
- **Plataformas:** D. **Refs:** `10C_SAU_dribbble-phenomenon-lably_dashboard-exames-ia_1.jpg`, `../../dashboard-ui/assets/visual-refs/DfUvP_ulPC6_2.jpg`.
