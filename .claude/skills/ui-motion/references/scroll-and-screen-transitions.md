# Scroll e transição de telas: dar "vida" aos componentes

> **Diretriz do usuário (nota de 09/11/2026):** "Transição de telas, scroll para comportamento dinâmico dos componentes para dar 'vida' a eles. **Avaliar onde faz sentido.**"
>
> Leia isso como uma decisão de produto: o objetivo é usar scroll e transições para os componentes parecerem vivos, mas **cada caso precisa justificar o movimento**. A regra não é animar tudo no scroll.

O que vem dos reels está referenciado; o resto está marcado como **(complemento)**.

## 1. Onde faz sentido (avaliar caso a caso)

| Situação | Comportamento sugerido | Por quê |
|---|---|---|
| Navegação entre telas (lista → detalhe, card → página) | Shared element: o card vira a página e o "voltar" retorna à origem (ver `page-transitions-and-timing.md`) | Evita o "Tap. Cut.": o usuário não precisa se reencontrar na tela (reel DfwhC1riuuO) |
| Header/título de página ao rolar | Large title que encolhe e vira título compacto na barra (ver `page-transitions-and-timing.md`) | Mostra que você saiu do topo sem perder o contexto |
| Seções de landing page entrando na tela | Reveal curto (≤ 700 ms, fade + deslocamento pequeno), uma vez só, com stagger de 70–100 ms entre filhos | Cascata guia o olho; nada surge do nada (ver regras de duração no `SKILL.md`) |
| Números e KPIs que entram na viewport | Contagem até o valor (rolling number) quando o card aparece | O olho vê a mudança em vez de perdê-la (reel DfP6EoLBtgg) |
| Toolbars/barras inferiores em leitura longa | Esconder ao rolar para baixo e mostrar ao rolar para cima **(complemento)** | Libera espaço de leitura sem esconder a navegação |
| Storytelling/produto (hero, "como funciona") | Seção fixada (pin) com progresso ligado ao scroll (scrub) **(complemento)** | O scroll vira o controle de uma narrativa; só vale para conteúdo sequencial. Exemplo real: site conceito RWB Porsche (`DYpD5C7zwx6`, @rish_designs): 1 palavra-título gigante + 1 ângulo do carro 3D por seção, fundo alternando escuro/claro, texto atrás do objeto (detalhes em `motion-for-social-video.md` §4) |

## 2. Onde NÃO faz sentido **(complemento)**

- **Telas de trabalho repetitivo:** em formulários, tabelas, dashboards de uso diário, settings e checkout, o usuário volta muitas vezes e o movimento vira atrito. Fique com feedback de estado (press, sucesso, erro) e não ponha efeitos de scroll.
- **Conteúdo que o usuário precisa ler ou comparar agora:** nada de reveal que atrase o texto. Se o conteúdo já está na viewport no load, ele aparece sem animação.
- **Scroll-jacking:** não altere a velocidade nem a direção do scroll nativo, e não prenda o usuário numa seção longa. Reforço da rodada 10A (@theglidestudio `DgEyy8nRybB`, "Follow, don't lead", print `DgEyy8nRybB_1.jpg`): "sua página briga com quem rola"; na versão calma **o polegar dita o ritmo e, parou de rolar, o movimento para**. Efeito com `scrub` ligado ao scroll obedece a isso; animação disparada que continua sozinha depois de o usuário parar não.
- **Parallax decorativo em mobile:** custa performance e não informa nada.
- **Animações que repetem** a cada vez que o elemento sai e volta da viewport: anime uma vez.

## 3. Checklist de decisão

Antes de colocar motion ligado a scroll ou a uma transição de tela, responda:

1. **Informa algo?** Origem e destino, hierarquia, progresso ou mudança de valor. Se a resposta for só "fica bonito", corte ou reduza.
2. **Com que frequência a pessoa vê isso?** Primeira visita ou landing aceita mais expressão; uso diário pede o mínimo.
3. **Atrasa a tarefa?** Reveal de no máximo 700 ms, e nunca bloqueia interação. Navegação precisa poder ser interrompida e revertida (regra de springs do `SKILL.md`).
4. **Respeita `prefers-reduced-motion`?** Troque deslocamentos e escalas por fade simples, ou nada.
5. **Roda a 60 fps em mobile médio?** Anime só `transform` e `opacity` e verifique no dispositivo **(complemento)**.

## 4. Implementação **(complemento)**

- **CSS nativo (scroll-driven animations).** Para reveals e headers simples, sem JS:

```css
@media (prefers-reduced-motion: no-preference) {
  .reveal {
    animation: reveal linear both;
    animation-timeline: view();
    animation-range: entry 0% entry 40%;
  }
}
@keyframes reveal {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: none; }
}
```

  Verifique o suporte do browser-alvo. Sem suporte, o conteúdo aparece direto (fallback seguro).

