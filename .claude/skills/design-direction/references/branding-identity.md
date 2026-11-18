# Branding e identidade visual

Destilado da rodada 3 de perfis do Instagram: @gg.designhub (marca, logo, embalagem), @theglidestudio (movimento do
logo), @ramotion (sistemas de marca completos), @dailywebdesign (antes/depois de paleta, reposts de @ui.abraham e
@pierredelcourr), @rish_designs e @uidesignpatterns (direção de arte de páginas). Hex são estimativas de captura.
A fórmula de cor de base continua sendo o 2+1 de `color-palettes.md`; aqui está como ela vira **marca**.

## 1. A marca é julgada em ~3 segundos (@gg.designhub, DfyleZbk4Oz)

Antes de provar o produto, o cliente já decidiu se a marca é "barata", "nova e pequena" ou "confiável". Os 5 pontos
de contato comparados (✗/✓) no carrossel:

| Ponto de contato | ✗ passa a impressão de… | ✓ passa a impressão de… |
|---|---|---|
| Placa/fachada | suja, enferrujada → "loja barata" | limpa → "loja confiável" |
| Logo | parece ícone de app grátis → "nova e pequena" | símbolo próprio → "marca de verdade" |
| Cores | 5 cores brigando → "confuso" | **2 ou 3 cores → "confiante"** |
| Perfil no Instagram | sem logo, sem bio, posts aleatórios → saem antes do DM | logo, destaques, feed consistente |
| Embalagem | capa lisa → "produto local" | caixa com marca → "vale mais" |

Regra: **consistência e clareza valem mais que parecer caro.** Bom branding é parecer coerente e certo para o
negócio, não sofisticado.

## 2. Logo: 6 erros de iniciante (@gg.designhub, Dfv9GTJE0Av)

1. **Elementos demais** — cada forma precisa de função; "Hill Valley Resorts" com montanha+sol+cabana+árvores → só a montanha.
2. **Fonte sem propósito** — a fonte comunica personalidade; escolha pelo caráter e público, não pelo enfeite.
3. **Ignorar escala** — teste em tamanho de ícone de app; detalhe fino some pequeno.
4. **Depender de cor** — o logo precisa funcionar **em preto e branco chapado**; degradê não é muleta.
5. **Seguir tendência** — degradê da moda envelhece; relevância e originalidade duram.
6. **Desenhar sem entender a marca** — antes: objetivos do negócio, público, posicionamento, valores, direção visual.

Checklist rápido (complemento): 1 ideia central · legível a 16–32 px · versão 1 cor · funciona em fundo claro e escuro.

## 3. Embalagem comunica preço (@gg.designhub, DfuCgQ4zpgI)

"Mesmo biscoito, mesma receita, mesma fábrica" em três embalagens = três preços percebidos (₹10 → ₹150).

| Faixa | Cor | Tipografia | Composição | Leitura |
|---|---|---|---|---|
| Budget | vermelho/laranja vivos, cores altas | bold, grande | ofertas ("25% EXTRA"), selos, pouco espaço | "barato" |
| Mid-range | azul + bege, selo verde "VALUE" | sans limpa | benefício explícito ("made with real butter") | "confiável, bom valor" |
| Premium | **preto + dourado** | **serifa discreta** | **muito espaço vazio**, holofote | "caro" |

Regras:
- **Defina o preço e o posicionamento primeiro; depois desenhe para ele.**
- Design caro em produto barato (ou o contrário) é *mismatch* → perda de vendas. Não "deixe tudo premium".
- Vale para web também (complemento): landing de produto barato com serifa+dourado+vazio promete o que não entrega;
  SaaS premium com selos e cores gritando parece promoção.

## 4. Movimento do logo (@theglidestudio, Dfzkwu3hSj5)

"O logo ganha um segundo; o movimento é parte do logo." Mesmo símbolo, três personalidades, todas em 1,00 s:

| Movimento | Personalidade |
|---|---|
| Desenhado numa linha única e lenta (traço percorre o contorno) | **Calm** |
| Peças que se encaixam rápido (snap) | **Quick** |
| Cresce a partir de um ponto | **Friendly** |

Escolha o movimento pela personalidade da marca **antes** de animar; apresente as variações lado a lado com a mesma
duração para o cliente comparar. Implementação (easing, stroke-dashoffset, springs): skill `ui-motion` /
`ext-gsap-*`.

## 5. Sistemas de marca da Ramotion (Dak9nkTFpYI, DSIMwtvDluO, DVg6uh7AV25)

Os três cases repetem a mesma fórmula — é o 2+1 expandido para um sistema inteiro:

> **1 cor de marca saturada + preto/escuro + 1–2 cores de apoio**, tipografia **display larga só em títulos** e uma
> sans neutra (**Inter**) no corpo.

| Case | Marca (saturada) | Escuro | Apoio | Tipo | Notas |
|---|---|---|---|---|---|
| Source (infra edge para devs) | Green `#06B250` | `#0D0F0E` / cinza-verde `#1E2422` | Laranja `#F7A21B`, Ciano `#16B4F2` | **Funnel Display** (títulos) + **Inter** (corpo) | Paleta em "pastas" empilhadas com rótulo mono `GREEN #06B250 / R:6 G:178 B:80`; 1 palavra do título em verde ("magic ✦"); tags `// PRODUCT PAGES`, grid, halftone, ícones pixelados = "feito para devs" |
| Borea AI (investimentos com IA) | Azul `#3D5BF5` | quase preto / radial roxo `#2A1830 → #0B0B10` | Laranja `#F26B3A` (gradiente azul→laranja no símbolo) | sans geométrica larga e pesada | Verde/vermelho **só** para variação de preço; pilha de palavras esmaecidas com 1 em branco ("*Transparent*") |
| Murf AI (voz por IA) | gradiente roxo `#7B5CF5` → magenta `#E0368A` → laranja `#F7A21B` | roxo escuro `#2A1240` | lavanda `#EFE9FB`, pastéis por categoria | sans | O **mesmo gradiente** em logo, borda de moldura, palavra-chave do título e CTA — consistência faz o gradiente virar marca |

