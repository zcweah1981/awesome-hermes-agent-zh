import os
import shutil
from pathlib import Path

# 配置映射关系
REPO_ROOT = Path("/opt/projects/awesome-hermes-agent-zh")
DOCS_ROOT = REPO_ROOT / "docs"

def sync_starters():
    """将 starters 下的 README 同步到 docs/starters/"""
    starters_dir = REPO_ROOT / "starters"
    target_docs_dir = DOCS_ROOT / "starters"
    target_docs_dir.mkdir(parents=True, exist_ok=True)

    for item in starters_dir.iterdir():
        if item.is_dir() and (item / "README.md").exists():
            # 生成官网用的文件名，如 single-agent.md
            target_name = f"{item.name}.md"
            shutil.copy(item / "README.md", target_docs_dir / target_name)
            print(f"[Hyoga/Ops] Synced Starter: {item.name} -> {target_name}")

def sync_examples():
    """将 examples 下的说明同步到 docs/examples/"""
    examples_dir = REPO_ROOT / "examples" / "skills"
    target_docs_dir = DOCS_ROOT / "examples"
    target_docs_dir.mkdir(parents=True, exist_ok=True)

    for item in examples_dir.iterdir():
        if item.is_dir() and (item / "README.md").exists():
            target_name = f"{item.name}.md"
            shutil.copy(item / "README.md", target_docs_dir / target_name)
            print(f"[Hyoga/Ops] Synced Example: {item.name} -> {target_name}")

if __name__ == "__main__":
    print("[Hyoga/Ops] Starting Auto-Syncing Content...")
    sync_starters()
    sync_examples()
    print("[Hyoga/Ops] Sync Complete.")
