# Hermes Agent 中文站 V2 — 正式页面来源映射

## 目标
定义 V2 六个固定模块在 GitHub 仓库中的正式内容来源，作为后续 RM -> SM 放行与独立站实现的统一映射依据。

| 模块 | 仓库来源文件 | 说明 |
|---|---|---|
| 首页 | `README.md` + `docs/index.md` | GitHub 顶层产品入口与站点首页源头 |
| 从这开始 | `docs/start/index.md` | 四层递进学习路径入口（先跑起来 → 开始上手 → 玩出花样 → 自己造东西） |
| 现成方案 | `docs/solutions/index.md` | 四类现成方案总入口（content / office / management / dev） |
| 国内落地 | `docs/china/index.md` | 国内落地主入口，先做模型、成本、provider、自托管决策，再按需进入 custom OpenAI-Compatible 参考页 |
| 遇到问题 | `docs/issues/index.md` | 问题与排障总入口；`docs/known-issues.md` 降级为过渡参考页 |
| 从 OpenClaw 过来 | `docs/migrate/index.md` | 迁移与兼容主入口；compare / migration / coexist 三页作为正式正文来源 |

## 当前使用规则
1. 每个模块必须能映射到唯一主来源文件。
2. README 负责总入口，不替代各模块正文来源。
3. 若后续补充模块正文来源，必须在本文件追加，不得口头漂移。
4. legacy site 文件不计入正式页面来源映射。
5. 页面层新增样板时，必须同时登记对应实现层映射文件。

## RM3 页面层 + 实现层双映射样板
| 模块 | 页面层文件 | 实现层文件 | 说明 |
|---|---|---|---|
| 现成方案 / content | `docs/solutions/content/content-repurpose-workbench.md` | `docs/solutions/content/agents/content-repurpose-workbench-agents.md` | RM3 首个场景页与对应 agents 映射占位 |
| 现成方案 / office | `docs/solutions/office/mail-docs-workbench.md` | `docs/solutions/office/agents/mail-docs-workbench-agents.md` | RM3 办公流程首个场景页与对应 agents 映射占位 |
| 现成方案 / management | `docs/solutions/management/pm-inspection-workbench.md` | `docs/solutions/management/agents/pm-inspection-workbench-agents.md` | RM3 项目管理首个场景页与对应 agents 映射占位 |
| 现成方案 / dev | `docs/solutions/dev/repo-inspection-workbench.md` | `docs/solutions/dev/agents/repo-inspection-workbench-agents.md` | RM3 开发交付首个场景页与对应 agents 映射占位 |

## 本轮明确不触碰
- `site/`
- `tests/`
- `CHANGELOG.md`
- `vercel.json`
- `DELIVERY_KANBAN.md`

## 当前状态
accepted
