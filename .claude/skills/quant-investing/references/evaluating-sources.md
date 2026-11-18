# Como avaliar posts e influenciadores financeiros

Destilado das rodadas 4A/4B (Instagram, 16 perfis): @tradionquant, @rational_edge, @kwaant, @guiainvest, @econoweek, @boletinhos, @humphreytalks, @brianferoldi, @academiadevalor e outros. Ranking dos perfis: `sources-ranking.md`. Itens "(complemento)" são conhecimento geral.

> Conteúdo educacional, não recomendação de investimento. Avalie o **método** do post; não endosse nem repita recomendações de ativos.

## Filtro nº 1: a premissa está escrita?
Os perfis mais rigorosos põem **na legenda** universo, período, fonte, custos e limitações. Sem premissa = nota baixa, por mais bonito que seja o gráfico.

## Checklist (use na ordem; cada "não" derruba a confiança)

| # | Pergunta | Exemplo bom | Sinal de alerta |
|---|---|---|---|
| 1 | **Fonte dos dados** nomeada? | Ken French/CRSP diário 1926–2026; Yahoo retorno total | "Estudos mostram", print de tweet, dado sem link |
| 2 | **Período e amostra**: quantos eventos/janelas? | 1.084 janelas de 10 anos; 25 eleições | Um gráfico de 10 anos de alta; um exemplo escolhido |
| 3 | **Benchmark** investível? | vs SPY / comprar já / buy and hold | vs zero, vs poupança, sem comparação |
| 4 | **Custos** (taxas, spread, slippage)? | 0,10% por compra; líquido de taxas do fundo | "Sem custos" ou silêncio |
| 5 | **Caixa remunerado** quando a regra espera? | T-bills / CDI | Caixa rende zero (favorece o "comprar já" artificialmente ou esconde custo de oportunidade) |
| 6 | **Impostos**? | Declara "impostos ignorados" ou modela IR | Rebalanceamento/giro sem IR |
| 7 | **Inflação / real vs nominal**? | "valores nominais, sem descontar inflação" (declarado) | 15% a.a. bruto, nominal, 20 anos, sem aviso |
| 8 | **Moeda** de medida coerente? | Mede patrimônio em BRL **e** USD | Compara juro **real** de um país com **nominal** de outro |
| 9 | **Nº de testes / versões**? | "venceu X de N"; placar "0 de 2" | Mostra só o vencedor (viés de seleção, ver `backtest-pitfalls.md` §3) |
| 10 | **Robustez** (data de início, parâmetros)? | "qualquer data de 1/09 a 15/10 não muda" | Um único parâmetro/data |
| 11 | **Ceticismo explícito**? | "ou sorte?", "história, não previsão", limitações listadas | Certeza, "sempre", "garantido" |
| 12 | **Reprodutível**? Dá para refazer a conta? | Taxa, prazo, aporte e capitalização declarados | Resultado final sem premissas (patrimônio inicial, aportes) |
| 13 | **Consistência interna** entre slides/legenda? | Números batem | Faixas de preço diferentes em slides vizinhos; legenda ≠ card |
| 14 | **Conflito de interesse / CTA**? | Declara publi; CTA não muda o conteúdo | "Comente X", funil para consultoria/curso/ferramenta, publi de corretora no mesmo vídeo que cita hack dela |
| 15 | **Simulação ou backtest?** declarado? | "SIMULATED", "seed 99", "ilustrativo" | Simulação apresentada como resultado real |

Pontuação sugerida (complemento): 5 = passa em 1–5, 9–12 e declara limitações; 4 = método bom mas ilustrativo/produto; 3 = dados reais mas sem premissas ou com CTA forte; 2 = aritmética certa com premissas otimistas; 1 = opinião sem fonte.

## Premissas mínimas de uma simulação de patrimônio
Para aceitar (ou refazer) uma projeção, exija: capital inicial; aporte (valor, frequência, **início ou fim do período**); taxa (bruta/líquida, **nominal/real**) e capitalização (mensal = (1+a)^(1/12)−1); prazo; IR e custos; inflação; fonte da taxa; para backtest histórico, fonte dos índices e se incluem dividendos.

