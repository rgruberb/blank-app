# Testes de robustez antes de ir ao vivo

Fonte principal: @rational_edge, reel `DfuDLH7BUsx` ("Why it works in the backtest and fails live: you never ran these").
Complementos de @tradionquant `DftZ6l2CC_e` (higiene de backtest) e `DfVf0L-AIkP` (comparar contra buy and hold).
Itens marcados "(complemento)" são conhecimento geral, não vêm dos reels.

> Conteúdo educacional. Os números dos reels são de exemplos **simulados**, não recomendação de investimento.

O reel abre com o problema: um backtest in-sample de **+373%** e uma linha "live (out-of-sample)" que anda de lado/cai. A tese: o algoritmo funciona no backtest e falha ao vivo porque três testes nunca foram rodados. O autor diz que descarta **a maioria das estratégias** nesses testes, antes de chegarem ao MetaTrader.

---

## 0. Higiene do backtest (pré-requisito)

Fonte: `DftZ6l2CC_e` (projeto 3, MA crossover 50/200).

| Item | Regra | Reprova se |
|---|---|---|
| Look-ahead | Atrase o sinal em **1 dia**: sinal no fim do dia 1, entrada/saída no dia 2 | O sinal usa o fechamento do mesmo candle em que opera |
| Custos | Inclua custos de transação | Backtest sem custo, ou custo irreal |
| Benchmark | Compare com **buy and hold** | Não supera segurar o ativo |

Número da imagem: no S&P 500 com dividendos, um painel mostra "**16 of 56** versions of this rule (other day counts)" em destaque vermelho (o critério exato dessas 16 não é legível no frame); o gráfico ao lado mostra buy and hold **$598,384** vs crossover **$436,007** (**$162,377 a menos**). "Most strategies fail right there."
Em `DfVf0L-AIkP`, o placar final é "Rules that beat holding: **0 of 1**".

(complemento) Também cuide de survivorship bias, dados ajustados por splits/dividendos e slippage.

---

## 1. Monte Carlo (reshuffle de trades)

**O que é.** Pegue a lista de trades do backtest e embaralhe a ordem ~**1.000 vezes**. Os trades são os mesmos; só a sequência muda. "You're not testing the strategy. You're testing the luck of the sequence."

**Como rodar.**
```bash
python .claude/skills/quant-investing/scripts/mc_drawdown.py trades.csv --mode pct --n 1000
#   --mode pct : retorno fracionário por trade (compõe)
#   --mode pnl : P&L em dinheiro por trade (soma a --capital)
```
O código mostrado no reel faz o mesmo: `rng.permutation(trades)`, `equity = np.cumprod(1 + order)`, `peak = np.maximum.accumulate(equity)`, `dd = 1 - equity/peak`, e tira um percentil dos max drawdowns.

**Critério (texto na tela).** "Size for the **95th-percentile drawdown**, not the backtest one."
Exemplo do reel: max DD do backtest **5,9%** → p95 simulado **14,0%** → **2,4x**.

**Reprova / alerta se:** alguma ordem plausível **dobra** o drawdown ("If some order doubles your drawdown, your live account will see it eventually"). Na prática: se p95/backtest ≥ 2x, o tamanho de posição baseado no DD do backtest está errado — redimensione pelo p95 ou descarte se o p95 passa do seu limite de perda.

(complemento) Reshuffle não altera retorno total nem expectativa (mesmos trades), só o caminho. Não captura mudança de regime nem dependência serial; para isso, use bootstrap com reposição ou block bootstrap.

---

## 2. Walk-forward

**O que é.** Otimize em um bloco de histórico, teste no bloco seguinte (dados nunca vistos). Repita janela após janela.

**Como rodar.**
1. Divida a série em janelas: `train` (otimização) + `test` (fora da amostra) e avance.
2. Em cada janela, escolha parâmetros só com `train`; aplique fixos em `test`.
3. Concatene os segmentos de teste: essa é a curva out-of-sample.
O reel mostra uma função `walk_forward(prices, train=..., test=...)` com `for start in range(0, last, test)`, e um exemplo com **5 janelas** e OOS **+32,0%**.

**Critério (texto na tela).** "Out-of-sample should keep a **solid share of in-sample performance**."
(O reel não define um percentual exato; (complemento) uma régua comum é exigir que o OOS preserve uma fração relevante do IS — p. ex. ≥50% — e seja positivo na maioria das janelas.)

**Reprova se:** só funciona onde foi otimizado. "If it only works where you optimized it, that's not an edge. That's memory."

---

## 3. Sensibilidade de parâmetros

**O que é.** Mexa um pouco em **cada** parâmetro e veja o resultado na vizinhança (heatmap de parâmetro A x parâmetro B).

**Como rodar.** Grade em torno dos valores escolhidos (ex.: ±1–3 passos em cada eixo); rode o backtest em cada célula; plote heatmap do lucro/Sharpe. O reel mostra `sensitivity(strategy)` com loop duplo `for i, lb in enumerate(LOOKBACKS): for j, st in enumerate(STOPS)` e uma função `neighbors(...)` que checa a vizinhança.

**Critério (texto na tela).** "Neighbouring parameters should still work. **A lone peak is a warning.**"
- Edge real = **platô**: tudo ao redor ainda funciona (no exemplo verde, "plateau" **100%** das vizinhas ok).
- **Pico solitário** (uma célula verde cercada de vermelho) = overfit.

**Reprova se:** é um "lonely spike" — "the first regime change kills it".

---

## Resumo do gate

| Teste | Pergunta | Passa | Reprova |
|---|---|---|---|
| Higiene | Sem look-ahead, com custos, vs buy and hold? | Sinal atrasado 1 dia, custo incluso, bate B&H | Qualquer item faltando / perde do B&H |
| Expectativa | Trade médio > $0 **após custos**? | Sim | Não (ver `win-rate-fallacy.md`) |
| Monte Carlo | Qual DD a sequência pode gerar? | Risco dimensionado pelo p95 | Ordem plausível dobra o DD e você dimensionou pelo backtest |
| Walk-forward | Funciona em dados não vistos? | OOS mantém boa parte do IS | Só funciona in-sample |
| Sensibilidade | Vizinhos funcionam? | Platô | Pico solitário |
