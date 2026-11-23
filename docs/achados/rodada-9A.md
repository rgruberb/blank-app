# Rodada 9A: fundações oficiais (Apple HIG, Material 3, Carbon Motion)

Data da leitura: 22/11/2026. Todas as páginas foram abertas no Chrome e lidas como texto. Nada foi preenchido, nenhum login feito.
Legenda de aplicabilidade: **[PWA]** = PWA/Capacitor do cliente, **[WEB]** = painel web, **[AMBOS]**.

## Resumo (principais aprendizados)

1. **Apple HIG não publica números de motion** (nem ms, nem curvas, nem springs). A página Motion só traz princípios: motion com propósito, opcional, breve, cancelável. Os números de motion do app terão de vir de Material/Carbon ou de calibragem própria.
2. **Reduce Motion (Apple, Accessibility)**: apertar springs para reduzir bounce, fazer animação seguir o gesto, evitar animar profundidade (z), trocar transições x/y/z por fades, evitar entrar/sair de blur. Isso vira regra direta para `useReducedMotion` do Motion for React. [AMBOS]
3. **Material 3 mudou de easing+duração para springs (M3 Expressive, maio/2025)**. A página oficial diz que o sistema antigo ainda serve para transições, mas "não é mais mantido". Para web há tabela oficial de conversão spring → cubic-bezier + duração (ex.: expressive default spatial = `cubic-bezier(0.38, 1.21, 0.22, 1.00)` em 500 ms).
4. **Carbon é o único com tokens de duração e easing completos e simples**: 70/110/150/240/400/700 ms; productive `cubic-bezier(0.2, 0, 0.38, 0.9)` e expressive `cubic-bezier(0.4, 0.14, 0.3, 1)`. Regra útil: microinteração 90–120 ms com ease-out.
5. **Alvos de toque**: Apple 44×44 pt (mínimo 28×28 pt); Material 48×48 dp com 8 dp de espaço entre alvos. Para o PWA, usar 44 px como piso e 48 px como padrão confortável.
6. **Tipografia**: Apple iOS default 17 pt / mínimo 11 pt, evitar pesos Ultralight/Thin/Light. Material usa escala Major Second (1,125) com base 14 e 30 estilos (15 baseline + 15 emphasized). Contraste Apple: 4,5:1 mínimo, 7:1 recomendado para texto pequeno em Dark Mode.
7. **Layout adaptativo**: Material tem 5 breakpoints (compact <600, medium 600–839, expanded 840–1199, large 1200–1599, extra-large 1600+ dp) e regra de trocar barra inferior por navigation rail ao alargar. Útil para o painel web × PWA. Apple orienta por size classes (compact/regular), não por dispositivo.
8. **Cuidado**: boa parte de Apple (Liquid Glass, Dynamic Type, SF Symbols, detents de sheet) é de app nativo. No PWA só valem como referência visual e de comportamento, não como API.
9. **Lacunas desta rodada**: tokens numéricos de springs (stiffness/damping) do Material e a tabela de tipografia M3 ficam em módulos interativos que não aparecem no texto; marcados "não especificado".

---

## Ficha 1: Apple HIG (página inicial)

- https://developer.apple.com/design/human-interface-guidelines/ | status: ✅ abriu
- Subpáginas visitadas: ver fichas 2 a 4 e "Subpáginas extras" abaixo.
- Tema: guia de design de todas as plataformas Apple; nível: todos; idioma: EN; preço: gratuito. 
- Tags: [oficial]
- Regras e números: página-índice, sem números. Organiza em Design fundamentals, Foundations (Accessibility, App icons, Color, Layout, Materials, Typography), Patterns, Components, Inputs, Technologies. Lista "New and updated" na data da leitura.
- Para que serve no app: ponto de entrada para navegação, componentes e fundamentos.
- Limitações: nativo-first; sem equivalente web explícito.

## Ficha 2: Apple HIG, Motion

