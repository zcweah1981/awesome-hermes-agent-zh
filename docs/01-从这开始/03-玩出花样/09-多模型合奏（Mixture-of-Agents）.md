# 09-多模型合奏（Mixture-of-Agents）

> 💡 **速答**：MoA (Mixture-of-Agents) 让一组“参考模型”先生成答案，再由“聚合模型”提炼方案。这就像让 DeepSeek 负责草稿，Claude 负责逻辑，最后让 GPT 聚合出最稳的结果。

![MoA 专家组合奏图：Reference Models 生成草稿 -> Aggregator 聚合结论](../../assets/play-tricks-moa-v1.webp)

---

## 🛠️ 配置实战
在 `config.yaml` 中配置一个 MoA 模型：
```yaml
models:
  moa-pro:
    provider: moa
    aggregator: anthropic/claude-3-5-sonnet
    references:
      - deepseek/deepseek-chat
      - openai/gpt-4o
```

---

## ➡️ 下一步
- 上一步：[08-教-Hermes-学习新技能-learn](./08-教-Hermes-学习新技能-learn.md)
- 下一阶段：[04-自己造东西](../04-自己造东西/01-总览.md)
- 回到目录：[03-玩出花样](./01-总览.md)
