# Prompts para a extensão Claude in Chrome

Mande uma rodada por vez no painel do Claude no Chrome, com o Instagram logado. Ao final de cada rodada a extensão gera o `rodada-<N>.md` com os achados e a lista de prints. Cole o resultado (e os prints, se baixou) na sessão das skills.

Ordem: 1 → 2 → 3A → 3B → 3C → 4A → 4B → 5 → 6 → 7 → 8A → 8B.

**Modelos:** use **Sonnet 5.5** como padrão (rápido e bom em ler slides) e **Opus 5.5** nas rodadas 4A e 4B, que pedem julgamento sobre rigor e conflito de interesse. Não use Haiku: ele pula slides e resume demais. Se uma resposta cortar no meio ou vier rasa, refaça só os links que falharam com o Opus 5.5. O modelo é escolhido no seletor da extensão.

---

## Rodada 1: Links 1 a 8

**Modelo:** Sonnet 5.5

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

**Modelo:** Sonnet 5.5

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

**Modelo:** Sonnet 5.5

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

**Modelo:** Sonnet 5.5 (troque para Opus 5.5 se as notas vierem genéricas)

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

**Modelo:** Sonnet 5.5

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

**Modelo:** Opus 5.5 (avaliar rigor quantitativo e conflito de interesse)

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

Quant (novo):
8. https://www.instagram.com/quantstackai/

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

**Modelo:** Opus 5.5 (a extensão decide sozinha quem entra)

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

---

## Rodada 5: Novos carrosséis (18/11)

**Modelo:** Sonnet 5.5

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
https://www.instagram.com/p/De7NqmHkbzU/
https://www.instagram.com/p/DfFnuSOkqi9/
https://www.instagram.com/p/Dfr5It0xAzA/
https://www.instagram.com/p/DfztwFuxh4f/
https://www.instagram.com/p/Dfr6X8qFPwC/
https://www.instagram.com/p/De_J0aOl9SJ/
https://www.instagram.com/p/Df1eAHODjT9/
https://www.instagram.com/p/DfKaOBqjUr4/
https://www.instagram.com/p/Dfo__tSjk9k/

Não comente, não curta e não siga ninguém; apenas leia.

AO FINAL DA RODADA, gere o arquivo `rodada-5.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas com os principais aprendizados da rodada;
   - depois, TODOS os blocos e listas desta rodada;
   - no fim, uma seção "Prints".
2. Prints: tire print só dos slides ou frames com algo visual importante (layout, paleta, gráfico, antes/depois, curva de animação, tabela de números), no máximo 3 por post. Nomeie cada um como `<ID>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-5.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-5.md` num ÚNICO bloco de código Markdown. Na seção "Prints", ponha uma linha por print: nome | link direto (em carrossel, use `?img_index=N`; em reel, o segundo do vídeo) | o que mostra e por que importa.
```

---

## Rodada 6: Vídeos do Facebook

**Modelo:** Sonnet 5.5

```
Abra cada link abaixo no Facebook, um por vez (são vídeos/reels). Assista cada um até o fim, com o som ligado se houver narração.

Para cada link, gere um bloco Markdown neste formato:

### <ID ou título> — <autor/página>
- Tipo: reel | vídeo | post
- Tema: design visual | UI/motion | UX | dashboard | investimentos | outro
- Legenda: <texto completo da legenda>
- Narração/fala: <resumo fiel do que é dito, com os números e termos citados>
- Cena a cena: <o que aparece na tela em ordem: textos, números, cores (hex aproximado), layout, componentes, animações>
- Regras/lições práticas: <lista objetiva do que o vídeo ensina>

Links:
https://www.facebook.com/share/r/1CTThcky5H/
https://www.facebook.com/share/1AE3r4BKt6/
https://www.facebook.com/share/r/1A3pMvMBW2/
https://www.facebook.com/share/v/1cLd9NchWN/

Não comente, não reaja e não siga ninguém; apenas assista e leia.

AO FINAL DA RODADA, gere o arquivo `rodada-6.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas com os principais aprendizados da rodada;
   - depois, TODOS os blocos e listas desta rodada;
   - no fim, uma seção "Prints".
2. Prints: tire print só dos slides ou frames com algo visual importante (layout, paleta, gráfico, antes/depois, curva de animação, tabela de números), no máximo 3 por post. Nomeie cada um como `<ID>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-6.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-6.md` num ÚNICO bloco de código Markdown. Na seção "Prints", ponha uma linha por print: nome | link direto (em carrossel, use `?img_index=N`; em reel, o segundo do vídeo) | o que mostra e por que importa.
```

---

## Rodada 7: Novos perfis de UI e dashboards

**Modelo:** Sonnet 5.5

```
Abra estes perfis do Instagram, um por vez. Pule os posts listados como "já analisados".

