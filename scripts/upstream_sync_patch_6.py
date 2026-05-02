from pathlib import Path
import re

def update_python():
    py_path = Path("/opt/projects/awesome-hermes-agent-zh/scripts/upstream_sync.py")
    content = py_path.read_text(encoding="utf-8")
    
    # We need to update render_check_markdown and render_issue_body
    if "version_sync" not in content.split("def render_check_markdown")[1]:
        # Add it to the markdown report
        replacement = """
    if "version_sync" in payload:
        vs = payload["version_sync"]
        lines.append(f"- **Baseline Version**: `{vs.get('baseline')}`")
        if vs.get("latest"):
            lines.append(f"- **Latest Upstream**: `{vs.get('latest')}`")
            if vs.get("outdated"):
                lines.append("  - ⚠️ **OUTDATED**: Upstream is newer than baseline.")
        lines.append("")
"""
        content = re.sub(
            r"(\s+lines\.append\(\"- \*\*R2 Provider Sources Confirmed\*\*: \" \+ str\(summary\.get\(\"r2_provider_sources_confirmed\", 0\)\)\)\n\s+lines\.append\(\"\"\))",
            r"\1" + replacement,
            content
        )
        py_path.write_text(content, encoding="utf-8")
        print("Patched render_check_markdown")

update_python()
