# Rodada 4B: perfis de trading quantitativo no Instagram

*Coletado em 18/11/2026, só leitura: nenhuma curtida, comentário ou follow.*

## Resumo da rodada

1. Os perfis mais rigorosos mostram a **premissa do teste na legenda**: universo, período, custos e limitações. Faça isso o filtro nº 1: sem premissa, nota baixa.
2. **Drawdown "normal" é bem maior do que parece.** Numa simulação do @rational_edge, uma estratégia boa (Sharpe 1) passa 90% dos dias abaixo do próprio pico. Um stop de −10% na estratégia mataria 64% das boas em 3 anos.
3. **Viés de seleção / múltiplos testes** é o tema da vez. O Deflated Sharpe (@kwaant) e o "leaderboard" (@rational_edge) mostram que o melhor de N backtests sem edge já parece ótimo: Sharpe ≈ 1,66 com 200 versões.
4. **Três testes de robustez antes de operar ao vivo:** Monte Carlo reembaralhando trades (use o DD do percentil 95, não o do backtest), walk-forward e sensibilidade de parâmetros (procure platô, não pico).
5. **Taxa de acerto não diz nada sozinha.** Com preço aleatório e custo por trade, 9.999 de 10.000 traders com 90% de acerto perderam dinheiro. A métrica que conta é o **trade médio depois dos custos** (@tradionquant).
6. **"Esperar a queda" vs. comprar já** (dados Ken French/CRSP, 1926–2026, 1.084 inícios): esperar ganhou em só 47,1% das janelas de 10 anos.
7. Os perfis sugeridos pelo Instagram são **pouco úteis para @tradionquant**: a lista é genérica e personalizada. Os de @rational_edge são melhores, mas misturam instituições (IMC, Citadel, J.P. Morgan) com perfis de varejo e sinais.
8. Nas hashtags há muito "comente X para receber", AI-hype e marketing de ferramenta. #tradingsistematico é quase todo varejo e robôs à venda, e não rendeu nenhum candidato.
9. Dois dos melhores (@kwaant, @quantwright) **vendem software de backtest**, não sinal. O conteúdo é educativo, mas o CTA é de produto.

---

## 1. Perfis sugeridos ("Sugestões para você")

### A partir de @tradionquant
A lista veio genérica e personalizada, sem relação com o tema. Na maior parte são perfis pessoais, de games e de clips.
Relevantes ou parcialmente relevantes: `whyitworks.maths`, `tickr_lab`, `investing.md`, `capitalhank`.
O resto descartei por estar fora do tema: gamedrops.gg, abbas0007, ceocuts.clips, dudateperino, shorthair_audrey, crisconcham, therozengirls, massucattoj, scott.yale, arash_kmh, natancyt, raymondzhang98, rohanab10, larissakup, alexnewcomer_, miranda_halsey, dra.giselebernstein e outros (80 no total).

### A partir de @rational_edge (75 perfis; os ligados a finanças)
- **Instituições:** imctrading, citadelsecurities, hudsonrivertrading, jpmorganassetmanagement, jpmorganprivatebank, jpmwealth, kkr, ishares, onecarlyle, fortune500, lse
- **Educação quant/finanças:** quantguy_usa, quantchics, quant.finance.institute, corporate_finance_institute, 365financialanalyst, macro_quant_rick, davidarias_cfa, quantscience_, quant.dhawan, quanta.financee, matfinog, arbitrage.andy
- **Varejo / trading discricionário / sinais (descartar):** orderflowschool, wallstbets, atraintrades, orochitrading, nuranatrades, your_finance_brother, floorinsider, worldclassedge, astongilltrading, vagafx, ayaantrades, trdr_john, confluencetrading, iamideaguy

## 2. Hashtags: perfis que apareceram (contagem entre os ~45 posts de topo carregados)

