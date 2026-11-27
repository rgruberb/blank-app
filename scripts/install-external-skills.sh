#!/usr/bin/env bash
# Instala as skills de terceiros (lista do Chase AI). Opções: --global, --extras, --extras-all (ver o fim do arquivo) em .claude/skills/ deste projeto
# ou em ~/.claude/skills/ com --global. As skills NÃO são versionadas aqui
# (licenças de transitions.dev e react-bits não permitem redistribuição).
set -euo pipefail
DEST="$(cd "$(dirname "$0")/.." && pwd)/.claude/skills"
GLOBAL=0; EXTRAS=0; EXTRAS_ALL=0
for a in "$@"; do
  case "$a" in
    --global) GLOBAL=1 ;;
    --extras) EXTRAS=1 ;;
    --extras-all) EXTRAS=1; EXTRAS_ALL=1 ;;
  esac
done
[ "$GLOBAL" = 1 ] && DEST="$HOME/.claude/skills"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
mkdir -p "$DEST"

# repo | subpasta(s) com SKILL.md
SKILLS=(
  "Leonxlnx/taste-skill|skills/taste-skill"
  "pbakaus/impeccable|.claude/skills/impeccable"
  "greensock/gsap-skills|skills/gsap-core skills/gsap-timeline skills/gsap-scrolltrigger skills/gsap-plugins skills/gsap-react skills/gsap-frameworks skills/gsap-utils skills/gsap-performance"
  "microsoft/playwright-cli|skills/playwright-cli"
  "Jakubantalik/transitions.dev|skills/transitions-dev skills/transitions-polish skills/transitions-ui-generation"
  "Manavarya09/design-extract|skills/extract-design"
)

for entry in "${SKILLS[@]}"; do
  repo="${entry%%|*}"; paths="${entry#*|}"
  echo "→ $repo"
  git clone -q --depth 1 "https://github.com/$repo" "$TMP/$repo"
  for p in $paths; do
    name="$(basename "$p")"
    rm -rf "${DEST:?}/ext-$name"
    cp -R "$TMP/$repo/$p" "$DEST/ext-$name"
    echo "   instalada: ext-$name"
  done
done

cat <<'MSG'

React Bits (DavidHDev/react-bits) não é uma skill, é uma biblioteca de componentes.
Instale componente por componente (guia: .claude/skills/ui-motion/references/react-bits.md):
  npx shadcn@latest add @react-bits/<Componente>-TS-TW
  npx jsrepo@latest add https://reactbits.dev/r/<Componente>-TS-TW
Playwright CLI também precisa do binário:  npm install -g @playwright/cli
MSG

# ---------------------------------------------------------------------------
# Extras opcionais: plugins citados nos posts do @gut1n (rodada 10A).
# São instalados como PLUGINS do Claude Code (escopo do usuário), não como pastas ext-*.
#   --extras      instala 5 plugins leves + só as 2 skills de acessibilidade do ECC (como pastas ext-ecc-*)
#   --extras-all  também instala o claude-mem (hooks + processo em segundo plano)
# O ECC inteiro (~1.089 skills) NÃO é instalado: as skills de motion dele repetem o ui-motion com outros números.
# Não são usados para criar as skills deste repositório.
# ---------------------------------------------------------------------------
if [ "$EXTRAS" = 1 ]; then
  if ! command -v claude >/dev/null 2>&1; then
    echo "Extras: o CLI 'claude' não foi encontrado. Instale o Claude Code e rode de novo." >&2
    exit 1
  fi
  # repo | plugin@marketplace | licença
  EXTRA_PLUGINS=(
    "cathrynlavery/diagram-design|diagram-design@diagram-design|MIT"
    "multica-ai/andrej-karpathy-skills|andrej-karpathy-skills@karpathy-skills|licença não exibida no repositório"
    "hugohe3/ppt-master|ppt-master@ppt-master|MIT"
    "mattpocock/skills|mattpocock-skills@mattpocock|MIT"
    "expo/skills|expo@expo-plugins|MIT"
  )
  if [ "$EXTRAS_ALL" = 1 ]; then
    EXTRA_PLUGINS+=(
      "thedotmack/claude-mem|claude-mem@thedotmack|Apache-2.0 — ATENÇÃO: instala hooks e um processo em segundo plano (memória entre sessões)"
    )
  fi
  for e in "${EXTRA_PLUGINS[@]}"; do
    IFS='|' read -r repo plugin lic <<< "$e"
    echo "→ extra: $repo ($lic)"
    claude plugin marketplace add "$repo" >/dev/null || { echo "   falhou ao adicionar o marketplace $repo" >&2; continue; }
    claude plugin install "$plugin" || echo "   falhou ao instalar $plugin" >&2
  done
  # ECC: só as skills de acessibilidade (MIT), copiadas como pastas.
  echo "→ extra: affaan-m/ECC (só accessibility e frontend-a11y; MIT)"
  if git clone -q --depth 1 https://github.com/affaan-m/ECC "$TMP/ecc"; then
    for sk in accessibility frontend-a11y; do
      rm -rf "${DEST:?}/ext-ecc-$sk"
      cp -R "$TMP/ecc/skills/$sk" "$DEST/ext-ecc-$sk"
      echo "   instalada: ext-ecc-$sk"
    done
  else
    echo "   falhou ao clonar o ECC" >&2
  fi
  echo "Extras: plugins instalados no usuário (remova com: claude plugin uninstall <plugin>); skills ECC em $DEST."
fi
