#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

(cd "$ROOT_DIR/01-product" && bash ./install_to_profile.sh miniapp-product)
(cd "$ROOT_DIR/02-builder" && bash ./install_to_profile.sh miniapp-builder)
(cd "$ROOT_DIR/03-api" && bash ./install_to_profile.sh miniapp-api)
(cd "$ROOT_DIR/04-qa" && bash ./install_to_profile.sh miniapp-qa)
(cd "$ROOT_DIR/99-solution-validator" && bash ./install_to_profile.sh miniapp-validator)

echo "installed team bundle to miniapp-product / miniapp-builder / miniapp-api / miniapp-qa / miniapp-validator"
