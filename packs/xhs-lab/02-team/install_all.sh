#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROFILE_PREFIX="${1:-xhs}"

(cd "$ROOT_DIR/01-topic-strategist" && bash ./install_to_profile.sh "$PROFILE_PREFIX-strategy")
(cd "$ROOT_DIR/02-drafter" && bash ./install_to_profile.sh "$PROFILE_PREFIX-draft")
(cd "$ROOT_DIR/03-polisher" && bash ./install_to_profile.sh "$PROFILE_PREFIX-polish")
(cd "$ROOT_DIR/04-review" && bash ./install_to_profile.sh "$PROFILE_PREFIX-review")
(cd "$ROOT_DIR/99-solution-validator" && bash ./install_to_profile.sh "$PROFILE_PREFIX-validator")

echo "installed team bundle to $PROFILE_PREFIX-strategy / $PROFILE_PREFIX-draft / $PROFILE_PREFIX-polish / $PROFILE_PREFIX-review / $PROFILE_PREFIX-validator"
