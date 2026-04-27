#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROFILE_PREFIX="${1:-ppt}"

(cd "$ROOT_DIR/01-structure-planner" && bash ./install_to_profile.sh "$PROFILE_PREFIX-structure")
(cd "$ROOT_DIR/02-slide-writer" && bash ./install_to_profile.sh "$PROFILE_PREFIX-slidewriter")
(cd "$ROOT_DIR/03-slide-polisher" && bash ./install_to_profile.sh "$PROFILE_PREFIX-polish")
(cd "$ROOT_DIR/04-review" && bash ./install_to_profile.sh "$PROFILE_PREFIX-review")
(cd "$ROOT_DIR/99-solution-validator" && bash ./install_to_profile.sh "$PROFILE_PREFIX-validator")

echo "installed team bundle to $PROFILE_PREFIX-structure / $PROFILE_PREFIX-slidewriter / $PROFILE_PREFIX-polish / $PROFILE_PREFIX-review / $PROFILE_PREFIX-validator"
