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
cp -R skills/solutions/* "$TARGET/skills/solutions/"
echo "installed to $TARGET"
