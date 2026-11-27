# Checklists por componente

Cada item traz a regra, os números da fonte e o "antes → depois" que aparece nos frames.

---

## 1. Botão primário: 6 decisões (`Ddy5RJOha1U`, @motion_ui_interface)
O exemplo é sempre "Add to cart". As seis decisões não envolvem a cor.

| # | Decisão | Antes | Depois / regra |
|---|---|---|---|
| 1 | **Size** | 40px: o polegar erra, e padding fino parece descuido | **48px** de altura e **24px** de padding lateral. Mínimo **44px**, alvo 48 |
| 2 | **Label** | 14px, peso medium, afunda no fill; "OK"/"Submit" | **Semibold, sentence case** (sem CAPS); a fonte usa 17px, que cai fora da escala 1,2: use 16 ou 19 (`typography-and-touch.md` §2). **Verbo + objeto** ("Add to cart"). O label diz o que acontece em seguida |
| 3 | **Contrast** | Fill cinza chapado a **1.6:1** contra a página: sem borda, some | Fill com gradiente "satin", rim de 1px a **4:1**, label branco a **14:1**. Regra: **label ≥ 4.5:1, borda ≥ 3:1** |
| 4 | **Depth** | Fill chapado parece impresso, não clicável | Recessed track, borda superior iluminada, sombra **8px abaixo, 24 de blur**. "Light from above, shadow falls down" |
| 5 | **Detail** | Cantos vivos brigam com as letras redondas; label sem pista | Pill: **radius = altura ÷ 2** (24 para 48). **Um ícone** de 20px, a **10px** do label. Nunca 2 ícones |
| 6 | **Motion** | Estático | Hover: luz percorre o rim em **200ms**. Press: afunda **1px**. Spinner → check "Added ✓". **Latência** (prazo do sistema, não duração de animação): resposta visível em **≤ 100ms** e estado final ou spinner em **≤ 300ms**. A animação segue os tokens de `ui-motion` (feedback visual em 0 ms, press 160 ms) |

## 2. Botão: 6 regras (`DfemaTCBncA`, @designmotionhq)
Partes do botão: shadow, fill, border, label e focus ring. Exemplo: "Create workspace".
1. **Tap target ≥ 44px** mesmo que o visual seja menor. O frame mostra 32px visual e 44px de área de toque. Reforçado por `DfwojjrirKz` (@designmotionhq): 44pt iOS / 48dp Android, web com piso de 24px e meta 44, área por padding (20 + 12 + 12) e ~8px entre alvos. Detalhes em `typography-and-touch.md` §1.
2. **O label diz a ação**: "Create workspace", não "Submit".
3. **Um primário por tela**. Cancel fica como ghost, para o olho saber onde pousar.
4. **Loading**: mantenha a largura, troque o label por spinner e **ignore o segundo clique**. O frame mostra "Requests sent: 1".
5. **Focus ring sempre visível** para quem usa teclado. Nunca entregue `outline: none`.
6. **Disabled explica o porquê**, por exemplo "ⓘ Name your workspace first".

## 3. Telas de configurações: 6 falhas (`DdRneVWhBSY`)
Gancho do reel: "You flipped one toggle. It signed 24 colleagues out." Fechamento: "Settings are a surface. Design it."
| # | Falha | Correção |
|---|---|---|
| 1 | Sem botão de salvar e sem confirmação ("they flip it and hope") | Estado "Saved" visível na linha, **ou** save explícito com linhas "dirty" marcadas |
| 2 | Preferência pessoal e switch da empresa inteira com a mesma aparência ("Require 2FA" vs "Weekly digest email") | **Escopo em cada linha**: pessoal, workspace ou todos. "Put the scope on the row." **É o erro mais caro** |
| 3 | 60 settings numa lista plana, sem busca | Filtro, seções reais e link direto para cada linha |
| 4 | Label sem explicação ("Four labels. Four guesses.") | Uma linha sob o label dizendo a consequência, nos termos do usuário |
| 5 | Nada marca o que foi alterado ("Which three did you touch?") | Marcar o que está fora do default e oferecer reset por linha em 1 toque. "Mark it. Let them reset it." |
| 6 | Só vale depois de restart e não avisa ("Not broken. Just pending.") | Dizer **antes do flip** quando vale: agora, no próximo sign-in ou após restart |