- https://developer.apple.com/design/human-interface-guidelines/foundations/motion (redirecionou para `/design/human-interface-guidelines/motion`) | status: ✅ abriu
- Subpáginas: nenhuma adicional.
- Tema: motion; nível: intermediário; EN; gratuito. Tags: [oficial]
- Regras extraídas:
  - Adicionar motion com propósito; motion excessivo distrai e pode causar desconforto. [AMBOS]
  - Tornar motion opcional: não ser o único meio de comunicar algo importante; complementar com háptico e áudio. [PWA]
  - Feedback de motion deve seguir o gesto e ser realista (se a view entrou deslizando por cima, não sair para o lado). [PWA]
  - Feedback breve e preciso; evitar motion em interações muito frequentes; permitir cancelar (não obrigar a esperar a animação). [AMBOS]
  - Fps (30–60) é citado só para jogos.
  - Valores de duração, easing e springs: **não especificado** na página.
  - Liquid Glass: resposta do movimento ao toque direto é mais enfática; com trackpad, mais sutil.
  - iOS/iPadOS/macOS/tvOS: sem considerações adicionais. Itens de visionOS e watchOS não se aplicam.
  - Changelog: 9/set/2025 "guidance for Liquid Glass".
- Para que serve: princípios para todas as transições (onboarding, abrir/fechar sheets, listas).
- Limitações: nenhum número; Liquid Glass não existe em PWA.

## Ficha 3: Apple HIG, Accessibility

- https://developer.apple.com/design/human-interface-guidelines/accessibility | status: ✅ abriu
- Tema: acessibilidade; nível: intermediário; EN; gratuito. Tags: [oficial]
- Regras e números extraídos:
  - **Texto ampliável**: permitir aumentar texto em pelo menos **200%** (140% no watchOS). [AMBOS]
  - **Tamanhos de texto (padrão / mínimo)**: iOS/iPadOS 17 pt / 11 pt; macOS 13 / 10; tvOS 29 / 23; visionOS 17 / 12; watchOS 16 / 12. [PWA: iOS; WEB: macOS como referência de desktop]
  - Fontes finas: usar tamanho maior que o recomendado.
  - **Contraste (WCAG AA citado)**: até 17 pt, 4,5:1; 18 pt, 3:1; texto em negrito, 3:1. Se não atingir por padrão, oferecer esquema de alto contraste com Increase Contrast; checar light e dark. [AMBOS]
  - Preferir cores do sistema; não depender só de cor (usar formas/ícones).
  - **Alvo de controle (padrão / mínimo)**: iOS/iPadOS **44×44 pt / 28×28 pt**; macOS 28×28 / 20×20; tvOS 66×66 / 56×56; visionOS 60×60 / 28×28; watchOS 44×44 / 28×28. [PWA]
  - **Espaçamento entre controles**: cerca de **12 pt** de padding em elementos com bezel; cerca de **24 pt** em elementos sem bezel. [AMBOS]
  - Gestos simples; sempre oferecer alternativa ao gesto (ex.: swipe para dispensar + botão). [PWA]
  - Cognitivo: evitar elementos com tempo limite que se auto-dispensam; evitar autoplay sem controle; confirmação dupla para ações difíceis de desfazer (Assistive Access).
  - **Reduce Motion**: reduzir animações automáticas/repetitivas (zoom, scale, movimento periférico); apertar springs para reduzir bounce; rastrear animações direto no gesto; evitar animar profundidade em camadas z; trocar transições x/y/z por fades; evitar animar entrando/saindo de blur. [AMBOS]
  - VoiceOver: descrever interface e conteúdo; teclado: não sobrescrever atalhos do sistema; Full Keyboard Access e Switch Control citados.
  - Changelog: 9/jun/2025 (Assistive Access, Switch Control, Accessibility Nutrition Labels); 7/mar/2025 (Dynamic Type movido para Typography).
- Para que serve: auditoria de todas as telas (formulários, agenda, mensagens, dashboards).
- Limitações: termos nativos (VoiceOver, Dynamic Type); no PWA o equivalente é leitor de tela do SO + `prefers-reduced-motion` + zoom/`rem`.

