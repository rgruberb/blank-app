# Transições de página, duração e curvas

## Quanto tempo deve durar — Dfvja0XCyIi (@theglidestudio)
"Esta animação está um segundo longa demais." Velocidade é metade de como o motion é sentido.
- **Lenta demais** → você espera o site "se exibir" (tela: menu abrindo em **2,4 s**).
- **Rápida demais** → você nunca vê de onde as coisas vieram (tela: **0,1 s**).
- **Regra** (tela): **Press 0,16 s · Reveal 0,7 s · Scene 1,2 s**. "Um press leva um piscar, um reveal menos de um segundo, uma cena completa pouco mais de um."
- "Bom motion nunca é algo que você espera. Acaba exatamente quando você o percebe."

Outras durações das fontes: card expand 350 ms; success 470 ms; add to cart 500 ms; bell 760 ms; download icon 1,2 s; ícones 300–600 ms; checkout line 400 ms; map pin 200 ms para pousar.
Interação contínua (arrastar, scroll, pull) **não tem duração**: segue o dedo 1:1 (photo viewer) ou com resistência (35%), e só a soltura usa spring.

## Easing vs. spring
- **Ease-out** (rápido → devagar) para algo que entra/expande: card expand 350 ms (DfP6EoLBtgg mostra a curva contra a linear).
- **S-curve / ease-in-out** para coisas que vão de um estado a outro inteiro: card flip 180°, success tick, checkout line (curvas S nas telas).
- **Spring com overshoot** para respostas físicas: press (95% → 100% passando um pouco), estrelas com pop, unlock (34% overshoot), números rolando.
- **Spring subamortecido (oscilante)** só para chamar atenção: sino ±24° assentando em 760 ms; map pin com 2 quiques.
- iOS: damping 0.8 → **~1.5% de overshoot** (De4B0UxPXIk). Toasts: **stiffness 180, damping 20** (DXRpZTTMr9a).
- Linear: só para progresso mecânico ou loops (spinner). Movimento de UI linear "para seco como máquina" (o "sem" do reel: linear 300 ms).

## Card → página (shared element) — DfwhC1riuuO (@theglidestudio)
"Você toca num card. Para onde foi a página?" Um corte seco obriga a pessoa a se reencontrar.
1. **O card vira a página**: a imagem do card cresce até ser o hero da página de detalhe (tela: o anel "Halo" do grid vira o topo da página de produto).
2. **Voltar volta**: a página encolhe exatamente para a posição de origem no grid.
3. **Menus começam no botão**: o menu nasce do botão hambúrguer que o abriu.
"Nada simplesmente aparece. Tudo na tela veio de algum lugar."
Implementação: View Transitions API (`view-transition-name` igual no card e no hero) ou FLIP — ver `css-recipes.md`. Duração alvo: um reveal (~350–700 ms).

## Outros padrões de navegação
- **Side menu** (DfWjKQPhUbn): página encolhe para **86%** e desliza **150 px**; o menu fica embaixo — "push, don't cover".
- **Large title** (DfWjKQPhUbn): **34 → 18 px** ligado ao scroll, encolhe para a top bar em vez de sumir.
- **Dynamic Island** (Dflzxq5Bqfj): alertas crescem da pílula — morph, don't pop.
- **Interrupção** (De4B0UxPXIk): toda transição de painel/rota precisa poder reverter no meio (0 ms de espera vs 180 ms).

## Reduced motion (complemento)
Com `prefers-reduced-motion: reduce`: substitua zoom/slide/shared element por crossfade ≤ 150 ms ou corte; remova parallax, bounce e oscilação; mantenha mudanças de estado visíveis (cor, ícone, texto) e progresso.