- **Transição entre telas.** Use a View Transitions API (`document.startViewTransition`, com `view-transition-name` no card e no hero) ou FLIP. Os snippets estão em `css-recipes.md`.
- **Pin, scrub e coreografia complexa:** use a skill `ext-gsap-scrolltrigger` (ScrollTrigger com `scrub`, `pin`, `toggleActions: "play none none none"` para animar uma vez) e `ext-gsap-react` em React.
- **Verificação.** Use `ext-playwright-cli` para rolar a página e gravar screenshots ou vídeo do comportamento antes de dar como pronto.

## 5. Um momento animado por página ou tela (rodada 5)
Regra repetida em 2 posts do @noahelhadedy:
- `De_J0aOl9SJ` (bibliotecas de UI animada): "escolha **um momento animado por página**. Hero **ou** CTA, não os dois. Menos movimento parece mais premium."
- `Dfo__tSjk9k` (componentes de motion): "um momento lúdico por tela. **Se tudo mexe, nada é especial.**"
- Prints em `assets/visual-refs/`: `De_J0aOl9SJ_1.jpg` (hero com fumaça WebGL como **o** momento da página; o resto é
  estático) e `Dfo__tSjk9k_1.jpg`, `Dfo__tSjk9k_2.jpg`, `Dfo__tSjk9k_3.jpg` (pull cord, swipe deck, parallax ticket: um componente lúdico por palco).

Como aplicar **(complemento)**:
- O "momento" é o efeito **expressivo** (reveal de hero, componente lúdico, fundo WebGL, tilt). Feedback funcional (press a 95%, hover, foco, sucesso, toast, skeleton) **não conta**: continua em todo lugar.
- Na landing, escolha onde está a decisão: hero (primeira impressão) **ou** CTA (conversão). O resto entra com reveal curto e discreto, ou sem animação.
- Em tela de app, no máximo 1 componente lúdico (ex.: hold to publish, pull cord) e só onde ele também comunica algo.
- Bate com o "Von Restorff: um destaque, nunca três" de `ux-patterns` e com o "WebGL ≤ 1 por página" de `react-bits.md`.
- **Tensão registrada:** o @mobileeditingclub (§6) lista 5 padrões para o mesmo site. Leia como cardápio: escolha 1 expressivo e trate os outros como micro-feedback discreto.

## 6. Motion de site: 5 padrões e como pedir ao Claude (`Dff1uulGoxb`, @mobileeditingclub com @adrianabubori, rodada 1)
Carrossel "How to animate Websites with Claude". Os 5 padrões cobrem o ciclo da página:

| Padrão | O que a fonte pede | Papel no ciclo |
|---|---|---|
| `/headline-reveal` | Imagem do produto + headline + cores da marca; hero com **revelação suave da imagem e texto em sequência**, movimento sutil | Entrada |
| `/micro-interactions` | **Leve deslocamento da imagem no hover**, resposta clara do botão ou transição suave entre detalhes do produto, **um efeito de cada vez** | Resposta |
| `/portfolio-showcase` | Transições de imagem suaves e navegação simples entre projetos, trabalho em destaque e pouco texto | Navegação |
| `/animated-gallery` | Imagens **reveladas uma após a outra**, movimento sutil, espaçamento consistente, layout limpo | Descoberta |
| `/scroll-reveal` | Produto, imagens e texto entrando conforme o scroll, sequência clara, **próxima ação fácil de achar** | Progressão |

Fluxo recomendado pela fonte:
1. Dê ao Claude os **visuais**, as **cores da marca** e uma **descrição verbal do movimento** (o quê, em que ordem, com que intensidade).
2. Construa e valide **um efeito por vez**.
3. Teste no **desktop e no mobile**.
4. Texto sempre legível; o movimento guia até a próxima ação.

**(complemento)** Traduza "suave" e "sutil" para os tokens do `SKILL.md` antes de pedir: reveal ≤ 700 ms ease-out, stagger 70–100 ms na galeria, deslocamento de hover de poucos px, uma vez só no scroll. Visual do layout do carrossel: `Dff1uulGoxb_2.jpg`. O fluxo completo ficou atrás de "comente WEBSITE" e não foi visto.

## 7. Interações "premium" de site e o custo de cada uma (`DgNTvDZCMNX`, @thedesignstack.co.in, rodada 10A)
Carrossel "Parte 4": cada interação tem função **e** custo. Vale como filtro antes de escolher o **um** momento animado (§5).

| Interação | Função | Custo citado |
|---|---|---|
| Rastro do cursor | primeira tela memorável | some no celular (sem cursor) |
| Mudança de fundo por seção | ritmo entre seções | pode falhar em contraste |
| Spotlight no cursor | clima | pode esconder conteúdo |
| Footer takeover (o rodapé sobe e cobre a página) | fechamento marcante | exige cuidado no mobile |
| Distorção de imagem no hover | tato em portfólio | custa performance |
| Cenas guiadas por scroll | narrativa | dos mais pesados |
| Showreel em tela cheia | portfólio/agência | dos mais pesados |

(complemento) Efeito que depende de cursor precisa de equivalente no toque ou de nenhum efeito no mobile; mudança de fundo por seção exige medir o contraste de cada par texto × fundo (`design-direction` → `color-palettes.md`); WebGL/vídeo ≤ 1 por página (`react-bits.md`).