## 4. Paginação: 6 erros (`DdtzWoMhLtW`)
Gancho: "You scrolled 400 rows… you hit back. Row one." Fechamento: "Pagination is navigation."
1. **Mostre o total**: "Page 3 of 48 · 1,187 results", não três pontinhos e um chevron.
2. **Reserve o espaço**: 2 linhas carregando acima empurram tudo **68px** e o toque cai no item errado. Use altura fixa ou skeleton.
3. **O footer precisa ser alcançável**: infinite scroll enterra contato, termos e suporte. Use "Load more, then stop".
4. **Página na URL**: `?page=3&sort=price` sobrevive a refresh e pode ser compartilhada. Estado de componente não.
5. **Diga quando acabou**: "End of results — 1,187 shown". Um spinner eterno parece quebrado; terminado e quebrado ficam idênticos.
6. **Back é back**: restaure o scroll offset e marque a linha tocada. O frame mostra "400 rows restored on back".

## 5. Chat: 6 decisões (`DerGbJAhUTm`)
| # | Decisão | Números / regra |
|---|---|---|
| 1 | Alignment | Suas mensagens à direita, as deles à esquerda. O lado diz quem falou, sem precisar ler nomes |
| 2 | Grouping | **4px** dentro de uma sequência do mesmo remetente, **18px** entre pessoas (antes eram 14px uniformes). **1 avatar por sequência**. 5 bolhas viram 3 turnos |
| 3 | Colour | Suas bolhas e o botão de enviar levam o accent, com texto escuro a **8.3:1** |
| 4 | Timestamps | 5 mensagens em 2 minutos com 5 timestamps viram **1 divisor** no início ("stamp the gap") |
| 5 | Status | "Online" no header e "Read" **só sob a sua última mensagem** |
| 6 | Motion | Typing dots; mensagens novas deslizam em **240ms**; a sua sobe da caixa de texto e muda de sent para read |

## 6. Command palette ⌘K: 6 decisões (`DeUr5-AhdvQ`)
1. **Hierarchy**: antes, input e resultados tinham todos 18px. Depois, input de **44 → 68px** com texto de **26px** e detalhes em **14px**. O input é a coisa mais "alta" da tela.
2. **Grouping**: em vez de 1 lista misturada, **3 grupos** (Actions, Pages, Recent) com ícone por tipo (24px no frame).
3. **Match**: destaque as letras digitadas ("inv" em "New **inv**oice"). "Every row says why it's here."
4. **Focus**: painel elevado com sombra e **primeiro resultado já selecionado**, para que Enter funcione.
5. **Shortcuts**: `⌘N` na própria linha e `↑↓ ↵ esc` no footer. "Clicks teach the keys."
6. **Motion**: abre em **150ms**, refiltra a cada tecla, as setas deslizam a seleção, Enter mostra spinner e depois abre.

## 7. Toolbar lotada (`DfreUkyBNQg`, Hick's law)
Gancho: "Find the crop tool. Found it yet?" Uma barra de 12 ícones parece lenta.
1. Mantenha os **3 a 5** tools de uso diário. "Count what they tap, not what you shipped."
2. **Um** action com accent; o resto fica quieto.
3. **Uma palavra sob cada ícone** (Crop, Adjust, Filters, Erase, More). "Glance, don't guess."
4. Tools raros atrás de **More** (Rotate, Flip, Stickers, Light), a um toque de distância.
5. Agrupe o resto **por tarefa** ("Edit, then Adjust"). Dois grupos curtos são lidos mais rápido que uma fila longa.
6. Exceção para experts: dê **atalhos** de teclado.

## 8. Micro-interações em slow-mo (vídeo de `DfgcqeMBPCU`)
O áudio e os frames deste reel mostram "More smooth details, in slow-mo (part 6)". A legenda fala de dark patterns (veja `dark-patterns.md`). Valores exibidos nos frames:
- **Bottom sheet**: segue o dedo e faz snap em **146px** com **overshoot de 7px**; a página escurece.
- **Tooltip**: cresce da seta, escala **50% → 100%** a partir da seta.
- **Typing dots**: 3 pontos em onda, **100ms** de defasagem; depois a bolha se abre na mensagem.
- **Toast**: entra subindo **64px**; o anterior recua para **92%** e forma uma pilha.
- **File drop**: o arquivo sobe a **110%**, a zona brilha e ele pousa a **55%**.
- **Payment**: "Pay" vira check "Paid" e solta confetti de **18 peças, com pico em 460ms**, caindo com gravidade.

**Tooltip de arraste com o resultado antes de soltar** (`Dfr4RMBlaPH`, @felvrabr, rodada 7, grade de reservas "Maren"): ao esticar uma reserva no calendário tipo Gantt aparece **"Drag to extend · 4 nights · 29 Dec → 2 Jan · $4,280"**. Barras com cor por estado (terracota = Booked, teal = New). Regra: durante qualquer arraste que muda valor (reserva, intervalo de datas, slider de preço), mostre em tempo real **o que vai acontecer** (quantidade, intervalo, total), não só a posição. **(complemento)**: o tooltip segue o ponteiro sem atraso (Doherty), usa dígitos tabulares, some no drop e o valor final aparece no card; com teclado, a mesma informação vai num `aria-live`. Motion do arraste em `ui-motion` (`micro-interactions.md` §10).

