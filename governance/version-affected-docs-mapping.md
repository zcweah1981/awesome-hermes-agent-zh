# 版本变化 → 中文站页面 影响映射规则

| 字段 | 值 |
|------|------|
| project_id | hermes-zh |
| task_id | hermes-zh:UPSTREAM-VERSION-LEDGER-SYNC-20260519-T3-CONTENT-AFFECTED-DOCS-MAPPING |
| created_at | 2026-05-19 |
| owner | ikki-content-1 |
| status | draft → review |
| source_files | version-ledger.yaml, site-route-map.yaml, upstream-source-registry.yaml |

---

## 1. 映射规则总览

### 1.1 设计原则

1. **版本变化域（domain） → 优先级层（tier） → 受影响文档列表**：三层映射，逐层收敛
2. **元标签（breaking_change / deprecation / new_feature / bug_fix）不独立成层**，而是叠加在域标签上升级优先级
3. **所有映射已与 site-route-map.yaml 交叉校验**：29 个已分层文档全部有对应路由
4. **未分层文档已分类处理**：43 个文档页分为 exempt / provider_driven / recommend_tier 三类

### 1.2 域 → 层映射

| 变化域 (change_category) | 优先级 | SLA | 影响范围 |
|---|---|---|---|
| `install` | **P0** | 48h | 安装相关全部页面 |
| `cli` | **P0** | 48h | CLI 命令、环境变量、安装页 |
| `configuration` | **P0** | 48h | 配置相关全部页面 |
| `provider` | **P1** | 1 周 | Provider / 自定义模型页 |
| `gateway` | **P1** | 1 周 | Gateway / 消息推送页 |
| `tools` | **P1** | 1 周 | Tools / Toolsets 参考页 |
| `skills` | **P1** | 1 周 | Skills 相关页 |
| `mcp` | **P1** | 1 周 | MCP 配置与集成页 |
| `memory` | **P2** | 2 周 | 记忆系统相关页 |
| `troubleshooting` | **P2** | 2 周 | FAQ / 问题排查页 |
| `profiles` | **P2** | 2 周 | Profile 相关页 |
| `automation` | **P2** | 2 周 | 自动化 / cron 相关页 |
| `api_server` | **P2** | 2 周 | API 服务相关页 |
| `breaking_change` | **+1 升级** | 继承升级后层级 | 叠加在域标签上 |
| `deprecation` | **+1 升级** | 继承升级后层级 | 叠加在域标签上 |
| `new_feature` | **按域** | 继承域层级 | 不升级 |
| `bug_fix` | **按域** | 继承域层级 | 不升级 |

### 1.3 元标签优先级升级规则

- **breaking_change**：域 P1 → 升级到 P0，域 P2 → 升级到 P1
- **deprecation**：域 P2 → 升级到 P1
- **new_feature / bug_fix**：不升级，保持原域层级
- 同一版本变更可携带多个域标签

---

## 2. P0 — 必同步（阻塞安装/运行）

**触发条件**：install / cli / configuration 域发生变更
**SLA**：检测到变更后 **48 小时内**完成内容仓同步

| # | 内容仓路径 | 站点 slug | 页面标题 | 触发域 |
|---|---|---|---|---|
| P0-1 | `docs/01-从这开始/01-先跑起来/02-先准备运行环境.md` | `/start/get-running/prepare-environment` | 🧱 02-先准备运行环境 | install, configuration |
| P0-2 | `docs/01-从这开始/01-先跑起来/04-把 Hermes 装上去.md` | `/start/get-running/install-hermes` | 📦 04-把 Hermes 装上去 | install |
| P0-3 | `docs/01-从这开始/01-先跑起来/05-配好 AI 大模型并完成第一次互动.md` | `/start/get-running/first-hello` | 💬 05-配好 AI 大模型并完成第一次互动 | install, configuration |
| P0-4 | `docs/06-reference/02-CLI 命令参考.md` | `/reference/cli-commands` | ⌨️ 02-CLI 命令参考 | cli |
| P0-5 | `docs/06-reference/05-环境变量参考.md` | `/reference/environment-variables` | ⚙️ 05-环境变量参考 | configuration |
| P0-6 | `docs/05-遇到问题/02-安装更新与环境问题.md` | `/issues/install-environment` | 02-安装/更新/环境问题 | install, troubleshooting |

---

## 3. P1 — 评估同步（核心功能体验受损）

**触发条件**：provider / gateway / tools / skills / mcp 域发生变更
**SLA**：检测到变更后 **1 周内**完成内容仓同步