## Ficha 4: Apple HIG, Design principles

- https://developer.apple.com/design/human-interface-guidelines/design-principles | status: ✅ abriu (a 1ª leitura veio vazia por carregamento tardio; releitura ok)
- Tema: princípios; nível: iniciante; EN; gratuito. Tags: [oficial]
- Conteúdo: 8 princípios: Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight. Changelog: "June 8, 2026: Reintroduced design principles."
- Regras utilizáveis (sem números):
  - Agency: levar direto à tarefa; fluxos guiados fáceis de pular; facilitar recuperação de erros (desfazer). [AMBOS]
  - Responsibility: pedir permissão com justificativa; coletar só o necessário. [AMBOS]
  - Familiarity: manter aparência e comportamento consistentes; dar feedback claro. [AMBOS]
  - Flexibility: acessibilidade desde o início; preservar contexto ao adaptar entre plataformas; suportar vários métodos de entrada. [AMBOS]
  - Simplicity: "simplicidade não é minimalismo"; hierarquia clara; texto conciso. [AMBOS]
  - Delight: não confundir delight com decoração; "momentos definidores" (inclusive mensagens de erro). [AMBOS]
- Para que serve: critérios de revisão de design (design-direction).
- Limitações: nível alto, sem números.

## Subpáginas extras do HIG (visitadas)

### Layout
- https://developer.apple.com/design/human-interface-guidelines/layout | ✅ | atualizada em 9/set/2026
- Regras: ordenar por importância (topo/lado inicial); alinhar e agrupar; **progressive disclosure**; diferenciar controles de conteúdo (Liquid Glass; "scroll edge effect"); conteúdo de fundo deve se estender sob sidebars/toolbars/tab bars. [AMBOS]
- **Size classes** (iOS/iPadOS): horizontal e vertical, cada uma compact ou regular. Decidir layout por size class, não por dispositivo ou orientação; manter a funcionalidade e mudar só quanto é visível; em espaços maiores, trocar tab bar por sidebar. [AMBOS]
- Safe areas e layout guides: respeitar; margens e largura legível de texto vêm dos guides do sistema. **Valores de margem em pt para iPhone: não especificado.** Breakpoints em px: não especificado (Apple usa size classes).
- Números só para tvOS (safe area 60 pt topo/base e 80 pt laterais; grid 2 colunas 860 pt, espaçamento 40/100 pt), visionOS (centros de botões ≥60 pt) e watchOS: **não aplicáveis**.
- Testar com Dynamic Type, localizações e menores/maiores layouts.

### Typography
- https://developer.apple.com/design/human-interface-guidelines/typography | ✅
- Regras: evitar pesos Ultralight, Thin e Light; preferir Regular, Medium, Semibold, Bold; minimizar o número de typefaces; manter hierarquia ao aumentar o texto; priorizar conteúdo importante ao escalar; não truncar em áreas roláveis; empilhar layout em tamanhos grandes. [AMBOS]
- Fontes: SF Pro (variável, com optical sizes dinâmicos), SF Pro Rounded, New York (serifada). Não embutir fontes do sistema em apps nativos. [PWA: usar `system-ui`/`-apple-system` ou fonte própria]
- **Escala iOS/iPadOS (tabela capturada no tamanho de Dynamic Type "xSmall", que foi a aba exibida; NÃO é o tamanho padrão "Large")**: Large Title 31/38 pt, Title 1 25/31, Title 2 19/24, Title 3 17/22, Headline 14/19 (semibold), Body 14/19, Callout 13/18, Subhead 12/16, Footnote 12/16, Caption 1 11/13, Caption 2 11/13 (tamanho/leading). A tabela do tamanho Large (padrão) não foi capturada; só se confirma pela página Accessibility que o corpo padrão do iOS é 17 pt. Tamanhos de acessibilidade AX1: Large Title 44/52, Title 1 38/46, Title 2 34/41, Title 3 31/38, Headline 28/34, Body 28/34, Callout 26/32, Subhead 25/31, Footnote 23/29, Caption 1 22/28, Caption 2 20/25.
- **Tracking SF Pro (1/1000 em)**: 11 pt +6; 12 pt 0; 13 pt −6; 14 pt −11; 15 pt −16; 16 pt −20; 17 pt −26; 18 pt −25; 20 pt −23; 22 pt −12; 24 pt +3; 28 pt +14; 34 pt +12; 40 pt +10; 48 pt +8; 60 pt +4; 80 pt 0. [AMBOS: pode virar `letter-spacing` em em]
- macOS não suporta Dynamic Type.

