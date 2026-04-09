# Hermes Agent 中文指南

![Hermes Agent 中文指南 Banner](./docs/public/hero-banner.svg)

面向中文开发者的 Hermes Agent 上手、选型与实战资源库。

这个仓库聚焦三件事：
- 帮你快速完成安装与首跑
- 帮你选择合适的模型与 Provider
- 提供可直接复用的模板、案例与排障说明

快速入口：
- [30 秒快速开始](./docs/quick-start.md)
- [模型与 Provider](./docs/models.md)
- [Starter 模板](./docs/starters/index.md)
- [示例项目](./docs/examples/index.md)
- [常见问题](./docs/known-issues.md)
- [Hermes vs OpenClaw](./docs/openclaw-compare.md)
- [多 Agent 协作](./docs/team-flow.md)

---

## Hermes Agent 是什么

Hermes Agent 是一个可扩展的 AI Agent 框架，支持：
- 终端执行
- 文件读写
- Web 搜索与提取
- 浏览器自动化
- 多智能体协作
- 技能与工具扩展
- Telegram / Discord / Slack 等消息平台接入

如果你希望把大模型从“聊天”推进到“执行任务”，Hermes 是一条非常直接的落地路线。

---

## 这个仓库适合谁

- 第一次接触 Hermes Agent 的中文开发者
- 想在国内环境里稳定接入模型的团队
- 希望搭建单人公司 / 小团队 AI 工作流的人
- 需要可复制模板，而不是只看概念介绍的用户

---

## 30 秒快速开始

1. 安装 Hermes Agent

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc   # 或 source ~/.zshrc
```

2. 选择模型

```bash
hermes setup
# 或
hermes model
```

3. 启动

```bash
hermes
```

如果你想直接指定模型：

```bash
hermes chat --provider deepseek --model deepseek-chat
```

---

## 推荐阅读路径

### 我只想先跑起来
1. [快速开始](./docs/quick-start.md)
2. [模型与 Provider](./docs/models.md)
3. [常见问题](./docs/known-issues.md)

### 我想给团队做选型
1. [Hermes 到底适合谁，不适合谁](./docs/fit-guide.md)
2. [Hermes vs OpenClaw](./docs/openclaw-compare.md)
3. [多 Agent 协作](./docs/team-flow.md)

### 我想搭项目骨架
1. [Starter 模板](./docs/starters/index.md)
2. [single-agent starter 模板说明](./docs/single-agent-starter-guide.md)
3. [team-basic starter 模板说明](./docs/team-basic-starter-guide.md)

### 我想看具体案例
1. [示例项目](./docs/examples/index.md)
2. [Telegram 汇报示例](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/examples/telegram-report)
3. [仓库巡检示例](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/examples/repo-review)

---

## 当前收录内容

### 入门与配置
- [快速开始](./docs/quick-start.md)
- [安装前准备](./docs/install-prep.md)
- [模型与 Provider](./docs/models.md)
- [自定义 OpenAI-Compatible 接口配置指南](./docs/custom-openai-compatible.md)
- [常见配置错误排查](./docs/config-errors.md)
- [第一次跑不起来时的标准排查顺序](./docs/first-run-checklist.md)
- [常见问题](./docs/known-issues.md)

### 选型与协作
- [Hermes 到底适合谁，不适合谁](./docs/fit-guide.md)
- [Hermes vs OpenClaw](./docs/openclaw-compare.md)
- [从 OpenClaw 迁移到 Hermes](./docs/openclaw-migration.md)
- [迁移后校验清单](./docs/migration-checklist.md)
- [多 Agent 协作](./docs/team-flow.md)
- [SOUL 管角色，MD 管项目](./docs/soul-md-workflow.md)

### 模板与项目结构
- [Starter 模板](./docs/starters/index.md)
- [single-agent starter 模板说明](./docs/single-agent-starter-guide.md)
- [team-basic starter 模板说明](./docs/team-basic-starter-guide.md)
- [Hermes 项目目录组织规范](./docs/project-structure.md)
- [Hermes 项目文件编写指南](./docs/project-files-guide.md)
- [Hermes 中文用户最常见的 3 条使用路径](./docs/user-paths.md)

### 实战案例
- [示例项目索引](./docs/examples/index.md)
- [Webhook 集成示例](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/examples/skills/webhook-notifier)
- [Telegram 汇报示例](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/examples/telegram-report)
- [仓库巡检示例](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/examples/repo-review)

---

## 官方参考

- [官方文档](https://hermes-agent.nousresearch.com/)
- [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart/)
- [AI Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers/)
- [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/)

---

## 贡献方向

欢迎补充：
- 中文环境下的真实排障案例
- 可运行的 Starter 模板
- 行业场景案例
- 国内模型接入经验

如果你发现文档过时，欢迎直接提 [Issue](https://github.com/zcweah1981/awesome-hermes-agent-zh/issues) 或 [PR](https://github.com/zcweah1981/awesome-hermes-agent-zh/pulls)。
