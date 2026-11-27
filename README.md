# Skills de Design, UI/UX e Investimentos para Claude Code

Skills próprias, destiladas de ~70 reels do Instagram (vídeo + frames + transcrição do áudio), de 10 rodadas de coleta com a extensão Claude in Chrome (carrosséis, perfis e vídeos do Facebook, ver `docs/achados/`) e de um curso de 2h no YouTube, mais um instalador para as 7 skills de terceiros recomendadas pelo Chase AI.

## Estrutura

As skills estão em três camadas:

1. **Por tema**: o conhecimento de base, que vale para qualquer plataforma.
2. **Por plataforma**: as regras específicas de cada plataforma, com ponteiros para as skills de tema e para as imagens delas. Essas skills não têm imagens próprias.
3. **Por segmento** (`segmento-*`): o que muda num setor (tom, paleta medida em produtos reais, o que nunca animar, regulação que muda a tela, templates e componentes do setor), com ponteiros para plataforma e tema.

```
.claude/skills/
│  ── por plataforma ──
├── website-ui/         sites, landing pages, portfólio, e-commerce, blog (Major Third 1,25, Core Web Vitals, SEO)
├── desktop-app-ui/     web apps SaaS, admin, CRM e apps Mac/Windows (app shell, densidade 1,2, tabelas, teclado, ⌘K)
├── mobile-app-ui/      apps iOS/Android/React Native/Flutter (44pt/48dp, zona do polegar, tab bar, bottom sheet, gestos)
│  ── por segmento ──
├── segmento-financeiro/     banco digital, fintech, corretora, pagamentos, crédito, investimento (números tabulares, CET, LGPD)
├── segmento-crm/            CRM, pipeline, leads, contas e metas comerciais (denso, cor só para ação e estado)
├── segmento-publicidade/    agência, anunciante, gestor de tráfego, ferramenta de marketing (anúncio identificável, KPI com período)
├── segmento-marca-pessoal/  creator, freelancer, consultor, portfólio, link na bio (personalidade manda, publi identificada)
├── segmento-saude/          clínica, consultório, telemedicina, healthtech, plano de saúde (calmo, legível, dado sensível na LGPD)
├── segmento-juridico/       advocacia, departamento jurídico, legaltech, prazos e contratos (sóbrio, Provimento OAB 205/2021)
│  ── por tema ──
├── design-direction/   paleta 2+1, 60/30/10, camadas, confiança, branding, par tipográfico, workflow com Claude/Claude Design
├── ui-motion/          micro-interações, easing e springs, loaders, transições, scroll, React Bits, motion para redes
├── ux-patterns/        leis de UX, alvos de toque, tipografia, grade de 8, componentes, dark patterns, performance percebida
├── dashboard-ui/       galeria de dashboards, KPIs, gráficos, glassmorphism, gamificação, fintech e apps de score
│  ── investimentos ──
├── quant-investing/    validação de backtest, armadilhas, Deflated Sharpe, baseline, avaliação de fontes, carreira quant
└── ext-*/              skills de terceiros (não versionadas; ver abaixo)
```

**Prioridade (da mais forte para a mais fraca):** skill de app específico (`projetos/<app>/`, copiada para a repo do app) > skill de **segmento** (`segmento-*`) > skill de **plataforma** > skill de **tema** > skills de **terceiros** (`ext-*`). As de terceiros servem para implementação (código, APIs, checkers) e usam os valores das skills do projeto. A de segmento ou de app só sobrepõe o que diz explicitamente; no resto valem plataforma e tema. Os 3 conflitos conhecidos (quantidade de animação, durações, sombras) estão resolvidos na seção "Prioridade entre skills" das skills de plataforma, da `ui-motion` e da `design-direction`.

**Por qual começar:** se o projeto é de um setor, abra primeiro a skill `segmento-*` correspondente; depois a de plataforma (`website-ui`, `desktop-app-ui` ou `mobile-app-ui`). Ela diz quais arquivos das skills de tema abrir.

Cada skill de tema tem:

