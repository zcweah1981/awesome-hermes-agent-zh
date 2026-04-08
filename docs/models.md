# 模型与 Provider 选择

这页不再把“自定义 endpoint”当默认方案，而是基于 Hermes Agent 官方 provider 文档，整理中文用户最常用的接入路径。

官方参考：
- AI Providers: https://hermes-agent.nousresearch.com/docs/integrations/providers/
- Configuration: https://hermes-agent.nousresearch.com/docs/user-guide/configuration/
- Quickstart: https://hermes-agent.nousresearch.com/docs/getting-started/quickstart/

---

## 核心原则

先记住一句话：

优先用官方 provider，最后才用 custom endpoint。

因为：
- 官方 provider 会随 Hermes 版本持续维护
- `hermes model` / `hermes setup` 会帮你减少手工配置错误
- 仓库文档不应该诱导用户走一条更重、更脆弱的自定义路径

推荐优先级：

1. 官方 provider
2. `.env` 注入 API key
3. `hermes model` 选择模型
4. 只有当官方没覆盖时，再考虑 custom endpoint

---

## 官方已支持的重点 Provider（和中文用户最相关）

### 1. DeepSeek

- 官方 provider: `deepseek`
- 密钥变量：`DEEPSEEK_API_KEY`
- 适合：低成本、高性价比、通用对话、代码任务

示例：

```bash
# ~/.hermes/.env
DEEPSEEK_API_KEY=sk-xxx

hermes chat --provider deepseek --model deepseek-chat
```

建议：
- 如果你只是想最快跑通国内模型，DeepSeek 依然是优先选项
- 仓库文档里不再把它写成 custom provider

---

### 2. Qwen / DashScope / Alibaba Cloud

- 官方 provider: `alibaba`
- 官方别名：`dashscope`、`qwen`
- 密钥变量：`DASHSCOPE_API_KEY`
- 适合：中文理解、企业侧接入、阿里云体系

示例：

```bash
# ~/.hermes/.env
DASHSCOPE_API_KEY=sk-xxx

hermes chat --provider alibaba --model qwen-max
```

说明：
- 文档里可以写 Qwen，但配置时要以 Hermes 官方 provider 标识为准
- 不建议继续把 Qwen 写成 `providers.custom` 默认范式

---

### 3. z.ai / GLM

- 官方 provider: `zai`
- 密钥变量：`GLM_API_KEY`
- 适合：国内替代、综合能力模型路线

示例：

```bash
# ~/.hermes/.env
GLM_API_KEY=xxx

hermes chat --provider zai --model glm-4.5
```

说明：
- 官方文档现在已经把 GLM 放入一等 provider
- 我们仓库后续应使用 `zai` 口径，而不是再默认教用户手改自定义 base_url

---

### 4. Kimi / Moonshot

- 官方 provider: `kimi-coding`
- 密钥变量：`KIMI_API_KEY`
- 适合：长文本、中文写作、代码辅助

示例：

```bash
# ~/.hermes/.env
KIMI_API_KEY=sk-xxx

hermes chat --provider kimi-coding --model moonshot-v1-auto
```

说明：
- Kimi 现在也属于官方一等支持路径
- 这意味着仓库可以直接写官方 provider 教程，而非自定义 endpoint 教程

---

### 5. MiniMax / MiniMax China

- 官方 provider: `minimax` / `minimax-cn`
- 密钥变量：`MINIMAX_API_KEY` / `MINIMAX_CN_API_KEY`
- 适合：需要补充国产 provider 覆盖范围的团队

---

### 6. OpenRouter

- 官方 provider: `openrouter`
- 密钥变量：`OPENROUTER_API_KEY`
- 适合：想统一接多个海外/聚合模型的用户

示例：

```bash
# ~/.hermes/.env
OPENROUTER_API_KEY=sk-or-xxx

hermes chat --provider openrouter --model anthropic/claude-sonnet-4
```

补充：
- 很多辅助模型（vision / summarization / compression）默认也会走 OpenRouter 路线
- 所以即使主模型不是 OpenRouter，很多高级功能依然建议准备一个 `OPENROUTER_API_KEY`

---

### 7. Anthropic

- 官方 provider: `anthropic`
- 支持方式：`hermes model`、Anthropic API key、Claude Code 凭据复用
- 适合：高质量推理、代码与复杂任务

---

### 8. Hugging Face

- 官方 provider: `huggingface`（别名 `hf`）
- 密钥变量：`HF_TOKEN`
- 适合：实验性模型与开源生态

---

## 配置应该放哪

根据官方 Configuration 文档：

### Secret

放在：

`~/.hermes/.env`

例如：

```bash
DEEPSEEK_API_KEY=sk-xxx
DASHSCOPE_API_KEY=sk-xxx
GLM_API_KEY=xxx
KIMI_API_KEY=sk-xxx
OPENROUTER_API_KEY=sk-or-xxx
```

### 非 Secret

放在：

`~/.hermes/config.yaml`

例如终端后端、压缩策略、工具集配置等。

结论：
- API key 不要再大段写进 README 示例里
- 文档应该强调 `.env` 与 `config.yaml` 的职责分离

---

## 什么时候才需要 Custom Endpoint

只有这些情况才建议：

- 你在用自建 vLLM / SGLang / OpenAI-compatible 服务
- 你在用官方尚未内建的一家第三方 API
- 你需要特殊 base URL / 鉴权方式

也就是说：
- DeepSeek：通常不需要 custom
- Qwen：通常不需要 custom
- GLM：通常不需要 custom
- Kimi：通常不需要 custom

这就是当前仓库必须修正的地方。

---

## 推荐选型建议

### 我只想最快跑通

- DeepSeek
- 然后执行：`hermes model`

### 我主要是中文场景

- Qwen / Kimi / GLM

### 我想保留更强的多模型切换能力

- OpenRouter + 至少一个国内 provider

### 我是团队环境

- 主模型走官方 provider
- 辅助模型保留 OpenRouter 作为补充

---

## 验收标准

本页完成后，用户应该能回答：

- 哪些模型已经有官方 provider
- 哪些 API key 应该放 `.env`
- 什么时候该用 `hermes model`
- 什么时候才需要 custom endpoint

---

## 下一步

- 安装与首轮启动：`./quick-start.md`
- 常见问题：`./known-issues.md`
