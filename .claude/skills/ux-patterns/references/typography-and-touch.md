# Alvos de toque, escala tipográfica e contraste

Regras numéricas de 4 carrosséis/reels do @designmotionhq (série "DMHQ / UI Geometry"), de 2 reels do @motion_ui_interface, do carrossel "Cheat Codes" do @gg.designhub (escala 1,25, grade de 8, medida) e de 1 post do @shohan.designs (números em matriz de pontos). Os números são das fontes; o que está marcado **(complemento)** é inferência ou ajuste nosso.

---

## 1. Alvo de toque (`DfwojjrirKz`, @designmotionhq, carrossel de 8 folhas)
Gancho: "A 20 px icon is not a 44 px button." Ícones de 20px com área clicável de 20px são o erro.

| # | Regra | Número |
|---|---|---|
| 1 | Mínimos nativos | **44 × 44 pt** no iOS, **48 × 48 dp** no Android |
| 2 | Piso na web | **24 × 24 CSS px** (WCAG 2.2 AA, critério 2.5.8); **mire 44** (AAA, 2.5.5) |
| 3 | Cresça a área com padding, não o ícone | **20 + 12 + 12 = 44** (`.icon-btn { padding: 12px; }`). Hover e focus ring também ocupam os 44 |
| 4 | Áreas nunca se sobrepõem | Entre alvos pequenos vizinhos, **~8px** de folga. Centros a **32px** = áreas sobrepostas; centros a **52px** = 8px entre áreas. Linhas grandes de lista podem encostar |

Tokens da fonte (resumidos):
```css
:root { --tap: 44px; /* 48px no Android */ --tap-gap: 8px; }
.icon-btn { display: inline-grid; place-items: center; min-width: var(--tap); min-height: var(--tap); }
.toolbar { display: flex; gap: var(--tap-gap); }
```

**Reforça** o que já está na skill: botão primário ≥ 44px (alvo 48) em `components-checklists.md` §1–2 (`Ddy5RJOha1U`, `DfemaTCBncA`: 32px visual com 44px de toque) e o X falso de `dark-patterns.md` (alvo ≥ 44px). Lei por trás: Fitts (`ux-laws.md`).
**Nuance (não contradição):** a regra antiga dizia "≥ 44px" sem distinguir plataforma. Agora: 44pt iOS / 48dp Android como mínimo nativo; na web 24px é só o piso de conformidade AA, o alvo de produto continua 44.

Checklist de auditoria **(complemento)**: medir `getBoundingClientRect()` de todo `button, a, [role=button], input[type=checkbox]` com Playwright; reprovar < 24px na web e < 44px em app/mobile; checar distância entre centros de ícones vizinhos (≥ tamanho do alvo + 8px).

### 1b. Fontes oficiais e NN/g (rodadas 9A e 9B)
| Fonte | Alvo padrão | Mínimo | Espaço entre alvos |
|---|---|---|---|
| **Apple HIG** (Accessibility) | **44 × 44 pt** (iOS/iPadOS/watchOS) · macOS 28 × 28 | **28 × 28 pt** (macOS 20 × 20) | ~**12 pt** de padding em elementos com bezel; ~**24 pt** sem bezel |
| **Material 3** | **48 × 48 dp** (≈ 9 mm; recomendado 7–10 mm); ícone 24 dp com padding até 48 | ponteiro (mouse) 44 × 44 dp | **≥ 8 dp** |
| **NN/g** (`touch-target-size`) | **1 × 1 cm** físico; ação primária/em movimento ~**2 × 2 cm** | — | ~2 mm, mas alvo grande primeiro |

- **Bate** com §1 (44pt/48dp, ~8px entre alvos). Novo: o **mínimo absoluto da Apple é 28pt** (para controle secundário em espaço apertado), não 44; 44 continua o padrão desta skill **(complemento)**: use 28 só em controle não primário e nunca abaixo do piso web de 24px.
- 1 cm físico ≈ 38–48 CSS px conforme a densidade da tela, ou seja, 44px já atende **(complemento)**. 1 dp ≈ 1 CSS px também é inferência da rodada, não da fonte.
- Detalhes do NN/g (view–tap asymmetry, mapas, idosos) em `nng-research.md` §3.

---

## 2. Escala tipográfica (`DfjxqzkCrUI`, @designmotionhq, carrossel de 8 folhas)
Gancho: "Random font sizes are a quick tell of a generated UI." O "antes" tem 6 tamanhos (52, 35, 32, 19, 18, 14px) com saltos irregulares (×1,49, ×1,09, ×1,68…).

