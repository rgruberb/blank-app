# Rodada 4A — Perfis de investimento e quant no Instagram

_Leitura feita em 18/11/2026, sem curtir, comentar nem seguir ninguém. Critério de escolha dos posts: utilidade para quem quer validar estratégias com dados._

> **Sobre as legendas e os textos dos slides:** nesta rodada, as legendas e as frases longas dos slides estão em **resumo fiel em português**, não copiadas palavra por palavra (direitos autorais dos autores). Números, rótulos de gráficos, tabelas e fórmulas foram transcritos integralmente.
>
> **Transparência:** sou o Claude, feito pela Anthropic. Um dos posts analisados (@brianferoldi, Df2T4p4NCHR) avalia uma ação "Anthropic", e um dos posts listados do @humphreytalks é publicidade do Claude. Descrevi os dois sem juízo de valor.

## Resumo da rodada

- **@tradionquant é, de longe, a melhor fonte quantitativa da rodada.** Todo post traz período, fonte dos dados (Ken French/CRSP, Yahoo Finance, Cboe), custos, regra de entrada e número de amostras. Também mostra a taxa de acerto, não só um exemplo.
- **Lição central do @tradionquant:** regras populares de timing perderam para "comprar e segurar". "Comprar na queda de 10%" ganhou só em 47,1% de 1.084 janelas de 10 anos. Esperar as eleições de meio de mandato perdeu em 19 de 25. Copiar o ETF dos Republicanos no Congresso (GOP) perdeu US$ 2.235 contra o SPY. O ETF dos Democratas (NANC) ganhou só US$ 589 em 3,7 anos, e a própria conta pergunta se foi sorte.
- **Método reutilizável:** compare a regra com um benchmark simples, com várias datas de início (não uma só), custo e caixa remunerado. Reporte "venceu X de N vezes" e a diferença média, não um único caso.
- **@brianferoldi:** ensina análise fundamentalista com scorecards bem estruturados (margens, P/L futuro, faixas de preço). As notas são subjetivas, o post é funil para a ferramenta dele (Stock Simplifier) e há inconsistências entre slides. Não há backtest das notas.
- **@guiainvest:** é o único brasileiro com simulação longa (31–32 anos, carteira 1/3 Ibovespa, 1/3 CDI, 1/3 S&P 500). A ideia de rebalancear pelo aporte, sem vender, é boa. Mas a premissa não é divulgada (patrimônio inicial, aportes, fonte), e um slide traz números que não fazem sentido. O conteúdo é funil para consultoria.
- **@econoweek e @boletinhos:** fazem simulações de juros compostos que eu reproduzi (as do Econoweek batem exatamente). Há erros pequenos no Boletinhos (R$ 12.200 em vez de R$ 12.000) e premissas otimistas: 15% a.a. bruto, sem IR nem inflação.
- **@humphreytalks:** finanças pessoais com aritmética simples (regra dos 4%, Barista/Coast FIRE). É claro, mas não testa a regra dos 4% nem mostra fonte.
- **@academiadevalor:** quase todo o conteúdo é opinião e política em prints de tweets. Os poucos dados vêm sem link para a fonte.
- **Regra geral da rodada:** desconfie de simulação sem premissas escritas. Exija período, fonte, custos, impostos, inflação e número de testes.

---

## 1. @tradionquant

- **Status:** ativo · 1.979 seguidores · 9 posts · último post em 18/11/2026.
- **Perfil:** "matemática por trás do trading". Reels curtos (55–85 s) com animação em fundo escuro ou desenhos de gatos, que testam regras populares ("100 regras"). Mostra dados, metodologia e fonte em toda legenda, e sempre diz que é história, não previsão. Não vende sinal. Há isca de lead ("comente DESK") e um site (tradionlabs.com).

### Posts mais recentes ainda não analisados

O perfil só tem 9 posts. Excluídos os 3 já analisados (DfVf0L-AIkP, DfoRErMChB-, DftZ6l2CC_e), restam 6:

| # | Link | Tipo | Resumo | Tema |
|---|---|---|---|---|
| 1 | https://www.instagram.com/reel/Df3vKx3je7o/ | reel (74 s) | 3 modelos financeiros para iniciantes com balanços reais (Netflix, LBO da Deckers, Capital One + Discover) | carreira / valuation |
| 2 | https://www.instagram.com/reel/Df1IZS-CY_8/ | reel (78 s) | 3 projetos quant com dados gratuitos (earnings, opções do SPY, S&P desde 1988) | carreira / estatística |
| 3 | https://www.instagram.com/reel/DfjCMULExt_/ | reel (66 s) | "Comprar na queda" vs comprar já: 1.084 janelas de 10 anos | backtest/validação |
| 4 | https://www.instagram.com/reel/DfdO2jkgZ-f/ | reel (85 s) | Copiar trades do Congresso (NANC, GOP) vs SPY | backtest/validação |
| 5 | https://www.instagram.com/reel/DfV5v9TFUhf/ | reel (60 s) | Esperar as midterms para investir: 25 eleições, 1926–2022 | backtest/validação |
| 6 | https://www.instagram.com/reel/De5DhqJyLBO/ | reel (55 s) | Aumentar a aposta depois de um dia vermelho (martingale) | risco e drawdown |

### DfV5v9TFUhf — @tradionquant
- Tipo: reel (59,7 s; frames verificados a cada ~6 s até o fim, sem áudio)
- Tema: backtest/validação
- Legenda (resumo fiel): esperar as midterms passarem parece seguro, mas em 19 de 25 eleições (1926–2022) deixou o investidor com menos dinheiro um ano depois. O teste compara dois investidores com US$ 10.000: um compra no fim de setembro, o outro deixa o caixa em T-bills e compra na véspera da eleição; ambos são avaliados um ano após o voto. A bolsa subiu no ano seguinte ao voto 23 de 25 vezes, mas os dois estavam comprados nesse ano; a diferença está só nas ~6 semanas anteriores, quando a bolsa costuma subir. Em média, cada semana em caixa custou cerca de US$ 13 a cada US$ 10.000 (ações vs T-bills, 1926–2026). Em 2026, o S&P 500 caiu 2,9% entre 22/09 e a véspera do voto (US$ 10.000 viraram US$ 9.712), então esperar compensou: foi a 7ª vez em 26. Trocar a data de início para qualquer dia entre 1/09 e 15/10 não muda a conclusão. Metodologia: mercado americano inteiro com dividendos (dados diários de Ken French) vs T-bills de 1 mês; compra no fechamento de 22/09 (ou dia útil seguinte) vs último fechamento antes da eleição; 2026 usa o preço do S&P 500 (Cboe). Aviso de conteúdo educativo.
- Frame a frame:
  - 0–7 s: título sobre esperar as midterms ter "dado errado"; gráfico de 2026 com linha "Waited in cash" e "Bought in Sept $9,712"; eixo de fim de set/2026 até o voto; "$10,000 each".
  - 13 s: "We tested it: 25 midterms", com barra de 25 colunas de 1926 a 2026 (a de 2026 em destaque).
  - 19 s: "Who had more a year later?" — "Waited in cash: six times" (hachurado) vs "Bought in Sept: 19 times" (bege).
  - 25 s: "The year after the vote" — "Stocks up: 23 of 25 times", "Stocks down: two times" (vermelho).
  - 31 s: "The 2022 midterm, up close": régua fim de set → voto → um ano depois; pilhas de moedas "Bought in Sept" vs "Waited in cash".
  - 37 s: "Before the vote" — "Stocks up: 19 of 25 times", "Stocks down: the same six times".
  - 43 s: "Your cost of waiting": fileira de semanas ("one week"), cada uma com custo.
  - 49 s: volta ao gráfico de 2026 ("But in 2026,").
  - 54–59 s: "Waiting paid" **seven of 26 midterms**, com 7 colunas verdes; termina com a pergunta "or lucky?".
- Regras/lições práticas:
  - Teste a regra contra a alternativa simples (comprar já), com caixa remunerado (T-bills), não com caixa a zero.
  - Isole a janela que realmente difere entre as estratégias (as 6 semanas antes do voto), não o ano inteiro.
  - Reporte a frequência ("6 de 25") **e** o custo médio por unidade de tempo (≈ US$ 13 por semana a cada US$ 10 mil).
  - Faça teste de robustez da data de início (qualquer dia de 1/09 a 15/10).
  - Um acerto recente (2026) não valida a regra: pergunte "foi sorte?".
- Evidência: sim. Dados diários de Ken French (mercado dos EUA com dividendos) e T-bills de 1 mês, 1926–2026; S&P 500 (Cboe) para 2026. Amostra pequena (25 eventos), o que o próprio post reconhece.

### DfjCMULExt_ — @tradionquant
- Tipo: reel (65,9 s; frames a cada ~6 s até o fim)
- Tema: backtest/validação
- Legenda (resumo fiel): é melhor esperar uma queda ou comprar logo? Teste com 100 anos de preços reais dos EUA ("dia 2 de 100 regras"). Dados: mercado americano com dividendos reinvestidos (Ken French Data Library / CRSP, diário, 1926–2026). Duas contas de US$ 10.000: uma compra no 1º dia; a outra deixa o caixa em T-bills até o mercado fechar 10% abaixo da máxima histórica, aí compra e segura. Custo de 0,10% por compra, impostos ignorados. Uma nova corrida começa em todo fim de mês de 1926 a 2016 (1.084 inícios), e cada uma é avaliada 10 anos depois. Aviso de que é história, não previsão.
- Frame a frame:
  - 2 s: "Testing 100 trading rules – Day 2 · Buy the dip, explained with cats"; dois gatos com US$ 10.000 cada (um em ações, outro em caixa).
  - 8 s: máxima histórica (2000) e linha "his sale price: 10% below the high".
  - 14 s: OCT 2006 — um gato compra já; o outro espera, com "$10,000 cash".
  - 20 s: AUG 2007 — a bolsa quase toca o preço-alvo e o gato "just missed his price".
  - 26 s: JAN 2008, 15 meses depois: o gato que espera tem "+$602 interest".
  - 32–38 s: JAN 2008 — o gato compra; a pergunta é se ganhou, e a resposta é "No… isn't the bottom".
  - 44 s: gato "Waiting for a sale" ("Is your cash…").
  - 50–57 s: grade de 1.084 inícios (1926 → 2016) colorida por vencedor; o início dos gatos (OCT 2006) aparece destacado.
  - 60 s: a grade reordenada mostra **47,1%** de vitórias para "esperar a queda", com "2 ties".
  - 64 s: placar "Rules that beat holding: **0 of 2**" (regra 1 = alta taxa de acerto ✗; regra 2 = buy the dip ✗). Exemplo OCT 2006 → SEP 2026 (20 anos): **US$ 84.606** (comprar já) vs **US$ 82.966** (esperar), ou US$ 1.640 atrás.
