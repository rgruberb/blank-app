---
name: ux-patterns
description: Padrões e checklists de UX com números concretos para revisar e corrigir interfaces: 18 leis de UX (Fitts, Hick, Doherty, Proximity, Von Restorff…), alvos de toque (44pt/48dp, web 24px), escala tipográfica (1,2 ou 1,25) com line-height, tracking e medida, grade de 8px, contraste, dark mode, botão primário, settings, paginação, chat, ⌘K, toolbar, tela de decisão, fluxo de pedido, dark patterns, "AI slop", performance percebida e pesquisa NN/g (onboarding, empty state, formulário, dashboard, permissões, HEART/CASTLE). Use quando o usuário pedir "revisar UX", "auditar a tela", "botão parece barato", "settings", "paginação", "infinite scroll", "chat", "⌘K", "toolbar lotada", "dark pattern", "app parece feito por IA", "app lento", "skeleton", "alvo de toque", "tamanho de fonte", "escala tipográfica", "line-height", "grid de 8", "espaçamento", "contraste", "dark mode", "tela de compra/decisão", "progresso do pedido", "onboarding", "empty state", "formulário", "permissão" ou "NN/g".
---

# UX Patterns

Regras de UX que dá para testar numa tela real, tiradas de 14 reels (@motion_ui_interface, @designmotionhq e @gustagoat.ai), das rodadas 3A–3C de perfis (@designmotionhq, @motion_ui_interface, @theglidestudio, @rish_designs, @ui.pixel, @dailywebdesign) das rodadas 1, 2 e 7 (@gg.designhub, @designmotionhq, @felvrabr, @shohan.designs) e, como fonte de pesquisa, do **Nielsen Norman Group** (rodada 9B) e das guias oficiais **Apple HIG** e **Material 3** (rodada 9A). Os números dos reels são de demonstração; os do NN/g vêm de estudos (muitos de 2015–2019). Use-os como alvo padrão, não como lei física.

## Quando usar
- Revisar ou criar um componente: botão, settings, lista paginada, chat, ⌘K, toolbar, dashboard.
- Justificar uma mudança de UX com uma lei nomeada e um número.
- Auditar um app gerado por IA (aparência genérica, fonte default, lentidão).
- Detectar padrões enganosos (trial, social proof falso, close falso).
- Definir alvos de toque, tamanhos de fonte, line-height e contraste de um design system.

## Checklist central

**Leis-base** (detalhes em `references/ux-laws.md`)
- Fitts: ação principal grande e perto (0.66s → 0.28s).
- Hick e Choice overload: mostrar poucos itens e o resto em "More" (12 → 4 apps: 0.74s → 0.46s; geleias 3% → 30%).
- Chunking: agrupar o que precisa ser lembrado (~4 chunks), por exemplo `415 555 0123`.
- Doherty: feedback em até **400ms**, mesmo quando o trabalho é lento. Na primeira tela, **título primeiro**: 2 s em branco "parecem uma hora".
- Proximity: label a **8px** do próprio campo e **24px** do próximo.
- Von Restorff: **um** destaque, nunca três.
- Tesler e Parkinson: o sistema preenche o que já sabe (31 → 16 teclas; 30 → 7).
- Postel: aceitar qualquer formato e normalizar.
- Figure-ground: backdrop atrás de modal (contraste do fundo 17.4:1 → 2.5:1).
- Goal gradient: progresso nunca começa do zero. Peak-end: a última tela é desenhada de propósito.

**Botão primário**
- Altura ≥ **44px** (alvo 48), padding lateral 24px, área de toque ≥ 44px mesmo que o visual seja menor.
- Label 16 ou 19px semibold (escala 1,2; a fonte usa 17), sentence case, **verbo + objeto** ("Add to cart", nunca "Submit/OK").
- Contraste do label ≥ **4.5:1** e da borda ≥ **3:1**. Fill cinza a 1.6:1 some.
- Um primário por tela; Cancel como ghost. Pill: radius = altura ÷ 2; no máximo 1 ícone, a 10px do label.
- Latência: resposta em **≤ 100ms** e estado final/spinner em **≤ 300ms** (prazo do sistema, não duração de animação; a animação segue `ui-motion`: press 160 ms, feedback em 0 ms). Loading mantém a largura e ignora o 2º clique.
- Focus ring visível (nunca `outline: none`). Disabled diz o porquê.

