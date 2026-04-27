#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROFILE_PREFIX="${1:-gzh}"

(cd "$ROOT_DIR/01-article-strategist" && bash ./install_to_profile.sh "$PROFILE_PREFIX-strategy")
(cd "$ROOT_DIR/02-article-writer" && bash ./install_to_profile.sh "$PROFILE_PREFIX-writer")
(cd "$ROOT_DIR/03-editor" && bash ./install_to_profile.sh "$PROFILE_PREFIX-edit")
(cd "$ROOT_DIR/04-review" && bash ./install_to_profile.sh "$PROFILE_PREFIX-review")
(cd "$ROOT_DIR/99-solution-validator" && bash ./install_to_profile.sh "$PROFILE_PREFIX-validator")

echo "installed team bundle to $PROFILE_PREFIX-strategy / $PROFILE_PREFIX-writer / $PROFILE_PREFIX-edit / $PROFILE_PREFIX-review / $PROFILE_PREFIX-validator"