- Regras/lições práticas:
  - Regra de entrada precisa ser objetiva (−10% da máxima) e testada em **todas** as datas de início possíveis, não num exemplo escolhido.
  - Remunere o caixa parado (T-bills) e inclua custo de transação (0,10%).
  - "Esperar a queda" perdeu na maioria das janelas (ganhou 47,1%) porque a queda pode não vir e a bolsa sobe enquanto você espera.
  - Leve um placar de regras testadas (0 de 2 venceram o buy-and-hold).
- Evidência: sim. Ken French / CRSP diário, 1926–2026, 1.084 janelas. Observação: o exemplo dos gatos usa 20 anos, enquanto o teste agregado usa 10 anos. Não é erro, mas são horizontes diferentes.

### DfdO2jkgZ-f — @tradionquant
- Tipo: reel (84,6 s; frames a cada ~7 s até o fim)
- Tema: backtest/validação
- Legenda (resumo fiel): copiar os trades que os congressistas reportam bate um fundo simples de S&P 500? US$ 10.000 em cada um: NANC (copia os Democratas), GOP (copia os Republicanos; lançado como KRUZ) e SPY. Os membros podem reportar até 45 dias depois, então os fundos operam com base nos relatórios, não nas contas reais. Período: de 07/02/2023 (1º pregão dos dois fundos) ao fechamento de 05/11/2026. Preços do Yahoo Finance com dividendos reinvestidos, depois das taxas de cada fundo; sem impostos nem custos de negociação.
- Frame a frame:
  - 3 s: capa com o Capitólio e três bonecos (Copies Democrats / Buys the market / Copies Republicans).
  - 10–24 s: 7 Feb 2023: Subversive NANC, SPDR SPY e Subversive GOP, US$ 10.000 cada.
  - 31 s: documento carimbado "reported up to 45 days late" / "up to 45 days".
  - 38–45 s: a corrida; em 2025, NANC **US$ 18.158**, SPY **US$ 17.086**, GOP **US$ 14.763**, com mini gráfico das três linhas.
  - 52 s: NANC chega a ficar **US$ 1.072** à frente do mercado.
  - 59–66 s: 2026 — "lead shrinking"; GOP em US$ 16.274.
  - 73–84 s: placar em 5 Nov 2026: NANC **US$ 19.098** (+US$ 589 vs mercado), SPY **US$ 18.509**, GOP **US$ 16.274** (−US$ 2.235 vs mercado).
- Regras/lições práticas:
  - Compare sempre com o benchmark investível (SPY), depois das taxas dos fundos.
  - Leve em conta a defasagem da informação (até 45 dias): o fundo não replica o trade real.
  - Olhe a trajetória, não só o resultado final: a vantagem do NANC encolheu de US$ 1.072 para US$ 589.
  - Uma estratégia que "copia" não garante nada: a versão GOP perdeu 12% em relação ao SPY.
- Evidência: sim. Yahoo Finance (retorno total, líquido de taxas), 07/02/2023 a 05/11/2026. Limite: uma única janela de ~3,7 anos e nenhum teste de significância.

## 2. @brianferoldi

- **Status:** ativo · 310K seguidores · 4.055 posts · último post em 17/11/2026 (vários por dia).
- **Perfil:** educação em análise de ações ("I teach investors how to analyze stocks"), em dois formatos: carrosséis "cheat sheet"/scorecard de uma empresa e reels em que ele explica com folha impressa e marca-texto. Vende livro, cursos e a ferramenta própria Stock Simplifier. Quase todo post termina com "comente STOCK(S)" para receber a ferramenta "grátis". Mostra muitos dados financeiros (margens, múltiplos, CAGR), mas as notas de 1 a 5 são julgamento próprio e não há backtest delas.

### 10 posts mais recentes (fixados excluídos)

| # | Link | Tipo | Resumo | Tema |
|---|---|---|---|---|
| 1 | https://www.instagram.com/p/Df2dzg5DjZI/ | carrossel (3) | Cheat sheet de Walt Disney ($DIS): fase 4/5, negócio 2,8/5, valuation 3/5 | valuation/fundamentos |
| 2 | https://www.instagram.com/reel/Df2T4p4NCHR/ | reel (108 s) | "Por que a Anthropic vale US$ 1,4 tri?": P/S atual vs futuro e comparação com pares | valuation/fundamentos |
| 3 | https://www.instagram.com/p/Df2CuhhDopj/ | carrossel (14) | Sandisk a US$ 809: scorecard em 7 fatores | valuation/fundamentos |
| 4 | https://www.instagram.com/reel/Df1_YUat1SE/ | reel | ARM está cara ou barata? | valuation/fundamentos |
| 5 | https://www.instagram.com/p/Df1I67kjkkE/ | carrossel | Versão curta do Sandisk (fase 3/5, negócio 3,3/5, valuation 3/5) | valuation/fundamentos |
| 6 | https://www.instagram.com/reel/Dfzf_xFoHMJ/ | reel | IONQ a US$ 28: cara ou barata? | valuation/fundamentos |
| 7 | https://www.instagram.com/reel/DfzfQClNPBl/ | reel | IONQ a US$ 28 (segunda versão do mesmo tema) | valuation/fundamentos |
| 8 | https://www.instagram.com/p/DfxspqKmmbe/ | carrossel | Cheat sheet da Disney (mesma legenda do post 1, publicada 2 dias antes) | valuation/fundamentos |
| 9 | https://www.instagram.com/p/DfxSPIRmr7B/ | carrossel | Cheat sheet da Joby Aviation (fase 1/5, negócio 3,8/5) | valuation/fundamentos |
| 10 | https://www.instagram.com/reel/DfxG_L4NMwR/ | reel | Microsoft a US$ 525 está barata? | valuation/fundamentos |

### Df2CuhhDopj — @brianferoldi
- Tipo: carrossel (14 slides)
- Tema: valuation/fundamentos
- Legenda (resumo fiel): pergunta se Sandisk é compra a US$ 809 e mostra a nota nos 7 fatores. Negócio: gosta (4/5). Moat: fino (2/5). Direção do moat: estável (3/5). Crescimento: alto (5/5). Gestão: razoável (3/5). Risco: moderado (3/5). Valuation: preço justo (3/5). Classifica como negócio de fase 3 (a escala começa a pagar: a receita desacelera um pouco, mas o lucro cresce mais rápido que as vendas). Veredito: negócio médio, valuation justa. Lição: um bom negócio e um bom investimento não são a mesma coisa, e o preço pago define o retorno. CTA "comente STOCK".
- Slide a slide:
  1. Capa com pergunta "cheap or expensive at $809?"; gráfico de preço (eixo US$ 0–2.500) com pico perto de US$ 2.000 e queda até **US$ 809**; **+2148% em 2 anos**.
  2. Overview: missão, o que faz (memória NAND flash) e como ganha dinheiro (SSDs para nuvem/empresa, drives embarcados, cartões, pendrives). Receita por segmento **US$ 20,3B**: Edge 60% (US$ 12,2B, ▲195%), Datacenter 25,4% (US$ 5,2B, ▲437%), Consumer 14,5% (US$ 2,9B, ▲29%).
  3. Clientes: três grupos de compradores; concorrentes citados (Kioxia, Micron, Samsung, SK Hynix, Yangtze). Mapa de receita por região: Ásia 68%, Américas 25%, EMEA 7%.
  4. Financial overview (TTM): margem bruta **80,0%**, operacional **72,5%**, líquida **67,0%**, FCF **59,9%**. Crescimento: receita 1 ano **+272,4%**, 3 anos **+48,3%**, EPS 1 ano **−1137,9%**, FCF 1 ano **+3265,3%**. Valuation trailing: P/S 4,0x, P/L 6,5x, P/VP 6,3x, P/FCF 6,6x. Saúde financeira: caixa US$ 5,1B, dívida US$ 0, dívida/PL 0,00x, EBIT/juros 599,8x. Valuation forward: P/S 2,1x, P/L 3,0x, P/FCF 3,5x.
  5. Qualidade do negócio (4 perguntas com marcadores ✗/–/✓): receita previsível? Não (cíclica, ligada ao preço do flash). Consegue subir preço? Não. Resiste a recessão? Fraco. Posição competitiva? Média.
  6. Fase: receita crescendo? Sim, **29% a.a. desde FY22** (gráfico até US$ 29B). Lucrativa? Sim, **US$ 21B** de lucro operacional. Devolve capital? Só recompras (US$ 9,5B; ações de 146M para 144M; dividendo US$ 0,00). Linha do tempo de 5 fases, com Sandisk na **fase 3: Operating Leverage**.
  7. CTA da ferramenta Stock Simplifier ("10.000+ ações").
  8. Moat: largura **Thin (2)**; direção **Stable (3)**. Switching costs: moderado. Network effects, ativos intangíveis, custo baixo e counter-positioning: nenhum.
  9. Crescimento **High (5)**: CAGR de receita 1 ano +272,4%, 3 anos +49,3%; CAGR de lucro 1 ano −1137,9%. Gráfico 2022–LTM de receita (−37,6%, +9,5%, +10,4%, +175,3%, +43,1%) e lucro (−301,4%, +69,9%). Indústria crescendo? Devagar. Espaço para novos produtos? Improvável.
  10. Gestão **Decent (3)**: CEO David V. Goeckeler (1,7 ano no cargo, 0,459% das ações ≈ US$ 529M); cofundador Eli Harari. Receita vs estimativa: bateu **8/8** (média +7,8%). EPS vs estimativa: bateu **8/8** (média +81,6%). Nota dos funcionários: 3,4/5.
  11. Risco **Moderate (3)**: receita diversificada (top 10 clientes = 44%); disrupção: algum risco; fora do controle: muito (preço do flash, joint venture com Kioxia, fábricas no Japão/Malásia, tarifas); saúde financeira: forte (sem dívida de longo prazo, FCF 59,8%).
  12. Valuation: tabela trailing vs forward (P/S 4,0x → 2,1x; P/L 6,4x → **3,0x, marcado como melhor métrica**; P/FCF 6,6x → 3,5x). A justificativa é que o lucro deve crescer 120% no próximo ano. Gráfico do P/L forward (faixa 1,6x–7,9x, com projeção de analistas 2,7x–2,6x). Régua de preço: **US$ 423 / US$ 851 / US$ 1.708 / US$ 2.136** (muito atraente → justo → caro → muito caro), com o preço atual em **US$ 809**.
  13. Veredito: escala Sell / Pass / Hold / **Watch** / Buy. Negócio médio, valuation justa. Fase 3 de 5. Nota composta **3,3/5**. Valuation: P/L forward 3,0x vs média de 2,6x. Régua de US$ 186 a US$ 1.311, com o preço em US$ 809,11.
  14. CTA final ("comente STOCK") e aviso de que não é recomendação de investimento.
