#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

(cd "$ROOT_DIR/01-product" && bash ./install_to_profile.sh webdev-product)
(cd "$ROOT_DIR/02-builder" && bash ./install_to_profile.sh webdev-builder)
(cd "$ROOT_DIR/03-api" && bash ./install_to_profile.sh webdev-api)
(cd "$ROOT_DIR/04-qa" && bash ./install_to_profile.sh webdev-qa)
(cd "$ROOT_DIR/99-solution-validator" && bash ./install_to_profile.sh webdev-validator)

echo "installed team bundle to webdev-product / webdev-builder / webdev-api / webdev-qa / webdev-validator"
