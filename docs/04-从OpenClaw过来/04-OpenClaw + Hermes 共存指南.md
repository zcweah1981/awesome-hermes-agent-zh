# OpenClaw + Hermes 共存指南

> 一句话先说清楚：共存不是折中方案，而是从“临时使用”走向“长期复用”的最稳升级路径。

这一页不讨论“要不要立刻迁移”，它只解决一件事：
如果你现在不想全迁，怎样让 OpenClaw 和 Hermes 长期互补共存。

---

## 🎯 先记住这一页最重要的判断

对大多数 OpenClaw 用户来说，最稳的路线不是马上迁移，而是先共存。

你可以继续用 OpenClaw 做前台交互和需求探索，同时让 Hermes 承接那些已经稳定、重复、值得沉淀的流程。

---

## 🧭 结构图：OpenClaw 做前台，Hermes 做后台

![OpenClaw + Hermes 共存结构图：OpenClaw 作为前台交互与探索层，Hermes 作为后台执行与沉淀层，中间最稳路径是先共存再迁移。](./assets/openclaw-hermes-coexistence-structure-v4.webp)

这张图要表达的重点不是“谁更强”，而是：
- OpenClaw 继续负责接收需求、澄清任务、快速试 prompt
- Hermes 负责执行标准化流程、调用 skills、使用 memory、输出稳定结果
- 共存的价值在于：你不用推翻已有生态，就能先把稳定部分抽出来沉淀

---

## 🚦 如果你现在只想快速选一种共存方式

直接按当前状态走：
- 我还习惯 OpenClaw 的对话体验，但想把复杂稳定流程交给 Hermes → 模式 A：OpenClaw 前台，Hermes 后台
- 我还在试 prompt，但已经出现重复任务 → 模式 B：OpenClaw 做实验场，Hermes 做沉淀层
- 我已经开始以 Hermes 为主，只保留 OpenClaw 做临时探索 → 模式 C：Hermes 主系统，OpenClaw 临时工具

如果你现在拿不准，默认先看模式 B。对多数用户来说，这是最稳的一条。

---

## 🧩 三种共存模式分别适合谁

![OpenClaw + Hermes 三种共存模式图：前台/后台、实验场/沉淀层、主系统/临时工具三种模式。](./assets/openclaw-hermes-coexistence-modes-v4.webp)

### 模式 A：OpenClaw 做前台，Hermes 做后台
适合：
- 习惯 OpenClaw 的交互方式
- 希望保留前台对话体验
- 但希望复杂任务由 Hermes 执行

这条模式适合把 OpenClaw 当作入口，把 Hermes 当作执行系统。

### 模式 B：OpenClaw 做实验场，Hermes 做沉淀层
适合：
- 还在试 prompt
- 已经发现某些任务会重复
- 想把稳定经验沉淀下来
- 但不想一次性迁移全部流程

这是本页最重要的一种模式，因为它能解释：
- OpenClaw 不是被替代，而是成为 Hermes 资产沉淀的前置实验场

### 模式 C：Hermes 做主系统，OpenClaw 做临时工具
适合：
- 已经以 Hermes 为主要工作系统
- 已经有 profiles / skills / memory
- 但仍然需要 OpenClaw 做临时探索

这条模式更适合已经开始系统化的人，而不是刚开始接触共存的人。

---

## 📋 哪些内容适合先沉淀给 Hermes

当你选择模式 B 时，最重要的问题不是“搬什么文件”，而是“哪些经验已经值得沉淀”。

| OpenClaw 中的内容 | 更适合沉淀到 Hermes 的方式 |
|---|---|
| 临时 prompt | SOUL / Profile |
| agent 人设 | SOUL.md |
| 工具调用 | SKILL.md |
| 多轮对话经验 | Memory |
| 重复步骤 | Workflow |
| 输出格式 | Template |
| 成功输出 | Example |
| 失败经验 | Known Issues / 注意事项 |

关键不是复制 prompt，而是把已经被验证过的经验，转成 Hermes 可以长期维护的结构。

---

## 🛠 共存应该怎么一步步推进

![OpenClaw + Hermes 共存操作图：从 OpenClaw 为主，到 OpenClaw + Hermes 并行，再到 Hermes 为主的三阶段推进。](./assets/openclaw-hermes-coexistence-operation-v4.webp)

一个更稳的推进顺序通常是：

### 阶段 1：OpenClaw 为主
重点：
- 找到真实需求
- 试 prompt
- 试 agent 组合
- 看输出是否有价值

这个阶段不要急着写 skills，也不要急着设计复杂结构。

### 阶段 2：OpenClaw + Hermes 并行
重点：
- 提炼 SOUL
- 拆 SKILL
- 收集 examples
- 建 templates
- 选择模型和入口

这个阶段的目标不是一次性迁完，而是把稳定部分单独沉淀出来。

### 阶段 3：Hermes 为主
重点：
- profiles 固化
- skills 标准化
- memory 持续积累
- cron / workflow 自动化
- 团队入口接入

只有当前两个阶段已经跑顺，才值得进入这一层。

---

## ✅ 共存成功标准

如果共存做对了，应该出现这些结果：
- 不再每次重复写 prompt
- 同类任务输出更稳定
- 角色边界更清楚
- 关键流程可以复用
- 可以换模型
- 可以接 Web UI / CLI / 飞书 / 企业微信 / 钉钉
- 可以逐步自动化
- 成本更可控

---

## ⚠️ 共存不适合谁

不适合：
- 只是偶尔问答
- 没有重复任务
- 不需要沉淀
- 不想维护任何配置
- 连一个稳定案例都没有跑通

如果你还没有跑通过一个稳定案例，先继续用 OpenClaw 探索，不要急着进入共存阶段。

---

## ✅ 看完这页你应该能立刻判断什么

看完后你应该能直接回答这 4 个问题：
1. 共存是不是妥协，还是最稳的升级方式？
2. 我更适合哪一种共存模式？
3. 我应该先把哪个环节交给 Hermes？
4. 我现在是不是还没到该迁移主系统的时候？

---

## ➡️ 下一步

完成后进入：
- [从 OpenClaw 到 Hermes：迁移路径](<./05-%E4%BB%8E%20OpenClaw%20%E5%88%B0%20Hermes%EF%BC%9A%E8%BF%81%E7%A7%BB%E8%B7%AF%E5%BE%84.md>)

如果你想先回到上一阶段入口重新确认位置：
- [04-从OpenClaw过来 | 总览](./01-总览.md)

---

## 🔗 共存后的下一步

- 共存稳定后，如果要逐步迁移：看[迁移路径](/docs/openclaw/migration-path)。
- 如果共存时出现配置冲突：看[配置 Profiles 与环境隔离问题](/docs/issues/config-profiles-environment)。
- 需要查 Hermes Profiles：看[Profile 命令参考](/docs/reference/profile-commands)。
- 想把 OpenClaw 经验沉淀为 Hermes 用法：看[多个助手一起工作](/docs/start/build/profiles)和[上下文系统](/docs/start/build/context-system)。
