# 项目 CI 与 PR 契约

> CI 状态：`初始化中`
>
> 合并治理模式：`platform-enforced`
>
> CI 汇总检查：`CI Gate`
>
> 目标分支：`main`

## 1. GitHub 能力检测

- 仓库：`zcweah1981/awesome-hermes-agent-zh`
- 所有者类型：个人
- 可见性：Public
- GitHub 计划：无法确认；公开仓当前能力足够
- Branch Protection / Ruleset：可用，`main` 已配置
- Required Status Checks：可用，Required `CI Gate` 已配置
- GitHub 原生 Auto-merge：可用；仓库元数据 `allow_auto_merge=true`
- 最终治理模式：`platform-enforced`
- 选择依据：公开仓支持 PR、Required Check、分支保护与原生 Auto-merge，可以由 GitHub 平台强制执行。

## 2. 项目环境

- 运行时：Python 3.12
- 包管理器：pip
- 锁文件：CI 依赖固定在 `requirements-ci.txt`
- Monorepo：否
- 测试框架：pytest
- 数据库/缓存：不适用
- 浏览器/E2E：不适用
- 外部服务：Required CI 不访问生产平台；`link-check` 只读公开链接

## 3. 真实验证命令

| 范围 | 本地与 CI 命令 | 是否纳入 CI Gate | 状态 |
|---|---|---:|---|
| 安装/依赖 | `python -m pip install -r requirements-ci.txt` | 是 | 已实现 |
| lint | 无独立 lint；内容结构由 pytest 和质量脚本校验 | 否 | 不适用 |
| typecheck | 无 Python 类型检查基线 | 否 | 未纳入 |
| unit/integration test | `python -m pytest -q` | 是 | 已实现 |
| route/order | `python scripts/normalize_route_order.py` | 是 | 已实现 |
| 内容质量 | `python scripts/content_quality_check.py` | 是 | 已实现 |
| production build | 不适用；由站点代码仓负责 | 否 | 不适用 |
| database migration | 不适用 | 否 | 不适用 |
| E2E/关键路径 | 不适用 | 否 | 不适用 |
| 外链检查 | `.github/workflows/link-check.yml` | 否，独立检查 | 已实现 |

不存在的能力不使用 `echo success`、空测试、无断言测试或无条件 `--if-present` 伪造通过。

## 4. GitHub Actions

- 工作流：`.github/workflows/content-check.yml`；独立 `.github/workflows/link-check.yml`
- 触发：`pull_request` 到 `main`、`push main`；link-check 另有 schedule 和手动触发
- Runner：标准 `ubuntu-latest`
- 测试服务：无
- 缓存：`actions/setup-python` 的 pip cache
- 超时：`content-check` 15 分钟；link-check 使用 Action 默认 job 上限
- 并发取消：同一 ref 取消旧运行
- 权限：`content-check` 与 link-check 均仅 `contents: read`；失败报告只写 Actions Summary 和 Artifact，不自动创建 Issue
- Secret 使用：Required `CI Gate` 不使用生产 Secret
- `CI Gate` 汇总逻辑：单一顺序 job；pytest、route/order、质量或 Pack/关键路径检查失败即失败
- 是否使用付费 runner：否
- Actions 用量与预算提醒：公开仓使用标准 GitHub-hosted runner；维持并发取消，不启用付费 larger runner

## 5. PR 治理

### 通用要求

- 所有进入 `main` 的变更使用任务分支和 PR：是
- 独立 Reviewer：按 `AGENTS.md` 风险规则
- 合并方式：`squash`
- 合并后删除远程分支：仓库设置已启用
- 删除本地任务分支：确认 PR 已 `MERGED` 后执行
- 禁止直接推送 `main`：由 Branch Protection 强制
- 禁止 `--admin` 绕过：是

### `platform-enforced`

- Required `CI Gate`：已配置
- Branch Protection / Ruleset：要求 PR、严格 Required `CI Gate`、线性历史和解决讨论
- GitHub 原生 Auto-merge：已启用；仅在获得生产发布授权后对发布 PR 使用
- Force push：禁止
- 删除 `main`：禁止

### `agent-gated`

- Agent 合并脚本：不适用
- 检查是否要求 `CI Gate` 存在：由平台 Required Check 强制
- 是否等待全部 CI：由平台原生 Auto-merge 等待
- 是否核对 head SHA：由 GitHub PR 与 Required Check 绑定提交
- 是否使用 `--match-head-commit`：不适用
- 原生 Auto-merge：使用
- 平台 Branch Protection：可用

## 6. 验证证据

- CI 初始化 PR：[#104](https://github.com/zcweah1981/awesome-hermes-agent-zh/pull/104)
- 成功 Actions run：[content-check #197](https://github.com/zcweah1981/awesome-hermes-agent-zh/actions/runs/30210709998)
- `CI Gate`：提交 `a5e5aafecb437caa4997acf8b4525e7ead2ca699` 已成功
- 合并治理模式：`platform-enforced`
- 合并验证 PR：未执行；合并内容仓 `main` 会触发站点内容同步和双生产发布链，当前请求不包含生产发布授权
- 合并提交：未产生
- 分支清理：未执行，PR #104 保持 open
- 已知平台限制：无 CI 平台能力限制；当前只缺少生产授权边界内的自动合并与清理实证

## 7. 状态判定

当前为 `初始化中`：CI、Required `CI Gate`、Branch Protection 与原生 Auto-merge 能力均已建立；尚未在不越过生产授权边界的前提下完成自动合并和分支清理闭环。

满足以下条件后改为 `就绪（platform-enforced）`：

- 待合并 head SHA 的 Required `CI Gate` 成功；
- 获得生产发布授权后，原生 Auto-merge 完成 squash merge；
- PR 状态、合并提交和远程/本地分支清理均经核对。

## 8. 故障处理

- CI 失败：读取具体步骤日志，修复后推送同一任务分支
- CI 基础设施损坏：保持 PR open，不直接推送 `main`
- GitHub 权限不足：报告缺失权限，不使用管理员绕过
- 平台功能受计划限制：重新检测并按需切换 `agent-gated`
- `CI Gate` 未出现：确认 workflow 触发、目标分支和检查名仍为 `CI Gate`
- PR head SHA 变化：等待新提交对应的全部 Required Checks
- 本地/CI 不一致：优先修复路径、换行、编码和 Python 版本差异
