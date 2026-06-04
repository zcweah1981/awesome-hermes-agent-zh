# Hermes 中文站官方文档与第三方资料整合更新计划

> 计划编号：OFFICIAL-AND-THIRDPARTY-CONTENT-PLAN-20260604-0001  
> 项目：hermes-zh / awesome-hermes-agent-zh  
> 日期：2026-06-04  
> 状态：待执行  
> 原则：官方文档是事实源；第三方资料只作为场景、理解、选型和案例补充。

## 1. 目标

把 Hermes 官方操作文档与国外第三方教程、文章、视频、社区案例统一纳入中文站内容规划，形成可执行的更新路线：

1. 修正中文站与官方操作文档不一致的内容。
2. 补齐官方已出现但中文站缺失的新能力说明。
3. 把第三方热门资料整理成中文用户可读的精选入口和场景库。
4. 保持内容仓、站点仓、导航、搜索、sitemap、llms/ai-index 的发布闭环。

## 2. 范围边界

### 2.1 本轮包括

- 官方操作文档对比与同步。
- 第三方文章/视频/社区案例 Source Map。
- 新增或修改中文站内容页面。
- 必要的导航、索引、搜索、站点构建与链接校验。
- 内容仓 baseline / source map / governance plan 更新。

### 2.2 本轮不包括

- 不直接搬运第三方全文。
- 不把第三方观点写成官方事实。
- 不把官方 main 未发布代码变化夸大成稳定 release 能力。
- 不触碰与本计划无关的页面视觉和站点 UI。
- 不重写中文站信息架构，只做必要补页和入口调整。

## 3. 来源分级

### 3.1 官方事实源

官方来源用于确定命令、参数、能力边界、安装步骤、环境变量、配置方法。

已确认需纳入的官方页面：

- Installation: https://hermes-agent.nousresearch.com/docs/getting-started/installation
- Quickstart: https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- Windows Native: https://hermes-agent.nousresearch.com/docs/user-guide/windows-native
- Desktop App: https://hermes-agent.nousresearch.com/docs/user-guide/desktop
- TUI: https://hermes-agent.nousresearch.com/docs/user-guide/tui
- Profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Profile Distributions: https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions
- CLI Commands Reference: https://hermes-agent.nousresearch.com/docs/reference/cli-commands
- Codex App-Server Runtime: https://hermes-agent.nousresearch.com/docs/user-guide/features/codex-app-server-runtime
- User Stories: https://hermes-agent.nousresearch.com/docs/user-stories
- GitHub Releases: https://github.com/NousResearch/hermes-agent/releases

### 3.2 第三方补充源

第三方来源只作为场景、叙事、教程路径、选型角度、案例灵感。

首批候选来源：

- DataCamp Hermes setup/tutorial: https://www.datacamp.com/es/tutorial/hermes-agent
- dev.to Deep Dive & Build-Your-Own Guide: https://dev.to/truongpx396/hermes-agent-deep-dive-build-your-own-guide-1pcc
- Daily Dose of Data Science Hermes Agent Masterclass: https://www.dailydoseofds.com/p/hermes-agent-masterclass
- Metics Media YouTube setup guide: https://www.youtube.com/watch?v=LvWobwr0Neg
- Tech With Tim / beginner setup videos: https://www.youtube.com/watch?v=1ve4Atbqmoo
- BoxminingAI live tutorial: https://www.youtube.com/watch?v=QFCnFA_IXTA
- Petronella release tracker / guide: https://petronellatech.com/blog/hermes-agent-ai-guide-2026
- utilo review: https://utilo.io/en/home/blog/hermes-agent-review-2026
- explainx.ai explainer: https://explainx.ai/blog/hermes-agent-nous-research-remote-vps-telegram-cli-guide
- MindStudio cron jobs article: https://www.mindstudio.ai/blog/hermes-agent-cron-jobs-plain-english-github-backup
- Composio alternatives: https://composio.dev/content/hermes-agent-alternatives
- Reddit use cases megathread: https://www.reddit.com/r/hermesagent/comments/1t6gf4j/megathread_hermes_agent_use_cases_what_the
- HackerNoon Hermes tests/comparison articles: https://hackernoon.com/
- Umbrel App Store Hermes Agent: https://apps.umbrel.com/app/hermes-agent
- TrueNAS Apps Hermes Agent: https://apps.truenas.com/catalog/hermes-agent_community
- AUR package: https://aur.archlinux.org/packages/hermes-agent
- Docker Hub image pages: https://hub.docker.com/r/nousresearch/hermes-agent

## 4. 核心内容差异与更新方向

### 4.1 P0：Windows 安装路线纠偏

#### 官方现状

官方已提供 Windows Native early beta，并给出 PowerShell 安装命令：

```powershell
iex (irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1)
```

Windows installer 处理 uv、Python 3.11、Node.js 22、Portable Git、ripgrep、ffmpeg、PATH 等。

#### 中文站现状

当前中文站多处仍偏向“Windows 用户先走 WSL2，不要停在 PowerShell/CMD”。这与官方新文档不完全一致。