### Color e Dark Mode
- https://developer.apple.com/design/human-interface-guidelines/color e `/dark-mode` | ✅
- Regras: papéis semânticos (background primário/secundário/terciário; label primário/secundário/terciário/quaternário; separator; link; placeholder); não usar um papel com outro significado; não fixar valores de cores do sistema ("podem mudar entre versões"); fornecer variantes light, dark e alto contraste mesmo se o app tiver um só modo; não depender só da cor; considerar cultura (ex.: vermelho/verde em Stocks). [AMBOS]
- Liquid Glass sem cor própria; cor só com parcimônia, no fundo de ação primária. [PWA: só como referência visual]
- **Dark Mode**: não oferecer configuração de aparência específica do app; contraste mínimo **4,5:1**, buscar **7:1** em texto pequeno; usar fundos "base" e "elevated" (camadas mais claras para o que está à frente); suavizar fundos brancos de imagens. Valores RGB de cores do sistema: **não capturados** (swatches visuais).
- Observação para o produto: "evitar configuração de aparência própria" vale para app nativo; num PWA, seguir `prefers-color-scheme` é o equivalente.

### Tab bars
- https://developer.apple.com/design/human-interface-guidelines/tab-bars | ✅ | atualizada 8/jun/2026
- Regras: tab bar para navegação, não para ações (ações vão em toolbar); sempre visível ao navegar entre seções (exceto sob modal); poucas abas (mais fácil); evitar abas de overflow ("More"); não desabilitar nem esconder abas (explicar se a seção está vazia); rótulos de uma palavra; ícones preenchidos; badge só para informação crítica (oval vermelho); no iPhone a tab bar flutua sobre o conteúdo com fundo Liquid Glass e pode minimizar ao rolar; no iPad fica no topo e pode virar sidebar; ao permitir personalização, padrão de **cinco abas ou menos**. [PWA / AMBOS]
- Altura da tab bar no iPhone: **não especificado** (só tvOS: 68 pt, a 46 pt do topo).

### Sheets
- https://developer.apple.com/design/human-interface-guidelines/sheets | ✅ | atualizada 24/mar/2026
- Regras: sheet para tarefa curta e contextual; apenas uma sheet por vez; no iOS pode ser modal ou não modal; botões: Cancel (borda inicial), Done (borda final), Back para fluxos de vários passos; nunca mostrar os três juntos; sempre emparelhar Done com Cancel ou Back. **Detents**: `large` (altura total) e `medium` (cerca de metade da altura total); incluir **grabber** em sheets redimensionáveis (também permite VoiceOver); suportar deslizar para baixo para dispensar e, se houver alterações não salvas, confirmar com action sheet; no iPad, preferir estilos page/form sheet. Para fluxos longos ou complexos, preferir alternativa (tela cheia). [PWA]
- Duração/animação de apresentação: não especificado.

---

## Ficha 5: Material 3, Motion (visão geral e "how it works")

