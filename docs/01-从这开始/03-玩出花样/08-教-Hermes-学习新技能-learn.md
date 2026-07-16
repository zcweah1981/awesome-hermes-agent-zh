# 08-教 Hermes 学习新技能（/learn）

> 💡 **速答**：`/learn` 让 Agent 能够从你的对话中“提炼逻辑”。当你完成了一次复杂的调试或处理后，输入 `/learn`，Agent 会将这段操作路径固化为永久的 **Skill**。

![Hermes 自进化逻辑：演示引导 -> 逻辑提炼 -> 技能固化](../../assets/play-tricks-learn-v1.webp)

---

## 🧠 核心原理：演示即编程
不需要写复杂的 YAML 或 Python 代码。只要你带 Agent 成功走通了一遍，它就能学会：
1. **引导**：带 Agent 执行“读取 CSV -> 清洗数据 -> 绘制图表”。
2. **提炼**：任务成功后输入 `/learn`。
3. **固化**：Agent 生成并保存 `csv-plot-skill`。
4. **验证**：通过 `/journey` 查看它提炼的逻辑是否与你一致。

---

## ➡️ 下一步
- 上一步：[07-用桌面端操作 Hermes](./07-用桌面端操作 Hermes.md)
- 下一步：[09-多模型合奏（Mixture-of-Agents）](./09-多模型合奏（Mixture-of-Agents）.md)
- 回到目录：[03-玩出花样](./01-总览.md)
