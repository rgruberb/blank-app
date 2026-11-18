# O que construir para entrar em finanças/quant sem experiência

Fontes: @tradionquant — `DftZ6l2CC_e` (quant) e `DfoRErMChB-` (finanças/banking/PE); @neuron.machinelearning `DfowdSMiPzc` (ML + estatística); @quantfinance.ai `DfztwFuxh4f` (toolkit de pairs) e `Dfr5It0xAzA` (conceitos); @daytrading `DfFnuSOkqi9` (ideias de estratégia). Itens "(complemento)" não vêm dos posts.

> Conteúdo educacional, não recomendação de investimento.

## Trilha quant (`DftZ6l2CC_e`) — "learn by building these three projects"

Dados citados na legenda: Nvidia, Apple e Tesla desde 2021; Coca-Cola e PepsiCo desde 1999; S&P 500 com dividendos desde 1988. Futuros são simulação a partir do histórico, não previsão.

### 1. Monte Carlo Portfolio Risk
- Pegue algumas ações; estime **retornos, volatilidade e correlações**.
- Simule **10.000 futuros** possíveis para o portfólio.
- Da distribuição tire **VaR** (quanto pode perder num mês ruim) e **Expected Shortfall** (quão ruim fica além disso).
- Exemplo na tela: "value at risk — 1 month in 20: lose more than **$1,435**"; "expected shortfall — those worst months: **$1,776** on average". Frames mostram NVDA ~+40%/ano e AAPL ~+20%/ano (últimos 5 anos) e um fan chart ("2,764 simulated futures" ended up vs down).
- **Lição:** a **correlação**, não as ações individuais, é o que dirige o risco do portfólio.

### 2. Pairs Trading / Statistical Arbitrage
- Duas ações que andam juntas (ex.: **Coca-Cola (KO) e PepsiCo**); teste **cointegração**.
- Regrida uma na outra → **hedge ratio** (na tela: "for each Coca-Cola share, hold **0.25** PepsiCo shares").
- Acompanhe o spread como **Z-score**. Quando esticar **2 desvios-padrão**, venda a cara e compre a barata; saia quando reverter. (Tela: z = **+2.27**, "Coca-Cola pricey" → bet against KO, buy PepsiCo.)
- **Lição:** mean reversion — e que **relações podem quebrar**.
- **Toolkit de 4 algoritmos** (@quantfinance.ai `DfztwFuxh4f`, par **simulado**, β verdadeiro 1,5, half-life 10 d, ajuste nos primeiros 750 d e trade nos 750 seguintes):
  | Bloco | Para quê | Nota de produção (do post) | Resultado ilustrativo |
  |---|---|---|---|
  | **Engle-Granger** (OLS + ADF nos resíduos) | hedge ratio β e se o spread é estacionário | teste as duas direções; use valores críticos de EG (≈ −3,3 a 5%), não a tabela ADF comum | β̂ 1,52, ADF −4,7 |
  | **Ornstein-Uhlenbeck** (AR(1) no spread) | velocidade de reversão θ = −ln φ e **half-life = ln 2 / θ** | descarte pares com half-life longa; estimativa ruidosa em amostra curta | half-life 11,5 d (verdadeira 10 d) |
  | **Filtro de Kalman** | β que deriva no tempo (Q = drift, R = variância do spread) | calibre Q e R no treino; monitore as inovações | RMSE de β 0,04 vs OLS 0,05 |
  | **Regra de z-score** | entra em \|z\| > 2 contra o desvio, sai perto de 0,5 | média/desvio rolantes; stop perto de \|z\| = 4; inclua custos e aluguel de ações | Sharpe 0,46 (Kalman) vs 0,23 (OLS estático) |
  O próprio autor avisa: 1 caminho, sem custos, amostra pequena. (complemento) Com ~750 dias, o erro-padrão de um Sharpe anualizado é ≈ √(252/750) ≈ **0,58**: 0,46 vs 0,23 é indistinguível de ruído.
- **Contraexemplo com dados reais** (@neuron.machinelearning `DfowdSMiPzc`): de 91 pares de 14 ações, 1 passou a 5% (esperado por acaso: 4,55) e quebrou após 2016 (z = +13,4). Corrija para múltiplos testes e valide fora da amostra (`backtest-pitfalls.md` §3).