- https://m3.material.io/styles/motion (redirecionou para `/styles/motion/overview/how-it-works`) | status: ✅ abriu
- Links 5 e 6 mostram o **mesmo conteúdo**.
- Subpáginas visitadas: `/styles/motion/overview/specs`, `/styles/motion/easing-and-duration/tokens-specs`.
- Tema: motion; nível: intermediário/avançado; EN; gratuito. Tags: [oficial]
- Regras e números extraídos:
  - **M3 Expressive (maio/2025)** introduziu o sistema de **física com springs**; "substitui o sistema anterior baseado em easing e duração".
  - Dois esquemas de motion: **expressive** (overshoot/bounce, para momentos de destaque e interações-chave) e **standard** (mínimo de bounce, para produtos utilitários). Dá para criar esquema customizado.
  - Spring = rigidez (stiffness) + amortecimento (damping) + velocidade inicial. Tokens: `md.sys.motion.spring.{fast|default|slow}.{spatial|effects}`; o esquema é escolhido no nível do produto, não no nome do token.
  - **Spatial** (posição, rotação, tamanho, cantos arredondados): pode ultrapassar o valor final. **Effects** (cor, opacidade): sem overshoot.
  - Velocidades: default para animações que cobrem parte da tela (bottom sheet); fast para componentes pequenos (switch, botão); slow para telas inteiras.
  - Valores numéricos de stiffness/damping: **não especificado** no texto das páginas (aparecem em módulo de tokens).
  - Disponibilidade: Jetpack Compose e Android Views disponíveis; Flutter indisponível; Web "compatível com springs do Compose".
  - **Tabela oficial Web: converter springs em curvas (cubic-bezier + duração)**:
    - Expressive fast spatial `0.42, 1.67, 0.21, 0.90` 350 ms
    - Expressive default spatial `0.38, 1.21, 0.22, 1.00` 500 ms
    - Expressive slow spatial `0.39, 1.29, 0.35, 0.98` 650 ms
    - Expressive fast effects `0.31, 0.94, 0.34, 1.00` 150 ms
    - Expressive default effects `0.34, 0.80, 0.34, 1.00` 200 ms
    - Expressive slow effects `0.34, 0.88, 0.34, 1.00` 300 ms
    - Standard fast/default/slow spatial `0.27, 1.06, 0.18, 1.00` com 350 / 500 / 750 ms
    - Standard fast/default/slow effects iguais às de expressive (150 / 200 / 300 ms)
    - Recomendação: usar springs quando houver gesto ou interrupção; usar as curvas só em animações sem interrupção.
  - **Sistema legado (ainda disponível, "não mais mantido")**:
    - Easing emphasized decelerate `cubic-bezier(0.05, 0.7, 0.1, 1.0)`; emphasized accelerate `cubic-bezier(0.3, 0.0, 0.8, 0.15)`; "emphasized" puro não tem equivalente CSS (usar standard).
    - Standard `cubic-bezier(0.2, 0.0, 0, 1.0)`; standard decelerate `cubic-bezier(0, 0, 0, 1)`; standard accelerate `cubic-bezier(0.3, 0, 1, 1)`.
    - Durações: short1–4 = 50/100/150/200 ms; medium1–4 = 250/300/350/400 ms; long1–4 = 450/500/550/600 ms; extra-long1–4 = 700/800/900/1000 ms. Exemplos oficiais: seleção 200 ms standard; FAB→sheet 400 ms emphasized; card→tela cheia 500 ms emphasized; carrossel ambiente 1000 ms.
  - Reduce motion/`prefers-reduced-motion`: **não especificado** nestas páginas.
- Para que serve: tokens de motion do app (sheets, transições de tela, botões), e mapa para `transition` do Motion for React (springs) ou CSS (cubic-bezier). [AMBOS]
- Limitações: springs em Compose; no Web depender da tabela de conversão. Observação: valores de y > 1 nas curvas spatial produzem overshoot em CSS.

## Ficha 6: Material 3, Adaptive design (link 7)

