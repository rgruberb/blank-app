# Camadas visuais e layout que transmite confiança

## 1. As "camadas" (@thedzianis, DfSIP2iBuFI; @thearseniodev, DfVlIwHISSv)

> "Same layout in all four — the layers are what people remember." — @thedzianis

O reel DfSIP2iBuFI mostra **a mesma landing page ("Relay" — headline "The handoffs run *themselves.*", diagrama de workflow à direita)** em 4 estados. O layout não muda; só se empilham camadas:

| # | Camada | O que muda na tela | Resultado dito |
|---|---|---|---|
| 0 | Zero design | Fundo cinza claro `#CBCBCB`-ish, wireframe, botões pretos padrão | "a landing page with zero design" |
| 1 | **Identidade**: cor + tipografia | Fundo preto, **um acento acid lime `#C7F44F`** (CTA pill, badge do logo), headline sans + **segunda linha em serif itálico** ("*themselves.*"), labels em **mono** | "Now it has a personality" |
| 2 | **Profundidade**: luz + vidro | Um feixe/onda de luz verde-lime atrás de cards em **frosted glass** (painéis translúcidos com blur) | "Now it looks expensive" |
| 3 | **Movimento** | O stream de luz flui; o workflow "roda" (nós do diagrama animam) | "Now people stop scrolling" |

Ordem prática: **identidade → profundidade → movimento**. Não pule para movimento sem identidade definida.

Tipografia da camada 1 (visto no card "Acid Lime" do reel): trio `Aa` sans / `Aa` serif itálico / `Aa` mono. Uso: sans no headline, serif itálico em 1 palavra/linha de ênfase, mono em labels/eyebrows/metadados.

DfVlIwHISSv reforça com "every site here is just three layers": **2 cores base + 1 elemento de destaque**, onde o terceiro "layer" pode ser:
- uma cor (black + electric blue + **neon green**),
- **luz** (deep purple + soft teal + luz atrás de uma esfera 3D iridescente: "now it's a movie"),
- **um objeto/cena** (sky blue + grass green + uma TV antiga num campo, com pôr do sol em sunset peach: "now it's a memory").

Visual desses sites: hero full-bleed com objeto 3D central (orbe de vidro azul com ícone; blob iridescente roxo/verde; TV CRT em gramado com céu), headline curto (ex.: "Motion instead of chrome", "Turn data into decisions", "*Tape doesn't last.*" em script/itálico), nav mínima, 1 CTA.

## 2. Layout que parece seguro (@theglidestudio, DfyFShTounu)

> "Same words, different layout. Space, alignment and a calm rhythm say you're careful. Trust is built before anyone reads a word. A page that looks cared for gets believed."

O reel compara duas telas mobile escuras (fundo `#09090B`) com o mesmo conteúdo: "Your invoices, handled." + subtítulo + CTA "Get started" + lista de 3 itens (linhas com pílulas de status) + tab bar (Send / Track / Get paid).

Versão "insegura" (esquerda):
- headline grande espremido, margens apertadas;
- **dois botões** concorrendo ("Book a demo" + "Get started");
- itens da lista desalinhados, nav superior com muitos links;
- elementos extras (banner de cookie/aviso, botão de chat flutuante) colados no conteúdo.

Versão "segura" (direita), construída em 3 passos mostrados na tela — **"Space." → "Space. Alignment." → "Space. Alignment. Calm."**:
- **Espaço**: margens laterais generosas, mais ar entre headline, subtítulo, CTA e lista;
- **Alinhamento**: tudo numa única coluna/borda esquerda; lista dentro de um card com linhas de altura igual e pílulas de status alinhadas à direita;
- **Ritmo calmo**: um único CTA primário (pílula branca), headline menor e de peso médio, hierarquia clara, ruído removido (nav reduzida a logo + "Sign in").

Regras práticas:
1. Um CTA primário por tela/seção; secundário vira link ou some.
2. Uma borda de alinhamento esquerda por coluna; nada "flutuando".
3. Espaçamento em escala consistente (complemento: múltiplos de 4/8px; seções com 2–3x o espaço interno dos cards).
4. Remova widgets que competem com o conteúdo acima da dobra (chat, banners) ou afaste-os.
5. Headline curto e sem gritar; confiança vem da calma, não do tamanho.

## 3. Movimento no site (@mobileeditingclub, Dff1kjUiR4o — só texto)

Cinco tipos de movimento sugeridos para pedir ao Claude:
1. **Headline reveal** — animação curta de abertura; manter legível e o movimento sutil.
2. **Micro-interactions** — hover effects, image shifts, transições suaves entre detalhes de produto.
3. **Portfolio showcase** — transições guiando o visitante pelos projetos, dando contexto a cada um.
4. **Animated gallery** — revelar imagens uma após a outra, "each project gets its moment".
5. **Scroll reveal** — imagens, detalhes e texto de apoio entram conforme o scroll.

Processo: entregue ao Claude **seus visuais, cores da marca e uma descrição clara do movimento**; **construa um efeito por vez**; revise **em desktop e mobile**.

(complemento) Respeite `prefers-reduced-motion`; anime `transform`/`opacity`. Para implementação use as skills `ui-motion` e `ext-gsap-*` (ScrollTrigger para scroll reveal).
