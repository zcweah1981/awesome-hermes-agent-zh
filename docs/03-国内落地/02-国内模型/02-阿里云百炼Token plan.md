# 阿里云百炼 Token Plan：套餐、API Key 与 Hermes 接入

> 💡 **速答**：阿里云当前提供 Hermes Agent 专项接入说明，Token Plan 个人版和团队版
> 都可通过兼容端点接入。套餐价格、模型清单和促销会变化；配置前仍应以当前官方
> Hermes Agent 页与套餐页确认 Key 类型、Base URL、协议和模型名。

> 🎯 一句话先说清楚：如果你想先买一个"多模型统一入口"，并且希望预算按包月控制、后面还能在阿里云生态里继续扩展，那么阿里云百炼 Token Plan 值得先看。

这一页只解决一件事：帮你判断阿里云百炼 Token Plan 值不值得选，以及怎么按官方 Token Plan 团队版路线把它接进 Hermes。

这一页先不解决：
- 最低门槛起步该选哪条按量接口
- 单厂商会员权益型 Coding Plan 怎么买
- 你已经有 OneAPI / NewAPI / LM Studio / Ollama 时该怎么复用现成兼容层

## 🔎 搜索收录速答

阿里云百炼 Token Plan 适合想用一个 OpenAI-Compatible 入口管理 Qwen、DeepSeek 等模型的 Hermes 用户。你需要重点确认三件事：套餐是否覆盖目标模型、endpoint 是否能按 OpenAI 兼容格式调用、Hermes 里是否把 provider 与 model name 分开配置。想比较其它国内模型，可以继续看[腾讯云 Token Plan](/docs/china/models/tencent-token-plan)、[MiniMax Token Plan](/docs/china/models/minimax-token-plan)和[自定义兼容接口](/docs/china/models/openai-compatible-endpoint)。


## 🚀 先看主线

![阿里云百炼 Token 接入流程示意图（Hermes 风格版）](./assets/aliyun-bailian-tokenplan-hero-v18.webp)

这张图只想帮你先抓住 4 个点：
- 这是一条“统一套餐入口”路线，不是单模型按量页
- 核心价值是多模型可切换、预算更稳定
- 阿里云当前有 Hermes Agent 专项文档，主线是用团队版专属 Key 走兼容协议
- 真正要跑通的是「拿专属 Key → 写入 Hermes → 选模型 → 做最小验证」

如果你现在更想先把第一条链路跑通、先少花钱、先少做选择，这页通常不是第一优先；那种情况通常会先回看 [07-DeepSeek按量计费接口](./07-DeepSeek按量计费接口.md)。

## ✨ 这条路最适合谁

- 你想先买一个统一套餐入口，而不是一个个比较单次调用价格
- 你已经在阿里云生态里，后面也大概率会继续用阿里云相关产品
- 你想让 Hermes 后面能切多家模型，但又不想分别维护多套上游账号
- 你更看重“包月预算可控”，而不是“每次调用是否最低价”
- 你希望把接入、换模型、后续扩展都留在同一个生态里处理

## 🧭 先按你的当前状态分流

| 你的当前情况 | 直接建议 |
|---|---|
| 我只想先最低门槛把 Hermes 跑起来 | 先回看 [07-DeepSeek按量计费接口](./07-DeepSeek按量计费接口.md) |
| 我已经决定优先走阿里云生态 | 留在这页继续 |
| 我想买一个统一套餐，再慢慢切模型 | 留在这页继续 |
| 我已经有稳定 OpenAI-Compatible 兼容层 | 优先看 [08-自定义兼容接口](./08-自定义兼容接口.md) |
| 我还在比较阿里云和腾讯云两条统一套餐路线 | 这页看完后继续看 [03-腾讯云 Token Plan](<./03-%E8%85%BE%E8%AE%AF%E4%BA%91Token%20Plan.md>) |

如果你只记一句话：
- 想先买统一入口、又偏阿里云生态 → 看阿里云百炼 Token Plan
- 只想先跑通 Hermes → 不要先在这页做套餐决策

## 💰 先看价格，再决定值不值得买

阿里云百炼 Token Plan 团队版当前给出三种坐席。下表记录的是官方基础价和固定额度；
标准、高级坐席可能另有短期促销，购买前应再次查看官方页面。

| 坐席 | 官方基础价 | Credits | 适合谁 | 我怎么理解 |
|---|---:|---:|---|---|
| 标准坐席 | ¥198 / 坐席 / 月 | 25,000 Credits / 坐席 / 月 | 轻度使用、先试水 | 最稳的起步档 |
| 高级坐席 | ¥698 / 坐席 / 月 | 100,000 Credits / 坐席 / 月 | 高频使用 AI | 更适合作为团队主力 |
| 尊享坐席 | ¥1,398 / 坐席 / 月 | 250,000 Credits / 坐席 / 月 | 重度依赖 AI 的核心成员 | 更像长期生产力入口 |

