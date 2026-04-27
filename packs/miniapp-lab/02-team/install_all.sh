#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROFILE_PREFIX="${1:-miniapp}"

(cd "$ROOT_DIR/01-product" && bash ./install_to_profile.sh "$PROFILE_PREFIX-product")
(cd "$ROOT_DIR/02-builder" && bash ./install_to_profile.sh "$PROFILE_PREFIX-builder")
(cd "$ROOT_DIR/03-api" && bash ./install_to_profile.sh "$PROFILE_PREFIX-api")
(cd "$ROOT_DIR/04-qa" && bash ./install_to_profile.sh "$PROFILE_PREFIX-qa")
(cd "$ROOT_DIR/99-solution-validator" && bash ./install_to_profile.sh "$PROFILE_PREFIX-validator")

echo "installed team bundle to $PROFILE_PREFIX-product / $PROFILE_PREFIX-builder / $PROFILE_PREFIX-api / $PROFILE_PREFIX-qa / $PROFILE_PREFIX-validator"