- **#quanttrading:** quantfinance.ai (4), ayaantrades (4), fidetolabs (4), fidetolabs.math (3), arwazaz_ (3), kwaant (4), seb.ai (2), quantguy_usa (2), artillerytrades (2), drjuliankam (2), sumedhhkumar.ai (2), rational_edge, atsmatrix, iclosegreen, quantmind.lab, quantstackai, hunidcapital, raycfu, holisticapital, deltatrendtrading, cloud9.markets
- **#algotrading:** quantfinance.ai (4), arwazaz_ (3), quantstackai (3), algoexchange (3), algocourt (2), atsmatrix (2), kwaant (2), it_munch (2), quant_swing_algo_fintech (2), rational_edge, quantnative, code2model, trendspider, sentinel.trades, tickr.trades, mirkovicdev, athenixacademy, artillerytrades, sjosephburns, msbintel, syntaix.ai, invista.ja
- **#backtesting:** kwaant (4), arwazaz_ (4), algocourt (3), syntaix.ai, sentinel.trades, proplensapp, quantifiedstrategies, fidetolabs, tradezella (2 cada), rational_edge, quantfinancetogo, bayesiansystems, quantwright, quantgauge, stratos_quant, thealphainsider, propquantx, quantnative, quantfinance.ai, vagafx
- **#quantfinance:** quantfinance.ai (4), quantguy_usa (4), quantfinancetogo (3), davidarias_cfa (3), datainterview, quant.dhawan, nishantaqc, tradelyze.io, quantcurve, oddsandlines, aryanbuildsai, quant_research_decoded, quant.lab.ai (2 cada), quantpapers, rational_edge, quantnative, quant_grad, quantdi, mirkovicdev
- **#tradingsistematico:** robustus.studio, tradingalgoacademy.es, rock.quant (2), tradingnote.co (2), sersansistemas (2), holotrading (2), quantprotocol, robotizztrader, facil__investir (2). Quase tudo é varejo e robô; nenhum entrou na lista.

**Descartados de propósito:** quantifiedstrategies (vende estratégias, tem destaque "Testimonials"), arwazaz_ ("comente X para receber"), bayesiansystems (foco em prop firm, destaque "Results"), seb.ai ("AI & Income", hype), ayaantrades / atraintrades / iclosegreen (trading discricionário de varejo), whyitworks.maths (3 posts, 13 seguidores: cedo demais), quantscience_ (venda de curso).

## 3. Lista de candidatos (10)

| # | @handle | Link | Seguidores | Último post | Descrição | Rigor (1–5) |
|---|---|---|---|---|---|---|
| 1 | @rational_edge | https://www.instagram.com/rational_edge/ | 8.091 | 14/11/2026 | Pesquisa quant sistemática: simulações de drawdown, robustez e viés de seleção, com premissas explícitas | **5** |
| 2 | @tradionquant | https://www.instagram.com/tradionquant/ | 1.980 | 17/11/2026 | Testa "regras de trading populares" com simulação e dados reais (Ken French/CRSP), metodologia na legenda | **5** |
| 3 | @kwaant | https://www.instagram.com/kwaant/ | 1.118 | 17/11/2026 | Deflated Sharpe, walk-forward, custos; CTA de lista de espera do próprio software | **4** |
| 4 | @quantfinancetogo | https://www.instagram.com/quantfinancetogo/ | 73,2 mil | 18/11/2026 | "Quant finance de A a Z": série de conceitos com código; bio diz "No financial advice" | 4 |
| 5 | @quantpapers | https://www.instagram.com/quantpapers/ | 80,4 mil | 13/10/2026 | Papers de quant finance resumidos (só 11 posts) | 4 |
| 6 | @quant_research_decoded | https://www.instagram.com/quant_research_decoded/ | 44,2 mil | 16/06/2026 | Pesquisador quant explicando modelos institucionais (último post há 5 meses, perto do limite) | 4 |
| 7 | @fidetolabs.math | https://www.instagram.com/fidetolabs.math/ | 2.971 | 17/11/2026 | "Math for Quant": filtros CUSUM, amostragem de eventos (linha López de Prado) | 4 |
| 8 | @fidetolabs | https://www.instagram.com/fidetolabs/ | 18 mil | 17/11/2026 | Ferramentas de dados para o fluxo quant; divulga comunidade (paga?) | 3 |
| 9 | @datainterview | https://www.instagram.com/datainterview/ | 5.051 | 17/11/2026 | Preparo para entrevistas quant/DS; explica estratégias com números (ex.: reversão à média com Bollinger) | 3 |
| 10 | @quantwright | https://www.instagram.com/quantwright/ | 171 | 17/11/2026 | Agente de pesquisa de backtest ("sem se enganar"); marketing de produto | 3 |

