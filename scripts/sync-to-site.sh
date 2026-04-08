#!/bin/bash
# Sync script to populate site content from repository docs

REPO_ROOT="/opt/projects/awesome-hermes-agent-zh"
DOCS_DIR="$REPO_ROOT/docs"
# Assuming site content lives in a sibling or specific directory, 
# for now we'll just simulate the sync logic or target a build dir.
TARGET_DIR="$REPO_ROOT/dist"

echo "Starting sync from $DOCS_DIR to $TARGET_DIR..."

mkdir -p "$TARGET_DIR"

# Simple rsync or cp logic for SSoT
cp -R "$DOCS_DIR"/* "$TARGET_DIR/"

echo "Sync completed."
