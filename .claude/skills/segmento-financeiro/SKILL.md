---
name: segmento-financeiro
description: Camada de SEGMENTO financeiro (código FIN) para qualquer empresa do setor — banco digital, fintech, corretora, carteira, pagamentos, crédito, investimento, cobrança e faturamento. Traz tom (preciso, calmo, transparente), paleta medida em produtos reais (branco + 1 cor de marca), números tabulares e R$ com 2 casas, o que nunca animar, confiança e selos, regulação que muda a tela (CET da Res. CMN 4.881/2020, LGPD, aviso de rentabilidade), 5 templates TPL-FIN e 14 componentes CMP-FIN, diferenças website × desktop × mobile e ponteiros para as skills de plataforma e tema. Use quando falarem em "app de banco", "banco digital", "fintech", "corretora", "carteira", "wallet", "pagamentos", "checkout de pagamento", "extrato", "saldo", "Pix", "transferência", "cartão de crédito", "fatura", "crédito", "empréstimo", "CET", "investimentos", "rentabilidade", "cripto", "trading" ou "página de preços de fintech".
---

# segmento-financeiro (FIN)

Skill de **segmento**: o que muda quando o produto mexe com dinheiro de alguém. Vale para qualquer empresa do setor
(banco, fintech, corretora, meio de pagamento, crédito, seguros com cobrança); não descreve nenhum app específico.
Fonte principal: pesquisa 10B (27/11/2026; hex por `getComputedStyle` em páginas públicas, nenhum produto logado) e
galeria 10C/C2–C4/10A. **(inferência)** = conclusão da pesquisa, não da fonte.

## Código do segmento
`FIN`. Templates `TPL-FIN-01…05` (`references/templates.md`), componentes `CMP-FIN-01…14`
(`references/componentes.md`), imagens em `assets/visual-refs/` (índice: `references/visual-index.md`).

## Quando usar
- Telas de saldo, extrato, transferência/Pix, cartão e fatura, simulação de crédito, carteira de investimentos,
  checkout/pagamento, cobrança, preços de serviço financeiro, landing de banco/fintech, onboarding com CPF.
- Junto com a skill de plataforma (`website-ui`, `desktop-app-ui`, `mobile-app-ui`) e, para painel, `dashboard-ui`.
- Não use para CRM/vendas (→ `segmento-crm`) nem para validar estratégia de trading (→ `quant-investing`).

## Prioridade (quando as regras conflitam)
1. Skill de **app específico** (se o projeto tiver uma) > 2. **segmento** (esta) > 3. **plataforma** (`website-ui`,
`desktop-app-ui`, `mobile-app-ui`) > 4. **tema** (`design-direction`, `ui-motion`, `ux-patterns`, `dashboard-ui`) >
5. **skills de terceiros** (`ext-*`: só implementação, com os valores das skills acima).
Esta skill decide **cor, tom, números, o que não animar e o que a regulação exige**; layout, alvos e breakpoints vêm
da plataforma.

## Tom e personalidade
- Preciso, calmo, transparente, confiável; no varejo soma "acessível" e "amigável" (Nubank, Wise).
- O usuário quer sentir que o número está certo, o dinheiro está seguro e nada será cobrado sem aviso (inferência).
- NN/g: credibilidade começa por parecer legítimo e profissional; não peça dados antes de atender confiança básica
  ("Hierarchy of Trust", lido via busca).

## Regras centrais (com números)
**1. Paleta — fundo branco/quase branco, texto quase preto, UMA cor de marca para ação.** Medidos (10B):
| Produto | Ação/marca | Texto | Superfície |
|---|---|---|---|
| Nubank | `#8D0DE3` (`#5D0599`, `#1E002F`) | `#000000` | `#F3EFE6`, `#ECDFFF` |
| Stripe | `#533AFD` (`#7F7DFC`) | `#061B31`, `#50617A`, `#64748D` | `#F8FAFD`, `#E5EDF5` |
| Wise | `#9FE870` sobre `#163300` | `#0E0F0C`, `#454745` | `#E8EBE6` |
| Revolut | `#191C1F`/`#000000` | `#1F1F1F`, `#717173` | `#F7F7F7`, `#C9C9CD` |
| Inter | `#FF7A00` (`#EA7100`) | `#161616`, `#747684` | `#E6E4E4` |
| Itaú | `#FF6200`, `#000066` | `#000000`, `#3B3B3B` | `#F1F2F4`, `#CFD1D3` |
- **Evite** (inferência): verde/vermelho puros como único sinal de ganho/perda; cor de marca saturada como fundo de
  área cheia de números; CTA vermelho igual à cor de alerta. Marca verde? Diferencie do verde semântico
  (`../dashboard-ui/references/layout-patterns.md` §8).
- Hex são de páginas de marketing; o produto logado pode diferir (não medido).