- Regras/lições práticas:
  - Separe a qualidade do negócio do preço: "bom negócio ≠ bom investimento".
  - Para empresas cíclicas com lucro explodindo, P/L trailing engana. Ele usa P/L forward e diz por quê.
  - Classifique a "fase" da empresa para escolher as métricas que importam (crescimento vs margens vs devolução de capital).
  - Olhe o histórico de surpresas (bateu 8/8 estimativas) e a concentração de clientes (top 10 = 44%).
  - **Cuidado com as inconsistências do próprio post:** EPS 1 ano de −1137,9% convive com margem líquida de 67% (provável artefato de cálculo a partir de prejuízo); a régua de preço do slide 12 (US$ 423–2.136) não bate com a do slide 13 (US$ 186–1.311); a nota do negócio é 4/5 na legenda, mas o post curto (Df1I67kjkkE) diz 3,3/5.
- Evidência: parcial. Dados financeiros com data (TTM até 02/10/2026, preço de 13/11/2026), mas sem fonte citada. As notas de 1 a 5 são opinião, e a régua de preço justo não tem método explícito nem teste histórico.

### Df2T4p4NCHR — @brianferoldi
- Tipo: reel (108,3 s; frames a cada ~8 s até o fim)
- Tema: valuation/fundamentos
- Legenda (resumo fiel): CTA "comente Stocks" para receber a ferramenta de fases; título "Why is Anthropic worth $1.4 trillion? (ANT Stock Analysis)".
- Frame a frame:
  - 0–8 s: folha "ANTHROP\C — Nasdaq (ANT)" com dados de IPO destacados com marca-texto; legenda falada "and $78 per share".
  - 16–24 s: gráfico de receita acelerando (rótulo ~**US$ 17,0B**), descrito como empresa que acabou de começar a gerar receita, puxada por adoção empresarial.
  - 32–40 s: demonstrativo consolidado de resultados sobre a grade de 5 fases; ele grifa a receita e cita "but just $1.26 billion" (linha de resultado; o rótulo exato não ficou legível).
  - 48 s: grade de fases (Startup → Hyper growth → Operating leverage → Capital return → Decline).
  - 56 s: **Price-to-Sales 40x**.
  - 64 s: diagrama "Market Capitalization" ÷ receita dos últimos 12 meses vs receita estimada (múltiplo trailing vs forward).
  - 80–88 s: **US$ 1,4 tri ÷ US$ 35B (LTM) = 40x**; **US$ 1,4 tri ÷ US$ 118–135B (estimativa 2027) = 10x–12x**.
  - 96 s: tabela de crescimento / P/S / P/S forward: Anthropic **1.368% / 40x / 10–12x**; Nvidia **106% / 12x / 7x**; Microsoft **19% / 11x / 9x**; Google **25% / 7x / 6x**.
  - 104 s: volta à grade de fases ("use isso numa ação que você tem").
- Regras/lições práticas:
  - Para empresas em hipercrescimento, compare o P/S trailing com o forward: 40x pode virar 10–12x se a projeção se confirmar.
  - Ponha o múltiplo ao lado do crescimento e de pares (P/S de 6x–12x para big techs crescendo 19%–106%).
  - O resultado depende da estimativa de receita (US$ 118–135B); se ela falhar, o múltiplo real fica bem maior.
- Evidência: parcial. Números de capitalização, receita e estimativas na tela, mas sem fonte nem data das estimativas. Não há teste histórico de quando P/S forward alto funcionou.

### Df2dzg5DjZI — @brianferoldi
- Tipo: carrossel (3 slides)
- Tema: valuation/fundamentos
- Legenda (resumo fiel): a Walt Disney em uma página (fase, nota em cada fator, sinais verdes e vermelhos, valuation), feita com o Stock Simplifier. Veredito: negócio médio, valuation justa. Fase 4 de 5, negócio 2,8/5, valuation 3/5. CTAs para salvar e comentar "STOCK".
- Slide a slide:
  1. Capa verde-escura com o logo da Disney: "$DIS Breakdown — The Walt Disney cheat sheet".
  2. Página única: preço **US$ 118,70** (15/11/2026), market cap US$ 205B, receita TTM US$ 98,9B. Nota composta **2,9 — WATCH**. Notas: Business "Like it 4"; Moat "Narrow 3"; Moat direction "Eroding 2"; Growth "Below avg 2"; Management "Decent 3"; Risk "Moderate 3"; Valuation "Fair value 3".
     - Mix de receita: Entertainment 44%, Experiences 38%, Sports 18%.
     - Fase: 4, Capital Return.
     - Moat: switching costs, network effects, low-cost e counter-positioning = nenhum; intangíveis = moderado; todos estáveis.
     - Gestão: CEO Josh D'Amaro (0,5 ano no cargo); participação do CEO 0,002% (US$ 4M); ROIC 5%; lucro vs estimativas: bate; shareholder yield 3,4%; margem líquida 9,3%.
     - Crescimento: CAGR de receita 1/3/5 anos = +4,6% / +4,0% / +9,2%; CAGR de lucro = −24,0% / +58,0% / +51,4%.
     - Métricas-chave: receita +4,0% (3 anos), margem operacional 13,7%, FCF 8,4%, lucro +58,0% (3 anos), retorno sobre capital 5%.
     - Balanço: caixa US$ 5,2B, dívida US$ 46B. Dividend yield 1,1%, shareholder yield 3,4%. Margem bruta 37,6%, líquida 9,3%.
     - Valuation: barato US$ 110,69 / justo US$ 120,07 / caro US$ 129,46. P/S 2,1x, P/L 24,5x, P/VP 1,9x, P/FCF 24,7x.
     - Sinais verdes: receita segue forte, moat se ampliando, margens e FCF crescendo. Sinais vermelhos: receita desacelera, valuation à frente dos fundamentos, risco central se concretiza.
  3. CTA "Comment STOCK" e aviso de que não é recomendação.
- Regras/lições práticas:
  - O formato de uma página (fase + 7 fatores + flags + faixa de preço) é um bom checklist reutilizável.
  - Dívida de US$ 46B contra caixa de US$ 5,2B e ROIC de 5% explicam o "negócio médio" melhor do que a nota.
  - **Inconsistências:** a legenda diz "Business 2,8/5", mas o card mostra "Business 4" e composta 2,9. O sinal verde "moat se ampliando" contradiz "Moat direction: Eroding" (os flags parecem genéricos de template).
- Evidência: parcial. Dados financeiros com data, sem fonte. O post da Disney foi publicado duas vezes (DfxspqKmmbe e Df2dzg5DjZI) com a mesma legenda.

## 3. @humphreytalks

- **Status:** ativo · 907K seguidores · 520 posts · último post em 17/11/2026.
- **Perfil:** finanças pessoais para o público americano (FIRE, 401(k), contas, ETFs, imóveis), em reels com o autor falando para a câmera e cartelas de animação com contas simples. Divulga downloads gratuitos e conta remunerada (link na bio) e faz publis (inclusive do Claude). Mostra aritmética básica, sem fonte nem teste das regras (ex.: 4%).

### 10 posts mais recentes (fixados excluídos)

| # | Link | Tipo | Resumo | Tema |
|---|---|---|---|---|
| 1 | https://www.instagram.com/reel/Df3G85Iu8EF/ | reel (38 s, collab @thehumphreyshow) | Jovem de 25 anos com US$ 40 mil investidos ganhando US$ 21/h (trecho de podcast) | finanças pessoais |
| 2 | https://www.instagram.com/reel/Df0YNnIRYza/ | reel | Conta corrente vs poupança de alto rendimento | finanças pessoais |
| 3 | https://www.instagram.com/reel/Dfsc4wszufD/ | reel (73 s) | 4 coisas para fazer antes de 2027 | finanças pessoais |
| 4 | https://www.instagram.com/reel/DfnXbEfykOm/ | reel | O que é ESPP | finanças pessoais |
| 5 | https://www.instagram.com/reel/DfijYr-u65R/ | reel (67 s) | 3 níveis de patrimônio (US$ 100 mil, 500 mil, 2 mi) | finanças pessoais |
| 6 | https://www.instagram.com/reel/Dfibq5oOUcL/ | reel | Comprou casa de US$ 2,5 mi por US$ 1,3 mi? | opinião/mercado |
| 7 | https://www.instagram.com/reel/DfaR1gzBFD-/ | reel (63 s) | Barista FIRE explicado com a regra dos 4% | finanças pessoais |
| 8 | https://www.instagram.com/reel/DfXYMPBB_7g/ | reel | Publicidade do Claude (@claudeai) | outro |
| 9 | https://www.instagram.com/reel/DfVQstWBxSp/ | reel | 5 coisas para melhorar quando começar a ganhar bem | finanças pessoais |
| 10 | https://www.instagram.com/reel/DfQIb8gyod1/ | reel | 4 mudanças ao atingir US$ 5 milhões | finanças pessoais |

