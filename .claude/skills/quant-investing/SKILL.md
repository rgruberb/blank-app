---
name: quant-investing
description: Análise quantitativa e validação de estratégias de trading/investimento — explica por que estratégias funcionam no backtest e falham ao vivo, roda testes de robustez em Python (Monte Carlo reshuffle de trades, walk-forward, sensibilidade de parâmetros), desmonta a falácia da alta taxa de acerto com expectativa/payoff/drawdown após custos, e orienta quem quer entrar em finanças/quant sem experiência com projetos de portfólio. Use quando o usuário mencionar "backtest", "validar estratégia", "taxa de acerto" / "win rate", "Monte Carlo", "walk-forward", "overfitting", "drawdown", "expectativa", "carreira quant" ou projetos para currículo em finanças.
---

# Quant Investing — validação de estratégias e carreira quant

> **Aviso:** conteúdo educacional, não recomendação de investimento. Os números vêm de exemplos **simulados** dos reels-fonte. Sempre diga isso ao usuário ao falar de estratégias reais.

## Princípios centrais
1. **Backtest bonito ≠ edge.** Exemplo da fonte: +373% in-sample e falha ao vivo porque três testes não foram rodados.
2. **A única pergunta da taxa de acerto:** *depois dos custos, o trade médio ganha dinheiro?* Win rate 90% pode perder sempre (9.999 de 10.000 traders simulados perderam).
3. **Teste o que pode dar errado:** a sorte da sequência (Monte Carlo), dados não vistos (walk-forward), vizinhança dos parâmetros (sensibilidade).
4. **Compare com buy and hold.** "Rules that beat holding: 0 of 1"; crossover 50/200 terminou $162.377 abaixo do buy and hold.

## Checklist antes de ir ao vivo (gate)
Reprovou em um item → não vai ao vivo (ou volta para pesquisa).

- [ ] **Sem look-ahead:** sinal atrasado em 1 dia (sinal no fechamento do dia 1, ordem no dia 2).
- [ ] **Custos incluídos** (taxas, e (complemento) slippage/spread).
- [ ] **Bate buy and hold** no mesmo período/ativo.
- [ ] **Expectativa > 0 após custos:** `E = p·W − (1−p)·L − custo`.
- [ ] **Monte Carlo (≈1.000 reshuffles):** dimensione risco pelo **p95 do max drawdown**, não pelo do backtest. Alerta se alguma ordem plausível **dobra** o DD (exemplo: 5,9% → 14,0%, 2,4x).
- [ ] **Walk-forward:** otimiza numa janela, testa na seguinte, várias janelas; OOS deve manter **uma parte sólida** do desempenho IS. Só funciona onde otimizou → "memory", não edge.
- [ ] **Sensibilidade:** mexa cada parâmetro um pouco; precisa ser **platô** (vizinhos funcionam). **Pico solitário** = reprovado.

Detalhes, código e critérios: `references/validation-tests.md`.

## Métricas que importam vs taxa de acerto
| Métrica | Fórmula / leitura | Por que |
|---|---|---|
| Expectativa (trade médio) | `p·W − (1−p)·L − c` | Decide se ganha dinheiro. Deve ser > 0 **após custos** |
| Payoff ratio | `R = W / L` | Win rate só tem sentido junto com R |
| Breakeven win rate | `p* = (L + c)/(W + L)` | Ex.: alvo 1 / stop 9 com custo 0,45W exige **94,5%** |
| Max drawdown (p95 MC) | percentil 95 dos reshuffles | O que a conta ao vivo vai ver um dia |
| Desempenho OOS / IS | walk-forward | Distingue edge de memória |
| Excesso vs buy and hold | retorno estratégia − B&H | Se não supera segurar, para quê? |

**Taxa de acerto sozinha não diz nada:** ela mostra onde o alvo foi colocado, não habilidade. Alta taxa + payoff baixo é hipersensível a custos. Ver `references/win-rate-fallacy.md`.

## Workflow: analisar a estratégia/backtest do usuário
1. **Pedir dados** (o que faltar):
   - Lista de trades (retorno % ou P&L por trade, com datas) **ou** série de preços + regras exatas.
   - Custos assumidos (taxa, slippage), capital, tamanho de posição.
   - Parâmetros e como foram escolhidos (otimizados? em qual período?).
   - Período in-sample vs out-of-sample, ativo e benchmark.
2. **Higiene:** checar look-ahead (`shift(1)` no sinal), custos, survivorship (complemento) e benchmark buy and hold.
3. **Métricas básicas** em Python (pandas/numpy): n trades, `p`, `W`, `L`, `R`, expectativa antes/depois de custos, `p*`, max DD, retorno vs B&H.
4. **Monte Carlo:**
   ```bash
   python .claude/skills/quant-investing/scripts/mc_drawdown.py trades.csv --mode pct --n 1000   # retornos fracionários
   python .claude/skills/quant-investing/scripts/mc_drawdown.py trades.csv --mode pnl --capital 10000
   ```
   Usa a última coluna numérica do CSV (`--col N` para outra). Reporta DD do backtest, percentis p5–p99, razão p95/backtest e alerta se ≥2x.
5. **Walk-forward** (se houver preços + regras): janelas train/test rolantes, parâmetros escolhidos só no train; reportar OOS por janela e agregado vs IS.
6. **Sensibilidade:** grade ±alguns passos em cada parâmetro → heatmap; classificar como platô ou pico.
7. **Relatório** ao usuário, curto:
   - Veredito por item do checklist (passa / reprova / sem dados).
   - Tabela de métricas; DD p95 sugerido para dimensionamento.
   - Principais riscos (custos, overfit, sorte da sequência, regime).
   - Aviso educacional. Nunca prometa retorno nem recomende comprar/vender ativo.

Se o usuário só tem win rate/“setup de 90%”: calcule `p*` com o payoff e custo dele e mostre a expectativa — essa é a resposta.

## Carreira quant / finanças sem experiência
- **Quant:** (1) Monte Carlo de risco de portfólio (VaR/ES; correlação manda no risco), (2) pairs trading com cointegração, hedge ratio e z-score ±2, (3) backtest de crossover 50/200 com sinal atrasado, custos e B&H.
- **IB/PE/Equity research:** (1) modelo DCF completo (3 demonstrativos + WACC → EV), (2) stock pitch de 10 slides com price target, (3) industry deep dive.
Detalhes: `references/quant-portfolio-projects.md`.

## Quando abrir cada arquivo
| Situação | Abrir |
|---|---|
| Rodar/explicar Monte Carlo, walk-forward, sensibilidade, higiene de backtest | `references/validation-tests.md` |
| "Minha estratégia acerta 80/90%", expectativa, payoff, custos | `references/win-rate-fallacy.md` |
| Carreira, portfólio, currículo, "por onde começo em quant/finanças" | `references/quant-portfolio-projects.md` |
| Precisa ver gráfico/número original ou citar a fonte | `references/visual-index.md` → imagem em `assets/visual-refs/` |
| Imagem `DfuDLH7BUsx.jpg` | ilustrar os 3 testes de robustez (DD 5,9%→14,0%, platô vs pico) |
| Imagem `DfVf0L-AIkP.jpg` | ilustrar 90% vs 35% e “fee eats almost half” |
| Imagens `DftZ6l2CC_e.jpg` / `DfoRErMChB-.jpg` | projetos quant / projetos IB-PE |
