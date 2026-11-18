# Ranking de fontes (Instagram) para aprender quant

Avaliação feita em 16–18/11/2026 (rodadas 3A, 4A, 4B; rodadas 2 e 5 só pelos posts citados, sem seguidores coletados), só leitura. Seguidores e status são da data da coleta. Nota de rigor 1–5 pelo checklist de `evaluating-sources.md`. "Bio" = nota dada só pela bio e 1–2 legendas, sem análise de slides.

> Conteúdo educacional. Ranking do **método** dos perfis, não endosso de produtos nem de recomendações.

## Perfis avaliados

| Handle | Ativo? | Seguidores | Tipo | Vende algo? | Rigor | O que aproveitar |
|---|---|---|---|---|---|---|
| @rational_edge | sim (14/11/2026) | ~8,1 mil | pesquisa quant sistemática; simulações com código Python | guia grátis por comentário ("TEST"); sem sinal | **5** | 3 testes de robustez (`validation-tests.md` §1–3), drawdown normal e regra de desligamento (§4), custos de execução e toolkit de bibliotecas (`backtest-pitfalls.md`). Sempre declara "simulated", seed e limitações |
| @tradionquant | sim (18/11/2026) | ~2,0 mil | testa regras populares ("100 regras") com dados reais (Ken French/CRSP, Yahoo, Cboe) | isca de lead ("DESK"), site; sem sinal | **5** | Falácia do win rate, "venceu X de N" com caixa remunerado e custo, placar de regras, projetos de portfólio (`win-rate-fallacy.md`, `validation-tests.md` §5, `quant-portfolio-projects.md`) |
| @kwaant | sim (17/11/2026) | ~1,1 mil | educação em validação; demo do próprio software | **sim**: software de backtest (lista de espera) | **4** | Deflated Sharpe e nº de versões; pipeline regras→custos→testes→melhoria em dados não vistos; DD p95 (1 em 20) (`backtest-pitfalls.md` §3–4) |
| @neuron.machinelearning | n/d | n/d | 5 projetos ML + estatística em dados reais, com código e placar ✓/✕ (`DfowdSMiPzc`) | **sim**: livro *Machine Learning from First Principles*; scripts por comentário ("QUANT") | **4** | Baseline ingênua (53% vs "sempre sobe" 53,5%, p = 0,78, conferido) e 91 pares → 4,55 falsos positivos (`backtest-pitfalls.md` §3, §5). Desconto: legenda diz "9% melhor que GARCH" (é 5%; 9,4% é vs naive), "20 stocks" vs 12–14 no código, dados até 2018 |
| @quantfinancetogo | sim | ~73 mil | conceitos de quant de A a Z com código | não declarado ("no financial advice") | 4 (bio) | candidato para próxima rodada |
| @quantpapers | sim (13/10/2026) | ~80 mil | resumos de papers (11 posts) | não visto | 4 (bio) | candidato para próxima rodada |
| @quant_research_decoded | quase inativo (16/06/2026) | ~44 mil | pesquisador explicando modelos institucionais | não visto | 4 (bio) | candidato, perto do limite de 6 meses |
| @fidetolabs.math | sim | ~3,0 mil | "math for quant": CUSUM, amostragem de eventos (linha López de Prado) | não visto | 4 (bio) | candidato para próxima rodada |
| @quantfinance.ai | n/d | n/d | infográficos quant (perfil marcado "AI content") | não visto; CTAs de engajamento | **3** | Toolkit de pairs (Engle-Granger, OU/half-life, Kalman, z-score) com código e disclaimers honestos (simulado, 1 caminho, sem custos); grade de 15 conceitos como roteiro de estudo (`quant-portfolio-projects.md`) |
| @fidetolabs | sim | ~18 mil | ferramentas de dados quant | comunidade (paga?) | 3 (bio) | — |
| @datainterview | sim | ~5,1 mil | preparo para entrevistas quant/DS | provável curso | 3 (bio) | exemplos numéricos de estratégias (Bollinger) |
| @quantwright | sim | 171 | agente de pesquisa de backtest | **sim**: produto | 3 (bio) | discurso "sem se enganar"; marketing |
| @brianferoldi | sim (vários/dia) | 310 mil | análise fundamentalista em scorecards | **sim**: livro, cursos, ferramenta; CTA "comente STOCK" | 3 | Formato de scorecard (fase + 7 fatores, trailing vs forward) para stock pitch; notas subjetivas e inconsistências (`quant-portfolio-projects.md`) |
| @guiainvest | sim (quase diário) | 443 mil | consultoria CVM; alocação, dolarização | **sim**: consultoria ("Diagnóstico Patrimonial Gratuito") | 3 | Rebalancear pelo aporte; medir patrimônio em duas moedas; premissas não divulgadas (`evaluating-sources.md`) |
| @artillerytrades | n/d | n/d | curadoria de ferramentas ("uma ferramenta grátis por dia") | CTA "comente QUANT" + Discord "onde meus bots postam cada trade"; sem produto pago visível | **2** | Lista de 5 repos (qlib, FinRL, ML4T, vectorbt, quantstats) com licença e data das estrelas (`backtest-pitfalls.md` §1). Headline de hype ("hedge fund quants build with these") |
| @daytrading | n/d | n/d | mídia de notícias/educação de trading | não visto ("follow for daily updates") | **2** | Lista de 7 ideias de estratégia para backtestar; legenda cita custos/slippage/overfitting, mas nenhum teste próprio e o gráfico de resultado mostra a estratégia abaixo do S&P |
| @econoweek | sim | 254 mil | finanças pessoais, opinião | publis (ex.: corretora de cripto) | 2 | Simulação de aporte indexado à renda, reproduzível e com premissas |
| @humphreytalks | sim | 907 mil | finanças pessoais EUA (FIRE, 401(k)) | downloads, conta remunerada, publis | 2 | Aritmética da regra dos 4% / Coast e Barista FIRE (com conta que não fecha) |
| @boletinhos | quase inativo (19/06/2026) | ~60 mil | finanças pessoais geração Z, memes | publis (contabilidade, crédito) | 2 | Holerite líquido; juros compostos com erro de total aportado |
| @academiadevalor | sim | 119 mil | opinião/política em prints de tweets | captação, viagens com milhas | 1 | Quase nada; exemplo de viés de seleção de período |

