# Camadas visuais e layout que transmite confiança

## 1. As "camadas" (@thedzianis, DfSIP2iBuFI; @thearseniodev, DfVlIwHISSv)

> "Same layout in all four — the layers are what people remember." — @thedzianis

O reel DfSIP2iBuFI mostra **a mesma landing page ("Relay" — headline "The handoffs run *themselves.*", diagrama de workflow à direita)** em 4 estados. O layout não muda; só se empilham camadas:

| # | Camada | O que muda na tela | Resultado dito |
|---|---|---|---|
| 0 | Zero design | Fundo cinza claro `#CBCBCB`-ish, wireframe, botões pretos padrão | "a landing page with zero design" |
| 0→1 | Transição | "Now add black": a mesma página escurece primeiro (cinza escuro), depois preto puro | — |
| 1 | **Identidade**: cor + tipografia | Fundo preto, **um acento acid lime `#C7F44F`** (CTA pill, badge do logo), headline sans + **segunda linha em serif itálico** ("*themselves.*"), labels em **mono** | "Now it has a personality" |
| 2 | **Profundidade**: luz + vidro | Um feixe/onda de luz verde-lime atrás de cards em **frosted glass** (painéis translúcidos com blur) | "Now it looks expensive" |
| 3 | **Movimento** | O stream de luz flui; o workflow "roda" (nós do diagrama animam) | "Now people stop scrolling" |

Os últimos frames mostram que as mesmas camadas continuam nas outras seções ("Most of a process is *glue*.", painel com barra de progresso lime): o sistema de camadas é aplicado ao site inteiro, não só ao hero.

Ordem prática: **identidade → profundidade → movimento**. Não pule para movimento sem identidade definida.

Tipografia da camada 1 (visto no card "Acid Lime" do reel): trio `Aa` sans / `Aa` serif itálico / `Aa` mono. Uso: sans no headline, serif itálico em 1 palavra/linha de ênfase, mono em labels/eyebrows/metadados.

DfVlIwHISSv reforça com "every site here is just three layers": **2 cores base + 1 elemento de destaque**, onde o terceiro "layer" pode ser:
- uma cor (black + electric blue + **neon green `#63F24B`** no CTA e em faíscas do orbe),
- **luz** (deep purple + soft teal + **Aurora Light `#66ACC5`** como brilho atrás do blob 3D iridescente: "Add the light behind it… now it's a movie"),
- **um objeto/cena** (sky blue + grass green + **uma TV antiga** num campo; depois "let the sun go down": céu em **sunset peach `#DC9F8D`** e tela da TV acesa: "now it's a memory").

Visual desses sites: hero full-bleed com objeto 3D central (orbe de vidro azul com ícone; blob iridescente roxo/verde; TV CRT em gramado com céu), headline curto (ex.: "Motion instead of chrome", "Turn data into decisions", "*Tape doesn't last.*" em script/itálico), nav mínima, 1 CTA.

## 2. Layout que parece seguro (@theglidestudio, DfyFShTounu)

> "Same words, different layout. Space, alignment and a calm rhythm say you're careful. Trust is built before anyone reads a word. A page that looks cared for gets believed."

O reel abre com "Which page looks safe?" e "Same words. Only the layout changed." e compara duas telas mobile escuras (fundo `#09090B`) com o mesmo conteúdo: "Your invoices, handled." + subtítulo + CTA "Get started" + lista de 3 itens (linhas com pílulas de status) + tab bar (Send / Track / Get paid).

Versão "insegura" (esquerda):
- headline grande espremido, margens apertadas;
- **dois botões** concorrendo ("Book a demo" + "Get started");
- itens da lista desalinhados, nav superior com muitos links;
- elementos extras (banner de cookie/aviso, botão de chat flutuante) colados no conteúdo.

Versão "segura" (direita), construída em 3 passos mostrados na tela — **"Space." → "Space. Alignment." → "Space. Alignment. Calm."**:
- **Espaço**: margens laterais generosas, mais ar entre headline, subtítulo, CTA e lista;
- **Alinhamento**: tudo numa única coluna/borda esquerda; lista dentro de um card com linhas de altura igual e pílulas de status alinhadas à direita;
- Nos frames de "Space. Alignment." aparece um **grid de colunas sobreposto** à tela segura (linhas verticais finas), e em "Calm." **faixas horizontais** marcando o espaçamento entre blocos — ou seja, o espaço vem de grid + escala vertical consistente, não de "olhômetro".
- **Ritmo calmo**: um único CTA primário (pílula branca), headline menor e de peso médio, hierarquia clara, ruído removido (nav reduzida a logo + "Sign in").

Fechamento: a versão segura sozinha com "Cared for gets believed."; logo glide (script branco com um ponto azul como único acento).

Regras práticas:
1. Um CTA primário por tela/seção; secundário vira link ou some.
2. Uma borda de alinhamento esquerda por coluna; nada "flutuando".
3. Espaçamento em escala consistente: múltiplos de 8 px (8, 16, 24, 32, 48, 64; 4 px só em micro-elementos), regra confirmada por @gg.designhub (`De_FtT3k-tT`, rodada 1). Seções com 2–3x o espaço interno dos cards (complemento). Grid de 8 pt, escala tipográfica e medida de linha (45–75 caracteres) em detalhe: skill `ux-patterns`.
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

Versão em carrossel do mesmo conteúdo (rodada 1): `Dff1uulGoxb` (@mobileeditingclub com @adrianabubori). Acrescenta
só a forma: um slide por efeito com título-comando ("/headline-reveal", "/scroll-reveal"), o prompt escrito acima do
mockup do navegador e fundos alternados creme `~#F4EEE6` / café `~#2E1F1C`. Valores de duração/easing ficam em `ui-motion`.

## 4. Sombra tingida (camada de profundidade) — @gg.designhub, `De_FtT3k-tT` (rodada 1)

Print `De_FtT3k-tT_3.jpg` ("Kill Pure Black Shadows"):
- **Erro de iniciante:** `rgba(0,0,0,.25)`: fica "sujo e artificial".
- **Regra:** pegue o **matiz do fundo/card**, baixe o brilho e use **opacidade baixa** (ex.: navy profundo para cards azuis).
- **Fórmula:** **blur = 2× o Y-offset**. Exemplo do post: Y 8 px · blur 16 px · opacidade 8%.

```css
/* complemento: tokens a partir da regra; troque o HSL pelo matiz do seu fundo */
:root {
  --shadow-hue: 222 60% 18%;                                   /* navy escuro do tema azul */
  --shadow-1: 0 4px 8px  hsl(var(--shadow-hue) / .08);         /* Y 4 · blur 8 */
  --shadow-2: 0 8px 16px hsl(var(--shadow-hue) / .08);         /* Y 8 · blur 16 (o exemplo do post) */
  --shadow-3: 0 16px 32px hsl(var(--shadow-hue) / .10);        /* elevação alta */
}
```

Como encaixa nas camadas: a sombra tingida é a versão "clara" da camada 2 (profundidade). Em tema escuro, as referências
desta skill usam luz/glow atrás de vidro em vez de sombra (§1); a sombra quase some sobre preto. **Divergência:** a
receita glass da `dashboard-ui` usa `box-shadow: 0 8px 32px rgba(0,0,0,.35)` (preto, blur 4× o Y). Ela é para vidro
escuro sobre foto, onde a sombra precisa separar o painel da imagem; a regra da @gg.designhub vale para superfícies
claras e chapadas. Não misture as duas na mesma tela.
