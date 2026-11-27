# Fontes de benchmark para app desktop / painel web

Pesquisa 9 (nov/2026; dado bruto em `docs/achados/rodada-9A.md`…`9D.md`). ✅ = aberto sem login · ⚠️ = abre com
limite · 🔒 = exige login (pendente). Lista geral de galerias e perfis: `../../design-direction/references/learning-sources.md` §5.

| Fonte | Status | Serve para | Limite |
|---|---|---|---|
| Material 3 layout (m3.material.io) | ✅ | breakpoints, rail, layouts canônicos list-detail / feed / supporting pane | dp; margens e grid em números não publicados nas páginas lidas |
| Carbon (carbondesignsystem.com) | ✅ | motion **productive** para ferramenta de trabalho; produto enterprise denso | nada de gestos/mobile |
| NN/g (nngroup.com) | ✅ | tabelas, dashboards, abas, empty states, CASTLE, apps complexos | estudos de 2017–2022; relatórios de apps corporativos parte grátis |
| shadcn Blocks + **Supabase Library** | ✅ | blocks de dashboard, login, conta, chat prontos sobre shadcn | blocks genéricos: troque tokens e hierarquia |
| Kits Figma: CRM UI Kit for SaaS Dashboards, Obra shadcn (CC BY 4.0) | ✅ | mapa de componentes e estados do painel | qualidade de kit de comunidade varia |
| Dribbble (tag dashboard / busca "creator dashboard") | ⚠️ | tendência visual de KPI, gráficos, sidebar | shot conceitual sem estados; anti-bot após ~20 aberturas |
| Behance | ⚠️ | case completo com processo | "log in to view more"; filtre por apreciações |
| **Mobbin** (seção Sites/Web apps) | 🔒 **pendente** | telas reais de web apps SaaS | exige conta |

## Como usar sem copiar
1. Comece pela **pergunta da tela** (o que o gestor decide aqui?) e colete 3–5 referências de fontes diferentes.
2. Extraia **estrutura** (shell, densidade, ordem dos blocos, estados), não paleta, ilustração ou marca.
3. Shot de Dribbble não tem dado real: refaça com os seus números e teste vazio, carregando, erro, texto longo.
4. Valide contra NN/g (barras/linhas, tabela com painel lateral) e contra `dashboard-ui` antes de adotar.

## Prints da pesquisa 9
Na repo (caminho a partir de `.claude/skills/`):
- `ui-motion/assets/visual-refs/9A_carbon-easing-curves_1.jpg` — curvas productive × expressive.
- `ux-patterns/assets/visual-refs/9B_tabelas_painel-lateral-crm_1.jpg` — tabela de oportunidades com edição em painel lateral não modal.
- `dashboard-ui/assets/visual-refs/9B_dashboards_linha-e-barras_1.jpg` — linha + barras, o formato recomendado.
- `ux-patterns/assets/visual-refs/9B_tabs_google-finance-in-page_1.jpg` — dois níveis de abas internas com gráfico.
- `ux-patterns/assets/visual-refs/9B_empty-states_datadog_1.jpg` — empty state que ensina.
- `dashboard-ui/assets/visual-refs/ref_dribbble_dashboard-ui_1.jpg` — listagem Dribbble de dashboards (banner de cookies).

Não versionados (ficaram fora da repo, no scratchpad da pesquisa; reabra pela URL da fonte):
- `9A_m3-canonical-listdetail_1.jpg` — list-detail anotado (bar, rail, pane 1, pane 2).
- `9A_m3-canonical-feed_1.jpg` — grade de cards com rail e filtros em chips.
- `9D_shadcn-blocks-dashboard_1.jpg` e `9D_shadcn-blocks-dashboard_2.jpg` — dashboard-01 no desktop e empilhado no mobile.
- `9D_figma-crm-dashboard-kit_1.jpg` — CRM kit: métricas, tarefas, tabelas, gráficos.
- `9D_figma-obra-shadcn-kit_1.jpg` — componentes shadcn no Figma.
- `9D_supabase-library-blocks_1.jpg` — blocks de login, métricas, chat e conta.
- `ref_dribbble_dashboard-ui_2.jpg` — segunda página da listagem Dribbble.
