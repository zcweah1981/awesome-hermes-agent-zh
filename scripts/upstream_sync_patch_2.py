from pathlib import Path
import re

def update_python():
    py_path = Path("/opt/projects/awesome-hermes-agent-zh/scripts/upstream_sync.py")
    content = py_path.read_text(encoding="utf-8")
    
    if "def fetch_latest_github_release" not in content:
        fetch_func = """
def fetch_latest_github_release(repo: str = "NousResearch/hermes-agent") -> str | None:
    try:
        req = Request(
            f"https://api.github.com/repos/{repo}/releases/latest",
            headers={"User-Agent": "hermes-zh-upstream-sync", "Accept": "application/vnd.github.v3+json"}
        )
        with urlopen(req, timeout=5) as res:
            data = json.loads(res.read().decode("utf-8"))
            return data.get("tag_name")
    except Exception as e:
        return None
"""
        content = re.sub(
            r"def repo_relative\(path: Path\) -> str:", 
            fetch_func + "\ndef repo_relative(path: Path) -> str:", 
            content
        )
        
        # Add to output payload in do_check
        content = re.sub(
            r"(results = \[\])",
            r"baseline_ver = config.get('hermes_upstream_baseline_version', 'unknown')\n    latest_ver = fetch_latest_github_release() if not options.no_network else None\n    \n    version_info = {'baseline': baseline_ver, 'latest': latest_ver}\n    if latest_ver and baseline_ver and latest_ver != baseline_ver:\n        version_info['outdated'] = True\n    \n    \1",
            content
        )
        
        content = re.sub(
            r"return \{\n\s+\"status\": \"ok\",",
            r"return {\n        \"status\": \"ok\",\n        \"version_sync\": version_info,",
            content
        )
        
        content = re.sub(
            r"print\(json\.dumps\(\{\"status\": \"ok\"\}, indent=2\)\)",
            r"print(json.dumps(payload, indent=2))",
            content
        )
        
        py_path.write_text(content, encoding="utf-8")
        print("Updated upstream_sync.py")

update_python()
