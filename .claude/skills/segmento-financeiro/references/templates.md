# Templates FIN — direções visuais com tokens

Base: rodada 10B §13 (hex medidos por `getComputedStyle` em páginas públicas, 27/11/2026) + galeria 10C/C2–C4/10A.
Regras de leitura:
- Hex **sem `~`** = medido na 10B. Hex **com `~`** = leitura aproximada de imagem (feita em outra skill ou na 10A), não medido.
- Escala, raio, sombra e motion **não foram medidos** em nenhum produto; os valores abaixo vêm das skills de tema do
  projeto e estão marcados **(inferência)** quando são escolha desta skill.
- Escala tipográfica: **1,2** para produto denso (painel, app) e **1,25** para site (`ux-patterns/references/typography-and-touch.md` §2;
  `website-ui` regra 7). Sombra: só em elemento que flutua, tingida (`design-direction/references/layers-and-trust-layout.md` §4).
- Tokens de motion: `ui-motion/SKILL.md` "Tokens de motion recomendados". Em FIN, nunca animar valor na confirmação,
  botão de confirmar nem aviso de custo/risco.

---

## TPL-FIN-01 — Sóbrio institucional
| Token | Valor |
|---|---|
| Fundo | `#FFFFFF` / `#F1F2F4` |
| Texto | `#000000` (principal), `#3B3B3B` (secundário) |
| Bordas/neutros | `#CFD1D3` |
| Acento (1 só) | laranja `#FF6200` **ou** azul-marinho `#000066` |
| Par tipográfico | família própria de display + texto neutro (Itaú usa `Itau Display`/`Itau Text`); sem família própria: sans neutra do catálogo de `design-direction/references/typography-pairing.md` (inferência) |
| Escala | 1,25 no site; 1,2 no app (inferência) |
| Raio | médio, constante (inferência; não medido) |
| Sombra | nenhuma em seções; tingida só em menu/modal |
| Densidade | média |
| Motion | mínimo: estado e foco |
- **Quando usar:** banco tradicional, cooperativa, previdência, seguradora, público mais velho; quando a marca precisa
  parecer instituição.
- **Fontes:** itau.com.br (10B ✅).
- **Imagens:** nenhuma própria do Itaú; estrutura de confiança em `10C_FIN_wise_selos-confianca-regulacao_1.jpg` e
  aviso em `10C_FIN_mercury_home-aviso-regulatorio_1.jpg`.

## TPL-FIN-02 — Fintech moderna
| Token | Valor |
|---|---|
| Fundo | `#FFFFFF`, `#F8FAFD` |
| Superfícies | `#E5EDF5` (Stripe) ou `#F3EFE6` bege / `#ECDFFF` lilás claro (Nubank) |
| Texto | `#061B31`, `#50617A`, `#64748D` (Stripe) ou `#000000` (Nubank) |
| Acento (só CTA/link) | `#533AFD` (Stripe; apoio `#7F7DFC`) **ou** `#8D0DE3` (Nubank; escuros `#5D0599`, `#1E002F`) |
| Par tipográfico | sans geométrica (Stripe `sohne-var`; Nubank `nuSansDisplay` + `nuSansText`) |
| Escala | 1,25 site / 1,2 app |
| Raio | CTA em pílula (Stripe, imagens) |
| Sombra | card de produto flutuante sobre gradiente (Stripe, imagens) |
| Densidade | baixa no varejo; média-alta no painel B2B |
| Motion | suave de estado |
- **Quando usar:** fintech de varejo, pagamentos, SaaS financeiro; quando a marca tem uma cor forte e o resto pode ser
  neutro.
- **Fontes:** nubank.com.br, stripe.com/br, docs.stripe.com/stripe-apps/design (10B ✅).
- **Imagens:** `10C_FIN_stripe_checkout-pagamento_1.jpg`, `10C_FIN_stripe-billing_planos-precos-cards_1.jpg`,
  `10C_FIN_stripe-invoicing_fatura-pagamento-moeda_1.jpg`.

