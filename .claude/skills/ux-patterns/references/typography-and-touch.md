# Alvos de toque, escala tipográfica e contraste

Regras numéricas de 3 carrosséis/reels do @designmotionhq (série "DMHQ / UI Geometry") e de 2 reels do @motion_ui_interface. Os números são das fontes; o que está marcado **(complemento)** é inferência ou ajuste nosso.

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

---

## Checklist rápido (copie para a auditoria)
- [ ] Todo alvo ≥ 44pt/48dp (app) ou ≥ 24px com meta 44 (web); área cresce por padding; ≥ 8px entre alvos pequenos.
- [ ] Tamanhos de fonte vêm de **uma** escala (ex.: 16 × 1,2^n); nenhum tamanho "solto".
- [ ] Line-height 1,5 / 1,2 / 1,1 conforme o tamanho; tracking −0,02em em títulos grandes e +0,06em em caps.
- [ ] Parágrafos com `max-width: ~60ch`.
- [ ] Contraste: 4,5:1 texto e placeholder, 3:1 texto grande, ícones e bordas; scrim em texto sobre foto.
- [ ] Dark mode: sem #000, texto ~87%, accent clareado, elevação por luminosidade.
