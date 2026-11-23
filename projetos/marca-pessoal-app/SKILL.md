---
name: marca-pessoal-app
description: Skill exclusiva do app de gestão de marca pessoal (presença, conteúdo, agenda, portfólio, networking, propostas, contratos, mensagens e resultados), com painel web para gestor e cliente e app do cliente em PWA, depois empacotado com Capacitor. Traz as decisões já tomadas para este produto (D1–D8), o stack, os tokens da Fase 1, os fluxos críticos, o checklist de 56 itens e o plano de 90 dias, e indica qual skill geral de design abrir em cada caso. Use sempre que a tarefa for neste app: criar ou revisar tela, componente, fluxo, design system, motion, onboarding, perfil, portfólio, agenda, propostas, mensagens, painel do gestor ou do cliente, ou "auditar o app de marca pessoal".
---

# App de gestão de marca pessoal

Esta skill vale **só para este app**. As regras gerais de design ficam nas skills gerais (`mobile-app-ui`, `desktop-app-ui`, `website-ui`, `ui-motion`, `ux-patterns`, `design-direction`, `dashboard-ui`). Aqui estão só as decisões do produto.

**Prioridade:** neste app, as decisões abaixo valem sobre as skills gerais. No resto, siga as skills gerais, que valem sobre as de terceiros.

## Produto
- **Usuários:** profissionais que gerenciam a própria marca pessoal. Público avançado, em PT e EN.
- **Painel web:** para o gestor (opera e acompanha a carteira) e para o cliente (acompanha o próprio resultado) → `desktop-app-ui`.
- **App do cliente:** PWA no piloto; depois o mesmo código React vai para iOS e Android com Capacitor → `mobile-app-ui`.
- **Perfil e portfólio públicos:** quando forem página aberta → `website-ui`.
- **Stack:** React 18, TypeScript, Vite, Supabase, Tailwind, shadcn/ui na variante **Base UI** (uma base só), Motion for React. **Não usar React Native.**
- **Visual:** inspirado em iOS (clean, tipografia forte, gestos naturais, animações curtas), sem copiar a Apple.

## Decisões do produto (D1–D8)
| # | Decisão |
|---|---|
| D1 | Tipografia: escala 16 × 1,2ⁿ com corpo 16 no app **e** no painel; botão primário em 16 ou 19 semibold. O corpo 17 pt do iOS é só referência. Perfil público (site) em Major Third 1,25 |
| D2 | "Feedback em 100 ms, concluído em 300 ms" é prazo de resposta do sistema. A animação do press segue o `ui-motion`: feedback visual em 0 ms, press de 160 ms, escala 0,95 |
| D3 | O painel web usa os mesmos tokens de motion do app. Onde o `ui-motion` não define, micro = 80 ms. Carbon só como comparação |
| D4 | Painel operacional do gestor **sem gauge**: barras e linhas. No painel e no app do cliente, só anel de meta com o número visível, no máximo 1–2 por tela (`dashboard-ui` padrão 17) |
| D5 | Tab bar com **5 abas como hipótese**: Início, Agenda, Conteúdo, Mensagens, Perfil. Validar com teste de usuários antes de fechar. Sem aba "More" |
| D6 | O app do cliente segue o tema do sistema, sem seletor. O painel web tem seletor Claro/Escuro/Sistema |
| D7 | Sem personalização por cliente no piloto. Depois, só a cor de destaque, com contraste ≥ 4,5:1 validado automaticamente |
| D8 | Largura de texto: token `--measure: 50ch`. Regra: 45–75 caracteres, 45–60 em formulários |

## Obrigatório desde o dia 1
- `<MotionConfig reducedMotion="user">` na raiz. O padrão do Motion é `"never"`.
- Tokens: `--press-scale .95`, `--dur-press 160ms`, micro 80 ms, `--dur-expand 350ms` ease-out, `--dur-success 470ms`, `--dur-reveal ≤700ms`, `--stagger 70/100ms`, curva `cubic-bezier(0.22, 1, 0.36, 1)`.
- Alvos de toque: `--tap: 44px` (48 no botão primário) e `--tap-gap: 8px`. Safe areas com `env(safe-area-inset-*)`; `body { position: relative }` para o Drawer no iOS.
- Breakpoints: 375 / 768 / 1024 / 1280 / 1440 / 1920.
- Cor: 2 bases + 1 acento em 60/30/10. Dark mode em `#0C1424`, com texto a 87%.
- Qualidade: Lighthouse e axe-core no CI; Playwright nas viewports 360, 375, 390, 768, 1280 e 1440.
- Camada própria `ios/`: tab bar, título grande de 34 → 18 px, sheet com snap points (Drawer do shadcn) e swipe-back. Ionic React só como plano B, se o app empacotado no Capacitor precisar de transições nativas.

## Quando abrir `references/sintese.md`
| Precisa de | Seção |
|---|---|
| Tabela completa da Fase 1 (tokens, shell, acessibilidade) | §13 Fase 1 |
| Onboarding, perfil, portfólio, agenda, propostas, mensagens, configurações, estados | §13 Fase 2 |
| Identidade, motion system, gestos, animação de dados | §13 Fase 3 |
| Auditar uma tela ou o app (56 itens sim/não) | §14 |
| Plano de 90 dias e critérios de pronto | §15 (g) |
| Por que shadcn e não Mantine, HeroUI ou Ionic | §15 (h) |
| Referências, ferramentas, onde aprender | §6–12, §15 (a)–(e) |
| Lacunas e conflitos já resolvidos | §16 |

## Workflow
1. **Identifique a superfície:** app do cliente (`mobile-app-ui`), painel web (`desktop-app-ui`) ou página pública (`website-ui`).
2. **Aplique D1–D8 e os itens obrigatórios** acima. Para o detalhe do fluxo, abra a §13 da síntese.
3. **Siga a skill geral da superfície** para o resto (componentes, estados, motion, UX).
4. **Antes de entregar**, rode os itens relevantes do checklist (§14) e teste nas viewports.