- `SKILL.md`: regras centrais e workflow.
- `references/*.md`: o conhecimento detalhado, carregado sob demanda.
- `references/visual-index.md`: tabela que diz o que cada imagem mostra, quando abrir, e os perfis avaliados como fonte.
- `assets/visual-refs/`: folhas de contato 4x3 com frames dos reels (`<id>.jpg`) e prints dos carrosséis (`<id>_<n>.jpg`). O Claude lê as imagens quando precisa de um exemplo visual.

## Skills exclusivas de um app

`projetos/<app>/` guarda skills feitas para um app específico. Elas ficam fora de `.claude/skills/` para não carregarem nos outros projetos. Para usar uma delas, copie a pasta para `.claude/skills/` na repo daquele app.

- `projetos/marca-pessoal-app/`: app de gestão de marca pessoal, com as decisões D1–D8, os itens obrigatórios do dia 1 e a síntese da pesquisa em `references/sintese.md`.

## Instalar como plugin (recomendado: atualiza sem copiar pastas)

Esta repo é um **marketplace de plugins** do Claude Code (`design-skills`), com 3 plugins:

| Plugin | O que traz |
|---|---|
| `design-ui` | As 13 skills de design: plataforma, segmento e tema |
| `quant-investing` | Validação de estratégias de investimento |
| `marca-pessoal-app` | Skill exclusiva do app de marca pessoal. Instale só na repo desse app |

**No seu computador (todos os projetos).** No terminal:

```bash
claude plugin marketplace add rgruberb/blank-app
claude plugin install design-ui@design-skills
claude plugin install quant-investing@design-skills
```

Ou, dentro do Claude Code: `/plugin install design-ui --marketplace rgruberb/blank-app` (e o mesmo para `quant-investing`).

**Para atualizar** depois de mudanças no `main`:

```bash
claude plugin marketplace update design-skills
claude plugin update design-ui@design-skills
```

**Em outra repo (vale também para as sessões na nuvem dessa repo).** Acrescente ao `.claude/settings.json` daquela repo (junte com o que já existir):

```json
{
  "extraKnownMarketplaces": {
    "design-skills": { "source": { "source": "github", "repo": "rgruberb/blank-app" } }
  },
  "enabledPlugins": {
    "design-ui@design-skills": true
  }
}
```

Observações:
- **Repo privada:** a instalação precisa de acesso ao GitHub com a sua conta. No computador, isso é o seu login do Git. Numa sessão na nuvem de outra repo, `rgruberb/blank-app` precisa estar acessível para a sessão; se não estiver, a sessão avisa.
- **Dentro desta repo**, não instale o plugin: as skills já carregam pela pasta `.claude/skills/`, e instalar duplicaria os nomes.
- **No chat do claude.ai** (fora do Claude Code), plugins não se aplicam: lá as skills entram por upload de `.zip` em Configurações → Skills.

## Skills de terceiros

```bash
./scripts/install-external-skills.sh            # neste projeto (.claude/skills/ext-*)
./scripts/install-external-skills.sh --global   # em ~/.claude/skills
```

Nas sessões do Claude Code na nuvem, a instalação é **automática**: o gatilho `.claude/hooks/session-start.sh` (registrado em `.claude/settings.json`) roda o script ao abrir a sessão se alguma skill `ext-*` estiver faltando, e pula a instalação quando já está tudo instalado. No seu computador, rode o script manualmente.

O script instala: taste-skill, impeccable, gsap-skills (8), playwright-cli, transitions.dev (3) e design-extract. React Bits é uma biblioteca de componentes, não uma skill; o script mostra como usar. As skills de terceiros não são copiadas para esta repo porque algumas licenças (transitions.dev, react-bits) não permitem redistribuição.

## Fontes

Veja [docs/sources.md](docs/sources.md) para o status de cada link e o plano de próximas fontes. Os prompts para coletar as fontes pendentes com a extensão Claude in Chrome estão em [docs/chrome-prompts.md](docs/chrome-prompts.md). As imagens em `visual-refs` são frames de conteúdo de terceiros, para referência pessoal. Mantenha a repo privada.
