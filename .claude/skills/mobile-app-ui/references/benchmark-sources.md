# Fontes de benchmark para app mobile

Pesquisa 9 (nov/2026; dado bruto em `docs/achados/rodada-9A.md`…`9D.md`). ✅ = aberto sem login · ⚠️ = abre com
limite · 🔒 = exige login (pendente). Lista geral de galerias e perfis para continuar aprendendo:
`design-direction/references/learning-sources.md` §5.

| Fonte | Status | Serve para | Limite |
|---|---|---|---|
| **Mobbin** (mobbin.com) | 🔒 **pendente** | telas e fluxos reais de apps iOS/Android (onboarding, paywall, agenda, mensagens, perfil); seção Animations | só a home é pública; biblioteca e categorias exigem conta; MCP só Pro/Team. Abrir logado numa rodada própria |
| Apple HIG + kit Figma **iOS and iPadOS 26/27** | ✅ | comportamento oficial (tab bar, sheet, layout guides, safe areas) | licença Apple Design Resources: só mockup; exige SF Symbols instalado |
| Material 3 (m3.material.io) + **Material 3 Design Kit** (Figma, CC BY 4.0) | ✅ | breakpoints, rail, layouts canônicos (list-detail, feed) | unidades em dp; springs só em Compose |
| NN/g (nngroup.com) | ✅ | regra testada com usuário (alvos, navegação, onboarding, permissões, formulários) | muitos estudos 2015–2019; sem motion nem PWA; relatório mobile (5ª ed.) é pago |
| Dribbble | ⚠️ | tendência visual de telas mobile | shots são conceito editado, não produto; anti-bot após ~20 aberturas |
| Behance | ⚠️ | estudo de caso com várias telas e processo | "log in to view more"; muito case de estudante (filtre por apreciações) |
| Ionic docs / Framework7 kitchen sink | ✅ | ver padrões iOS rodando no navegador (sheet, tab bar, título grande) | estilo próprio da lib |
| Motion examples (motion.dev/examples) | ✅ | swipe actions, sheet, card stack | parte dos exemplos é Motion+ (pago) |

## Como usar sem copiar
1. Defina antes a pergunta (ex.: "como apps de agenda mostram o slot livre?") e colete **3–5** telas de fontes diferentes.
2. Anote o **padrão** (estrutura, hierarquia, estado, gesto), não pixels, cores nem ilustrações; refaça com os tokens do projeto.
3. Prefira app em produção (Mobbin, kits oficiais) a shot conceitual; shot sem estado vazio/erro não prova nada.
4. Confira a regra na fonte oficial (HIG/Material/NN/g) antes de adotar algo visto só em galeria.
5. Nunca reproduza marca, ícones (SF Symbols), assets de kit Apple ou layout inteiro de terceiros.

## Prints da pesquisa 9 (não versionados)
Ficam fora da repo (pasta de scratchpad da pesquisa); reabra pela URL da fonte se precisar.
- `9A_apple-tabbar_1.jpg` — tab bar iOS flutuante, 4 abas + busca separada.
- `9A_apple-sheet-detents_1.jpg` — sheet nos detents large e medium, com grabber e fechar.
- `9A_m3-canonical-listdetail_1.jpg` / `9A_m3-canonical-feed_1.jpg` — layouts canônicos M3 com bar/rail e painéis.
- `9B_navegacao_facebook-tabbar_1.jpg` — tab bar inferior iOS × no topo Android.
- `9B_touch-targets_target-app_1.jpg` — botões primários ~2 cm e tab bar de 5 com rótulo.
- `9B_permissoes_venmo-camera-negada_1.jpg` — câmera negada: explica e leva a "Open Settings".
- `9B_formularios_hoteltonight-botao-fixo_1.jpg` — formulário com pagamento fixo no rodapé.
- `9B_formularios_slack-forca-senha_1.jpg` — medidor de força de senha inline.
- `9B_empty-states_datadog_1.jpg` — empty state que ensina.
- `9C_perfil-criador_nomey_1..3.jpg` — perfil de criador e grade com tab bar flutuante de 4 ícones (conceito Behance).
- `9C_propostas_cook_1..2.jpg` — onboarding e cards de oferta (conceito Behance).
- `9D_figma-ios27-kit_1.jpg` — layout guides/safe areas do kit Apple iOS 27.
- `9D_shadcn-drawer_1.jpg` / `_2.jpg` — drawer lateral com CTA fixo; drawer inferior com handle e snap ("peek").
- `9D_ionic-ios-sheet-modal_1.jpg` / `9D_ionic-ios-tab-bar_1.jpg` — sheet e tab bar no modo iOS do Ionic.
- `9D_framework7-ios26-kitchen-sink_1.jpg` — título grande, lista agrupada inset (estilo iOS 26).
- `9D_motion-examples-swipe_1.jpg` — exemplos de swipe, sheet e card stack do Motion.
- `ref_dribbble_ui-ux-design_1.jpg` — listagem Dribbble "UI UX Design" (shots de app, banner de cookies).
