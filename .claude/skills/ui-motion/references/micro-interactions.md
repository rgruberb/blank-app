# Catálogo de micro-interações

Valores das fontes (legenda, transcrição ou texto na tela das folhas de contato). "Tela" = valor lido no frame do vídeo. "(complemento)" = boa prática geral, não vem das fontes.
Os reels de @motion_ui_interface mostram cada interação a 1× e a ¼ de velocidade, com o gráfico da curva abaixo.

## 1. Detalhes invisíveis do iPhone — De4B0UxPXIk
| # | Detalhe | Valores | Por que funciona |
|---|---|---|---|
| 1 | Press feedback | encolhe no toque, **0 ms** (o "sem" espera o release, **120 ms**) | o dedo recebe resposta antes de levantar |
| 2 | Springs | **damping 0.8, overshoot 1.5%**, depois assenta; o "sem" é linear, **300 ms**, para seco | objetos reais se movem assim |
| 3 | Momentum | flick desliza **1000 px** após soltar, desacelera ~0,2%/ms (tela: "rate 0.998") | sensação de empurrar algo com peso |
| 4 | Rubber band | puxão de **200 px estica 86 px**, volta com spring | a elasticidade avisa que é o fim da lista |
| 5 | Interruptível | inverte no meio do movimento, **0 ms** de espera (o "sem" espera **180 ms**) | ninguém espera animação terminar |
| 6 | Cantos contínuos | curva entra gradualmente (squircle), sem "círculo colado na reta" | você não nomeia, mas percebe |

## 2. Apps premium — DfP6EoLBtgg
| Interação | Valores | Por que |
|---|---|---|
| Button press | afunda para **95%**, volta com spring (curva: queda, overshoot, assenta) | o "squish" confirma que o toque pegou |
| Pull to refresh | dedo **100%** → lista **35%** (curva sublinear vs. linha diagonal do dedo) | resistência parece física |
| Rolling number | dígitos rolam um após o outro, **100 ms** de intervalo; curva com leve overshoot | o olho vê a mudança em vez de perdê-la |
| Drag to reorder | item sobe e cresce para **105%**, os outros deslizam (**200 ms**, tela) | parece mover um cartão real |
| Card expand | **ease-out 350 ms** (rápido → devagar; gráfico compara com linear) | chega rápido e pousa suave |
| Success tick | primeiro desenha o círculo, depois o tick, **470 ms** (curva S) | ver terminar faz o momento parecer concluído |

## 3. Mais detalhes — DfTr-mwhZT3
| Interação | Valores | Por que |
|---|---|---|
| Add to cart | item voa em **arco** até o carrinho, **500 ms**, badge pula (+1) | você vê para onde foi |
| Submit button | pílula → spinner → tick, uma forma só (**260 → 64 px**, **270 ms** na tela) | o olho nunca perde o objeto |
| List load | linhas chegam **70 ms** separadas | cascata parece rápida e calma |
| Swipe away | segue o dedo, inclina **12°**, sai com velocidade (flick) | como um cartão na mão |
| Card flip | gira **180°**, sobe **8%** no meio do giro (curva S) | profundidade = físico |
| Notification bell | balança **±24°**, oscilação amortecida, assenta em **760 ms**; badge entra com pop | chama atenção sem irritar |

## 4. Mais detalhes — DfWjKQPhUbn
| Interação | Valores | Por que |
|---|---|---|
| Speed dial (FAB) | "+" gira **45°** e vira "×"; ações abrem em leque/arco **100 ms** separadas | "fan out, don't pop" |
| Slider | thumb cresce **40%** (tela: 140%) ao agarrar; bolha de valor segue com atraso e alcança | "grow when grabbed" |
| Large title | encolhe **34 → 18 px** para a top bar, **ligado ao scroll** | você sempre sabe onde está |
| Long press | linha afunda durante **400 ms** de hold, depois sobe **5%**, resto da tela escurece | dá tempo de cancelar e confirma o modo |
| Page dots | borda da frente sai primeiro, a de trás segue (**130 ms** de diferença, tela): o dot estica e "snapa" | movimento elástico, contínuo |
| Side menu | página encolhe para **86%** e desliza **150 px**; menu fica por baixo | "push, don't cover" |

