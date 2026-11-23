# Par tipográfico (font pairing)

Fontes: infográfico "Font Pairing" de @gfx.om (`DescJ2zTeSf`, imagem única, 19/10/2026, selo "AI content"; print
`DescJ2zTeSf_1.jpg`), somado ao que a skill já tinha: trio de identidade (@thedzianis, `layers-and-trust-layout.md` §1)
e display + Inter dos sistemas da Ramotion (`branding-identity.md` §5). **Escala tipográfica, line-height, tracking e
medida de linha não ficam aqui**: estão na skill `ux-patterns` (`../../ux-patterns/references/typography-and-touch.md`).

## 1. Regras (as 4 "Quick Tips" do post, mais o que se repete nas outras fontes)

1. **2–3 famílias no máximo** por projeto. A hierarquia vem dos **pesos** (Bold/Display no título, Medium/Semibold no
   subtítulo, Regular/Light no corpo), não de mais fontes.
2. **Contraste entre display e corpo**: uma fonte com personalidade (serif, display, script ou condensada) nos
   títulos e uma sans neutra e legível no corpo. Duas fontes "parecidas" (duas grotescas) não formam par, só confundem.
3. **Escolha pelo tom da marca** (luxo, tech, amigável, editorial) e pela faixa de preço (`branding-identity.md` §3:
   premium = serifa discreta; budget = display alta e pesada).
4. **O mesmo par em tudo**: site, app, social, embalagem. Trocar de par entre peças quebra a marca.

## 2. Os 12 pares do post (título + corpo)

As bolinhas de cor de cada card são só ilustração; não são paleta recomendada.

| # | Tom (rótulo do post) | Título | Corpo | Quando usar (complemento) |
|---|---|---|---|---|
| 1 | Modern & Clean | Playfair Display | Montserrat | editorial, moda, portfólio |
| 2 | Bold & Minimal | Montserrat | Lato | SaaS e institucional sem serifa (contraste só de peso: par fraco) |
| 3 | Elegant & Classic | Bodoni Moda | Poppins | beleza, luxo acessível |
| 4 | Creative & Stylish | Pacifico | Montserrat | comida, infantil, eventos; script só em 1–3 palavras |
| 5 | Strong & Modern (o post diz isso, mas é par serif + sans clássico) | Lora | Open Sans | blog, educação, saúde |
| 6 | Minimal & Stylish | Helvetica Neue | Source Sans Pro | corporativo; **Helvetica Neue é comercial** (não está no Google Fonts) |
| 7 | Vintage & Classic | Abril Fatface | Raleway | cafeteria, cervejaria, pôster |
| 8 | Tech & Modern | Rajdhani | Roboto | dashboards técnicos, games, IoT |
| 9 | Soft & Friendly | Quicksand | Nunito | app de bem-estar, infantil, onboarding leve |
| 10 | Luxury & Premium | Cormorant Garamond | Lato | hotelaria, joias, vinho |
| 11 | Edgy & Bold | Anton | Muli (hoje se chama **Mulish** no Google Fonts) | streetwear, esporte, campanha |
| 12 | Fresh & Modern | Fraunces | Inter | startup com tom humano; casa com o trio sans/serif itálico |

Erros e cuidados do post: rótulo 5 não bate com o par; "Muli" foi renomeada; Helvetica Neue exige licença
(pergunta que apareceu nos comentários). Fora isso, todas estão no Google Fonts (verifique o nome atual antes de usar).

## 3. Como isso conversa com o que a skill já tinha

| Padrão | Fonte | Estrutura | Observação |
|---|---|---|---|
| **Par display + corpo** | @gfx.om | 2 famílias, contraste por estilo | regra geral; a base para escolher |
| **Trio de identidade** | @thedzianis (`DfSIP2iBuFI`), Relay (`Dd9nhiOyrZU`) | sans no headline, **serif itálico em 1 palavra**, mono em labels | 3 famílias, dentro do limite de 2–3 |
| **Display só em títulos + Inter** | @ramotion (`Dak9nkTFpYI_2`: Funnel Display + Inter) | 2 famílias, display larga | igual ao par 12 do post (display + Inter) |
| **Display condensada + serif itálico** | @niki.aroca (`DfKxflroHj3`) | "CREATE *without* LIMITS" | a serif itálica faz a ênfase |
| **Script + grotesca pesada** em capa | @craftwork.design (`DfKaOBqjUr4`, rodada 5; print `DfKaOBqjUr4_1.jpg`) | "Selected / **Design skills** / Part 2" | 3 camadas tipográficas só na capa; não leve o script para o corpo |

**Divergência registrada:** o post fala em 2–3 fontes e mostra só pares; o trio da skill (sans + serif + mono) usa as 3.
Os dois cabem na regra se o mono ficar só em rótulos/metadados e a serif só em ênfase. Nenhuma fonte indica 4 famílias.

## 4. Workflow rápido (complemento)

1. Defina o tom em 1 palavra (luxo / tech / amigável / editorial / ousado) e a faixa de preço.
2. Escolha 1 par da tabela (ou uma variante: troque a sans de corpo por Inter se o projeto for app/dashboard).
3. Decida se entra a 3ª família (mono para dados/labels, ou serif itálico para ênfase). Nunca as duas e mais um script.
4. Monte a escala e o line-height com `ux-patterns` (`typography-and-touch.md`); só depois teste o par em título
   longo, número grande (tabular) e texto de botão.
5. Em brand book, documente: nome da família, pesos usados, onde cada uma entra (como os rótulos mono da Ramotion:
   "FUNNEL DISPLAY – HEADLINES / INTER – BODY").

## 5. Onde buscar fontes (Typewolf, rodada 9C; print `9C_typewolf_google-fonts_1.jpg`)

- https://www.typewolf.com/google-fonts — "The 40 Best Free Fonts Available on Google Fonts" (atualizado 12/01/2026):
  todas open source e livres para uso comercial, só famílias com **vários pesos** (evita display de peso único). Um
  asterisco marca famílias boas para **texto corrido** (pesos regular/itálico/negrito, contraste baixo, aberturas
  grandes, x-height alta).
- A home "What's Trending in Type" mostra sites reais com as fontes (ex.: Neue Montreal, Suisse Int'l, DM Sans,
  Switzer); várias são **pagas** (Neue Haas, Suisse, Canela): confira a licença antes de propor, inclusive para embutir
  em app (Capacitor/Electron).
- Os pares recomendados do Typewolf ("The Definitive Guide to Free Fonts") **não foram extraídos**; use os 12 pares da §2.
- Complemento: confira suporte a acentos do português (ã, ç, õ) na página da fonte antes de fechar o par.

