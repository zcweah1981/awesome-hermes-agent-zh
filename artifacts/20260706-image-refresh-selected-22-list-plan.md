# 20260706 selected-22 文章主图重做清单与执行方案

## 1. 任务范围

- 任务组：`image-refresh-selected-22`
- 本任务只负责固化清单与方案，不直接改文章、不替换图片。
- 后续执行只替换每篇文章顶部第一张、非真实截图类主图；正文中的真实截图、操作证据图、中段结构图和既有截图不纳入本批。
- 生图模型固定使用 `cx/gpt-5.4-image`。
- 风格固定参考现有中文站结构图家族：`docs/assets/rm2-2-get-running-index-06-stage-map-closed.webp`、`docs/assets/rm2-3-get-started-index-01-daily-usage-path.webp`、`docs/assets/rm2-5-cron-and-automation-01-scheduled-flow-map.webp`、`docs/assets/solution-practical-03-github-backup-cron-v1.webp`。

## 2. 22 篇文章清单

| 序号 | 文章路径 | 当前顶部主图 | 执行动作 | 新图建议命名 |
|---:|---|---|---|---|
| 01 | `docs/01-从这开始/05-实战应用/07-SOUL.md 人格定制.md` | `docs/assets/solution-practical-07-soul-persona-layers-v1.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-07-soul-persona.webp` |
| 02 | `docs/01-从这开始/05-实战应用/08-Obsidian 第二大脑知识库.md` | `docs/assets/solution-practical-08-obsidian-second-brain-v1.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-08-obsidian-second-brain.webp` |
| 03 | `docs/01-从这开始/05-实战应用/09-Kanban 多 Agent 编排.md` | `docs/assets/solution-practical-09-kanban-multi-agent-orchestration-v1.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-09-kanban-orchestration.webp` |
| 04 | `docs/01-从这开始/05-实战应用/10-Home Assistant 智能家居.md` | `docs/assets/solution-practical-10-home-assistant-control-loop-v1.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-10-home-assistant.webp` |
| 05 | `docs/01-从这开始/05-实战应用/11-Discord 接入.md` | `docs/assets/practical-v2-01-discord-entry.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-11-discord-entry.webp` |
| 06 | `docs/01-从这开始/05-实战应用/12-MCP 接入指南.md` | `docs/assets/practical-12-mcp-official-screenshot-zh-v1.webp` | 仅当确认不是官方真实截图时重做；若是截图则保持不动并从执行批次剔除 | `docs/assets/refresh-20260706-practical-12-mcp-entry.webp` |
| 07 | `docs/01-从这开始/05-实战应用/13-Ollama 本地模型.md` | `docs/assets/practical-v2-02-ollama-local-model.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-13-ollama-local.webp` |
| 08 | `docs/01-从这开始/05-实战应用/14-GitHub PR 自动审查.md` | `docs/assets/practical-v2-05-github-pr-review.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-14-github-pr-review.webp` |
| 09 | `docs/01-从这开始/05-实战应用/15-自定义 Skills.md` | `docs/assets/practical-v2-04-custom-skills.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-15-custom-skills.webp` |
| 10 | `docs/01-从这开始/05-实战应用/16-安全加固.md` | `docs/assets/practical-v2-10-security-hardening.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-16-security-hardening.webp` |
| 11 | `docs/01-从这开始/05-实战应用/17-语音模式.md` | `docs/assets/practical-v2-11-voice-mode.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-17-voice-mode.webp` |
| 12 | `docs/01-从这开始/05-实战应用/18-Hermes Agent 进阶实战.md` | `docs/assets/practical-v2-06-advanced-skills-mcp-subagents.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-18-advanced-practice.webp` |
| 13 | `docs/01-从这开始/05-实战应用/19-Hermes Agent 控制室.md` | `docs/assets/practical-v2-07-control-room-specialist-teams.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-19-control-room.webp` |
| 14 | `docs/01-从这开始/05-实战应用/20-60 天分析师工作流.md` | `docs/assets/practical-v2-08-60-days-6-lessons.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-20-analyst-60-days.webp` |
| 15 | `docs/01-从这开始/05-实战应用/21-Hermes Agent 与 Ollama 最快路径.md` | `docs/assets/practical-v2-03-ollama-fast-local-install.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-21-ollama-fast-path.webp` |
| 16 | `docs/01-从这开始/05-实战应用/22-Hermes Agent 深度拆解与自建指南.md` | `docs/assets/practical-v2-09-deep-dive-build-your-own.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-22-deep-dive-build.webp` |
| 17 | `docs/01-从这开始/05-实战应用/23-实战：个人项目开发工作流.md` | `docs/assets/practical-v2-23-personal-dev-workflow.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-23-personal-dev-workflow.webp` |
| 18 | `docs/01-从这开始/05-实战应用/24-实战：用-session_search-打造你的外部记忆.md` | `docs/assets/rm2-4-memory-01-memory-layer-map.webp` | 重做顶部非截图主图，避免继续复用通用记忆图 | `docs/assets/refresh-20260706-practical-24-session-search-memory.webp` |
| 19 | `docs/01-从这开始/05-实战应用/25-实战：服务器自动化运维.md` | `docs/assets/practical-v2-25-server-automation-ops.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-25-server-automation-ops.webp` |
| 20 | `docs/01-从这开始/05-实战应用/26-Hermes-Agent-最佳实践：从工具到助理.md` | `docs/assets/practical-v2-26-tool-to-assistant-best-practices.webp` | 重做顶部非截图主图；注意当前文件已有其他工作区改动，本批执行时需先核对差异 | `docs/assets/refresh-20260706-practical-26-tool-to-assistant.webp` |
| 21 | `docs/01-从这开始/05-实战应用/27-实战：个人事务处理中心.md` | `docs/assets/solution-message-summary-output-map-v1.webp` | 重做顶部非截图主图，避免继续复用消息摘要方案图 | `docs/assets/refresh-20260706-practical-27-personal-control-center.webp` |
| 22 | `docs/01-从这开始/05-实战应用/28-高级玩法：NotebookLM 超级知识库.md` | `docs/assets/practical-v2-28-notebooklm-super-knowledge-base.webp` | 重做顶部非截图主图 | `docs/assets/refresh-20260706-practical-28-notebooklm-knowledge-base.webp` |

