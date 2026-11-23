# Bibliotecas de componentes para web app desktop (React)

Fonte: pesquisa 9D (docs e repositórios oficiais lidos em 22–23/11/2026; dado bruto em `docs/achados/rodada-9D.md`).
Cenário avaliado: painel web + app mobile (PWA → Capacitor) no mesmo código, Tailwind, **React 18**. Versões mudam:
confira antes de instalar. Versão mobile desta tabela (gestos, camada iOS): `../../mobile-app-ui/references/component-libraries.md`.

## Compatibilidade

| Biblioteca | Licença | React 18? | Estilo | Para o painel desktop |
|---|---|---|---|---|
| **shadcn/ui** | MIT | **sim** (novos projetos: Tailwind v4 + React 19; Tailwind v3 + React 18 segue funcionando) | Tailwind, código copiado | Sidebar, Navigation Menu, Breadcrumb, Menubar, **Data Table**/Table/Pagination, **Command** + Kbd (⌘K), Sheet (painel lateral), Dialog/Alert Dialog, Tabs, Calendar, Field/Combobox, Empty/Skeleton/Spinner, Toast (Base UI: success/info/warning/error/loading, `toast.promise`, "Undo"). 3 variantes: **Base UI / React Aria / Radix UI** — escolha uma e fique nela |
| Radix Primitives | MIT | sim | headless | base WAI-ARIA madura da variante Radix |
| React Aria | Apache-2.0 | sim | headless | a11y e i18n fortes (date picker, PT/EN); mais verboso |
| Headless UI | MIT (v2.2) | sim | headless + Tailwind | catálogo pequeno; redundante com shadcn |
| Mantine v9 | MIT | **não — exige React 19.2+** | CSS Modules | kit admin completo; só após migrar para React 19 |
| HeroUI v3 | Apache-2.0 | **não — exige React 19+ e Tailwind v4** | Tailwind v4 (base React Aria) | idem |
| Ionic React / Framework7 / Ant Design Mobile / Vant | MIT | — | próprio | **kits mobile**: não usar no painel desktop |
| Motion for React | MIT (núcleo) | sim (18.2+) | — | `layout`/`layoutId` (aba ativa, card → detalhe), `AnimatePresence` (toasts, painéis); `<MotionConfig reducedMotion="user">` (padrão é "never") |

## Critérios
Customização com Tailwind · acessibilidade (Base UI/Radix/React Aria) · compatível com React 18 hoje · peso (não
medido na 9D) · maturidade · licença · cobre tabela, ⌘K, sidebar e painel lateral sem lib extra.

## Recomendação (9D, Parte 4)
**shadcn/ui (variante Base UI) + Tailwind + Motion**, o mesmo stack do mobile; no desktop quase tudo já existe como
componente (Data Table, Command, Sidebar, Sheet). Mantine e HeroUI ficam para reavaliar se o projeto subir para React 19.
Ionic é plano B **só do app Capacitor**, nunca do painel. Qualidade: Lighthouse e axe-core no CI; Storybook quando os
componentes próprios passarem de ~10.

## Referências prontas (inspiração, não copiar)
- shadcn **Blocks** (`dashboard-01`: sidebar, KPI com tendência, gráfico com filtro de período) — ui.shadcn.com/blocks.
- Supabase Library — blocks de login, painel de métricas, chat e conta sobre shadcn (licença exata não verificada).
- Kits Figma: Obra shadcn/ui Community Edition (CC BY 4.0), CRM UI Kit for SaaS Dashboards (CC BY 4.0), Material 3
  Design Kit (CC BY 4.0). Ver `benchmark-sources.md`.
- **shadcn.io não é o shadcn/ui oficial**: site comercial; plano Individual só para uso pessoal/open source.