### 3. Moving Average Crossover Backtest
- Compre quando a média de **50 dias** cruza acima da de **200 dias**. É a estratégia mais simples — "and that's the point".
- A habilidade real é **testar**: atrase o sinal em **1 dia** (nunca usar dados do futuro), inclua **custos de transação**, compare contra **buy and hold**.
- Tela: buy and hold **$598,384** vs crossover **$436,007** (**$162,377 a menos**); "16 of 56 versions of this rule (other day counts)". "Most strategies fail right there."

(complemento) Próximos passos naturais: aplicar `validation-tests.md` (Monte Carlo, walk-forward, sensibilidade) ao projeto 3 e publicar o notebook com os resultados negativos — mostrar que você sabe **reprovar** uma estratégia é um sinal forte.

## Trilha finanças / IB / PE (`DfoRErMChB-`) — "three finance projects on your resume"

Dados citados: Form 8-K do FY2026 da Apple, histórico do S&P 500 desde 1988, lucro operacional anual de 10 grandes empresas de chips listadas nos EUA.

### 1. DCF Valuation Model
- Construa tudo você mesmo: **DRE (income statement), balanço, fluxo de caixa** e o **DCF** por cima.
- Projete receita, modele custos, calcule o **WACC**, chegue ao **enterprise value**.
- Tela: vendas da Apple, 4 anos reais (FY23–FY26, pico **$479B** em FY26) e depois **+6%/ano assumido** (FY27–29).
- Por que importa: valuation é a maior parte do trabalho de analistas de banking e PE. "If you can't model, you can't do the job."

### 2. Stock Pitch Deck
- Escolha uma ação, pesquise e monte uma recomendação de compra/venda em **10 slides**: Cover, Thesis, Company, Industry, Financials, Valuation, Catalysts, Risks, (Buy/Sell).
- Inclua tese, financials, valuation, riscos e **price target**; apresente como um equity analyst.
- Por que importa: mostrar que você forma **sua própria visão** e a defende.

### 3. Industry Deep Dive
- Uma indústria a fundo: **cadeia de valor**, principais players, como competem, regulação, **onde o dinheiro é feito**.
- Tela (semicondutores, tamanho = vendas anuais): NVIDIA **$216B**, TSMC **$123B**, Micron **$133B** (como rotulado), além de Broadcom, AMD, ASML, Intel, Qualcomm, Applied Materials, TI.
- Por que importa: bancos atendem clientes **por setor** (tela: Tech, Healthcare, Banks & Insurers, Energy, Consumer, Industrials); quem conhece uma indústria "sounds like they belong in the room" — e é quem fica (Analyst → Associate → VP).

## Outras ideias de projeto vistas nas rodadas seguintes

Só pelo resumo na grade (posts não abertos): @tradionquant `Df1IZS-CY_8` — 3 projetos quant com dados gratuitos (earnings, opções do SPY, S&P desde 1988); `Df3vKx3je7o` — 3 modelos financeiros com balanços reais (Netflix, LBO da Deckers, fusão Capital One + Discover).

### Trilha ML + estatística (@neuron.machinelearning `DfowdSMiPzc`, dados reais até 2018)
Cinco projetos curtos em NumPy/pandas/scikit-learn, cada um com um teste estatístico que diz se o padrão é real:
1. **Volatilidade:** GARCH(1,1) por máxima verossimilhança + gradient boosting corrigindo; erro 0,500 (naive) → 0,477 (GARCH) → 0,453 (híbrido). Melhora de 5% sobre o GARCH (a legenda diz 9%, que é vs naive).
2. **Pairs:** 91 pares, 1 achado = ruído (acima).
3. **Regimes:** mistura gaussiana de 2 componentes em retorno e vol de 21 d, sem rótulos; marca 70% de 2008.
4. **Fatores:** PCA por autovetores da covariância; PC1 = "o mercado" (42,7%, corr 0,988).
5. **Direção:** random forest 53,0% vs "sempre sobe" 53,5%, p = 0,78 → sem edge (`backtest-pitfalls.md` §5).
O valor para portfólio é o **placar ✓/✕ honesto**: mostrar os fracassos junto dos sucessos.