**2. Tipografia e números.** Sans neutra/geométrica, com display próprio para títulos e neutra para texto
(Inter em Wise, Revolut e Inter; famílias próprias em Nubank, Stripe `sohne-var`, Itaú). Pares sugeridos em
`design-direction/references/typography-pairing.md`.
- `font-variant-numeric: tabular-nums` em todo valor em coluna ou que muda; KPI em **uma linha** (`white-space: nowrap`)
  e **≤ ~30px no celular** (`10A_Deq_kvJBI3g_1.jpg`: "€5.3M" quebrava em 48px). Uso de tabular nos produtos medidos:
  **não verificado**.
- Corpo mínimo **16px** no mobile (inferência). Valores alinhados à direita em tabela (`desktop-app-ui` regra 4).

**3. Densidade.** **Média-baixa no varejo** (uma ação por tela: Nubank, Wise, Revolut); **média-alta em painel de
negócio** (Stripe Dashboard: listas, filtros, detalhe de objeto). Stripe Apps limita personalização de cor para manter
contraste (docs ✅).

**4. Motion.** Aceitável: transição curta de estado, confirmação de sucesso, carregamento de saldo (tokens em
`ui-motion`). **Nunca animar** (inferência): valor monetário contando na tela de confirmação, botão de confirmar que se
move, aviso de custo/risco. Contador ao vivo só em marketing e rotulado (Ramp, `10C_FIN_ramp_…`). Durações nos
produtos: não verificado.

**5. Dados, números e precisão.**
- R$ com separador brasileiro e **sempre 2 casas**; moeda estrangeira com código explícito (USD, EUR) e, se houver
  conversão, original e convertida lado a lado (Stripe Invoicing `€29,99 | $31,88`).
- Crédito: taxa **% a.m. e % a.a.** + **CET % a.a.** antes do botão principal.
- Rentabilidade: **data da cota**, período (mín. 12 meses para avaliar, exemplo Sicredi), "líquida de taxas, não de
  impostos" quando for o caso e "rentabilidade passada não representa garantia de rentabilidade futura".
- Toda variação com **sinal (+/−) além da cor**; todo número com data/fonte; "taxa variável" sempre rotulada (Revolut).
- Abreviação (R$ 1,2 mi) só com o valor exato acessível (tooltip/leitor de tela) (inferência).

**6. Confiança.** Bloco de segurança visível (Nubank "Segurança é prioridade", "Me roubaram"); faixa de 3 provas —
volume, regulador com link, suporte 24/7 (Wise); selos só se verificáveis e de direito do produto (Monzo: prêmio +
proteção de depósito); número de clientes (Nubank "130 milhões"). FGC "onde couber" é inferência.

**7. Regulação (resumo; detalhe em `references/regulacao.md` — não é aconselhamento jurídico).**
CET em % a.a. na oferta/contratação de crédito (Res. CMN 4.881/2020; a 3.517/2007 está **revogada**); LGPD arts. 6º,
8º, 9º e 18 (finalidade, consentimento destacado, informação ostensiva, tela de direitos do titular); fundos: Res. CVM
175 (seção de material de divulgação, texto não lido); Anbima e CDC art. 54-B: não verificados.

**8. Acessibilidade.** Público amplo, inclui idosos e baixa literacia financeira (inferência): contraste alto nos
valores (4,5:1 texto — `ux-patterns/references/typography-and-touch.md` §3); ganho/perda nunca só por cor; alvos
grandes na confirmação (44pt/48dp, `mobile-app-ui` regra 1); siglas explicadas (CET, CDI, a.a., IOF).

## Diferenças por plataforma
| Plataforma | Papel no FIN | Abra |
|---|---|---|
| **Website** | institucional + captação (CPF/e-mail no topo), preços transparentes, faixa de confiança, aviso regulatório visível | `../website-ui/SKILL.md` regras 4, 6, 12; `../website-ui/references/website-patterns.md` §2, §4, §9 |
| **App desktop** | painel de negócio: listas, filtros, detalhe de objeto, exportação (Stripe Dashboard) | `../desktop-app-ui/SKILL.md` regras 3, 4, 10; `../desktop-app-ui/references/desktop-patterns.md` §3, §7; `../dashboard-ui/references/layout-patterns.md` §10 |
| **App mobile** | fluxo curto, **uma decisão por tela**, biometria (inferência), saldo + ações + extrato na 1ª dobra, confirmar no rodapé | `../mobile-app-ui/SKILL.md` regras 2, 9, 15; `../mobile-app-ui/references/mobile-patterns.md` §8, §9, §13 |

## Templates (direções visuais) — tokens em `references/templates.md`
| Código | Nome | Base |
|---|---|---|
| `TPL-FIN-01` | Sóbrio institucional | branco/`#F1F2F4`, texto `#000`/`#3B3B3B`, acento `#FF6200` ou `#000066` (Itaú) |
| `TPL-FIN-02` | Fintech moderna | branco + marca saturada só no CTA (`#8D0DE3` Nubank, `#533AFD` Stripe) |
| `TPL-FIN-03` | Verde confiança | `#9FE870` sobre `#163300`, texto `#0E0F0C`, transparência de taxa como mensagem (Wise) |
| `TPL-FIN-04` | Preto premium | `#191C1F`/`#1F1F1F` + cinzas `#C9C9CD` (Revolut) |
| `TPL-FIN-05` | Painel escuro de investimento | quase preto + 1 acento; verde/vermelho só para variação (hex aproximados das referências de `dashboard-ui`) |

