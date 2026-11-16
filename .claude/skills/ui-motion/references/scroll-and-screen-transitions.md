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
| Storytelling/produto (hero, "como funciona") | Seção fixada (pin) com progresso ligado ao scroll (scrub) **(complemento)** | O scroll vira o controle de uma narrativa; só vale para conteúdo sequencial |

## 2. Onde NÃO faz sentido **(complemento)**

- **Telas de trabalho repetitivo:** em formulários, tabelas, dashboards de uso diário, settings e checkout, o usuário volta muitas vezes e o movimento vira atrito. Fique com feedback de estado (press, sucesso, erro) e não ponha efeitos de scroll.
- **Conteúdo que o usuário precisa ler ou comparar agora:** nada de reveal que atrase o texto. Se o conteúdo já está na viewport no load, ele aparece sem animação.
- **Scroll-jacking:** não altere a velocidade nem a direção do scroll nativo, e não prenda o usuário numa seção longa.
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
