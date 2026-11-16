# Dark patterns e versão honesta, e como evitar "AI slop"

## A. Dark patterns: "Six more tricks apps use on you" (`DfgcqeMBPCU`, só a legenda)
> Atenção: só a **legenda** deste reel trata de dark patterns. O áudio e os frames mostram micro-interações (veja `components-checklists.md` §8). Não há imagem dos dark patterns. A legenda chama a lista de "6 more", então a primeira parte não está nas fontes.

A coluna "falha" vem da legenda. A legenda promete a "honest version" mas não a descreve, por isso a coluna "versão honesta" é **(complemento)**.

| # | Truque (fonte) | Versão honesta (complemento) |
|---|---|---|
| 1 | **Free trial trap**: no dia 8 cobra **$79.99** sem aviso | Avisar antes da cobrança, mostrar data e valor na assinatura e cancelar em 1 passo |
| 2 | **Fake social proof**: contadores de visitantes aleatórios, os mesmos compradores repetidos | Mostrar só dados reais e verificáveis, ou não mostrar nada |
| 3 | **Disguised ad**: o botão grande de download é um anúncio **8× maior** que o link real | O link real é o maior; anúncio rotulado como anúncio e visualmente distinto |
| 4 | **Nagging**: "Not now" é a única saída, então o app continua pedindo | Oferecer "Não, obrigado" permanente e respeitar a recusa |
| 5 | **The decoy**: o Medium existe para fazer o Large parecer só **$0.50** mais caro | Planos com valor próprio; destacar um (Von Restorff) sem plano-isca |
| 6 | **Fake close**: o X está pintado dentro do anúncio | Botão de fechar real, com alvo ≥ 44px e foco de teclado |

Leis relacionadas (`ux-laws.md`): Von Restorff (um destaque legítimo), Peak-end (o final honesto molda a memória) e Banner blindness.

---

## B. Dashboard com cara de IA: 5 tells e 5 fixes (`Dc-4jNbtyJg`, @designmotionhq)
O frame "antes" mostra header roxo→azul, "Welcome back, Jordan 👋", 4 cards iguais ($48,250 / 2,340 / 3.8% / 1.2%) e badges verdes "+12.5%".

| # | Tell | Fix |
|---|---|---|
| 1 | **Gradiente** roxo→azul no header, no botão e no fill do chart ("gradients with nothing to say") | **Um accent chapado**, para a cor voltar a significar algo |
| 2 | **Ícones em tiles pastel**, uma cor por card (blue, green, purple, orange). "Four colors, four numbers" é decoração | Tire os tiles. **O número é o herói** |
| 3 | **4 cards idênticos** (mesmo tamanho, mesmo peso, mesmo badge verde). "Um dashboard sem hierarquia é uma planilha com padding" | **1 métrica primária grande e 3 secundárias pequenas** |
| 4 | **Cantos de 16px e drop shadow em tudo** (cards, inputs, badges, chart). "When everything floats, nothing does" | Bordas hairline, **radius menor nas partes menores**, sombra **só no que abre acima da página** (menu, popover) |
| 5 | **Copy placeholder** ("Welcome back, Jordan 👋", "+12.5% from last month") e números sem forma | **Nomeie o período** ("Revenue · Aug 1 to Aug 31"), use **tabular digits** e um **sparkline em vez de badge** |

## C. Fonte genérica: "Your app looks AI-made" (`DfPJo9UBJ7D`, @designmotionhq)
São 4 decisões de tipografia. Exemplo dos frames: "Northside Cycles", app de agendamento de reparo de bike.
1. **O default**: a mesma stack (`system-ui, sans-serif`) em 3 apps diferentes parece "starter template", e a pessoa reconhece o template antes de ler.
2. **Uma fonte do mundo do produto**: uma oficina não deve soar como banco. Os frames comparam bank, fintech e workshop; a escolhida é Bricolage Grotesque, "sturdy warm face, like a workshop sign".
3. **Carregue de verdade**: `<link href="…Bricolage+Grotesque…&display=swap">`. Sem isso, o visitante recebe o fallback enquanto **a sua máquina esconde o erro porque a fonte está instalada localmente** ("installed locally" vs "fallback in prod").
4. **Uma família, dois pesos** (400/700). A hierarquia vem de tamanho e peso: frames com 40/700, 24/700, 18/400, 14/400. O contraexemplo usa 3 fontes.

Complemento: para validar o item 3, abra a página num browser limpo (por exemplo `ext-playwright-cli`) e confira a fonte computada e o request `.woff2`.
