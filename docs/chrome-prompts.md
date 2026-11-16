# Prompts para a extensão Claude in Chrome

Mande uma rodada por vez no painel do Claude no Chrome, com o Instagram logado. Ao final de cada rodada a extensão gera o `rodada-<N>.md` com os achados e a lista de prints. Cole o resultado (e os prints, se baixou) na sessão das skills.

Ordem: 1 → 2 → 3A → 3B → 3C → 4A → 4B.

---

## Rodada 1: Links 1 a 8

```
Abra cada link abaixo no Instagram, um por vez. Em carrosséis, avance por TODOS os slides; em reels, assista até o fim.

Para cada link, gere um bloco Markdown neste formato:

### <ID do post> — @<autor>
- Tipo: carrossel (N slides) | reel
- Tema: design visual | UI/motion | UX | dashboard | investimentos | outro
- Legenda: <texto completo da legenda>
- Slide a slide: <para cada slide: todo o texto visível, números, cores (hex aproximado), fontes, layout e componentes mostrados>
- Regras/lições práticas: <lista objetiva do que o post ensina>

Links:
https://www.instagram.com/p/DfEmKLLFEDi/
https://www.instagram.com/p/DfUnwyQGCTA/
https://www.instagram.com/p/Dff1uulGoxb/
https://www.instagram.com/p/De_FtT3k-tT/
https://www.instagram.com/p/DescJ2zTeSf/
https://www.instagram.com/p/DfFBFpXDZLv/
https://www.instagram.com/reel/DfkSCaRNfa0/
https://www.instagram.com/p/DfkBGDyDgqS/

Não comente, não curta e não siga ninguém; apenas leia.

AO FINAL DA RODADA, gere o arquivo `rodada-1.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas com os principais aprendizados da rodada;
   - depois, TODOS os blocos e listas desta rodada;
   - no fim, uma seção "Prints".
2. Prints: tire print só dos slides ou frames com algo visual importante (layout, paleta, gráfico, antes/depois, curva de animação, tabela de números), no máximo 3 por post. Nomeie cada um como `<ID>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-1.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-1.md` num ÚNICO bloco de código Markdown. Na seção "Prints", ponha uma linha por print: nome | link direto (em carrossel, use `?img_index=N`; em reel, o segundo do vídeo) | o que mostra e por que importa.
```

---

## Rodada 2: Links 9 a 16

```
Abra cada link abaixo no Instagram, um por vez. Em carrosséis, avance por TODOS os slides; em reels, assista até o fim.

Para cada link, gere um bloco Markdown neste formato:

### <ID do post> — @<autor>
- Tipo: carrossel (N slides) | reel
- Tema: design visual | UI/motion | UX | dashboard | investimentos | outro
- Legenda: <texto completo da legenda>
- Slide a slide: <para cada slide: todo o texto visível, números, cores (hex aproximado), fontes, layout e componentes mostrados>
- Regras/lições práticas: <lista objetiva do que o post ensina>

Links:
https://www.instagram.com/p/DfcdrhgFFMR/
https://www.instagram.com/p/DfaQe-CiBfJ/
https://www.instagram.com/p/DfUvP_ulPC6/
https://www.instagram.com/p/Dfus5sWFAov/
https://www.instagram.com/p/DftsSH-jnfs/
https://www.instagram.com/p/DfRucYFjrac/
https://www.instagram.com/p/DfUWa0jAed7/
https://www.instagram.com/p/DfowdSMiPzc/

Não comente, não curta e não siga ninguém; apenas leia.

AO FINAL DA RODADA, gere o arquivo `rodada-2.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas com os principais aprendizados da rodada;
   - depois, TODOS os blocos e listas desta rodada;
   - no fim, uma seção "Prints".
2. Prints: tire print só dos slides ou frames com algo visual importante (layout, paleta, gráfico, antes/depois, curva de animação, tabela de números), no máximo 3 por post. Nomeie cada um como `<ID>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-2.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-2.md` num ÚNICO bloco de código Markdown. Na seção "Prints", ponha uma linha por print: nome | link direto (em carrossel, use `?img_index=N`; em reel, o segundo do vídeo) | o que mostra e por que importa.
```

---

## Rodada 3A: Perfis de design já usados (só posts novos)

