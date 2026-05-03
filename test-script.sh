          ISSUE_DATE="$(date -u +%F)"
          # Get title from python script output or set default
          if [ -f /opt/projects/awesome-hermes-agent-zh/upstream-issue.json ]; then
            TITLE="$(jq -r '.title' /opt/projects/awesome-hermes-agent-zh/upstream-issue.json)"
            # Update title based on whether check has outdated warning
            if grep -q "Official upstream release is at" /opt/projects/awesome-hermes-agent-zh/upstream-check.md; then
              TITLE="【版本落后预警】${TITLE}"
            fi
          else
            TITLE="R1 官方来源同步：${ISSUE_DATE} upstream 检查"
          fi
          echo $TITLE