**Alvos e tipografia** (`references/typography-and-touch.md`)
- Toque: **44pt** iOS, **48dp** Android; web piso **24px**, meta **44**. Cresça por padding (**20 + 12 + 12 = 44**), **~8px** entre alvos pequenos.
- Fonte: **uma** escala por projeto: `16 × 1,2^n` (16, 19, 23, 28, 33, 40, 48) para produto denso **ou** Major Third `16 × 1,25^n` (12,8, 16, 20, 25, 31, 39, 49) para site/editorial (a divisão por tipo de produto é complemento). Line-height **1,5** no corpo caindo até **1,1** nos títulos grandes; tracking **−0,02em** em títulos, **+0,05–0,06em** em caps; linha de **45–75** caracteres (45–60 em formulários), token `--measure: 50ch` (`typography-and-touch.md` §2b).
- Espaçamento: grade de **8** (8, 16, 24, 32, 48, 64), **4** só para micro; nada de 13 ou 27px.
- Arraste que muda valor mostra o resultado antes de soltar ("Drag to extend · 4 nights", `components-checklists.md` §8).
- Contraste: texto e placeholder **4,5:1**; texto grande (24px ou 19px bold), ícones e bordas **3:1**; scrim em texto sobre foto.
- Dark mode: sem `#000` (ex.: `#0C1424`), texto a **87%**, accent clareado, elevação por luminosidade.

**Pesquisa NN/g** (`references/nng-research.md`; checklist em `components-checklists.md` §12)
- Onboarding: evite o instrucional; prefira dica em contexto e empty state que ensina. Só quando o app precisa de dados para começar.
- Tab bar mobile com **3–5** destinos e rótulo (NN/g: teto de 4–5; regra de plataforma em `mobile-app-ui` §3); tabs internas com 1–2 palavras e ≥ 2 indicadores de seleção.
- Alvo físico **~1 cm** (ação primária ~2 cm). Empty state: estado do sistema + ensina + botão.
- Formulário: coluna única, rótulo fora do placeholder, validação inline **depois de concluir o campo**, erro ao lado com cor + ícone.
- Dashboard: barras/linhas > pizza/donut/gauge; cor nunca é o único sinal (**diverge de `dashboard-ui`**, critério em §6).
- Confiança: 5 níveis de compromisso; não peça login/dados antes de entregar valor. Permissão em contexto com motivo (**+12%** de aceite).
- Métricas: HEART para consumo, **CASTLE** para ferramenta de trabalho.

**Tela de decisão** (`components-checklists.md` §9): só sinais imediatos e contexto mínimo; as duas ações opostas com o mesmo peso no rodapé; tirar atrito, não somar features.

**Fluxo de pedido** (§10): progresso em etapas nomeadas igual na home e no detalhe; rodapé fixo com total + primário; o valor do botão bate com o total.

**Settings**: confirmar o save · escopo em cada linha (pessoal, workspace, todos) · busca e seções · uma linha de consequência · marcar o que não é default e oferecer reset · dizer quando vale (agora, próximo login, restart).

**Paginação**: total visível ("Page 3 of 48 · 1,187 results") · espaço reservado (sem shift de 68px) · footer alcançável · `?page=&sort=` na URL · "End of results" · back restaura o scroll e a linha.

**Chat**: suas mensagens de um lado · 4px dentro de uma sequência e 18px entre pessoas · accent nas suas (texto a 8.3:1) · timestamp só no intervalo · "Read" só na última · typing e slide-in em 240ms.