## Erros reais achados (refaça a conta sempre)
| Post | O que dizia | Conferência |
|---|---|---|
| @boletinhos `DV8keeQjlW0` | R$ 200/mês, 15% a.a., 5 anos: aportado R$ 12.200, acumulado R$ 17.266,14 | Acumulado ✓ (taxa mensal 1,1715%, aporte no fim). Aportado é **R$ 12.000** (60×200). Mês 1 usa aporte no início, os demais no fim: convenções misturadas. 15% bruto, sem IR/inflação |
| @econoweek `Df1c5Bjvc_l` | R$ 564 mil vs R$ 2,68 mi em 30 anos (6,8% líquido, nominal) | ✓ bate (R$ 563.612 vs R$ 2.684.486); declara ser nominal |
| @guiainvest `DfpIvG7oM8u` | R$ 1 mi a 5% real: +630 mil / +1 mi / +1,67 mi por década | ✓ (R$ 628.895 / 1.024.403 / 1.668.645) |
| @guiainvest `Dfj6KNVIPj8` | R$ 20,5 mi vs R$ 18,3 mi = "mais de R$ 2,1 mi" | Diferença é **R$ 2,2 mi**; patrimônio inicial, aportes e fontes não divulgados; "quase 32" vs "31 anos"; cards do slide 2 com números sem relação ao texto |
| @guiainvest `Dft8PmnDd1t` | CDI +14% vs dólar de R$ 4,99 → R$ 5,65 | Em USD: 1,14 / (5,65/4,99) − 1 ≈ **+0,7%** (a rodada 4A anotou +0,9%, que só vale com dólar +13% exato). Compara juro real BR (~9%) com nominal EUA (~5%) |
| @humphreytalks `DfaR1gzBFD-` | Barista FIRE: US$ 1.000/mês fecha a lacuna | Lacuna = 50.000 − 24.000 = US$ 26.000/ano ≈ **US$ 2.167/mês**. Regra dos 4% sem fonte nem risco de sequência; mistura 8% (retorno) e 4% (saque) |
| @brianferoldi (scorecards) | notas 1–5 e faixas de preço | Faixas diferentes em slides vizinhos; nota da legenda ≠ card; EPS −1.137,9% com margem líquida 67% (artefato de base negativa) |
| @academiadevalor `DfVllE2AeAa` | S&P 500 subindo 10 anos: "nunca espere a máxima" | Viés de seleção de período, sem dividendos nem câmbio; não testa DCA vs aporte único (o teste de verdade é o de @tradionquant, `validation-tests.md` §5) |
| @neuron.machinelearning `DfowdSMiPzc` | GARCH + ML "9% melhor que GARCH"; 53% vs 53,5%, p = 0,78 | Erro 0,477 → 0,453 = **5,0%** sobre o GARCH; 9,4% é vs naive (0,500). p = 0,780 ✓ (436/823); vs moeda p ≈ 0,09. "20 stocks" no slide vs 12–14 no código |
| @tradionquant / @rational_edge | vários | Números conferidos batem (ex.: midterms 19+6=25; NANC +589/GOP −2.235; simulação de drawdown reproduzida em Python) |

## Ideias aproveitáveis mesmo de fontes medianas
- **Rebalancear pelo aporte** (@guiainvest `Dfj6KNVIPj8`): (1) escreva o peso-alvo; (2) direcione aportes e dividendos à classe **abaixo do alvo**; (3) venda só em desvio extremo. Evita IR antecipado e corretagem e gera compra anticíclica automática (ex.: 93% dos aportes de 2003–2011 foram ao S&P 500 com dólar médio R$ 1,99). O resultado numérico do post não é reproduzível (premissas ausentes); a regra é que vale. (complemento) Teste-a você: simule a carteira 1/3 Ibovespa, 1/3 CDI, 1/3 S&P em BRL com aporte fixo, comparando aporte neutro, aporte dirigido e rebalanceamento com venda + 15% de IR sobre o ganho.
- **Meça o patrimônio em duas moedas** (hoje, há 1 e há 5 anos): retorno em BRL pode ser ~zero em USD.
- **Indexe o aporte à renda** (metade de cada aumento): efeito 2x em 10 anos e 4,8x em 30 (nominal, Econoweek).
- **Viés do crescimento exponencial** (Stango & Zinman, Journal of Finance 2009, citado sem autores pelo post): projete com fórmula, não intuição linear.
- **Avalie oferta de emprego pelo líquido** (descontos de 22,5% no exemplo de R$ 5.000 → R$ 3.877, soma confere).

## Como o Claude usa isto
- Usuário traz um post/print/reel: passe o checklist, refaça as contas em Python, liste premissas faltantes e conflitos de interesse, e dê uma nota 1–5 com justificativa.
- Separe **método** (aproveitável) de **recomendação** (não repetir). Nunca opine sobre a ação/ativo do post.
