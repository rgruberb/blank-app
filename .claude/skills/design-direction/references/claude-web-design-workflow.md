# Workflow: usar o Claude para web design

Fontes: @thearseniodev (Dd9nhiOyrZU, DfVlIwHISSv — legendas), @thedzianis (DfSIP2iBuFI), @mobileeditingclub (Dff1kjUiR4o). Os reels de @thearseniodev e @thedzianis promovem uma biblioteca de assets ("getlayersai"/"LAYERS"); o princípio vale independentemente da ferramenta.

## Princípio central: mostrar, não descrever

> "Stop asking Claude to 'make your website look premium.' That's way too vague." — Dd9nhiOyrZU
> "Adjectives get you an interpretation. References get you the result." — DfVlIwHISSv

- Adjetivos ("modern", "clean", "expensive", "premium") obrigam o modelo a **inventar toda a direção criativa** → resultado genérico e uma hora corrigindo o palpite.
- Em vez disso, aponte para **uma cena real, uma transição real, uma seção real que já está certa**. O modelo parte de código/visual concreto, não de adjetivos.
- Divisão de papéis: **humano decide mood, escolhe referências e controla hierarquia; Claude faz o trabalho pesado** ("Here's the vision. Here's the toolkit. Make it real.").
- O autor conecta o agente via **MCP a uma biblioteca de assets reais** (cenas 3D cinemáticas, efeitos de movimento, vídeos de fundo, seções interativas) e o Claude lê os componentes reais. Equivalentes neste projeto: `ext-extract-design` (extrai tokens de um site por URL), screenshots/imagens anexadas, trechos de código de componentes existentes.

## Passo a passo recomendado

1. **Colete referências concretas** (2–5): URLs, screenshots, um componente que já funciona. Se for URL, rode `ext-extract-design` para obter cores/fontes/espaçamento reais.
2. **Defina a direção em decisões, não adjetivos**:
   - paleta 2+1 com hex (ver `color-palettes.md`);
   - trio tipográfico (sans / serif itálico de ênfase / mono para labels) ou equivalente;
   - hierarquia: qual é o único CTA, qual o headline;
   - qual é a "terceira camada" (cor, luz, objeto/cena).
3. **Construa em camadas** sobre o mesmo layout: zero design → identidade → profundidade (luz, frosted glass) → movimento. Valide cada camada antes da próxima.
4. **Movimento: um efeito por vez**, passando visuais + cores + descrição do movimento; teste desktop e mobile.
5. **Critique** com `ext-impeccable` / `ext-taste-skill` (anti-slop) e cheque confiança (espaço, alinhamento, ritmo calmo — ver `layers-and-trust-layout.md`).

## Modelos de prompt

Ruim:
> "Make my landing page look premium and modern."

Bom (baseado nos princípios das fontes):
> "Landing page para [produto]. Mood: escuro, técnico, calmo. Paleta: base #0A0A0A + texto #E6E6E6, acento único #C7F44F usado só no CTA primário e no badge do logo. Tipografia: headline sans, segunda linha em serif itálico, labels em mono. Referência de layout: [screenshot/URL] — copie a estrutura do hero (headline à esquerda, diagrama de workflow à direita). Camada de profundidade: um feixe de luz verde atrás de cards em frosted glass. Não adicione movimento ainda."

Movimento (Dff1kjUiR4o):
> "Adicione só um headline reveal: o título entra palavra por palavra em ~600ms, sutil e legível. Cores da marca: [...]. Depois me mostre em desktop e mobile antes do próximo efeito."

## O que se vê no resultado mostrado (Dd9nhiOyrZU)

Site "Relay" dark gerado com essa abordagem, seção por seção:
- Hero: feixes de luz verde/lime fluindo, headline "The handoffs run *themselves.*", CTA pill lime, cards de vidro com diagrama de workflow.
- "Most of a process is *glue*." — texto curto + painel lateral sobre fundo de streams.
- "Approvals where people already are" — mock de app de mensagens com botão lime; gráfico de barras 3D isométrico (barra destacada em lime).
- Transição: um tile/ícone lime que cresce e preenche a tela (o acento vira transição de seção).
- "*Boring* in the ways that matter." — cards de features com ícone lime.
- "A *Tuesday*, seen from Relay." — heatmap/tabela + anel de progresso lime.
- "Numbers we did *not* have to explain away" — métricas grandes (56,703 / 9 / 73%) com medidor em barras lime.
- "You pay for runs, not *for seats*." — slider de volume + pricing $29 / $89 / $290, plano do meio destacado (badge + botão lime).
- CTA final: card de fundo lime "Pick the task you *hate* most." + footer.

Padrão: **todo título de seção usa uma palavra em serif itálico** e o lime aparece 1–2 vezes por seção (CTA, dado-chave). Útil como referência de **consistência do acento e da tipografia ao longo de várias seções**.
