# Skills de Design, UI/UX e Investimentos para Claude Code

Skills próprias, destiladas de ~70 reels do Instagram (vídeo + frames + transcrição do áudio), de 10 rodadas de coleta com a extensão Claude in Chrome (carrosséis, perfis e vídeos do Facebook, ver `docs/achados/`) e de um curso de 2h no YouTube, mais um instalador para as 7 skills de terceiros recomendadas pelo Chase AI.

## Estrutura

As skills estão em duas camadas:

1. **Por tema**: o conhecimento de base, que vale para qualquer plataforma.
2. **Por plataforma**: as regras específicas de cada plataforma, com ponteiros para as skills de tema e para as imagens delas. Essas skills não têm imagens próprias.

```
.claude/skills/
│  ── por plataforma ──
├── website-ui/         sites, landing pages, portfólio, e-commerce, blog (Major Third 1,25, Core Web Vitals, SEO)
├── desktop-app-ui/     web apps SaaS, admin, CRM e apps Mac/Windows (app shell, densidade 1,2, tabelas, teclado, ⌘K)
├── mobile-app-ui/      apps iOS/Android/React Native/Flutter (44pt/48dp, zona do polegar, tab bar, bottom sheet, gestos)
│  ── por tema ──
├── design-direction/   paleta 2+1, 60/30/10, camadas, confiança, branding, par tipográfico, workflow com Claude/Claude Design
├── ui-motion/          micro-interações, easing e springs, loaders, transições, scroll, React Bits, motion para redes
├── ux-patterns/        leis de UX, alvos de toque, tipografia, grade de 8, componentes, dark patterns, performance percebida
├── dashboard-ui/       galeria de dashboards, KPIs, gráficos, glassmorphism, gamificação, fintech e apps de score
│  ── investimentos ──
├── quant-investing/    validação de backtest, armadilhas, Deflated Sharpe, baseline, avaliação de fontes, carreira quant
└── ext-*/              skills de terceiros (não versionadas; ver abaixo)
```

**Por qual começar:** primeiro a de plataforma (`website-ui`, `desktop-app-ui` ou `mobile-app-ui`). Ela diz quais arquivos das skills de tema abrir.

Cada skill de tema tem:

- `SKILL.md`: regras centrais e workflow.
- `references/*.md`: o conhecimento detalhado, carregado sob demanda.
- `references/visual-index.md`: tabela que diz o que cada imagem mostra, quando abrir, e os perfis avaliados como fonte.
- `assets/visual-refs/`: folhas de contato 4x3 com frames dos reels (`<id>.jpg`) e prints dos carrosséis (`<id>_<n>.jpg`). O Claude lê as imagens quando precisa de um exemplo visual.

## Skills de terceiros

```bash
./scripts/install-external-skills.sh            # neste projeto (.claude/skills/ext-*)
./scripts/install-external-skills.sh --global   # em ~/.claude/skills
```

Nas sessões do Claude Code na nuvem, a instalação é **automática**: o gatilho `.claude/hooks/session-start.sh` (registrado em `.claude/settings.json`) roda o script ao abrir a sessão se alguma skill `ext-*` estiver faltando, e pula a instalação quando já está tudo instalado. No seu computador, rode o script manualmente.

O script instala: taste-skill, impeccable, gsap-skills (8), playwright-cli, transitions.dev (3) e design-extract. React Bits é uma biblioteca de componentes, não uma skill; o script mostra como usar. As skills de terceiros não são copiadas para esta repo porque algumas licenças (transitions.dev, react-bits) não permitem redistribuição.

## Fontes

Veja [docs/sources.md](docs/sources.md) para o status de cada link e o plano de próximas fontes. Os prompts para coletar as fontes pendentes com a extensão Claude in Chrome estão em [docs/chrome-prompts.md](docs/chrome-prompts.md). As imagens em `visual-refs` são frames de conteúdo de terceiros, para referência pessoal. Mantenha a repo privada.
