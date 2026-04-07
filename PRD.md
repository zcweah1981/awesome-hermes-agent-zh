# PRD: Hermes Agent 中文生态

## 1. 产品定位
提供“极短交付周期”和“极高交付质量”的 Hermes Agent 中文落地实践指南。帮助中国开发者绕过网络、支付和文档门槛，直接进入 Agent 开发阶段。

## 2. 核心价值 (Value Proposition)
- **零门槛直连**: 默认集成 DeepSeek/Qwen 替代 Anthropic/OpenAI，无缝兼容。
- **开箱即用模板**: 提供覆盖单体助手、编码智能体、多智能体协作(OPC)的 `config.yaml`。
- **本地化连接**: 包含钉钉、微信、飞书等国内 IM 的接入最佳实践。

## 3. 用户路径 (User Journey)
1. 访问首页 (30秒了解核心价值)
2. 复制 `quick-start` 的 DeepSeek `config.yaml` 跑通第一个 Agent。
3. 浏览 `/starters` 寻找适合自己业务的模板。

## 4. 范围控制 (Scope Control)
- **In Scope**:
  - VitePress 静态文档站 (只讲实战，不讲底层原理)。
  - `config.yaml` 与环境变量配置示例。
- **Out of Scope**:
  - Hermes Agent 引擎本身的 C/C++/Python 底层修改。
  - 大而全的英文官网 API 翻译。