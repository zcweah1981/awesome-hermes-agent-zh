#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

(cd "$ROOT_DIR/01-topic-strategist" && bash ./install_to_profile.sh xhs-strategy)
(cd "$ROOT_DIR/02-drafter" && bash ./install_to_profile.sh xhs-draft)
(cd "$ROOT_DIR/03-polisher" && bash ./install_to_profile.sh xhs-polish)
(cd "$ROOT_DIR/04-review" && bash ./install_to_profile.sh xhs-review)
(cd "$ROOT_DIR/99-solution-validator" && bash ./install_to_profile.sh xhs-validator)

echo "installed team bundle to xhs-strategy / xhs-draft / xhs-polish / xhs-review / xhs-validator"