## 5. Mais detalhes — DfZkZZ4hkuV
| Interação | Valores | Por que |
|---|---|---|
| Star rating | estrelas preenchem **100 ms** separadas, cada uma com pop (overshoot) | preenche em sequência, não de uma vez |
| One-time code | dígitos caem **70 ms** separados, caixas acendem em onda | "drop in, then glow" = funcionou |
| Accordion | seta gira **180°**, painel abre (**62 px** na tela), linhas abaixo deslizam | abrir espaço em vez de pular |
| Password strength | medidor enche enquanto digita, **4 segmentos**, vermelho → azul | você sabe antes de enviar |
| To-do | check desenha, linha risca, item afunda para o fim, **470 ms** | sai do caminho |
| Reactions | emojis aparecem **70 ms** separados; o escolhido cresce **1,6×** e voa até a mensagem | "pop, grow, fly" |

## 6. Mais detalhes — DfcwOHLh76I
| Interação | Valores | Por que |
|---|---|---|
| Copy button | ícone morfa em check, label vira "Copied", botão alarga **36 px** | morph, não swap |
| Text field | placeholder flutua e vira label (**20 → 14 px**, tela), linha cresce do centro | "float, don't vanish" |
| Checkout steps | check desenha, linha enche em **400 ms**, próximo dot pulsa | progressão legível |
| Map pin | cai em **200 ms**, quica **2 vezes**, achata no impacto, ondas se espalham | peso + localização |
| Delete | linha encolhe e voa para a lixeira em **400 ms**, tampa fecha, lista fecha o vão | o item foi para algum lugar |
| Photo viewer | segue o dedo **1:1** para baixo e encolhe; ao soltar volta (spring) para a thumbnail | "follow, then return" |

## 7. Ícones que morfam — DfVOGNnzR_D ("icons should move, not swap")
| Ícone | Valores |
|---|---|
| Play / pause | triângulo se divide em 2 barras, **300 ms** |
| Download | seta cai → anel enche (0–100%) → tick, **1,2 s** |
| Tema claro/escuro | **8 raios** retraem um a um, sombra "esculpe" a lua, **600 ms** (tela) |
| Search | círculo se "desdesenha" e o cabo gira até virar X, **400 ms** |
| Send | avião sai em curva (**400 ms**, tela) e um novo entra com spring |
| Unlock | haste sobe (**+18 px**, tela) com **34% de overshoot** e abre |

## 8. Detalhes visuais "caros" do iPhone — Dflzxq5Bqfj
1. **Vidro fosco**: blur, não bloqueie — **30 px** de blur atrás da tab bar.
2. **Cantos concêntricos**: raio interno = externo − padding (**36 − 12 = 24**).
3. **Centro óptico**: centralize pelo olho — ícone play deslocado **+11 px**.
4. **Tipo grande apertado**: relógio com tracking **−6 px**.
5. **Ícones casados com o texto**: traço **2,4 px** (o "errado" mostra 1 px ao lado de texto bold).
6. **Dynamic Island**: alertas crescem da pílula — "morph, don't pop", **1 forma** que estica e assenta.

**Cartão premium em 6 camadas — DfRkH5LIHgZ (@motion_ui_interface, rodada 3A)**. Mesma ideia de "várias decisões pequenas empilhadas": base com gradiente de **3 paradas** (escuro → mais escuro) · padrão de ondas a **8%** de opacidade · conteúdo de 4 elementos numa **só borda esquerda** · rim light de **1 px a 28% branco** · **glare a 18% branco que acompanha a inclinação** (a única camada em movimento) · **duas sombras, 8 px + 30 px**. Para o glare (complemento): ligue a posição de um gradiente radial ao `pointermove`/giroscópio com spring, limite a inclinação a poucos graus e desligue em `prefers-reduced-motion` (ver também `ext-transitions-dev`, "card hover tilt").

## 9. Toasts — DXRpZTTMr9a (5 regras)
1. **Posição**: desktop canto inferior direito; mobile no topo; **nunca centralizado** (bloqueia o conteúdo).
2. **Timing**: info **4 s**, warning **7 s**, erro **até o usuário reconhecer**. Timer fixo é bug. (Tela mostra barra de progresso de tempo dentro do toast.)
3. **Stacking**: máx. **3 visíveis**; novos empurram os antigos com spring **damping 20, stiffness 180**.
4. **Sempre dispensável**: botão fechar, swipe no mobile, **pausa no hover**. Se não dá para escapar, é modal.
5. **Cor**: ícone + **borda esquerda colorida** por tipo; só tingir o fundo não basta — **6%** dos usuários não distinguem.

