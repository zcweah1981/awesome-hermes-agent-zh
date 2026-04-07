# Hermes vs OpenClaw: 为什么你应该迁移？

如果你之前是 OpenClaw 的忠实用户，你可能会问：**“Hermes Agent 到底强在哪里？我为什么要花时间迁移？”**

本页面将从架构、性能、生态三个维度为你进行硬核对比。

## 1. 核心对比表

| 特性 | OpenClaw | Hermes Agent |
| :--- | :--- | :--- |
| **底层引擎** | 基于早期 Agent 框架 | 自主研发，深度优化推理路径 |
| **学习能力** | 静态技能库 | **内置学习闭环** (从会话中自动提取技能) |
| **多节点协作** | 串行/简单分发 | **原生 ACP 协议** (高性能并发、状态同步) |
| **国内适配** | 需要繁琐插件 | **原生支持 Custom Provider** (一键直连 DeepSeek) |
| **资源占用** | 较高 | 极低 (可在 $5 VPS 稳定运行) |
| **记忆系统** | 简单的历史窗口 | **跨会话持久记忆 + RAG 搜索** |

## 2. Hermes 的三大“杀手锏”

### A. 自动技能进化 (Skill Evolution)
OpenClaw 的工具通常需要手动编写脚本。而在 Hermes 中，当你成功教导 Agent 完成一个复杂任务后，你可以直接说：` /skill_save `。它会把这段成功的逻辑固化为技能，下次直接调用。

### B. ACP (Agent Control Protocol) 协议
Hermes 引入了 ACP 协议，这让“多智能体协作”不再是噱头。通过 `delegate_task`，你可以让 Coder 写代码，QA 同步进行测试，中间状态通过 ACP 实时流转，效率提升 300% 以上。

### C. 极低延迟与模型中立
Hermes 对国内模型（DeepSeek, Qwen）的支持是“一等公民”级别的。通过简单的 `config.yaml` 映射，你可以获得近乎原生的推理速度。

## 3. 迁移指南 (3步搞定)

1. **导出提示词**: 将你 OpenClaw 中的 `system_prompt` 导出为 `.txt` 文件。
2. **编写 Config**: 使用我们提供的 [Starter 模板](https://github.com/zcweah1981/awesome-hermes-agent-zh/tree/main/starters) 建立你的 `config.yaml`。
3. **注入技能**: 将你的自定义工具脚本放入 `/skills` 目录，并在 Hermes 中通过 ` /skill_load ` 载入。

---
*无论你以前在 OpenClaw 积累了多少，Hermes 都能让你以更小的代价获得更强的 AI 能力。*