```
Abra estes perfis do Instagram, um por vez. Pule os posts listados como "já analisados".

1. https://www.instagram.com/gg.designhub/ (nenhum analisado ainda)
2. https://www.instagram.com/rational_edge/ (já analisados: DfuDLH7BUsx)
3. https://www.instagram.com/theglidestudio/ (já analisados: Dfvja0XCyIi, DfwhC1riuuO, DfyFShTounu)
4. https://www.instagram.com/motion_ui_interface/ (já analisados: Dd25eCoBJGr, Dd4UtBDBsIS, DdRneVWhBSY, DdtzWoMhLtW, Ddy5RJOha1U, De4B0UxPXIk, DeUr5-AhdvQ, Del7XTgsuwI, DerGbJAhUTm, DfP6EoLBtgg, DfTr-mwhZT3, DfVOGNnzR_D, DfWjKQPhUbn, DfZkZZ4hkuV, DfcwOHLh76I, DfgcqeMBPCU, Dflzxq5Bqfj)
5. https://www.instagram.com/designmotionhq/ (já analisados: DUEjWRukT_2, DXRpZTTMr9a, DZ2Dp5wt0pJ, Dc-4jNbtyJg, DfPJo9UBJ7D, DfemaTCBncA, DfreUkyBNQg)
6. https://www.instagram.com/_code_and_chill_/ (já analisados: DbfG6fuPE9y, De12lc1vUmr, Deoi1WhP83h, DfCWtPgPcfP, DffBnb2vlUn, DfkNvnePItL, DfrqAX9v59S)
7. https://www.instagram.com/code.xr/ (já analisados: DeoGCPlzKOs, DfHrMboTVDZ, DfKPFDwz2aA, DfMH6YTTcwx)
8. https://www.instagram.com/niki.aroca/ (já analisados: DfIaULMIRC-, DfKxflroHj3)

Para cada perfil:
1. Escreva 2–3 linhas sobre o perfil: tema principal, estilo visual e tipo de conteúdo.
2. Liste os 10 posts mais recentes ainda não analisados com: link, tipo (carrossel/reel), resumo de 1 linha e tema.
3. Escolha os 3 posts mais úteis e analise cada um neste formato (em carrosséis, avance por TODOS os slides; em reels, assista até o fim):

### <ID do post> — @<autor>
- Tipo: carrossel (N slides) | reel
- Tema: design visual | UI/motion | UX | dashboard | investimentos | outro
- Legenda: <texto completo da legenda>
- Slide a slide: <para cada slide: todo o texto visível, números, cores (hex aproximado), fontes, layout e componentes mostrados>
- Regras/lições práticas: <lista objetiva do que o post ensina>

Não comente, não curta e não siga ninguém; apenas leia.

AO FINAL DA RODADA, gere o arquivo `rodada-3A.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas com os principais aprendizados da rodada;
   - depois, TODOS os blocos e listas desta rodada;
   - no fim, uma seção "Prints".
2. Prints: tire print só dos slides ou frames com algo visual importante (layout, paleta, gráfico, antes/depois, curva de animação, tabela de números), no máximo 3 por post. Nomeie cada um como `<ID>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-3A.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-3A.md` num ÚNICO bloco de código Markdown. Na seção "Prints", ponha uma linha por print: nome | link direto (em carrossel, use `?img_index=N`; em reel, o segundo do vídeo) | o que mostra e por que importa.
```

---

## Rodada 3B: Novos perfis de motion e UX

```
Abra estes perfis do Instagram, um por vez:

1. https://www.instagram.com/gifux/
2. https://www.instagram.com/ramotion/
3. https://www.instagram.com/nick_buturishvili/
4. https://www.instagram.com/ranjithalingal/
5. https://www.instagram.com/uxdesignmastery/
6. https://www.instagram.com/ui.tips/
7. https://www.instagram.com/ultimateuiux/
8. https://www.instagram.com/christvizcarra/
9. https://www.instagram.com/uxmemo/

Para cada perfil:
1. Verifique se existe e se está ativo: número de seguidores e data do último post. Se não existir ou não postar há mais de 6 meses, escreva só "INATIVO: <motivo>" e passe para o próximo.
2. Escreva 2–3 linhas sobre o perfil: tema principal, estilo visual, tipo de conteúdo e qualidade (dicas concretas com números/comparações vs. só inspiração).
3. Liste os 10 posts mais recentes ainda não analisados com: link, tipo (carrossel/reel), resumo de 1 linha e tema.
4. Escolha os 3 posts mais úteis e analise cada um neste formato (em carrosséis, avance por TODOS os slides; em reels, assista até o fim):

