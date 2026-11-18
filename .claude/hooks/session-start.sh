#!/bin/bash
# Instala as skills de terceiros (.claude/skills/ext-*) quando faltarem.
# Roda só em sessões na nuvem do Claude Code; localmente, use scripts/install-external-skills.sh.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}"

SKILLS_DIR=.claude/skills
EXPECTED="ext-taste-skill ext-impeccable ext-gsap-core ext-gsap-timeline ext-gsap-scrolltrigger ext-gsap-plugins ext-gsap-react ext-gsap-frameworks ext-gsap-utils ext-gsap-performance ext-playwright-cli ext-transitions-dev ext-transitions-polish ext-transitions-ui-generation ext-extract-design"
# O hash fica dentro de uma pasta instalada (ignorada pelo git via .claude/skills/ext-*/)
hashes=$SKILLS_DIR/ext-taste-skill/.session-start.sha256

missing=0
for s in $EXPECTED; do
  [ -f "$SKILLS_DIR/$s/SKILL.md" ] || missing=1
done

if [ "$missing" = 1 ] || ! sha256sum --check --status "$hashes" 2>/dev/null; then
  rm -f "$hashes"
  echo "Instalando skills de terceiros..." >&2
  ./scripts/install-external-skills.sh >&2
  sha256sum .claude/hooks/session-start.sh scripts/install-external-skills.sh > "$hashes"
fi
