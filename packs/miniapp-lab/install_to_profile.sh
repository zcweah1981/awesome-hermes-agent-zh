#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <target-profile-name-or-path>"
  echo "Examples:"
  echo "  $0 miniapp-lab"
  echo "  $0 ~/.hermes/profiles/miniapp-lab"
  exit 1
fi

INPUT="$1"
if [[ "$INPUT" == *"/"* ]]; then
  TARGET="$INPUT"
else
  TARGET="$HOME/.hermes/profiles/$INPUT"
fi

mkdir -p "$TARGET"
mkdir -p "$TARGET/skills/solutions"
cp SOUL.md "$TARGET/SOUL.md"
cp -R skills/solutions/wechat-mini-program-assistant "$TARGET/skills/solutions/"
echo "miniapp-lab installed to $TARGET"
