# 官方新功能映射到实际应用内容更新

## 发现项
根据官方 v0.17.0、v0.18.0 版本发布日志及社区文档，梳理出以下重点新功能。

## 功能列表及来源

| 功能 | 官方来源/社区参考 |
| :--- | :--- |
| **Hermes Desktop App** (Projects, memory graph) | [v0.18.0 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v0.18.0), [v0.17.0 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v0.17.0), [Surface Release (hermes-ai.net)](https://hermes-ai.net/changelog) |
| **Web Admin/Gateway** (scale-to-zero) | [v0.18.0 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v0.18.0), [Surface Release (hermes-ai.net)](https://hermes-ai.net/changelog) |
| **Remote Gateway** | [Surface Release (hermes-ai.net)](https://hermes-ai.net/changelog) |
| **Profiles** (Profile Builder in Dashboard) | [v0.17.0 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v0.17.0) |
| **/undo command** | [Surface Release (hermes-ai.net)](https://hermes-ai.net/changelog) |
| **Codex Runtime** (Implicit from GPT-5.5 mention) | [Changelog Entry](https://hermes-ai.net/changelog) |
| **Cron/no_agent/[SILENT]** | [Tenacity Release (hermes-ai.net)](https://hermes-ai.net/changelog) |
| **MCP 安全** (Implicit from security defaults) | [Tenacity Release (hermes-ai.net)](https://hermes-ai.net/changelog) |
| **Skills Hub** (Browser & Install from Dashboard) | [v0.17.0 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v0.17.0) |
| **多消息平台** (iMessage, WhatsApp, Raft, Google Chat) | [v0.17.0 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v0.17.0), [Tenacity Release](https://hermes-ai.net/changelog), [Foundation Release](https://hermes-ai.net/changelog) |
| **Mixture-of-Agents (MoA)** | [v0.18.0 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v0.18.0) |
| **Agent Self-Verification (`/goal` contracts)** | [v0.18.0 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v0.18.0) |
| **`/learn` command** | [v0.18.0 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v0.18.0) |
| **/journey command & Memory Graph** | [v0.18.0 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v0.18.0) |
| **Async Subagents (`delegate_task(background=true)`)** | [v0.17.0 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v0.17.0) |
| **Automation Blueprints** | [v0.17.0 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v0.17.0) |

## 功能到内容更新映射表

| 功能 | 映射策略 | 建议动作 | 产出物 |
| :--- | :--- | :--- | :--- |
| **Hermes Desktop** | **新增实际应用页** | 撰写一篇完整的 Hermes Desktop 指南，涵盖安装、项目管理、内存可视化、快捷键等。 | 1. 教程：`hermes-desktop-complete-guide.md` <br> 2. 新增导航入口 |
| **Web Admin/Gateway** | **更新旧文** | 更新现有的“部署”和“管理”相关文章，加入 Gateway 自动扩缩、远程连接等新特性。 | 更新 `/docs/deployment/self-hosting.md` |
| **Profiles** | **更新旧文** | 更新“核心概念”中的 Profiles 章节，加入在仪表板中通过构建器管理 Profile 的内容。 | 更新 `/docs/core-concepts/profiles.md` |
| **/undo command** | **只放参考索引** | 在“常用命令”速查表中增加 `/undo` 命令。 | 更新 `/docs/reference/cli-commands.md` |
| **Codex Runtime** | **暂不处理** | 官方信息较少，且可能与特定订阅绑定，暂不作为通用功能推广。 | N/A |
| **Cron/no_agent** | **新增实际应用页** | 撰写一篇关于“自动化任务”的文章，专门介绍如何使用 `cron` 和 `no_agent` 模式创建轻量级、无 LLM 的监控脚本。 | 教程：`hermes-automation-with-no-agent-cron.md` |
| **MCP 安全** | **更新旧文** | 在“安全”相关的章节中，补充关于 MCP 安全默认设置和最佳实践的内容。 | 更新 `/docs/security/best-practices.md` |
| **Skills Hub** | **更新旧文** | 更新“技能”相关文档，介绍如何在 Web UI 中浏览、安装和管理技能。 | 更新 `/docs/core-concepts/skills.md` |
| **多消息平台** | **新增实际应用页** | 创建一个新的“集成”专题，包含 iMessage, WhatsApp, Google Chat 等平台的详细配置和使用指南。 | 1. 专题页: `/integrations/index.md` <br> 2. 各平台指南: `/integrations/imessage.md`, `/integrations/whatsapp.md` 等 |
| **Mixture-of-Agents** | **新增实际应用页** | 撰写高级教程，解释 MoA 原理、如何配置和使用，以及如何解读其透明推理过程。 | 教程：`advanced/mixture-of-agents.md` |
| **Agent Self-Verification** | **新增实际应用页** | 撰写“可靠自动化”教程，重点介绍如何使用 `/goal` 的完成契约来确保任务被正确验证。 | 教程：`workflow/reliable-automation-with-goal-contracts.md` |
| **`/learn` command** | **新增实际应用页** | 撰写教程，演示如何从不同来源（代码、URL、历史记录）中自动提炼和保存技能。 | 教程：`workflow/auto-skill-creation-with-learn.md` |
| **Async Subagents** | **更新旧文** | 在 `delegate_task` 的文档中，补充 `background=true` 的用法和适用场景。 | 更新 `/docs/reference/tool-delegation.md` |
| **Automation Blueprints**| **新增实际应用页** | 撰写一篇面向初学者的“自动化蓝图”指南，展示如何通过表单轻松创建自动化任务。 | 教程：`getting-started/automation-blueprints.md` |

