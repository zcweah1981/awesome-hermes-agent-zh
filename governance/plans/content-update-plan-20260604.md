# 内容更新规划：官方操作差异与第三方资料整合（2026-06-04）

> Recovery Group：`CONTENT-ARCHITECTURE-PLAN-RECOVERY-20260604-084206`  
> Source Map：`/opt/projects/awesome-hermes-agent-zh/governance/research/official-and-thirdparty-source-map-20260604.md`  
> 基础计划：`/opt/projects/awesome-hermes-agent-zh/governance/plans/official-and-thirdparty-content-plan-20260604.md`  
> 状态：已补齐 required deliverable；本文件不是 placeholder。

## 1. 目标

把 Hermes 官方操作文档与第三方教程/评测/社区资料转成中文站可执行更新路线：

- 修正中文站与官方操作文档不一致的安装、CLI、Profile、Desktop、TUI、Provider 内容。
- 补齐官方已成文但中文站缺失的新能力说明。
- 将第三方资料整理成教程精选、场景库、选型指南、自托管生态参考。
- 明确导航、搜索、sitemap、llms/ai-index 的后续技术集成验收边界。

## 2. 新增页清单

### P0：把一整套 Agent 打包分享（Profile Distribution）

- 建议路径：`docs/01-从这开始/04-自己造东西/把一整套 Agent 打包分享.md`
- 读者：已经会创建 Profile，希望把 Agent 交给团队/社区复用的用户。
- 目标：解释 Profile Distribution、安装别人分享的 Agent、发布自己的 Agent。
- 来源：官方 Profiles、Profile Distributions、Skills、Cron、MCP 文档。
- 验收标准：包含 `distribution.yaml`、`SOUL.md`、`config.yaml`、`skills/`、`cron/`、`mcp.json`、安装/更新/发布流程；不得把第三方 pack 写成官方预装能力。

### P0：Windows 三路线安装指南

- 建议路径：更新 `01-先跑起来` 安装链路内相关页面。
- 读者：Windows 普通用户、开发者、非开发者。
- 目标：从“只推荐 WSL2”修正为 WSL2 / Windows Native early beta / Desktop Installer 三路线。
- 来源：官方 Installation、Windows Native、Desktop。
- 验收标准：PowerShell 命令准确；保留 early beta 边界；普通用户能选路线。

### P1：用桌面端操作 Hermes

- 建议路径：`docs/01-从这开始/01-先跑起来/用桌面端操作 Hermes.md`
- 读者：不想长期使用终端的用户。
- 目标：说明 Desktop App 是同一 Hermes runtime 的桌面入口。
- 来源：官方 Desktop App、Installation、Updating。
- 验收标准：说明 `--include-desktop`、`hermes desktop`、`hermes desktop --cwd <path>`、`hermes gui` deprecated alias。

### P1：国外教程精选

- 建议路径：`docs/02-现成方案/国外教程精选.md`
- 读者：希望通过文章/视频快速上手的用户。
- 目标：整理 DataCamp、dev.to、Daily Dose、YouTube、MindStudio 等第三方教程。
- 来源：Source Map T-01 到 T-10。
- 验收标准：至少 8 条资料；每条包含来源、适合谁、可借鉴点、注意事项、URL；标注第三方资料可能滞后。

### P1：别人正在用 Hermes 做什么

- 建议路径：`docs/02-现成方案/别人正在用 Hermes 做什么.md`
- 读者：还没明确使用场景的潜在用户。
- 目标：用开发工作流、Telegram 任务助理、VPS 长期运行、Cron 自动化、知识库、多 Agent 协作解释 Hermes。
- 来源：官方 User Stories、MindStudio Cron、YouTube/VPS 教程、社区案例。
- 验收标准：每个场景说明适合谁、输入、输出、风险。

### P2：Hermes 适合谁选型指南

- 建议路径：`docs/02-现成方案/Hermes 适合谁选型指南.md`
- 读者：在 Hermes、Claude Code、Codex、OpenClaw、自托管方案间比较的人。
- 目标：中性选型，不做竞品攻击。
- 来源：官方定位、Composio alternatives、utilo review、第三方评测。
- 验收标准：说明适合/不适合人群；不强调 zero-trust；不制造恐慌。

### P2：国外自托管生态参考

- 建议路径：`docs/03-国内落地/01-国内部署/国外自托管生态参考.md`
- 读者：准备部署到 VPS、NAS、Docker、家庭服务器的用户。
- 目标：整理 Docker Hub、Umbrel、TrueNAS、AUR、VPS 教程的部署启发。
- 来源：Docker Hub、Umbrel、TrueNAS、AUR、explainx.ai、YouTube VPS 教程。
- 验收标准：保持“参考”定位，不写成官方推荐部署路线。

## 3. 修改页清单

### M0：先准备运行环境

- 路径：`docs/01-从这开始/01-先跑起来/02-先准备运行环境.md`
- 修改目标：加入 Windows Native early beta 与 Desktop Installer 选择说明。
- 来源：Installation、Windows Native。
- 验收标准：三路线清楚，保留普通用户判断。

