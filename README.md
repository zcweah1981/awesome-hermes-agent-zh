# Hermes Agent 中文指南

面向中文用户的 Hermes Agent 上手、选型与实战资源库。

这个仓库聚焦三件事：
- 帮你快速完成安装与首跑
- 帮你选择合适的模型与 Provider
- 提供可直接复用的模板、案例与排障说明

快速入口：
- [快速开始](./docs/quick-start.md)
- [模型与 Provider](./docs/models.md)
- [常见问题](./docs/known-issues.md)
- [Hermes vs OpenClaw](./docs/openclaw-compare.md)
- [多 Agent 协作](./docs/team-flow.md)
- [Starter 模板](./docs/starters/index.md)
- [示例项目](./docs/examples/index.md)

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
1. [模型与 Provider](./docs/models.md)
2. [Hermes vs OpenClaw](./docs/openclaw-compare.md)
3. [多 Agent 协作](./docs/team-flow.md)

### 我想搭项目骨架
1. [Starter 模板](./docs/starters/index.md)
2. [single-agent](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/starters/single-agent) 或 [team-basic](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/starters/team-basic)

### 我想看具体案例
1. [示例项目](./docs/examples/index.md)
2. 进入 [配置示例](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/examples/configs) 或 [Webhook 集成示例](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/examples/skills/webhook-notifier)

---

## 当前收录内容

### [快速开始](./docs/quick-start.md)
包含安装、初始化、首轮对话与国内环境建议。

### [模型与 Provider](./docs/models.md)
覆盖 DeepSeek、Qwen、GLM、Kimi、OpenRouter 等常见接入路径。

### [常见问题](./docs/known-issues.md)
覆盖 SSL、代理、编码、权限、依赖缺失等高频问题。

### [Hermes vs OpenClaw](./docs/openclaw-compare.md)
帮助已有其他 Agent 框架经验的用户快速理解 Hermes 的使用方式。

### [Starter 模板](./docs/starters/index.md)
提供适合直接复制的基础项目模板。

### [示例项目](./docs/examples/index.md)
提供更接近真实业务的参考结构与配置样例。

---

## 推荐模型组合

### 个人开发者
- 主模型：DeepSeek 或 Qwen
- 备选：OpenRouter

### 中文内容与长文本场景
- Kimi / Qwen / GLM

### 多模型切换与海外模型需求
- OpenRouter + 一个国内 Provider

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
