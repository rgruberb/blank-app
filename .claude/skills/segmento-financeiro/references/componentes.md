# Componentes FIN

Origem: 10B §14 (CMP-FIN-01 a 08) e galeria 10C/C2–C4/10A (CMP-FIN-09 a 14). Nomes entre crases (`trust-strip`)
são os nomes sugeridos nas fichas da galeria. **(inferência)** = regra desta skill, não da fonte.
Regras transversais: valor com `tabular-nums`; R$ com 2 casas; variação com sinal + cor; contraste 4,5:1 no texto e
3:1 em ícones/bordas (`ux-patterns`); alvo 44pt/48dp no mobile, 24px mínimo na web.

---

## CMP-FIN-01 — Card de saldo com variação
- **Descrição:** primeiro bloco da home de conta/carteira: quanto tenho e como mudou.
- **Anatomia:** rótulo ("Saldo disponível") → valor grande em 1 linha → variação com sinal e período → composição do
  total logo abaixo (ex.: conta + investimentos) → ações rápidas (CMP-FIN-13). Opcional: botão "ocultar valores" (inferência).
- **Estados:** carregando (skeleton do tamanho do número), oculto (•••••), negativo (sinal "−" + cor + palavra), erro de
  atualização com "atualizado às hh:mm".
- **Regras:** `white-space: nowrap`, `tabular-nums`, **≤ ~30px no celular** (`10A_Deq_kvJBI3g_1.jpg`); data/hora da
  posição; nunca animar contagem no saldo de confirmação (inferência).
- **Plataformas:** mobile (1ª dobra com ações + extrato), desktop (saldo + composição + 1 CTA cheio, `dashboard-ui` §10).
- **Referências:** `10C_FIN_dribbble-conceptzilla_banco-app-ios-saldo-transacoes_1.jpg` (`balance-hero`,
  `currency-tabs`); `10A_DfkL5N_H4GK_1.jpg` (cards de métrica); `dashboard-ui` `DfcdrhgFFMR_1.jpg`.

## CMP-FIN-02 — Linha do extrato com data e status
- **Anatomia:** ícone/logo da contraparte → nome + tipo ("Débito", "Transferência", "Conversão") → valor à direita com
  sinal → valor convertido/secundário embaixo quando houver → status (chip com texto) → agrupamento por dia ("Hoje").
- **Estados:** concluída, pendente, estornada, falhou (texto + ícone + cor, nunca só cor); expandida com detalhes.
- **Regras:** entradas e saídas diferenciadas por sinal e cor; data completa acessível; busca e filtros no topo da lista.
- **Plataformas:** mobile (lista agrupada); desktop (tabela com coluna de status, `desktop-app-ui` regra 4).
- **Referências:** `10C_FIN_dribbble-conceptzilla_…` (`transaction-list`), `10C_FIN_dribbble-outcrowd_…`
  (`transaction-history` com chip "Success").

## CMP-FIN-03 — Resumo de confirmação de transferência
- **Anatomia:** destinatário (nome, instituição, chave/conta parcialmente mascarada) → valor → data/agendamento →
  tarifa (mesmo se zero) → saldo após → botão "Confirmar" + "Voltar/editar".
- **Estados:** revisão, autenticando (biometria/senha), sucesso com comprovante, erro com motivo e próximo passo.
- **Regras:** valor estático (nunca animado), botão fixo na mesma posição (inferência); "saldo disponível" visível no
  campo de valor (`amount-field`, Outcrowd); sucesso com check (`ui-motion` sucesso 470 ms) e comprovante compartilhável.
- **Plataformas:** mobile (rodapé fixo, `mobile-app-ui` regra 2); web (modal ou etapa).
- **Referências:** `10C_FIN_dribbble-outcrowd_…` (`quick-transfer`, "Available to send"); `ux-patterns/references/components-checklists.md` §9.

## CMP-FIN-04 — Quadro de custo (CET, taxa a.m./a.a., total a pagar)
- **Anatomia:** valor solicitado → nº e valor das parcelas → taxa de juros **% a.m. e % a.a.** → **CET % a.a.** →
  tarifas/seguros/IOF discriminados → **total a pagar** → link "como calculamos".
- **Estados:** simulação (editável com CMP-FIN-07), proposta final, expirada.
- **Regras:** aparece **antes** do botão de contratar e no mesmo peso visual do valor; seguro/opcional **desmarcado** por
  padrão (inferência); siglas explicadas. Base: Res. CMN 4.881/2020 (ver `regulacao.md`).
- **Plataformas:** todas.
- **Referências:** sem imagem própria; estrutura escolha + resumo em `10C_FIN_stripe_checkout-pagamento_1.jpg`.

## CMP-FIN-05 — Selo de rentabilidade com data da cota e aviso
- **Anatomia:** rentabilidade % → período (12m, 24m, no ano) → **data da cota** → "líquida de taxas, não de impostos"
  (quando for o caso) → aviso "rentabilidade passada não representa garantia de rentabilidade futura" → comparação com
  índice (CDI) rotulada.
- **Regras:** período mínimo de 12 meses para avaliação (exemplo Sicredi); "taxa variável" rotulada (Revolut); nunca % sem
  data (inferência).
- **Plataformas:** todas. **Referências:** Sicredi (via busca), Revolut BR (10B).

## CMP-FIN-06 — Alerta de segurança/fraude
- **Anatomia:** ícone + título curto → o que aconteceu → ação imediata ("Não fui eu", "Bloquear cartão") → canal de
  ajuda.