## 9. Tela de decisão: "desenhe para o momento" (`DXeeUP7FKGs`, @rish_designs via @ultimateuiux)
App de trading "Markets" (lista de ativos + detalhe com candles). A tese da legenda, resumida: a tela não foi feita para *parecer* app de trading, e sim para o instante em que a pessoa decide comprar, vender ou esperar. Bom UX é tirar atrito entre intenção, decisão e ação, não somar features.
1. **Responda na hora o que importa agora**: o que está se mexendo ("Today's Movers"), o preço e a variação. Nada de mostrar tudo.
2. **Sinais imediatos + contexto mínimo**: variação sempre com **sinal (+/−) e cor**, em pílula.
3. **Camada de ajuda para reduzir dúvida, não para enfeitar**: card "AI Report" com veredito curto ("BEARISH"), 2–3 frases e link "View Full Analysis →".
4. **As duas ações da decisão com o mesmo peso**, lado a lado, fixas no rodapé (zona do polegar): Sell vermelho e Buy no accent.
5. **Um accent só** para estado ativo: aba, período (1D) e CTA positivo.
- **Divergência registrada**: §2 diz "um primário por tela". Aqui há **dois** botões de mesmo peso. Leitura **(complemento)**: quando a decisão é entre duas ações opostas e igualmente legítimas (comprar/vender, aceitar/recusar uma oferta), ambas são primárias; a regra de um primário vale para ação principal vs secundária/cancelar. Ação destrutiva continua com cor de alerta.
- Visual: `DXeeUP7FKGs_1.jpg`.

## 10. Fluxo de pedido/serviço (`DX_bA4rCWf0`, @ui.pixel; design de @oshioke.ui, app de lavanderia)
1. **Progresso do pedido em 4 etapas nomeadas** (Picked → Washing → Out for delivery → Delivered), **a mesma barra na home e no detalhe**. Liga com Uniform connectedness e Goal gradient (`ux-laws.md`).
2. **Rodapé fixo com total + botão primário**: "Delivery Fee $5 / Estimated Total $21" + "Schedule A Collection". A pessoa vê o custo no momento de decidir.
3. **Revisão antes de pagar**: itens, horários, endereço e subtotal, e o botão diz o valor ("PAY NOW $…"). Atenção: no exemplo o botão diz $43 e o subtotal $26. **Confira que o valor do botão bate com o total**.
4. **Pedido ativo com status em selo** ("On Process") + mapa da rota + ação de cancelar visível.
5. **Tab bar com botão central circular** para a ação principal. **Divergência**: Serial position (`ux-laws.md`, parte 2) manda a ação-chave para o início ou o fim, não para o meio. O botão central funciona porque é **visualmente distinto** (Von Restorff), não pela posição **(complemento)**.
- Outra referência (`DVv7OOECewR`, @ui.pixel, app "WayLoo"): tab bar flutuante em pílula com a aba ativa no accent; o accent fica reservado a botões, selos e estado ativo.

## 11. Home redesenhada: antes/depois (`DfzgxEKlx8z`, @dailywebdesign; por @ui.abraham, app imobiliário)
- Paleta mista (coral, laranja, azul-lilás) → **um azul** com neutros.
- **Não abra a home com estado vazio** ("No properties found" na primeira dobra). Mostre conteúdo útil: cartões com foto grande, preço, selo e nota.
- Filtros em pílula com **um estado ativo cheio**, em vez de 4 cores de contorno.
- Banner com ilustração e **um CTA claro** no lugar de bloco de gradiente com texto longo.

## 12. Checklists de pesquisa NN/g (rodada 9B; detalhes e fontes em `nng-research.md`)
**Onboarding**
- [ ] Sem tour/deck instrucional se o app não precisa de dados para começar; prefira dica em contexto e empty state que ensina.
- [ ] Se houver deck: "Skip" visível, poucos cards, 1 conceito por card; tema/cores fora do onboarding.

**Navegação**
- [ ] Tab bar mobile com **3–5 destinos** (NN/g: teto 4–5; vale `mobile-app-ui` §3), ícone + rótulo, sempre visível; sem "More".
- [ ] Tabs internas: rótulo de 1–2 palavras, **≥ 2 indicadores de seleção**, um nível; no mobile, acordeão para conteúdo longo.