### 这页该怎么判断套餐

最简单的判断方式不是先比“理论最划算”，而是先问三件事：
- 你是不是已经接受“先买套餐”这件事
- 你后面会不会真的切多家模型
- 你是不是想把预算控制在固定包月范围内

如果答案都是“是”，这页就值得继续看；如果你对这些还没想清楚，先回 [07-DeepSeek按量计费接口](./07-DeepSeek按量计费接口.md) 这种按量起步页通常更省心。

## 🤖 它为什么值得单独看

### 1）它卖的不是一个模型，而是一个多模型入口

截至 2026-07-28，阿里云 Hermes Agent 专项页给出的 Token Plan 示例包括：
- qwen3.8-max-preview
- qwen3.7-max
- qwen3.7-plus
- qwen3.6-flash
- glm-5.2
- deepseek-v4-pro

模型会更新或下线，完整可用范围应回到 Token Plan 个人版或团队版的“支持的模型”页面确认。

所以它的核心价值不是“押中某一个模型”，而是：
- 先买一个统一入口
- 后面再根据任务切模型
- 把模型选择留到真正开始使用时再细化

### 2）它和阿里云生态的协同更自然

如果你本来就在阿里云里做事，这条路的优势很直接：
- 账号体系更统一
- 后续扩展路径更清楚
- 不需要把“模型套餐”单独拆到另一家生态去维护

### 3）它对工具兼容场景更友好

阿里云官方明确提到，这条路线适配多种主流编程与 Agent 工具，包括：
- Hermes Agent
- OpenClaw
- Qwen Code
- Qoder
- Claude Code
- OpenCode

对 Hermes 用户来说，真正重要的是：
- 这不是只能在官网里用的套餐
- 官方已经明确给了 Hermes 的接法
- 后面换模型时不用重搭整条链路

## 🧰 怎么把阿里云百炼 Token Plan 接进 Hermes

这里的主线按阿里云官方 Hermes 接入文档来走：
- Token Plan 团队版专属 API Key
- 兼容模式 Base URL
- Hermes 写入 custom 配置
- 再做最小验证

### Step 1. 先确认你要走的是 Token Plan 团队版主线

现在做什么：
- 先确认你接入的是 Token Plan 团队版专属入口

为什么做：
- 因为这页的官方主线不是“通用百炼按量 Key”，而是 Token Plan 团队版专属 Key + 兼容模式接入

怎么做：
- 先进入官方 Token Plan 团队版页面
- 确认你拿的是这条套餐路线的专属 Key

看到什么算成功：
- 你已经明确本页主线是 Token Plan 团队版，不是普通 API Key 教程

失败先查什么：
- 如果你手上只有普通百炼按量 Key，说明你看的可能不是这页主线

### Step 2. 获取 Token Plan 团队版专属 API Key

现在做什么：
- 去官方页面拿专属 API Key

为什么做：
- 因为 Hermes 后面要接的就是这把 Key，而不是你自己猜的任意阿里云 Key

怎么做：
- 进入官方 Token Plan 团队版页面
- 找到专属 API Key 的获取入口
- 复制并妥善保存

看到什么算成功：
- 你已经拿到 Token Plan 团队版专属 API Key

失败先查什么：
- 是否进错到通用 API Key 页面
- 是否拿到的不是 Token Plan 团队版专属 Key

### Step 3. 按当前官方 Hermes Agent 说明写入连接参数

现在做什么：
- 把 provider、base_url、api_mode、api_key、model.default 写进 Hermes

为什么做：
- 因为阿里云当前 Hermes Agent 页面默认使用 Anthropic 兼容协议，并明确给出这五项配置

怎么做：
- 在终端里执行：

```bash
hermes config set model.provider custom
hermes config set model.base_url https://token-plan.cn-beijing.maas.aliyuncs.com/apps/anthropic
hermes config set model.api_mode anthropic_messages
hermes config set model.api_key YOUR_API_KEY
hermes config set model.default qwen3.8-max-preview
```

官方也说明 Hermes 支持 OpenAI 兼容协议：此时使用以
`/compatible-mode/v1` 结尾的 Base URL，并移除 `model.api_mode` 配置。两套协议不要混写。

看到什么算成功：
- 这些配置已经写进 Hermes
- 官方说明里的五项映射都对齐了

失败先查什么：
- 是否把 Base URL 写错
- 是否把 Anthropic 与 OpenAI 兼容端点、`api_mode` 混在一起
- 是否把模型名、Key 或 provider 写错

### Step 4. 先用默认文本模型做最小验证

现在做什么：
- 先用一个文本模型确认链路可用

为什么做：
- 因为先证明文字链路能通，比先折腾多模态模型更重要

怎么做：
- 执行：

```bash
hermes chat -q "你好"
```

看到什么算成功：
- Hermes 能正常返回一条文本回复
- 不再报 Base URL / API Key / 模型错误