**⌘K**: input como maior elemento (44 → 68px) · grupos Actions/Pages/Recent · letras digitadas destacadas · 1º resultado pré-selecionado · atalhos na linha · abre em 150ms e filtra a cada tecla.

**Toolbar**: 3–5 tools diários · 1 accent · label sob cada ícone · raros em More · grupos por tarefa · atalhos para experts.

**Anti "AI slop"** (`references/dark-patterns.md` §B–C): um accent chapado sem gradiente · número é o herói, sem tiles pastel · 1 métrica primária e 3 secundárias · bordas hairline, sombra só no que flutua · período nomeado, tabular digits, sparkline · fonte do mundo do produto, carregada de verdade, 1 família com 2 pesos.

**Dark patterns** (`references/dark-patterns.md` §A): trial que cobra sem aviso, social proof falso, anúncio disfarçado, nagging sem "não", decoy de preço, X falso. Sempre proponha a versão honesta.

**Performance** (`references/perceived-performance.md`, 31 itens): primeiro o que se sente (skeleton, streaming de IA token a token, optimistic UI, lazy loading, virtualização), depois rede, backend e banco, por fim medição (RUM e teste no celular em rede lenta).

## Workflow: auditar → corrigir → verificar

1. **Auditar**
   - Identifique os componentes presentes na tela ou no código.
   - Para cada um, passe o checklist acima e anote: problema, lei violada, número atual vs alvo e arquivo:linha.
   - Para uma crítica mais ampla, rode `ext-impeccable` (audit/critique). Para WCAG (contraste, foco, alvos), rode `design:accessibility-review`.
2. **Corrigir**
   - Comece pelo que é mais caro para o usuário: escopo de settings, back que perde a posição, botão sem feedback, cobrança enganosa.
   - Depois vem hierarquia e ruído (Hick, Von Restorff, AI slop) e por fim o polish.
   - Use `ext-impeccable` (polish) para o acabamento.
3. **Verificar**
   - Teste no browser com `ext-playwright-cli`: tamanho dos alvos, foco via Tab, `?page=` sobrevivendo a refresh, back restaurando o scroll, segundo clique ignorado durante o loading.
   - Teste também com fonte carregada em browser limpo e em celular com rede lenta.
   - Reporte antes → depois com os números.

## Quando abrir cada reference
| Arquivo | Abra quando |
|---|---|
| `references/ux-laws.md` | Precisar da definição, falha e correção de qualquer uma das 18 leis, ou citar o número da demonstração |
| `references/components-checklists.md` | For mexer em botão, settings, paginação, chat, ⌘K, toolbar, micro-interações (sheet, tooltip, toast, file drop, pagamento), tela de decisão (comprar/vender), fluxo de pedido ou home com estado vazio |
| `references/typography-and-touch.md` | Precisar de alvo de toque (inclui Apple 44/28pt, Material 48dp + 8dp, NN/g 1 cm), escala e tamanhos de fonte (1,2 vs 1,25 vs Material 1,125; Apple 17/11pt), line-height, tracking, medida de linha, grade de espaçamento de 8, números em matriz de pontos, contraste mínimo ou dark mode |
| `references/dark-patterns.md` | Houver fluxo de assinatura, preço, ads ou popups, ou o app "parecer feito por IA" (dashboard ou fonte) |
| `references/perceived-performance.md` | O app parecer lento, ou ao revisar app de vibe coding antes de lançar |
| `references/nng-research.md` | Onboarding, tab bar/tabs, empty state, formulário e erros, login, dashboard (barras × donut/gauge), tabela de dados, confiança, permissões, métricas HEART/CASTLE, ou quando precisar citar estudo do NN/g e suas lacunas |
| `references/visual-index.md` | Antes de abrir qualquer imagem, para escolher qual |