*Notas 4, 6, 7, 8, 9 e 10: dei com base na bio e em 1–2 legendas, sem análise de slides.*

**Top 3 escolhidos para análise:** @rational_edge, @tradionquant, @kwaant.

---

## 4. Análise dos posts

*Os seis posts são reels. As legendas estão resumidas com fidelidade (números mantidos), não copiadas na íntegra: o texto completo está no link de cada post. Os "slides" são os quadros do vídeo lidos em vários tempos (t = segundos).*

### DfuDLH7BUsx — @rational_edge
- Link: https://www.instagram.com/p/DfuDLH7BUsx/ · 14/11/2026 · ~2.175 curtidas
- Tipo: reel (46 s)
- Tema: backtest/validação
- Legenda (resumo): explica por que a estratégia funciona no backtest e falha ao vivo: faltaram três testes antes de entrar ao vivo (reembaralhamento Monte Carlo, walk-forward e sensibilidade de parâmetros). Para cada teste há um ponto a conferir na tela. Pede para salvar o post e oferece um guia de testes de robustez para quem comentar "TEST". Avisa que é exemplo simulado e não é recomendação. Hashtags: #algotrading #quantfinance #backtesting #riskmanagement #systematictrading.
- Quadro a quadro:
  - t≈2: título "Why does your algorithm work in the backtest, and fail live? You never ran these." Gráfico "Equity – simulated": backtest in-sample (tracejado branco) sobe até ~+300%; live out-of-sample (azul) fica perto de 0%. Eixo X Y1–Y5. Cartões: BACKTEST **+373%**, LIVE **−0,4%**.
  - t≈9: "1 · Monte Carlo (Test 1/3)": "Size for the 95th-percentile drawdown, not the backtest one." Leque de 1.000 curvas de equity ("Reshuffles 1,000", 160 trades). Código `monte_carlo.py`: `rng = np.random.default_rng(seed)`; loop `order = rng.permutation(trades)` (mesmos trades, nova ordem), `equity = np.cumprod(1 + order)`, `peak = np.maximum.accumulate(equity)`, `dd[i] = (1 - equity/peak).max()`, `return np.percentile(dd, 95)`.
  - t≈16: histograma dos max drawdowns. Cartões: BACKTEST MAX DD **5,9%** · WORST 5% OF ORDERS **14,0%** · VS THE BACKTEST **2,4×**.
  - t≈23–26: "2 · Walk-forward (Test 2/3)": "Out-of-sample should keep a solid share of in-sample performance." Janelas Optimize/Test deslizando sobre 7 anos (Y1–Y7), "Window 5/5". Código `walk_forward.py`: `fit = prices[start:start+train]`, `nxt = prices[start+train:start+train+test]`, `pf = sensitivity(fit)`, escolhe o melhor (lookback, stop) e `oos.append(backtest(nxt, *best))`. Cartões: WINDOWS TESTED **5** · IN-SAMPLE / YEAR **+32,0%**. A curva OOS (vermelha) cai abaixo de 0%.
  - t≈29: "Test 3 of 3 – Sensitivity", `sensitivity(strategy)`.
  - t≈36: "3 · Parameter sensitivity": "Neighbouring parameters should still work. A lone peak is a warning." Heatmap Profit factor (lookback × stop, eixos 10–70 × 1,0–4,0) e grade 5×5 "Plateau" com PF entre ~1,26 e 1,40. Código: `pf[i,j] = profit_factor(trades)`; `neighbours_ok(pf,i,j)`: `near = pf[max(i-2,0):i+3, max(j-2,0):j+3]`, `return (near > 1).mean()`. Cartão: PLATEAU · NEIGHBOURS OK **100%**.
  - t≈44: "Follow @rational_edge for more quantitative insights".
