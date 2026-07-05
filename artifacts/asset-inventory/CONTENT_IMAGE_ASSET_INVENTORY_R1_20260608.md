# 内容源图片 Inventory Proof — R1 2026-06-08

## 任务
- task_id: `HERMES-ZH-P0-FOT-CONTENT-IMAGE-WEBP-CLEANUP-R1-20260608-133412-T1-LONG-CONTENT-ASSET-INVENTORY-UNUSED-MAP`
- 范围: `/opt/projects/awesome-hermes-agent-zh/docs/**/*.md(x)` + `/opt/projects/awesome-hermes-agent-zh/docs/assets/**/*`
- 站点仓仅用于状态保护与同步口径核对: `/opt/projects/hermes-zh`
- 生成时间 UTC: `2026-06-08T07:44:40.280667+00:00`

## 安全边界
- 未部署，未触发 Preview / Production。
- 本卡只产出 inventory proof；未删除文件、未转换图片、未替换引用。
- conversion_before_after: `[]`
- deleted_files: `[]`
- reference_replacements: `[]`

## Git 保护状态
### 内容仓 `/opt/projects/awesome-hermes-agent-zh`
```text
M docs/assets/desktop-07-real-chat-v1.webp
 M docs/assets/desktop-07-real-session-resume-v1.webp
 M docs/assets/prepare-environment-01-choice-map-cards-v2.webp
 M docs/assets/rm2-2-connect-terminal-01-local-vs-ssh-route.webp
 M docs/assets/rm2-2-get-running-index-06-stage-map-closed.webp
 M docs/assets/rm2-3-connect-platform-01-platform-connection-map.webp
 M docs/assets/rm2-3-connect-platform-02-platform-config-ui.webp
 M docs/assets/rm2-3-skills-curated-01-skill-scenario-map.webp
 M docs/assets/rm2-3-slash-commands-01-command-groups.webp
 M docs/assets/rm2-4-advanced-usage-index-01-single-agent-upgrade-map.webp
 M docs/assets/rm2-4-custom-llm-01-model-routing-map.webp
 M docs/assets/rm2-4-memory-01-memory-layer-map.webp
 M docs/assets/rm2-4-skins-01-theme-comparison.webp
 M docs/assets/rm2-4-soul-01-soul-structure-map.webp
 M docs/assets/rm2-4-toolsets-01-toolset-map-v4.webp
 M docs/assets/rm2-5-acp-ide-01-editor-workflow-map.webp
 M docs/assets/rm2-5-context-files-01-long-term-rules-map.webp
 M docs/assets/rm2-5-context-references-01-temporary-material-map.webp
 M docs/assets/rm2-5-context-system-01-two-layer-map.webp
 M docs/assets/rm2-5-cron-and-automation-01-scheduled-flow-map.webp
 M docs/assets/rm2-5-mcp-and-plugins-01-main-route.webp
 M docs/assets/rm2-5-memory-providers-01-overview-map.webp
 M docs/assets/rm2-5-memory-providers-02-holographic-first-route.webp
 M docs/assets/rm2-5-memory-providers-03-honcho-multi-agent-route.webp
 M docs/assets/rm2-5-memory-providers-04-compare-decision-route.webp
 M docs/assets/rm2-5-profiles-01-multi-profile-map.webp
 M docs/assets/rm2-learning-path-gemini-final-v2.webp
?? artifacts/
main
```

### 站点仓 `/opt/projects/hermes-zh`
```text
M app/docs/[...slug]/page.tsx
 M app/layout.tsx
 M content-cache/generated/build-meta.json
 M content-cache/generated/search-index.json
 M public/content-assets/desktop-07-real-chat-v1.webp
 M public/content-assets/desktop-07-real-session-resume-v1.webp
 M public/content-assets/prepare-environment-01-choice-map-cards-v2.webp
 M public/content-assets/rm2-2-connect-terminal-01-local-vs-ssh-route.webp
 M public/content-assets/rm2-2-get-running-index-06-stage-map-closed.webp
 M public/content-assets/rm2-3-connect-platform-01-platform-connection-map.webp
 M public/content-assets/rm2-3-connect-platform-02-platform-config-ui.webp
 M public/content-assets/rm2-3-skills-curated-01-skill-scenario-map.webp
 M public/content-assets/rm2-3-slash-commands-01-command-groups.webp
 M public/content-assets/rm2-4-advanced-usage-index-01-single-agent-upgrade-map.webp
 M public/content-assets/rm2-4-custom-llm-01-model-routing-map.webp
 M public/content-assets/rm2-4-memory-01-memory-layer-map.webp
 M public/content-assets/rm2-4-skins-01-theme-comparison.webp
 M public/content-assets/rm2-4-soul-01-soul-structure-map.webp
 M public/content-assets/rm2-4-toolsets-01-toolset-map-v4.webp
 M public/content-assets/rm2-5-acp-ide-01-editor-workflow-map.webp
 M public/content-assets/rm2-5-context-files-01-long-term-rules-map.webp
 M public/content-assets/rm2-5-context-references-01-temporary-material-map.webp
 M public/content-assets/rm2-5-context-system-01-two-layer-map.webp
 M public/content-assets/rm2-5-cron-and-automation-01-scheduled-flow-map.webp
 M public/content-assets/rm2-5-mcp-and-plugins-01-main-route.webp
 M public/content-assets/rm2-5-memory-providers-01-overview-map.webp
 M public/content-assets/rm2-5-memory-providers-02-holographic-first-route.webp
 M public/content-assets/rm2-5-memory-providers-03-honcho-multi-agent-route.webp
 M public/content-assets/rm2-5-memory-providers-04-compare-decision-route.webp
 M public/content-assets/rm2-5-profiles-01-multi-profile-map.webp
 M public/content-assets/rm2-learning-path-gemini-final-v2.webp
 M public/fonts/noto-serif-sc.woff2
 M tests/performance/route-cache-headers.test.ts
 M tests/seo/canonical-slash.test.ts
 M vercel.json
fix/vercel-stoploss-r1-rework5-20260607
```

## 汇总
|metric|value|
|---|---|
|docs md/mdx files|120|
|image assets under docs/assets|175|
|referenced assets|110|
|unreferenced assets|65|
|ambiguous refs|47|
|missing refs|0|
|>300KB assets|129|
|Cloudflare top-path hit assets|0|

## Cloudflare 今日 Top paths
- 采集状态: `ok`
- 采集 proof JSON: `/opt/projects/awesome-hermes-agent-zh/artifacts/asset-inventory/cloudflare_top_paths_20260608.json`
- 注：仅用路径命中标记内容图片热度，不改变线上配置。

|rank|path|requests|bytes|
|---|---|---|---|
|-|-|-|-|

