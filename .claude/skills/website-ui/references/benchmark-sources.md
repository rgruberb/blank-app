# Fontes de benchmark para website

Pesquisa 9C (verificado em 22–23/11/2026; dado bruto em `docs/achados/rodada-9C.md`). ✅ = aberto sem login ·
⚠️ = abre com limite · 🔒 = exige login (pendente). Lista geral de galerias e perfis:
`design-direction/references/learning-sources.md` §5.

| Fonte | Status | Serve para | Limite |
|---|---|---|---|
| **Awwwards** (awwwards.com; /websites/portfolio/) | ✅ | landing e portfólio de alto nível: hero, tipografia, motion; Site of the Day com nota | premia sites experimentais e pesados (WebGL, scroll-jacking) que ferem LCP/INP e a regra de 1 momento animado; Academy/Creative Pass pagos |
| **Land-book** (land-book.com) | ✅ | **padrões de seção** (hero, pricing, case, footer): abas Websites / **Sections** / Mobile / Motion / OG Images / Headlines; filtros Landing, Portfolio, Blog, Ecommerce | só web; parte dos itens são templates pagos |
| **SiteInspire** (siteinspire.com/websites) | ✅ | layout editorial e tipografia forte; filtros por categoria, estilo, tipo, assunto, plataforma (Portfolio 1.449, Typographic 2.108, Minimal 861 em 22/11/2026) | acervo de agências; `?categories=5` redireciona sem filtro — filtre pela interface |
| **Coolors** (coolors.co; /contrast-checker) | ✅ | gerar/extrair paleta, prévia, Tailwind Colors; **contrast checker WCAG** (AA 4,5:1 normal / 3:1 grande; AAA 7:1 / 4,5:1) | paleta ≠ papéis semânticos; exportar tokens exige conferência; limites do plano grátis não verificados |
| **Typewolf** (typewolf.com; /google-fonts) | ✅ | "What's Trending in Type" (sites reais + fontes); **"40 Best Google Fonts"** (open source, uso comercial, vários pesos; atual. 12/01/2026); "Flawless Typography Checklist" | muitas fontes da home são pagas; pares do guia de fontes livres **não extraídos**; licença de embed em app: ler na foundry |
| Dribbble | ⚠️ | tendência de landing/portfólio em shot | conceito editado; anti-bot após ~20 aberturas |
| Behance | ⚠️ | case completo de marca/site | "log in to view more" |
| Mobbin (seção Sites) | 🔒 **pendente** | sites reais por fluxo | exige conta; MCP só no Pro (o conector deste ambiente responde "requires a paid plan") |
| Godly → recent.design, Refero, designeer.xyz | ⚠️ (rodadas 10A/C2) | sites escolhidos a dedo (Godly), telas e fluxos reais (Refero, MCP pago), catálogo curado (designeer) | ver `design-direction/references/learning-sources.md` §5 e `reference-apis.md` |

## Como usar sem copiar
1. Escolha **1 pergunta** por busca ("como sites de serviço pessoal mostram preço?") e junte **3–5** exemplos de fontes diferentes.
2. Anote **estrutura e decisão** (ordem das seções, tamanho do hero, onde fica o CTA, quanto texto), não cor, foto,
   ilustração, copy nem logo; refaça com os tokens de `design-direction`.
3. Rode o exemplo escolhido no PageSpeed/Lighthouse antes de imitar o efeito: Awwwards premia o que pesa.
4. Passe paleta e pares pelo Coolors (claro e escuro) e a fonte pela licença.
5. URL de referência que o usuário trouxe → `ext-extract-design` extrai tokens para **estudo**, não para clonar marca.

## Prints da pesquisa 9
Na repo (caminho a partir de `.claude/skills/`):
- `segmento-marca-pessoal/assets/visual-refs/9C_portfolio_awwwards-daniel-neath_1.jpg` — portfólio de product design: título grande, navegação e hero.
- `segmento-marca-pessoal/assets/visual-refs/9C_landing_land-book_1.jpg` — abas Websites/Sections/Mobile/Motion e filtros por tipo.
- `segmento-publicidade/assets/visual-refs/9C_portfolio_siteinspire_1.jpg` — galeria com filtros por categoria.
- `design-direction/assets/visual-refs/9C_coolors_contrast-checker_1.jpg` — contrast checker (razão 8,42 e nota por tamanho de texto).
- `design-direction/assets/visual-refs/9C_typewolf_google-fonts_1.jpg` — lista "40 Best Google Fonts".
- `ux-patterns/assets/visual-refs/9B_formularios_slack-forca-senha_1.jpg` — validação de senha inline (formulário de cadastro).

Não versionados (ficaram no scratchpad da pesquisa; reabra pela URL da fonte): `ref_landbook_home_1.jpg` e
`ref_siteinspire_home_1.jpg`, segundas capturas das mesmas homes acima — use as versões da repo.
