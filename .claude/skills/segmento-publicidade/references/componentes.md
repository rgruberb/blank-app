# Componentes — Publicidade (CMP-PUB)

Formato: anatomia, estados, regras, plataformas, referências. Base: lista de componentes da ficha PUB (10B §14),
fichas de imagem 10C/C2–C4 e `dashboard-ui`. "(inferência)" = conclusão nossa.

---

## CMP-PUB-01 — Hierarquia campanha → conjunto → anúncio
- **Anatomia:** três níveis (campanha: objetivo + orçamento; conjunto: público + posicionamento; anúncio: criativo +
  texto), com breadcrumb ou árvore lateral e contagem de filhos.
- **Estados:** ativo, pausado, em revisão, rejeitado, rascunho, erro de especificação.
- **Regras:** o nível atual sempre visível; editar um nível mostra o impacto nos filhos (inferência).
- **Plataformas:** web (principal); mobile só leitura e pausar.
- **Referências:** 10B PUB §6 (estrutura do Ads Manager).

## CMP-PUB-02 — Seletor de objetivo
- **Anatomia:** lista de objetivos com ícone, nome e uma linha de explicação; um selecionado.
- **Estados:** padrão, hover/foco, selecionado, desabilitado (com motivo).
- **Regras:** primeira decisão do fluxo; nenhuma pré-seleção que aumente gasto (inferência).
- **Plataformas:** web, desktop. **Referências:** 10B PUB §6.