| # | Regra | Número |
|---|---|---|
| 1 | Uma escala modular, uma razão | `size = 16 × 1,2^n`, arredondado e guardado como token: **16, 19, 23, 28, 33, 40, 48px** |
| 2 | Line-height cai conforme o tamanho cresce (sem unidade) | Corpo **16/24 = 1,5** · título **28/34 = 1,2** · display **48/53 = 1,1** |
| 3 | Tracking segue o tamanho | Títulos grandes **−0,02em**; corpo **0**; rótulos em caixa-alta **+0,06em** (ex.: 14px). Comece aí e ajuste a olho |
| 4 | Medida de linha | **45 a 75 caracteres**, `p { max-width: 60ch; }`. Conte na sua fonte |

Tokens da fonte (resumidos): `--text-0: 16px` … `--text-6: 48px`; `body` 16/1,5; `h2` 28/1,2; `h1` 48/1,1 com `letter-spacing: -0.02em`.

**Divergências com o que já está na skill (registrar, não apagar):**
- `DfPJo9UBJ7D` (`dark-patterns.md` §C) usa a hierarquia **40/24/18/14**. Só 40 cai na escala 1,2; 24, 18 e 14 não. As duas fontes concordam em "1 família, poucos pesos, hierarquia por tamanho"; divergem nos valores. Escolha **uma** escala por projeto e não misture.
- Botão primário com label **17px** (`Ddy5RJOha1U`) e ⌘K com input **26px / detalhes 14px** (`DeUr5-AhdvQ`) também ficam fora da escala 1,2. **(complemento)**: em componentes, arredonde para o degrau vizinho (17 → 16 ou 19; 26 → 28) se o projeto adotar a escala; se seguir a escala nativa iOS (17pt corpo), mantenha a nativa e não misture as duas.

### 2b. Escala 1,25 (Major Third): duas fontes novas, rodadas 1 e 2
**`DfRucYFjrac` (@designmotionhq, carrossel de 8 folhas, rodada 2).** O **mesmo autor** do `DfjxqzkCrUI` (razão 1,2), agora com outra razão. Gancho: "Type that looks designed is mostly four numbers."

| # | Regra | Número |
|---|---|---|
| 1 | Uma razão, todos os tamanhos (inclui 1 degrau de label abaixo da base) | `16 × 1,25^n`: **12,8 · 16 · 20 · 25 · 31,25 · 39,06 · 48,83px** (exibidos sem arredondar; resumo: 12,8/16/20/25/31/39/49). O "antes" ad hoc 14/18/21/30/36 tem razões todas diferentes |
| 2 | Line-height sem unidade, cai com o tamanho | **1,5** (16px → 24) · **1,4** (20 → 28) · **1,25** (31,25 → 39,1) · **1,1** (48,83 → 53,7). Título com line-height de corpo fica "solto": 73px vs 54px |
| 3 | Tracking por função, sempre em `em` | Títulos **≥ 39px: −0,02em** (−0,98px a 49px) · corpo **0** · labels caixa-alta pequenos **+0,05em** (+0,64px a 12,8px) |
| 4 | Medida | `max-width: 50ch` = **66–71 caracteres** nessa fonte; acima de **~75** o olho perde a linha (90ch = 125 caracteres). `ch` muda com a fonte: conte na sua |

Tokens da fonte (slide 6, `DfRucYFjrac_3.jpg`): `--step--1: 0.8rem` · `--step-0: 1rem` · `--step-1: 1.25rem` · `--step-2: 1.563rem` · `--step-3: 1.953rem` · `--step-4: 2.441rem` · `--step-5: 3.052rem`; `--lh-0: 1.5` · `--lh-1: 1.4` · `--lh-2: 1.3` · `--lh-3: 1.25` · `--lh-4: 1.15` · `--lh-5: 1.1`; `--measure: 50ch`; `h1, h2 { letter-spacing: -0.02em }`; `.label { letter-spacing: 0.05em }`. "Use cada degrau com o seu line-height."
Conferência da rodada: as contas batem. Erro menor do slide: a última razão "ad hoc" aparece como 1,28, mas 36 ÷ 30 = 1,20. A legenda fala em 4 passos de line-height, o slide 3 mostra 4 e o código usa 6. Último slide é propaganda do "UX Engine".

**`De_FtT3k-tT` (@gg.designhub, carrossel "Cheat Codes", rodada 1), slide #03 "Fail-Safe Type Hierarchy":** Major Third **1,250** arredondada: **16** Body · **20** Subhead · **25** H3 · **31** H2 · **39** Hero/H1 (`De_FtT3k-tT_2.jpg`). Slide #05: linha de **45–75 caracteres** (com espaços); entrelinha **140–160%** no corpo e **110–120%** em títulos. A capa promete 6 regras e entrega 5.