## 大文件优先级（>300KB，按大小降序）
|asset|KB|status|ref_count|referencing_docs|priority_flags|
|---|---|---|---|---|---|
|docs/assets/desktop-07-structure-v1.webp|2428.8|referenced|1|docs/01-从这开始/03-玩出花样/07-用桌面端操作 Hermes.md|>300KB, P1-large|
|docs/assets/rm2-4-profile-distribution-structure-v1.webp|2232.8|referenced|1|docs/01-从这开始/04-自己造东西/09-把一整套 Agent 打包分享.md|>300KB, P1-large|
|docs/assets/rm2-4-profile-distribution-operation-v1.webp|2088.6|referenced|1|docs/01-从这开始/04-自己造东西/09-把一整套 Agent 打包分享.md|>300KB, P1-large|
|docs/assets/desktop-07-real-chat-v1.webp|1873.6|referenced|1|docs/01-从这开始/03-玩出花样/07-用桌面端操作 Hermes.md|>300KB, P1-large|
|docs/assets/desktop-07-real-session-resume-v1.webp|1773.5|referenced|1|docs/01-从这开始/03-玩出花样/07-用桌面端操作 Hermes.md|>300KB, P1-large|
|docs/assets/desktop-07-real-project-picker-v1.webp|1605.6|referenced|1|docs/01-从这开始/03-玩出花样/07-用桌面端操作 Hermes.md|>300KB, P1-large|
|docs/assets/practical-v2-10-security-hardening.webp|1575.4|referenced|1|docs/01-从这开始/05-实战应用/16-安全加固.md|>300KB, P1-large|
|docs/assets/practical-v2-08-60-days-6-lessons.webp|1426.2|referenced|1|docs/01-从这开始/05-实战应用/20-60 天分析师工作流.md|>300KB, P1-large|
|docs/assets/practical-v2-02-ollama-local-model.webp|1387.4|referenced|1|docs/01-从这开始/05-实战应用/13-Ollama 本地模型.md|>300KB, P1-large|
|docs/assets/practical-v2-06-advanced-skills-mcp-subagents.webp|1361.3|referenced|1|docs/01-从这开始/05-实战应用/18-Hermes Agent 进阶实战.md|>300KB, P1-large|
|docs/assets/practical-v2-09-deep-dive-build-your-own.webp|1354.5|referenced|1|docs/01-从这开始/05-实战应用/22-Hermes Agent 深度拆解与自建指南.md|>300KB, P1-large|
|docs/assets/solution-multiplatform-output-bundle-v1.webp|1340.2|referenced|1|docs/02-现成方案/01-内容创作与发布/06-多平台内容改写助手.md|>300KB, P1-large|
|docs/assets/practical-v2-04-custom-skills.webp|1317.2|referenced|1|docs/01-从这开始/05-实战应用/15-自定义 Skills.md|>300KB, P1-large|
|docs/assets/practical-v2-03-ollama-fast-local-install.webp|1315.3|referenced|1|docs/01-从这开始/05-实战应用/21-Hermes Agent 与 Ollama 最快路径.md|>300KB, P1-large|
|docs/assets/desktop-07-operation-v1.webp|1307.9|unreferenced|0|-|>300KB, P1-large|
|docs/assets/practical-v2-05-github-pr-review.webp|1280.9|referenced|1|docs/01-从这开始/05-实战应用/14-GitHub PR 自动审查.md|>300KB, P1-large|
|docs/assets/practical-v2-01-discord-entry.webp|1256.8|referenced|1|docs/01-从这开始/05-实战应用/11-Discord 接入.md|>300KB, P1-large|
|docs/assets/practical-v2-07-control-room-specialist-teams.webp|1250.9|referenced|1|docs/01-从这开始/05-实战应用/19-Hermes Agent 控制室.md|>300KB, P1-large|
|docs/assets/solution-action-plan-output-map-v1.webp|1242.1|referenced|1|docs/02-现成方案/02-办公效率与知识整理/05-行动计划助手.md|>300KB, P1-large|
|docs/assets/solution-message-summary-output-map-v1.webp|1239.2|referenced|1|docs/02-现成方案/02-办公效率与知识整理/06-邮件群消息摘要助手.md|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-summary-cliacp-fixed-gemini-3-pro-image-preview.webp|1237.3|referenced|1|docs/02-现成方案/02-办公效率与知识整理/04-资料总结助手.md|>300KB, P1-large|
|docs/assets/solution-action-plan-standard-vs-lite-v1.webp|1234.9|referenced|1|docs/02-现成方案/02-办公效率与知识整理/05-行动计划助手.md|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-summary-compare-gemini-3-pro-image-preview.webp|1230.1|referenced|1|docs/02-现成方案/02-办公效率与知识整理/04-资料总结助手.md|>300KB, P1-large|
|docs/assets/solution-twitter-setup-chain-v1.webp|1212.8|referenced|1|docs/02-现成方案/01-内容创作与发布/05-X-Twitter 内容与互动助手.md|>300KB, P1-large|
|docs/assets/solution-multiplatform-solo-vs-batch-v1.webp|1204.4|referenced|1|docs/02-现成方案/01-内容创作与发布/06-多平台内容改写助手.md|>300KB, P1-large|
|docs/assets/solution-twitter-read-vs-actions-v1.webp|1203.6|referenced|1|docs/02-现成方案/01-内容创作与发布/05-X-Twitter 内容与互动助手.md|>300KB, P1-large|
|docs/assets/solution-message-summary-complete-vs-quick-v1.webp|1195.6|referenced|1|docs/02-现成方案/02-办公效率与知识整理/06-邮件群消息摘要助手.md|>300KB, P1-large|
|docs/assets/solution-meeting-output-map-v1.webp|1194.6|unreferenced|0|-|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-meeting-cliacp-gemini-3-pro-image-preview.webp|1187.1|referenced|1|docs/02-现成方案/02-办公效率与知识整理/02-会议纪要助手.md|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-meeting-compare-gemini-3-pro-image-preview.webp|1182.1|referenced|1|docs/02-现成方案/02-办公效率与知识整理/02-会议纪要助手.md|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-meeting-output-final-gemini-3-pro-image-preview.webp|1137.0|referenced|1|docs/02-现成方案/02-办公效率与知识整理/02-会议纪要助手.md|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-summary-output-gemini-3-pro-image-preview.webp|1126.2|referenced|1|docs/02-现成方案/02-办公效率与知识整理/04-资料总结助手.md|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-daily-output-gemini-3-pro-image-preview.webp|1103.9|referenced|1|docs/02-现成方案/02-办公效率与知识整理/03-项目日报助手.md|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-daily-cliacp-gemini-3-pro-image-preview.webp|1096.8|referenced|1|docs/02-现成方案/02-办公效率与知识整理/03-项目日报助手.md|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-daily-compare-ultrastrict-gemini-3-pro-image-preview.webp|1080.1|referenced|1|docs/02-现成方案/02-办公效率与知识整理/03-项目日报助手.md|>300KB, P1-large|
|docs/assets/practical-v2-11-voice-mode.webp|1019.5|referenced|1|docs/01-从这开始/05-实战应用/17-语音模式.md|>300KB, P1-large|
|docs/assets/solution-ppt-cli-vs-acp-review-candidate-02-lines.webp|991.0|referenced|1|docs/02-现成方案/01-内容创作与发布/04-PPT 助手.md|>300KB, P1-large|
|docs/assets/rm2-3-get-started-index-01-daily-usage-path.webp|970.4|referenced|1|docs/01-从这开始/02-开始上手/01-总览.md|>300KB, P1-large|
|docs/assets/solution-daily-output-map-v1.webp|966.9|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-practical-04-three-tier-model-routing-v1.webp|959.1|referenced|1|docs/01-从这开始/05-实战应用/04-月费8美金三层模型级联省钱指南.md|>300KB, P1-large|
|docs/assets/solution-practical-02-telegram-entry-map-v1.webp|951.1|referenced|1|docs/01-从这开始/05-实战应用/02-Telegram 消息入口接入.md|>300KB, P1-large|
|docs/assets/solution-practical-05-token-cost-stack-v1.webp|947.0|referenced|1|docs/01-从这开始/05-实战应用/05-Token 成本优化避坑指南.md|>300KB, P1-large|
|docs/assets/solution-summary-output-map-v1.webp|946.0|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-xhs-output-map-v1.webp|942.0|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-ppt-output-map-v1.webp|940.2|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-practical-07-soul-persona-layers-v1.webp|919.7|referenced|1|docs/01-从这开始/05-实战应用/07-SOUL.md 人格定制.md|>300KB, P1-large|
|docs/assets/solution-practical-06-vps-self-hosting-path-v1.webp|916.4|referenced|1|docs/01-从这开始/05-实战应用/06-VPS 自托管 Hermes.md|>300KB, P1-large|
|docs/assets/solution-practical-01-daily-briefing-flow-v1.webp|913.7|referenced|1|docs/01-从这开始/05-实战应用/01-用 Hermes 做每日晨间简报.md|>300KB, P1-large|
|docs/assets/solution-practical-09-kanban-multi-agent-orchestration-v1.webp|911.4|referenced|1|docs/01-从这开始/05-实战应用/09-Kanban 多 Agent 编排.md|>300KB, P1-large|
|docs/assets/solution-practical-03-github-backup-cron-v1.webp|893.1|referenced|1|docs/01-从这开始/05-实战应用/03-GitHub 备份 Cron Job.md|>300KB, P1-large|
|docs/assets/solution-summary-standard-vs-decision-v1.webp|890.0|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-gzh-output-map-v1.webp|875.4|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-practical-08-obsidian-second-brain-v1.webp|874.7|referenced|1|docs/01-从这开始/05-实战应用/08-Obsidian 第二大脑知识库.md|>300KB, P1-large|
|docs/assets/solution-daily-cli-vs-acp-v1.webp|874.6|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-daily-standard-vs-manager-v1.webp|867.2|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-meeting-standard-vs-action-v1.webp|826.1|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-gzh-cli-vs-acp-v1.webp|823.2|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-practical-10-home-assistant-control-loop-v1.webp|791.6|referenced|1|docs/01-从这开始/05-实战应用/10-Home Assistant 智能家居.md|>300KB, P1-large|
|docs/assets/solution-gzh-single-vs-series-v1.webp|772.9|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-summary-cli-vs-acp-v1.webp|750.6|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-ppt-structure-vs-script-v1.webp|730.5|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-miniapp-3-layer-map-v2.webp|661.5|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-ppt-structure-vs-script-review-candidate-07-integrated.webp|642.0|referenced|1|docs/02-现成方案/01-内容创作与发布/04-PPT 助手.md|>300KB, P1-large|
|docs/assets/solution-miniapp-3-layer-map-v5.webp|621.7|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-gzh-single-vs-series-v3-cliproxy-g31.webp|618.8|referenced|1|docs/02-现成方案/01-内容创作与发布/03-公众号写作助手.md|>300KB, P1-large|
|docs/assets/solution-miniapp-3-layer-map-v3.webp|617.2|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-miniapp-solo-vs-team-map-v4.webp|589.1|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-miniapp-team-handoff-proof.webp|585.9|referenced|1|docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md|>300KB, P1-large|
|docs/assets/solution-miniapp-solo-vs-team-map-zh-v1.webp|584.8|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-gzh-cli-vs-acp-v3-cliproxy-g31.webp|582.3|referenced|1|docs/02-现成方案/01-内容创作与发布/03-公众号写作助手.md|>300KB, P1-large|
|docs/assets/solution-xhs-output-map-v3-cliproxy-g31.webp|579.9|referenced|1|docs/02-现成方案/01-内容创作与发布/02-小红书内容助手.md|>300KB, P1-large|
|docs/assets/03-domestic-deploy-overview-map-v17.webp|577.4|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-miniapp-3-layer-map-v7.webp|574.6|referenced|1|docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md|>300KB, P1-large|
|docs/assets/solution-xhs-single-vs-series-v3-cliproxy-g31.webp|573.4|referenced|1|docs/02-现成方案/01-内容创作与发布/02-小红书内容助手.md|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v1.webp|572.9|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-miniapp-solo-vs-team-map-zh-v2.webp|568.1|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-webdev-3-layer-map-v1.webp|566.9|referenced|1|docs/02-现成方案/03-应用开发与快速原型/03-敏捷 Web 开发助手.md|>300KB, P1-large|
|docs/assets/solution-ppt-team-handoff-review-candidate-02.webp|552.5|referenced|1|docs/02-现成方案/01-内容创作与发布/04-PPT 助手.md|>300KB, P1-large|
|docs/assets/solution-webdev-solo-vs-team-map-v1.webp|551.8|referenced|1|docs/02-现成方案/03-应用开发与快速原型/03-敏捷 Web 开发助手.md|>300KB, P1-large|
|docs/assets/solution-miniapp-solo-real-run-proof.webp|540.3|referenced|1|docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md|>300KB, P1-large|
|docs/assets/solution-miniapp-solo-vs-team-map-zh-v6.webp|531.5|referenced|1|docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md|>300KB, P1-large|
|docs/assets/solution-miniapp-3-layer-map-v6.webp|525.0|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-v2.webp|524.1|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-miniapp-3-layer-map-v4.webp|515.5|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-webdev-cli-vs-acp-map-v1.webp|506.9|referenced|1|docs/02-现成方案/03-应用开发与快速原型/03-敏捷 Web 开发助手.md|>300KB, P1-large|
|docs/assets/solution-gzh-output-map-v3-cliproxy-g31.webp|505.5|referenced|1|docs/02-现成方案/01-内容创作与发布/03-公众号写作助手.md|>300KB, P1-large|
|docs/assets/rm2-3-slash-commands-02-session-save-resume.webp|503.4|referenced|1|docs/01-从这开始/02-开始上手/03-常用斜杠命令与会话管理.md|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v2.webp|498.7|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-ppt-structure-vs-script-v3-cliproxy-g31.webp|498.4|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v10.webp|493.2|referenced|1|docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md|>300KB, P1-large|
|docs/assets/prepare-environment-01-choice-map-cards-v2.webp|488.7|referenced|1|docs/01-从这开始/01-先跑起来/02-先准备运行环境.md|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v5.webp|484.8|unreferenced|0|-|>300KB, P1-large|
|docs/assets/rm2-3-slash-commands-03-persona-command-success.webp|467.1|referenced|1|docs/01-从这开始/02-开始上手/03-常用斜杠命令与会话管理.md|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v3.webp|461.2|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-xhs-cli-vs-acp-v3-cliproxy-g31.webp|454.1|referenced|1|docs/02-现成方案/01-内容创作与发布/02-小红书内容助手.md|>300KB, P1-large|
|docs/assets/03-aliyun-hermes-remote-login.webp|439.5|unreferenced|0|-|>300KB, P1-large|
|docs/assets/practical-11-discord-official-screenshot-zh-v1.webp|434.4|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-miniapp-solo-vs-team-map-zh-v5.webp|428.9|unreferenced|0|-|>300KB, P1-large|
|docs/assets/practical-12-mcp-official-screenshot-zh-v1.webp|411.1|referenced|1|docs/01-从这开始/05-实战应用/12-MCP 接入指南.md|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v9.webp|404.3|unreferenced|0|-|>300KB, P1-large|
|docs/assets/03-aliyun-hermes-dangerous-command.webp|399.7|unreferenced|0|-|>300KB, P1-large|
|docs/assets/practical-18-security-official-screenshot-zh-v1.webp|399.7|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-ppt-output-map-review-pass-01.webp|399.1|unreferenced|0|-|>300KB, P1-large|
|docs/assets/rm2-3-skills-curated-01-skill-scenario-map.webp|390.4|referenced|1|docs/01-从这开始/02-开始上手/04-常用 Skills（按日常使用场景精选）.md|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v8.webp|387.5|unreferenced|0|-|>300KB, P1-large|
|docs/assets/03-domestic-deploy-overview-map-v6.webp|382.9|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v7.webp|381.4|unreferenced|0|-|>300KB, P1-large|
|docs/assets/rm2-5-profiles-01-multi-profile-map.webp|380.9|referenced|1|docs/01-从这开始/04-自己造东西/02-多个助手一起工作.md|>300KB, P1-large|
|docs/assets/practical-19-voice-mode-official-screenshot-zh-v1.webp|380.6|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-miniapp-solo-vs-team-map-zh-v3.webp|376.6|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v6.webp|376.0|unreferenced|0|-|>300KB, P1-large|
|docs/assets/practical-14-github-pr-review-official-screenshot-zh-v1.webp|372.8|unreferenced|0|-|>300KB, P1-large|
|docs/assets/03-aliyun-hermes-instance-list.webp|371.7|unreferenced|0|-|>300KB, P1-large|
|docs/assets/03-domestic-deploy-overview-map-v8.webp|370.3|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-miniapp-solo-followup-proof.webp|364.4|referenced|1|docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v4.webp|355.5|unreferenced|0|-|>300KB, P1-large|
|docs/assets/solution-miniapp-solo-vs-team-map-zh-v4.webp|353.1|unreferenced|0|-|>300KB, P1-large|
|docs/assets/rm2-3-slash-commands-01-command-groups.webp|352.3|referenced|1|docs/01-从这开始/02-开始上手/03-常用斜杠命令与会话管理.md|>300KB, P1-large|
|docs/assets/rm2-4-advanced-usage-index-01-single-agent-upgrade-map.webp|348.9|referenced|1|docs/01-从这开始/03-玩出花样/01-总览.md|>300KB, P1-large|
|docs/assets/practical-13-ollama-official-screenshot-zh-v1.webp|342.2|unreferenced|0|-|>300KB, P1-large|
|docs/assets/rm2-3-connect-platform-03-first-message-success-v3.webp|341.6|referenced|1|docs/01-从这开始/02-开始上手/05-接入一个消息平台（推荐飞书）.md|>300KB, P1-large|
|docs/assets/rm2-5-api-server-01-openai-compatible-backend-map.webp|341.5|unreferenced|0|-|>300KB, P1-large|
|docs/assets/rm2-2-connect-terminal-01-local-vs-ssh-route.webp|339.8|referenced|1|docs/01-从这开始/01-先跑起来/03-进入终端并连接服务器.md|>300KB, P1-large|
|docs/assets/rm2-4-skins-01-theme-comparison.webp|334.2|referenced|1|docs/01-从这开始/03-玩出花样/06-让终端更顺眼.md|>300KB, P1-large|
|docs/assets/solution-xhs-single-vs-series-v1.webp|333.8|unreferenced|0|-|>300KB, P1-large|
|docs/assets/03-aliyun-hermes-terminal-start.webp|329.5|unreferenced|0|-|>300KB, P1-large|
|docs/assets/rm2-4-soul-01-soul-structure-map.webp|329.5|referenced|1|docs/01-从这开始/03-玩出花样/02-让 Hermes 更像你.md|>300KB, P1-large|
|docs/assets/solution-meeting-cli-vs-acp-v1.webp|308.3|unreferenced|0|-|>300KB, P1-large|
|docs/assets/rm2-4-toolsets-01-toolset-map-v4.webp|300.8|referenced|1|docs/01-从这开始/03-玩出花样/05-让工具更顺手.md|>300KB, P1-large|

