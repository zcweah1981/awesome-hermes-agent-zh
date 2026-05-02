from pathlib import Path
import re

def update_python():
    py_path = Path("/opt/projects/awesome-hermes-agent-zh/scripts/upstream_sync.py")
    content = py_path.read_text(encoding="utf-8")
    
    # Let's insert the version check inside `validate()`
    if "baseline_ver =" not in content:
        # locate the start of the return dict in validate
        validate_match = re.search(r"(\s+payload = \{\n\s+\"status\": status,)", content)
        if not validate_match:
            validate_match = re.search(r"(\s+return \{\n\s+\"status\": status,)", content)
            
        if validate_match:
            replacement = """
    baseline_ver = config.get('hermes_upstream_baseline_version', 'unknown')
    latest_ver = fetch_latest_github_release() if not options.no_network else None
    
    version_info = {'baseline': baseline_ver, 'latest': latest_ver}
    if latest_ver and baseline_ver and latest_ver != baseline_ver:
        version_info['outdated'] = True
        issues.append(f"Official upstream release is at {latest_ver}, but baseline is {baseline_ver}")
        status = "issues_found"
    """ + validate_match.group(1).replace("return {", "payload = {").replace("\"status\": status,", "\"status\": status,\n        \"version_sync\": version_info,")
            
            content = content.replace(validate_match.group(1), replacement)
            
            # replace return payload or dict with return payload
            content = re.sub(
                r"(\s+\"reachability\": reachability_results\n\s+\})",
                r"\1\n    return payload",
                content
            )
            
            py_path.write_text(content, encoding="utf-8")
            print("Successfully patched upstream_sync.py validate()")
        else:
            print("Could not match return payload in validate()")

update_python()