**DIVERGÊNCIA registrada (não apagar nenhuma):**
| Ponto | `DfjxqzkCrUI` (3A, @designmotionhq) | `DfRucYFjrac` (rodada 2, @designmotionhq) | `De_FtT3k-tT` (rodada 1, @gg.designhub) |
|---|---|---|---|
| Razão | **1,2** (16, 19, 23, 28, 33, 40, 48) | **1,25** (12,8 … 48,83) | **1,25** (16 … 39) |
| Line-height | 1,5 / 1,2 / 1,1 | 1,5 / 1,4 / 1,25 / 1,1 (código: 6 valores) | corpo 1,4–1,6; títulos 1,1–1,2 |
| Tracking caps | +0,06em | +0,05em | — |
| Medida | 45–75 car., `60ch` | `50ch` ≈ 66–71 car., teto ~75 | 45–75 car. |

Leitura: o mesmo perfil publicou as duas razões, então nenhuma é "a regra" dele. Todas concordam em **uma razão só, line-height caindo com o tamanho, tracking negativo em título e teto de ~75 caracteres**. **(complemento)** Como escolher: **1,2** para produto denso (dashboard, app, muitos níveis em tela pequena: saltos menores); **1,25** para site, landing e conteúdo editorial (mais contraste entre níveis). Escolha **uma** por projeto e registre nos tokens. O tracking caps de 0,05 ou 0,06em é diferença de ajuste fino: comece em 0,05em e ajuste a olho. Na escala 1,25, os componentes de §2 também ficam fora (17px do botão → 16 ou 20; 26px do ⌘K → 25).

### 2c. Escalas oficiais: Apple e Material 3 (rodada 9A)
- **Apple HIG (iOS/iPadOS)**: corpo padrão **17 pt**, mínimo **11 pt** (macOS 13/10; watchOS 16/12; visionOS 17/12). Texto deve poder crescer **200%**. Evitar pesos **Ultralight, Thin e Light**; preferir Regular, Medium, Semibold, Bold; fonte fina pede tamanho maior. Tracking do SF Pro varia por tamanho (17 pt −26/1000 em; 28 pt +14; 11 pt +6). Tabela capturada só no tamanho "xSmall" de Dynamic Type (Large Title 31, Body 14), **não** no padrão "Large": não use como escala.
- **Material 3**: escala **Major Second (1,125)** com base **14**, 30 estilos (15 baseline + 15 emphasized), Roboto, web em `rem` (16px = 1rem). Linha de texto **40–60 caracteres**. Line-height cresce ~7% em CJK/árabe e ~30% em birmanês/telugu.

**DIVERGÊNCIA registrada (não apagar):** Material usa **1,125 base 14**; esta skill usa **1,2** (produto denso) ou **1,25** (site), base **16** (§2 e §2b). Apple não publica razão: usa estilos nomeados com corpo 17. **(complemento)** Mantenha 1,2/1,25 base 16 por padrão; adote 1,125/14 só se o projeto seguir o Material à risca (app Android/Material You). O corpo 17pt da Apple já foi tratado em §2 (label 17px do botão: escala nativa iOS não se mistura com a modular). O mínimo de **11pt** (Apple) vale como piso para caption/legenda; na web, não use texto de leitura abaixo de 12px **(complemento)**. Medida: Material 40–60 car. × skill 45–75: as duas cabem em `50ch`.

---

## 3. Contraste em números (`DfuDHh3h14c`, @designmotionhq, reel)
"Your grey text passes the eye test. Not the checker." Contraste vai de 1:1 a 21:1; cinza claro sobre branco fica perto de 2:1.

| Elemento | Mínimo |
|---|---|
| Texto de corpo | **4,5:1** |
| Texto grande (**24px**, ou **19px bold**) | **3:1** |
| Ícones e bordas de input | **3:1** |
| Placeholder (continua sendo texto) | **4,5:1** (o exemplo falha a 1,7:1) |
| Texto sobre imagem | scrim escuro, medido **no ponto mais claro** da foto |
| Isentos | botões desabilitados e logos |

Também: use **cinzas sólidos por tema**, não preto a 50% de opacidade (o resultado muda conforme o fundo).
**Reforça** `components-checklists.md` §1 (label ≥ 4,5:1, borda ≥ 3:1). Nota: o limiar "19px bold" da fonte é arredondamento de 14pt bold (≈18,66px) da WCAG **(complemento)**.

---

