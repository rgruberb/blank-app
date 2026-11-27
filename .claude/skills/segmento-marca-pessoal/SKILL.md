---
name: segmento-marca-pessoal
description: 'Camada de SEGMENTO marca pessoal (código MPE) para qualquer pessoa que vende a si mesma — creator, influenciador, freelancer, consultor, palestrante, artista, designer com portfólio. O único segmento em que a personalidade da pessoa manda: densidade baixa, motion tolerante no estilo (ainda 1 momento animado por página; nunca no CTA), moldura neutra (Framer #1F1F1F) ou viva (Linktree #E9C0E9/#D2E823 com texto #1E2330), link na bio mobile-first, portfólio com estudo de caso em 4 blocos, prova social real com data, publi identificada (CONAR art. 28), LGPD na captura de e-mail, templates TPL-MPE e componentes CMP-MPE (perfil, botões de link, reserve seu endereço, grade de portfólio, agenda, depoimento). Use em "marca pessoal", "personal brand", "creator", "criador de conteúdo", "influenciador", "portfólio pessoal", "link na bio", "link in bio", "freelancer", "site pessoal", "mídia kit", "agendar call", "página de palestrante".'
---

# Segmento: Marca pessoal (MPE)

Skill de **segmento**: o que muda quando o produto é a marca de uma pessoa, para qualquer pessoa ou ferramenta do
setor (link na bio, portfólio, site pessoal, perfil de creator, agenda pública). Não repete regras gerais: plataforma
(`website-ui`, `desktop-app-ui`, `mobile-app-ui`) e tema (`design-direction`, `ui-motion`, `ux-patterns`,
`dashboard-ui`) continuam valendo. Fontes: ficha MPE da rodada 10B (27/11/2026), imagens 10C/C2–C4, posts 10A,
pesquisa 9C e `docs/pesquisa-marca-pessoal/sintese.md` (só o que é geral). "(inferência)" = conclusão nossa.

## Código
**MPE.** Templates `TPL-MPE-NN`, componentes `CMP-MPE-NN`. Imagens podem receber `REF-MPE-NN` em
`references/visual-index.md` (coluna vazia).

## Quando usar
- Link na bio, site/portfólio pessoal, estudo de caso, perfil público de creator, mídia kit, agenda de shows/aulas/
  palestras, página de agendamento de call, loja do creator.
- Editor/painel do creator (métricas, links) — combine com `dashboard-ui`.
- O app de gestão de marca pessoal do projeto tem skill própria: `projetos/marca-pessoal-app/SKILL.md` (vence esta).
- Publi/patrocínio: o selo vem de `segmento-publicidade` (`CMP-PUB-08/09`).

## Prioridade
skill de app específico (ex.: `marca-pessoal-app`) > **segmento (esta)** > plataforma > tema > terceiros (`ext-*`).
Esta skill só sobrepõe o que diz explicitamente (paleta da pessoa, tom, densidade baixa, regulação); no resto valem
plataforma e tema. **Motion "tolerante" não sobrepõe o limite de 1 momento animado por página** de `website-ui`/`ui-motion`:
a tolerância é de *estilo* (hover e microinterações com personalidade, easing mais expressivo), não de quantidade.

## Tom e personalidade
- Autoral, expressivo, direto, humano, memorável. O dono quer identidade própria; o visitante quer entender **quem é
  a pessoa em segundos** (10B).
- Duas escolas (Behance, via busca): **personalidade forte** (logo manuscrito para ser lembrada pelo nome) ×
  **minimalismo** que comunica o que faz e mostra o processo. Escolha uma; não misture (inferência).
- A paleta é **da pessoa**; a plataforma é moldura (inferência, 10B).

## Regras centrais
**Paleta (hex medidos com `getComputedStyle`, 10B)**
- Linktree: `#FFFFFF`, texto `#1E2330`, lilás `#E9C0E9`, lima `#D2E823`, `#ECFEF2`, `#676B5F`.
- Framer Marketplace: fundos `#1F1F1F` `#111111` `#FFFFFF`; texto `#FFFFFF` `#999999`; azul `#0099FF`.
- Vitrine autoral (Awwwards): `#222222` `#F8F8F8` + 1 destaque `#FFF083`.
- Lilás e lima pedem **texto escuro** `#1E2330` (contraste não calculado na fonte → calcule; alvo 4,5:1).
- **Evitar** (inferência): moldura colorida que compita com a identidade; mais de 1 acento (2 bases + 1 acento,
  `design-direction`).

**Tipografia**
- Linktree `Linksans` (própria); Framer `Inter` (+ `walsheim`); Behance cita `sofia pro`. Mínimos: não verificados.
- Nome da pessoa como display grande (Awwwards "DANIEL NEATH · PRODUCT DESIGN PORTFOLIO"; capa Nomey).
- Site: escala 1,25 (16/20/25/32), linha 45–75 caracteres, raio interno = externo − padding (10A `DfzcornCO73`,
  `DgOzQOLk5m9`). Fonte open source com acentos PT verificados; licença de embed lida na foundry (9C).

**Densidade**
- **Baixa**: uma pessoa, uma mensagem, poucos blocos; o trabalho é o foco e a formatação simples para navegar e
  contatar (Behance blog, via busca). Link na bio: botões principais primeiro, sem dezenas sem hierarquia.

**Motion**
- O segmento **mais tolerante** no estilo: microinterações, transição de portfólio, hover (10B). Quantidade: continua
  1 momento expressivo por página (ver Prioridade). Transição grade→case **expressiva** (shared element, morph,
  card→página) **conta** como o momento: com ela, o hero do case/portfólio fica estático (ou o hero anima e a transição
  é fade/slide padrão, que não conta). Reveal discreto de seção (≤ 8px, ≤ 400 ms, sem stagger) não conta.