Regras tiradas dos cases:
1. Documente cada cor com **hex e RGB** no próprio brand book.
2. Display marcante **só** em títulos; corpo sempre em sans neutra (Inter). Nunca a display em parágrafo.
3. Destaque **uma** palavra do título com a cor de marca.
4. Ordem de apresentação do sistema (útil para pedir ao Claude Design ou montar um brand book):
   **logo → construção (grid, círculos, ângulos) → paleta + tipo → ícones/componentes → telas completas → aplicações (outdoor, mockups)**.
5. Desenhe também 404 e estados vazios dentro do sistema (Borea tem 404 "Oops! We've Hit a Snag").
6. Linguagem visual pode carregar o público sem ilustração literal (mono + `//` + grid = devs).
7. Revise dados nos mockups: o case Borea mostra o ticker da Apple como "APPL" (correto: AAPL).

Prints: `Dak9nkTFpYI_1.jpg` (paleta em pastas), `Dak9nkTFpYI_2.jpg` (par Funnel Display + Inter),
`Dak9nkTFpYI_3.jpg` (página de produto escura, acento laranja), `DVg6uh7AV25_2.jpg` (hero com gradiente de marca).

## 6. Antes/depois de paleta (@dailywebdesign)

**Home de app imobiliário (repost de @ui.abraham, DfzgxEKlx8z)** — mesma função, paleta trocada:
- Antes: coral no header + filtros com contorno laranja + bloco em gradiente azul-lilás + ícones laranja → paleta mista,
  sem hierarquia; a home abria com estado vazio "No properties found".
- Depois: **um azul só** (`~#3F6F9A`) + neutros; banner com ilustração e 1 CTA branco "Explore Properties"; filtros em
  pílula com **um** estado ativo escuro; cartões com foto grande, selo, nota e preço.
- Lição: reduzir para 1 cor de marca resolve mais que "melhorar" cada cor; a cor ativa precisa ser única.

**Combinações explicadas (repost de @pierredelcourr, DfmovsHjtmH)** — cada combo = 1 base escura + 1 fundo suave +
1 acento quente, mostrado aplicado em mockups (logo, bolsa, boné, post, embalagem), não só como swatch:

| Marca fictícia | Base escura | Fundo suave | Acento quente |
|---|---|---|---|
| Repalo (tênis) | Midnight Navy `~#0B2A4A` | Soft Blue `~#BDE0F3` | Coral Orange `~#FF6B5E` |
| Woofers (restaurante) | Deep Burgundy `~#7A1F2B` | Pale Pink/creme `~#F7E8D8` | Mustard `~#F2B01E` |
| (Helvetica Family) | Neon Black `~#111111` | Powder Blue `~#B5D8F0` | Poppy Red `~#E5262D` |

Também: **dê nome às cores** (Soft Blue, Midnight Navy) — ajuda a memorizar e a comunicar com cliente e com o Claude.
Essas três entraram no catálogo de `color-palettes.md`.

## 7. Direção de arte de páginas de marca

- **Scroll-storytelling de produto** (@rish_designs, site conceito RWB Porsche, DYpD5C7zwx6): cada seção = **1
  palavra-título gigante + 1 ângulo do produto 3D**; alternar fundo escuro/claro marca troca de capítulo; **texto atrás
  do objeto** (oclusão) dá profundidade; título misto outline + sólido ("THE / HERITAGE") hierarquiza sem trocar de
  fonte; navbar mínima com um único CTA colorido. Prints `DYpD5C7zwx6_1.jpg`, `DYpD5C7zwx6_2.jpg`.
- **Foto em tons de cinza com um ponto de cor** (@uidesignpatterns, DSUPZJUjRwO: astronauta PB com viseira rosa) cria
  foco sem paleta extra; serifa fina grande + menu em mono caixa-alta pequena = tom editorial.
- **404 como peça de marca** (@uidesignpatterns, DaFury4qJHn): foto de personalidade em tela cheia, "404" grande,
  frase em serifa itálica, CTA contornado de volta. Mantenha a saída visível.
- **Portfólio em que o movimento é a identidade** (@uidesignpatterns, DcyWWw-hCTz): miniaturas que se reorganizam em
  formas sobre cinza neutro (só inspiração; implementar via `ui-motion`).

## 8. Workflow de identidade (complemento, combinando as fontes)

1. Pesquisa (objetivos, público, posicionamento, valores) e **faixa de preço**.
2. Paleta: 1 saturada de marca + escuro + 1–2 apoio (ou 2+1 clássico); nomeie e documente hex/RGB.
3. Par tipográfico: display só em títulos + Inter (ou sans neutra) no corpo; 12 pares prontos por tom em `typography-pairing.md`.
4. Logo: 1 ideia; testar pequeno e em P&B; escolher o movimento (calm/quick/friendly).
5. Aplicar nos 5 pontos de contato (fachada/site, logo, cores, perfil social, embalagem) e conferir consistência.
6. Desenhar 404/vazios no sistema; revisar dados reais dos mockups.