- https://m3.material.io/foundations/adaptive-design/overview (redirecionou para `/foundations/layout/layout-overview/overview`) | status: ✅ abriu
- Subpáginas visitadas: `/foundations/layout/breakpoints/overview` (a URL `.../applying-layout/window-size-classes` redirecionou para ela), `/foundations/layout/grids-spacing/spacing`, `/styles/typography/type-scale-tokens`, `/foundations/designing/structure` (acessibilidade).
- Tema: layout adaptativo; nível: intermediário; EN; gratuito. Tags: [oficial]
- Renomeações (maio/2026): **"window size classes" → "breakpoints"; "responsive layout" → "adaptive design"**; novo **layout scaffold**; guias para mobile, desktop e espacial.
- **Breakpoints (largura em dp)**: Compact <600 (celular em retrato); Medium 600–839; Expanded 840–1199 (inclui celular em paisagem e desktop); Large 1200–1599; Extra-large ≥1600. Também há breakpoints de altura (compact/medium/expanded), raramente necessários.
- **Painéis recomendados**: compact 1; medium 1 (ou 2); expanded 1 ou 2 (recomendado 2); large 1 ou 2 (recomendado 2); extra-large 1 a 3. Dois painéis em medium só com conteúdo de baixa densidade.
- **Navegação por breakpoint**: compact = navigation bar (ou rail expandida modal); medium = navigation bar ou rail; expanded+ = rail expandida (modal ou standard). Diálogos: full-screen dialog/bottom sheet em compact; menu em medium+.
- Cinco perguntas ao mudar de breakpoint: o que revelar, dividir, redimensionar, reposicionar, trocar. Trocar só componentes funcionalmente equivalentes (barra inferior ↔ rail; bottom sheet ↔ menu); não trocar botão por chip.
- **Largura de linha de texto**: ajustar margens e estilos para **40–60 caracteres por linha**.
- Margens e gap em dp, grid de colunas: **não especificado** nas páginas lidas (a página de spacing só traz princípios: agrupamento, ritmo, proximidade).
- **Tipografia M3**: 1 escala com 30 estilos (15 baseline + 15 emphasized, de Display Large a Label Small); escala **Major Second (1,125)**, tamanho-base **14**; fonte padrão Roboto (brand para Display/Headline, plain para Body/Label); web usa `rem` (16 px = 1 rem; sp/16); line height se adapta por categoria de idioma (script latino = base; CJK/árabe etc. ≈ +7%; birmanês/telugu ≈ +30%). Tabela de tamanhos por estilo: **não especificado no texto capturado**. Evitar mudar o tamanho ao customizar estilos.
- **Alvos (Material, acessibilidade)**: toque **mínimo 48×48 dp** (≈ 9 mm; recomendado 7–10 mm); ícone 24 dp com padding até 48; ponteiro mínimo 44×44 dp; espaçamento entre alvos **8 dp ou mais**. A página cita que o iOS recomenda 44×44.
- Acessibilidade web: 8 landmarks ARIA (navigation, search, main, banner, complementary, contentinfo, region, form); rótulos únicos em landmarks repetidos; um só H1; não pular níveis de heading.
- Cor e papéis de cor, dark mode e navigation bar (altura): **não lidos nesta rodada** (fora dos links semente).
- Para que serve: grelha do painel web (gestor/cliente) e transição PWA ↔ desktop; escolha de navegação por largura.
- Limitações: unidade dp (Android); no web aplicar como px CSS (equivalência 1 dp ≈ 1 px CSS é inferência minha, não da fonte).

---

## Ficha 7: Carbon Design System, Motion (link 31)