### <ID do post> — @<autor>
- Tipo: carrossel (N slides) | reel
- Tema: design visual | UI/motion | UX | dashboard | investimentos | outro
- Legenda: <texto completo da legenda>
- Slide a slide: <para cada slide: todo o texto visível, números, cores (hex aproximado), fontes, layout e componentes mostrados>
- Regras/lições práticas: <lista objetiva do que o post ensina>

No final, dê uma nota de 1 a 5 para cada perfil como fonte de aprendizado de UI/UX, com uma frase de justificativa.

Não comente, não curta e não siga ninguém; apenas leia.

AO FINAL DA RODADA, gere o arquivo `rodada-3B.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas com os principais aprendizados da rodada;
   - depois, TODOS os blocos e listas desta rodada;
   - no fim, uma seção "Prints".
2. Prints: tire print só dos slides ou frames com algo visual importante (layout, paleta, gráfico, antes/depois, curva de animação, tabela de números), no máximo 3 por post. Nomeie cada um como `<ID>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-3B.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-3B.md` num ÚNICO bloco de código Markdown. Na seção "Prints", ponha uma linha por print: nome | link direto (em carrossel, use `?img_index=N`; em reel, o segundo do vídeo) | o que mostra e por que importa.
```

---

## Rodada 3C: Novos perfis de inspiração visual

```
Abra estes perfis do Instagram, um por vez:

1. https://www.instagram.com/uidesignpatterns/
2. https://www.instagram.com/dailywebdesign/
3. https://www.instagram.com/interfacely/
4. https://www.instagram.com/twohabitsdesign/
5. https://www.instagram.com/ui.pixel/
6. https://www.instagram.com/spruzzo.ui/

Para cada perfil:
1. Verifique se existe e se está ativo: número de seguidores e data do último post. Se não existir ou não postar há mais de 6 meses, escreva só "INATIVO: <motivo>" e passe para o próximo.
2. Escreva 2–3 linhas sobre o perfil: tema principal, estilo visual, tipo de conteúdo e qualidade (dicas concretas vs. só inspiração).
3. Liste os 10 posts mais recentes ainda não analisados com: link, tipo (carrossel/reel), resumo de 1 linha e tema.
4. Escolha os 3 posts mais úteis e analise cada um neste formato (em carrosséis, avance por TODOS os slides; em reels, assista até o fim):

### <ID do post> — @<autor>
- Tipo: carrossel (N slides) | reel
- Tema: design visual | UI/motion | UX | dashboard | investimentos | outro
- Legenda: <texto completo da legenda>
- Slide a slide: <para cada slide: todo o texto visível, números, cores (hex aproximado), fontes, layout e componentes mostrados>
- Regras/lições práticas: <lista objetiva do que o post ensina>

No final, dê uma nota de 1 a 5 para cada perfil como fonte de aprendizado de UI/UX, com uma frase de justificativa.

Não comente, não curta e não siga ninguém; apenas leia.

AO FINAL DA RODADA, gere o arquivo `rodada-3C.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas com os principais aprendizados da rodada;
   - depois, TODOS os blocos e listas desta rodada;
   - no fim, uma seção "Prints".
2. Prints: tire print só dos slides ou frames com algo visual importante (layout, paleta, gráfico, antes/depois, curva de animação, tabela de números), no máximo 3 por post. Nomeie cada um como `<ID>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-3C.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-3C.md` num ÚNICO bloco de código Markdown. Na seção "Prints", ponha uma linha por print: nome | link direto (em carrossel, use `?img_index=N`; em reel, o segundo do vídeo) | o que mostra e por que importa.
```

---

## Rodada 4A: Perfis de investimentos e quant

```
Abra estes perfis do Instagram, um por vez:

Quant / trading sistemático:
1. https://www.instagram.com/tradionquant/ (já analisados: DfVf0L-AIkP, DfoRErMChB-, DftZ6l2CC_e)

Educação em investimentos (internacional):
2. https://www.instagram.com/brianferoldi/
3. https://www.instagram.com/humphreytalks/

Educação financeira e economia (Brasil):
4. https://www.instagram.com/econoweek/
5. https://www.instagram.com/academiadevalor/
6. https://www.instagram.com/guiainvest/
7. https://www.instagram.com/boletinhos/