## Cloudflare Top paths 命中的内容图片
|asset|public_path|KB|status|ref_count|cf_requests|cf_bytes|
|---|---|---|---|---|---|---|
|-|-|-|-|-|-|-|

## Top 50 图片资产（按大小）
|asset|KB|status|ref_count|dimensions|format|priority_flags|
|---|---|---|---|---|---|---|
|docs/assets/desktop-07-structure-v1.webp|2428.8|referenced|1|2560x1440|PNG|>300KB, P1-large|
|docs/assets/rm2-4-profile-distribution-structure-v1.webp|2232.8|referenced|1|2560x1440|PNG|>300KB, P1-large|
|docs/assets/rm2-4-profile-distribution-operation-v1.webp|2088.6|referenced|1|2560x1440|PNG|>300KB, P1-large|
|docs/assets/desktop-07-real-chat-v1.webp|1873.6|referenced|1|2560x1440|PNG|>300KB, P1-large|
|docs/assets/desktop-07-real-session-resume-v1.webp|1773.5|referenced|1|2560x1440|PNG|>300KB, P1-large|
|docs/assets/desktop-07-real-project-picker-v1.webp|1605.6|referenced|1|2560x1440|PNG|>300KB, P1-large|
|docs/assets/practical-v2-10-security-hardening.webp|1575.4|referenced|1|1600x900|PNG|>300KB, P1-large|
|docs/assets/practical-v2-08-60-days-6-lessons.webp|1426.2|referenced|1|1600x900|PNG|>300KB, P1-large|
|docs/assets/practical-v2-02-ollama-local-model.webp|1387.4|referenced|1|1600x900|PNG|>300KB, P1-large|
|docs/assets/practical-v2-06-advanced-skills-mcp-subagents.webp|1361.3|referenced|1|1600x900|PNG|>300KB, P1-large|
|docs/assets/practical-v2-09-deep-dive-build-your-own.webp|1354.5|referenced|1|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-multiplatform-output-bundle-v1.webp|1340.2|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/practical-v2-04-custom-skills.webp|1317.2|referenced|1|1600x900|PNG|>300KB, P1-large|
|docs/assets/practical-v2-03-ollama-fast-local-install.webp|1315.3|referenced|1|1600x900|PNG|>300KB, P1-large|
|docs/assets/desktop-07-operation-v1.webp|1307.9|unreferenced|0|2560x1440|PNG|>300KB, P1-large|
|docs/assets/practical-v2-05-github-pr-review.webp|1280.9|referenced|1|1600x900|PNG|>300KB, P1-large|
|docs/assets/practical-v2-01-discord-entry.webp|1256.8|referenced|1|1600x900|PNG|>300KB, P1-large|
|docs/assets/practical-v2-07-control-room-specialist-teams.webp|1250.9|referenced|1|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-action-plan-output-map-v1.webp|1242.1|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/solution-message-summary-output-map-v1.webp|1239.2|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-summary-cliacp-fixed-gemini-3-pro-image-preview.webp|1237.3|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/solution-action-plan-standard-vs-lite-v1.webp|1234.9|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-summary-compare-gemini-3-pro-image-preview.webp|1230.1|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/solution-twitter-setup-chain-v1.webp|1212.8|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/solution-multiplatform-solo-vs-batch-v1.webp|1204.4|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/solution-twitter-read-vs-actions-v1.webp|1203.6|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/solution-message-summary-complete-vs-quick-v1.webp|1195.6|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/solution-meeting-output-map-v1.webp|1194.6|unreferenced|0|1600x900|PNG|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-meeting-cliacp-gemini-3-pro-image-preview.webp|1187.1|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-meeting-compare-gemini-3-pro-image-preview.webp|1182.1|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-meeting-output-final-gemini-3-pro-image-preview.webp|1137.0|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-summary-output-gemini-3-pro-image-preview.webp|1126.2|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-daily-output-gemini-3-pro-image-preview.webp|1103.9|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-daily-cliacp-gemini-3-pro-image-preview.webp|1096.8|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/office-integrated-final-v1/office-daily-compare-ultrastrict-gemini-3-pro-image-preview.webp|1080.1|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/practical-v2-11-voice-mode.webp|1019.5|referenced|1|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-ppt-cli-vs-acp-review-candidate-02-lines.webp|991.0|referenced|1|1408x768|PNG|>300KB, P1-large|
|docs/assets/rm2-3-get-started-index-01-daily-usage-path.webp|970.4|referenced|1|1376x768|PNG|>300KB, P1-large|
|docs/assets/solution-daily-output-map-v1.webp|966.9|unreferenced|0|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-practical-04-three-tier-model-routing-v1.webp|959.1|referenced|1|1360x765|PNG|>300KB, P1-large|
|docs/assets/solution-practical-02-telegram-entry-map-v1.webp|951.1|referenced|1|1360x765|PNG|>300KB, P1-large|
|docs/assets/solution-practical-05-token-cost-stack-v1.webp|947.0|referenced|1|1360x765|PNG|>300KB, P1-large|
|docs/assets/solution-summary-output-map-v1.webp|946.0|unreferenced|0|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-xhs-output-map-v1.webp|942.0|unreferenced|0|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-ppt-output-map-v1.webp|940.2|unreferenced|0|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-practical-07-soul-persona-layers-v1.webp|919.7|referenced|1|1360x765|PNG|>300KB, P1-large|
|docs/assets/solution-practical-06-vps-self-hosting-path-v1.webp|916.4|referenced|1|1360x765|PNG|>300KB, P1-large|
|docs/assets/solution-practical-01-daily-briefing-flow-v1.webp|913.7|referenced|1|1360x765|PNG|>300KB, P1-large|
|docs/assets/solution-practical-09-kanban-multi-agent-orchestration-v1.webp|911.4|referenced|1|1360x765|PNG|>300KB, P1-large|
|docs/assets/solution-practical-03-github-backup-cron-v1.webp|893.1|referenced|1|1360x765|PNG|>300KB, P1-large|

