
# P0/P1 文章规范修复最终验收报告

**任务 ID:** `hz-p0-p1-style-repair-20260705-T4-final-qa-and-report`
**执行人:** `Ikki (Content Agent)`
**日期:** 2026-07-05

## 1. 验收范围
- P0 级别文章: `docs/01-从这开始/` 目录下的所有 Markdown 文件。
- P1 级别文章: `docs/02-现成方案/` 目录下的所有 Markdown 文件。

## 2. 验收标准
1.  **无 frontmatter**: 文件顶部无 `---...---` 元数据块。
2.  **无模板残留**: 无 `[TBD]`、`[占位符]` 等字样。
3.  **无占位图**: 无指向 `assets/placeholder.png` 的链接。
4.  **无断链图片**: 所有图片路径有效。
5.  **有固定下一步**: 每篇文章结尾有明确的“下一步”引导。
6.  **技术检查通过**: `pytest` 测试通过。

## 3. 验收结果

### 3.1 内容规范检查

**结论: 严重不通过。** 发现大量图片链接断裂，共计 111 个问题点。

**问题清单:**

#### P0 文件问题清单

- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/总览.md**
  - [ ] 图片文件不存在: ../assets/rm2-learning-path-gemini-final-v2.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/01-先跑起来/01-总览.md**
  - [ ] 图片文件不存在: ../../assets/rm2-2-get-running-index-06-stage-map-closed.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/01-先跑起来/02-先准备运行环境.md**
  - [ ] 图片文件不存在: ../../assets/prepare-environment-01-choice-map-cards-v2.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/01-先跑起来/03-进入终端并连接服务器.md**
  - [ ] 图片文件不存在: ../../assets/rm2-2-connect-terminal-01-local-vs-ssh-route.webp
  - [ ] 图片文件不存在: ../../assets/rm2-2-connect-terminal-02-ssh-login-success.webp
  - [ ] 图片文件不存在: ../../assets/rm2-2-connect-terminal-03-ssh-git-success.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/01-先跑起来/04-把 Hermes 装上去.md**
  - [ ] 图片文件不存在: ../../assets/rm2-2-install-hermes-01-install-command-running.webp
  - [ ] 图片文件不存在: ../../assets/rm2-2-install-hermes-02-version-and-doctor-success.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/01-先跑起来/05-配好 AI 大模型并完成第一次互动.md**
  - [ ] 图片文件不存在: ../../assets/rm2-2-first-hello-01-model-setup-success.webp
  - [ ] 图片文件不存在: ../../assets/rm2-2-first-hello-02-first-reply-success.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/02-开始上手/01-总览.md**
  - [ ] 图片文件不存在: ../../assets/rm2-3-get-started-index-01-daily-usage-path.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/02-开始上手/02-认识 Hermes 的基本使用方式.md**
  - [ ] 图片文件不存在: ../../assets/rm2-3-basic-usage-01-cli-main-surface.webp
  - [ ] 图片文件不存在: ../../assets/rm2-3-basic-usage-02-basic-chat-flow-success.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/02-开始上手/03-常用斜杠命令与会话管理.md**
  - [ ] 图片文件不存在: ../../assets/rm2-3-slash-commands-01-command-groups.webp
  - [ ] 图片文件不存在: ../../assets/rm2-3-slash-commands-02-session-save-resume.webp
  - [ ] 图片文件不存在: ../../assets/rm2-3-slash-commands-03-persona-command-success.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/02-开始上手/04-常用 Skills（按日常使用场景精选）.md**
  - [ ] 图片文件不存在: ../../assets/rm2-3-skills-curated-01-skill-scenario-map.webp
  - [ ] 图片文件不存在: ../../assets/rm2-3-skills-curated-02-skill-call-success.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/02-开始上手/05-接入一个消息平台（推荐飞书）.md**
  - [ ] 图片文件不存在: ../../assets/rm2-3-connect-platform-01-platform-connection-map.webp
  - [ ] 图片文件不存在: ../../assets/rm2-3-connect-platform-02-platform-config-ui.webp
  - [ ] 图片文件不存在: ../../assets/rm2-3-connect-platform-03-first-message-success-v3.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/03-玩出花样/01-总览.md**
  - [ ] 图片文件不存在: ../../assets/rm2-4-advanced-usage-index-01-single-agent-upgrade-map.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/03-玩出花样/02-让 Hermes 更像你.md**
  - [ ] 图片文件不存在: ../../assets/rm2-4-soul-01-soul-structure-map.webp
  - [ ] 图片文件不存在: ../../assets/rm2-4-soul-02-soul-behavior-diff.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/03-玩出花样/03-让 Hermes 记住你.md**
  - [ ] 图片文件不存在: ../../assets/rm2-4-memory-01-memory-layer-map.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/03-玩出花样/04-自定义 AI 大模型.md**
  - [ ] 图片文件不存在: ../../assets/rm2-4-custom-llm-01-model-routing-map.webp
  - [ ] 图片文件不存在: ../../assets/rm2-4-custom-llm-02-provider-config-success.webp
  - [ ] 图片文件不存在: ../../assets/rm2-4-custom-llm-03-custom-model-success.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/03-玩出花样/05-让工具更顺手.md**
  - [ ] 图片文件不存在: ../../assets/rm2-4-toolsets-01-toolset-map-v4.webp
  - [ ] 图片文件不存在: ../../assets/rm2-4-toolsets-02-tools-toggle-success.webp
  - [ ] 图片文件不存在: ../../assets/rm2-4-toolsets-03-debug-safe-flow.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/03-玩出花样/06-让终端更顺眼.md**
  - [ ] 图片文件不存在: ../../assets/rm2-4-skins-01-theme-comparison.webp
  - [ ] 图片文件不存在: ../../assets/rm2-4-skins-02-theme-switch-success.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/03-玩出花样/07-用桌面端操作 Hermes.md**
  - [ ] 图片文件不存在: ../../assets/desktop-07-real-chat-v1.webp
  - [ ] 图片文件不存在: ../../assets/desktop-07-real-project-picker-v1.webp
  - [ ] 图片文件不存在: ../../assets/desktop-07-real-session-resume-v1.webp
  - [ ] 图片文件不存在: ../../assets/desktop-07-structure-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/04-自己造东西/01-总览.md**
  - [ ] 图片文件不存在: ../../assets/rm2-5-build-your-own-index-01-system-capability-map-v3.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/04-自己造东西/02-多个助手一起工作.md**
  - [ ] 图片文件不存在: ../../assets/rm2-5-profiles-01-multi-profile-map.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/04-自己造东西/03-接入外部记忆系统/01-总览.md**
  - [ ] 图片文件不存在: ../../../assets/rm2-5-memory-providers-01-overview-map.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/04-自己造东西/03-接入外部记忆系统/02-Holographic记忆.md**
  - [ ] 图片文件不存在: ../../../assets/rm2-5-memory-providers-02-holographic-first-route.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/04-自己造东西/03-接入外部记忆系统/03-Honcho记忆.md**
  - [ ] 图片文件不存在: ../../../assets/rm2-5-memory-providers-03-honcho-multi-agent-route.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/04-自己造东西/03-接入外部记忆系统/04-外部记忆对比.md**
  - [ ] 图片文件不存在: ../../../assets/rm2-5-memory-providers-04-compare-decision-route.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/04-自己造东西/04-上下文系统/01-总览.md**
  - [ ] 图片文件不存在: ../../../assets/rm2-5-context-system-01-two-layer-map.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/04-自己造东西/04-上下文系统/02-上下文文件.md**
  - [ ] 图片文件不存在: ../../../assets/rm2-5-context-files-01-long-term-rules-map.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/04-自己造东西/04-上下文系统/03-上下文引用.md**
  - [ ] 图片文件不存在: ../../../assets/rm2-5-context-references-01-temporary-material-map.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/04-自己造东西/05-把 Hermes 接进外部系统.md**
  - [ ] 图片文件不存在: ../../assets/rm2-5-mcp-and-plugins-01-main-route.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/04-自己造东西/06-把 Hermes 暴露成后端服务.md**
  - [ ] 图片文件不存在: ../../assets/rm2-5-api-server-01-openai-compatible-backend-map-v5.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/04-自己造东西/07-让 Hermes 自己自动跑.md**
  - [ ] 图片文件不存在: ../../assets/rm2-5-cron-and-automation-01-scheduled-flow-map.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/04-自己造东西/08-放进编辑器里用.md**
  - [ ] 图片文件不存在: ../../assets/rm2-5-acp-ide-01-editor-workflow-map.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/04-自己造东西/09-把一整套 Agent 打包分享.md**
  - [ ] 图片文件不存在: ../../assets/rm2-4-profile-distribution-structure-v1.webp
  - [ ] 图片文件不存在: ../../assets/rm2-4-profile-distribution-operation-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/01-用 Hermes 做每日晨间简报.md**
  - [ ] 图片文件不存在: ../../assets/solution-practical-01-daily-briefing-flow-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/02-Telegram 消息入口接入.md**
  - [ ] 图片文件不存在: ../../assets/solution-practical-02-telegram-entry-map-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/03-GitHub 备份 Cron Job.md**
  - [ ] 图片文件不存在: ../../assets/solution-practical-03-github-backup-cron-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/04-月费8美金三层模型级联省钱指南.md**
  - [ ] 图片文件不存在: ../../assets/solution-practical-04-three-tier-model-routing-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/05-Token 成本优化避坑指南.md**
  - [ ] 图片文件不存在: ../../assets/solution-practical-05-token-cost-stack-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/06-VPS 自托管 Hermes.md**
  - [ ] 图片文件不存在: ../../assets/solution-practical-06-vps-self-hosting-path-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/07-SOUL.md 人格定制.md**
  - [ ] 图片文件不存在: ../../assets/solution-practical-07-soul-persona-layers-v1.webp
  - [ ] 图片文件不存在: ../../assets/rm2-4-soul-02-soul-behavior-diff.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/08-Obsidian 第二大脑知识库.md**
  - [ ] 图片文件不存在: ../../assets/solution-practical-08-obsidian-second-brain-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/09-Kanban 多 Agent 编排.md**
  - [ ] 图片文件不存在: ../../assets/solution-practical-09-kanban-multi-agent-orchestration-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/10-Home Assistant 智能家居.md**
  - [ ] 图片文件不存在: ../../assets/solution-practical-10-home-assistant-control-loop-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/11-Discord 接入.md**
  - [ ] 图片文件不存在: ../../assets/practical-v2-01-discord-entry.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/12-MCP 接入指南.md**
  - [ ] 图片文件不存在: ../../assets/practical-12-mcp-official-screenshot-zh-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/13-Ollama 本地模型.md**
  - [ ] 图片文件不存在: ../../assets/practical-v2-02-ollama-local-model.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/14-GitHub PR 自动审查.md**
  - [ ] 图片文件不存在: ../../assets/practical-v2-05-github-pr-review.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/15-自定义 Skills.md**
  - [ ] 图片文件不存在: ../../assets/practical-v2-04-custom-skills.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/16-安全加固.md**
  - [ ] 图片文件不存在: ../../assets/practical-v2-10-security-hardening.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/17-语音模式.md**
  - [ ] 图片文件不存在: ../../assets/practical-v2-11-voice-mode.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/18-Hermes Agent 进阶实战.md**
  - [ ] 图片文件不存在: ../../assets/practical-v2-06-advanced-skills-mcp-subagents.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/19-Hermes Agent 控制室.md**
  - [ ] 图片文件不存在: ../../assets/practical-v2-07-control-room-specialist-teams.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/20-60 天分析师工作流.md**
  - [ ] 图片文件不存在: ../../assets/practical-v2-08-60-days-6-lessons.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/21-Hermes Agent 与 Ollama 最快路径.md**
  - [ ] 图片文件不存在: ../../assets/practical-v2-03-ollama-fast-local-install.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/22-Hermes Agent 深度拆解与自建指南.md**
  - [ ] 图片文件不存在: ../../assets/practical-v2-09-deep-dive-build-your-own.webp

