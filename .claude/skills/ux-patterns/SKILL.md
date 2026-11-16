---
name: ux-patterns
description: Padrões e checklists de UX com números concretos para revisar e corrigir interfaces. Cobre 18 leis de UX demonstradas lado a lado (Fitts, Hick, Chunking, Doherty, Proximity, Von Restorff, Goal gradient, Postel, Tesler, Closure, Figure-ground, Choice overload e outras), botão primário (6 decisões e 6 regras), telas de configurações (6 falhas), paginação e infinite scroll (6 erros), chat (6 decisões), command palette ⌘K, toolbar lotada, micro-interações, dark patterns e sua versão honesta, como tirar a cara de "AI slop" de dashboards e fontes default, e 31 itens de performance real e percebida (skeleton, streaming, optimistic UI etc.). Use quando o usuário pedir "revisar UX", "auditar a tela", "melhorar botão", "botão parece barato", "tela de settings", "página de configurações", "paginação", "infinite scroll", "tela de chat", "command palette", "⌘K", "toolbar lotada", "dark pattern", "app parece feito por IA", "dashboard genérico", "app lento", "skeleton" ou "performance percebida".
---

# UX Patterns

Regras de UX que dá para testar numa tela real, tiradas de 14 reels (@motion_ui_interface, @designmotionhq e @gustagoat.ai). Os números são das demonstrações dos reels. Use-os como alvo padrão, não como lei física.

## Quando usar
- Revisar ou criar um componente: botão, settings, lista paginada, chat, ⌘K, toolbar, dashboard.
- Justificar uma mudança de UX com uma lei nomeada e um número.
- Auditar um app gerado por IA (aparência genérica, fonte default, lentidão).
- Detectar padrões enganosos (trial, social proof falso, close falso).

## Checklist central

**Leis-base** (detalhes em `references/ux-laws.md`)
- Fitts: ação principal grande e perto (0.66s → 0.28s).
- Hick e Choice overload: mostrar poucos itens e o resto em "More" (12 → 4 apps: 0.74s → 0.46s; geleias 3% → 30%).
- Chunking: agrupar o que precisa ser lembrado (~4 chunks), por exemplo `415 555 0123`.
- Doherty: feedback em até **400ms**, mesmo quando o trabalho é lento.
- Proximity: label a **8px** do próprio campo e **24px** do próximo.
- Von Restorff: **um** destaque, nunca três.
- Tesler e Parkinson: o sistema preenche o que já sabe (31 → 16 teclas; 30 → 7).
- Postel: aceitar qualquer formato e normalizar.
- Figure-ground: backdrop atrás de modal (contraste do fundo 17.4:1 → 2.5:1).
- Goal gradient: progresso nunca começa do zero. Peak-end: a última tela é desenhada de propósito.

**Botão primário**
- Altura ≥ **44px** (alvo 48), padding lateral 24px, área de toque ≥ 44px mesmo que o visual seja menor.
- Label 17px semibold, sentence case, **verbo + objeto** ("Add to cart", nunca "Submit/OK").
- Contraste do label ≥ **4.5:1** e da borda ≥ **3:1**. Fill cinza a 1.6:1 some.
- Um primário por tela; Cancel como ghost. Pill: radius = altura ÷ 2; no máximo 1 ícone, a 10px do label.
- Feedback em **100ms**, concluído em **300ms**. Loading mantém a largura e ignora o 2º clique.
- Focus ring visível (nunca `outline: none`). Disabled diz o porquê.

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
| `references/components-checklists.md` | For mexer em botão, settings, paginação, chat, ⌘K, toolbar ou micro-interações (sheet, tooltip, toast, file drop, pagamento) |
| `references/dark-patterns.md` | Houver fluxo de assinatura, preço, ads ou popups, ou o app "parecer feito por IA" (dashboard ou fonte) |
| `references/perceived-performance.md` | O app parecer lento, ou ao revisar app de vibe coding antes de lançar |
| `references/visual-index.md` | Antes de abrir qualquer imagem, para escolher qual |

## Imagens (`assets/visual-refs/<ID>.jpg`)
São folhas de contato 4×3 com frames antes/depois. **Cada uma custa bastante contexto**: abra no máximo 1–2, só quando precisar ver o layout (espaçamentos anotados, hierarquia), não para tirar números, que já estão nos references. Consulte `visual-index.md` para escolher. Atalhos:
- Botão: `Ddy5RJOha1U` (medidas) ou `DfemaTCBncA` (estados).
- Settings: `DdRneVWhBSY`. Paginação: `DdtzWoMhLtW`. Chat: `DerGbJAhUTm`. ⌘K: `DeUr5-AhdvQ`. Toolbar: `DfreUkyBNQg`.
- Dashboard genérico: `Dc-4jNbtyJg`. Fonte: `DfPJo9UBJ7D`. Micro-interações: `DfgcqeMBPCU`.
- Leis: `Dd25eCoBJGr`, `Dd4UtBDBsIS`, `Del7XTgsuwI`.

## Skills complementares
- `ext-impeccable`: audit, critique e polish de interface.
- `ext-playwright-cli`: abrir e testar o app no browser (verificação).
- `design:accessibility-review`: auditoria WCAG 2.1 AA (contraste, foco, touch targets).

## Notas de fidelidade
- `DfgcqeMBPCU`: a legenda é sobre dark patterns, mas o vídeo mostra micro-interações. As versões honestas são **(complemento)**.
- A série de leis tem 4 partes; a parte 3 não está nas fontes.
- O "kit" de performance e o plugin "UX Engine" mencionados nos reels não estão incluídos.

## Skills externas (dependências)
Esta skill pode delegar para: `ext-impeccable`, `ext-playwright-cli`. Elas **não** fazem parte da repo; são instaladas por `scripts/install-external-skills.sh`.
1. Antes de delegar, confira se a pasta existe em `.claude/skills/<nome>/` ou `~/.claude/skills/<nome>/`.
2. Se faltar, **pergunte ao usuário** antes de instalar e, com o ok, rode `./scripts/install-external-skills.sh` (ou `--global`). Depois da instalação, o Claude Code normalmente já enxerga as skills novas; se alguma não aparecer, leia o `SKILL.md` instalado com Read e siga as instruções dele.
3. Se o usuário não quiser instalar, siga sem elas usando as references desta skill.

