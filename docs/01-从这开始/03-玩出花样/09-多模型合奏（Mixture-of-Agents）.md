# 09-多模型合奏（Mixture-of-Agents）

> 💡 **速答**：MoA (Mixture-of-Agents) 是一种“专家集群”模式。它让多个参考模型先产出初稿，再由聚合模型进行融合，极大提升了逻辑推理的上限。

![MoA 专家组合奏流转图：DeepSeek 逻辑推理 + Claude 意图对齐 -> Aggregator 聚合结论](../../assets/play-tricks-moa-v1.webp)

---

## 🛠️ 配置示例
在你的 `config.yaml` 中，可以定义如下虚拟模型：
```yaml
models:
  moa-pro:
    provider: moa
    aggregator: anthropic/claude-3-5-sonnet  # 聚合者：负责最终逻辑对齐
    references:
      - deepseek/deepseek-chat           # 专家1：负责发散与推导
      - openai/gpt-4o                    # 专家2：负责知识补充
```

---

## ➡️ 下一步
- 上一步：[08-教-Hermes-学习新技能-learn](./08-教-Hermes-学习新技能-learn.md)
- 下一阶段：[04-自己造东西](../04-自己造东西/01-总览.md)
- 回到目录：[03-玩出花样](./01-总览.md)