- Regras/lições práticas:
  - Dimensione o risco pelo drawdown do **percentil 95** do Monte Carlo (aqui 2,4× o DD do backtest), não pelo DD histórico.
  - Walk-forward: otimize numa janela, teste na seguinte, nunca vista. O OOS precisa reter uma fração relevante do IS.
  - Sensibilidade: o ótimo deve estar num **platô**; se os vizinhos têm PF ≤ 1, é overfitting.
  - Backtest de +373% com ao vivo de −0,4% é o sintoma clássico de não ter feito esses testes.
- Evidência: exemplo **simulado**, com código Python na tela (numpy). Não usa dados reais nem cita fonte.

### Dfj-RfohT0S — @rational_edge
- Link: https://www.instagram.com/p/Dfj-RfohT0S/ · 10/11/2026
- Tipo: reel (53 s)
- Tema: risco e drawdown
- Legenda (resumo): "Sua estratégia está no vermelho: quebrou ou é azar?" Simulação de 10.000 estratégias com edge real (+10%/ano, vol 10%, Sharpe 1) e 10.000 mortas (−2%/ano, mesma vol) durante 3 anos.
  1. *Quanto tempo é normal?* As boas passam 90% dos dias abaixo do pico; o maior período típico sem nova máxima é de 10,7 meses.
  2. *Quão fundo é normal?* Desligar a −10% mata 64% das boas (e 97% das mortas). A −20% mata 5% das boas e 52% das mortas. Regra mais apertada sempre mata mais das duas, então defina antes de entrar ao vivo.
  3. *Quanto tempo para saber?* 19% das boas parecem piores que uma morta típica após 6 meses; 11% após 1 ano; 1,8% após 3 anos.
  - Limitações declaradas: retornos diários normais, edge e vol constantes, sem custos. Caudas reais são mais gordas e edges decaem. Escale pela sua vol: com 20% de vol, os drawdowns dobram. "Simulação, não backtest."
  - Hashtags: #trading #daytrading #quanttrading #algotrading #backtesting.
- Quadro a quadro:
  - t≈0–6: "10,000 GOOD STRATEGIES · 3 YEARS" [SIMULATED], "+10% A YEAR · SHARPE 1 · A REAL EDGE", grade de quadrados azuis enchendo. Legenda: "10,000 good" / "I simulated".
  - t≈12: "ALL 10,000 · EVERY DAY": **90%** "OF DAYS BELOW ITS OWN HIGH" (vermelho).
  - t≈18: "ONE GOOD STRATEGY · 3 YEARS": **+7%**, "9 MONTHS WITHOUT A NEW HIGH", curva lateral ("Flat isn't [broken]").
  - t≈25: fundo claro, "GOOD STRATEGIES KILLED · 3 YEARS": **64%** "QUITTING AT −10%" (grade 64% vermelha / 36% azul).
  - t≈32: "KILLED IN 3 YEARS · QUIT AT −20%": barras GOOD **5%** vs DEAD **52%**.
  - t≈39: "RESULT AFTER 6 MONTHS": **1 IN 5** "GOOD BUT LOOKS DEAD". Histogramas sobrepostos GOOD (amarelo) × DEAD (vermelho) quase coincidem.
  - t≈45: "RESULT AFTER 3 YEARS": **1.8%**; os histogramas se separam ("in 100").
  - t≈51: resumo "BEFORE YOU TURN IT OFF": 01 HOW LONG IS NORMAL? (90% dos dias abaixo do pico; flat típico 10,7 meses) · 02 HOW DEEP IS NORMAL? (−10% mata 64% das boas; −20%: 5% boas, 52% mortas) · 03 HOW LONG TO TELL? (6 meses: 19%; 3 anos: 1,8%).
  - Rodapé: "NOT FINANCIAL ADVICE · SEED 99".
- Regras/lições práticas:
  - Defina o critério de desligamento (DD máximo) **antes** de entrar ao vivo e calibre pela vol da estratégia.
  - Com Sharpe 1, ficar ~10 meses sem nova máxima é normal; não desligue por "estar lateral".
  - Stop de −10% na equity com vol de 10% mata a maioria das estratégias boas; −20% separa muito melhor.
  - Com 6 meses de histórico não dá para distinguir boa de morta (1 em 5 confunde); só com ~3 anos.
  - Drawdown escala linearmente com a vol (vol 20% ⇒ DD 2×).
