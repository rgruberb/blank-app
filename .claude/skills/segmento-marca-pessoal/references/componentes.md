# Componentes — Marca pessoal (CMP-MPE)

Formato: anatomia, estados, regras, plataformas, referências. Base: lista da ficha MPE (10B §14), fichas de imagem
C2–C3, 9C e regras gerais das skills de tema/plataforma. "(inferência)" = conclusão nossa.

---

## CMP-MPE-01 — Cartão de perfil
- **Anatomia:** foto, nome, **uma linha de posicionamento** (o que faz, para quem), ícones sociais, handle; opcional
  selo de verificado e um CTA.
- **Estados:** padrão, sem foto (iniciais), carregando (skeleton do tamanho final).
- **Regras:** o visitante entende quem é em segundos (10B); no máximo **um** CTA no cartão (Nomey); foto real.
- **Plataformas:** todas; topo do link na bio. **Referências:** Beacons (C2), `../../design-direction/assets/visual-refs/9C_perfil-criador_nomey_2.jpg`.

## CMP-MPE-02 — Botão de link com ícone
- **Anatomia:** botão largura total, ícone da rede/tipo à esquerda, rótulo verbo + objeto ("Agendar call 1:1").
- **Estados:** padrão, hover, press (escala 0,95, `ui-motion`), foco visível, destacado (fixado no topo).
- **Regras:** alvo ≥ 44pt/48dp e 8px entre botões (`mobile-app-ui`); hierarquia: 1–3 principais em destaque, demais
  neutros; nada de dezenas sem ordem (10B §11); texto escuro sobre cor viva.
- **Plataformas:** mobile principal. **Referências:** Linktree (10B), Beacons (botões laranja "Book a 1:1 glam call").

## CMP-MPE-03 — Campo "reserve seu endereço"
- **Anatomia:** prefixo fixo do domínio (`beacons.ai/`) + campo do nome + botão "Claim your link" no mesmo bloco.
- **Estados:** vazio, digitando, disponível, já usado, inválido.
- **Regras:** checagem de disponibilidade inline; é a conversão principal da landing de ferramenta de link na bio (C2).
- **Plataformas:** website. **Referências:** `10C_MPE_beacons_perfil-link-bio-mock_1.jpg`.

## CMP-MPE-04 — Grade de portfólio
- **Anatomia:** cards com capa, título, tipo/cliente, ano; filtros em chips.
- **Estados:** carregando, filtro sem resultado, hover com prévia.
- **Regras:** o trabalho é o foco (Behance blog); data visível (inferência); card → página do case com transição
  contínua (`ui-motion`, card→página); texto alternativo em cada capa.
- **Plataformas:** website principal; mobile em 1–2 colunas. **Referências:** `website-ui` §11; Awwwards Portfolio.

## CMP-MPE-05 — Estudo de caso em 4 blocos
- **Anatomia:** (1) introdução, (2) problema, (3) processo, (4) exemplos anotados; ficha com papel, prazo, cliente.
- **Regras:** mostrar processo, não só o final (Behance "Portfolio 2017", via busca); linhas de 45–75 caracteres;
  autorização do cliente para expor o trabalho: não coberta pela fonte (ver `regulacao.md`).
- **Plataformas:** website. **Referências:** 10B §6; `../../design-direction/assets/visual-refs/9C_propostas_cook_2.jpg` (processo em cards numerados).

## CMP-MPE-06 — Agenda pública
- **Anatomia:** lista por data (dia, mês, cidade/local ou online, título, botão de ingresso/inscrição).
- **Estados:** próximos, esgotado, cancelado, passados (colapsados).
- **Regras:** data completa e fuso em evento online (inferência); esgotado com texto, não só cor.
- **Plataformas:** website, mobile. **Referências:** 10B §6 (shows, aulas, palestras).

## CMP-MPE-07 — Faixa de prova social
- **Anatomia:** logos de clientes (monocromáticos) + 1–3 números grandes com rótulo e data.
- **Regras:** só dado real com data (10B §7–8); contador aleatório é dark pattern (`ux-patterns`); logos não competem
  com o acento (`website-ui` §2).
- **Plataformas:** website. **Referências:** Linktree "70M+", Beacons "Join 10M+ creators" com avatares.

## CMP-MPE-08 — Depoimento com origem
- **Anatomia:** citação curta, nome, cargo/empresa, foto, link ou data.
- **Regras:** depoimento real e verificável (CDC art. 37 §1º, inferência de aplicação); sem nome = não use
  (`website-ui` §2).
- **Plataformas:** website, mídia kit. **Referências:** 10B §14.

## CMP-MPE-09 — Seletor de agendamento
- **Anatomia:** calendário mensal com dias disponíveis → lista de horários do dia → botão de reservar **ao lado** dos
  horários; fuso exibido.
- **Estados:** sem horário, horário selecionado, reservando, confirmado, conflito.
- **Regras:** 3 passos visíveis (dia, horário, reservar; Calendly); slots com alvo ≥ 44px; fuso detectado com busca
  por cidade (sintese §13, regra geral); confirmação com resumo e convite de calendário (inferência).
- **Plataformas:** website (embed), mobile (sheet com CTA fixo). **Referências:**
  `10C_MPE_calendly_agenda-reserva-calendario_1.jpg`.

## CMP-MPE-10 — Selo "publi/parceria"
- **Anatomia:** rótulo de texto ("Publicidade", "Parceria paga", "#publi") junto ao post/link patrocinado.
- **Regras:** CONAR art. 28 / CDC art. 36 (identificação); termo e posição exigidos ao influenciador: **não
  verificados** (Guia CONAR 2026 não lido). Detalhe em `segmento-publicidade` `CMP-PUB-08/09`.
- **Plataformas:** todas.

## CMP-MPE-11 — Vitrine de produtos do creator
- **Anatomia:** título da coleção, cards de produto (imagem, nome, preço, botão "Shop"), card flutuante de destaque.
- **Regras:** preço e condição completos (CDC 37 §1º); vitrine não empurra o CTA principal para baixo da dobra
  (inferência).
- **Plataformas:** mobile, website. **Referências:** Beacons ("The Glow Edit", card "Glow Drops").

## CMP-MPE-12 — Captura de e-mail com aviso LGPD
- **Anatomia:** campo de e-mail + botão + **linha de aviso** logo abaixo (finalidade) + link da política; caixa de
  consentimento separada para marketing, desmarcada.
- **Estados:** vazio, inválido, enviando, confirmado (com como cancelar).
- **Regras:** LGPD art. 9º (informação clara e ostensiva), art. 8º (consentimento destacado), art. 6º (só o
  necessário); pedir e-mail depois do valor, não em pop-up na chegada (`website-ui` §2). Exemplo de aviso sob o campo:
  Buffer "By entering your email, you agree to receive emails from Buffer."
- **Plataformas:** website, link na bio. **Referências:** `regulacao.md`;
  `../../segmento-publicidade/assets/visual-refs/10C_PUB_buffer_agendamento-ideias-boards_1.jpg`.