Para cada perfil:
1. Verifique se existe e se está ativo: número de seguidores e data do último post. Se não existir ou não postar há mais de 6 meses, escreva só "INATIVO: <motivo>" e passe para o próximo.
2. Escreva 2–3 linhas sobre o perfil: tema, estilo, tipo de conteúdo; diga se vende curso/sinal/produto financeiro e se mostra dados/testes ou só opinião.
3. Liste os 10 posts mais recentes ainda não analisados com: link, tipo (carrossel/reel), resumo de 1 linha e tema.
4. Escolha os 3 posts mais úteis para quem quer validar estratégias com dados e analise cada um neste formato (em carrosséis, avance por TODOS os slides; em reels, assista até o fim):

### <ID do post> — @<autor>
- Tipo: carrossel (N slides) | reel
- Tema: backtest/validação | risco e drawdown | estatística | valuation/fundamentos | carreira | finanças pessoais | opinião/mercado
- Legenda: <texto completo da legenda>
- Slide a slide: <para cada slide: todo o texto visível, números, gráficos (eixos, valores), fórmulas e tabelas>
- Regras/lições práticas: <lista objetiva do que o post ensina>
- Evidência: <o post mostra dados, teste ou fonte? qual?>

No final, dê uma nota de 1 a 5 para cada perfil como fonte de aprendizado QUANTITATIVO (rigor, dados, transparência), com uma frase de justificativa.

Não comente, não curta e não siga ninguém; apenas leia.

AO FINAL DA RODADA, gere o arquivo `rodada-4A.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas com os principais aprendizados da rodada;
   - depois, TODOS os blocos e listas desta rodada;
   - no fim, uma seção "Prints".
2. Prints: tire print só dos slides ou frames com algo visual importante (layout, paleta, gráfico, antes/depois, curva de animação, tabela de números), no máximo 3 por post. Nomeie cada um como `<ID>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-4A.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-4A.md` num ÚNICO bloco de código Markdown. Na seção "Prints", ponha uma linha por print: nome | link direto (em carrossel, use `?img_index=N`; em reel, o segundo do vídeo) | o que mostra e por que importa.
```

---

## Rodada 4B: Descoberta de perfis quant

```
Objetivo: encontrar perfis do Instagram que ensinam trading quantitativo, backtest, estatística de mercado e gestão de risco COM DADOS.

1. Abra https://www.instagram.com/tradionquant/ e https://www.instagram.com/rational_edge/. Em cada um, abra "Contas sugeridas"/"Perfis parecidos" (seta ao lado do botão Seguir) e anote os perfis listados.
2. Pesquise as hashtags #quanttrading, #algotrading, #backtesting, #quantfinance e #tradingsistematico. Anote os perfis que aparecem com conteúdo educativo, ou seja, sem venda de sinais.
3. Desses perfis, monte uma lista com no máximo 10 candidatos. Descarte quem vende sinal, promete retorno, faz "copy trade", mostra "lifestyle" ou não posta há mais de 6 meses.
4. Para cada candidato: @handle, link, seguidores, data do último post, descrição de 1 linha e nota de 1 a 5 de rigor quantitativo.
5. Para os 3 melhores, analise os 2 posts mais úteis de cada um neste formato:

### <ID do post> — @<autor>
- Tipo: carrossel (N slides) | reel
- Tema: backtest/validação | risco e drawdown | estatística | valuation/fundamentos | carreira | finanças pessoais | opinião/mercado
- Legenda: <texto completo da legenda>
- Slide a slide: <para cada slide: todo o texto visível, números, gráficos (eixos, valores), fórmulas e tabelas>
- Regras/lições práticas: <lista objetiva do que o post ensina>
- Evidência: <o post mostra dados, teste ou fonte? qual?>

Não comente, não curta e não siga ninguém; apenas leia.

AO FINAL DA RODADA, gere o arquivo `rodada-4B.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas com os principais aprendizados da rodada;
   - depois, TODOS os blocos e listas desta rodada;
   - no fim, uma seção "Prints".
2. Prints: tire print só dos slides ou frames com algo visual importante (layout, paleta, gráfico, antes/depois, curva de animação, tabela de números), no máximo 3 por post. Nomeie cada um como `<ID>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-4B.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-4B.md` num ÚNICO bloco de código Markdown. Na seção "Prints", ponha uma linha por print: nome | link direto (em carrossel, use `?img_index=N`; em reel, o segundo do vídeo) | o que mostra e por que importa.
```