1. https://www.instagram.com/felvrabr/ (já analisados: Dfui4V5BMbz, DfpCOjIB1Rb, Dfr9S5yhlvX)
2. https://www.instagram.com/shohan.designs/ (nenhum analisado ainda)
3. https://www.instagram.com/code_and_chill/ (confira se é o mesmo criador de @_code_and_chill_; se for, pule estes: DbfG6fuPE9y, De12lc1vUmr, Deoi1WhP83h, DfCWtPgPcfP, DffBnb2vlUn, DfkNvnePItL, DfrqAX9v59S, DfXoXVFPBfd, DfeT74YvQaD, Dfct0mNvg3f)

Para cada perfil:
1. Verifique se existe e se está ativo: número de seguidores e data do último post. Se não existir ou não postar há mais de 6 meses, escreva só "INATIVO: <motivo>" e passe para o próximo.
2. Escreva 2–3 linhas sobre o perfil: tema principal, estilo visual, tipo de conteúdo e qualidade (dicas concretas vs. só inspiração).
3. Liste os 10 posts mais recentes ainda não analisados com: link, tipo (carrossel/reel), resumo de 1 linha e tema.
4. Escolha os 3 posts mais úteis e analise cada um neste formato (em carrosséis, avance por TODOS os slides; em reels, assista até o fim). Dê preferência a posts com GAMIFICAÇÃO (progresso, níveis, pontos, badges, streaks, rankings, metas, recompensas) em painéis de gestor ou de cliente:

### <ID do post> — @<autor>
- Tipo: carrossel (N slides) | reel
- Tema: design visual | UI/motion | UX | dashboard | investimentos | outro
- Legenda: <texto completo da legenda>
- Slide a slide: <para cada slide: todo o texto visível, números, cores (hex aproximado), fontes, layout e componentes mostrados>
- Regras/lições práticas: <lista objetiva do que o post ensina>

No final, dê uma nota de 1 a 5 para cada perfil como fonte de aprendizado de UI/UX, com uma frase de justificativa.

Não comente, não curta e não siga ninguém; apenas leia.

AO FINAL DA RODADA, gere o arquivo `rodada-7.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas com os principais aprendizados da rodada;
   - depois, TODOS os blocos e listas desta rodada;
   - no fim, uma seção "Prints".
2. Prints: tire print só dos slides ou frames com algo visual importante (layout, paleta, gráfico, antes/depois, curva de animação, tabela de números), no máximo 3 por post. Nomeie cada um como `<ID>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-7.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-7.md` num ÚNICO bloco de código Markdown. Na seção "Prints", ponha uma linha por print: nome | link direto (em carrossel, use `?img_index=N`; em reel, o segundo do vídeo) | o que mostra e por que importa.
```

---

## Rodada 8A: Novos links de design (18–21/11)

**Modelo:** Sonnet 5.5

```
Abra cada link abaixo no Instagram, um por vez. Em carrosséis, avance por TODOS os slides; em reels, assista até o fim.

FILTRO DE DESIGN (obrigatório): só analise posts sobre design de interface: UI, UX, motion, dashboards, apps, sites, design visual, tipografia, cor, componentes ou ferramentas de design. Se um link NÃO for de design (investimento, trading, finanças pessoais, lifestyle, humor, propaganda sem tela de produto), escreva só "FORA DO TEMA: <ID> — <assunto em 1 linha>" e passe para o próximo. Um app de cripto ou finanças conta como design SÓ se o post mostrar as telas e explicar decisões de interface.

Para cada link de design, gere um bloco Markdown neste formato:

### <ID do post> — @<autor>
- Tipo: carrossel (N slides) | reel
- Tema: design visual | UI/motion | UX | dashboard | investimentos | outro
- Legenda: <texto completo da legenda>
- Slide a slide: <para cada slide: todo o texto visível, números, cores (hex aproximado), fontes, layout e componentes mostrados>
- Regras/lições práticas: <lista objetiva do que o post ensina>
- Plataforma: website | app desktop/web app | app mobile | outro

Links:
https://www.instagram.com/reel/Df4ZOofhX_s/
https://www.instagram.com/reel/Df4FMmPBbM5/
https://www.instagram.com/reel/DfNKemOBLZx/
https://www.instagram.com/reel/Df2Vqx0S48U/
https://www.instagram.com/p/DfPzX1JlJHz/
https://www.instagram.com/p/Dfg5mkYDluh/
https://www.instagram.com/p/Df3y6C7jmyA/
https://www.instagram.com/p/DfxHmxAjjkn/
https://www.instagram.com/p/Df7XGzblNVX/
https://www.instagram.com/p/Df7OIz4kpet/
https://www.instagram.com/p/Df98Kn-EeH9/
https://www.instagram.com/p/Df97ZX9liyl/
https://www.instagram.com/p/DgAbYyRkZhC/
https://www.instagram.com/p/DfSlTkciSbg/

Não comente, não curta e não siga ninguém; apenas leia.

AO FINAL DA RODADA, gere o arquivo `rodada-8A.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas com os principais aprendizados da rodada;
   - depois, TODOS os blocos e listas desta rodada;
   - no fim, uma seção "Prints".