### Ideias de estratégia para backtestar (@daytrading `DfFnuSOkqi9`, só descrição)
Pairs divergence, compressão de volatilidade com rompimento, **post-earnings drift** (a ação segue na direção da surpresa por dias ou semanas; o gráfico do slide mostra BHAR anormal por decil de surpresa), continuação de gap intraday, reversão por z-score, rotação por RSI (momentum relativo) e retorno fechamento→abertura (overnight vs intraday). A legenda cita Python, QuantConnect e Backtrader como plataformas. O post não traz teste próprio e o único gráfico de resultado (rotação por RSI, 1992–2024) mostra a estratégia **abaixo do S&P**; a legenda lembra custos, slippage, overfitting e mudança de regime. Use como lista de hipóteses, cada uma passando pelo gate do `SKILL.md`.

### Conceitos para estudar (grade de @quantfinance.ai `Dfr5It0xAzA`, conteúdo marcado "AI content")
Paridade put-call (C − P = S − K·e^(−rT)), smile de volatilidade, árvore binomial, lema de Itô, regressão linear (β), componentes principais, filtro de Kalman, autocorrelação, lei dos grandes números, caudas gordas, cadeias de Markov, overfitting, max drawdown, information ratio (α ÷ tracking error) e market impact (ordens maiores movem o preço contra você). Serve como roteiro de estudo; as definições são de 1 linha, sem profundidade.

### 4. Placar de regras populares (formato "100 regras" de @tradionquant)
- Escolha regras que circulam (buy the dip, esperar eleição, copiar o Congresso, alta taxa de acerto) e teste cada uma contra **comprar e segurar** com **todas as datas de início**, caixa remunerado e custo. Reporte "venceu X de N" e a diferença média (método em `validation-tests.md` §5).
- Dados gratuitos citados: Ken French Data Library (mercado dos EUA com dividendos, diário desde 1926; T-bills de 1 mês), Yahoo Finance (retorno total), Cboe.
- (complemento) Publique o placar com o nº total de regras testadas: é a forma honesta de lidar com múltiplos testes (`backtest-pitfalls.md` §3).

### 5. Checklist de robustez como biblioteca
- (complemento) Empacote Monte Carlo reshuffle (p95 do DD), walk-forward, heatmap de sensibilidade e Deflated Sharpe num módulo reutilizável e aplique a uma estratégia sua; mostre o que **reprovou**.
- Stack gratuita sugerida por @rational_edge (`DfFYu5XmREJ`): backtesting.py / vectorbt / bt / NautilusTrader, QuantStats, statsmodels (HAC), arch (SPA), TA-Lib, PyPortfolioOpt, scikit-learn (`TimeSeriesSplit`). Pegadinhas de cada uma: `backtest-pitfalls.md` §1.

### Para o stock pitch / equity research: scorecard fundamentalista (método de @brianferoldi)
Registrado só o **método**, sem avaliar nenhuma ação (os posts-fonte analisam empresas específicas; não reproduzimos notas nem recomendações).
- Uma página por empresa: **fase** do negócio (Startup → Hipercrescimento → Alavancagem operacional → Retorno de capital → Declínio) + 7 fatores (negócio, moat, direção do moat, crescimento, gestão, risco, valuation) + sinais verdes/vermelhos + faixa de preço.
- A fase escolhe a métrica: em cíclicas com lucro explodindo, P/L **trailing** engana → olhar o **forward** e dizer por quê; em hipercrescimento, comparar **P/S trailing vs forward** (cap. de mercado ÷ receita LTM vs ÷ receita estimada) e pôr ao lado de crescimento e pares. O forward depende inteiramente da estimativa de receita: se ela falha, o múltiplo real é maior.
- Separe **qualidade do negócio** de **preço**: bom negócio ≠ bom investimento.
- Olhe concentração de clientes, histórico de surpresas vs estimativas, dívida vs caixa e ROIC.
- **Limites do método:** notas 1–5 são julgamento subjetivo, sem fonte dos dados nem backtest das notas; foram achadas inconsistências entre slides do mesmo post (faixas de preço diferentes, nota da legenda ≠ nota do card, sinais de template que contradizem a nota). (complemento) No seu pitch, cite a fonte de cada número, explique o método da faixa de preço e confira a consistência interna.

## Como o Claude usa isto
- Pergunta de carreira → recomende a trilha (quant vs IB/PE), os 3 projetos, e o que cada um ensina.
- Para quant, ofereça scaffolding em Python (pandas/numpy; (complemento) `statsmodels` para cointegração/regressão, `yfinance` ou CSV para dados).
- Sempre lembrar: o entregável de valor é o **teste honesto**, não uma curva bonita.
