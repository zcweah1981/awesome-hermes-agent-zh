#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <target-profile-path>"
  exit 1
fi

TARGET="$1"
mkdir -p "$TARGET"
mkdir -p "$TARGET/skills/solutions"
cp SOUL.md "$TARGET/SOUL.md"
cp -R skills/solutions/wechat-mini-program-assistant "$TARGET/skills/solutions/"
echo "miniapp-lab installed to $TARGET"
