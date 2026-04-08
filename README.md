# 🚀 Hermes Agent 中文实战入口 (Awesome Hermes Agent ZH)

<p align="center">
  <strong>仓库负责真实内容，站点负责展示与引导。</strong>
</p>

<p align="center">
  <a href="./docs/quick-start.md"><strong>快速开始</strong></a> ·
  <a href="./docs/models.md"><strong>模型与 Provider</strong></a> ·
  <a href="./docs/known-issues.md"><strong>常见问题</strong></a> ·
  <a href="./docs/openclaw-compare.md"><strong>Hermes vs OpenClaw</strong></a> ·
  <a href="./starters"><strong>Starters</strong></a>
</p>

---

## 目标

这个仓库不是做一份“中文二次创作文档站”，而是做 Hermes Agent 的中文实战入口：

- 基于官方文档持续校准
- 优先提供可执行、可复制、可验证的内容
- 仓库作为正文单一真理源（SSoT）
- 独立站只负责展示、导航、分发，不维护另一套正文

---

## 当前策略

我们已经明确纠偏：

### 1. 先跟官方文档对齐

官方文档已经覆盖：
- Installation
- Quickstart
- AI Providers
- Configuration

并且官方已经支持很多一等 provider，包括：
- DeepSeek
- Qwen / DashScope / Alibaba
- GLM / z.ai
- Kimi / Moonshot
- MiniMax
- OpenRouter
- Anthropic
- Hugging Face

所以本仓库不再默认把“自定义 provider / custom endpoint”写成主路径。

### 2. 仓库只补官方文档没有解决好的中文落地问题

我们重点补：
- 中文用户如何理解官方 provider 体系
- 中文环境下安装与代理注意事项
- 国内模型选型建议
- 仓库里的 starter、example、技能样例
- 真实可复用的项目组织方式

### 3. 独立站从仓库内容生成

正文在仓库里维护：
- `README.md`
- `docs/*.md`
- `examples/`
- `starters/`

站点负责：
- 首页展示
- 导航与分发
- 搜索与入口

---

## 最短成功路径

### 1. 按官方方式安装

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc   # 或 source ~/.zshrc
```

### 2. 用官方方式配置 provider

```bash
hermes setup
# 或
hermes model
```

### 3. 启动

```bash
hermes
```

如果你希望显式指定：

```bash
hermes chat --provider deepseek --model deepseek-chat
```

结论：
- 优先走官方 provider
- 优先走 `hermes setup` / `hermes model`
- 最后才考虑 custom endpoint

---

## 仓库内容结构

### docs/
真实正文来源。

当前重点页面：
- `docs/quick-start.md`
- `docs/models.md`
- `docs/known-issues.md`
- `docs/openclaw-compare.md`

### examples/
放配置样例、技能样例、可复制案例。

### starters/
放可直接复制的 starter 模板。

### scripts/
放同步脚本与自动化辅助脚本。

---

## 你应该先看哪几页

### 我是第一次安装
看：`docs/quick-start.md`

### 我想知道 DeepSeek / Qwen / GLM / Kimi 应该怎么选
看：`docs/models.md`

### 我在国内环境遇到证书、代理、超时问题
看：`docs/known-issues.md`

### 我原来在看 OpenClaw，想比较路线
看：`docs/openclaw-compare.md`

---

## 当前内容边界

这个仓库当前优先做：
- 安装
- provider 选择
- 中文环境落地
- starters
- examples
- 对比与迁移

暂不优先做：
- 大量视觉包装
- 脱离仓库正文的独立站花活
- 和官方文档重复但没有增量价值的搬运

---

## 官方参考

- Installation: https://hermes-agent.nousresearch.com/docs/getting-started/installation
- Quickstart: https://hermes-agent.nousresearch.com/docs/getting-started/quickstart/
- AI Providers: https://hermes-agent.nousresearch.com/docs/integrations/providers/
- Configuration: https://hermes-agent.nousresearch.com/docs/user-guide/configuration/

---

## 下一步优先级

1. 基于官方 provider 文档继续修正旧内容
2. 把 `examples/` 和 `starters/` 补成真实可运行资产
3. 再让独立站消费仓库正文做展示

如果你认同这个方向，下一轮我会继续清理：
- `known-issues.md` 里过时的 `custom/...` 表述
- `openclaw-compare.md` 里不准确或过重承诺的技术描述
- `examples/` 和 `starters/` 的真实度与可运行性