- Evidência: **simulação Monte Carlo** com parâmetros e seed explícitos e limitações declaradas. Sem dados reais.

### Dfs5F7ZP3oy — @kwaant
- Link: https://www.instagram.com/p/Dfs5F7ZP3oy/ · 13/11/2026
- Tipo: reel (70 s)
- Tema: estatística (backtest/validação)
- Legenda (resumo): Deflated Sharpe Ratio: seu melhor backtest pode ser só o mais sortudo. Ao testar 200 versões, a melhor parece ótima mesmo sem edge: 200 versões sem edge ainda dão um Sharpe máximo de ~1,66. O DSR vai de 0 a 1 e mede a probabilidade de o melhor vencer a sorte de tudo o que foi tentado; o corte usual é 0,95. Fecha com o CTA do produto (lista de espera grátis) e o aviso "exemplo ilustrativo, não resultado real". Hashtags: #backtesting #tradingstrategy #algotrading #futurestrading #quanttrading.
- Quadro a quadro:
  - t≈0: "SHARPE RATIO – The more settings you test, the less your Sharpe ratio means." Contador VERSIONS TESTED 178→200, BEST SHARPE SO FAR **1.80**, grade de mini-curvas "the more you test, the higher the best".
  - t≈12: "That's return for the risk you took, and 1.8 looks great." Card "EMA 40 · STOP 2 ATR · TARGET 1R · BEST OF 200", Sharpe **1.8**, setas RETURN/RISK, fórmula **SHARPE = RETURN ÷ RISK**.
  - t≈22: "THE REAL BAR – So beating zero isn't enough." Dot plot "200 NO-EDGE VERSIONS" com Sharpe de −2 a 2, centrado em 0 ("THE BAR: 0" riscado), "YOURS 1.8" na cauda direita.
  - t≈32: "DEFLATED SHARPE RATIO – a score from 0 to 1 of how likely your edge beats the luck of everything you tried." Barra 0–1, "EVERYTHING YOU TRIED".
  - t≈45: "This 1.8, from 200 versions, scores **0.61**." SHARPE 1.8 (FROM 200 VERSIONS) → DEFLATE → DSR **0.61**, marcador 0.95, selo "LUCK NOT RULED OUT".
  - t≈53: "WHAT IT MEANS – It means it's probably not luck." "DOESN'T MEAN: ~~It makes money~~ / MEANS: It's probably not luck." SHARPE 1.8 FROM 10 VERSIONS → DSR **0.96**, "ABOVE 0.95".
  - t≈61–68: tela do produto (BEST SHARPE 1.8) e CTA "FREE WAITLIST · LINK IN BIO".
- Regras/lições práticas:
  - O Sharpe do melhor backtest precisa ser descontado pelo **número de versões testadas**: 200 tentativas sem edge já produzem Sharpe ~1,66.
  - Use o **Deflated Sharpe** (Bailey & López de Prado) com corte de 0,95.
  - O mesmo Sharpe 1,8 vale DSR 0,61 com 200 versões e 0,96 com 10: **registre quantas versões você testou**.
  - DSR alto significa "provavelmente não é sorte", **não** "dá dinheiro".
- Evidência: exemplo **ilustrativo** (declarado). O conceito é de literatura conhecida, mas o post não cita o paper. É conteúdo educativo com CTA de produto.

