#!/usr/bin/env bash
# Instala as skills de terceiros (lista do Chase AI) em .claude/skills/ deste projeto
# ou em ~/.claude/skills/ com --global. As skills NÃO são versionadas aqui
# (licenças de transitions.dev e react-bits não permitem redistribuição).
set -euo pipefail
DEST="$(cd "$(dirname "$0")/.." && pwd)/.claude/skills"
[ "${1:-}" = "--global" ] && DEST="$HOME/.claude/skills"
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
Use direto do site reactbits.dev ou via CLI, por exemplo:
  npx shadcn@latest add https://reactbits.dev/r/<Componente>-TS-TW
Playwright CLI também precisa do binário:  npm install -g @playwright/cli
MSG
