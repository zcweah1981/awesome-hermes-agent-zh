# 06-Kimi登月计划

> 🎯 一句话结论：如果你更看重 Kimi 的 Coding 体验，或者你正在判断“先买会员权益”还是“直接走开放平台按量接口”，Kimi 这页必须拆成两条线看：**Kimi Code** 和 **Kimi API**。

这一页沿用前一页更清楚的写法：先讲适合谁、价格和权益怎么选、它到底强在哪，再讲真正适合接 Hermes 的是哪一条。

## 🚀 接入主线图

![Kimi登月计划核心与四模块结构图](./assets/kimi-moonshot-modules-cliproxy-v2.png)

先看图，Kimi 这条线最关键的不是先背命令，而是先认清两层边界：

- **Kimi Code**：会员体系里的 Coding 权益
- **Kimi API**：开放平台按量计费接口

这两层如果不先拆开，后面无论买套餐、配工具，还是接 Hermes，都会越看越乱。

## ✨ 这条路适合谁

- 你已经对 Kimi 的 coding 能力有兴趣，想认真比较它值不值得买
- 你想先看会员权益，再判断要不要走 API 路线
- 你希望在长文本写作、日常助理和编程之间共享一套能力体系
- 你不想把“会员型 Coding 权益”和“开放平台按量接口”混为一谈
- 你已经明确会在 Kimi CLI、Claude Code、Roo Code 或 Hermes 这类工具里长期使用模型

## 🧭 先看最短决策

| 你的情况 | 建议 |
|---|---|
| 你想先买一套 Coding 权益，直接进开发工具里用 | 走 **Kimi Code / 登月计划** |
| 你想按量付费，自己接 Hermes、脚本或自定义工作流 | 走 **Kimi API** |
| 你最关心的是价格门槛低、先跑通再说 | 优先回看 [07-DeepSeek按量计费接口](./07-DeepSeek按量计费接口.md) |
| 你还没想清楚是会员还是 API | 先回 [国内模型总览](../01-总览.md) |

如果你只想记住一句话：

- **想买 Coding 权益 → 看 Kimi Code**
- **想接 Hermes / 按量调用 → 看 Kimi API**

## 💰 价格和权益怎么选

Kimi 官方会员定价页当前默认展示的是**年付视图**，这一页先按官方当前展示价来写；如果你打开官网时切到了月付，请以官网实时页面为准。

### Kimi Code 对应的会员档位

| 档位 | 官方当前展示价 | Kimi Code 权益 | 适合谁 | 我怎么理解 |
|---|---:|---|---|---|
| Moderato | $180 / 年 | Kimi Code 1x credits | 先体验 Kimi Code | 先感受 Coding 能力 |
| Allegretto | $372 / 年 | Kimi Code 5x credits | 日常高频开发 | 更适合作为个人主力档 |
| Allegro | $948 / 年 | Kimi Code 15x credits | 重度编码与多任务 | 更适合把 Kimi 当长期工具 |
| Vivace | $1,908 / 年 | Kimi Code 30x credits | 大项目 / 高强度使用 | 面向最重度开发与代码库场景 |

### Kimi Code 这一页真正该怎么看

Kimi 会员页不是单独卖一个“代码模型”，而是把 **Kimi Code** 放进整套会员权益里。

这意味着你买的不是一个孤立接口，而是一套更偏产品化的体验：

- Kimi Code 作为会员权益可直接使用
- 同时共享 Kimi 会员体系里的其他能力
- 按不同会员档位给不同倍数的 Kimi Code credits

所以这页的第一判断不是“API 单价多少”，而是：**你要不要为 Kimi 的整套开发体验买单。**

## 🏆 它的核心优势到底是什么

这一页的关键不是“它能不能生成代码”这么简单，而是：**Kimi Code 为什么值得单独拿出来讲。**

### 1）它首先是一种会员型 Coding 权益

官方文档把 Kimi Code 定义成：

- Kimi 生态里的 premium subscription tier
- 专门面向开发者的高级 AI Coding 能力

这和单纯的开放平台按量 API 不一样：

- 它更像“为开发流程准备好的会员权益”
- 重点是工作流体验，而不是单次接口调用

### 2）它对现有开发工具很友好

Kimi Code 文档明确强调它可兼容：

- **Kimi Code CLI**
- **Claude Code**
- **Roo Code**

这意味着它并不是一个只能在官网里点点试试的能力，而是想直接切进开发工具链。

### 3）性能卖点很明确

官方文档给出的重点包括：