### DfktYl-S6Uz — @kwaant
- Link: https://www.instagram.com/p/DfktYl-S6Uz/ · 10/11/2026
- Tipo: reel (46 s)
- Tema: backtest/validação
- Legenda (resumo): como um profissional testaria sua estratégia. Um backtest com intuição não é teste. O profissional escreve regras exatas, faz o backtest com custos e slippage reais e checa sorte, overfitting, dados não vistos e o tamanho provável dos drawdowns. Toda melhoria precisa se sustentar em dados nunca vistos, senão é descartada. Fecha com o pitch do produto (do inglês para Pine Script), a lista de espera e os avisos legais.
- Quadro a quadro:
  - t≈3: "YOUR STRATEGY – before trusting it." Card "YOUR BACKTEST", selo **UNTESTED**, PROFIT **+154%**, eixo 2010–2022.
  - t≈10: "STEP 1 · RULES – and it becomes exact rules." Exemplo em linguagem natural: "Buy the first pullback to the 20 EMA. Stop 8 points below my entry. Take profit at twice my risk."
  - t≈17: "STEP 2 · BACKTEST – with real costs and slippage." Tags ENTRY 20 EMA · STOP 8 PTS · TARGET 2R. **BEFORE COSTS +184% / AFTER COSTS +121%**, área entre as curvas, 2010–2026, "UP TO 16+ YEARS · YOU CHOOSE THE WINDOW".
  - t≈20: "STEP 3 · TEST – luck, overfitting, unseen data," painéis LUCK CHECK, OVERFITTING, UNSEEN DATA, DRAWDOWN.
  - t≈24: "…and how bad drawdowns are likely to get." "SAME TRADES, RESHUFFLED 1,000 TIMES": BACKTEST DRAWDOWN **−16%** ("the order that happened") vs WORST LIKELY DRAWDOWN **−21%** ("1 in 20 orders is at least this bad"). "+ MORE: Walk-forward test".
  - t≈27: "STEP 4 · IMPROVE – and rejects every one that only fits the past." Seis variações em volta de YOUR STRATEGY: WIDER STOP (marcada "OVERFIT"), TIME EXIT, TIGHTER TARGET, SKIP FIRST HOUR, VOL FILTER, TREND FILTER, cada uma com trecho "UNSEEN".
  - t≈31–34: "STEP 5 · OPTIMIZE – It reruns every test on the improved version, tuned for the live market." BEFORE **+121%** → IMPROVED **+149%**, checks em LUCK / OVERFITTING / UNSEEN DATA / DRAWDOWN, STOP **11 PTS**, TARGET **2.7R**, abas LIVE MARKET / PROP FIRM RULES.
  - t≈38: "WHAT YOU GET – the evidence and Pine Script." TOTAL RETURN **+149%** · MAX DRAWDOWN **−16%** · SHARPE **0.97** · WIN RATE **44%** · PROFIT FACTOR **1.17** · TRADES **2,097**. Mais: Sortino + Calmar, longs vs shorts, o que causou o pior DD, avg win/loss, quebra por horário, "everything it tried", "what was thrown out as luck".
- Regras/lições práticas:
  - Formalize a ideia em regras exatas (entrada, stop, alvo) antes de testar.
  - Inclua **custos e slippage**: no exemplo, o retorno cai de +184% para +121%.
  - Use o DD do **pior 1 em 20** reembaralhamentos (−21%), não o histórico (−16%).
  - Cada melhoria precisa passar em dados **não vistos**; a que só melhora o passado é overfitting.
  - Relate o conjunto completo: Sharpe, PF, win rate, nº de trades e o que foi descartado.
- Evidência: **ilustrativo** (declarado) e demonstração do próprio produto. Sem dados reais nem fonte.