### DfaR1gzBFD- — @humphreytalks
- Tipo: reel (62,8 s; frames a cada ~6 s até o fim)
- Tema: finanças pessoais
- Legenda (resumo fiel): Barista FIRE é uma aposentadoria antecipada em que um trabalho de meio período cobre a diferença entre o que a carteira paga e as despesas. Pergunta se o seguidor usaria o método.
- Frame a frame:
  - 3 s: ícone de US$ com "$1,000 per month is worth over $300,000".
  - 9–15 s: o autor explica o trabalho de meio período como ponte entre a carteira e as despesas.
  - 21–27 s: "Age 45 · 4% rule": carteira US$ 600.000 × 4% = **US$ 24.000/ano**.
  - 33 s: "The gap" (barras): saque seguro US$ 24.000 vs despesas anuais US$ 50.000 (eixo US$ 0–60K).
  - 39 s: menção à estratégia Coast FIRE.
  - 51 s: "The math": US$ 12.000 ÷ 4% (= US$ 300.000).
  - 57 s: "Portfolio needed" com despesas de US$ 50.000/ano: sem Barista FIRE **US$ 1.250.000**; com Barista FIRE (meio período) **US$ 600.000**.
  - 62 s: pede comentários.
- Regras/lições práticas:
  - Regra dos 4%: carteira necessária = despesa anual ÷ 0,04 (US$ 50.000 → US$ 1,25 mi).
  - Cada US$ 1.000/mês de renda ativa "vale" US$ 300.000 de carteira (US$ 12.000 ÷ 4%).
  - **Conta que não fecha no vídeo:** a lacuna é de US$ 26.000/ano (US$ 50 mil − US$ 24 mil), ou seja, ≈ US$ 2.167/mês de meio período, não US$ 1.000.
- Evidência: não. A regra dos 4% é apresentada como dada, sem fonte (ex.: Trinity Study) nem discussão de sequência de retornos, inflação ou horizonte longo para quem para aos 45.

### DfijYr-u65R — @humphreytalks
- Tipo: reel (67 s; frames a cada ~7 s até o fim)
- Tema: finanças pessoais
- Legenda (resumo fiel): três níveis de patrimônio que mudam a vida, e pergunta qual o seguidor busca.
- Frame a frame:
  - 3 s: lista Tier 1 US$ 100k / Tier 2 (oculto) / Tier 3 (oculto).
  - 10–13 s: Tier 1 **US$ 100.000** × retorno médio de 8% a.a. = **US$ 8.000/ano**.
  - 17 s: **US$ 500.000** antes dos 45.
  - 24 s: "Coast FIRE": US$ 500 mil antes dos 45 cresceria até a aposentadoria plena aos 67 (sem novos aportes, a ~8%).
  - 31–34 s: comparação com o patrimônio mediano americano: **US$ 216.100** vs Tier 2 US$ 500.000 (eixo US$ 0–600k).
  - 38–43 s: Tier 3 **US$ 2.000.000** × 4% = **US$ 80.000/ano**.
  - 50 s: "maybe not yet": alto custo de vida, várias casas, muitos filhos.
  - 64 s: "It gets easier": Tier 1 leva 5–10 anos; depois, "compounding does the work".
- Regras/lições práticas:
  - Converta patrimônio em renda: ×8% (retorno esperado) ou ×4% (saque seguro). São duas premissas diferentes no mesmo vídeo.
  - O primeiro US$ 100 mil é o mais lento; depois os juros compostos aceleram.
  - Coast FIRE: um valor suficiente cedo pode crescer sozinho até a aposentadoria.
- Evidência: fraca. O patrimônio mediano dos EUA (US$ 216.100) é mostrado sem fonte (não verifiquei). O retorno de 8% não é justificado nem ajustado por inflação.

### Dfsc4wszufD — @humphreytalks
- Tipo: reel (73 s; frames a cada ~8 s até o fim)
- Tema: finanças pessoais
- Legenda (resumo fiel): quatro coisas financeiras para fazer antes de 2027; pergunta o que o seguidor está fazendo antes do fim do ano.
- Frame a frame:
  - 5 s: calendário de dezembro/2026 com o dia 31 marcado; checklist: 1. **401(k) match**; 2–4 ocultos.
  - 25 s: tela "Contributions": employer match 4% / your contribution 4% → "Full match".
  - 33 s: barras **Cash US$ 108k, Debt −US$ 22k, Net worth US$ 86k**, para "começar o ano que vem" (aparentemente o item 2: calcular o patrimônio líquido).
  - 41–49 s: tax-loss harvesting: ganhos (parte tributada / não tributada) vs perdas vendidas, compensando **até US$ 3.000/ano** da renda comum.
  - 57–65 s: item 4: nova dedução de caridade, **US$ 1.000 (solteiro) / US$ 2.000 (casado)** em doações em dinheiro.
- Regras/lições práticas:
  - Contribua no mínimo o percentual que a empresa iguala (match), porque é retorno imediato.
  - Calcule o patrimônio líquido (ativos − dívidas) no fim do ano, como linha de base.
  - Realize prejuízos para abater ganhos, e até US$ 3.000 da renda comum (regra dos EUA).
- Evidência: regras fiscais americanas citadas sem fonte. Não é conteúdo de validação de estratégia.

## 4. @econoweek