## Componentes característicos — detalhe em `references/componentes.md`
| Código | Nome | Código | Nome |
|---|---|---|---|
| `CMP-FIN-01` | Card de saldo com variação | `CMP-FIN-08` | Gerenciador de consentimento e direitos LGPD |
| `CMP-FIN-02` | Linha do extrato com data e status | `CMP-FIN-09` | Faixa de confiança (volume · regulador · suporte) |
| `CMP-FIN-03` | Resumo de confirmação de transferência | `CMP-FIN-10` | Aviso regulatório fixo |
| `CMP-FIN-04` | Quadro de custo (CET, a.m./a.a., total) | `CMP-FIN-11` | Checkout escolha + resumo |
| `CMP-FIN-05` | Selo de rentabilidade com data e aviso | `CMP-FIN-12` | Barra de limite usado/disponível |
| `CMP-FIN-06` | Alerta de segurança/fraude | `CMP-FIN-13` | Ações rápidas + seletor de moeda/conta |
| `CMP-FIN-07` | Seletor de período | `CMP-FIN-14` | Cartão de preço por serviço |

## Anti-padrões
- Esconder tarifa/CET depois do botão principal; "rentabilidade" sem data nem período (inferência).
- Pré-selecionar seguro/upsell; botão de cancelar escondido; contagem regressiva falsa (inferência; catálogo geral em
  `../ux-patterns/references/dark-patterns.md`).
- Pedir CPF, renda ou documentos antes de mostrar valor/segurança (NN/g, Prominence-Interpretation, via busca).
- Animar valor na confirmação; Buy maior que Sell (`dashboard-ui` §8); selo que o produto não tem direito de usar.
- Cor de marca em fundo de tabela; vermelho de CTA = vermelho de alerta; número de KPI quebrando linha.
- Citar a Res. CMN 3.517/2007 (revogada) como base do CET.

## Workflow
1. Identifique a superfície (website/desktop/mobile) e abra a skill de plataforma.
2. Escolha um `TPL-FIN` (ou derive da marca do cliente mantendo "1 cor de marca para ação"); defina tokens.
3. Liste as telas (saldo/extrato, transferência + confirmação, crédito com CET, carteira, cartão, segurança) e os
   `CMP-FIN` de cada uma.
4. Passe pelo checklist de números (regra 5) e pela `references/regulacao.md` para cada tela que mostra custo,
   rentabilidade ou coleta dado pessoal.
5. Abra 1–2 imagens do `references/visual-index.md` para a tela em questão; adapte sem copiar marca, nome ou layout.
6. Verifique contraste e "não só cor" (`design:accessibility-review`), e no navegador com `ext-playwright-cli`.

## Onde está o resto
| Preciso de… | Abra |
|---|---|
| Card de ticker, detalhe do ativo, Buy/Sell iguais | `../dashboard-ui/references/layout-patterns.md` §8 |
| Ordem de leitura do dashboard fintech, score, dois acentos com papéis | `../dashboard-ui/references/layout-patterns.md` §10 |
| Gauge × barras (score com 1 número vs comparação) | `../dashboard-ui/references/layout-patterns.md` §11 |
| Exemplos: orçamento, crédito privado, trading, Vaulto, Zentra, CreditPros, finanças pessoais | `../dashboard-ui/references/domain-examples.md` §5, §16, §20, §22, §23, §29 |
| Tela de decisão ("desenhe para o momento") | `../ux-patterns/references/components-checklists.md` §9 |
| Confiança em 5 níveis, formulários, dashboards (NN/g) | `../ux-patterns/references/nng-research.md` §5, §6, §8 |
| Dark patterns | `../ux-patterns/references/dark-patterns.md` |
| Contraste em números, escala tipográfica | `../ux-patterns/references/typography-and-touch.md` §2, §3 |
| Paleta 2+1, 60/30/10, validar contraste | `../design-direction/references/color-palettes.md` |
| Layout que parece seguro, sombra tingida | `../design-direction/references/layers-and-trust-layout.md` §2, §4 |
| Número rolando (onde é permitido), sucesso 470 ms, reduce motion | `../ui-motion/references/css-recipes.md` §5, §8, §13 |
| Tabela de dados densa | `../desktop-app-ui/references/desktop-patterns.md` §3 |
| Checkout e rodapé fixo com total no celular | `../mobile-app-ui/references/mobile-patterns.md` §8 |
| Normas, órgãos e URLs | `references/regulacao.md` |
| Fontes verificadas e da galeria | `references/fontes.md` |
| Quais imagens abrir | `references/visual-index.md` |
