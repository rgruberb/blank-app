# Paletas: 2 cores base + 1 acento

Fórmula repetida em 4 reels (@niki.aroca x2, @pierredelcourr, @diego.a.does) e também em @thearseniodev (DfVlIwHISSv):

> "The first two colors set the mood. The accent gives it personality." — @niki.aroca
> "Two colors that get along, and one that doesn't. That one only goes on the button you want to get clicked." — @diego.a.does
> "You don't need more colors. You just need one color that surprises people." — @niki.aroca

## Regras destiladas

1. **Duas cores base que "se dão bem"** (mesma família de temperatura/saturação, ou neutro + cor) definem o clima. Sozinhas parecem "fine", "clean but a little cold", "corporate", "a bit forgettable".
2. **Uma cor de acento que "não combina"** — contraste de matiz e alta saturação/luminosidade em relação às bases. É ela que torna a marca memorável ("now you'd recognize it anywhere", "now people screenshot it").
3. **O acento vai só no que deve ser clicado/lembrado.** Nos exemplos visuais o acento aparece em: botão CTA primário, um badge, uma palavra sublinhada no headline, um ícone, um detalhe de produto. Nunca em fundos grandes.
4. **Quantidade: "a little", "a touch", "a hint", "one splash".** Na prática dos frames, o acento ocupa uma fração mínima da tela (estimativa (complemento): ~5–10% da área; o resto fica em base 1 + base 2).
5. Uma combinação 2+1 funciona em contextos além de site: identidade de marca, packaging, social (Dfa860wIQn4 mostra grids de marca e embalagem).

## Catálogo completo das combinações citadas

Hex = aproximado, amostrado dos swatches nos frames (vídeo comprimido; os rótulos de hex originais são ilegíveis). Use como ponto de partida e ajuste contraste.

| Base 1 | Base 2 | Acento | Efeito descrito | Fonte |
|---|---|---|---|---|
| Charcoal Black `#24222D` | Royal Blue `#1657F9` | Tangerine Orange `#F17E07` | "completely different vibe" | DfIaULMIRC- |
| Marshmallow White `#EDEDEF` | Galactic Violet `#5630F7` | Bubblegum Pink `#F353CF` | "pretty basic" → "looks premium" | DfIaULMIRC- |
| Aqua Jade `#82FFEE` | Midnight Abyss `#171C44` | Baby Pink `#F66ACB` | "already a great combo" → "impossible to ignore" | DfIaULMIRC- |
| Mandarin Orange `#F0450D` | Forest Green `#076849` | Crest Yellow (swatch não aparece nos frames) | "now you know exactly where to click" | DfKxflroHj3 |
| Onyx Black `#02000B` | Electric Indigo `#621CF6` | Tropical Mint `#91FFBF` | "a bit forgettable" → "you'd recognize it anywhere" | DfKxflroHj3 |
| Seal Blue `#DDF1FA` (azul gelo) | Navy Blue `#092C54` | Crimson Pink (swatch não aparece) | "the whole page comes together" | DfKxflroHj3 |
| Obsidian Black `#12121A` | Ice Grey `#E0E5E9` | Racing Red `#DF0A40` | "clean but cold" → "the whole brand has energy" | Dfa860wIQn4 |
| Deep Charcoal `#1C171E` | Electric Violet `#7226F8` | Acid Lime (swatch não aparece; ver `#C7F44F` de DfSIP2iBuFI) | "now try scrolling past it" | Dfa860wIQn4 |
| Raspberry Pink `#B10050` | Pale Pink `#FBCAE0` | Butter Yellow `#F7E86B` | "soft and playful" → packaging chama atenção | Dfa860wIQn4 |
| Cream `#F4EEE0` | Ink Black `#10120F` | Burnt Orange `#CD481D` | "fine" → "now it's a Y Combinator startup" | Dfc-Q-0yy0W |
| Navy `#0D1838` | White `#FFFFFD` | Hot Pink `#EF2289` | "corporate" → "now people screenshot it" | Dfc-Q-0yy0W |
| Charcoal `#1E1F1A` | Sand `#D1CAB0` | Electric Blue `#3564F2` | "calm" → "now it's Series A" | Dfc-Q-0yy0W |
| Midnight Black `#060606` | Electric Blue `#1236D2` | Neon Green | "clean" → "you can't look away" | DfVlIwHISSv |
| Deep Purple `#572DB7` | Soft Teal `#42CA98` | luz/brilho (não uma cor; camada de luz) | "cool" → "now it's a movie" | DfVlIwHISSv |
| Sky Blue `#3D5DCA` | Grass Green `#2C6835` | Sunset Peach `#D79E95` + objeto (TV antiga) | "now it's a memory" | DfVlIwHISSv |
| Preto (dark UI) | cinza/branco do texto | Acid Lime `#C7F44F` | "now it has a personality" | DfSIP2iBuFI |

## Padrões que se repetem nas combinações

- **Base escura + base saturada fria, acento quente/neon**: charcoal+royal blue → laranja; onyx+indigo → mint; deep charcoal+violet → lime; black+electric blue → neon green.
- **Base clara neutra + base escura, acento quente saturado**: cream+ink → burnt orange; navy+white → hot pink; obsidian+ice grey → racing red.
- **Duas bases da mesma família (monocromático), acento complementar**: raspberry+pale pink → butter yellow; seal blue+navy → crimson pink.
- **Acento quase sempre complementar ou oposto em temperatura** às bases (azul↔laranja, violeta↔lime/mint, rosa↔amarelo, verde↔rosa/pêssego).
- Nenhum exemplo usa mais de 3 cores de marca (fora fotos/ilustração).

## Como aplicar no código (complemento)

- Defina tokens: `--base-1`, `--base-2`, `--accent` (+ derivados de texto/borda/hover). Não crie um quarto token de marca.
- Use `--accent` apenas em: CTA primário, estado ativo/foco, 1 destaque tipográfico por seção, indicadores de dado-chave.
- Cheque contraste do texto sobre o acento (WCAG AA 4.5:1 para texto normal). Acentos neon/lime/mint pedem texto escuro; racing red/hot pink/burnt orange/electric blue normalmente aceitam texto branco.
