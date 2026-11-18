# Motion para reel, vídeo de produto e logo

Regras para motion **fora do app**: texto em reel, vídeo de produto/demo de site, logo animado e carrossel educativo. Fontes: @theglidestudio (rodada 3A), @rish_designs, @roman.knox via @ultimateuiux e @ramotion (3B), @uidesignpatterns (3C). Inferências estão marcadas **(complemento)**. A parte de marca (escolher personalidade, paleta, logo estático) fica na skill `design-direction`; aqui fica só o movimento.

---

## 1. Texto em reel (`DfxpIbfP-SB`, @theglidestudio)
"Você tem um segundo para ler isto." A maior parte do texto de reel some antes de a pessoa terminar.
1. **No máximo 6 palavras por tela, em tamanho grande.**
2. **Segure ~1,2 s** ("uma respiração inteira") cada texto.
3. **Teste**: se não dá para ler **duas vezes**, está rápido demais.
4. O próprio vídeo mostra o ritmo como recurso visual: timecode em mono e barra de progresso fina com um ponto de cor.
5. Movimento observado: o texto entra com **blur e sobe**, trocando palavra a palavra.

**Reforça** a duração de "cena" do mesmo estúdio (`Dfvja0XCyIi`, `page-transitions-and-timing.md`): 1,2 s é o tempo de uma cena completa e de um texto de reel. Use o token `--dur-scene`.
**(complemento)**: para frases maiores que 6 palavras, quebre em telas sucessivas de ≤ 6 palavras, cada uma com 1,2 s; a entrada (blur + subida) deve caber num reveal curto (~300–500 ms) dentro desse tempo, não somar a ele.

## 2. Logo animado (`Dfzkwu3hSj5`, @theglidestudio)
"Seu logo ganha um segundo. Use." O movimento faz parte do logo.
| Movimento | Personalidade |
|---|---|
| Desenhado em **uma linha única e lenta** (traço percorrendo o contorno) | **Calmo** |
| Peças que **se encaixam rápido** | **Rápido** |
| **Cresce a partir de um ponto** | **Amigável** |
- Duração de referência: **~1,00 s** (régua de 0 a 1,00 s no vídeo).
- Escolha o movimento pela personalidade da marca **antes** de animar.
- Apresente as variações **lado a lado, com a mesma duração**, para o cliente comparar.
- **(complemento)**: o logo animado deve terminar parado na forma estática final; em `prefers-reduced-motion` mostre direto o logo final ou um fade curto.

## 3. Site em vídeo de produto: título primeiro (`Dfy7ig_B-FL`, @theglidestudio)
"Uma página em branco por dois segundos parece uma hora." Mostre o **título primeiro** e deixe o resto deslizar para dentro (no exemplo, os cartões de um calendário entram em cascata). Uma página que responde na hora parece uma empresa que responde. Vale para o site real (ver `page-transitions-and-timing.md`) e para o vídeo de demo: não abra o vídeo com o site carregando.

## 4. Scroll-storytelling de site conceito (`DYpD5C7zwx6`, @rish_designs via @ultimateuiux, site "RWB Porsche")
- Cada seção = **uma palavra-título gigante + um ângulo do produto 3D** (HERITAGE, PERFECTION, DRIVE).
- **Alternar fundo escuro e claro** entre seções marca a troca de capítulo.
- **Texto atrás do objeto 3D** (oclusão) dá profundidade sem ilustração extra.
- Título misto **outline + sólido** ("THE / HERITAGE") hierarquiza sem trocar de fonte.
- Navbar mínima com um só CTA colorido.
- Liga com a linha "Storytelling/produto" de `scroll-and-screen-transitions.md` (pin + scrub) e vale só para landing/conceito, nunca para tela de trabalho.
- Visual: `DYpD5C7zwx6_1.jpg` (seção escura) e `DYpD5C7zwx6_2.jpg` (seção clara com oclusão). Prints pequenos, de baixa resolução.

## 5. Carrossel educativo (`DXZUwW2jca_`, @roman.knox via @ultimateuiux, "Claude skills for designers")
Template fixo por slide: **número grande → título em 2 linhas → 1 frase de benefício → bloco de ação (comando) → paginação "N/7" + botão "swipe"**. Um accent só (laranja) e gradiente no título dão unidade aos 7 slides. Erro do próprio post: a numeração pula do 5 para o 7. Revise numeração e contagem antes de publicar.
Conteúdo citado (só como referência; comandos não verificados): skills frontend-design, figma, theme-factory, brand-guidelines, canvas-design e skill-creator. Visual: `DXZUwW2jca__1.jpg`.

## 6. Outros formatos observados
- **Reel de "fixes" numerados** (@motion_ui_interface, `DfSa0GRh-gS`, `DfMN-fgIxOu`, `DfRkH5LIHgZ`): barra de progresso segmentada no topo (6 ou 10 partes), contador "FIX 0N / 6" em mono, título com uma palavra-chave no accent e uma **pílula antes → depois** com o número ("TEMP 20 px → 76 px"). Uma dica por cena, ~50–60 s no total. Bom formato para vídeo de produto que explica mudanças.
- **Vídeo dentro do carrossel** (@ramotion, `Dak9nkTFpYI`, `DSIMwtvDluO`, `DVg6uh7AV25`): slides em vídeo para o que precisa de tempo: especímen de tipo percorrendo os pesos, construção do logo, rolagem vertical da página do hero até o texto longo. Imagens estáticas para paleta e kit de ícones.
- **Motion como marca de portfólio** (@uidesignpatterns, `DcyWWw-hCTz`, laurent.fyi): dezenas de miniaturas se reorganizam em formas (círculo, rosto, estrela) com blur de movimento. Só para portfólio/marca pessoal.

## Checklist rápido (vídeo/reel)
- [ ] ≤ 6 palavras por tela, grandes, ~1,2 s cada; passa no teste "ler duas vezes".
- [ ] Primeira imagem já mostra o título/produto (nada de tela em branco ou loading).
- [ ] Logo: movimento escolhido pela personalidade, ~1 s, termina no logo estático.
- [ ] Variações comparadas com a mesma duração.
- [ ] Carrossel: numeração e contagem conferidas, paginação "N/total" e CTA de swipe.
