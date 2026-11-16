# Skills de Design, UI/UX e Investimentos para Claude Code

Skills próprias, destiladas de ~60 reels do Instagram (vídeo + frames + transcrição do áudio), mais um instalador para as 7 skills de terceiros recomendadas pelo Chase AI.

## Estrutura

```
.claude/skills/
├── design-direction/   paletas (2 cores + 1 acento), camadas, layout de confiança, workflow de web design com Claude
├── ui-motion/          micro-interações, easing, durações, loaders, transições de página
├── ux-patterns/        leis de UX, botões, settings, paginação, chat, ⌘K, dark patterns, performance percebida
├── dashboard-ui/       galeria de dashboards e glassmorphism
├── quant-investing/    validação de backtest (Monte Carlo, walk-forward), falácia da taxa de acerto, carreira quant
└── ext-*/              skills de terceiros (não versionadas; ver abaixo)
```

Cada skill própria tem:

- `SKILL.md`: regras centrais e workflow.
- `references/*.md`: o conhecimento detalhado, carregado sob demanda.
- `references/visual-index.md`: tabela que diz o que cada imagem mostra e quando abrir.
- `assets/visual-refs/<id>.jpg`: folha de contato 4x3 com frames do reel original. O Claude lê as imagens quando precisa de um exemplo visual.

## Skills de terceiros

```bash
./scripts/install-external-skills.sh            # neste projeto (.claude/skills/ext-*)
./scripts/install-external-skills.sh --global   # em ~/.claude/skills
```

Nas sessões do Claude Code na nuvem, a instalação é **automática**: o gatilho `.claude/hooks/session-start.sh` (registrado em `.claude/settings.json`) roda o script ao abrir a sessão se alguma skill `ext-*` estiver faltando, e pula a instalação quando já está tudo instalado. No seu computador, rode o script manualmente.

O script instala: taste-skill, impeccable, gsap-skills (8), playwright-cli, transitions.dev (3) e design-extract. React Bits é uma biblioteca de componentes, não uma skill; o script mostra como usar. As skills de terceiros não são copiadas para esta repo porque algumas licenças (transitions.dev, react-bits) não permitem redistribuição.

## Fontes

Veja [docs/sources.md](docs/sources.md) para o status de cada link e o plano de próximas fontes. Os prompts para coletar as fontes pendentes com a extensão Claude in Chrome estão em [docs/chrome-prompts.md](docs/chrome-prompts.md). As imagens em `visual-refs` são frames de conteúdo de terceiros, para referência pessoal. Mantenha a repo privada.