## 10. Drag-and-drop / upload — DZ2Dp5wt0pJ
- Drop zone responde **antes** do drop com **3 sinais**: borda, glow, mudança de copy ("Release to upload").
- **Progresso honesto**: % + tempo restante (tela: "70% · 6s left · 1.9 MB/s"), nunca só spinner.
- **Retry inline**: se morre em 90%, retoma de onde parou ("Resuming from 90%"), arquivo continua carregado.
- **Preview como prova**: thumbnail + tipo + tamanho, não só o nome.
- **Fila independente**: cada arquivo tem seu progresso e seu retry; uma falha não bloqueia os outros 9.
- **Tooltip de arraste com o resultado** (`Dfr4RMBlaPH`, @felvrabr, rodada 7): esticar uma reserva mostra "Drag to extend · 4 nights · 29 Dec → 2 Jan · $4,280" em tempo real. Regra de UX em `ux-patterns` (`components-checklists.md` §8). **(complemento)**: o tooltip segue o ponteiro 1:1 sem easing, o número troca sem animar a cada passo (só no drop use o número rolando) e a barra faz snap à célula com spring curto.

## 11. Tab bar líquida "Meniscus" — DbfG6fuPE9y (@_code_and_chill_)
"A aba ativa não desliza — a barra derrete em volta dela"; cada encaixe é resolvido por tangência para o líquido nunca vincar (HTML + CSS + JS). Nos frames:
- A aba ativa vira uma **"gota" (bead) circular que sobe acima da barra**, ligada a ela por um menisco suave; o rótulo aparece sob a gota.
- **Cada aba tem sua cor** (Home verde-limão, Messages laranja, Settings rosa) e um **glow difuso da mesma cor** sob a barra; o título grande da página troca junto (Home → Messages → Settings).
- Dá para **tocar** numa aba ou **arrastar a gota** ao longo da barra ("Tap a tab — or drag the bead along the bar"); durante o arraste a gota troca de cor ao passar pelas abas.
Use como referência de indicador de aba com morph/metaball. (Sem valores numéricos.)

## 12. Dashboard "Instrumental" com detalhe em spring — De1j52PFdpL (@moxen.studio)
Dashboard escuro de API ("Monitorea sin perder detalle"): medidores de linha, agulha (gauge), anel, ampulheta, histograma, com números ao vivo (1.112 → 1.195 req/s). Ao passar o mouse num gráfico aparece um tooltip; ao selecionar o painel "Peticiones por segundo" ele **cresce com spring** até ocupar um card maior, as barras ficam laranja, aparece um chip/tooltip laranja e o resto do dashboard **escurece**; depois volta ao grid. Exemplo de "foco" em data-viz: crescer + escurecer o resto (mesmo princípio do long press). (Sem valores; áudio irrelevante.)

## 13. Pílula de navegação que desliza — Code & Chill (@_code_and_chill_, Facebook, rodada 6)
Reels de ~5 s em loop (dashboards "SaaS revenue analytics" e "Private credit loan management"): a **pílula do item ativo desliza** na sidebar até o item clicado e a tela troca com uma **transição curta**; 4 telas em ~5 s (Funnels → Campaigns → Cohorts; Property → Portfolio → Risk). O painel de código mostra `slidePill(pill, target)` com `gsap.to(…, { ease: 'power3.out' })` (leitura aproximada; duração não legível). Os KPIs fazem contagem entre frames.
- Princípio: o indicador **viaja** de um item ao outro (mesma regra do "morph, não swap"); não some num e reaparece no outro.
- **(complemento)** Valores: 250–350 ms com ease-out forte (`power3.out` ≈ `cubic-bezier(0.22, 1, 0.36, 1)`), interrompível (clique no meio parte da posição atual), só `transform` (translate/scale da pílula, medidos com FLIP). Troca de conteúdo ≤ 200–300 ms com fade + deslocamento curto; em `prefers-reduced-motion` a pílula pula direto. Pronto: `ext-transitions-dev` ("sliding tabs", "segmented control") ou `PillNav` em `react-bits.md`. Indicador líquido alternativo: §11.