#### P1 文件问题清单

- **/opt/projects/awesome-hermes-agent-zh/docs/02-现成方案/01-内容创作与发布/02-小红书内容助手.md**
  - [ ] 图片文件不存在: ../../assets/solution-xhs-single-vs-series-v3-cliproxy-g31.webp
  - [ ] 图片文件不存在: ../../assets/solution-xhs-output-map-v3-cliproxy-g31.webp
  - [ ] 图片文件不存在: ../../assets/solution-xhs-cli-vs-acp-v3-cliproxy-g31.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/02-现成方案/01-内容创作与发布/03-公众号写作助手.md**
  - [ ] 图片文件不存在: ../../assets/solution-gzh-single-vs-series-v3-cliproxy-g31.webp
  - [ ] 图片文件不存在: ../../assets/solution-gzh-output-map-v3-cliproxy-g31.webp
  - [ ] 图片文件不存在: ../../assets/solution-gzh-cli-vs-acp-v3-cliproxy-g31.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/02-现成方案/01-内容创作与发布/04-PPT 助手.md**
  - [ ] 图片文件不存在: ../../assets/solution-ppt-structure-vs-script-review-candidate-07-integrated.webp
  - [ ] 图片文件不存在: ../../assets/solution-ppt-team-handoff-review-candidate-02.webp
  - [ ] 图片文件不存在: ../../assets/solution-ppt-output-map-review-candidate-09-cn-teamstyle.webp
  - [ ] 图片文件不存在: ../../assets/solution-ppt-cli-vs-acp-review-candidate-02-lines.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/02-现成方案/01-内容创作与发布/05-X-Twitter 内容与互动助手.md**
  - [ ] 图片文件不存在: ../../assets/solution-twitter-read-vs-actions-v1.webp
  - [ ] 图片文件不存在: ../../assets/solution-twitter-setup-chain-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/02-现成方案/02-办公效率与知识整理/02-会议纪要助手.md**
  - [ ] 图片文件不存在: ../../assets/office-integrated-final-v1/office-meeting-compare-gemini-3-pro-image-preview.webp
  - [ ] 图片文件不存在: ../../assets/office-integrated-final-v1/office-meeting-output-final-gemini-3-pro-image-preview.webp
  - [ ] 图片文件不存在: ../../assets/office-integrated-final-v1/office-meeting-cliacp-gemini-3-pro-image-preview.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/02-现成方案/02-办公效率与知识整理/03-项目日报助手.md**
  - [ ] 图片文件不存在: ../../assets/office-integrated-final-v1/office-daily-compare-ultrastrict-gemini-3-pro-image-preview.webp
  - [ ] 图片文件不存在: ../../assets/office-integrated-final-v1/office-daily-output-gemini-3-pro-image-preview.webp
  - [ ] 图片文件不存在: ../../assets/office-integrated-final-v1/office-daily-cliacp-gemini-3-pro-image-preview.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/02-现成方案/02-办公效率与知识整理/04-资料总结助手.md**
  - [ ] 图片文件不存在: ../../assets/office-integrated-final-v1/office-summary-compare-gemini-3-pro-image-preview.webp
  - [ ] 图片文件不存在: ../../assets/office-integrated-final-v1/office-summary-output-gemini-3-pro-image-preview.webp
  - [ ] 图片文件不存在: ../../assets/office-integrated-final-v1/office-summary-cliacp-fixed-gemini-3-pro-image-preview.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md**
  - [ ] 图片文件不存在: ../../assets/solution-miniapp-solo-vs-team-map-zh-v6.webp
  - [ ] 图片文件不存在: ../../assets/solution-miniapp-3-layer-map-v7.webp
  - [ ] 图片文件不存在: ../../assets/solution-miniapp-cli-vs-acp-map-zh-v10.webp
  - [ ] 图片文件不存在: ../../assets/solution-miniapp-solo-real-run-proof.webp
  - [ ] 图片文件不存在: ../../assets/solution-miniapp-solo-followup-proof.webp
  - [ ] 图片文件不存在: ../../assets/solution-miniapp-team-handoff-proof.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/02-现成方案/03-应用开发与快速原型/03-敏捷 Web 开发助手.md**
  - [ ] 图片文件不存在: ../../assets/solution-webdev-solo-vs-team-map-v1.webp
  - [ ] 图片文件不存在: ../../assets/solution-webdev-3-layer-map-v1.webp
  - [ ] 图片文件不存在: ../../assets/solution-webdev-cli-vs-acp-map-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/02-现成方案/01-内容创作与发布/06-多平台内容改写助手.md**
  - [ ] 图片文件不存在: ../../assets/solution-multiplatform-solo-vs-batch-v1.webp
  - [ ] 图片文件不存在: ../../assets/solution-multiplatform-output-bundle-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/02-现成方案/02-办公效率与知识整理/05-行动计划助手.md**
  - [ ] 图片文件不存在: ../../assets/solution-action-plan-standard-vs-lite-v1.webp
  - [ ] 图片文件不存在: ../../assets/solution-action-plan-output-map-v1.webp
