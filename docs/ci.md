# 项目 CI 与 PR 契约

> 状态：`初始化中`
>
> Required Check：`CI Gate`
>
> 目标分支：`main`

## 1. 项目环境

- 运行时：Python 3.12
- 包管理器：pip
- 依赖版本文件：`requirements-ci.txt`
- Monorepo：否
- 测试框架：pytest
- 数据库/缓存：不适用
- 浏览器/E2E：不适用
- 外部服务：Required CI 只验证本地仓库；网络巡查和站点 dispatch 使用独立 workflow

## 2. 真实验证命令

| 范围 | 本地与 CI 命令 | Required | 状态 |
|---|---|---:|---|
| 安装 | `python -m pip install -r requirements-ci.txt` | 是 | 已实现 |
| unit/integration test | `python -m pytest -q` | 是 | 本地已验证，远端待验证 |
| route map source | `content-check` 内置校验 | 是 | 已实现 |
| Pack manifest | `content-check` 内置校验 | 是 | 已实现 |
| 外部链接 | Lychee workflow | 否 | 独立检查 |
| production build | 不适用，由代码仓负责 | 否 | 不适用 |

## 3. GitHub Actions

- 工作流：`.github/workflows/content-check.yml`
- 触发：PR 到 `main`、`main` push
- Runner：`ubuntu-latest`
- 测试服务：无
- 缓存：pip cache，以 `requirements-ci.txt` 为键
- 超时：15分钟
- 并发取消：同 ref 取消旧运行
- 权限：`contents: read`
- Secret 使用：Required CI 不使用 Secret
- `CI Gate` 汇总逻辑：单一顺序 job；pytest、route或Pack检查失败即失败

`link-check`、上游巡查、第三方巡查和站点 dispatch 保持独立，不作为稳定 Required Check 的替代品。

## 4. PR 治理

- 所有进入 `main` 的变更通过 PR：已配置 Branch protection
- 人工 GitHub approval：默认不要求
- Reviewer：按 `AGENTS.md` 风险规则
- 合并方式：squash
- Auto-merge：仓库能力已启用；当前初始化 PR 未启用
- 合并后删除分支：已启用，待安全 PR 合并验证
- Force push：已禁止
- 管理员绕过：不得用于绕过失败门禁

## 5. 验证证据

- CI 初始化 PR：待创建
- 成功 run：待验证
- Branch protection：已配置 Required `CI Gate`、PR、线性历史，禁止 force push 和删除
- 自动合并验证：受阻；`docs/**` 合并会触发站点同步与发布，本任务不含生产部署授权
- 本地验证：2026-07-26 已通过 15 项 pytest；workflow YAML 已完成解析校验
- 已知限制：H1、图片格式/冗余资产、来源复核和页尾导航红线尚未全部进入 Required CI

## 6. 故障处理

- CI 失败：先区分内容合同失败、测试失败和外部网络失败
- CI 基础设施损坏：标记受阻，不直接推送 `main`
- GitHub 权限不足：报告缺失权限，不使用管理员绕过
- Required check 卡住：确认 workflow 触发和检查名仍为 `CI Gate`
- 本地/CI 不一致：优先修复路径分隔符、换行和控制台编码差异