| # | 内容仓路径 | 站点 slug | 页面标题 | 触发域 |
|---|---|---|---|---|
| P1-1 | `docs/01-从这开始/03-玩出花样/04-自定义 AI 大模型.md` | `/start/personalize/custom-model` | 🤖 04-自定义 AI 大模型 | provider |
| P1-2 | `docs/01-从这开始/03-玩出花样/05-让工具更顺手.md` | `/start/personalize/toolsets-and-workflow` | 🧩 05-让工具更顺手 | tools |
| P1-3 | `docs/01-从这开始/02-开始上手/04-常用 Skills（按日常使用场景精选）.md` | `/start/getting-started/curated-skills` | 🏷️ 04-常用 Skills | skills |
| P1-4 | `docs/01-从这开始/04-自己造东西/05-把 Hermes 接进外部系统.md` | `/start/build/mcp-and-plugins` | 🔌 05-把 Hermes 接进外部系统 | mcp |
| P1-5 | `docs/06-reference/06-Built-in Tools 参考.md` | `/reference/built-in-tools` | 🧰 06-Built-in Tools 参考 | tools |
| P1-6 | `docs/06-reference/07-Toolsets 参考.md` | `/reference/toolsets` | 🗂️ 07-Toolsets 参考 | tools |
| P1-7 | `docs/06-reference/08-MCP 配置参考.md` | `/reference/mcp-config` | 🔌 08-MCP 配置参考 | mcp |
| P1-8 | `docs/06-reference/09-内置 Skills 目录.md` | `/reference/bundled-skills` | 🧠 09-内置 Skills 目录 | skills |
| P1-9 | `docs/06-reference/10-可选 Skills 目录.md` | `/reference/optional-skills` | 🧩 10-可选 Skills 目录 | skills |
| P1-10 | `docs/05-遇到问题/03-模型 Provider 与自定义 endpoint 问题.md` | `/issues/provider-endpoint` | 03-模型/Provider/自定义 endpoint 问题 | provider |
| P1-11 | `docs/05-遇到问题/05-Gateway Messaging 与推送问题.md` | `/issues/gateway-messaging` | 05-Gateway/Messaging/推送问题 | gateway |
| P1-12 | `docs/05-遇到问题/06-Tools Skills MCP 问题.md` | `/issues/tools-skills-mcp` | 06-Tools/Skills/MCP 问题 | tools, skills, mcp |

---

## 4. P2 — 记录不改正文（周边体验）

**触发条件**：memory / troubleshooting / profiles / automation / api_server 域发生变更
**SLA**：检测到变更后 **2 周内**完成内容仓同步

| # | 内容仓路径 | 站点 slug | 页面标题 | 触发域 |
|---|---|---|---|---|
| P2-1 | `docs/01-从这开始/03-玩出花样/03-让 Hermes 记住你.md` | `/start/personalize/memory-basics` | 🧠 03-让 Hermes 记住你 | memory |
| P2-2 | `docs/01-从这开始/04-自己造东西/03-接入外部记忆系统/02-Holographic记忆.md` | `/start/build/memory-providers/holographic` | 🪞 02-Holographic记忆 | memory |
| P2-3 | `docs/01-从这开始/04-自己造东西/03-接入外部记忆系统/03-Honcho记忆.md` | `/start/build/memory-providers/honcho` | 🧠 03-Honcho记忆 | memory |
| P2-4 | `docs/01-从这开始/04-自己造东西/03-接入外部记忆系统/04-外部记忆对比.md` | `/start/build/memory-providers/compare` | ⚖️ 04-外部记忆对比 | memory |
| P2-5 | `docs/01-从这开始/04-自己造东西/04-上下文系统/02-上下文文件.md` | `/start/build/context-system/context-files` | 📄 02-上下文文件 | configuration |
| P2-6 | `docs/01-从这开始/04-自己造东西/04-上下文系统/03-上下文引用.md` | `/start/build/context-system/context-references` | 🔗 03-上下文引用 | configuration |
| P2-7 | `docs/01-从这开始/04-自己造东西/06-把 Hermes 暴露成后端服务.md` | `/start/build/api-server` | 🌐 06-把 Hermes 暴露成后端服务 | api_server |
| P2-8 | `docs/01-从这开始/04-自己造东西/07-让 Hermes 自己自动跑.md` | `/start/build/automation` | 🤖 07-让 Hermes 自己自动跑 | automation |
| P2-9 | `docs/06-reference/04-Profile 命令参考.md` | `/reference/profile-commands` | 👤 04-Profile 命令参考 | profiles |
| P2-10 | `docs/05-遇到问题/04-CLI TUI 与会话问题.md` | `/issues/cli-tui-session` | 04-CLI/TUI/会话问题 | troubleshooting |
| P2-11 | `docs/05-遇到问题/07-配置 Profiles 与环境隔离问题.md` | `/issues/config-profiles-environment` | 07-配置/Profiles/环境隔离问题 | profiles, troubleshooting |

---

## 5. 未分层文档处理规则

### 5.1 豁免（exempt）— 不受上游版本影响

**规则**：这些页面为本地原创内容或迁移指南，与上游版本变更无关，无需纳入版本同步链路。

