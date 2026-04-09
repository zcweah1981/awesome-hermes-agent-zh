---
layout: home

hero:
  name: "Hermes Agent 中文指南"
  text: "给中文开发者的上手、选型与落地入口"
  tagline: "快速开始、模型选择、Starter 模板、实战案例与常见问题，全部围绕真实使用场景整理。"
  image:
    src: /logo.svg
    alt: Hermes Agent 中文指南 Logo
  actions:
    - theme: brand
      text: 30 秒快速开始
      link: /quick-start
    - theme: alt
      text: 看 Starter 模板
      link: /starters/index
    - theme: alt
      text: 看示例项目
      link: /examples/index

features:
  - title: 快速开始
    details: 从安装、模型选择到首轮运行，先帮你把 Hermes 真正跑起来。
    link: /quick-start
  - title: 模型与 Provider
    details: 优先走官方 provider 路径，减少无效 custom 配置，适合中文用户的实际接入环境。
    link: /models
  - title: 常见问题
    details: 覆盖代理、SSL、编码、权限、依赖等高频问题，减少环境折腾。
    link: /known-issues
  - title: Starter 模板
    details: 提供 single-agent、team-basic、advanced-coding-team 三类项目骨架。
    link: /starters/index
  - title: 示例项目
    details: 提供 webhook、Telegram 汇报、仓库巡检等更接近真实工作的案例。
    link: /examples/index
  - title: 选型与协作
    details: 帮你判断 Hermes 是否适合当前阶段，并理解多 Agent 协作的业务价值。
    link: /team-flow
---

## 为什么看这个站

这里不是开发过程记录，也不是内部 PRD，而是面向中文用户的直接入口：
- 想快速安装并跑通 Hermes
- 想选一个合适的模型或 Provider
- 想复制一个可用 Starter
- 想参考一个更接近真实工作的 Example

## 推荐阅读路径

### 第一次使用
- [快速开始](./quick-start.md)
- [模型与 Provider](./models.md)
- [常见问题](./known-issues.md)

### 想搭项目骨架
- [Starter 模板](./starters/index.md)
- [single-agent starter 模板说明](./single-agent-starter-guide.md)
- [team-basic starter 模板说明](./team-basic-starter-guide.md)

### 想看具体案例
- [示例项目](./examples/index.md)
- [Telegram 汇报示例](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/examples/telegram-report)
- [仓库巡检示例](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/examples/repo-review)

### 想做选型或迁移
- [Hermes vs OpenClaw](./openclaw-compare.md)
- [从 OpenClaw 迁移到 Hermes](./openclaw-migration.md)
- [多 Agent 协作](./team-flow.md)

## 当前收录内容

### 入门与配置
- [快速开始](./quick-start.md)
- [安装前准备](./install-prep.md)
- [模型与 Provider](./models.md)
- [自定义 OpenAI-Compatible 接口配置指南](./custom-openai-compatible.md)
- [常见配置错误排查](./config-errors.md)
- [第一次跑不起来时的标准排查顺序](./first-run-checklist.md)
- [常见问题](./known-issues.md)

### 选型与协作
- [Hermes 到底适合谁，不适合谁](./fit-guide.md)
- [Hermes vs OpenClaw](./openclaw-compare.md)
- [从 OpenClaw 迁移到 Hermes](./openclaw-migration.md)
- [迁移后校验清单](./migration-checklist.md)
- [多 Agent 协作](./team-flow.md)
- [SOUL 管角色，MD 管项目](./soul-md-workflow.md)

### 模板与项目结构
- [Starter 模板](./starters/index.md)
- [single-agent starter 模板说明](./single-agent-starter-guide.md)
- [team-basic starter 模板说明](./team-basic-starter-guide.md)
- [Hermes 项目目录组织规范](./project-structure.md)
- [Hermes 项目文件编写指南](./project-files-guide.md)
- [Hermes 中文用户最常见的 3 条使用路径](./user-paths.md)

### 实战案例
- [示例项目索引](./examples/index.md)
- [Webhook 集成示例](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/examples/skills/webhook-notifier)
- [Telegram 汇报示例](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/examples/telegram-report)
- [仓库巡检示例](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/examples/repo-review)