- https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview | status: ✅ abriu (banner de cookies apareceu; não foi aceito nem alterado)
- Abas "Choreography" e "Code" existem; **não visitadas**.
- Tema: motion; nível: intermediário; EN; gratuito (open source). Tags: [oficial]
- Regras e números extraídos:
  - Dois estilos: **productive** (eficiente, sutil, para tarefas) e **expressive** (momentos importantes: nova página, ação primária, alertas). Reservar expressive para momentos ocasionais.
  - **Easing** (CSS): standard productive `cubic-bezier(0.2, 0, 0.38, 0.9)`; standard expressive `cubic-bezier(0.4, 0.14, 0.3, 1)`; entrance productive `cubic-bezier(0, 0, 0.38, 0.9)`; entrance expressive `cubic-bezier(0, 0, 0.3, 1)`; exit productive `cubic-bezier(0.2, 0, 1, 0.9)`; exit expressive `cubic-bezier(0.4, 0.14, 1, 1)`.
  - Usar standard quando o elemento está visível do início ao fim; entrance ao aparecer; exit ao sair definitivamente (se sai mas fica perto, como side panel, usar standard).
  - **Tokens de duração**: `duration-fast-01` 70 ms (botão, toggle); `duration-fast-02` 110 ms (fade); `duration-moderate-01` 150 ms (expansões pequenas); `duration-moderate-02` 240 ms (expansão, toast); `duration-slow-01` 400 ms (grandes expansões, notificações importantes); `duration-slow-02` 700 ms (escurecimento de fundo).
  - Duração deve crescer com a distância/tamanho da animação; "Motion Generator" calcula; dynamic duration "em breve".
  - Checklist: feedback imediato; microinteração com ease-out e duração estática **90–120 ms**; em telas pequenas movimentos sutis passam despercebidos; se o usuário nota o motion com frequência, considerar remover.
  - Motion adaptativo: sempre oferecer alternativas às transições de estado, versões simplificadas/reduzidas para mobile e tablet, e uma forma estática de comunicar a mesma mensagem.
  - Em Carbon, `prefers-reduced-motion` por nome: **não especificado**.
- Para que serve: tabela de durações/easing de referência para botões, toasts, modais, painéis laterais, dashboards. [AMBOS, com ênfase em WEB]
- Limitações: pensado para produtos enterprise desktop; nada sobre gestos, toque nem navegação mobile nesta página.

---

## Tabela comparativa: Apple × Material 3 × Carbon

| Critério | Apple HIG | Material 3 | Carbon |
|---|---|---|---|
| Durações de motion | **Não especificado** (princípio: breve, cancelável) | Springs (expressive/standard × fast/default/slow). Equivalentes web: spatial 350/500/650 ms (expressive), 350/500/750 (standard); effects 150/200/300 ms. Legado: 50 a 1000 ms em 16 tokens | 70, 110, 150, 240, 400, 700 ms; micro 90–120 ms |
| Easing | **Não especificado** (watchOS: easing embutido, não customizável) | Spring (stiffness+damping). Legado/CSS: standard `0.2,0,0,1`; emphasized decelerate `0.05,0.7,0.1,1`; accelerate `0.3,0,0.8,0.15`. Spatial expressive default `0.38,1.21,0.22,1.00` | Productive `0.2,0,0.38,0.9`; expressive `0.4,0.14,0.3,1`; entrance e exit com variantes |
| Alvos de toque | **44×44 pt** padrão, 28×28 pt mínimo; 12 pt de padding (com bezel) / 24 pt (sem bezel) | **48×48 dp**; ponteiro 44 dp; ≥8 dp entre alvos | **Não especificado** na página lida |
| Escala tipográfica | iOS: padrão 17 pt, mínimo 11 pt; 11 text styles + tamanhos AX; SF Pro; evitar pesos finos | Major Second 1,125, base 14; 15 baseline + 15 emphasized; Roboto; sp/rem | **Não especificado** (página de motion apenas) |
| Navegação mobile | Tab bar inferior (poucas abas, ≤5 se personalizável, sempre visível, sem desabilitar); sheets com detents medium/large e grabber; sidebar no iPad | Navigation bar (compact); rail em medium+; bottom sheet em compact ↔ menu em medium+; 1 painel em compact/medium | **Não especificado** |
| Reduce Motion | Detalhado (springs mais firmes, fades no lugar de x/y/z, sem blur animado) | **Não especificado** nas páginas lidas | Princípio de alternativas reduzidas/estáticas, sem detalhes |

Leitura prática para o app (inferência minha, a validar na síntese): usar a regra de acessibilidade/gestos da Apple, os números de duração/easing do Carbon (ou das curvas web do Material) e os breakpoints do Material para o painel.

