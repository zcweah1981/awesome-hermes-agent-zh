# 09-多模型合奏（Mixture-of-Agents）

> 💡 **速答**：Mixture-of-Agents (MoA) 是 v0.18.0 引入的高级推理模式。它不再依赖单一模型，而是让一组“参考模型”先各自生成答案，再由一个“聚合模型”对这些答案进行评估、对比和提炼。这种方式能显著提升复杂逻辑推理和代码编写的准确度。

---

## 🧠 为什么需要 MoA

不同的模型有不同的擅长领域：
- **DeepSeek**：逻辑严密，适合做底层推导。
- **Claude 3.5 Sonnet**：文笔优美，指令遵循极强，适合做最终聚合。
- **GPT-4o**：常识丰富，适合做辅助参考。

通过 MoA，你可以把它们组合成一个“专家组”。

## 🛠️ 配置实战

在 Hermes 中，MoA 模型被视为一种特殊的 `provider`。你可以在 `config.yaml` 或环境变量中定义。

### 1. 典型配置示例
假设你想配置一个名为 `super-thinker` 的合奏模型：

```yaml
# config.yaml 示例
models:
  super-thinker:
    provider: moa
    aggregator: anthropic/claude-3-5-sonnet  # 最终出单的模型
    references:                               # 提供参考的专家组
      - deepseek/deepseek-chat
      - openai/gpt-4o
      - google/gemini-1.5-pro
```

### 2. 在对话中使用
配置好后，你可以直接切换到该合奏模型：
```text
/model super-thinker
```
当你提问时，Hermes 会展示每个参考模型的思考片段，最后给出聚合后的完美答案。

## 🎯 推荐场景

- **核心架构设计**：需要多方权衡利弊时。
- **复杂 Bug 修复**：单一模型可能看不出深层原因时。
- **创意写作**：需要汇总不同风格的初稿时。

## ⚠️ 成本提醒

**注意**：MoA 会同时消耗所有参与模型的 Token。如果你配置了 3 个参考模型 + 1 个聚合模型，一次提问将产生 4 倍（甚至更多）的 Token 消耗。请根据任务的严肃程度量力而行。

---

## ➡️ 下一步

了解了多模型合奏后，你可以进一步探索：
- [04-自定义 AI 大模型](../03-玩出花样/04-自定义%20AI%20大模型.md)
- [08-MCP 配置参考](../../06-reference/08-MCP%20配置参考.md)