失败先查什么：
- Key 是否正确
- Base URL 是否仍指向兼容模式入口
- `model.default` 是否仍是当前套餐支持的模型

### Step 5. 需要补充时，再回看通用 API Key 流程

现在做什么：
- 只有在你确实管理的是通用百炼 API Key 时，才去补看那条资料

为什么做：
- 因为这页的主线不是“所有阿里云 Key 的总教程”，而是 Token Plan 团队版接 Hermes

怎么做：
- 把通用 API Key 页面当作补充参考
- 但不要把它和 Token Plan 团队版主线混成一条

看到什么算成功：
- 你已经分清“主线接法”和“补充参考”的边界

失败先查什么：
- 如果你越看越混，说明你把两种 Key 流程混在一起了

## 📎 官方依据截图

### 1. Token Plan 团队版接入说明

![Hermes Agent 配置 Token Plan 团队版的官方说明截图](./assets/aliyun-bailian-hermes-config-section.webp)

这张图只证明三件事：
- 先去 Token Plan 团队版页面拿专属 API Key
- 在 Hermes 里配置 Base URL / API Key / 默认模型
- 配置最终会写入 `~/.hermes/config.yaml`

### 2. 通用百炼 API Key 创建页（补充参考）

![阿里云百炼通用 API Key 创建页截图](./assets/aliyun-bailian-get-api-key-section.webp)

这张图是通用 API Key 创建页，只适合作为补充参考，不应替代 Token Plan 团队版主线。

## ❓FAQ

### 1. 这页为什么不是默认起步页？

因为这页要求你先接受“统一套餐 + 包月预算 + 生态选择”这组决策。

如果你现在只想先跑通 Hermes，按量接口通常更轻、更快。

### 2. 阿里云百炼 Token Plan 和通用百炼 API Key 是一回事吗？

不是。

这页主线强调的是 Token Plan 团队版专属 Key。通用 API Key 页面只是补充参考，不应替代这页主线。

### 3. 我接进 Hermes 后，为什么建议先用文本模型验证？

因为先验证最小文本链路，最容易判断问题究竟在 Key、Base URL、模型名，还是在更复杂的多模态能力上。

## ⚠️ 风险点与默认建议

### 风险点
- 把 Token Plan 团队版专属 Key 和通用百炼 API Key 混为一谈
- 一上来就想测图像模型，结果文字链路都还没跑通
- 其实只想先试跑，却过早做了包月套餐决策

### 默认建议
- 如果你已经明确走阿里云生态，再看这页最值
- 默认先用官方页面当前示例模型做最小验证，并在运行前复核支持列表
- 默认先把文本链路跑通，再去扩展多模态能力

## ➡️ 下一步

完成后进入：
- [03-腾讯云 Token Plan](<./03-%E8%85%BE%E8%AE%AF%E4%BA%91Token%20Plan.md>)

如果你想先回到上一阶段入口重新确认位置：
- [02-国内模型总览](./01-总览.md)

## 📎 官方依据

- https://www.aliyun.com/benefit/scene/tokenplan
- https://help.aliyun.com/zh/model-studio/hermes-agent
- https://help.aliyun.com/zh/model-studio/token-plan-team-overview
- https://help.aliyun.com/zh/model-studio/token-plan-team-quickstart
- https://help.aliyun.com/zh/model-studio/get-api-key

## 🧾 R2 官方同步记录

- source_id: `aliyun-bailian`
- checked_at: `2026-07-28`
- change_type: `official-source-confirmation`
- affected_doc: `docs/03-国内落地/02-国内模型/02-阿里云百炼Token plan.md`
- 本轮结论：已从阿里云当前 Hermes Agent 专项页确认个人版/团队版接入、Anthropic/OpenAI 兼容端点、专属 API Key、`model.default` 字段与验证命令。
- 后续规则：价格仅保留官方基础价快照；促销、可用模型、控制台按钮和额度限制仍以厂商官方页面实时显示为准。
- 官方来源：
  - https://help.aliyun.com/zh/model-studio/hermes-agent
  - https://help.aliyun.com/zh/model-studio/token-plan-team-overview
  - https://help.aliyun.com/zh/model-studio/token-plan-team-quickstart

---

## 🔗 模型接入关联路径

- 还没部署 Hermes：先回到[国内部署](/docs/china/deploy)确认服务器和远程环境。
- 要换国内模型：优先比较[腾讯云](/docs/china/models/tencent-token-plan)和[MiniMax](/docs/china/models/minimax-token-plan)。
- 使用非内置平台：看[自定义兼容接口](/docs/china/models/openai-compatible-endpoint)，再对照[模型 Provider 与自定义 endpoint 问题](/docs/issues/provider-endpoint)。
- 要查环境变量和配置项：进入[环境变量参考](/docs/reference/environment-variables)和[Profile 命令参考](/docs/reference/profile-commands)。
