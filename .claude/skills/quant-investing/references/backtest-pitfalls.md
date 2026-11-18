# Armadilhas de backtest: lookahead, custos, splits, múltiplos testes e baseline ingênua

Fontes: @rational_edge (`DfFYu5XmREJ` toolkit de bibliotecas, `DfhKkrmsz0w` custos de execução, `Dfo2E88PT0J` leaderboard, só pelo título), @kwaant (`Dfs5F7ZP3oy` Deflated Sharpe, `DfktYl-S6Uz` pipeline de teste), @neuron.machinelearning (`DfowdSMiPzc` baseline ingênua e 91 pares), @artillerytrades (`De7NqmHkbzU` 5 repos). Itens "(complemento)" não vêm dos posts.

> Conteúdo educacional, não recomendação de investimento. Os números dos posts são **simulados/ilustrativos** (declarado pelos autores).

Complementa `validation-tests.md` (Monte Carlo, walk-forward, sensibilidade). Aqui ficam os erros que fazem o backtest mentir **antes** desses testes.

---

## 1. Três regras de "não se engane" (`DfFYu5XmREJ`, slide 8)

| Regra | O que fazer | Erro típico |
|---|---|---|
| **Custos** | Configure taxa, spread e slippage antes do 1º resultado | Três motores populares começam com custo **zero** (backtesting.py, vectorbt, bt) |
| **Timing (lookahead)** | Execute na **barra seguinte** ao sinal (`signal.shift(1)`) | `bt` executa na própria barra do sinal por padrão: "shift it" |
| **Splits** | **Nunca embaralhe o tempo**: `TimeSeriesSplit` | `train_test_split` do scikit-learn embaralha por padrão |

(O autor cita López de Prado, *Advances in Financial Machine Learning* (2018), cap. 7: validação cruzada comum vaza o futuro em finanças; **purging** (e embargo, complemento) corrige.)

### Pegadinhas por biblioteca (conferidas pelo autor em 14/10/2026; versões mudam)
| Biblioteca | Uso | Pegadinha |
|---|---|---|
| backtesting.py (AGPL-3.0) | uma ideia, gráfico interativo | custo padrão zero; um ativo por teste; AGPL obriga abrir código se distribuir/servir |
| vectorbt (Apache + Commons Clause) | grades de 1.000 parâmetros | custo zero; free sem ordem limite/alavancagem; não pode revender |
| bt (MIT) | carteiras, rebalanceamento | executa na barra do sinal |
| NautilusTrader (LGPL-3.0) | ordens reais, event-driven | docs v2, pip instala v1 |
| QuantStats (Apache-2.0) | tearsheet, Sharpe, DD | **win rate conta dias, não trades**; anualiza com **252** (cripto: `periods=365`) |
| statsmodels (BSD-3) | regressões, testes | erro-padrão assume independência → use **HAC** (Newey-West) |
| TA-Lib (BSD-2) | indicadores | um NaN apaga todos os valores seguintes |
| arch (NCSA) | GARCH, bootstrap, **SPA test** (data snooping) | prevê magnitude, não direção; escale retornos ×100 |
| PyPortfolioOpt (MIT) | média-variância, HRP | alimentado com médias passadas, **maximiza o erro** |
| scikit-learn (BSD-3) | ML, CV | `train_test_split` embaralha |

Também descontinuados/pagos na data: backtrader (sem release desde abr/2023), mlfinlab (licença paga), LEAN CLI (tier pago). Antes de adotar: cheque licença e último commit.