## 3. 执行原则

1. 每篇只处理正文中第一张 Markdown 图片，且必须是结构图、路径图、流程图、对比图或输出物总览图。
2. 真实截图、官方截图、终端截图、云控制台截图、产品页面截图一律不重绘；如果顶部第一张就是截图，执行 Agent 必须记录“跳过原因”，不得用 AI 图替换。
3. 新图统一输出 `.webp`，优先 16:9 横图，放入 `docs/assets/`。
4. 保留文章原有叙事结构；只改图片引用、alt 文本和必要的一句读图说明，不扩写正文。
5. 不删除旧图，除非后续清理任务明确要求。
6. 不触碰真实截图资产，不改中段截图引用，不改治理文档中与本任务无关的字段。

## 4. 统一生图提示词框架

```text
Model: cx/gpt-5.4-image
Aspect ratio: 16:9
Output: webp
Style reference: docs/assets/rm2-2-get-running-index-06-stage-map-closed.webp, docs/assets/rm2-3-get-started-index-01-daily-usage-path.webp, docs/assets/rm2-5-cron-and-automation-01-scheduled-flow-map.webp, docs/assets/solution-practical-03-github-backup-cron-v1.webp

Create a clean Chinese technical workflow hero diagram for an article about [ARTICLE TOPIC].
Use the Awesome Hermes Agent Chinese site visual style: warm off-white background, dark ink text, muted teal/orange/blue accents, rounded cards, clear arrows, simple system icons, high readability, no people, no mascots, no decorative poster style.
The diagram should show [3-5 KEY NODES] as an end-to-end workflow, with short Chinese labels only.
Make it suitable as the first hero image of a beginner-friendly tutorial.
```

统一负面提示词：

```text
no cartoon characters, no hand-drawn style, no SVG export look, no neon spider web, no random particle network, no star map, no colorful gradient poster, no 3D mascot, no photorealistic people, no tiny unreadable text, no messy arrows, no decorative-only image, no large glowing cyan borders, no fake screenshots, no UI mockup pretending to be a real product, no secrets, no phone numbers, no private chat names
```

## 5. 分批建议

- T2：先处理 07-12，执行前重点确认 12 的当前主图是否属于真实截图。
- T3：处理 13-18，统一做“能力闭环 / 工具流转 / 多模块结构图”。
- T4：处理 19-23，统一做“实战工作流闭环图”。
- T5：处理 24-28，重点修复复用图与错配图，让每篇拥有独立主图。
- T6：统一验收：检查 22 篇文章第一张图引用存在、alt 文本包含主体/动作/结果、图片为 `.webp`、无真实截图被替换、无正文 frontmatter 或模板残留被引入。

## 6. 验收口径

- 清单数量必须为 22 篇。
- 每篇都有当前顶部主图路径、执行动作和建议新图路径。
- 方案明确“只替换顶部非截图主图”。
- 方案明确使用 `cx/gpt-5.4-image` 与参考图风格。
- 执行前需再次运行文件存在性检查，避免在脏工作区覆盖他人改动。
