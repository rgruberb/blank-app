# O que construir para entrar em finanças/quant sem experiência

Fontes: @tradionquant — `DftZ6l2CC_e` (quant) e `DfoRErMChB-` (finanças/banking/PE). Itens "(complemento)" não vêm dos reels.

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

## Como o Claude usa isto
- Pergunta de carreira → recomende a trilha (quant vs IB/PE), os 3 projetos, e o que cada um ensina.
- Para quant, ofereça scaffolding em Python (pandas/numpy; (complemento) `statsmodels` para cointegração/regressão, `yfinance` ou CSV para dados).
- Sempre lembrar: o entregável de valor é o **teste honesto**, não uma curva bonita.
