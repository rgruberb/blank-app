# Leis de UX: 24 leis demonstradas lado a lado

Fontes: série "UX laws in action" de @motion_ui_interface, em 4 partes. Esta skill tem 3 delas:
- Parte 1: `Dd25eCoBJGr` (Fitts, Hick, Chunking, Doherty, Proximity, Von Restorff)
- Parte 2: `Dd4UtBDBsIS` (Goal gradient, Postel, Tesler, Similarity, Serial position, Peak-end)
- Parte 4: `Del7XTgsuwI` (Closure, Figure-ground, Banner blindness, Parkinson, Connectedness, Choice overload)
- A parte 3 não está entre as fontes. O reel final fala em "24 UX laws in four parts".

Formato de cada entrada: **definição** · **falha típica (lado "antes")** · **correção (lado "depois")** · **número mostrado** · **regra**.
Os números foram tirados da legenda, da transcrição e dos frames. Todos são demonstrações dos reels, não benchmarks universais.

## Parte 1 (Dd25eCoBJGr)

| # | Lei | Definição | Falha típica | Correção | Número | Regra |
|---|---|---|---|---|---|---|
| 1 | **Fitts's law** | Alvo pequeno e distante é lento | Link minúsculo no canto ("small + far"): precisa de 2 correções de cursor | Botão grande perto do conteúdo ("big + close"): acerta em 1 movimento | **0.66s vs 0.28s** (card "Aurora Speaker $249") | Faça a ação principal grande e próxima |
| 2 | **Hick's law** | Cada opção adiciona tempo de decisão | Grade de 12 apps em "Share to" | 4 apps + botão "More" | **0.74s vs 0.46s** | Mostre as poucas que importam e esconda o resto |
| 3 | **Chunking** | A memória de trabalho guarda ~4 chunks, não 7 | Telefone digitado como `4155550123` (10 dígitos soltos) | `415 555 0123` (3 grupos) | **6 perdidos vs todos mantidos** | Agrupe o que a pessoa precisa lembrar |
| 4 | **Doherty threshold** | Abaixo de 400ms a resposta parece instantânea; silêncio parece botão quebrado | Botão "Save changes" fica mudo até terminar | Botão responde na hora ("Saving…" → "Saved") mesmo com o trabalho lento | Ambos salvam em **1.2s**; feedback em **0.98s vs 0.10s** (frames) | Responda em até 400ms, mesmo quando o trabalho é lento |
| 5 | **Proximity** | O olho agrupa o que está perto antes de ler | Espaços iguais deixam o label "flutuando" entre dois campos (1:1) | **8px** até o próprio campo e **24px** até o próximo (1:3) | **1:1 vs 1:3** | Mantenha o label mais perto do próprio campo |
| 6 | **Von Restorff** | O diferente é notado | 3 planos idênticos ($9 / $19 / $49) | Um plano destacado ($19, elevado e com cor) | — | Um destaque, nunca três |

## Parte 2 (Dd4UtBDBsIS)

| # | Lei | Definição | Falha típica | Correção | Número | Regra |
|---|---|---|---|---|---|---|
| 1 | **Goal gradient** | As pessoas aceleram perto da linha de chegada | Cartão fidelidade de 8 carimbos, todos vazios | Cartão de 10 com 2 já dados (os mesmos 8 faltando) | **19% vs 34%** completaram | Nunca comece o progresso do zero |
| 2 | **Postel's law** | Seja generoso no que aceita | Campo de telefone estrito rejeita formatos reais | Campo tolerante remove espaços e traços | **1 de 4 vs 4 de 4** inputs aceitos | Aceite qualquer formato e limpe depois |
| 3 | **Tesler's law** | A complexidade não some, ela só muda de lugar | Usuário digita street, city, state e zip | Pede o ZIP primeiro e preenche city e state | **31 vs 16 teclas** | Deixe o sistema carregar o trabalho |
| 4 | **Similarity** | Coisas parecidas parecem funcionar igual | Linhas de settings todas iguais: 3 tocáveis escondidas | Chevron nas linhas que abrem algo | **3 escondidas vs 0** | Faça o que é tocável parecer tocável |
| 5 | **Serial position** | Lembramos melhor o primeiro e o último itens | Ação-chave no meio da tab bar, no "vale" da curva | Ação movida para o fim, no pico | gráfico em U | Coloque ações-chave no início ou no fim |
| 6 | **Peak-end rule** | Julgamos pela melhor parte e pelo final | Recibo "Payment received" sem graça | Final caloroso ("You're all set!") | Memória **4.5/10 vs 8/10** | Desenhe a última tela de propósito |