### Repos de pesquisa/ML citados por @artillerytrades (`De7NqmHkbzU`, estrelas "as of Oct 2026" segundo o post)
| Repo | O que faz | Cuidado |
|---|---|---|
| microsoft/**qlib** (MIT, ~49k★) | plataforma de pesquisa quant com IA: dados → modelos que preveem retorno → backtest → carteira (Microsoft Research) | (complemento) pipeline pronto não elimina lookahead/custos/múltiplos testes; confira os padrões de custo e o calendário dos dados |
| AI4Finance-Foundation/**FinRL** (MIT, ~16k★) | agentes de *reinforcement learning* que aprendem a operar por tentativa e erro | (complemento) RL em preços é muito propenso a overfit: exija walk-forward, custos e baseline |
| stefan-jansen/**machine-learning-for-trading** (MIT segundo o post, ~21k★) | notebooks do livro *Machine Learning for Algorithmic Trading*: dados, fatores, modelos, backtests | material didático; bom ponto de partida para "ML em trading" |
| polakowo/**vectorbt** (~9,5k★) | backtest vetorizado (NumPy/Numba), milhares de combinações de parâmetros de uma vez | recursos avançados só na edição PRO paga; custo padrão zero (tabela acima); **testar 1.000 settings = 1.000 testes** → deflacione (§3) |
| ranaroussi/**quantstats** (Apache-2.0, ~7,7k★) | tearsheet em uma linha: drawdown, Sharpe, retornos mensais | win rate conta dias e anualiza com 252 (tabela acima) |

O post é marketing ("Hedge fund quants build with these…", CTA "comente QUANT" + Discord de bots); a lista em si é útil. Antes de adotar, cheque licença e último commit.

Mapa "qual usar quando": sinais → TA-Lib/scikit-learn; backtest → backtesting.py / vectorbt / bt / NautilusTrader; sorte ou edge? → arch (SPA), statsmodels (HAC); avaliar → QuantStats; dimensionar → PyPortfolioOpt.

```python
# (complemento) higiene mínima em pandas
pos = signal.shift(1).fillna(0)                 # executa na barra seguinte
ret = pos * px.pct_change() - cost * pos.diff().abs().fillna(0)
from sklearn.model_selection import TimeSeriesSplit
for tr, te in TimeSeriesSplit(n_splits=5).split(X): ...   # sem shuffle
```

---

## 2. Custos de execução: "mesmos trades, quatro verdades" (`DfhKkrmsz0w`)

Scalper de futuros simulado: 1 contrato, 2.000 trades/ano, edge real mas pequeno. Custos somados um a um:

| Etapa | Premissa | Resultado/ano |
|---|---|---|
| Backtest | toda ordem preenchida, sem custo | **+$81.888** |
| + spread e taxas | vende no bid, $4,50 por ida e volta → **$10,75/trade** | +$60.387 |
| + slippage de stop | stop vira ordem a mercado: 2 ticks piores em 33% dos trades | +$43.943 |
| + fills de limite reais | só preenche se o preço atravessar 1 tick; **13% nunca preenchem** | **−$19.826** |

- As ordens limite que não preenchem eram as melhores (+$257 em média no backtest); as que preenchem fazem só **+$8** antes de custos. **Seleção adversa** (complemento: nome usual).
- A ordem em que se somam os custos muda quanto cada um "parece" custar, não o resultado final.
- Conferência: 81.888 − 60.387 = 21.501 ≈ 2.000 × $10,75 = $21.500 ✓. Um frame mostra "68,387" no 2º degrau; a legenda diz 60.387, que é o valor consistente.
- Limites declarados: um setup ilustrativo (grade de ticks, vol 8 ticks/min, drift 1,5 tick/30 min, limite 2 ticks, stop 40 ticks).

Exemplo de @kwaant (`DfktYl-S6Uz`): o mesmo backtest vai de **+184% antes de custos** para **+121% depois** de custos e slippage.

**Regra:** em estratégias de alta frequência/payoff pequeno, modele spread, slippage de stop e probabilidade de fill de limite; não só a corretagem.

---

## 3. Viés de seleção / múltiplos testes

### O problema
"The more settings you test, the less your Sharpe ratio means." Testar 200 versões de uma regra **sem edge** já produz um melhor Sharpe ≈ **1,66** (@kwaant). O "leaderboard" (@rational_edge) mostra quem ganhou, não quantos tentaram. A barra real não é Sharpe > 0, é Sharpe > **o máximo esperado por sorte** dado o nº de tentativas.

### Deflated Sharpe Ratio (Bailey & López de Prado, 2014)
- Escala 0–1: probabilidade de o Sharpe observado vencer a sorte de **tudo o que foi tentado**. Corte usual: **0,95**.
- Exemplo (`Dfs5F7ZP3oy`): Sharpe **1,8** escolhido entre **200** versões → DSR **0,61** ("luck not ruled out"); o mesmo 1,8 entre **10** versões → DSR **0,96**.
- DSR alto quer dizer "provavelmente não é sorte", **não** "dá dinheiro".

Fórmulas (complemento, do paper):
```
SR0  = σ_SR · [ (1−γ)·Φ⁻¹(1 − 1/N) + γ·Φ⁻¹(1 − 1/(N·e)) ]    # máximo esperado de N Sharpes sem edge; γ ≈ 0,5772
DSR  = Φ( (SR − SR0)·√(T−1) / √(1 − g3·SR + (g4−1)/4 · SR²) )  # g3 = assimetria, g4 = curtose; SR na frequência dos T retornos
```
**Conferência (Python):** com dispersão dos Sharpes das tentativas σ_SR ≈ 0,6, SR0(200) = **1,659** (bate com "~1,66") e SR0(10) = 0,945. Calibrando o fator √(T−1)/… para dar 0,61 com N=200 (≈2,0), N=10 dá **0,955 ≈ 0,96**. Os números do post são internamente consistentes; T e σ_SR não foram divulgados.

```python
# (complemento) implementação mínima
from statistics import NormalDist; import numpy as np
N_ = NormalDist(); g = 0.5772156649
def sr0(n_trials, sd_sr):
    return sd_sr*((1-g)*N_.inv_cdf(1-1/n_trials) + g*N_.inv_cdf(1-1/(n_trials*np.e)))
def dsr(sr, n_trials, sd_sr, T, skew=0.0, kurt=3.0):   # sr, sd_sr na frequência dos dados
    z = (sr - sr0(n_trials, sd_sr))*np.sqrt(T-1)/np.sqrt(1 - skew*sr + (kurt-1)/4*sr**2)
    return N_.cdf(z)
```

### Regras práticas
1. **Registre quantas versões testou** (todas: parâmetros, filtros, ativos, períodos). Sem esse número o Sharpe não tem leitura.
2. Reporte o **Deflated Sharpe** (ou, complemento, o SPA/White Reality Check do `arch`) junto do Sharpe.
3. Prefira poucas hipóteses definidas antes de olhar os dados.
4. Toda "melhoria" (stop mais largo, filtro de horário, filtro de tendência...) precisa passar em **dados não vistos**; a que só melhora o passado é descartada (`DfktYl-S6Uz`: "wider stop" marcada OVERFIT).
5. Desconfie de rankings/leaderboards/"melhor estratégia do ano" sem o tamanho da população.

### Múltiplos testes com p-valor: 91 pares, 1 "achado" (`DfowdSMiPzc`)
14 ações → C(14,2) = **91 pares** testados para cointegração (Engle-Granger, corte 5%). **1 passou** (GOOG/GE, t = −4,11 in-sample) e **quebrou fora da amostra** (t = +1,96; spread chegou a **z = +13,4**). Por acaso se esperam 91 × 5% = **4,55** falsos positivos (o post arredonda para 4,5), então 1 em 91 é ruído.

Conferência e correções (complemento, Python):
- P(≥ 1 falso positivo em 91 testes independentes a 5%) = 1 − 0,95⁹¹ ≈ **99%**.
- **Bonferroni** (controla a chance de *qualquer* falso positivo): use α/m = 0,05/91 ≈ **0,00055** por teste. Conservador.
- **Benjamini-Hochberg** (controla a *fração* de descobertas falsas, FDR): ordene os p-valores p(1) ≤ … ≤ p(m) e aceite os k primeiros, com k o maior índice tal que p(k) ≤ (k/m)·q (q = 0,05). Menos conservador; bom para triagem de muitos pares/sinais.
- Em `statsmodels`: `from statsmodels.stats.multitest import multipletests; multipletests(pvals, alpha=.05, method='bonferroni' | 'fdr_bh')`.
- Mesmo passando na correção, **revalide fora da amostra** (tempo posterior): é isso que derrubou o par do exemplo.


---

## 4. Pipeline "como um profissional testaria" (`DfktYl-S6Uz`)

1. **Regras exatas:** ideia em linguagem natural → entrada, stop e alvo objetivos (ex.: pullback à EMA 20, stop 8 pts, alvo 2R).
2. **Backtest com custos e slippage reais** (+184% → +121%).
3. **Testes:** sorte (Monte Carlo), overfitting, dados não vistos (walk-forward), drawdown. Reembaralhando 1.000 vezes: DD do backtest **−16%** vs pior provável (**1 em 20 ordens**, i.e. p95) **−21%**.
4. **Melhorar** só com o que passa em dados não vistos.
5. **Re-rodar todos os testes** na versão melhorada (ex.: +121% → +149%).
6. **Reportar o conjunto completo**, não só o retorno: retorno total, max DD, Sharpe (0,97), win rate (44%), profit factor (1,17), nº de trades (2.097), Sortino/Calmar, long vs short, causa do pior DD, ganho/perda médios, quebra por horário, **tudo o que foi tentado e o que foi descartado como sorte**.

(O post é demonstração do produto do autor; o pipeline é genérico e vale para qualquer ferramenta.)

---

## 5. Baseline ingênua: "53% de acerto" que não é edge (`DfowdSMiPzc`, @neuron.machinelearning)

Random forest prevendo se o mercado (média de 12 ações dos EUA) sobe amanhã; treino 2005–2014, teste 2015–2018 (**823 dias**); features: lags 1–5, vol 21d, momentum 21d.

| Previsor | Acurácia |
|---|---|
| moeda (50/50) | 50,0% |
| random forest | **53,0%** |
| "sempre sobe" | **53,5%** |

Teste binomial da acurácia do modelo contra a taxa de "sempre sobe": **p = 0,78** → sem vantagem. "ML finds patterns. Statistics tells you which ones are real."

**Conferência (Python):** 436/823 = 52,98%; binomial bilateral vs 0,535 → p = **0,780** ✓. Vs a moeda (0,5) → p ≈ **0,094**: nem contra 50% os 53% são significativos a 5%. (complemento) Comparar contra uma taxa fixa é uma simplificação; o teste pareado correto entre dois previsores nos mesmos dias é o de **McNemar** (ou bootstrap em blocos), e acurácia não é lucro: avalie o retorno da regra após custos.

### Regras práticas
1. **Sempre reporte a baseline ingênua** ao lado do modelo: classe majoritária ("sempre sobe"), último valor/persistência, média histórica, buy and hold. Em mercados com drift positivo, "sempre sobe" já passa de 50%.
2. Teste a diferença **contra a baseline**, não contra 50% ou zero.
3. Separe treino/teste **no tempo** (§1); o mesmo post tem 3 sucessos e 2 fracassos e mostra os fracassos (placar ✓/✕).
4. O mesmo vale para previsão de volatilidade: no post, erro médio absoluto 0,500 (naive "mês passado") → 0,477 (GARCH(1,1)) → 0,453 (GARCH + gradient boosting no resíduo).

**Imprecisão da fonte (conferida):** a legenda diz "9% melhor que GARCH sozinho", mas (0,477 − 0,453)/0,477 = **5,0%**; os **9,4%** são contra a previsão ingênua (0,500 → 0,453). O slide final cita "20 US stocks", enquanto o código usa 12–14 tickers. Dados só até 2018; os scripts são isca ("comente QUANT") para venda de livro.

Outros resultados do post (dados reais, um teste cada, sem correção): mistura gaussiana sem rótulos marcou **70%** dos dias de 2008 como crise (14,8% dos dias; vol 3× maior); PCA em 12 ações: PC1 explica **42,7%** da variância, correlação 0,988 com o mercado.

