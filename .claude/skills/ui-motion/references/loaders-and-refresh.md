# Loaders, percepção de espera e formas de atualizar

## 3 truques de percepção — DUEjWRukT_2 (@designmotionhq)
"Mesmo tempo de carregamento, sensação diferente."
1. **Skeleton screens** — mostre o layout em vez de nada; o shimmer faz o cérebro entender que o conteúdo vem vindo e a espera parece menor. "Show the layout before the content."
2. **Optimistic UI** — ao tocar (ex.: like 142 → 143), não espere o servidor: mostre sucesso na hora. "Assume success. Update instantly." (complemento: reverta com mensagem clara se falhar.)
3. **Progress bar psychology** — comece rápido, desacelere no fim. Mesma duração, curva diferente: "fast start = perceived speed" (tela compara Linear 16% vs Psychological 31% no mesmo instante).
Combinados: skeleton + atualização instantânea + progresso psicológico.

## 8 estilos de loader — DfvAY82DSvD (@ale.uiux)
| # | Estilo | Quando usar |
|---|---|---|
| 01 | Spinner | esperas curtas, **< 3 s** (texto na tela) |
| 02 | Typing dots | chat / resposta sendo escrita |
| 03 | Progress bar | duração conhecida |
| 04 | Skeleton screen | feeds — sem saltos de layout |
| 05 | AI shimmer | respostas de IA ("Thinking…") |
| 06 | Progress ring | duração conhecida, espaço compacto (tela mostra %) |
| 07 | Pull to refresh | listas — conteúdo novo sob demanda |
| 08 | Shape morph | splash/loader de marca |

Regra: escolha pelo que você **sabe** da espera — duração desconhecida e curta → spinner; conhecida → barra/anel com %; conteúdo estruturado → skeleton.

## 8 formas de atualizar uma página — DfwavjimeIa (@ale.uiux)
| # | Padrão | Quando usar |
|---|---|---|
| 01 | Pull down | listas mobile; o indicador desliza junto |
| 02 | Elastic pull | pull com elasticidade/resistência (ver 35% / rubber band) |
| 03 | Release cue | sinal de "pode soltar" ao passar do limite |
| 04 | New posts pill | pílula "novos posts" — o leitor nunca perde o lugar |
| 05 | Live insert | feeds em tempo real, item entra no topo |
| 06 | Auto-load | infinite scroll |
| 07 | Load more | botão — o usuário mantém o controle |
| 08 | Refresh button | dashboards e web apps |

## Valores de pull-to-refresh (das outras fontes)
- Resistência: dedo **100%** → lista **35%** (DfP6EoLBtgg).
- Rubber band iOS: **200 px** de puxão → **86 px** de deslocamento, volta com spring (De4B0UxPXIk).
- Threshold e release cue: (complemento) dispare ao passar ~64–80 px de deslocamento visual; troque ícone/texto ("Solte para atualizar") e dê haptic no mobile.

## Upload (DZ2Dp5wt0pJ — resumo)
Drop zone com borda + glow + copy; % e tempo restante; retry inline que retoma (90% não volta a 0); preview com thumbnail/tipo/tamanho; progresso e retry por arquivo.

## Sucesso no fim da espera
Círculo desenha, depois o tick, **470 ms** (DfP6EoLBtgg); download: seta → anel → tick, **1,2 s** (DfVOGNnzR_D); submit: pílula 260 → 64 px vira spinner e depois tick (DfTr-mwhZT3).
