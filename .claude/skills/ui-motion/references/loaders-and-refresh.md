# Loaders, percepção de espera e formas de atualizar

## 3 truques de percepção — DUEjWRukT_2 (@designmotionhq)
"Mesmo tempo de carregamento, sensação diferente."
1. **Skeleton screens** — mostre o layout em vez de nada; o shimmer faz o cérebro entender que o conteúdo vem vindo e a espera parece menor. "Show the layout before the content."
2. **Optimistic UI** — ao tocar (ex.: like 142 → 143), não espere o servidor: mostre sucesso na hora. "Assume success. Update instantly." (complemento: reverta com mensagem clara se falhar.)
3. **Progress bar psychology** — comece rápido, desacelere no fim. Mesma duração, curva diferente: "fast start = perceived speed" (tela compara Linear 16% vs Psychological 31% no mesmo instante).
Combinados: skeleton + atualização instantânea + progresso psicológico.

## 8 estilos de loader — DfvAY82DSvD (@ale.uiux)
Legenda de cada slide (texto na tela) + o que o mockup mostra:

| # | Estilo | Quando usar (tela) | O que o mockup mostra |
|---|---|---|---|
| 01 | Spinner | "short waits, under 3 s" | anel girando sozinho |
| 02 | Typing dots | "chats and AI replies" | bolha "Are you coming?" + 3 pontos |
| 03 | Progress bar | "uploads you can measure" | "video.mp4 · Uploading…" com % (21% → 100%) |
| 04 | Skeleton screen | "feeds without layout jumps" | linhas/avatares cinza que viram a lista |
| 05 | AI shimmer | "while the model thinks" | prompt "Plan my week" + texto "Thinking…" com brilho passando, depois a resposta |
| 06 | Progress ring | "downloads and steps" | anel com % central ("Downloading 3 files"), termina num check |
| 07 | Pull to refresh | "new content on demand" | ícone girando no topo, lista desce |
| 08 | Shape morph | "a branded splash loader" | blob/quadrado arredondado que morfa ("Preparing your space") |

Regra: escolha pelo que você **sabe** da espera — duração desconhecida e curta → spinner; conhecida → barra/anel com %; conteúdo estruturado → skeleton.

## 8 formas de atualizar uma página — DfwavjimeIa (@ale.uiux)
| # | Padrão | Legenda na tela | Quando usar |
|---|---|---|---|
| 01 | Pull down | "the indicator slides over" | listas mobile |
| 02 | Elastic pull | "a playful, stretchy drop" | pull com gota elástica que estica (marca/brincadeira) |
| 03 | Release cue | "tells users when to let go" | complementa o pull: avisa o ponto de soltar |
| 04 | New posts pill | "never lose your place" | feeds longos: pílula no topo, o leitor não pula |
| 05 | Live insert | "real-time feeds, no gesture" | itens novos entram sozinhos no topo |
| 06 | Auto-load | "endless feeds, zero taps" | infinite scroll |
| 07 | Load more | "users stay in control" | botão no fim da lista |
| 08 | Refresh button | "dashboards and web apps" | ícone ↻ no canto; o mockup é um dashboard com KPIs (1,342 / €3.6k) e barras que se atualizam |

## Valores de pull-to-refresh (das outras fontes)
- Resistência: dedo **100%** → lista **35%** (DfP6EoLBtgg).
- Rubber band iOS: **200 px** de puxão → **86 px** de deslocamento, volta com spring (De4B0UxPXIk).
- Threshold e release cue: (complemento) dispare ao passar ~64–80 px de deslocamento visual; troque ícone/texto ("Solte para atualizar") e dê haptic no mobile.

## Upload (DZ2Dp5wt0pJ — resumo)
Drop zone com borda + glow + copy; % e tempo restante; retry inline que retoma (90% não volta a 0); preview com thumbnail/tipo/tamanho; progresso e retry por arquivo.

## Sucesso no fim da espera
Círculo desenha, depois o tick, **470 ms** (DfP6EoLBtgg); download: seta → anel → tick, **1,2 s** (DfVOGNnzR_D); submit: pílula 260 → 64 px vira spinner e depois tick (DfTr-mwhZT3).