## Referenced 清单（按大小）
|asset|KB|ref_count|referencing_docs|
|---|---|---|---|
|docs/assets/desktop-07-structure-v1.webp|2428.8|1|docs/01-从这开始/03-玩出花样/07-用桌面端操作 Hermes.md|
|docs/assets/rm2-4-profile-distribution-structure-v1.webp|2232.8|1|docs/01-从这开始/04-自己造东西/09-把一整套 Agent 打包分享.md|
|docs/assets/rm2-4-profile-distribution-operation-v1.webp|2088.6|1|docs/01-从这开始/04-自己造东西/09-把一整套 Agent 打包分享.md|
|docs/assets/desktop-07-real-chat-v1.webp|1873.6|1|docs/01-从这开始/03-玩出花样/07-用桌面端操作 Hermes.md|
|docs/assets/desktop-07-real-session-resume-v1.webp|1773.5|1|docs/01-从这开始/03-玩出花样/07-用桌面端操作 Hermes.md|
|docs/assets/desktop-07-real-project-picker-v1.webp|1605.6|1|docs/01-从这开始/03-玩出花样/07-用桌面端操作 Hermes.md|
|docs/assets/practical-v2-10-security-hardening.webp|1575.4|1|docs/01-从这开始/05-实战应用/16-安全加固.md|
|docs/assets/practical-v2-08-60-days-6-lessons.webp|1426.2|1|docs/01-从这开始/05-实战应用/20-60 天分析师工作流.md|
|docs/assets/practical-v2-02-ollama-local-model.webp|1387.4|1|docs/01-从这开始/05-实战应用/13-Ollama 本地模型.md|
|docs/assets/practical-v2-06-advanced-skills-mcp-subagents.webp|1361.3|1|docs/01-从这开始/05-实战应用/18-Hermes Agent 进阶实战.md|
|docs/assets/practical-v2-09-deep-dive-build-your-own.webp|1354.5|1|docs/01-从这开始/05-实战应用/22-Hermes Agent 深度拆解与自建指南.md|
|docs/assets/solution-multiplatform-output-bundle-v1.webp|1340.2|1|docs/02-现成方案/01-内容创作与发布/06-多平台内容改写助手.md|
|docs/assets/practical-v2-04-custom-skills.webp|1317.2|1|docs/01-从这开始/05-实战应用/15-自定义 Skills.md|
|docs/assets/practical-v2-03-ollama-fast-local-install.webp|1315.3|1|docs/01-从这开始/05-实战应用/21-Hermes Agent 与 Ollama 最快路径.md|
|docs/assets/practical-v2-05-github-pr-review.webp|1280.9|1|docs/01-从这开始/05-实战应用/14-GitHub PR 自动审查.md|
|docs/assets/practical-v2-01-discord-entry.webp|1256.8|1|docs/01-从这开始/05-实战应用/11-Discord 接入.md|
|docs/assets/practical-v2-07-control-room-specialist-teams.webp|1250.9|1|docs/01-从这开始/05-实战应用/19-Hermes Agent 控制室.md|
|docs/assets/solution-action-plan-output-map-v1.webp|1242.1|1|docs/02-现成方案/02-办公效率与知识整理/05-行动计划助手.md|
|docs/assets/solution-message-summary-output-map-v1.webp|1239.2|1|docs/02-现成方案/02-办公效率与知识整理/06-邮件群消息摘要助手.md|
|docs/assets/office-integrated-final-v1/office-summary-cliacp-fixed-gemini-3-pro-image-preview.webp|1237.3|1|docs/02-现成方案/02-办公效率与知识整理/04-资料总结助手.md|
|docs/assets/solution-action-plan-standard-vs-lite-v1.webp|1234.9|1|docs/02-现成方案/02-办公效率与知识整理/05-行动计划助手.md|
|docs/assets/office-integrated-final-v1/office-summary-compare-gemini-3-pro-image-preview.webp|1230.1|1|docs/02-现成方案/02-办公效率与知识整理/04-资料总结助手.md|
|docs/assets/solution-twitter-setup-chain-v1.webp|1212.8|1|docs/02-现成方案/01-内容创作与发布/05-X-Twitter 内容与互动助手.md|
|docs/assets/solution-multiplatform-solo-vs-batch-v1.webp|1204.4|1|docs/02-现成方案/01-内容创作与发布/06-多平台内容改写助手.md|
|docs/assets/solution-twitter-read-vs-actions-v1.webp|1203.6|1|docs/02-现成方案/01-内容创作与发布/05-X-Twitter 内容与互动助手.md|
|docs/assets/solution-message-summary-complete-vs-quick-v1.webp|1195.6|1|docs/02-现成方案/02-办公效率与知识整理/06-邮件群消息摘要助手.md|
|docs/assets/office-integrated-final-v1/office-meeting-cliacp-gemini-3-pro-image-preview.webp|1187.1|1|docs/02-现成方案/02-办公效率与知识整理/02-会议纪要助手.md|
|docs/assets/office-integrated-final-v1/office-meeting-compare-gemini-3-pro-image-preview.webp|1182.1|1|docs/02-现成方案/02-办公效率与知识整理/02-会议纪要助手.md|
|docs/assets/office-integrated-final-v1/office-meeting-output-final-gemini-3-pro-image-preview.webp|1137.0|1|docs/02-现成方案/02-办公效率与知识整理/02-会议纪要助手.md|
|docs/assets/office-integrated-final-v1/office-summary-output-gemini-3-pro-image-preview.webp|1126.2|1|docs/02-现成方案/02-办公效率与知识整理/04-资料总结助手.md|
|docs/assets/office-integrated-final-v1/office-daily-output-gemini-3-pro-image-preview.webp|1103.9|1|docs/02-现成方案/02-办公效率与知识整理/03-项目日报助手.md|
|docs/assets/office-integrated-final-v1/office-daily-cliacp-gemini-3-pro-image-preview.webp|1096.8|1|docs/02-现成方案/02-办公效率与知识整理/03-项目日报助手.md|
|docs/assets/office-integrated-final-v1/office-daily-compare-ultrastrict-gemini-3-pro-image-preview.webp|1080.1|1|docs/02-现成方案/02-办公效率与知识整理/03-项目日报助手.md|
|docs/assets/practical-v2-11-voice-mode.webp|1019.5|1|docs/01-从这开始/05-实战应用/17-语音模式.md|
|docs/assets/solution-ppt-cli-vs-acp-review-candidate-02-lines.webp|991.0|1|docs/02-现成方案/01-内容创作与发布/04-PPT 助手.md|
|docs/assets/rm2-3-get-started-index-01-daily-usage-path.webp|970.4|1|docs/01-从这开始/02-开始上手/01-总览.md|
|docs/assets/solution-practical-04-three-tier-model-routing-v1.webp|959.1|1|docs/01-从这开始/05-实战应用/04-月费8美金三层模型级联省钱指南.md|
|docs/assets/solution-practical-02-telegram-entry-map-v1.webp|951.1|1|docs/01-从这开始/05-实战应用/02-Telegram 消息入口接入.md|
|docs/assets/solution-practical-05-token-cost-stack-v1.webp|947.0|1|docs/01-从这开始/05-实战应用/05-Token 成本优化避坑指南.md|
|docs/assets/solution-practical-07-soul-persona-layers-v1.webp|919.7|1|docs/01-从这开始/05-实战应用/07-SOUL.md 人格定制.md|
|docs/assets/solution-practical-06-vps-self-hosting-path-v1.webp|916.4|1|docs/01-从这开始/05-实战应用/06-VPS 自托管 Hermes.md|
|docs/assets/solution-practical-01-daily-briefing-flow-v1.webp|913.7|1|docs/01-从这开始/05-实战应用/01-用 Hermes 做每日晨间简报.md|
|docs/assets/solution-practical-09-kanban-multi-agent-orchestration-v1.webp|911.4|1|docs/01-从这开始/05-实战应用/09-Kanban 多 Agent 编排.md|
|docs/assets/solution-practical-03-github-backup-cron-v1.webp|893.1|1|docs/01-从这开始/05-实战应用/03-GitHub 备份 Cron Job.md|
|docs/assets/solution-practical-08-obsidian-second-brain-v1.webp|874.7|1|docs/01-从这开始/05-实战应用/08-Obsidian 第二大脑知识库.md|
|docs/assets/solution-practical-10-home-assistant-control-loop-v1.webp|791.6|1|docs/01-从这开始/05-实战应用/10-Home Assistant 智能家居.md|
|docs/assets/solution-ppt-structure-vs-script-review-candidate-07-integrated.webp|642.0|1|docs/02-现成方案/01-内容创作与发布/04-PPT 助手.md|
|docs/assets/solution-gzh-single-vs-series-v3-cliproxy-g31.webp|618.8|1|docs/02-现成方案/01-内容创作与发布/03-公众号写作助手.md|
|docs/assets/solution-miniapp-team-handoff-proof.webp|585.9|1|docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md|
|docs/assets/solution-gzh-cli-vs-acp-v3-cliproxy-g31.webp|582.3|1|docs/02-现成方案/01-内容创作与发布/03-公众号写作助手.md|
|docs/assets/solution-xhs-output-map-v3-cliproxy-g31.webp|579.9|1|docs/02-现成方案/01-内容创作与发布/02-小红书内容助手.md|
|docs/assets/solution-miniapp-3-layer-map-v7.webp|574.6|1|docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md|
|docs/assets/solution-xhs-single-vs-series-v3-cliproxy-g31.webp|573.4|1|docs/02-现成方案/01-内容创作与发布/02-小红书内容助手.md|
|docs/assets/solution-webdev-3-layer-map-v1.webp|566.9|1|docs/02-现成方案/03-应用开发与快速原型/03-敏捷 Web 开发助手.md|
|docs/assets/solution-ppt-team-handoff-review-candidate-02.webp|552.5|1|docs/02-现成方案/01-内容创作与发布/04-PPT 助手.md|
|docs/assets/solution-webdev-solo-vs-team-map-v1.webp|551.8|1|docs/02-现成方案/03-应用开发与快速原型/03-敏捷 Web 开发助手.md|
|docs/assets/solution-miniapp-solo-real-run-proof.webp|540.3|1|docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md|
|docs/assets/solution-miniapp-solo-vs-team-map-zh-v6.webp|531.5|1|docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md|
|docs/assets/solution-webdev-cli-vs-acp-map-v1.webp|506.9|1|docs/02-现成方案/03-应用开发与快速原型/03-敏捷 Web 开发助手.md|
|docs/assets/solution-gzh-output-map-v3-cliproxy-g31.webp|505.5|1|docs/02-现成方案/01-内容创作与发布/03-公众号写作助手.md|
|docs/assets/rm2-3-slash-commands-02-session-save-resume.webp|503.4|1|docs/01-从这开始/02-开始上手/03-常用斜杠命令与会话管理.md|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v10.webp|493.2|1|docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md|
|docs/assets/prepare-environment-01-choice-map-cards-v2.webp|488.7|1|docs/01-从这开始/01-先跑起来/02-先准备运行环境.md|
|docs/assets/rm2-3-slash-commands-03-persona-command-success.webp|467.1|1|docs/01-从这开始/02-开始上手/03-常用斜杠命令与会话管理.md|
|docs/assets/solution-xhs-cli-vs-acp-v3-cliproxy-g31.webp|454.1|1|docs/02-现成方案/01-内容创作与发布/02-小红书内容助手.md|
|docs/assets/practical-12-mcp-official-screenshot-zh-v1.webp|411.1|1|docs/01-从这开始/05-实战应用/12-MCP 接入指南.md|
|docs/assets/rm2-3-skills-curated-01-skill-scenario-map.webp|390.4|1|docs/01-从这开始/02-开始上手/04-常用 Skills（按日常使用场景精选）.md|
|docs/assets/rm2-5-profiles-01-multi-profile-map.webp|380.9|1|docs/01-从这开始/04-自己造东西/02-多个助手一起工作.md|
|docs/assets/solution-miniapp-solo-followup-proof.webp|364.4|1|docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md|
|docs/assets/rm2-3-slash-commands-01-command-groups.webp|352.3|1|docs/01-从这开始/02-开始上手/03-常用斜杠命令与会话管理.md|
|docs/assets/rm2-4-advanced-usage-index-01-single-agent-upgrade-map.webp|348.9|1|docs/01-从这开始/03-玩出花样/01-总览.md|
|docs/assets/rm2-3-connect-platform-03-first-message-success-v3.webp|341.6|1|docs/01-从这开始/02-开始上手/05-接入一个消息平台（推荐飞书）.md|
|docs/assets/rm2-2-connect-terminal-01-local-vs-ssh-route.webp|339.8|1|docs/01-从这开始/01-先跑起来/03-进入终端并连接服务器.md|
|docs/assets/rm2-4-skins-01-theme-comparison.webp|334.2|1|docs/01-从这开始/03-玩出花样/06-让终端更顺眼.md|
|docs/assets/rm2-4-soul-01-soul-structure-map.webp|329.5|1|docs/01-从这开始/03-玩出花样/02-让 Hermes 更像你.md|
|docs/assets/rm2-4-toolsets-01-toolset-map-v4.webp|300.8|1|docs/01-从这开始/03-玩出花样/05-让工具更顺手.md|
|docs/assets/rm2-5-mcp-and-plugins-01-main-route.webp|286.7|1|docs/01-从这开始/04-自己造东西/05-把 Hermes 接进外部系统.md|
|docs/assets/rm2-2-get-running-index-06-stage-map-closed.webp|286.0|1|docs/01-从这开始/01-先跑起来/01-总览.md|
|docs/assets/rm2-5-context-references-01-temporary-material-map.webp|279.6|1|docs/01-从这开始/04-自己造东西/04-上下文系统/03-上下文引用.md|
|docs/assets/rm2-5-context-system-01-two-layer-map.webp|278.9|1|docs/01-从这开始/04-自己造东西/04-上下文系统/01-总览.md|
|docs/assets/rm2-5-api-server-01-openai-compatible-backend-map-v5.webp|273.6|1|docs/01-从这开始/04-自己造东西/06-把 Hermes 暴露成后端服务.md|
|docs/assets/rm2-5-cron-and-automation-01-scheduled-flow-map.webp|268.5|1|docs/01-从这开始/04-自己造东西/07-让 Hermes 自己自动跑.md|
|docs/assets/rm2-5-context-files-01-long-term-rules-map.webp|267.8|1|docs/01-从这开始/04-自己造东西/04-上下文系统/02-上下文文件.md|
|docs/assets/rm2-4-memory-01-memory-layer-map.webp|265.3|1|docs/01-从这开始/03-玩出花样/03-让 Hermes 记住你.md|
|docs/assets/rm2-5-acp-ide-01-editor-workflow-map.webp|265.2|1|docs/01-从这开始/04-自己造东西/08-放进编辑器里用.md|
|docs/assets/rm2-4-custom-llm-01-model-routing-map.webp|263.3|1|docs/01-从这开始/03-玩出花样/04-自定义 AI 大模型.md|
|docs/assets/rm2-5-memory-providers-03-honcho-multi-agent-route.webp|260.1|1|docs/01-从这开始/04-自己造东西/03-接入外部记忆系统/03-Honcho记忆.md|
|docs/assets/rm2-5-build-your-own-index-01-system-capability-map-v3.webp|258.2|1|docs/01-从这开始/04-自己造东西/01-总览.md|
|docs/assets/rm2-3-connect-platform-01-platform-connection-map.webp|244.9|1|docs/01-从这开始/02-开始上手/05-接入一个消息平台（推荐飞书）.md|
|docs/assets/rm2-5-memory-providers-02-holographic-first-route.webp|242.8|1|docs/01-从这开始/04-自己造东西/03-接入外部记忆系统/02-Holographic记忆.md|
|docs/assets/rm2-5-memory-providers-01-overview-map.webp|238.8|1|docs/01-从这开始/04-自己造东西/03-接入外部记忆系统/01-总览.md|
|docs/assets/rm2-5-memory-providers-04-compare-decision-route.webp|236.9|1|docs/01-从这开始/04-自己造东西/03-接入外部记忆系统/04-外部记忆对比.md|
|docs/assets/rm2-3-connect-platform-02-platform-config-ui.webp|225.9|1|docs/01-从这开始/02-开始上手/05-接入一个消息平台（推荐飞书）.md|
|docs/assets/rm2-4-custom-llm-02-provider-config-success.webp|195.2|1|docs/01-从这开始/03-玩出花样/04-自定义 AI 大模型.md|
|docs/assets/solution-ppt-output-map-review-candidate-09-cn-teamstyle.webp|168.4|1|docs/02-现成方案/01-内容创作与发布/04-PPT 助手.md|
|docs/assets/rm2-4-custom-llm-03-custom-model-success.webp|136.8|1|docs/01-从这开始/03-玩出花样/04-自定义 AI 大模型.md|
|docs/assets/rm2-3-skills-curated-02-skill-call-success.webp|136.7|1|docs/01-从这开始/02-开始上手/04-常用 Skills（按日常使用场景精选）.md|
|docs/assets/rm2-2-install-hermes-02-version-and-doctor-success.webp|131.4|1|docs/01-从这开始/01-先跑起来/04-把 Hermes 装上去.md|
|docs/assets/rm2-4-skins-02-theme-switch-success.webp|126.2|1|docs/01-从这开始/03-玩出花样/06-让终端更顺眼.md|
|docs/assets/rm2-4-toolsets-02-tools-toggle-success.webp|120.8|1|docs/01-从这开始/03-玩出花样/05-让工具更顺手.md|
|docs/assets/rm2-learning-path-gemini-final-v2.webp|115.4|1|docs/01-从这开始/总览.md|
|docs/assets/rm2-4-soul-02-soul-behavior-diff.webp|90.6|2|docs/01-从这开始/03-玩出花样/02-让 Hermes 更像你.md<br>docs/01-从这开始/05-实战应用/07-SOUL.md 人格定制.md|
|docs/assets/rm2-4-toolsets-03-debug-safe-flow.webp|86.8|1|docs/01-从这开始/03-玩出花样/05-让工具更顺手.md|
|docs/assets/rm2-2-install-hermes-01-install-command-running.webp|82.7|1|docs/01-从这开始/01-先跑起来/04-把 Hermes 装上去.md|
|docs/assets/rm2-2-first-hello-01-model-setup-success.webp|54.3|1|docs/01-从这开始/01-先跑起来/05-配好 AI 大模型并完成第一次互动.md|
|docs/assets/rm2-3-basic-usage-02-basic-chat-flow-success.webp|51.2|1|docs/01-从这开始/02-开始上手/02-认识 Hermes 的基本使用方式.md|
|docs/assets/rm2-2-first-hello-02-first-reply-success.webp|38.6|1|docs/01-从这开始/01-先跑起来/05-配好 AI 大模型并完成第一次互动.md|
|docs/assets/rm2-2-connect-terminal-02-ssh-login-success.webp|36.4|1|docs/01-从这开始/01-先跑起来/03-进入终端并连接服务器.md|
|docs/assets/rm2-3-basic-usage-01-cli-main-surface.webp|34.6|1|docs/01-从这开始/02-开始上手/02-认识 Hermes 的基本使用方式.md|
|docs/assets/rm2-2-connect-terminal-03-ssh-git-success.webp|28.8|1|docs/01-从这开始/01-先跑起来/03-进入终端并连接服务器.md|