- **/opt/projects/awesome-hermes-agent-zh/docs/02-现成方案/02-办公效率与知识整理/06-邮件群消息摘要助手.md**
  - [ ] 图片文件不存在: ../../assets/solution-message-summary-complete-vs-quick-v1.webp
  - [ ] 图片文件不存在: ../../assets/solution-message-summary-output-map-v1.webp

**总计发现 111 个内容规范问题。**

### 3.2 技术检查 (pytest)

- **命令:** `cd /opt/projects/awesome-hermes-agent-zh && python -m pytest -q`
- **结果:** `15 passed in 4.82s`
- **结论:** **通过。** 仓库的技术依赖和基本配置健康。

## 4. 阻塞点与风险

- **核心阻塞点:** P0/P1 文章中的所有图片资源全部丢失，导致用户无法理解核心图示内容。这是一个 **P0 级别的发布阻断 Bug**。
- **风险:** 强制发布将导致站点核心教程页面大面积内容残缺，严重影响用户体验和产品专业性。

## 5. 最终结论与下一步建议

- **是否可提交部署:** **否。**
- **建议:**
    1.  **立即挂起 (Suspend)** 当前发布流程。
    2.  **创建 P0 级紧急修复任务**，指派给内容或开发团队，目标是找回并正确链接所有丢失的图片资源。
    3.  在图片问题彻底解决并通过回归验收之前，**禁止将此分支合入主干或部署到生产环境**。

