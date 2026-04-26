#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

(cd "$ROOT_DIR/01-article-strategist" && bash ./install_to_profile.sh gzh-strategy)
(cd "$ROOT_DIR/02-article-writer" && bash ./install_to_profile.sh gzh-writer)
(cd "$ROOT_DIR/03-editor" && bash ./install_to_profile.sh gzh-edit)
(cd "$ROOT_DIR/04-review" && bash ./install_to_profile.sh gzh-review)
(cd "$ROOT_DIR/99-solution-validator" && bash ./install_to_profile.sh gzh-validator)

echo "installed team bundle to gzh-strategy / gzh-writer / gzh-edit / gzh-review / gzh-validator"