---

## Fontes verificadas (URLs abertas)

Links semente:
1. https://developer.apple.com/design/human-interface-guidelines/ ✅
2. https://developer.apple.com/design/human-interface-guidelines/foundations/motion ✅ (redirecionou para `/motion`)
3. https://developer.apple.com/design/human-interface-guidelines/accessibility ✅
4. https://developer.apple.com/design/human-interface-guidelines/design-principles ✅
5. https://m3.material.io/styles/motion ✅ (redirecionou para `/styles/motion/overview/how-it-works`)
6. https://m3.material.io/styles/motion/overview/how-it-works ✅
7. https://m3.material.io/foundations/adaptive-design/overview ✅ (redirecionou para `/foundations/layout/layout-overview/overview`)
31. https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview ✅

Subpáginas visitadas:
- https://developer.apple.com/design/human-interface-guidelines/layout ✅
- https://developer.apple.com/design/human-interface-guidelines/typography ✅
- https://developer.apple.com/design/human-interface-guidelines/color ✅
- https://developer.apple.com/design/human-interface-guidelines/dark-mode ✅
- https://developer.apple.com/design/human-interface-guidelines/tab-bars ✅
- https://developer.apple.com/design/human-interface-guidelines/sheets ✅
- https://m3.material.io/styles/motion/overview/specs ✅
- https://m3.material.io/styles/motion/easing-and-duration/tokens-specs ✅
- https://m3.material.io/foundations/layout/applying-layout/window-size-classes ✅ (redirecionou para `/foundations/layout/breakpoints/overview`)
- https://m3.material.io/foundations/layout/understanding-layout/spacing ✅ (redirecionou para `/foundations/layout/grids-spacing/spacing`)
- https://m3.material.io/styles/typography/type-scale-tokens ✅
- https://m3.material.io/foundations/designing/structure ✅ (título "Accessibility designing")

Observações de leitura: as páginas do HIG carregam o conteúdo depois do primeiro render; as leituras de `design-principles` e `layout` vieram vazias na primeira tentativa e foram refeitas com espera. Nenhum link deu 404 nem exigiu login.

## Prints

5 prints de referência visual (layouts e componentes que servem de modelo), entregues como arquivos separados:

| Nome | URL | O que mostra | Como usar de referência |
|---|---|---|---|
| 9A_m3-canonical-listdetail_1.jpg | https://m3.material.io/foundations/layout/canonical-examples/overview | Layout canônico list-detail anotado (Bar, Rail, Pane 1, Pane 2) | Painel web do gestor: lista de conversas/clientes + detalhe; kit Figma "M3 Design Kit" e código Compose linkados na página |
| 9A_m3-canonical-feed_1.jpg | https://m3.material.io/foundations/layout/canonical-examples/overview | Layout canônico feed (grade de cards com rail, barra de filtros em chips, pane) | Portfólio e conteúdo: grade de cards com filtros |
| 9A_apple-tabbar_1.jpg | https://developer.apple.com/design/human-interface-guidelines/tab-bars | Tab bar iOS flutuante: 4 abas + aba de busca separada, aba ativa em destaque | Navegação inferior do PWA/Capacitor (visual iOS-like) |
| 9A_apple-sheet-detents_1.jpg | https://developer.apple.com/design/human-interface-guidelines/sheets | Sheet iPhone nos detents large e medium, com grabber e botão de fechar | Bottom sheets (agenda, detalhe de proposta, filtros) |
| 9A_carbon-easing-curves_1.jpg | https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview | Curvas distância × tempo de productive e expressive, com os dois círculos de demonstração | Comparar a sensação das duas curvas ao calibrar `transition` |

Observação: os prints das tabelas de números (alvos, breakpoints, durações) foram dispensados, pois os valores já estão em texto nas fichas. Tentativas descartadas por pouco valor: breakpoints do Material (só texto) e tokens de duração do Carbon (coberta pelo banner de cookies, que não foi aceito).
