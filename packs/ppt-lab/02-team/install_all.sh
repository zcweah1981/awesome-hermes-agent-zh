#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

(cd "$ROOT_DIR/01-structure-planner" && bash ./install_to_profile.sh ppt-structure)
(cd "$ROOT_DIR/02-slide-writer" && bash ./install_to_profile.sh ppt-slidewriter)
(cd "$ROOT_DIR/03-slide-polisher" && bash ./install_to_profile.sh ppt-polish)
(cd "$ROOT_DIR/04-review" && bash ./install_to_profile.sh ppt-review)
(cd "$ROOT_DIR/99-solution-validator" && bash ./install_to_profile.sh ppt-validator)

echo "installed team bundle to ppt-structure / ppt-slidewriter / ppt-polish / ppt-review / ppt-validator"