#### 更新方案

把 Windows 路线改成三路线：

1. WSL2：稳定推荐。
2. Windows Native：官方 early beta，可试用但需说明边界。
3. Desktop Installer：适合非开发者或希望桌面入口的用户。

#### 影响页面

- `docs/01-从这开始/01-先跑起来/02-先准备运行环境.md`
- `docs/01-从这开始/01-先跑起来/03-进入终端并连接服务器.md`
- `docs/01-从这开始/01-先跑起来/04-把 Hermes 装上去.md`
- `docs/05-遇到问题/02-安装更新与环境问题.md`
- `docs/06-reference/05-环境变量参考.md`

### 4.2 P0：Profile Distributions 专题

#### 官方现状

官方新增 Profile Distribution 能力：把完整 Agent 作为 Git 仓库分发。

关键命令：

```bash
hermes profile install github.com/you/my-research-agent --alias
hermes profile update my-research-agent
```

核心结构：

```text
distribution.yaml
SOUL.md
config.yaml
skills/
cron/
mcp.json
README.md
```

#### 中文站现状

当前 Profile 参考页主要覆盖 list/use/create/delete/show/alias/rename/export/import/clone，缺少 distribution 体系。

#### 更新方案

新增专题：`把一整套 Agent 打包分享`。

内容包括：

- Profile 与 Profile Distribution 的区别。
- `distribution.yaml` 结构。
- 安装别人分享的 Agent。
- 发布自己的 Agent。
- 更新机制。
- 作者维护文件 vs 用户私有文件。
- 与中文站「现成方案 / packs」体系的关系。

#### 影响页面

- `docs/06-reference/04-Profile 命令参考.md`
- `docs/01-从这开始/04-自己造东西/新增：把一整套 Agent 打包分享.md`
- `docs/02-现成方案` 相关入口。

### 4.3 P1：Desktop App 页面

#### 官方现状