## CMP-PUB-03 — Barra de orçamento (diário/vitalício)
- **Anatomia:** alternância diário × vitalício, campo em moeda, período, estimativa; barra de pacing (gasto ÷ verba).
- **Estados:** normal, perto do limite, estourado, editando.
- **Regras:** moeda explícita; **número não anima enquanto o usuário edita**; valor padrão não deve ser alto
  (inferência); o gasto nunca pode passar do orçamento sem alerta (o conceito Nebula mostra "$12,845 of $5,000
  budget" sem aviso — observação nossa).
- **Plataformas:** web, desktop, mobile (ajuste rápido no app Ads Manager).
- **Referências:** 10B PUB §6, §5; `10C_PUB_dribbble-vektora_nebula-analytics-campanhas_1.jpg`.

## CMP-PUB-04 — Tabela de desempenho com colunas configuráveis
- **Anatomia:** checkbox, ID mono, nome, status em pílula (texto + cor), gasto, resultados, custo por resultado,
  ROAS; cabeçalho ordenável; menu "…" por linha; seletor de colunas e de período.
- **Estados:** carregando (skeleton), vazio, filtrado, linha selecionada, erro.
- **Regras:** `tabular-nums`, números à direita; status com texto, não só cor; período no topo da tabela.
- **Plataformas:** web/desktop (`desktop-app-ui` tabela de dados); no mobile vira lista com 2–3 métricas (inferência).
- **Referências:** Nebula (tabela "Ads sets" com ID, status Active, Spend, Purchases, ROAS); 10B §6.

## CMP-PUB-05 — Linha de KPIs com período e variação
- **Anatomia:** 4 cards (ex.: Spend, Revenue, ROAS, CTR) com rótulo, valor, contexto ("of $X budget") e variação
  "+14,2% vs last period".
- **Estados:** carregando, sem dado, variação positiva/negativa (sinal + cor + texto).
- **Regras:** valor numa linha, `tabular-nums`, `nowrap`, ~30px no máximo em card estreito (10A `Deq_kvJBI3g`);
  moeda e período explícitos; pôr métrica de qualidade ao lado de custo (10B §7); atribuição rotulada.
- **Plataformas:** todas. **Referências:** Nebula; `10A_Deq_kvJBI3g_1.jpg`; `dashboard-ui` §11 (gasto que conta).

## CMP-PUB-06 — Prévia por posicionamento e dispositivo
- **Anatomia:** seletor de posicionamento (Feed, Stories, Reels…) e de dispositivo; prévia em moldura do tamanho real;
  texto truncado como aparecerá.
- **Estados:** carregando mídia, prévia ok, corte de proporção, texto truncado, erro.
- **Regras:** prévia antes de publicar; mostrar onde o texto corta (inferência).
- **Plataformas:** web/desktop. **Referências:** 10B PUB §6 ("prévia por posicionamento e por dispositivo").

## CMP-PUB-07 — Checagem de especificação do criativo
- **Anatomia:** lista de verificação por item: formato (JPG/PNG), proporção (4:5), resolução (1440×1800; mín.
  600×750), peso (≤ 30 MB), texto principal (50–150), título (≤ 27), tolerância de proporção (3%).
- **Estados:** ok, aviso, erro bloqueante.
- **Regras:** contagem de caracteres ao vivo; erro diz o valor atual e o exigido. Os números acima valem para imagem
  no Feed do Facebook (Meta Ads Guide); outros posicionamentos e Google: não verificados.
- **Plataformas:** web/desktop. **Referências:** https://www.facebook.com/business/ads-guide/update/image (10B §7).

## CMP-PUB-08 — Selo "Publicidade/Patrocinado"
- **Anatomia:** rótulo de texto curto ("Publicidade", "Patrocinado") junto ao conteúdo, visível sem interação.
- **Estados:** único (não some no hover, não fica atrás de "ver mais") — inferência.
- **Regras:** CONAR art. 28 e CDC art. 36: anúncio identificável **fácil e imediatamente**, em qualquer formato.
  Termo exato, posição e duração em vídeo: **não verificados** (Guia CONAR de influenciadores não lido).
- **Plataformas:** todas, inclusive peça de vídeo. **Referências:** `regulacao.md`.

## CMP-PUB-09 — Rótulo de parceria paga
- **Anatomia:** rótulo da plataforma ("Parceria paga" no Instagram) + menção à marca.
- **Regras:** a regra oficial da Meta não foi aberta; descrição via fontes secundárias (10B §9). Use junto com o
  `CMP-PUB-08` quando houver dúvida (inferência).
- **Plataformas:** posts e reels. **Referências:** 10B PUB §9.

## CMP-PUB-10 — Receita atribuída por canal + recomendação
- **Anatomia:** tabela de receita por canal (campanhas, fluxos, e-mail, SMS, WhatsApp) com valor e %; card de
  recomendação com motivo e CTA ("criar fluxo").
- **Estados:** com recomendação, sem recomendação, carregando.
- **Regras:** recomendação explica o porquê e **não é aplicada sozinha** (inferência; anti-padrão 10B §11); janela
  de atribuição rotulada.
- **Plataformas:** web/desktop/tablet. **Referências:** `10C_PUB_klaviyo_dashboard-receita-atribuida_1.jpg`.

## CMP-PUB-11 — Calendário de publicação + quadro de ideias
- **Anatomia:** compositor com seletor de canais por avatar (ícone da rede sobreposto), calendário mensal com dia
  selecionado; quadro de ideias em colunas (Ideias / To do / Review).
- **Estados:** rascunho, agendado, publicado, erro de publicação.
- **Regras:** a rede de destino aparece no avatar; data e fuso do agendamento visíveis (inferência).
- **Plataformas:** web, mobile. **Referências:** `10C_PUB_buffer_agendamento-ideias-boards_1.jpg`.

## CMP-PUB-12 — Prova social com origem
- **Anatomia:** estrelas + "Based on 33.000+ reviews across" + selos das fontes (Capterra 4,5, TrustRadius, G2);
  ou contador exato ("375.227 creators, brands, and agencies") + faixa de logos.
- **Regras:** número real com origem; nada de contador aleatório (`ux-patterns/references/dark-patterns.md`); logos em
  monocromático para não competir (`website-ui` §2).
- **Plataformas:** website. **Referências:** `10C_PUB_mailchimp_home-selos-avaliacao_1.jpg`, Buffer.

## CMP-PUB-13 — Anel de distribuição de verba por canal
- **Anatomia:** anel segmentado por canal com legenda em 2 colunas; total no centro.
- **Regras:** cores de canal só no gráfico; valor e % em texto na legenda (não depender da cor). Alternativa mais
  legível para comparar: barras horizontais por canal ("Total 140,708").
- **Plataformas:** web/desktop. **Referências:** `dashboard-ui/references/domain-examples.md` §11 (`DfXoXVFPBfd`).