## Imagens (`assets/visual-refs/<ID>.jpg`)
São folhas de contato 4×3 com frames antes/depois. **Cada uma custa bastante contexto**: abra no máximo 1–2, só quando precisar ver o layout (espaçamentos anotados, hierarquia), não para tirar números, que já estão nos references. Consulte `visual-index.md` para escolher. Atalhos:
- Botão: `Ddy5RJOha1U` (medidas) ou `DfemaTCBncA` (estados).
- Settings: `DdRneVWhBSY`. Paginação: `DdtzWoMhLtW`. Chat: `DerGbJAhUTm`. ⌘K: `DeUr5-AhdvQ`. Toolbar: `DfreUkyBNQg`.
- Dashboard genérico: `Dc-4jNbtyJg`. Fonte: `DfPJo9UBJ7D`. Micro-interações: `DfgcqeMBPCU`.
- Leis: `Dd25eCoBJGr`, `Dd4UtBDBsIS`, `Del7XTgsuwI`.
- Tela de decisão (trading): `DXeeUP7FKGs_1` (print único, não folha 4×3).
- Escala 1,25: `DfRucYFjrac_1` (escada), `DfRucYFjrac_2` (line-height), `De_FtT3k-tT_2` (Major Third 16→39). Prints únicos, pequenos.
- NN/g: dashboard linha + barras `9B_dashboards_linha-e-barras_1`, empty state `9B_empty-states_datadog_1`, permissão negada `9B_permissoes_venmo-camera-negada_1`, senha com medidor `9B_formularios_slack-forca-senha_1`, tabela + painel lateral `9B_tabelas_painel-lateral-crm_1`, tabs internas `9B_tabs_google-finance-in-page_1`, alvo grande `9B_touch-targets_target-app_1` (prints únicos).
- Perfis avaliados (quem vale seguir, quem está inativo) e fontes de pesquisa/oficiais: fim do `visual-index.md`.

## Skills complementares
- `ext-impeccable`: audit, critique e polish de interface.
- `ext-playwright-cli`: abrir e testar o app no browser (verificação).
- `design:accessibility-review`: auditoria WCAG 2.1 AA (contraste, foco, touch targets).

## Notas de fidelidade
- `DfgcqeMBPCU`: a legenda é sobre dark patterns, mas o vídeo mostra micro-interações. As versões honestas são **(complemento)**.
- A série de leis tem 4 partes; a parte 3 não está nas fontes.
- Divergências registradas: escala 1,2 vs a hierarquia 40/24/18/14 de `DfPJo9UBJ7D` e o label de 17px (`typography-and-touch.md` §2); escala 1,2 (`DfjxqzkCrUI`) vs 1,25 do **mesmo autor** (`DfRucYFjrac`) e do @gg.designhub, com caps +0,06 vs +0,05em e medida 60ch vs 50ch (§2b); grade de 8 vs chat 18px e ícone a 10px (§6); "um primário por tela" vs Buy/Sell de mesmo peso (§9); botão central da tab bar vs Serial position (§10).
- Divergências das rodadas 9A/9B: NN/g evita pizza/donut/gauge e `dashboard-ui` usa donut/gauge/anéis (critério em `nng-research.md` §6); Material usa escala 1,125 base 14 vs 1,2/1,25 base 16 desta skill (`typography-and-touch.md` §2c); mínimo Apple 28pt vs padrão 44pt (§1b).
- O "kit" de performance e o plugin "UX Engine" mencionados nos reels não estão incluídos.

## Skills externas (dependências)
Esta skill pode delegar para: `ext-impeccable`, `ext-playwright-cli`. Elas **não** fazem parte da repo; são instaladas por `scripts/install-external-skills.sh`.
1. Antes de delegar, confira se a pasta existe em `.claude/skills/<nome>/` ou `~/.claude/skills/<nome>/`.
2. Se faltar, **pergunte ao usuário** antes de instalar e, com o ok, rode `./scripts/install-external-skills.sh` (ou `--global`). Depois da instalação, o Claude Code normalmente já enxerga as skills novas; se alguma não aparecer, leia o `SKILL.md` instalado com Read e siga as instruções dele.
3. Se o usuário não quiser instalar, siga sem elas usando as references desta skill.

