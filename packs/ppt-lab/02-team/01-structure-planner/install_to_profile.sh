#!/usr/bin/env bash
set -euo pipefail
if [ $# -lt 1 ]; then
  echo "Usage: $0 <target-profile-name-or-path>"
  exit 1
fi
TARGET_INPUT="$1"
if [[ "$TARGET_INPUT" == */* ]]; then
  TARGET="$TARGET_INPUT"
else
  TARGET="$HOME/.hermes/profiles/$TARGET_INPUT"
fi
mkdir -p "$TARGET"
mkdir -p "$TARGET/skills/solutions"
cp SOUL.md "$TARGET/SOUL.md"
while IFS= read -r -d "" skill_dir; do
  cp -R "$skill_dir" "$TARGET/skills/solutions/"
done < <(find skills/solutions -mindepth 1 -maxdepth 1 -type d -exec test -f "{}/SKILL.md" \; -print0)
echo "installed to $TARGET"