- **Nunca** (inferência, 10B): animar o botão de contato/CTA principal; atrasar o carregamento do link na bio;
  ignorar `prefers-reduced-motion`.
- Scroll: "Motion should follow the visitor" — parou de rolar, o movimento para; não sequestrar o scroll
  (10A `DgEyy8nRybB`). Um momento animado por página (`website-ui`); toda interação "premium" tem custo em mobile,
  contraste e performance (10A `DgNTvDZCMNX`).

**Dados e números**
- Prova social com número e **data** (inferência): "70M+" Linktree, "10M+ creators" Beacons. Seguidores/clientes só
  reais. Métricas do creator: período nomeado e `tabular-nums` (`dashboard-ui`).

**Confiança**
- Logos de clientes, depoimentos reais com origem, trabalho recente com data, contato visível (10B §8). Estudo NN/g
  específico de marca pessoal: não verificado.

**Regulação (resumo; `references/regulacao.md`, não é aconselhamento jurídico)**
- LGPD arts. 6º, 8º, 9º, 18: formulário de contato/newsletter e analytics com aviso claro e consentimento destacado;
  direitos do titular.
- CONAR art. 28 / CDC art. 36: post e link patrocinado identificados (aplicação ao creator = inferência).
- CDC art. 37 §1º: depoimento e número de prova social reais (inferência).
- Direito de imagem/autoral (foto de terceiros, trabalho de cliente no portfólio): **norma não lida** — lacuna.

**Acessibilidade**
- Público amplo e mobile-first (inferência): contraste do texto sobre foto/cor viva; alvo de toque ≥ 44pt/48dp com
  8px entre botões de link (`mobile-app-ui`); texto alternativo em imagens de portfólio; reduced motion.

## Diferenças por plataforma
| Website | App desktop | App mobile |
|---|---|---|
| portfólio completo, estudos de caso (Framer, Behance, Awwwards) → `website-ui` | editor/painel do creator → `desktop-app-ui` + `dashboard-ui` | **principal consumo**: link na bio aberto do Instagram/TikTok, uma coluna (inferência) → `mobile-app-ui` |

## Templates (`references/templates.md`)
- `TPL-MPE-01` Link-hub vibrante (Linktree)
- `TPL-MPE-02` Portfólio escuro editorial (Framer)
- `TPL-MPE-03` Minimalista de processo (Behance)
- `TPL-MPE-04` Vitrine autoral (Awwwards)
- `TPL-MPE-05` Perfil de creator com monetização (Beacons, Nomey)

## Componentes (`references/componentes.md`)
- `CMP-MPE-01` Cartão de perfil
- `CMP-MPE-02` Botão de link com ícone
- `CMP-MPE-03` Campo "reserve seu endereço"
- `CMP-MPE-04` Grade de portfólio
- `CMP-MPE-05` Estudo de caso em 4 blocos
- `CMP-MPE-06` Agenda pública
- `CMP-MPE-07` Faixa de prova social (logos + números com data)
- `CMP-MPE-08` Depoimento com origem
- `CMP-MPE-09` Seletor de agendamento (dia → horário → reservar)
- `CMP-MPE-10` Selo "publi/parceria"
- `CMP-MPE-11` Vitrine de produtos do creator
- `CMP-MPE-12` Captura de e-mail com aviso LGPD

## Anti-padrões
- Link na bio com dezenas de botões sem hierarquia; CTA escondido atrás de animação; contador de escassez falso.
- Depoimento inventado (CDC 37 §1º); publi sem rótulo (CONAR 28); e-mail capturado sem aviso (LGPD 9º).
- Moldura que compete com a identidade; personalidade e minimalismo misturados sem decisão (inferência).
- Portfólio só com imagens finais, sem problema e processo; trabalho sem data (inferência sobre Behance 2017).
- Copiar layout/ilustração de shot: extraia o padrão, não o pixel; junte 3 referências (sintese §6).

## Workflow
1. Superfície: link na bio (mobile) · site/portfólio · painel do creator · agenda/booking.
2. Decida a escola (personalidade × minimalismo) e a paleta **da pessoa**; escolha o TPL-MPE como moldura.
3. Monte com os CMP-MPE: perfil → ação principal → prova → trabalho → contato. Conteúdo real (foto, número, case).
4. Publi? `CMP-MPE-10`. Captura de dado? `CMP-MPE-12` + `references/regulacao.md`.
5. Verifique contraste (cor viva + texto escuro), alvos de toque, reduced motion e 375/768/1280/1440 (`website-ui`).

## Onde está o resto
- Detalhe: `references/templates.md`, `componentes.md`, `regulacao.md`, `fontes.md`, `visual-index.md`; imagens em
  `assets/visual-refs/`.
- Portfólio e prova social em site: `.claude/skills/website-ui/references/website-patterns.md` §2 e §11; benchmark
  (Awwwards, Land-book, SiteInspire): `website-ui/references/benchmark-sources.md`.
- Marca, logo, paleta e par tipográfico: `.claude/skills/design-direction/references/branding-identity.md`,
  `color-palettes.md`, `typography-pairing.md`; prints Nomey/Cook em `design-direction/assets/visual-refs/`.
- Reel, carrossel, logo animado: `.claude/skills/ui-motion/references/motion-for-social-video.md`.
- Dashboard de creator (Kreya, Blenz): `.claude/skills/dashboard-ui/references/domain-examples.md` §30.
- Perfil/tab bar/onboarding mobile: `.claude/skills/mobile-app-ui/references/mobile-patterns.md`.
- App específico: `projetos/marca-pessoal-app/SKILL.md`. Publi: `.claude/skills/segmento-publicidade/`.
