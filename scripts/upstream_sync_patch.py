import json
import urllib.request
import re
from pathlib import Path
import yaml

# 我们写个独立的小脚本来给 upstream_sync.py 和 yaml 打补丁

def update_yaml():
    yaml_path = Path("/opt/projects/awesome-hermes-agent-zh/governance/upstream-source-registry.yaml")
    content = yaml_path.read_text(encoding="utf-8")
    
    if "hermes_upstream_baseline_version" not in content:
        content = re.sub(
            r"(owner: content-maintainers\n)", 
            r"\1hermes_upstream_baseline_version: \"v1.1.2\"\n", 
            content
        )
        yaml_path.write_text(content, encoding="utf-8")
        print("Updated YAML baseline.")

update_yaml()