### M0：进入终端并连接服务器

- 路径：`docs/01-从这开始/01-先跑起来/03-进入终端并连接服务器.md`
- 修改目标：补充 PowerShell / Windows Terminal / WSL2 / SSH 边界。
- 来源：Windows Native、Installation。
- 验收标准：Windows Native 不再被误写成不可用。

### M0：把 Hermes 装上去

- 路径：`docs/01-从这开始/01-先跑起来/04-把 Hermes 装上去.md`
- 修改目标：同步 Linux/macOS shell installer、Windows PowerShell installer、Desktop include 标志。
- 来源：Installation、Desktop。
- 验收标准：命令可复制；说明 Desktop 不是独立 runtime。

### M0：Profile 命令参考

- 路径：`docs/06-reference/04-Profile 命令参考.md`
- 修改目标：增加 Profile Distribution 命令和目录结构。
- 来源：Profiles、Profile Distributions。
- 验收标准：`install`、`update`、`alias`、作者/用户文件边界齐全。

### M1：CLI / Slash / 环境变量 / 问题排查

- 路径：`docs/06-reference/02-CLI 命令参考.md`
- 修改目标：补齐 TUI、Desktop、portal、kanban 等官方命令变化。
- 路径：`docs/06-reference/03-Slash Commands 参考.md`
- 修改目标：补充 `/mouse`、`/reload`、`/agents`、`/tasks`、`/details` 等 TUI 相关命令，并标注适用界面。
- 路径：`docs/06-reference/05-环境变量参考.md`
- 修改目标：补充 `HERMES_TUI`、`HERMES_TUI_DIR`、`HERMES_DESKTOP_CWD`、Docker/Profile Distribution 相关变量边界。
- 路径：`docs/05-遇到问题/02-安装更新与环境问题.md`
- 修改目标：补齐 Windows Native、Portable Git、Desktop Installer、Docker、AUR 等常见问题。
- 验收标准：命令准确；不泄露密钥示例；避免 Telegram 与 TUI-only 命令混淆。

### M1：现成方案入口

- 路径：`docs/02-现成方案/README.md` 或对应索引页。
- 修改目标：增加国外教程精选、场景库、选型指南入口。
- 来源：第三方 Source Map。
- 验收标准：第三方入口标注为参考资料，不与官方能力混淆。

## 4. P0 / P1 / P2 排期

### P0：立即执行

1. Windows 安装路线纠偏。
2. Profile Distribution 专题与 Profile 参考更新。
3. 安装命令 / Quickstart / Provider 基础事实对齐。

### P1：本轮主交付

1. Desktop App 页面。
2. TUI / CLI / Slash Commands / 环境变量补齐。
3. 国外教程精选。
4. 场景库页面。
5. 安装问题页补充。

### P2：可延后

1. 选型指南。
2. 国外自托管生态参考。
3. 更细的第三方教程二次拆解。

## 5. 导航与索引影响

- `01-从这开始 / 04-自己造东西`：新增 Profile Distribution 专题。
- `01-从这开始 / 01-先跑起来`：新增或链接 Desktop App 页面。
- `02-现成方案`：新增国外教程精选、别人正在用 Hermes 做什么、选型指南。
- `03-国内落地 / 01-国内部署`：新增国外自托管生态参考。
- `06-reference`：更新 CLI、Slash Commands、Profile、环境变量参考。

后续技术验收需确认：

- 新增页进入 navigation / route-map。
- 搜索可搜到 `Profile Distribution`、`Desktop App`、`Windows Native`、`TUI`、`国外教程`。
- sitemap、llms / ai-index 收录新增页。
- 内链覆盖安装页 → Windows/Desktop/问题页，Profile 参考 → Profile Distribution，现成方案入口 → 第三方参考页。

## 6. 后续任务拆分

- Task A / Ikki：官方操作差异落地。
- Task B / Ikki：第三方增强页落地。
- Task C / Long：导航、搜索、sitemap、llms、build 技术集成校验。
- Task D / Hyoga：Preview 与外链 proof。
- Task E / Seiya：PM final gate。

## 7. 风险与待确认项

1. 第三方资料可能滞后，必须标注边界。
2. Windows Native 仍是 early beta，不可写成唯一推荐路线。
3. Profile Distribution 是官方 profile 分发机制，不等于中文站官方内置 packs。
4. Desktop App 是同一 runtime 的桌面入口，不是独立产品。
5. 选型指南必须中性，不做竞品攻击。
6. 自托管生态只做参考，不写成官方推荐部署。
7. 本轮不改视觉，不删除 `nav_start_click`。

## 8. 验收声明

本文件满足 recovery task 的 required output：

- 新增页清单：已覆盖。
- 修改页清单：已覆盖。
- 每页读者 / 目标 / 来源 / 验收标准：已覆盖。
- P0/P1/P2 优先级：已覆盖。
- 导航 / 搜索 / sitemap / llms 影响：已覆盖。
- 第三方资料边界：已覆盖。
- 文件路径：`/opt/projects/awesome-hermes-agent-zh/governance/plans/content-update-plan-20260604.md`。