**Empty state**
- [ ] Diz o estado do sistema, ensina a função e oferece **um botão** para a 1ª tarefa. Nunca "Sem registros" durante o carregamento.

**Formulário**
- [ ] Coluna única; **rótulo fora do campo** (placeholder nunca é o rótulo); "(opcional)" marcado.
- [ ] Validação inline **depois de concluir o campo** (blur), erro ao lado do campo com cor + ícone; sem tooltip de erro; ajuda extra após 3 erros.
- [ ] Botão de enviar embaixo dos campos ou fixo no rodapé, nunca no topo.

**Dashboard** (divergência com `dashboard-ui` em `nng-research.md` §6)
- [ ] Valores em barras/linhas; pizza/donut/gauge só como moldura de **um** número com meta, com o número escrito.
- [ ] Cor nunca é o único sinal (rótulo, forma, posição).

**Confiança e permissões**
- [ ] Valor entregue antes de pedir login, dados pessoais, pagamento ou conta conectada (5 níveis de compromisso).
- [ ] Permissão pedida **no contexto**, com "para que você possa [benefício]" (+12% de aceite com motivo) e caminho de volta às configurações se negada.

**Métricas**
- [ ] App de consumo → HEART; ferramenta de trabalho/painel → **CASTLE** (carga cognitiva, recursos avançados, satisfação, eficiência, aprendizado, erros).

## 13. Padrões da rodada 10A (Instagram, 27/11/2026; 1 frame + legenda por post)

### 13.1 Accordion: escolha pelo conteúdo (`DgLUGlUORly`, @ale.uiux, "6 ways to show more on tap")
| Tipo | Quando |
|---|---|
| Chevron | FAQ simples |
| Cards expansíveis | o item aberto precisa de prévia (viagem, produto); "o aberto sobe com uma prévia" |
| Aninhado | configurações em grupos |
| Etapas | checkout dividido em Envio → Pagamento → Revisão |
| Read more | artigo longo |
| Horizontal | galeria |
(complemento) Botão do cabeçalho com `aria-expanded`; abrir um não fecha os outros, salvo em etapas; animação de altura com `ext-transitions-dev` ("accordion").

### 13.2 Header fixo que come a tela (`DgCe3izzZVP`, @theglidestudio, "Half the screen is a header")
"Devolva a página ao leitor": no frame, o header de um site de notícias ocupava **50%** da altura do celular; correção 1 = **encolher**. As outras 2 correções não foram vistas. Reforça o header sticky ≤ 64–72px de `website-ui` §5 (complemento) e o large title que encolhe 34 → 18 de `mobile-app-ui`.

### 13.3 Arrastar para reordenar (`DgM5twdsInO`, @theglidestudio)
"Nada diz que elas se movem, então ninguém tenta": **alça visível**, **linha erguida** ao pegar, **espaço aberto** onde vai cair. Valores: `ui-motion` → `micro-interactions.md` §16.

### 13.4 Permissão de notificação (`DgDlMjfhNhc`, @theglidestudio, "Earn the yes before you ask")
Frame: "1. Wait until it matters" (app de plantas). Mesma regra do NN/g (§12 e `nng-research.md` §9): **peça no contexto, depois de entregar valor**, nunca na primeira abertura.

### 13.5 Número grande em 375 px (`Deq_kvJBI3g`, @designmotionhq, "On a 375px phone, five things break")
Fix 2 "Big numbers": **uma linha, tamanho com teto** — `white-space: nowrap; font-variant-numeric: tabular-nums; font-size` até **~30px** no celular (antes: €5.3M quebrado em 48px). Print: `dashboard-ui/assets/visual-refs/Deq_kvJBI3g_1.jpg`; CSS em `ui-motion` → `css-recipes.md` §14. Os outros 4 fixes não foram vistos.

### 13.6 Cinco "fixes" antes de recomeçar do zero (`DgOzQOLk5m9`, @gg.designhub)
(1) hierarquia: o mais importante maior, apoio discreto, ordem de leitura clara; (2) simplificar: tirar o não essencial, dar respiro, **uma** mensagem; (3) tipografia: entrelinha, 45–75 caracteres, contraste título × corpo; (4) remover o que não pertence (formas decorativas, informação repetida); (5) alinhamento e contraste: **uma grade**, texto com contraste forte, conferir no tamanho real de visualização. Reforço de @wejustclick.me (`Dft07xmDJkm`): contraste de cor, tamanho e peso cria foco; poucas cores e **uma lidera**. Prompts de auditoria equivalentes para o Claude: `design-direction` → `claude-web-design-workflow.md`.