2. Prints: tire print só dos slides ou frames com algo visual importante (layout, paleta, gráfico, antes/depois, curva de animação, tabela de números), no máximo 3 por post. Nomeie cada um como `<ID>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-8A.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-8A.md` num ÚNICO bloco de código Markdown. Na seção "Prints", ponha uma linha por print: nome | link direto (em carrossel, use `?img_index=N`; em reel, o segundo do vídeo) | o que mostra e por que importa.
```

---

## Rodada 8B: Novos perfis de design

**Modelo:** Sonnet 5.5

```
Abra estes perfis do Instagram, um por vez. Pule os posts listados como "já analisados".

1. https://www.instagram.com/ui.iliasmiah000/ (já analisados: DfV39ohhwAC, Df4ZOofhX_s, DfNKemOBLZx)
2. https://www.instagram.com/juicelab.uiux/ (já analisados: Df7OIz4kpet)
3. https://www.instagram.com/arounda.agency/ (já analisados: Df97ZX9liyl)
4. https://www.instagram.com/orbixdashboard/ (já analisados: Dfus5sWFAov, DfPzX1JlJHz)
5. https://www.instagram.com/viralapplaunch/ (já analisados: DfSlTkciSbg)

FILTRO DE DESIGN (obrigatório): só analise posts sobre design de interface: UI, UX, motion, dashboards, apps, sites, design visual, tipografia, cor, componentes ou ferramentas de design. Se um link NÃO for de design (investimento, trading, finanças pessoais, lifestyle, humor, propaganda sem tela de produto), escreva só "FORA DO TEMA: <ID> — <assunto em 1 linha>" e passe para o próximo. Um app de cripto ou finanças conta como design SÓ se o post mostrar as telas e explicar decisões de interface.

Para cada perfil:
1. Verifique se existe e se está ativo: número de seguidores e data do último post. Se não existir ou não postar há mais de 6 meses, escreva só "INATIVO: <motivo>" e passe para o próximo.
2. Escreva 2–3 linhas sobre o perfil: tema principal, estilo visual, tipo de conteúdo e qualidade (decisões de design explicadas com números vs. só inspiração). Diga se o perfil é majoritariamente de design; se não for, marque "PERFIL FORA DO TEMA" e não analise posts.
3. Liste os 10 posts mais recentes ainda não analisados com: link, tipo (carrossel/reel), resumo de 1 linha e tema.
4. Escolha os 3 posts de design mais úteis e analise cada um neste formato (em carrosséis, avance por TODOS os slides; em reels, assista até o fim):

### <ID do post> — @<autor>
- Tipo: carrossel (N slides) | reel
- Tema: design visual | UI/motion | UX | dashboard | investimentos | outro
- Legenda: <texto completo da legenda>
- Slide a slide: <para cada slide: todo o texto visível, números, cores (hex aproximado), fontes, layout e componentes mostrados>
- Regras/lições práticas: <lista objetiva do que o post ensina>
- Plataforma: website | app desktop/web app | app mobile | outro

No final, dê uma nota de 1 a 5 para cada perfil como fonte de aprendizado de UI/UX, com uma frase de justificativa.

Não comente, não curta e não siga ninguém; apenas leia.

AO FINAL DA RODADA, gere o arquivo `rodada-8B.md`:
1. Conteúdo:
   - no topo, um resumo de 5 a 10 linhas com os principais aprendizados da rodada;
   - depois, TODOS os blocos e listas desta rodada;
   - no fim, uma seção "Prints".
2. Prints: tire print só dos slides ou frames com algo visual importante (layout, paleta, gráfico, antes/depois, curva de animação, tabela de números), no máximo 3 por post. Nomeie cada um como `<ID>_<n>.png`.
3. Entrega:
   - Se você conseguir baixar arquivos, baixe o `rodada-8B.md` e os prints.
   - Se não conseguir, entregue o conteúdo completo do `rodada-8B.md` num ÚNICO bloco de código Markdown. Na seção "Prints", ponha uma linha por print: nome | link direto (em carrossel, use `?img_index=N`; em reel, o segundo do vídeo) | o que mostra e por que importa.
```
