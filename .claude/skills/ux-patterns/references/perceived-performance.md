# Performance real e percebida: 31 itens para app de vibe coding

Fonte: `Dfby7sPgMPU` (@gustagoat.ai, PT-BR). Tese da legenda: "App lento perde usuário. E quase sempre não é falta de servidor, é decisão técnica."
A ordem e o texto dos itens seguem a transcrição. A numeração foi conferida com os frames (03, 06, 09, 12, 15, 17, 20, 23, 27 e 30 aparecem com o rótulo). A coluna "Tag" só tem valor quando a categoria aparece no frame.
O "kit completo" (checklist, prompt de auditoria e de correção) é oferecido via comentário e **não** está nas fontes.

| # | Item | Tag no frame |
|---|---|---|
| 01 | Skeleton de carregamento | — |
| 02 | Imagens em WebP ou AVIF | — |
| 03 | Evitar chamadas duplicadas na API (o frame mostra 2 requisições iguais) | API |
| 04 | Debounce na busca e no autocompletar | — |
| 05 | Paginar os resultados da API | — |
| 06 | Arquivos estáticos via CDN ("busca lá na origem, longe") | REDE |
| 07 | Tarefas lentas numa fila | — |
| 08 | Corrigir consultas N+1 | — |
| 09 | Compressão Brotli ou Gzip ("pacote compacto") | REDE |
| 10 | Cache no Redis dos dados mais consultados | — |
| 11 | Remover dependências não usadas | — |
| 12 | Timeout nas APIs externas (o frame mostra um pagamento "processando…" esperando a API externa, com timeout de 1s) | API |
| 13 | Streaming da resposta da IA, token por token | — |
| 14 | Atualizar a tela sem esperar o servidor (optimistic UI) | — |
| 15 | Lazy loading nas imagens fora da tela ("2/6 imagens baixadas") | FRONTEND |
| 16 | Disparar em paralelo as requisições independentes | — |
| 17 | Índices para as consultas mais comuns ("busca direta") | BANCO DE DADOS |
| 18 | Rastrear requisições lentas com OpenTelemetry | — |
| 19 | Servidor perto do banco de dados | — |
| 20 | Renderizar no servidor ou no build ("conteúdo primeiro") | BACKEND |
| 21 | Scripts de terceiros carregados depois da página | — |
| 22 | Dividir o JavaScript por página (code splitting) | — |
| 23 | Virtualizar listas longas ("só desenha o que aparece") | FRONTEND |
| 24 | Pedir só as colunas necessárias | — |
| 25 | Pool de conexões | — |
| 26 | Evitar re-render desnecessário | — |
| 27 | Cache dos estáticos no navegador (contraexemplo no frame: "baixando tudo de novo" na 2ª visita) | REDE |
| 28 | Distribuir o tráfego entre várias instâncias | — |
| 29 | Hospedar as próprias fontes e limitar os pesos | — |
| 30 | Monitorar a velocidade dos usuários reais (RUM) | MEDIÇÃO |
| 31 | Testar no celular e em rede lenta | — |

## Quais itens são de "percebida" e quais são de "real" (complemento: agrupamento editorial)
- **Percebida, sentida na UI**: 01 skeleton, 13 streaming, 14 optimistic UI, 15 lazy loading, 23 virtualização, 26 re-render. Combine com Doherty (resposta < 400ms), latência do botão (resposta ≤ 100ms, estado final ≤ 300ms; animação pelos tokens de `ui-motion`), ⌘K abrindo em 150ms e paginação com espaço reservado (`components-checklists.md`).
- **Rede e assets**: 02, 06, 09, 21, 22, 27, 29.
- **API e backend**: 03, 04, 05, 07, 10, 12, 16, 19, 20, 25, 28.
- **Banco**: 08, 17, 24.
- **Medição**: 18, 30, 31.

## Como usar
1. Rode a lista como auditoria: marque cada item como OK, não se aplica ou falta, com evidência (arquivo e linha).
2. Corrija primeiro o que o usuário sente: skeleton, streaming, optimistic e o espaço reservado contra layout shift.
3. Verifique em celular e rede lenta (item 31). Complemento: throttling do DevTools ou `ext-playwright-cli`.

## Reforços de outras fontes
- **Título primeiro** (`Dfy7ig_B-FL`, @theglidestudio): 2 s de página em branco "parecem uma hora" e o visitante sai. Renderize o título e o CTA no primeiro paint (item 20) e deixe o resto entrar em cascata. Duração do reveal em `ui-motion` (`page-transitions-and-timing.md`).
- **Catálogo de loaders** (`Dfw7678GcQ2`, @dailywebdesign, por @vamshi.work): spinner, skeleton, progress bar, pulsing dots, loader no botão, tela cheia, pull-to-refresh e infinite scroll. Skeleton para conteúdo estruturado, barra quando o progresso é conhecido, loader no botão para ação do usuário. Sem tempos no vídeo; a tabela com "quando usar" está em `ui-motion` → `loaders-and-refresh.md`.