## 4. Dark mode não é inversão (`DfSa0GRh-gS`, @motion_ui_interface, reel com 6 fixes)
1. **Fundo**: cinza-azulado profundo, nunca preto puro (`#000000 → #0C1424`).
2. **Texto**: branco a **87%**; detalhes em cinza.
3. **Accent**: clarear no escuro, contraste **2,9:1 → 8,6:1** (só na legenda).
4. **Elevação**: superfície mais alta = **mais clara**, não com sombra.
5. **Imagens**: reduzir brilho para **82%** (só na legenda; comentaristas notam que piora fotos já escuras).
6. **Glow em vez de sombra**: no escuro a luz faz o papel da sombra. Comentaristas acharam o glow do exemplo exagerado; use com parcimônia **(complemento)**.

## 5. Mesmos dados, 10 correções (`DfMN-fgIxOu`, @motion_ui_interface, app de clima)
Hierarquia antes de cor: o número que a pessoa veio ver fica enorme (**20 → 76px**) · **uma** borda esquerda (não 6) · **3 tamanhos de espaçamento** reutilizados (eram 5) · sem caps, itálico ou sublinhado · branco + 1 accent · cinza de apoio **1,9:1 → 6,7:1** · ícones num estilo e tamanho · agrupar por hora e por semana em 2 cards · barras de faixa em vez de lista · fundo que combina com o dado (céu vivo). Liga com Von Restorff e Proximity (`ux-laws.md`) e com o "número é o herói" de `dark-patterns.md` §B.

## 6. Espaçamento em grade de 8 (`De_FtT3k-tT`, @gg.designhub, slide #01)
- Todo espaçamento em **múltiplos de 8**: **8, 16, 24, 32, 48, 64px**.
- **4px** só para micro: padding de ícone compacto e micro-badges.
- Nunca ajuste à mão para valores como **13px** ou **27px**.
- A fonte diz que isso "elimina 90% da inconsistência entre breakpoints". Número sem fonte; trate como opinião.

Como isso conversa com o que já está na skill:
- **Bate**: Proximity **8px / 24px** (`ux-laws.md`), botão **48px** de altura e **24px** de padding, toast subindo 64px, "3 tamanhos de espaçamento reutilizados" do app de clima (§5).
- **Fica fora da grade, com motivo**: alvo de toque **44pt** (mínimo de plataforma, não espaçamento; 48dp do Android cai na grade); padding **12px** do ícone (20 + 12 + 12) é múltiplo de 4, aceito como "micro". **(complemento)**
- **Fica fora sem motivo forte**: chat com **18px** entre pessoas e ícone a **10px** do label (`components-checklists.md`). **(complemento)** Num sistema de 8, use 16 ou 24 para o chat e 8 para o ícone; o que importa é a **proporção** (4 dentro vs ~4× entre grupos), não o número exato.

Tokens **(complemento)**: `--space-1: 4px` (micro) · `--space-2: 8px` · `--space-3: 16px` · `--space-4: 24px` · `--space-5: 32px` · `--space-6: 48px` · `--space-7: 64px`. Auditoria: procurar no CSS `margin|padding|gap` com valores fora de {4, 8, 16, 24, 32, 48, 64} e justificar cada exceção.

## 7. Números em fonte de matriz de pontos (`DffCenmFASU`, @shohan.designs, rodada 7)
App fitness: "93%" (Workout Quality), "89%" (progresso semanal), "68%" (treino) em **fonte de matriz de pontos**, contrastando com o título bold. Dá identidade de "medidor" ao score sem ilustração. **(complemento)**: só para **1 número-herói** por tela (Von Restorff); use dígitos de largura fixa para não pular quando o valor muda e confira a legibilidade em tamanho pequeno. Para loader em matriz de pontos, veja `ext-transitions-dev` ("matrix dot loaders").

---

## Checklist rápido (copie para a auditoria)
- [ ] Todo alvo ≥ 44pt/48dp (app) ou ≥ 24px com meta 44 (web); área cresce por padding; ≥ 8px entre alvos pequenos. Mínimo Apple 28pt só em controle secundário; ação primária mobile maior (~2 cm, NN/g).
- [ ] Texto ≥ 11pt (Apple) e nunca em peso Thin/Light/Ultralight em tamanho pequeno; texto escala até 200%.
- [ ] Tamanhos de fonte vêm de **uma** escala (16 × 1,2^n **ou** 16 × 1,25^n, nunca as duas); nenhum tamanho "solto".
- [ ] Espaçamentos em múltiplos de 8 (4 só em micro); exceções justificadas.
- [ ] Line-height 1,5 no corpo caindo até 1,1 nos títulos grandes; tracking −0,02em em títulos grandes e +0,05–0,06em em caps.
- [ ] Parágrafos com `max-width` entre `50ch` e `60ch` (conte: 45–75 caracteres).
- [ ] Contraste: 4,5:1 texto e placeholder, 3:1 texto grande, ícones e bordas; scrim em texto sobre foto.
- [ ] Dark mode: sem #000, texto ~87%, accent clareado, elevação por luminosidade.