## Unreferenced 清单（按大小）
|asset|KB|dimensions|format|priority_flags|
|---|---|---|---|---|
|docs/assets/desktop-07-operation-v1.webp|1307.9|2560x1440|PNG|>300KB, P1-large|
|docs/assets/solution-meeting-output-map-v1.webp|1194.6|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-daily-output-map-v1.webp|966.9|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-summary-output-map-v1.webp|946.0|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-xhs-output-map-v1.webp|942.0|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-ppt-output-map-v1.webp|940.2|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-summary-standard-vs-decision-v1.webp|890.0|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-gzh-output-map-v1.webp|875.4|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-daily-cli-vs-acp-v1.webp|874.6|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-daily-standard-vs-manager-v1.webp|867.2|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-meeting-standard-vs-action-v1.webp|826.1|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-gzh-cli-vs-acp-v1.webp|823.2|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-gzh-single-vs-series-v1.webp|772.9|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-summary-cli-vs-acp-v1.webp|750.6|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-ppt-structure-vs-script-v1.webp|730.5|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-miniapp-3-layer-map-v2.webp|661.5|1376x768|JPEG|>300KB, P1-large|
|docs/assets/solution-miniapp-3-layer-map-v5.webp|621.7|1376x768|JPEG|>300KB, P1-large|
|docs/assets/solution-miniapp-3-layer-map-v3.webp|617.2|1376x768|JPEG|>300KB, P1-large|
|docs/assets/solution-miniapp-solo-vs-team-map-v4.webp|589.1|1376x768|JPEG|>300KB, P1-large|
|docs/assets/solution-miniapp-solo-vs-team-map-zh-v1.webp|584.8|1376x768|JPEG|>300KB, P1-large|
|docs/assets/03-domestic-deploy-overview-map-v17.webp|577.4|1280x720|PNG|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v1.webp|572.9|1376x768|JPEG|>300KB, P1-large|
|docs/assets/solution-miniapp-solo-vs-team-map-zh-v2.webp|568.1|1376x768|JPEG|>300KB, P1-large|
|docs/assets/solution-miniapp-3-layer-map-v6.webp|525.0|1376x768|JPEG|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-v2.webp|524.1|1376x768|JPEG|>300KB, P1-large|
|docs/assets/solution-miniapp-3-layer-map-v4.webp|515.5|1376x768|JPEG|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v2.webp|498.7|1376x768|JPEG|>300KB, P1-large|
|docs/assets/solution-ppt-structure-vs-script-v3-cliproxy-g31.webp|498.4|1376x768|JPEG|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v5.webp|484.8|1376x768|JPEG|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v3.webp|461.2|1376x768|JPEG|>300KB, P1-large|
|docs/assets/03-aliyun-hermes-remote-login.webp|439.5|834x456|PNG|>300KB, P1-large|
|docs/assets/practical-11-discord-official-screenshot-zh-v1.webp|434.4|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-miniapp-solo-vs-team-map-zh-v5.webp|428.9|1376x768|JPEG|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v9.webp|404.3|1376x768|JPEG|>300KB, P1-large|
|docs/assets/03-aliyun-hermes-dangerous-command.webp|399.7|2660x326|PNG|>300KB, P1-large|
|docs/assets/practical-18-security-official-screenshot-zh-v1.webp|399.7|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-ppt-output-map-review-pass-01.webp|399.1|1408x768|JPEG|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v8.webp|387.5|1376x768|JPEG|>300KB, P1-large|
|docs/assets/03-domestic-deploy-overview-map-v6.webp|382.9|2752x1536|PNG|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v7.webp|381.4|1376x768|JPEG|>300KB, P1-large|
|docs/assets/practical-19-voice-mode-official-screenshot-zh-v1.webp|380.6|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-miniapp-solo-vs-team-map-zh-v3.webp|376.6|1376x768|JPEG|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v6.webp|376.0|1376x768|JPEG|>300KB, P1-large|
|docs/assets/practical-14-github-pr-review-official-screenshot-zh-v1.webp|372.8|1600x900|PNG|>300KB, P1-large|
|docs/assets/03-aliyun-hermes-instance-list.webp|371.7|2348x606|PNG|>300KB, P1-large|
|docs/assets/03-domestic-deploy-overview-map-v8.webp|370.3|2752x1536|PNG|>300KB, P1-large|
|docs/assets/solution-miniapp-cli-vs-acp-map-zh-v4.webp|355.5|1376x768|JPEG|>300KB, P1-large|
|docs/assets/solution-miniapp-solo-vs-team-map-zh-v4.webp|353.1|1376x768|JPEG|>300KB, P1-large|
|docs/assets/practical-13-ollama-official-screenshot-zh-v1.webp|342.2|1600x900|PNG|>300KB, P1-large|
|docs/assets/rm2-5-api-server-01-openai-compatible-backend-map.webp|341.5|2752x1536|PNG|>300KB, P1-large|
|docs/assets/solution-xhs-single-vs-series-v1.webp|333.8|1600x900|PNG|>300KB, P1-large|
|docs/assets/03-aliyun-hermes-terminal-start.webp|329.5|2732x250|PNG|>300KB, P1-large|
|docs/assets/solution-meeting-cli-vs-acp-v1.webp|308.3|1600x900|PNG|>300KB, P1-large|
|docs/assets/solution-batch2-qc-sheet-v1.webp|298.1|860x1020|PNG|-|
|docs/assets/rm2-5-build-your-own-index-01-system-capability-map.webp|291.0|2752x1536|PNG|-|
|docs/assets/solution-xhs-cli-vs-acp-v1.webp|288.7|1600x900|PNG|-|
|docs/assets/solution-ppt-cli-vs-acp-v1.webp|280.0|1600x900|PNG|-|
|docs/assets/03-domestic-deploy-overview-map-v4.webp|267.6|2752x1536|PNG|-|
|docs/assets/practical-15-skills-official-screenshot-zh-v1.webp|162.3|1600x900|PNG|-|
|docs/assets/rm2-4-memory-02-memory-read-write-success.webp|158.5|1720x980|PNG|-|
|docs/assets/rm2-5-memory-providers-03-honcho-status-proof.webp|152.8|1280x1292|PNG|-|
|docs/assets/rm2-5-profiles-02-profile-switch-success.webp|150.6|1720x1260|PNG|-|
|docs/assets/03-domestic-deploy-overview-map.webp|145.6|2752x1536|PNG|-|
|docs/assets/solution-miniapp-3-layer-map.webp|136.3|1600x900|PNG|-|
|docs/assets/rm2-5-memory-providers-02-holographic-status-proof.webp|102.3|1280x782|PNG|-|