## Descartados / não avaliados (resumo)
- **Vendem estratégia/sinal ou resultados:** quantifiedstrategies (destaque "Testimonials"), bayesiansystems (prop firm, destaque "Results"), quantscience_ (curso).
- **Hype / "comente X":** arwazaz_, seb.ai ("AI & Income").
- **Trading discricionário de varejo / sinais:** ayaantrades, atraintrades, iclosegreen, orderflowschool, wallstbets, orochitrading, nuranatrades, vagafx, trdr_john, confluencetrading e similares.
- **Cedo demais:** whyitworks.maths (3 posts, 13 seguidores).
- **#tradingsistematico:** quase tudo varejo e robôs à venda; nenhum candidato.
- **Instituições** (imctrading, citadelsecurities, hudsonrivertrading, J.P. Morgan, KKR, iShares...): institucional/recrutamento, não analisadas.
- **Só apareceram em hashtags, sem avaliação:** quantstackai, algocourt, quantnative, atsmatrix, entre outros.

## Top 3
1. **@rational_edge**: simulações com premissas, seed, código e limitações; números reproduzidos em Python.
2. **@tradionquant**: dados reais com fonte, todas as janelas, custo e caixa remunerado, ceticismo explícito.
3. **@kwaant**: Deflated Sharpe e pipeline de validação claros (descontar o CTA de produto).

Menção honrosa: **@neuron.machinelearning** (dados reais, código e fracassos mostrados; conferir os números da legenda).