- 输出速度最高可达 **100 Tokens/s**
- 5 小时 token 配额大约支持 **300–1,200 次** API 调用
- 最大并发可到 **30**

如果你最关心的是 Coding 速度、连续跑任务能力和稳定性，这些点都比“会不会写代码”更重要。

### 4）它仍然保留了开放平台那条线

Kimi 平台文档说明得很清楚：开放平台这一层提供了完整的 API 文档、Chat、Tool Use、文件接口、余额查询、定价和入门指南。

所以 Kimi 不是只有会员路线，它同时还有：

- **Kimi Code**：会员权益型路线
- **Kimi API**：开放平台按量接口路线

## 🔀 Kimi Code 和 Kimi API 到底怎么分

### 1）Kimi Code：偏“买体验”

更适合这类人：

- 你希望直接进入 Coding 工作流
- 你愿意为会员权益和更完整体验付费
- 你主要用 Kimi CLI、Claude Code、Roo Code 这类开发工具

### 2）Kimi API：偏“买接口”

更适合这类人：

- 你要按量计费，自己控制用量
- 你想把模型接到 Hermes、脚本、自定义 Agent 或其他开发系统里
- 你不想先买会员，只想先把接口跑通

这一页最重要的结论就是：

**想接 Hermes，重点看的是 Kimi API；想买 Coding 权益，重点看的是 Kimi Code。**

## 🧰 Hermes 怎么接 Kimi 这条线

这里不要混淆主线。

### 1）如果你买的是 Kimi Code

你应该优先按 Kimi Code 官方文档走：

- 先在 Kimi Code 官方站购买对应会员档位
- 进入 Console 管理 API Keys 或设备授权
- 按官方支持的开发工具接入，例如 Kimi Code CLI、Claude Code、Roo Code

这条路更偏**会员权益型 Coding 使用**，不是本页里最适合当作 Hermes 主线的部分。

### 2）如果你要接 Hermes

这页真正适合 Hermes 的，是 **Kimi API 开放平台** 这一条：

- 先去 Kimi 开放平台申请 API Key
- 再看开放平台文档里的入门指南、价格与计费、限速说明
- 按你的实际接入方式完成配置

你可以把它理解成：

- **Kimi Code**：偏会员产品线
- **Kimi API**：偏开发者接口线

如果你的目标是“把 Hermes 跑通”，优先级应落在 **Kimi API**，而不是把会员权益当成 Hermes 默认入口。

## ✅ 这页对 Kimi 的默认建议

如果你问我：Kimi 这页最该强调什么？

我的结论是：

- 不是先强调命令怎么配
- 而是先强调 **Kimi Code 和 Kimi API 必须分开看**

对比这一模块里其他页面后，Kimi 这页最值得强调的差异点是：

- 它同时存在会员权益路线和开放平台路线
- Kimi Code 更偏工作流体验
- Kimi API 更偏按量接口能力
- 你必须先选“买体验”还是“买接口”

如果你是下面这类人，Kimi 这页值得优先看：

- 已经认准 Kimi 的 Coding 体验
- 不想只看按量接口，而是要看整套开发体验值不值得买
- 想在会员权益和开放平台之间做清楚判断
- 准备把 Kimi 放进长期开发工作流里

## ⚠️ 常见问题

### 1. 这一页为什么要把 Kimi Code 和 Kimi API 分成两条线？

因为它们本质不同：

- Kimi Code 是会员权益
- Kimi API 是开放平台接口

如果不拆开，这页会把“买会员”和“接 API”混成一件事，读者会越看越乱。

### 2. 我如果只想接 Hermes，应该先看哪一条？

优先看 **Kimi API**。

因为 Hermes 主线更适合按开放平台接口来理解，而不是把会员权益当作默认接入口。

### 3. 我如果更看重 Coding 体验而不是 API 灵活性呢？

那就优先看 **Kimi Code / 登月计划**。

这条路的卖点不是“最低门槛”，而是“更完整的开发体验”。

## ➡️ 下一步

完成后进入：

- 如果你想继续看另一条单厂商路线，继续看 [07-DeepSeek按量计费接口](./07-DeepSeek按量计费接口.md)
- 如果你还在横向比较，回 [国内模型总览](../01-总览.md)

## 📎 官方依据

- https://www.kimi.com/code?track_id=9fde7b48-4728-4f8d-bdcf-fcae84046a80
- https://www.kimi.com/code/docs/en/
- https://www.kimi.com/membership/pricing
- https://platform.kimi.com/docs/overview
