from pathlib import Path
import re

def update_python():
    py_path = Path("/opt/projects/awesome-hermes-agent-zh/scripts/upstream_sync.py")
    content = py_path.read_text(encoding="utf-8")
    
    # We found `payload = {` at line 196
    
    if "baseline_ver" not in content:
        insert_code = """
    baseline_ver = config.get('hermes_upstream_baseline_version', 'unknown')
    latest_ver = fetch_latest_github_release() if not options.no_network else None
    
    version_info = {'baseline': baseline_ver, 'latest': latest_ver}
    if latest_ver and baseline_ver and latest_ver != baseline_ver:
        version_info['outdated'] = True
        issues.append(f"Official upstream release is at {latest_ver}, but baseline is {baseline_ver}")
        
"""
        # Right before `payload = {` we need to insert the config block check and fetch_latest
        content = re.sub(
            r"(\s+payload = \{\n)",
            insert_code + r"\1",
            content
        )
        
        # Now add version_sync to the payload dict
        content = re.sub(
            r"(\s+\"summary\": \{\n)",
            r"        \"version_sync\": version_info,\n\1",
            content
        )
        
        py_path.write_text(content, encoding="utf-8")
        print("Patched payload definition.")

update_python()