## TPL-FIN-03 — Verde confiança
| Token | Valor |
|---|---|
| Fundo de destaque | `#163300` (verde-escuro) com tipografia `#9FE870`; ou o inverso `#9FE870` com texto `#163300` |
| Fundo neutro | `#FFFFFF`, `#E8EBE6` |
| Texto | `#0E0F0C`, `#454745` |
| Acento | `#9FE870` (CTA pílula) |
| Par tipográfico | display condensado próprio (`Wise Sans`) + `Inter` no corpo |
| Escala | display muito grande em caixa-alta no hero; corpo 1,25 (inferência) |
| Raio | alto em cartões de preço; CTA pílula e botão circular de seta (imagens) |
| Sombra | quase nenhuma; contraste por cor de fundo |
| Densidade | baixa |
| Motion | não verificado; manter mínimo (inferência) |
- **Quando usar:** câmbio, remessa, conta global, qualquer produto cuja mensagem é "taxa clara"; o número da taxa vira
  título (`1,1% IOF`).
- **Cuidado:** marca verde compete com o verde de "ganho". Use outro tom/ícone para variação (`dashboard-ui` §8).
- **Fontes:** wise.com/br (10B ✅); wise.design 🔒.
- **Imagens:** `10C_FIN_wise_home-hero_1.jpg`, `10C_FIN_wise_selos-confianca-regulacao_1.jpg`,
  `10C_FIN_wise_precos-transparentes_1.jpg`.

## TPL-FIN-04 — Preto premium
| Token | Valor |
|---|---|
| Fundo escuro | `#191C1F`, `#000000` |
| Fundo claro | `#F7F7F7` |
| Texto | `#1F1F1F` (sobre claro); cinzas `#C9C9CD`, `#717173` |
| Acento | não medido como cor separada; o contraste preto/branco faz o papel (inferência) |
| Par tipográfico | `Aeonik Pro` (display) + `Inter` (texto) |
| Escala | 1,25 site / 1,2 app |
| Raio | não verificado |
| Sombra | nenhuma; elevação por tom (dark mode em `mobile-app-ui` regra 14) |
| Densidade | média |
| Motion | contido |
- **Quando usar:** conta premium, cartão de alta renda, investimento para público que valoriza status discreto.
- **Fontes:** revolut.com/en-BR (10B ✅; poupança com "taxa variável" na mesma seção).
- **Imagens:** sem print próprio; tom parecido em `10C_FIN_dribbble-conceptzilla_banco-app-ios-saldo-transacoes_1.jpg`
  (conceito, Dribbble).

## TPL-FIN-05 — Painel escuro de investimento
| Token | Valor |
|---|---|
| Fundo | quase preto: `~#0B0B0D` (Markets, `dashboard-ui` §20a) |
| Acento (1 só) | `~#D4FF3A` limão (Markets) **ou** `~#B4E33B` (trading de Berlim, `DgPLR1SDouB`, 10A, leitura aproximada) |
| Semânticas | verde/vermelho **só** para variação de preço; na ficha do `DgPLR1SDouB`: `~#00B38C`, `~#8F2B4B` (aproximado) |
| Texto | `~#FFFFFF` |
| Par tipográfico | preço em sans, dados auxiliares em mono (`dashboard-ui` §8); `DgPLR1SDouB` usa **Akshar** |
| Escala | 1,2 (inferência) |
| Raio | cards arredondados "para manter o visual calmo" (legenda `DgPLR1SDouB`) |
| Sombra | nenhuma; textura granulada sutil possível (Vaulto, `dashboard-ui` §10) |
| Densidade | média-alta |
| Motion | filtros de tempo a um toque; gráfico ao vivo; **nunca** animar o valor da ordem na confirmação |
- **Quando usar:** corretora, cripto, app de investimento, painel de tesouraria. Saldo e ativos à esquerda, ação
  principal no **único** gradiente da tela, Deposit/Buy ao lado do gráfico (legenda `DgPLR1SDouB`).
- **Fontes:** 10A `DgPLR1SDouB` (sem imagem legível); `dashboard-ui/references/layout-patterns.md` §8, §10;
  `dashboard-ui/references/domain-examples.md` §20, §22.
- **Imagens (em `dashboard-ui`):** `DXeeUP7FKGs_1.jpg`, `DfcdrhgFFMR_1.jpg`, `Dfr6X8qFPwC_2.jpg` (ver
  `visual-index.md`, "Imagens em outras skills").
- **Atenção:** hex deste template **não foram medidos**; confirme com a marca do cliente.
