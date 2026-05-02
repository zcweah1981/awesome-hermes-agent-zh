# R3 官方版本周期巡检计划 (Upstream Patrol Plan)

更新时间：2026-05-02

## 目标
建立 Hermes 官方 GitHub Releases 和官方 Docs 的自动化巡检机制。当官方发布新版本或发生破坏性变更时，系统能自动比对我们的“本地基线”，并提报需要同步的中文页面清单。

## 范围
- `governance/upstream-source-registry.yaml`: 引入本地版本基线声明。
- `scripts/upstream_sync.py`: 增加针对官方 GitHub Release 的版本拉取和比对逻辑。
- `.github/workflows/upstream-sync-check.yml`: 将版本比对集成到每周预警 Issue 生成中。
- `governance/upstream-sync-policy.md`: 宣告 R3 巡检机制落地。

## 任务拆分
- **R3-A：基线声明**：在 Registry 中定义 `hermes_upstream_baseline_version`。
- **R3-B：脚本扩展**：扩展 `upstream_sync.py` 支持基于 GitHub API 的版本检查并给出落后警告。
- **R3-C：工作流集成**：在 CI 中消费警告输出并渲染为 Issue。
- **R3-D：政策定稿**：更新治理文档。

## 验收标准
1. 不破坏 R1/R2 已有能力。
2. 脚本无依赖鉴权（或仅依赖 GITHUB_TOKEN）。
3. 模拟版本落后能正确报出警告。