- **Status:** ativo · 254K seguidores · 831 posts · último post em 18/11/2026.
- **Perfil:** o economista César Esperandio ("menos status, mais liberdade"): finanças pessoais, consumo consciente e vida simples, em reels de opinião e carrosséis com simulação. Faz publis (ex.: #publi Binance) e parcerias. Mostra dados só em simulações de juros compostos, que conferem; o resto é opinião.

### 10 posts mais recentes (fixados excluídos)

| # | Link | Tipo | Resumo | Tema |
|---|---|---|---|---|
| 1 | https://www.instagram.com/reel/Df4BxEVJCxd/ | reel (162 s) | Compras que viram despesa por anos (a partir de vídeo de @rafinhabastos) | finanças pessoais |
| 2 | https://www.instagram.com/reel/Df287rOJv8E/ | reel | "Concorda?" (opinião) | opinião/mercado |
| 3 | https://www.instagram.com/p/Df1c5Bjvc_l/ | carrossel (6) | Investir metade de cada aumento: R$ 564 mil vs R$ 2,7 mi em 30 anos | finanças pessoais |
| 4 | https://www.instagram.com/reel/DfzTqGKha9g/ | reel (179 s, #publi Binance) | Investimentos que ele não faz (COE etc.) e por que mudou de ideia sobre cripto | opinião/mercado |
| 5 | https://www.instagram.com/reel/DfubVtFOAt6/ | reel (69 s) | Ataque hacker ao Tesouro Direto: investimentos não afetados | risco e drawdown |
| 6 | https://www.instagram.com/reel/DfrJ0DbjC7R/ | reel | "Nosso dinheiro tá seguro?": ataques hacker | risco e drawdown |
| 7 | https://www.instagram.com/reel/DfolBWNHGnb/ | reel | Lista "menos status, mais liberdade" | finanças pessoais |
| 8 | https://www.instagram.com/reel/DfmbrIEiX8j/ | reel | 1 ano do transplante capilar (pessoal) | outro |
| 9 | https://www.instagram.com/p/DfjbVnzjRsP/ | imagem | Meme | outro |
| 10 | https://www.instagram.com/reel/Dfg2qpgkeLT/ | reel (158 s) | Gastou R$ 7 mil para recuperar o carro antigo em vez de trocar | finanças pessoais |

### Df1c5Bjvc_l — @econoweek
- Tipo: carrossel (6 slides)
- Tema: finanças pessoais
- Legenda (resumo fiel): pergunta se é realista investir metade de cada aumento de salário.
- Slide a slide:
  1. "Posso te dar um conselho?": quando o salário aumentar, não deixe tudo virar novo padrão de vida; aproveite uma parte e invista a outra. Foto do autor sobre roxo.
  2. "R$ 564 mil ou R$ 2,7 milhões?": diferença entre manter R$ 500/mês investidos e aumentar o aporte com metade de cada aumento salarial por 30 anos. Gráfico de área 0–30 anos: R$ 2,7 mi (verde) vs R$ 564 mil (cinza).
  3. "Funciona assim": aumento de R$ 250 → R$ 125 para viver melhor + R$ 125 para investir.
  4. "No começo, a diferença parece pequena": salário inicial R$ 5 mil, aumento anual de 5%. Marcos (aporte fixo / com metade dos aumentos): 5 anos R$ 35 mil / R$ 53 mil; 10 anos R$ 85 mil / R$ 180 mil; 20 anos R$ 248 mil / R$ 853 mil; 30 anos R$ 564 mil / **R$ 2,68 mi**. Nota: simulação de 30 anos com rentabilidade líquida estimada de 6,8% a.a., valores nominais, sem descontar inflação.
  5. "Não existe nenhuma mágica": investir mais + manter constância + tempo.
  6. "Não precisa ser metade": pode ser 10%, 20% ou 30%; o importante é não deixar todo aumento virar padrão de vida.
- Regras/lições práticas:
  - Indexe o aporte à renda: direcione uma fração fixa de cada aumento ao investimento.
  - O efeito aparece tarde: em 10 anos a diferença é de 2x; em 30 anos, de 4,8x.
  - **Verificação:** reproduzi a conta (6,8% a.a. com capitalização mensal, R$ 500/mês + 50% do aumento acumulado sobre R$ 5 mil a 5% a.a.). Deu R$ 563.612 vs R$ 2.684.486, e R$ 52.795 / R$ 179.888 / R$ 853.266 em 5/10/20 anos. **Bate com o post.**
  - Atenção: os valores são nominais. Os 6,8% líquidos não descontam a inflação, então o poder de compra real é bem menor.
- Evidência: simulação reproduzível, com premissas escritas no slide 4. Não usa dados históricos.

### DfzTqGKha9g — @econoweek
- Tipo: reel (179,4 s; frames verificados a cada ~12–20 s, sem áudio)
- Tema: opinião/mercado
- Legenda (resumo fiel): pergunta que investimento o seguidor não faz de jeito nenhum; diz que já foi resistente a cripto, mas mudou de opinião. Cita a Binance como parceira do conteúdo, adequando a operação às regras do Banco Central (mesmo app/site/login, com ajustes em produtos). #publi.
- Frame a frame (só legendas na tela; o conteúdo falado não pôde ser ouvido): falas fragmentadas como "normalmente", "de ganhar", "que o banco combina", "você bota a grana", "de todos os outros", "por exemplo", "entender mais" e "100%". Aos ~76 s, print de notícia sobre a BlackRock buscando tokenizar ETFs depois do sucesso do fundo de bitcoin. Aos ~130 s, print de manchete sobre a Binance perder mais de US$ 6 bilhões no "maior hack de criptomoedas da história".
- Regras/lições práticas:
  - Pelos comentários e legendas, o vídeo critica produtos de banco com retorno "combinado" (ex.: COE, em que no cenário ruim você só recupera o aportado, perdendo para a inflação).
  - **Conflito de interesse explícito:** o post é publi da Binance e mostra, no mesmo vídeo, notícia de hack bilionário na Binance.
- Evidência: não há teste. Limitação: assisti em frames, sem áudio, então o argumento completo não foi capturado.

### DfubVtFOAt6 — @econoweek
- Tipo: reel (68,9 s; frames em 3, 15, 22, 42 e 62 s, sem áudio)
- Tema: risco e drawdown
- Legenda (resumo fiel): pergunta a opinião do seguidor; diz que o Tesouro Direto foi alvo de ataque hacker, mas os investimentos não foram afetados.
- Frame a frame: o autor fala com os rótulos fixos "TESOURO DIRETO / ATAQUE HACKER". Legendas fragmentadas: "alvo de ataque", "impactados e nem", "ou que pareça real". Aos ~62 s, mostra no celular uma lista de notificações/mensagens.
- Regras/lições práticas:
  - Risco operacional e cibernético existe mesmo em título público. O dinheiro custodiado não foi afetado, mas o risco seguinte é golpe (phishing pedindo senha).
  - Um comentário útil: não clique em links, entre só pelo caminho que você já usa e confira o extrato.
- Evidência: não. Sem link da fonte da notícia. Assistido sem áudio.

## 5. @academiadevalor

- **Status:** ativo · 119K seguidores · 3.778 posts · último post em 15/11/2026.
- **Perfil:** "evolução no bolso e na mente". Quase só carrosséis com prints de tweets (principalmente de @otimistaoficial) sobre política, geopolítica e economia, com tom opinativo; alguns posts sobre dolarização e imóveis. Vende "oportunidades" (link de captação) e viagens "pagando até 90% menos" (milhas). Os dados aparecem sem link para a fonte.

### 10 posts mais recentes

| # | Link | Tipo | Resumo | Tema |
|---|---|---|---|---|
| 1 | https://www.instagram.com/p/DfxDG4rg4z_/ | imagem | "Somos o país do quê?": crítica política ao Brasil | opinião/mercado |
| 2 | https://www.instagram.com/p/Dfr96xnlvnK/ | carrossel | Carros chineses: destroem o mercado ou trazem concorrência? | opinião/mercado |
| 3 | https://www.instagram.com/p/DfrfzL9lvnA/ | carrossel (6) | Juro alto e preço de imóvel: FipeZAP, descontos médios de 13% | opinião/mercado |
| 4 | https://www.instagram.com/p/DfhK0CkFnaK/ | carrossel | Jensen Huang (Nvidia) e uma história "de Hollywood" | opinião/mercado |
| 5 | https://www.instagram.com/p/DfgGqLHFpwR/ | carrossel (5) | Investimentos chineses em setores estratégicos do Brasil | opinião/mercado |
| 6 | https://www.instagram.com/p/DferEWslr0B/ | carrossel | Corrupção e instituições: Paraguai vs Brasil | opinião/mercado |
| 7 | https://www.instagram.com/p/Dfc0VMaGjvA/ | carrossel | Episódio histórico da década de 1990 | opinião/mercado |
| 8 | https://www.instagram.com/p/Dfa38hgGuA4/ | carrossel | Notícia sobre a prisão do presidente destituído do Paraguai | opinião/mercado |
| 9 | https://www.instagram.com/p/DfXQ0pjlhZn/ | carrossel | Alerta sobre bloqueio de contas bancárias no Paraguai | risco e drawdown |
| 10 | https://www.instagram.com/p/DfVllE2AeAa/ | carrossel (1) | Dolarizar sem esperar o momento perfeito (gráfico S&P 500 em 10 anos) | opinião/mercado |

> Notícias políticas citadas nos posts (Paraguai, China) foram registradas como o post as apresenta. Não verifiquei esses fatos.

### DfVllE2AeAa — @academiadevalor
- Tipo: carrossel (1 slide)
- Tema: opinião/mercado
- Legenda (resumo fiel): o maior erro de quem quer dolarizar é esperar o momento perfeito; sempre vai parecer caro. Ninguém acerta o timing com consistência, então a estratégia é construir patrimônio em moeda forte aos poucos, com disciplina. Se o mercado subir, já está posicionado; se cair, continua comprando. Dolarizar não é apostar na alta do dólar, e sim reduzir a dependência de uma única moeda, economia e país. O objetivo é chegar em 10–20 anos com patrimônio mais diversificado, porque tempo não se compra de volta.
- Slide a slide:
  1. Print de tweet de @otimistaoficial: sempre que fala em dolarizar, alguém diz que é loucura investir nos EUA "na máxima". Gráfico do S&P 500: **7.688,62, +5.603 em 10 anos**; abas 3m / 6m / ano / 1a / 2a / 5a / **10a** / tudo; eixo Y 3.460–7.926; eixo X 2016–2026. Cinco balões com a mesma frase ("Você tá louco, investir nos EUA na máxima") em pontos sucessivos da subida.
- Regras/lições práticas:
  - Aportes periódicos (DCA) evitam depender de acertar o fundo.
  - "Estar na máxima" é o estado normal de um índice em alta. O gráfico mostra novas máximas repetidas em 10 anos.
- Evidência: um gráfico de preço (sem dividendos, sem câmbio). É anedótico: mostra um período de alta (viés de seleção) e não testa DCA vs aporte único. O @tradionquant (DfjCMULExt_) faz esse teste de verdade.

### DfrfzL9lvnA — @academiadevalor
- Tipo: carrossel (6 slides)
- Tema: opinião/mercado
- Legenda (resumo fiel): o juro sobe e o preço do imóvel cai? 73% consideram os imóveis caros, a intenção de compra cai e a inadimplência sobe. O imóvel não precisa desvalorizar; basta o dono precisar vender. Com financiamento caro há menos compradores, e quem tem dinheiro ganha poder de negociação. Pergunta se os imóveis estão caros ou se o dinheiro vale menos.
- Slide a slide (prints de tweets de @otimistaoficial):
  1. Arte "Juro sobe. Preço do imóvel cai?" (prédios, seta vermelha para baixo, moedas).
  2. A Caixa divulgou resultados com inadimplência maior, lucro menor e crédito mais caro. Pesquisa FipeZAP: **73%** dos entrevistados acham os imóveis caros e a intenção de compra está caindo.
  3. Com juros altos, o poder de compra cai: o imóvel segue anunciado por **R$ 800 mil**, mas menos gente consegue pagar, e o vendedor que precisa de dinheiro negocia.
  4. A pesquisa mostra que **67%** das transações tiveram algum desconto, com **abatimento médio de 13%** nos negócios abaixo do preço pedido. Não prevê colapso; os dados ainda mostram valorização em muitos mercados.
  5. Quem tem liquidez pode achar vendedores que aceitam propostas que não aceitariam em outro cenário; patrimônio se constrói comprando bem.
  6. Oportunidade é quando poucos conseguem comprar e alguns precisam vender; os próximos meses podem ser interessantes para quem tem dinheiro, paciência e sabe negociar.
- Regras/lições práticas:
  - Separe preço pedido de preço negociado (descontos médios de 13% em 67% das transações).
  - Juro alto reduz o número de compradores financiados, e quem paga à vista ganha poder de barganha.
- Evidência: cita FipeZAP e resultados da Caixa, mas sem link, data da pesquisa ou amostra. Não há série histórica de preço vs juros.

### DfgGqLHFpwR — @academiadevalor
- Tipo: carrossel (5 slides)
- Tema: opinião/mercado
- Legenda (resumo fiel): a China não precisa invadir o Brasil, está chegando com bilhões. Lista setores: energia (geração, distribuição, transmissão), petróleo (participação em um dos maiores campos), portos, cimento (CSN vendeu a divisão de cimentos por R$ 12,7 bi a uma chinesa, pendente de aprovações) e automóveis (BYD, GWM). Só em 2025, o Brasil recebeu US$ 6,1 bi em investimentos chineses, o maior destino mundial. Diz não ser contra o capital estrangeiro, mas distingue atrair capital de criar dependência, e critica o Brasil por discutir ideologia e criar impostos.
- Slide a slide:
  1. Tweet de @otimistaoficial com enquadramento político (a "esquerda" diz que querem entregar o Brasil aos EUA, mas estariam entregando à China) + imagem das bandeiras dos EUA e do Brasil.
  2. Thread de Drew Crawford (traduzida pelo Grok): State Grid assume a CPFL Energia em jan/2017; gasta ~R$ 30 bi em 2018 por outros acionistas; opera ~10% das linhas de alta tensão (mais de 16.000 km); em mar/2026, fecha acordo de ~R$ 7 bi por uma linha de 1.200 km em Minas Gerais.
  3. China Three Gorges compra 10 hidrelétricas da Duke Energy em 2016 e vira a maior geradora privada; SPIC paga R$ 7,18 bi pela usina de São Simão (concessão até 2048); duas estatais chinesas com 15% dos direitos excedentes de Búzios (~1,19 mi barris/dia em set/2026); China Merchants compra 90% da TCP em 2017; empresa apoiada pela CITIC paga US$ 1,1 bi pelo negócio de sementes de milho da Dow (18,5% do mercado).
  4. CMOC assume minas de ouro (MA, MG, BA) em jan/2026 por até US$ 1,015 bi; CSN Cimentos para a Huaxin por R$ 12,7 bi (7/11); MMG/China Minmetals aguarda aprovação europeia para comprar o negócio de níquel da Anglo American por US$ 500 mi; em 2025, o Brasil atraiu US$ 6,1 bi de investimento chinês, mais que qualquer país; em abr/2024, a State Grid disse querer investir mais R$ 200 bi.
  5. State Grid, Three Gorges, SPIC e CNOOC respondem à SASAC, em Pequim; o próprio governo brasileiro vendeu alguns desses ativos em leilão (São Simão, Búzios); o argumento final é que capital diversificado entre países evita que um único governo estrangeiro "segure o interruptor".
- Regras/lições práticas:
  - Para investidor, a lição útil é mapear a concentração de controle por origem do capital em setores regulados (energia, portos, mineração).
  - O post mistura dados verificáveis (valores, datas) com enquadramento político. Separe as duas coisas antes de usar.
- Evidência: muitos números com data, mas sem fontes linkadas (thread de terceiro, traduzida por IA). Não verifiquei os valores.

## 6. @guiainvest

- **Status:** ativo · 443K seguidores · 4.481 posts · último post em 18/11/2026 (quase diário).
- **Perfil:** consultoria de investimentos registrada na CVM ("desde 2008", "top 10 do Brasil"), com carrosséis escuros premium (laranja + preto, fotos de banco de imagem) sobre alocação, dolarização, dividendos e planejamento patrimonial. Toda peça leva ao "Diagnóstico Patrimonial Gratuito", ou seja, vende consultoria. Às vezes mostra simulações e cita estudos, mas sem divulgar premissas completas nem fontes dos dados.

### 10 posts mais recentes (fixados excluídos)

| # | Link | Tipo | Resumo | Tema |
|---|---|---|---|---|
| 1 | https://www.instagram.com/p/Df4jJj-Fuf4/ | carrossel | Para onde vai a liquidez extra de fim de ano (13º, PLR, bônus, dividendos) | finanças pessoais |
| 2 | https://www.instagram.com/p/Df11ZeOlqRR/ | carrossel | Depois de 20 anos acumulando: a fase de desacumular | finanças pessoais |
| 3 | https://www.instagram.com/p/DfzF3bGoT97/ | carrossel | Dólar a R$ 5,59 (maior em 15 meses): é hora de mandar dinheiro para fora? | opinião/mercado |
| 4 | https://www.instagram.com/p/DfwhFAlCLE1/ | carrossel | Midterms dos EUA, freios e contrapesos (Madison, 1788) e mercados | opinião/mercado |
| 5 | https://www.instagram.com/p/Dft8PmnDd1t/ | carrossel (9) | Um ano de CDI devolvido em 3 semanas de dólar | risco e drawdown |
| 6 | https://www.instagram.com/p/DfrlXeKoFkb/ | carrossel | Tratar dividendos futuros como salário garantido é risco | risco e drawdown |
| 7 | https://www.instagram.com/p/DfpIvG7oM8u/ | carrossel (8) | Dividendos parecem pequenos quando o patrimônio é pequeno (juros compostos) | estatística |
| 8 | https://www.instagram.com/reel/DfmzY9eEjqS/ | reel | Novembro Azul (institucional) | outro |
| 9 | https://www.instagram.com/p/Dfj6KNVIPj8/ | carrossel (8) | Rebalancear sem vender: 31 anos, +R$ 2,1 mi | backtest/validação |
| 10 | https://www.instagram.com/p/DfhET_6jsB7/ | carrossel | Patrimônio vs renda que ele gera para sustentar a vida | finanças pessoais |

### Dfj6KNVIPj8 — @guiainvest
- Tipo: carrossel (8 slides)
- Tema: backtest/validação
- Legenda (resumo fiel): em quase 32 anos de mercado brasileiro, dois investidores com o mesmo patrimônio inicial, os mesmos aportes e a mesma carteira (partes iguais de Ibovespa, CDI e S&P 500 em reais, sem vender nada) terminaram com mais de R$ 2,1 mi de diferença líquida. A única variável foi o destino de cada aporte: quem direcionou o dinheiro novo para a classe abaixo do peso-alvo terminou com **R$ 20,5 mi líquidos**; quem dividiu de forma neutra ficou com **R$ 18,3 mi**. Rebalancear vendendo antecipa 15% de imposto a cada venda com lucro e drena os juros compostos. Entre 2003 e 2011, a regra direcionou **93%** dos aportes ao mercado global com câmbio médio de **R$ 1,99**. Conclui que usar o aporte para calibrar a alocação não aciona imposto, não gera taxa e afasta o humor do investidor. CTA para salvar.
- Slide a slide:
  1. "Invest insights — Rebalancear a carteira sem vender" (foto de peso de metal sobre pedra).
  2. "A mesma carteira. Três resultados." 31 anos com 1/3 Ibovespa, 1/3 CDI e 1/3 S&P 500; quem direcionou aportes para a classe defasada atingiu R$ 20,5 mi líquidos, R$ 2,1 mi acima da divisão neutra. Três cards com mini gráficos: IBOVESPA (Asset 100% · IBOVESPA 10,50% · ROI −10,33%), CDI (Asset 80% · CDI 0,50% · ROI S&P CDI −10,77%), S&P 500 (Asset 100% · S&P 500 33,58% · ROI −17,31%).
  3. "Vender para rebalancear destrói o ganho": a venda aciona 15% de imposto em cada ganho, e o valor recolhido antes da hora deixa de render juros compostos por décadas.
  4. "**R$ 2,34 milhões**" foi o ganho bruto corroído pelo imposto em giros semestrais: o prêmio pré-IR de **R$ 2,5 mi** caiu para **R$ 160 mil** no resgate final.
  5. "Compra anticíclica sem previsão": entre 2003 e 2011, a regra mandou 93% dos aportes ao S&P 500 com dólar a R$ 1,99, e esses aportes viraram **28%** do patrimônio final.
  6. "A regra blinda contra o humor": em 1998 e 2002, as manchetes mandavam abandonar o Brasil; em 2010, o dólar parecia sem futuro; a alocação matemática tirou a decisão do calor das notícias.
  7. "Como aplicar no seu portfólio": (1) escreva o peso-alvo na política de investimentos; (2) direcione dividendos e novos recursos à classe defasada; (3) venda apenas quando houver desvio extremo sobre o alvo.
  8. "O aporte é a decisão mais barata": comparar o peso atual antes de cada aplicação não gera imposto nem corretagem e dispensa previsões.
- Regras/lições práticas:
  - Rebalanceie pelo fluxo (aportes e dividendos vão para a classe abaixo do alvo) e venda só em desvio extremo.
  - Em conta tributável, rebalancear vendendo com frequência (semestral) pode custar caro em imposto antecipado. O post estima que um prêmio de R$ 2,5 mi pré-IR vira R$ 160 mil.
  - O rebalanceamento por aporte gera compra anticíclica automática (ex.: dólar barato em 2003–2011).
  - **Pontos fracos:** não informa patrimônio inicial, valor dos aportes, fonte dos dados, se o Ibovespa inclui dividendos, nem como o CDI foi tributado. A legenda diz "quase 32 anos" e o slide diz "31 anos". Os números dos cards do slide 2 (ex.: "ROI −10,33%", "CDI 0,50%", "Asset 80%") não têm relação aparente com o texto e parecem ilustrativos.
- Evidência: simulação histórica descrita, mas não reproduzível (sem premissas nem fonte). É o post mais próximo de um backtest entre os perfis brasileiros.

### DfpIvG7oM8u — @guiainvest
- Tipo: carrossel (8 slides)
- Tema: estatística
- Legenda (resumo fiel): com patrimônio pequeno, os dividendos parecem irrelevantes; o que muda em duas décadas é a escala. O cérebro projeta bem o crescimento linear, mas não o composto. Cita um estudo do Journal of Finance mostrando que esse viés leva a subestimar o efeito do tempo. Exercício hipotético: R$ 1 mi a 5% a.a. acima da inflação, sem aportes, ganha ≈ R$ 630 mil na 1ª década, R$ 1 mi na 2ª e R$ 1,67 mi na 3ª; a última supera as duas primeiras somadas. Nos primeiros anos, a impaciência faz girar a carteira ou interromper a acumulação. Sugere avaliar se a estrutura aguenta tempo suficiente, não só quanto rendeu no ano.
- Slide a slide:
  1. "Investir com sabedoria — Dividendos parecem pequenos quando o patrimônio é pequeno".
  2. "No começo, o extrato parece um detalhe": em 2004, os primeiros dividendos pareciam irrelevantes; 20 anos depois, a carteira paga parte crescente da vida; o que mudou foi a escala.
  3. "O cérebro pensa em linha reta": projetamos bem o linear e mal o composto.
  4. "O viés do crescimento exponencial": gráfico com curva exponencial (laranja) vs reta (cinza). Estudo do Journal of Finance (2009): quem vê juros compostos como linha reta subestima o futuro, poupa menos e se endivida mais.
  5. "A parte íngreme da curva chega por último": três barras crescentes; R$ 1 mi a 5% a.a. real, sem aportes, ganha R$ 630 mil na 1ª década, R$ 1 mi na 2ª e R$ 1,67 mi na 3ª.
  6. "US$ 81,5 bilhões vieram após os 65 anos": dos US$ 84,5 bi de Warren Buffett citados por Morgan Housel em "A Psicologia Financeira", quase tudo veio na reta final.
  7. "Os primeiros anos testam a paciência": sem resultado imediato, o investidor gira a carteira, gasta a renda ou interrompe a acumulação.
  8. "A sua estrutura consegue continuar de pé?": mais importante que o rendimento do ano é manter bons ativos por tempo suficiente.
- Regras/lições práticas:
  - Ganho por década com juros compostos (5% real): ≈ 0,63x → 1,02x → 1,67x o capital inicial. A 3ª década supera as duas primeiras somadas.
  - **Verificação:** reproduzi (1,05^10, ^20, ^30): R$ 628.895 / R$ 1.024.403 / R$ 1.668.645. **Bate com o post.**
  - Desconfie da intuição linear ao projetar patrimônio; use fórmula ou planilha.
- Evidência: conta reproduzível. Cita o Journal of Finance (2009), coerente com o estudo de Stango & Zinman sobre "exponential growth bias", embora o post não dê autores nem título. Também cita Housel. O exemplo é hipotético (5% real constante, sem volatilidade).

### Dft8PmnDd1t — @guiainvest
- Tipo: carrossel (9 slides)
- Tema: risco e drawdown
- Legenda (resumo fiel): o CDI levou 12 meses para render 14%, e o dólar levou menos de três semanas para subir 13% (de R$ 4,99 para perto de R$ 5,65). Para quem mede patrimônio em dólar, quase um ano de rendimento foi devolvido em dias, embora o extrato em reais mostre saldo maior. O Brasil tem o juro real mais alto do mundo (~9% a.a.), que não é prêmio grátis, e sim compensação por risco e desconfiança; os EUA captam por 10 anos a ~5% a.a. Combustível, alimentos, tecnologia e viagens têm preço global, então depender só de renda fixa brasileira expõe tudo a uma moeda. A solução é medir o patrimônio em duas moedas (hoje, há 1 e há 5 anos) e construir proteção cambial aos poucos. CTA para o Diagnóstico Patrimonial Gratuito.
- Slide a slide:
  1. "Offshore Connection — Quanto vale o seu patrimônio em dólar hoje?" (foto da bolsa de Nova York).
  2. "Um ano de CDI devolvido em três semanas": CDI +14% em 12 meses; dólar +13% em menos de 3 semanas, de R$ 4,99 para perto de R$ 5,65.
  3. "O real apanhou de dois lados": dentro, dúvida sobre as contas do governo com Selic perto de 14%; fora, inflação americana acima do esperado levou o dólar ao maior nível global em 19 meses.
  4. "Juro alto não é prêmio. É risco.": para tomar dinheiro por 10 anos, os EUA pagam perto de 5% a.a., e o Brasil precisa pagar cerca de 15% (três vezes mais) para compensar a desconfiança.
  5. "Qual régua mede o seu patrimônio?": quem guarda tudo em uma moeda fica mais rico ou mais pobre sem decidir nada; ter parte em dólar não é aposta de curto prazo.
  6. "Você já gasta em dólar sem sair do Brasil": gasolina, pão, celular, máquinas e viagens têm preço formado lá fora.
  7. "O erro não é ter renda fixa no Brasil": o erro é ter apenas renda fixa brasileira e chamar isso de segurança.
  8. "Dois passos para agir com constância": (1) divida o patrimônio pela cotação do dólar hoje, há 1 ano e há 5 anos, para medir o poder de compra real; (2) defina a parcela em moeda forte e construa aos poucos, sem tentar acertar o fundo.
  9. "Quanto do seu patrimônio depende de uma única moeda?": CTA para a conversa de 30 minutos.
- Regras/lições práticas:
  - Meça o retorno na moeda em que você consome. Em dólar, CDI +14% com câmbio +13% dá ≈ +0,9% (1,14 / 1,132 − 1).
  - Juro alto embute risco-país e cambial.
  - Diversificação cambial gradual, sem timing.
  - **Inconsistências:** a legenda compara o juro **real** brasileiro (~9%) com o juro **nominal** americano (~5%), enquanto o slide compara nominais (15% vs 5%). Outro post do mesmo perfil, 2 dias depois (DfzF3bGoT97), fala em dólar a R$ 5,59 como "maior valor em 15 meses", enquanto este cita R$ 5,65 e "19 meses".
- Evidência: números de mercado sem fonte nem data exata. Não há teste histórico de diversificação cambial.

## 7. @boletinhos

- **Status:** ativo, por pouco · 59,9K seguidores · 39 posts · último post em 19/06/2026 (5 meses, dentro do limite de 6).
- **Perfil:** finanças pessoais para a geração Z, com memes, cores neon e linguagem informal ("sua sanidade financeira voltou"). Grande parte é publi (Contabilizei, Serasa) com captação por comentário ("comenta IR/COLA/É VÍDEO"). Não vende curso nem sinal. Usa números em exemplos simples, sem fonte e com alguns erros de conta.

### 10 posts mais recentes

| # | Link | Tipo | Resumo | Tema |
|---|---|---|---|---|
| 1 | https://www.instagram.com/reel/DZx62XVhLJY/ | reel (publi Contabilizei) | Abrir uma ME e faturar sem dor de cabeça | carreira |
| 2 | https://www.instagram.com/p/DZcpoeyDu9N/ | carrossel (marcado como "AI content"; publi Contabilizei) | Virar PJ: sem 13º, organizar antes | carreira |
| 3 | https://www.instagram.com/reel/DYDJ0uWBspQ/ | reel (publi Contabilizei) | Perfis no Imposto de Renda + manual gratuito | finanças pessoais |
| 4 | https://www.instagram.com/reel/DXt9PUHjhX9/ | reel (parceria Serasa) | Score de crédito é comportamento repetido | finanças pessoais |
| 5 | https://www.instagram.com/reel/DWWcD9lDqdh/ | reel | 326 mil brasileiros encerraram contas de bet em um clique | risco e drawdown |
| 6 | https://www.instagram.com/p/DWT9h3tjp10/ | carrossel (7) | Salário de R$ 5.000 vs R$ 3.877 que cai na conta | finanças pessoais |
| 7 | https://www.instagram.com/reel/DWE2wCtgSgZ/ | reel | Limite alto do cartão pode ser isca: como reduzir | finanças pessoais |
| 8 | https://www.instagram.com/p/DV8keeQjlW0/ | carrossel (7) | Juros compostos: "foto ou vídeo?", R$ 200/mês a 15% a.a. | finanças pessoais |
| 9 | https://www.instagram.com/reel/DVywoy6gaTZ/ | reel | Reserva de emergência de 3 a 6 meses de gastos ("power bank") | finanças pessoais |
| 10 | https://www.instagram.com/reel/DVlK0pVjp7C/ | reel (37,6 s) | PIX parcelado é crédito com juros; cartão sem juros não | finanças pessoais |

### DV8keeQjlW0 — @boletinhos
- Tipo: carrossel (7 slides)
- Tema: finanças pessoais
- Legenda (resumo fiel): alerta de calculadora de juros compostos. Quanto mais cedo o "vídeo" começa, mais "frames" acumula: começar com R$ 50 hoje vale mais que R$ 500 daqui a 3 anos. Dinheiro parado é foto; investido é vídeo rodando 24h. CTA "É VÍDEO" para receber o simulador.
- Slide a slide:
  1. "Imagina seu dinheiro te fazendo uma pergunta: é foto ou vídeo?" — **Foto R$ 12.200 / Vídeo R$ 17.266,14**.
  2. "R$ 200 por mês durante 5 anos": um ficou parado, o outro em movimento; "a grana foi a mesma".
  3. "Foto é dinheiro parado": o valor não muda, não cresce.
  4. "Vídeo é dinheiro em movimento": cada frame é um mês rendendo sobre o que já rendeu; "isso se chama juros compostos".
  5. "Como funciona na prática" — R$ 200 investidos a 15% a.a. (≈ 1,17% a.m.). Tabela aportado / acumulado: mês 01 R$ 200,00 / R$ 202,34; mês 03 R$ 600,00 / R$ 607,06; mês 05 R$ 1.000,00 / R$ 1.023,71; 01 ano R$ 2.400,00 / R$ 2.560,84; 03 anos R$ 7.200,00 / R$ 8.892,51; 05 anos **R$ 12.200,00** / R$ 17.266,14.
  6. "O ingrediente secreto": não é quanto nem onde, é por quanto tempo. 5 anos R$ 17.266,14; 10 anos R$ 51.994,53; 20 anos R$ 262.341,38.
  7. CTA: "Manda É VÍDEO" para receber o simulador.
- Regras/lições práticas:
  - Tempo é a variável dominante: R$ 200/mês viram ≈ R$ 17 mil em 5 anos, R$ 52 mil em 10 e R$ 262 mil em 20 (a 15% a.a.).
  - **Verificação:** reproduzi com taxa mensal de 1,1715% e aporte no fim do mês. Os valores de 3/5/10/20 anos batem (R$ 8.892,51; R$ 17.266,14; R$ 51.994,53; R$ 262.341,38).
  - **Erros:** total aportado em 5 anos é **R$ 12.000** (60 × 200), não R$ 12.200 (slides 1 e 5). A linha "mês 01 = R$ 202,34" usa aporte no início do mês, enquanto as demais usam aporte no fim (convenções misturadas).
  - **Premissa irrealista:** 15% a.a. bruto, nominal, sem IR e sem inflação. Em termos reais e líquidos, o resultado seria muito menor.
- Evidência: simulação reproduzível (taxa declarada), sem dado histórico nem fonte para a taxa.

### DWT9h3tjp10 — @boletinhos
- Tipo: carrossel (7 slides)
- Tema: finanças pessoais
- Legenda (resumo fiel): o primeiro holerite chega com outro número e você não entende; há uma pergunta simples que você podia ter feito antes de assinar.
- Slide a slide:
  1. Salário combinado **R$ 5.000,00**; caiu na conta **R$ 3.877** ("que conta é essa?").
  2. A pergunta que ninguém faz na entrevista é quanto vai cair na conta, não o bruto nem o número bonito da proposta. R$ 5.000 de salário ≠ R$ 5.000 na conta.
  3. "O que você não considerou": INSS **R$ 473**; vale-transporte **R$ 300**; vale-refeição **R$ 150**; plano de saúde **R$ 200**; imposto de renda **R$ 0\*** (\*isento para quem ganha até R$ 5.000 desde 2026).
  4. Nenhum desses descontos é ilegal nem "pegadinha"; só ninguém contou antes, e você podia ter perguntado.
  5. Antes de aceitar a vaga, pergunte: qual o salário líquido; se VR e VT são descontados; se tem plano de saúde e quanto sai do bolso. "Três perguntas. Cinco minutos."
  6. Já assinou e não entendeu? Pergunte ao RH por que cada valor foi descontado, se o desconto é obrigatório ou pode ser cancelado, e onde ver o FGTS.
  7. "Salário líquido não é surpresa": é uma conta que dá para fazer antes; CTA para mandar a quem acabou de ser contratado.
- Regras/lições práticas:
  - Avalie propostas pelo líquido. Nesse exemplo, os descontos somam R$ 1.123 (22,5%): 5.000 − 473 − 300 − 150 − 200 = **R$ 3.877** ✓.
  - Vale-transporte: desconto máximo de 6% do salário (R$ 300 em R$ 5.000) ✓.
  - Pergunte quais descontos são opcionais (VT, plano) e quais são obrigatórios (INSS).
- Evidência: a aritmética bate. A isenção de IR até R$ 5 mil a partir de 2026 é citada sem fonte; o valor de INSS (R$ 473) é aproximado e não verifiquei com a tabela de 2026.

### DVlK0pVjp7C — @boletinhos
- Tipo: reel (37,6 s)
- Tema: finanças pessoais
- Legenda (resumo fiel): PIX parcelado não é igual a parcelar no cartão. No cartão sem juros você não paga a mais; no PIX parcelado é crédito com juros. Pede para salvar e mandar a quem achava que era igual.
- Frame a frame: **análise parcial.** A captura de tela deste reel falhou repetidamente no navegador, então só verifiquei dois frames: a abertura (texto "Você viu 'PIX parcelado'", com logos BLTNS e um animal em close) e um frame verde com "RESPIRA". Não consegui ver o restante do vídeo.
- Regras/lições práticas (pela legenda):
  - PIX parcelado = operação de crédito com juros (compare o CET), diferente de "parcelado sem juros" no cartão.
- Evidência: nenhuma no que foi visto (sem taxas, CET ou exemplo numérico).

---

## Notas como fonte de aprendizado QUANTITATIVO

| Perfil | Nota | Justificativa |
|---|---|---|
| @tradionquant | 5/5 | Testes com fonte (Ken French/CRSP, Yahoo), período, custos, caixa remunerado, centenas de janelas e taxa de acerto, além de ceticismo explícito ("ou sorte?"). |
| @brianferoldi | 3/5 | Muitos dados fundamentalistas bem organizados (margens, P/L forward, pares), mas notas subjetivas, sem fonte, sem backtest e com inconsistências entre slides. |
| @humphreytalks | 2/5 | Aritmética simples e clara (regra dos 4%, FIRE), mas regras tomadas como dadas, sem fonte e com pequenas contas que não fecham. |
| @econoweek | 2/5 | A simulação de aportes é correta e reproduzível (premissas escritas), mas é exceção; o resto é opinião e publi. |
| @academiadevalor | 1/5 | Opinião e política em prints de tweets; números sem fonte e gráficos escolhidos a dedo. |
| @guiainvest | 3/5 | Traz simulação de 31 anos, estudo acadêmico e contas que conferem, mas sem premissas e fontes divulgadas, com números ilustrativos sem sentido e foco em captar clientes. |
| @boletinhos | 2/5 | Contas de juros compostos e holerite basicamente corretas, mas com erros (R$ 12.200), premissa de 15% bruto e muito conteúdo patrocinado. |

---

## Prints

Arquivos na pasta `prints/`.

| Arquivo | Link direto | O que mostra / por que importa |
|---|---|---|
| DfV5v9TFUhf_1.png | https://www.instagram.com/reel/DfV5v9TFUhf/ (19 s) | Placar "quem tinha mais um ano depois": esperar 6× vs comprar em setembro 19×; é o resultado central do teste |
| DfV5v9TFUhf_2.png | https://www.instagram.com/reel/DfV5v9TFUhf/ (37 s) | Antes do voto, a bolsa subiu 19 de 25 vezes; isola a janela que explica a diferença |
| DfV5v9TFUhf_3.png | https://www.instagram.com/reel/DfV5v9TFUhf/ (59 s) | "Esperar compensou 7 de 26": um acerto recente ≠ regra válida ("ou sorte?") |
| DfjCMULExt__1.png | https://www.instagram.com/reel/DfjCMULExt_/ (53 s) | Grade das 1.084 janelas de 10 anos (1926–2016) por vencedor: testar todas as datas de início |
| DfjCMULExt__2.png | https://www.instagram.com/reel/DfjCMULExt_/ (60 s) | Buy the dip venceu só 47,1% das janelas (2 empates) |
| DfjCMULExt__3.png | https://www.instagram.com/reel/DfjCMULExt_/ (64 s) | Placar de regras que venceram o buy-and-hold: 0 de 2; exemplo de 2006–2026 (US$ 84.606 vs US$ 82.966) |
| DfdO2jkgZ-f_1.png | https://www.instagram.com/reel/DfdO2jkgZ-f/ (45 s) | Corrida em 2025: NANC US$ 18.158, SPY US$ 17.086, GOP US$ 14.763 |
| DfdO2jkgZ-f_2.png | https://www.instagram.com/reel/DfdO2jkgZ-f/ (84 s) | Placar final em 05/11/2026: +US$ 589 e −US$ 2.235 vs SPY |
| Df2CuhhDopj_1.png | https://www.instagram.com/p/Df2CuhhDopj/?img_index=4 | Tabela de margens, crescimento, saúde financeira e múltiplos trailing/forward |
| Df2CuhhDopj_2.png | https://www.instagram.com/p/Df2CuhhDopj/?img_index=12 | Escolha da métrica (P/L forward), gráfico histórico do múltiplo e faixas de preço |
| Df2CuhhDopj_3.png | https://www.instagram.com/p/Df2CuhhDopj/?img_index=13 | Scorecard final 3,3/5 e régua de valuation (compare com o slide 12: as faixas não batem) |
| Df2T4p4NCHR_1.png | https://www.instagram.com/reel/Df2T4p4NCHR/ (88 s) | Cálculo P/S: US$ 1,4 tri ÷ US$ 35B = 40x vs ÷ US$ 118–135B = 10–12x |
| Df2T4p4NCHR_2.png | https://www.instagram.com/reel/Df2T4p4NCHR/ (96 s) | Tabela de pares: crescimento, P/S e P/S forward (Anthropic, Nvidia, Microsoft, Google) |
| Df2dzg5DjZI_1.png | https://www.instagram.com/p/Df2dzg5DjZI/?img_index=2 | Cheat sheet de uma página da Disney: modelo de checklist fundamentalista |
| DfaR1gzBFD-_1.png | https://www.instagram.com/reel/DfaR1gzBFD-/ (33 s) | "The gap": saque seguro de US$ 24k vs despesas de US$ 50k |
| DfaR1gzBFD-_2.png | https://www.instagram.com/reel/DfaR1gzBFD-/ (57 s) | Carteira necessária: US$ 1,25 mi (sem trabalho) vs US$ 600 mil (Barista FIRE) |
| DfijYr-u65R_1.png | https://www.instagram.com/reel/DfijYr-u65R/ (13 s) | Tier 1: US$ 100k × 8% = US$ 8.000/ano (premissa de retorno) |
| DfijYr-u65R_2.png | https://www.instagram.com/reel/DfijYr-u65R/ (64 s) | "It gets easier": 100k → 500k → 2M, com os juros compostos fazendo o trabalho |
| Dfsc4wszufD_1.png | https://www.instagram.com/reel/Dfsc4wszufD/ (49 s) | Tax-loss harvesting: perdas abatendo ganhos, até US$ 3.000/ano |
| Df1c5Bjvc_l_1.png | https://www.instagram.com/p/Df1c5Bjvc_l/?img_index=2 | Curva R$ 564 mil vs R$ 2,7 mi em 30 anos |
| Df1c5Bjvc_l_2.png | https://www.instagram.com/p/Df1c5Bjvc_l/?img_index=4 | Marcos de 5/10/20/30 anos e premissas (6,8% líquido, nominal), conferidos por mim |
| DfrfzL9lvnA_1.png | https://www.instagram.com/p/DfrfzL9lvnA/?img_index=5 | Dados FipeZAP: 67% das transações com desconto, média de 13% |
| DfVllE2AeAa_1.png | https://www.instagram.com/p/DfVllE2AeAa/ | S&P 500 em 10 anos com "máximas" repetidas; útil, mas é um caso de viés de seleção |
| DfgGqLHFpwR_1.png | https://www.instagram.com/p/DfgGqLHFpwR/?img_index=2 | Lista de aquisições chinesas no setor elétrico (State Grid/CPFL), dados sem fonte |
| Dfj6KNVIPj8_1.png | https://www.instagram.com/p/Dfj6KNVIPj8/?img_index=2 | "Mesma carteira, três resultados": R$ 20,5 mi vs R$ 18,3 mi; os cards têm números sem sentido |
| Dfj6KNVIPj8_2.png | https://www.instagram.com/p/Dfj6KNVIPj8/?img_index=4 | Custo fiscal do rebalanceamento semestral: R$ 2,5 mi pré-IR viram R$ 160 mil |
| Dfj6KNVIPj8_3.png | https://www.instagram.com/p/Dfj6KNVIPj8/?img_index=7 | As 3 regras de rebalanceamento por aporte, prontas para aplicar |
| DfpIvG7oM8u_1.png | https://www.instagram.com/p/DfpIvG7oM8u/?img_index=4 | Viés do crescimento exponencial: curva composta vs reta (Journal of Finance, 2009) |
| DfpIvG7oM8u_2.png | https://www.instagram.com/p/DfpIvG7oM8u/?img_index=5 | Ganho por década com 5% real: R$ 630 mil → R$ 1 mi → R$ 1,67 mi (conferido) |
| Dft8PmnDd1t_1.png | https://www.instagram.com/p/Dft8PmnDd1t/?img_index=2 | CDI +14% em 12 meses vs dólar +13% em 3 semanas: retorno medido em outra moeda |
| Dft8PmnDd1t_2.png | https://www.instagram.com/p/Dft8PmnDd1t/?img_index=4 | Juro de 10 anos: EUA ~5% vs Brasil ~15% (juro alto = risco) |
| DV8keeQjlW0_1.png | https://www.instagram.com/p/DV8keeQjlW0/?img_index=1 | "Foto R$ 12.200 vs vídeo R$ 17.266,14": o aportado correto é R$ 12.000 |
| DV8keeQjlW0_2.png | https://www.instagram.com/p/DV8keeQjlW0/?img_index=5 | Tabela de juros compostos (R$ 200/mês, 15% a.a.) com convenções misturadas |
| DV8keeQjlW0_3.png | https://www.instagram.com/p/DV8keeQjlW0/?img_index=6 | 5/10/20 anos: R$ 17 mil / R$ 52 mil / R$ 262 mil, efeito do tempo |
| DWT9h3tjp10_1.png | https://www.instagram.com/p/DWT9h3tjp10/?img_index=1 | Salário de R$ 5.000 vs R$ 3.877 líquido |
| DWT9h3tjp10_2.png | https://www.instagram.com/p/DWT9h3tjp10/?img_index=3 | Descontos linha a linha (INSS, VT, VR, plano, IR); a soma confere |