官方 Desktop App 是同一 Hermes runtime 的桌面入口，支持：

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash -s -- --include-desktop
hermes desktop
hermes desktop --cwd <path>
```

旧命令 `hermes gui` 是 deprecated alias。环境变量包括 `HERMES_DESKTOP_CWD`。

#### 更新方案

新增页面：`用桌面端操作 Hermes`。

内容包括：

- Desktop 不是独立产品，而是同一 runtime。
- 和 CLI/TUI/Gateway 的关系。
- 安装、启动、cwd、更新。
- Windows GUI installer 注意事项。

#### 影响页面

- 新增 Desktop 页面。
- `docs/06-reference/02-CLI 命令参考.md`
- `docs/06-reference/05-环境变量参考.md`
- `docs/05-遇到问题/02-安装更新与环境问题.md`

### 4.4 P1：TUI / CLI Reference 补齐

#### 官方现状

官方 TUI/CLI 文档包含：

```bash
hermes --tui
hermes --tui -c
hermes --tui --continue
hermes --tui -r <session>
hermes --tui --resume "..."
hermes --tui --dev
```

环境变量：

```bash
HERMES_TUI=1
HERMES_TUI_DIR=/path/to/prebuilt/ui-tui
```

Slash / UI 能力包括：

- `/mouse`
- `/reload`
- `/agents`
- `/tasks`
- `/usage`
- `/details`
- live session switcher
- collapsible startup banner

#### 更新方案

更新现有 CLI/TUI 页面与 Slash Commands 参考。

#### 影响页面

- `docs/05-遇到问题/04-CLI TUI 与会话问题.md`
- `docs/06-reference/02-CLI 命令参考.md`
- `docs/06-reference/03-Slash Commands 参考.md`
- `docs/06-reference/05-环境变量参考.md`

### 4.5 P1：Provider / Quickstart 对齐

#### 官方现状

官方 Quickstart provider 表包含 Nous Portal、OpenAI Codex、Anthropic、OpenRouter、Z.AI/GLM、Kimi、Kimi China、Arcee AI、GMI Cloud、MiniMax OAuth、MiniMax、MiniMax China、Alibaba Cloud/DashScope/Qwen、Hugging Face、AWS Bedrock、Azure Foundry、Google AI Studio、Google Gemini OAuth 等。

#### 更新方案

更新模型配置、国内模型、Provider 排障、环境变量页。中文站要重点解释国内可用性、API Key / OAuth / endpoint 边界。

#### 影响页面

- `docs/01-从这开始/01-先跑起来/05-配好 AI 大模型并完成第一次互动.md`
- `docs/01-从这开始/03-玩出花样/04-自定义 AI 大模型.md`
- `docs/03-国内落地/02-国内模型/...`
- `docs/05-遇到问题/03-模型 Provider 与自定义 endpoint 问题.md`
- `docs/06-reference/05-环境变量参考.md`

### 4.6 P2：Codex App-Server Runtime

新增高级说明页或参考页，标注 optional、openai/openai-codex 相关、国内 OAuth/订阅/网络边界。不得让普通用户误以为必须开启。

## 5. 第三方资料内容化方案

### 5.1 新手教程精选

#### 来源

- DataCamp
- Metics Media YouTube
- Tech With Tim / Alex Finn YouTube
- explainx.ai

#### 页面建议

新增：`国外教程怎么教 Hermes：适合新手看的资料精选`。

每项卡片包含：

- 来源。
- 适合谁。
- 借鉴点。
- 注意事项。
- 原文链接。

### 5.2 架构深挖与 Build-Your-Own

#### 来源

- dev.to Deep Dive
- Daily Dose Masterclass
- Petronella release tracker / guide

#### 页面建议

新增或补充：`Hermes 的运行架构：为什么它不是一个聊天网页`。

结构：

1. 入口层：CLI / TUI / Desktop / Gateway。
2. 能力层：tools / skills / memory / cron / MCP。
3. 执行层：terminal / browser / subagents / kanban。
4. 持久层：profiles / sessions / skills / memory。
5. 分发层：Profile Distribution。

### 5.3 场景库

#### 来源

- 官方 User Stories。
- Reddit use cases。
- MindStudio cron jobs。
- YouTube 实测。
- HackerNoon 实测。

#### 页面建议

新增：`别人正在用 Hermes 做什么`。

场景卡片：

- 每日简报。
- 自动备份。
- 竞品监控。
- 研究助理。
- 代码开发。
- 项目站会。
- 家庭助理。
- 内容流水线。
- 多 Agent 协作。

### 5.4 选型指南

#### 来源

- HackerNoon Hermes vs OpenClaw。
- Composio alternatives。
- utilo review。
- Medium Agent Landscape。
- i-scoop analysis。

#### 页面建议

新增或并入现成方案：`Hermes 适合谁：和其他 Agent 工具怎么选`。

要求：不拉踩、不夸大、不把第三方观点写成官方事实。

### 5.5 国外自托管生态参考

#### 来源

- Umbrel。
- TrueNAS。
- AUR。
- Docker Hub。
- SourceForge mirror。

#### 页面建议

新增到 `03-国内落地/01-国内部署`：`国外自托管生态参考：Umbrel、TrueNAS、AUR、Docker`。

要求：只写参考，不写成官方首选；国内路线仍优先 VPS / Docker / 云主机。

## 6. 执行阶段

### 阶段 A：Source Map 与事实边界

输出：`governance/research/official-and-thirdparty-source-map-20260604.md`

验收：

- 至少覆盖 10 个官方页面。
- 至少覆盖 15 个第三方来源。
- 每条来源有 URL、类型、可信度、可用于哪些页面。
- 标注官方事实 / 第三方观点 / 社区案例。

### 阶段 B：内容架构规划

输出：`governance/plans/content-update-plan-20260604.md`

验收：

- P0/P1/P2 分级。
- 新增页、修改页、入口页清单。
- 每页有读者、目标、来源、验收标准。
- 不出现 placeholder。

### 阶段 C：官方差异落地

优先实现：

- Windows Native。
- Profile Distribution。
- Desktop。
- TUI/CLI。
- Provider/Quickstart。

验收：

- 命令准确。
- 链接可用。
- 不再有过期的 WSL2 单一路线叙事。
- 文档校验通过。

### 阶段 D：第三方增强页面落地

实现：

- 国外教程精选。
- 场景库。
- 选型指南。
- 国外自托管生态参考。

验收：

- 不搬运全文。
- 每项保留来源链接。
- 不误称官方。
- 中文读者能直接判断是否需要进一步阅读。

### 阶段 E：站点集成与发布校验

验收：

- 导航/route-map 更新。
- search index 更新。
- sitemap 更新。
- llms/ai-index 更新。
- 构建通过。
- 链接检查通过。
- Preview proof 可见。

## 7. 派单拆分

### Task 1：Source Map 调研

负责人：Mu / Research  
优先级：P0  
输出：`governance/research/official-and-thirdparty-source-map-20260604.md`

### Task 2：内容架构规划

负责人：Ikki / Content  
优先级：P0  
输出：`governance/plans/content-update-plan-20260604.md`

### Task 3：官方操作差异落地

负责人：Ikki / Content + Long Review  
优先级：P0/P1  
输出：更新内容仓 docs。

### Task 4：第三方增强页落地

负责人：Ikki / Content  
优先级：P1/P2  
输出：新增教程精选、场景库、选型、自托管生态参考页。

### Task 5：技术集成与发布验证

负责人：Long / Hyoga  
优先级：P1  
输出：构建、链接、导航、索引、preview proof。

### Task 6：PM 验收

负责人：Seiya / PM  
优先级：P0  
输出：验收报告与剩余风险清单。

## 8. 验收总标准

- 官方命令、参数、链接准确。
- 第三方资料只作来源卡片/摘要/案例，不搬运全文。
- 第三方观点不写成官方事实。
- 不出现 placeholder docs。
- 新增页面被导航、搜索、sitemap、llms/ai-index 收录。
- 内容仓和站点仓边界清晰。
- 所有 Agent proof 可见。
- PM 最终验收后再进入生产发布。