## Parte 4 (Del7XTgsuwI)

| # | Lei | Definição | Falha típica | Correção | Número | Regra |
|---|---|---|---|---|---|---|
| 1 | **Closure** | O olho completa formas cortadas | 2 cards que cabem exatos na tela parecem o conjunto todo | Deixe aparecer **32%** do próximo card | **0% vs 32%** visível | Deixe o próximo card espiar |
| 2 | **Figure-ground** | O olho separa a tela em frente e fundo | Dialog "Delete 3 photos?" sem backdrop; a página atrás compete | Backdrop escurece a página (~70% no frame) | Contraste do fundo **17.4:1 → 2.5:1** | Escureça o que está atrás do foco |
| 3 | **Banner blindness** | As pessoas pulam tudo que parece anúncio | Aviso "Card expires Friday" num banner chamativo | Aviso dentro do feed, com estilo de conteúdo | **0 vs 2 olhadas** | Não deixe o importante parecer anúncio |
| 4 | **Parkinson's law** | A tarefa cresce até ocupar o tempo dado, então encolha a tarefa | Endereço completo digitado | Postcode + toque no endereço | **30 vs 7 teclas** | Preencha o que você já sabe |
| 5 | **Uniform connectedness** | Itens unidos por uma linha viram um grupo | 4 círculos soltos no checkout (Cart, Ship, Pay, Done) | Uma linha liga os passos: início, fim e próximo passo | **4 grupos vs 1 grupo** | Conecte os passos de um fluxo |
| 6 | **Choice overload** | Muitas opções paralisam | Mesa com 24 geleias (estudo das geleias) | 6 geleias | **3% vs 30%** compraram | Mostre menos opções de início |

## Leis repetidas em outros reels
- **Hick's law em toolbar** (`DfreUkyBNQg`, @designmotionhq): "decision time grows with every doubling of options". O gráfico em degraus mostra 1→2→4→8. Uma barra com 12 ícones parece lenta; mantenha 4. Detalhes em `components-checklists.md`.
- **Fitts e tamanho de alvo**: veja os botões (44–48px) em `components-checklists.md`. Regras numéricas completas (44pt iOS, 48dp Android, web 24px mín. e meta 44, padding 20 + 12 + 12, 8px entre alvos) em `typography-and-touch.md` §1 (`DfwojjrirKz`, @designmotionhq).
- **Doherty na primeira tela** (`Dfy7ig_B-FL`, @theglidestudio): "uma página em branco por 2 s parece uma hora". Mostre o **título primeiro** e deixe o resto entrar depois; uma página que responde na hora parece uma empresa que responde. Reforça skeleton e SSR de `perceived-performance.md` (itens 01 e 20).
- **Uniform connectedness em pedido** (`DX_bA4rCWf0`, @ui.pixel): barra de 4 etapas nomeadas repetida na home e no detalhe do pedido. Ver `components-checklists.md` §10.
- **Serial position vs botão central da tab bar**: o padrão comum de botão circular no meio da tab bar (`DX_bA4rCWf0`) contradiz a regra "ação-chave no início ou no fim" da parte 2. Registro de divergência em `components-checklists.md` §10.
- **Von Restorff com um accent só** (`DXeeUP7FKGs`, `DVv7OOECewR`, `DfzgxEKlx8z`): nas três fontes o accent fica reservado ao estado ativo e ao CTA; o resto é neutro.
- **Hick no momento de decisão** (`DXeeUP7FKGs`, @rish_designs): só os sinais imediatos e contexto suficiente para agir. Ver `components-checklists.md` §9.