### DfVf0L-AIkP — @tradionquant
- Link: https://www.instagram.com/p/DfVf0L-AIkP/ · 04/11/2026
- Tipo: reel (58 s)
- Tema: estatística (expectativa vs. taxa de acerto)
- Legenda (resumo): no teste, 9.999 de 10.000 traders desenhados para acertar 90% dos trades perderam dinheiro. Foram 10.000 traders simulados por lado em preço tipo cara-ou-coroa: 500 trades cada, US$ 10.000 iniciais, taxa de 5% do valor arriscado por trade. Um lado acerta 90% (ganhos minúsculos, perda do tamanho de nove ganhos). O outro acerta 35% (ganho quase 2× a perda). Antes das taxas, os dois têm média de US$ 0 por trade: a taxa de acerto só reflete onde fica o alvo. Depois das taxas, ambos perdem ~US$ 5 por trade no início. 9.999 dos "90%" terminaram no prejuízo; 1.641 dos "35%" terminaram no lucro, por variância e sorte. Pergunta-chave: depois dos custos, seu trade médio dá lucro? Fonte declarada: simulação própria.
- Quadro a quadro:
  - t≈2: "wins 90%" × "wins 35%": linhas "target = win" (verde) e "stop = loss" (vermelho) a distâncias diferentes do preço; "price moves like a coin flip". Texto: "Two simulated traders."
  - t≈10: "trade 4", "account: start $10,000", trajetórias das duas contas ("it runs.").
  - t≈18: "wins 90% – each dot = 1 trader", grade de 10.000 pontos.
  - t≈26: "**9,999 of 10,000** lost money" (grade vermelha; "1 got lucky"). "wins 35% – bigger swings": **8,359 lost money / 1,641 got lucky** (faixa verde).
  - t≈30: "before fees": os dois riscados, "**$0 a trade, on average**".
  - t≈34: "after fees": barras, "**−$5 a trade, on average**".
  - t≈42: "wins 90%" com target perto e stop longe ("win rate").
  - t≈50: "the real test: average trade, after fees:".
  - t≈57: "Follow for more @tradionquant".
- Regras/lições práticas:
  - Taxa de acerto é consequência da posição do alvo e do stop; sozinha não indica edge.
  - Métrica de decisão: **expectativa (trade médio) líquida de custos**.
  - Estratégias de payoff assimétrico (35%) têm mais variância: alguns ganham por sorte (16%), o que pode enganar no backtest.
  - Custos fixos por trade transformam expectativa zero em perda quase certa com muitos trades.
- Evidência: **simulação própria** com parâmetros explícitos (N, trades, capital, custo). Sem dados de mercado.

### DfjCMULExt_ — @tradionquant
- Link: https://www.instagram.com/p/DfjCMULExt_/ · 10/11/2026
- Tipo: reel (66 s)
- Tema: backtest/validação (dados históricos reais)
- Legenda (resumo): esperar a queda ou comprar já? Testado em 100 anos de ações americanas ("Dia 2 de testar 100 regras de trading"). Método: mercado acionário dos EUA com dividendos reinvestidos (Ken French Data Library / CRSP, diário, 1926–2026). Duas contas de US$ 10.000: uma compra no 1º dia; a outra fica em T-bills rendendo juros até o mercado fechar 10% abaixo da máxima histórica, e então compra e segura. Custo de 0,10% por compra, impostos ignorados. Uma nova corrida começa a cada fim de mês de 1926 a 2016 (1.084 inícios), avaliada 10 anos depois. "História, não previsão."
- Quadro a quadro:
  - t≈2–4: dois gatos sobre pilhas de US$ 10.000: "stocks" (verde, compra já) vs "cash" (azul, espera). Texto: "right away."
  - t≈13: "OCT 2006", "record high (2000)", linha tracejada "his sale price: 10% below the high", "+ cash paid out" ("they pay out.").
  - t≈26: "JAN 2008 – 15 months → JAN 2008", "record high", o gato da espera "WAITING FOR A SALE" com **+$602 interest**.
  - t≈38: "JAN 2008" – os dois agora em ações ("isn't the bottom.").
  - t≈50: "10-year races, start dates 1926 → 1977": mosaico azul (esperar ganhou) × verde (comprar já ganhou), "our cats' start month: OCT 2006".
  - t≈58: "**1,084 starts**, start dates 1926 → 2016": waffle chart, verde maior × azul **47.1%**, "2 ties".
  - t≈62: "OCT 2006 → SEP 2026 · 20 years": compra já **$84,606** × espera **$82,966** ("Waiting for the [dip]…").
- Regras/lições práticas:
  - Esperar 10% de queda a partir da máxima venceu comprar já em só **47,1%** das 1.084 janelas de 10 anos: pouco melhor que uma moeda e pior na média.
  - Os juros do caixa (T-bills) entram no teste; sem eles o resultado da espera seria pior.
  - No exemplo de out/2006 (20 anos), a espera ficou ~US$ 1,6 mil atrás, mesmo comprando antes da crise de 2008.
  - Bom desenho de teste: janelas móveis mensais, horizonte fixo, custos, fonte de dados nomeada.
