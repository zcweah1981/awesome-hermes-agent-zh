---
layout: home

hero:
  name: "Hermes Agent ZH"
  text: "最快、最稳的中文落地指南"
  tagline: "30秒接入 DeepSeek/Qwen，开箱即用的多 Agent 模板"
  image:
    src: /logo.png
    alt: Hermes Agent Logo
  actions:
    - theme: brand
      text: 🚀 快速开始
      link: /quick-start
    - theme: alt
      text: 📦 浏览模板
      link: https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/starters

features:
  - title: ⚡ 极速接入
    details: 针对国内网络环境优化，预置 DeepSeek、通义千问等主流模型配置，零门槛起步。
  - title: 🧩 场景模板
    details: 提供从单体助手到多子体协作 (OPC) 的现成模板，支持代码编写、文档审计等实战场景。
  - title: 🛡️ 中文排障
    details: 汇总国内特有的网络超时、编码乱码、环境依赖等“三大坑”解决方案。
  - title: 🔌 生态拓展
    details: 正在接入飞书、钉钉、微信等国内主流办公平台的集成指引。

# 下面是 Markdown 正文，确保在 GitHub 预览时依然可见
---

# Hermes Agent 中文生态 (hermes-agent-zh)

<p align="center">
  <img src="https://raw.githubusercontent.com/zcweah1981/awesome-hermes-agent-zh/main/docs/public/banner.png" alt="Hermes Agent Banner" style="max-width: 100%; border-radius: 8px;">
</p>

## 🚀 核心价值

- **零门槛直连**: 默认集成 **DeepSeek/Qwen** 替代 Anthropic/OpenAI，国内访问无阻。
- **开箱即用模板**: 提供覆盖单体助手、编码智能体、多智能体协作(OPC)的 `config.yaml`。
- **本地化连接**: 包含钉钉、微信、飞书等国内 IM 的接入最佳实践。

## 🛠️ 快速导航

- [**快速开始 (30秒上手)**](./quick-start) - 获取你的第一个 DeepSeek 配置文件。
- [**国内模型接入指南**](./models) - 涵盖 DeepSeek, Qwen, GLM, Kimi 等。
- [**实战模板库 (Starters)**](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/starters) - 直接下载即可运行。
- [**常见问题与排障**](./known-issues) - 遇到报错先看这里。

## 为什么选择 Hermes？

相比于其他 Agent 框架，Hermes 拥有：
- **原生 ACP 协议**: 极低延迟的多智能体并发协作。
- **内置学习闭环**: 自动从会话中提取并持久化技能。
- **极简部署**: 哪怕是在 $5 的 VPS 上也能流畅运行。