- **Regras:** bloco de segurança fixo e acessível na home/site (Nubank "Segurança é prioridade", "Me roubaram", "Canal de
  Denúncias"); vermelho de alerta diferente do CTA de marca (inferência); sem animação chamativa.
- **Referências:** nubank.com.br (10B ✅); Revolut Secure citado na home.

## CMP-FIN-07 — Seletor de período
- **Anatomia:** segmented control ou chips: 12/24/36 meses (crédito) ou 1D · 1W · 1M · 3M · 1Y · ALL (investimento).
- **Regras:** um toque; período ativo no acento; o gráfico e os números mudam juntos; período escrito no título do valor.
- **Referências:** 10B §14; `DgPLR1SDouB` (filtros de tempo acima do gráfico); `dashboard-ui` §8;
  `ux-patterns` `9B_tabs_google-finance-in-page_1.jpg`.

## CMP-FIN-08 — Gerenciador de consentimento e direitos LGPD
- **Anatomia:** lista de finalidades com toggle (desligado por padrão onde não for necessário) → texto claro de cada
  uma → registro de data → ações do titular: acessar, corrigir, exportar (portabilidade), eliminar.
- **Regras:** consentimento em cláusula destacada (LGPD art. 8º); informação clara e ostensiva (art. 9º); direitos do art. 18.
  Banner de cookies com **aceitar / rejeitar / personalizar** no mesmo nível (Monzo, Stripe) (inferência de boa prática).
- **Referências:** `10C_FIN_monzo_home-selos-protecao_1.jpg`, `10C_FIN_stripe_checkout-pagamento_1.jpg` (banners).

## CMP-FIN-09 — Faixa de confiança (volume · regulador · suporte)
- **Anatomia:** 3 colunas com ícone de linha + título + 1 frase: volume movimentado, **regulado por [órgão] com link**,
  suporte 24/7. Variante hero: selos de avaliação nas lojas acima do título; selos de prêmio/proteção no canto do hero.
- **Regras:** só selos reais, verificáveis e de direito do produto; link para o órgão; número com unidade e período.
- **Plataformas:** website. **Referências:** `10C_FIN_wise_selos-confianca-regulacao_1.jpg` (`trust-strip`),
  `10C_FIN_wise_home-hero_1.jpg` (`store-rating-badges`), `10C_FIN_monzo_home-selos-protecao_1.jpg` (`award-seal`,
  `protection-seal`); `website-ui/references/website-patterns.md` §2.

## CMP-FIN-10 — Aviso regulatório fixo
- **Anatomia:** faixa curta, fixa no rodapé do viewport, acima do banner de cookies: natureza da empresa e quem presta o
  serviço regulado.
- **Regras:** visível sem rolagem; texto curto; adaptar à regulação local (o exemplo é norte-americano: "not an
  FDIC-insured bank"); não esconder em rodapé de página (inferência).
- **Referências:** `10C_FIN_mercury_home-aviso-regulatorio_1.jpg` (`regulatory-notice`).

## CMP-FIN-11 — Checkout escolha + resumo
- **Anatomia:** coluna esquerda = escolha (plano em radio, abas de método de pagamento, campos de cartão com bandeiras);
  coluna direita = resumo (plano, preço/período, checklist do que inclui, **total devido hoje** com moeda).
- **Estados:** botão desabilitado até preencher; erro por campo; processando; sucesso.
- **Regras:** total do botão = total do resumo; desconto anual em selo ("Save 22%") ao lado da opção; moeda explícita.
- **Plataformas:** web (2 colunas) e mobile (resumo no rodapé fixo, `mobile-app-ui/references/mobile-patterns.md` §8).
- **Referências:** `10C_FIN_stripe_checkout-pagamento_1.jpg`; planos com "melhor valor" em
  `10C_FIN_stripe-billing_planos-precos-cards_1.jpg` (barra superior + etiqueta no plano destacado).

## CMP-FIN-12 — Barra de limite usado/disponível
- **Anatomia:** nome do limite → barra com parte usada cheia e restante hachurado → % dentro da barra → "usado / total"
  em valor à direita (`$7,189 / $10,000`).
- **Regras:** valor sempre em texto além da barra; cor de alerta só perto do teto (inferência).
- **Referências:** `10C_FIN_dribbble-outcrowd_fintech-dashboard-transferencia_1.jpg` (`limit-bars`).

## CMP-FIN-13 — Ações rápidas + seletor de moeda/conta
- **Anatomia:** abas por moeda/conta com saldo de cada uma → 3–4 ações (Adicionar, Enviar, Converter, Mais) em botões
  quadrados com ícone + rótulo. Variante de cobrança: duas moedas lado a lado e métodos Cartão/Banco/SEPA em linha.
- **Regras:** rótulo sempre visível; 1 ação primária cheia + secundárias em contorno no desktop (`dashboard-ui` §10).
- **Referências:** `10C_FIN_dribbble-conceptzilla_…` (`quick-actions`, `currency-tabs`),
  `10C_FIN_stripe-invoicing_fatura-pagamento-moeda_1.jpg` (`currency-toggle`, `payment-method-buttons`).

## CMP-FIN-14 — Cartão de preço por serviço
- **Anatomia:** título de promessa ("preciso e previsível") → cartão largo por serviço (enviar, receber, cartão) com nome,
  1 frase e botão circular de seta → detalhe com tarifa por operação.
- **Regras:** preço por uso exposto antes do cadastro; sem letras miúdas; comparar com "o que os outros escondem" só com
  dado verificável (inferência).
- **Plataformas:** website. **Referências:** `10C_FIN_wise_precos-transparentes_1.jpg` (`service-price-card`);
  `website-ui/references/website-patterns.md` §4.

---

### Estado vazio de pagamento (variação, sem código próprio)
Cartão de destaque "Adicionar método de pagamento" com ilustração e um botão, acima da tabela de faturas
(`10C_FIN_dribbble-flexy_faturamento-seguro-tablet_1.jpg`, `payment-promo-card`, `invoice-table`). Use ilustração própria.
