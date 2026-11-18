# Testes de robustez antes de ir ao vivo

Fonte principal: @rational_edge, reel `DfuDLH7BUsx` ("Why it works in the backtest and fails live: you never ran these").
Complementos de @tradionquant `DftZ6l2CC_e` (higiene de backtest) e `DfVf0L-AIkP` (comparar contra buy and hold).
Seções 4–5: @rational_edge `Dfj-RfohT0S` (drawdown normal / quando desligar) e @tradionquant `DfjCMULExt_`, `DfV5v9TFUhf`, `DfdO2jkgZ-f` (regra vs benchmark em muitas janelas). Lookahead, custos de execução, splits e múltiplos testes: `backtest-pitfalls.md`.
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

## 4. Drawdown esperado e regra de desligamento (`Dfj-RfohT0S`)

Pergunta: "a estratégia está no vermelho: quebrou ou é azar?" Simulação de **10.000 estratégias boas** (+10%/ano, vol 10%, **Sharpe 1**) e **10.000 mortas** (−2%/ano, mesma vol), 3 anos, retornos diários normais, sem custos, seed 99.

| Pergunta | Resultado |
|---|---|
| Quanto tempo abaixo do pico é normal? | Boas passam **90% dos dias** abaixo da própria máxima; maior trecho típico sem nova máxima: **10,7 meses** |
| Quão fundo é normal? | Desligar a **−10%** mata **64%** das boas (e 97% das mortas) em 3 anos; a **−20%** mata **5%** das boas e **52%** das mortas |
| Quanto tempo para saber? | Após 6 meses, **19%** das boas parecem piores que uma morta típica; 1 ano: 11%; 3 anos: **1,8%** |

**Conferência (Python, mesma configuração):** 90,4% dos dias abaixo do pico; −10% mata 63,7% das boas e 96,6% das mortas; −20% mata 4,7% e 51,6%. **Reproduz o post.** (Um frame do resumo em baixa resolução parece dizer "12%" e "2 anos"; a legenda e a simulação confirmam 52% e 3 anos.)

**Regras:**
- Defina o critério de desligamento (DD máximo, tempo sem nova máxima) **antes** de ir ao vivo e calibre-o pela **vol** da estratégia: o DD escala ~linearmente com a vol (vol 20% ⇒ DDs ~2x).
- Regra mais apertada sempre mata mais **das duas** (boas e mortas); não existe corte que só elimine as ruins.
- Com Sharpe 1, ficar ~10 meses lateral é normal. 6 meses de ao vivo não distinguem edge de azar; ~3 anos sim.
- Limites declarados: caudas reais são mais gordas e edges decaem, então DDs reais podem ser piores.
- (complemento) Use o p95 do DD do Monte Carlo (seção 1) como limite de desligamento, com folga, em vez de um número redondo.

```python
# (complemento) reproduzir
import numpy as np
rng = np.random.default_rng(99)
r = rng.normal(0.10/252, 0.10/np.sqrt(252), (10_000, 756))
eq = np.cumprod(1+r, 1); pk = np.maximum.accumulate(np.maximum(eq, 1), 1)
dd = 1 - eq/pk
print((eq < pk).mean(), (dd.max(1) >= .10).mean(), (dd.max(1) >= .20).mean())
```

---

## 5. Regra vs benchmark em muitas janelas ("venceu X de N")

Padrão dos testes de @tradionquant ("Testing 100 trading rules"), com dados reais:

| Teste | Desenho | Resultado |
|---|---|---|
| Buy the dip (`DfjCMULExt_`) | Mercado dos EUA com dividendos (Ken French/CRSP, diário, 1926–2026). Conta A compra no dia 1; conta B fica em **T-bills** até o mercado fechar 10% abaixo da máxima, então compra e segura. Custo **0,10%** por compra, sem impostos. Novo início **todo fim de mês** de 1926 a 2016 (**1.084 inícios**), avaliação 10 anos depois | Esperar venceu só **47,1%** (2 empates). Exemplo out/2006→set/2026: US$ 84.606 vs 82.966 (−US$ 1.640) |
| Esperar as midterms (`DfV5v9TFUhf`) | 25 eleições (1926–2022); compra no fim de setembro vs caixa em T-bills até a véspera; ambos avaliados 1 ano após o voto | Comprar em setembro teve mais **19 de 25** vezes; esperar custou ~US$ 13 por semana a cada US$ 10.000. Em 2026 esperar ganhou (7ª vez em 26): "ou sorte?" |
| Copiar o Congresso (`DfdO2jkgZ-f`) | ETFs NANC e GOP vs SPY, US$ 10.000, 07/02/2023–05/11/2026, retorno total líquido de taxas | NANC +US$ 589, GOP −US$ 2.235 (−12%) vs SPY; vantagem do NANC encolheu de US$ 1.072 para 589 |

**Regras de desenho de teste:**
1. Teste contra a **alternativa simples investível** (comprar já / SPY / buy and hold), não contra zero.
2. Caixa parado deve render (T-bills/CDI); custo de transação incluso.
3. Use **todas as datas de início** possíveis (janelas rolantes, horizonte fixo), não um exemplo escolhido. Reporte "**venceu X de N**" **e** a diferença média.
4. Faça **robustez da data/parâmetro** (ex.: qualquer data de 1/09 a 15/10 não muda a conclusão).
5. **Isole a janela que difere** entre as estratégias (as ~6 semanas antes do voto) para explicar o resultado.
6. Considere **defasagem de informação** (Congresso reporta até 45 dias depois).
7. Uma janela única (3,7 anos) ou um acerto recente não valida a regra: sem teste de significância, pergunte "foi sorte?".
8. Mantenha um **placar de regras testadas** ("Rules that beat holding: 0 of 2") e conte as tentativas (ver múltiplos testes em `backtest-pitfalls.md`).

(complemento) Janelas rolantes mensais se sobrepõem (1.084 janelas de 10 anos não são 1.084 observações independentes; são ~9 blocos independentes). Não trate "47,1%" como proporção com erro-padrão binomial ingênuo.

---

## Resumo do gate

| Teste | Pergunta | Passa | Reprova |
|---|---|---|---|
| Higiene | Sem look-ahead, com custos, vs buy and hold? | Sinal atrasado 1 dia, custo incluso, bate B&H | Qualquer item faltando / perde do B&H |
| Expectativa | Trade médio > $0 **após custos**? | Sim | Não (ver `win-rate-fallacy.md`) |
| Monte Carlo | Qual DD a sequência pode gerar? | Risco dimensionado pelo p95 | Ordem plausível dobra o DD e você dimensionou pelo backtest |
| Walk-forward | Funciona em dados não vistos? | OOS mantém boa parte do IS | Só funciona in-sample |
| Sensibilidade | Vizinhos funcionam? | Platô | Pico solitário |
| Múltiplos testes | Quantas versões tentou? Deflated Sharpe? | DSR ≥ 0,95 com N registrado | N desconhecido / DSR baixo |
| Desligamento | Critério definido antes? | DD máx. calibrado pela vol/p95 | Desliga "no feeling" ou −10% com vol 10% |
| Janelas | Venceu em quantas de N janelas? | Maioria + diferença média > 0 | Um exemplo escolhido / uma janela só |