## Ambiguous 引用清单
|source|kind|raw|normalized|reason|
|---|---|---|---|---|
|docs/03-国内落地/01-国内部署/02-阿里云轻量服务器部署教程.md|markdown_image|./assets/aliyun-buy-hermes-user.webp|docs/03-国内落地/01-国内部署/assets/aliyun-buy-hermes-user.webp|relative|
|docs/03-国内落地/01-国内部署/02-阿里云轻量服务器部署教程.md|markdown_image|./assets/aliyun-help-getting-started-top.webp|docs/03-国内落地/01-国内部署/assets/aliyun-help-getting-started-top.webp|relative|
|docs/03-国内落地/01-国内部署/02-阿里云轻量服务器部署教程.md|markdown_image|./assets/aliyun-help-getting-started-mid.webp|docs/03-国内落地/01-国内部署/assets/aliyun-help-getting-started-mid.webp|relative|
|docs/03-国内落地/01-国内部署/02-阿里云轻量服务器部署教程.md|markdown_image|./assets/aliyun-article-hermes-step.webp|docs/03-国内落地/01-国内部署/assets/aliyun-article-hermes-step.webp|relative|
|docs/03-国内落地/01-国内部署/03-腾讯云轻量服务器部署教程.md|markdown_image|./assets/tencent-buy-hermes-agent.webp|docs/03-国内落地/01-国内部署/assets/tencent-buy-hermes-agent.webp|relative|
|docs/03-国内落地/01-国内部署/03-腾讯云轻量服务器部署教程.md|markdown_image|./assets/tencent-official-buy-page-hermes-agent.webp|docs/03-国内落地/01-国内部署/assets/tencent-official-buy-page-hermes-agent.webp|relative|
|docs/03-国内落地/01-国内部署/03-腾讯云轻量服务器部署教程.md|markdown_image|./assets/tencent-server-list-login-entry.webp|docs/03-国内落地/01-国内部署/assets/tencent-server-list-login-entry.webp|relative|
|docs/03-国内落地/01-国内部署/03-腾讯云轻量服务器部署教程.md|markdown_image|./assets/tencent-login-popup-tat-agentuser.webp|docs/03-国内落地/01-国内部署/assets/tencent-login-popup-tat-agentuser.webp|relative|
|docs/03-国内落地/01-国内部署/03-腾讯云轻量服务器部署教程.md|markdown_image|./assets/tencent-api-key-create.webp|docs/03-国内落地/01-国内部署/assets/tencent-api-key-create.webp|relative|
|docs/03-国内落地/01-国内部署/03-腾讯云轻量服务器部署教程.md|markdown_image|./assets/tencent-api-key-copy.webp|docs/03-国内落地/01-国内部署/assets/tencent-api-key-copy.webp|relative|
|docs/03-国内落地/01-国内部署/03-腾讯云轻量服务器部署教程.md|markdown_image|./assets/tencent-terminal-ready.webp|docs/03-国内落地/01-国内部署/assets/tencent-terminal-ready.webp|relative|
|docs/03-国内落地/01-国内部署/03-腾讯云轻量服务器部署教程.md|markdown_image|./assets/tencent-terminal-prompt.webp|docs/03-国内落地/01-国内部署/assets/tencent-terminal-prompt.webp|relative|
|docs/03-国内落地/02-国内模型/02-阿里云百炼Token plan.md|markdown_image|./assets/aliyun-bailian-tokenplan-hero-v18.webp|docs/03-国内落地/02-国内模型/assets/aliyun-bailian-tokenplan-hero-v18.webp|relative|
|docs/03-国内落地/02-国内模型/02-阿里云百炼Token plan.md|markdown_image|./assets/aliyun-bailian-hermes-config-section.webp|docs/03-国内落地/02-国内模型/assets/aliyun-bailian-hermes-config-section.webp|relative|
|docs/03-国内落地/02-国内模型/02-阿里云百炼Token plan.md|markdown_image|./assets/aliyun-bailian-get-api-key-section.webp|docs/03-国内落地/02-国内模型/assets/aliyun-bailian-get-api-key-section.webp|relative|
|docs/03-国内落地/02-国内模型/03-腾讯云Token Plan.md|markdown_image|./assets/tencent-tokenplan-hero-gemini-31-v4.webp|docs/03-国内落地/02-国内模型/assets/tencent-tokenplan-hero-gemini-31-v4.webp|relative|
|docs/03-国内落地/02-国内模型/03-腾讯云Token Plan.md|markdown_image|./assets/tencent-tokenplan-api-key-real-screenshot.webp|docs/03-国内落地/02-国内模型/assets/tencent-tokenplan-api-key-real-screenshot.webp|relative|
|docs/03-国内落地/02-国内模型/04-智谱GLM Coding Plan.md|markdown_image|./assets/glm-coding-hero-v1.webp|docs/03-国内落地/02-国内模型/assets/glm-coding-hero-v1.webp|relative|
|docs/03-国内落地/02-国内模型/04-智谱GLM Coding Plan.md|markdown_image|./assets/glm-hermes-model-menu-docs.webp|docs/03-国内落地/02-国内模型/assets/glm-hermes-model-menu-docs.webp|relative|
|docs/03-国内落地/02-国内模型/05-MiniMax Token Plan.md|markdown_image|./assets/minimax-tokenplan-modules-cliproxy-v11-title.webp|docs/03-国内落地/02-国内模型/assets/minimax-tokenplan-modules-cliproxy-v11-title.webp|relative|
|docs/03-国内落地/02-国内模型/05-MiniMax Token Plan.md|markdown_image|./assets/minimax-hermes-provider-cn.webp|docs/03-国内落地/02-国内模型/assets/minimax-hermes-provider-cn.webp|relative|
|docs/03-国内落地/02-国内模型/05-MiniMax Token Plan.md|markdown_image|./assets/minimax-hermes-apikey-cn.webp|docs/03-国内落地/02-国内模型/assets/minimax-hermes-apikey-cn.webp|relative|
|docs/03-国内落地/02-国内模型/05-MiniMax Token Plan.md|markdown_image|./assets/minimax-hermes-model-select.webp|docs/03-国内落地/02-国内模型/assets/minimax-hermes-model-select.webp|relative|
|docs/03-国内落地/02-国内模型/06-Kimi登月计划.md|markdown_image|./assets/kimi-moonshot-modules-cliproxy-v2.webp|docs/03-国内落地/02-国内模型/assets/kimi-moonshot-modules-cliproxy-v2.webp|relative|
|docs/03-国内落地/02-国内模型/07-DeepSeek按量计费接口.md|markdown_image|./assets/deepseek-api-hero-v1.webp|docs/03-国内落地/02-国内模型/assets/deepseek-api-hero-v1.webp|relative|
|docs/03-国内落地/02-国内模型/08-自定义兼容接口.md|markdown_image|./assets/custom-endpoint-modules-cliproxy-v10-16x9-preview.webp|docs/03-国内落地/02-国内模型/assets/custom-endpoint-modules-cliproxy-v10-16x9-preview.webp|relative|
|docs/03-国内落地/03-国内入口/02-网页控制台（Dashboard）.md|markdown_image|./assets/dashboard-entry-structure-v2.webp|docs/03-国内落地/03-国内入口/assets/dashboard-entry-structure-v2.webp|relative|
|docs/03-国内落地/03-国内入口/03-API 服务与 Open WebUI.md|markdown_image|./assets/api-openwebui-entry-structure-v3.webp|docs/03-国内落地/03-国内入口/assets/api-openwebui-entry-structure-v3.webp|relative|
|docs/03-国内落地/03-国内入口/04-命令行（CLI）.md|markdown_image|./assets/cli-entry-structure-v2.webp|docs/03-国内落地/03-国内入口/assets/cli-entry-structure-v2.webp|relative|
|docs/03-国内落地/03-国内入口/05-飞书.md|markdown_image|./assets/feishu-entry-structure-v1.webp|docs/03-国内落地/03-国内入口/assets/feishu-entry-structure-v1.webp|relative|
|docs/03-国内落地/03-国内入口/05-飞书.md|markdown_image|./assets/feishu-create-app-official.webp|docs/03-国内落地/03-国内入口/assets/feishu-create-app-official.webp|relative|
|docs/03-国内落地/03-国内入口/06-企业微信（AI Bot）.md|markdown_image|./assets/wecom-entry-structure-v1.webp|docs/03-国内落地/03-国内入口/assets/wecom-entry-structure-v1.webp|relative|
|docs/03-国内落地/03-国内入口/06-企业微信（AI Bot）.md|markdown_image|./assets/wecom-create-bot-entry-official.webp|docs/03-国内落地/03-国内入口/assets/wecom-create-bot-entry-official.webp|relative|
|docs/03-国内落地/03-国内入口/07-钉钉.md|markdown_image|./assets/dingtalk-entry-structure-v3.webp|docs/03-国内落地/03-国内入口/assets/dingtalk-entry-structure-v3.webp|relative|
|docs/03-国内落地/03-国内入口/07-钉钉.md|markdown_image|./assets/dingtalk-robot-stream-official.webp|docs/03-国内落地/03-国内入口/assets/dingtalk-robot-stream-official.webp|relative|
|docs/03-国内落地/03-国内入口/08-个人微信.md|markdown_image|./assets/weixin-entry-structure-v2.webp|docs/03-国内落地/03-国内入口/assets/weixin-entry-structure-v2.webp|relative|
|docs/04-从OpenClaw过来/02-OpenClaw 和 Hermes 的关系.md|markdown_image|./assets/openclaw-hermes-relationship-structure-v4.webp|docs/04-从OpenClaw过来/assets/openclaw-hermes-relationship-structure-v4.webp|relative|
|docs/04-从OpenClaw过来/02-OpenClaw 和 Hermes 的关系.md|markdown_image|./assets/openclaw-hermes-comparison-v4.webp|docs/04-从OpenClaw过来/assets/openclaw-hermes-comparison-v4.webp|relative|
|docs/04-从OpenClaw过来/03-继续用、共存，还是迁移.md|markdown_image|./assets/openclaw-migration-decision-tree-v4.webp|docs/04-从OpenClaw过来/assets/openclaw-migration-decision-tree-v4.webp|relative|
|docs/04-从OpenClaw过来/03-继续用、共存，还是迁移.md|markdown_image|./assets/openclaw-three-paths-comparison-v4.webp|docs/04-从OpenClaw过来/assets/openclaw-three-paths-comparison-v4.webp|relative|
|docs/04-从OpenClaw过来/03-继续用、共存，还是迁移.md|markdown_image|./assets/openclaw-decision-operation-map-v4.webp|docs/04-从OpenClaw过来/assets/openclaw-decision-operation-map-v4.webp|relative|
|docs/04-从OpenClaw过来/04-OpenClaw + Hermes 共存指南.md|markdown_image|./assets/openclaw-hermes-coexistence-structure-v4.webp|docs/04-从OpenClaw过来/assets/openclaw-hermes-coexistence-structure-v4.webp|relative|
|docs/04-从OpenClaw过来/04-OpenClaw + Hermes 共存指南.md|markdown_image|./assets/openclaw-hermes-coexistence-modes-v4.webp|docs/04-从OpenClaw过来/assets/openclaw-hermes-coexistence-modes-v4.webp|relative|
|docs/04-从OpenClaw过来/04-OpenClaw + Hermes 共存指南.md|markdown_image|./assets/openclaw-hermes-coexistence-operation-v4.webp|docs/04-从OpenClaw过来/assets/openclaw-hermes-coexistence-operation-v4.webp|relative|
|docs/04-从OpenClaw过来/05-从 OpenClaw 到 Hermes：迁移路径.md|markdown_image|./assets/openclaw-hermes-migration-flow-v6.webp|docs/04-从OpenClaw过来/assets/openclaw-hermes-migration-flow-v6.webp|relative|
|docs/04-从OpenClaw过来/06-OpenClaw 用户常见问题与检查清单.md|markdown_image|./assets/openclaw-checklist-overview-v4.webp|docs/04-从OpenClaw过来/assets/openclaw-checklist-overview-v4.webp|relative|
|docs/04-从OpenClaw过来/06-OpenClaw 用户常见问题与检查清单.md|markdown_image|./assets/openclaw-troubleshooting-path-v4.webp|docs/04-从OpenClaw过来/assets/openclaw-troubleshooting-path-v4.webp|relative|

## Missing 引用清单
|source|kind|raw|normalized|
|---|---|---|---|
|-|-|-|-|

## 机器可读 proof
- JSON: `/opt/projects/awesome-hermes-agent-zh/artifacts/asset-inventory/CONTENT_IMAGE_ASSET_INVENTORY_R1_20260608.json`