| 分类 | 页面数 | 处理 |
|---|---|---|
| 现成方案 (solutions) | 12 | 不纳入版本同步，按本地节奏维护 |
| OpenClaw 迁移 (openclaw) | 5 | 不纳入版本同步，按本地节奏维护 |

### 5.2 Provider 驱动（provider_driven）— 按 provider_source 独立同步

**规则**：这些页面按 `upstream-source-registry.yaml` 中 provider_sources 条目独立同步，不走版本台账链路。

| 分类 | 页面数 | 同步触发 |
|---|---|---|
| 国内部署 (china/deploy) | 2 | 阿里云/腾讯云文档变更时 |
| 国内模型 (china/models) | 7 | 对应 provider 文档/定价变更时 |
| 国内入口 (china/entry) | 7 | provider 变更 + gateway 变更双重触发 |

> **china/entry 特殊规则**：gateway 域变更时需额外检查国内入口页是否受影响。

### 5.3 建议补充分层（recommend_tier）— 应纳入 version-ledger 但当前遗漏

**规则**：以下 10 个页面与上游行为强相关，建议 PM 评估后补充进入 version-ledger 对应 tier。

| # | 内容仓路径 | 站点 slug | 建议分层 | 理由 |
|---|---|---|---|---|
| G-1 | `docs/01-从这开始/02-开始上手/02-认识 Hermes 的基本使用方式.md` | `/start/getting-started/basic-usage` | P0 | CLI 基本操作，cli 变更直接影响 |
| G-2 | `docs/01-从这开始/02-开始上手/03-常用斜杠命令与会话管理.md` | `/start/getting-started/slash-commands-and-sessions` | P0 | 斜杠命令，cli 变更直接影响 |
| G-3 | `docs/01-从这开始/02-开始上手/05-接入一个消息平台（推荐飞书）.md` | `/start/getting-started/connect-message-platform` | P1 | 消息平台接入，gateway 变更影响 |
| G-4 | `docs/01-从这开始/01-先跑起来/03-进入终端并连接服务器.md` | `/start/get-running/connect-terminal` | P0 | 安装前序步骤，install 变更影响 |
| G-5 | `docs/01-从这开始/03-玩出花样/02-让 Hermes 更像你.md` | `/start/personalize/soul` | P2 | 个性化配置，configuration 变更影响 |
| G-6 | `docs/01-从这开始/03-玩出花样/06-让终端更顺眼.md` | `/start/personalize/skins-and-themes` | P2 | 终端主题，configuration 变更影响 |
| G-7 | `docs/01-从这开始/04-自己造东西/02-多个助手一起工作.md` | `/start/build/profiles` | P2 | Profiles 功能，profiles 变更影响 |
| G-8 | `docs/01-从这开始/04-自己造东西/08-放进编辑器里用.md` | `/start/build/acp-ide` | P1 | ACP/IDE 集成，cli 变更影响 |
| G-9 | `docs/05-遇到问题/08-Docker Nix SSH 与远程后端问题.md` | `/issues/docker-nix-remote` | P2 | 排障页，troubleshooting 变更影响 |
| G-10 | `docs/06-reference/03-Slash Commands 参考.md` | `/reference/slash-commands` | P0 | 命令参考，cli 变更直接影响 |

---

## 6. 使用方法

### 6.1 版本更新时如何使用本映射

1. **获取 release digest**：读取上游 GitHub release notes
2. **标记 change_categories**：识别本次更新涉及的域（如 `cli`, `tools`, `mcp`）
3. **叠加元标签**：检查是否有 `breaking_change` / `deprecation` / `new_feature` / `bug_fix`
4. **查表确定 tier**：根据第 1.2 节映射确定 P0/P1/P2
5. **应用升级规则**：根据第 1.3 节决定是否升级
6. **生成受影响页面清单**：按 tier 输出需要同步的页面列表
7. **更新 version-ledger.yaml**：在 versions 数组中追加本次记录

### 6.2 输出给 PM 的同步卡格式

每个同步任务卡包含：

```yaml
card:
  title: "[P0] 同步 CLI 命令参考 —— v2026.x.x 变更"
  tier: P0
  upstream_version: v2026.x.x
  change_categories: [cli, breaking_change]
  affected_docs:
    - source: docs/06-reference/02-CLI 命令参考.md
      slug: /reference/cli-commands
      action: full_review  # full_review | patch_update | metadata_only
  sla: 48h
  assignee: content
```

---

## 7. 验证结果

| 验证项 | 结果 |
|---|---|
| version-ledger P0 6 个文档全部匹配 site-route-map | ✅ 通过 |
| version-ledger P1 12 个文档全部匹配 site-route-map | ✅ 通过 |
| version-ledger P2 11 个文档全部匹配 site-route-map | ✅ 通过 |
| 43 个未分层文档已完成分类（exempt / provider / recommend） | ✅ 通过 |
| 元标签升级规则定义完整 | ✅ 通过 |
| JSON 计划文件已生成 | ✅ 通过 |
