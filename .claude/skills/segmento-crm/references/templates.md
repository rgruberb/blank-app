# Templates CRM — direções visuais com tokens

Base: rodada 10B §13 (hex medidos por `getComputedStyle` em páginas de marketing, 27/11/2026) + galeria 10C/C2/C4/10A.
- Hex sem `~` = medido. Produto logado **não** foi aberto: o app real pode diferir.
- Escala, raio e sombra **não foram medidos**; os valores vêm das skills de tema e estão marcados **(inferência)**.
  Escala **1,2** para app denso (`desktop-app-ui` regra 3; `ux-patterns/references/typography-and-touch.md` §2).
  Sombra só em elemento que flutua (menu, popover, card arrastado), tingida (`design-direction/references/layers-and-trust-layout.md` §4).
- Motion: tokens de `ui-motion/SKILL.md`; em CRM nunca reordenar linhas lidas, animar contador ao filtrar ou atrasar atalho.
- Tamanhos de texto: linha de tabela 13–14px (como as células do `desktop-app-ui`), com modo compacto opcional de 12px (piso); corpo 16px (escala geral de app).

---

## TPL-CRM-01 — Produtividade escura
| Token | Valor |
|---|---|
| Fundo | `#0F1011`; mais profundo `#08090A` |
| Texto | `#F7F8F8` (principal), `#D0D6E0`, `#8A8F98`, `#62666D` (terciário/desabilitado) |
| Acento / estado | verde `#27A644` (sucesso/ação), vermelho `#F34E52` (erro/risco) |
| Par tipográfico | `Inter Variable` + `Berkeley Mono` (IDs, atalhos) |
| Escala | 1,2 (inferência) |
| Raio | pequeno/médio (inferência; não medido) |
| Sombra | nenhuma; elevação por tom de fundo (dark mode em `desktop-app-ui` regra 11) |
| Densidade | alta |
| Motion | mínimo; foco em atalho e ⌘K |
- **Quando usar:** time técnico ou power users, uso de muitas horas, produto que vende velocidade.
- **Fontes:** linear.app (10B ✅). Linear é ferramenta de projetos citada pela 10B como **referência de densidade** para CRM.
- **Imagens:** dark de tabela em `10A_DgAT3fVBJ8B_1.jpg` (tom parecido; conceito).

## TPL-CRM-02 — Clara e fluida
| Token | Valor |
|---|---|
| Fundo | `#FFFFFF`; superfícies `#ECECED` |
| Texto | `#242629` (principal), `#101112`, `#505155`, `#75777C` |
| Bordas | `#CDCED2` |
| Acento | azul `#266DF0` (ação); roxo `#9B69FF` (secundário/IA) |
| Estado | verde `#007D53` sobre `#E0FCED` |
| Par tipográfico | `Inter` / `Inter Display` + `JetBrains Mono` |
| Escala | 1,2 (inferência) |
| Raio | médio; CTA escuro preenchido + secundário em contorno (imagem Attio) |
| Sombra | janela do app flutuante no site; no app, só menus (inferência) |
| Densidade | alta-média |
| Motion | contido |
- **Quando usar:** CRM moderno para startups e times de receita; quando o produto precisa parecer leve sem perder densidade.
- **Fontes:** attio.com (10B ✅).
- **Imagens:** `10C_CRM_attio_home-workspace-ia_1.jpg`, `10C_CRM_dribbble-conceptzilla_crm-leads-tabela_1.jpg` (claro, acento laranja).

## TPL-CRM-03 — Funil amigável
| Token | Valor |
|---|---|
| Fundo | `#FFFFFF`; tons claros de verde `#F3FCF2`, `#D7F9D3` |
| Texto | `#192435`; azul-petróleo `#27455C` |
| Acento | roxo `#6861F2` (ação no produto); amarelo `#FFDE00` (CTA de marketing) |
| Estado | verde `#017737` |
| Par tipográfico | `Inter` + `Haffer` (display) |
| Escala | 1,2 no app; 1,25 no site (inferência) |
| Raio | médio nos cartões; CTA pílula no site (imagens) |
| Sombra | leve no cartão de negócio (imagem) |
| Densidade | média |
| Motion | arrastar cartão entre etapas |
- **Quando usar:** PMEs, time comercial pouco técnico, venda consultiva em que o kanban é a tela principal.
- **Fontes:** pipedrive.com (10B ✅).
- **Imagens:** `10C_CRM_pipedrive_deals-kanban-app_1.jpg`, `10C_CRM_pipedrive_home-hero-confianca_1.jpg`,
  `10C_CRM_rd-station-crm_home-funil-kanban_1.jpg`.

## TPL-CRM-04 — Plataforma corporativa
| Token | Valor |
|---|---|
| Fundo | `#FCFCFA`, `#F8F5EE` |
| Texto | `#1F1F1F` |
| Acento | laranja `#FF4800` (HubSpot) **ou** azul Salesforce (**hex não medido**) |
| Profundidade | verde-escuro `#061C1D`, `#124548` (cartões de destaque) |
| Par tipográfico | `HubSpot Sans` + `HubSpot Serif` (marca própria); sem família própria, sans neutra + serifada para títulos de marketing (inferência) |
| Escala | 1,2 no app (inferência) |
| Raio | médio |
| Sombra | menus e popovers |
| Densidade | alta; muitos módulos |
| Motion | contido |
- **Quando usar:** suíte com marketing + vendas + atendimento, empresas maiores, muitos módulos e permissões.
  SLDS 2: tokens como CSS custom properties e caminho para dark mode (✅).
- **Fontes:** hubspot.com, lightningdesignsystem.com (10B ✅). HubSpot Canvas: ❌ design system público não confirmado.
- **Imagens:** `10C_CRM_hubspot_home-card-contato_1.jpg`.