## 14. 19 regras de animação de UI — DgI3UF_k_-G (@samro_ai, rodada 10A)
Reel "19 UI animation rules that make apps feel expensive": cada regra é uma cena com **dois celulares lado a lado, sem × com a regra** (frame visto: "Exaggeration", princípio Disney, checkout). Só a legenda e 1 frame foram lidos; a lista completa das 19 **não foi verificada**.
- Fontes citadas na legenda: **Doherty** (responder em até **400 ms**, IBM 1982); a maior parte do motion de UI fica entre **100 e 500 ms** (NN/g); **se é usado ~100 vezes por dia, não anime** (Emil Kowalski); **9 das 19** vêm dos 12 princípios da Disney (*The Illusion of Life*, 1981).
- Encaixe nos tokens: press 160 ms, morph 300–400 ms, expand 350 ms e sucesso 470 ms estão dentro de 100–500 ms. Reveal (~700 ms) e cena (~1,2 s) ficam fora, mas são de site/troca de tela; **valem os tokens da skill** (a faixa é heurística, não teto). Ações de alta frequência (enviar mensagem, marcar tarefa, trocar aba em app de trabalho): só feedback de estado, sem coreografia — igual a `scroll-and-screen-transitions.md` §2 e à regra de frequência da Atlassian (< 150 ms, `official-motion-guidelines.md`).

## 15. "The ABC of UI" — 42 micro-interações — DgFUOPxtOJK (@anside_design, rodada 10A)
Grade 6×7 com nome padronizado por célula (print `DgFUOPxtOJK_1.jpg`; animação de cada célula não verificada). Use como **checklist de inventário** no passo 1 do workflow: quais destes o produto tem e qual padrão desta skill cobre cada um.
| Grupo (complemento) | Nomes da grade | Onde está o padrão |
|---|---|---|
| Controles | Toggle, Checkbox, Radio Group, Range Slider, Star Rating, Stepper, Tab Switch, Grid ↔ List, Day/Night | §2–5, `ext-transitions-dev` (toggle, checkbox, sliding tabs) |
| Botões e ações | Live Burst (curtir), Send Button, Ripple Tap, Copy, Trash, Unlock, Play/Pause, Menu → Close | §1–2, §7 (morph) |
| Espera e progresso | Spinner, Progress Bar, Progress Ring, Dot Loader, Skeleton, Charging, Connecting, Equalizer | `loaders-and-refresh.md` |
| Arquivos | Download, Upload, Open Folder, Doc Preview | §10 |
| Superfícies | Accordion, Modal Pop, Toast, Notification, Card Flip, Carousel, Search Expand | §9, `page-transitions-and-timing.md` |
| Listas | Drag to Sort, Swipe Delete, Avatar Stack | §2, §16, `css-recipes.md` §10 |
| Texto e dados | Typing…, Float Label, Bar Chart | §5, §17 |
Lição da legenda: "ninguém nota o detalhe bem feito; sem ele o produto inteiro parece chapado". Não é licença para animar tudo: a regra de **um momento animado por página** continua valendo (o resto é feedback funcional).

## 16. Linhas arrastáveis — DgM5twdsInO (@theglidestudio, rodada 10A)
"Nada diz que elas se movem, então ninguém tenta." Três correções na mesma lista (frame: lista "Today" com alças à direita): **(1) mostre uma alça**, **(2) erga a linha** ao pegar, **(3) abra um espaço** onde ela vai cair. Reforça os tokens já existentes: lift **105%** e os outros abrindo espaço em **200 ms** (`css-recipes.md` §10). Desktop: alça aparece no hover e o cursor vira `grab` (complemento).

## 17. Texto animado: 6 formas — DgQYY6OpZMB (@ale.uiux, rodada 10A)
Regra da legenda: **cada animação de texto dura menos de 1 s**, para não atrasar a leitura.
| Forma | Contexto citado |
|---|---|
| Typewriter | notas e busca |
| Word stream | resposta de chat de IA (`ext-transitions-dev`: "streaming text") |
| Scramble | senhas e códigos |
| Retype | hero de landing (conta como o momento animado da página) |
| Typing dots | "digitando…" em chat |
| Letter rise | título de boas-vindas |
(complemento) Em `prefers-reduced-motion`, mostre o texto inteiro de uma vez; leitores de tela recebem o texto final, não as letras (`aria-live="polite"` só no resultado).

## 18. Componentes "com física" — The Kitchen (Df5J3c6EabL, @samro_ai sobre a biblioteca de dqnamo, rodada 10A)
Grade vista: Cassette Button, Scramble Text, Hold-to-delete, Cassette Player (carretéis girando), Hold to Confirm, Drum Zone, e um checkout que "imprime" um recibo. Código em cada página; a legenda oferece uma skill do Claude por DM (não verificada). Lições: **ação destrutiva com segurar para confirmar** (igual ao "hold to publish" de `react-bits.md`); personalidade física vale em **um** componente de destaque, não no produto inteiro. Biblioteca não instalada nem auditada.