- Evidência: **dados reais**, Ken French Data Library / CRSP, 1926–2026, com metodologia completa na legenda.

---

## Prints

Arquivos na pasta `prints/` (recortes do quadro do vídeo).

| Arquivo | Link direto | O que mostra / por que importa |
|---|---|---|
| DfuDLH7BUsx_1.png | https://www.instagram.com/p/DfuDLH7BUsx/ (t=16s) | Monte Carlo: histograma do DD + código; 5,9% vs 14,0% (2,4×). O núcleo numérico do post |
| DfuDLH7BUsx_2.png | https://www.instagram.com/p/DfuDLH7BUsx/ (t=26s) | Walk-forward: janelas Optimize/Test, código, 5 janelas, IS +32%/ano com OOS negativo |
| DfuDLH7BUsx_3.png | https://www.instagram.com/p/DfuDLH7BUsx/ (t=36s) | Heatmap de sensibilidade + grade "Plateau" de PF; visual de platô vs. pico |
| Dfj-RfohT0S_1.png | https://www.instagram.com/p/Dfj-RfohT0S/ (t=25s) | Waffle 64% das estratégias boas mortas com stop de −10%; paleta clara/escura |
| Dfj-RfohT0S_2.png | https://www.instagram.com/p/Dfj-RfohT0S/ (t=39s) | Histogramas boas × mortas após 6 meses ("1 in 5"); mostra a sobreposição |
| Dfj-RfohT0S_3.png | https://www.instagram.com/p/Dfj-RfohT0S/ (t=51s) | Cartão-resumo com as 3 perguntas e todos os números; bom modelo de slide final |
| Dfs5F7ZP3oy_1.png | https://www.instagram.com/p/Dfs5F7ZP3oy/ (t=22s) | Dot plot de 200 versões sem edge vs. "yours 1.8"; ilustra viés de seleção |
| Dfs5F7ZP3oy_2.png | https://www.instagram.com/p/Dfs5F7ZP3oy/ (t=45s) | Sharpe 1.8 → DSR 0.61, "luck not ruled out"; antes/depois |
| Dfs5F7ZP3oy_3.png | https://www.instagram.com/p/Dfs5F7ZP3oy/ (t=53s) | "Doesn't mean it makes money / means probably not luck"; DSR 0.96 com 10 versões |
| DfktYl-S6Uz_1.png | https://www.instagram.com/p/DfktYl-S6Uz/ (t=17s) | Antes/depois de custos (+184% → +121%) |
| DfktYl-S6Uz_2.png | https://www.instagram.com/p/DfktYl-S6Uz/ (t=24s) | 1.000 reembaralhamentos: DD −16% vs pior provável −21% |
| DfktYl-S6Uz_3.png | https://www.instagram.com/p/DfktYl-S6Uz/ (t=27.5s) | Árvore de 6 variações com trecho "unseen"; layout de rejeição por overfit |
| DfVf0L-AIkP_1.png | https://www.instagram.com/p/DfVf0L-AIkP/ (t=2s) | Os dois traders: alvo/stop a distâncias diferentes; layout minimalista |
| DfVf0L-AIkP_2.png | https://www.instagram.com/p/DfVf0L-AIkP/ (t=26s) | Grades de 10.000 pontos: 9.999 perdem (90%) vs 1.641 lucram (35%) |
| DfVf0L-AIkP_3.png | https://www.instagram.com/p/DfVf0L-AIkP/ (t=34s) | Após taxas: −US$ 5 por trade em média; a lição central |
| DfjCMULExt__1.png | https://www.instagram.com/p/DfjCMULExt_/ (t=26s) | Gráfico jan/2008 com linha "−10% da máxima" e +US$ 602 de juros; storytelling com dados |
| DfjCMULExt__2.png | https://www.instagram.com/p/DfjCMULExt_/ (t=58s) | Waffle de 1.084 inícios: esperar ganhou 47,1% |
| DfjCMULExt__3.png | https://www.instagram.com/p/DfjCMULExt_/ (t=62s) | Resultado de 20 anos: US$ 84.606 vs US$ 82.966 |
