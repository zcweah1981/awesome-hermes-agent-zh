# 02-阿里云百炼 Token Plan

> 💡 **速答**：阿里云百炼 Token Plan 是多模型统一入口的包月套餐——一个 API Key 可在通义千问、DeepSeek、Qwen 等模型间切换，适合想用套餐控预算的团队。接入 Hermes 走兼容模式，把百炼的 API Key 和 endpoint 填入 Hermes 自定义 provider 即可。

> 🎯 一句话先说清楚：如果你想先买一个"多模型统一入口"，并且希望预算按包月控制、后面还能在阿里云生态里继续扩展，那么阿里云百炼 Token Plan 值得先看。

这一页只解决一件事：帮你判断阿里云百炼 Token Plan 值不值得选，以及怎么按官方 Token Plan 团队版路线把它接进 Hermes。

这一页先不解决：
- 最低门槛起步该选哪条按量接口
- 单厂商会员权益型 Coding Plan 怎么买
- 你已经有 OneAPI / NewAPI / LM Studio / Ollama 时该怎么复用现成兼容层

## 🚀 先看主线

![阿里云百炼 Token 接入流程示意图（Hermes 风格版）](./assets/aliyun-bailian-tokenplan-hero-v18.webp)

这张图只想帮你先抓住 4 个点：
- 这是一条“统一套餐入口”路线，不是单模型按量页
- 核心价值是多模型可切换、预算更稳定
- 官方 Token Plan 团队版接 Hermes 的主线是兼容模式接入
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

阿里云百炼 Token Plan 官方当前给出三档套餐。

| 套餐 | 月费 | Credits | 适合谁 | 我怎么理解 |
|---|---:|---:|---|---|
| 标准版 | ¥198 / 月 | 25,000 Credits / 月 | 轻度使用、先试水 | 最稳的起步档 |
| 高级版 | ¥698 / 月 | 100,000 Credits / 月 | 高频使用 AI | 更适合作为个人主力 |
| 尊享版 | ¥1,398 / 月 | 250,000 Credits / 月 | 重度依赖 AI、多人或高频场景 | 更像长期生产力入口 |

### 这页该怎么判断套餐

最简单的判断方式不是先比“理论最划算”，而是先问三件事：
- 你是不是已经接受“先买套餐”这件事
- 你后面会不会真的切多家模型
- 你是不是想把预算控制在固定包月范围内

如果答案都是“是”，这页就值得继续看；如果你对这些还没想清楚，先回 [07-DeepSeek按量计费接口](./07-DeepSeek按量计费接口.md) 这种按量起步页通常更省心。

## 🤖 它为什么值得单独看

### 1）它卖的不是一个模型，而是一个多模型入口

官方页面能看到的代表模型包括：
- Qwen3.6-Plus
- Qwen-Image-2.0
- Qwen-Image-2.0-Pro
- Wan2.7-Image
- Wan2.7-Image-Pro
- GLM-5
- MiniMax-M2.5
- DeepSeek-V3.2

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

### Step 3. 按官方兼容模式把连接参数写进 Hermes

现在做什么：
- 把 provider、base_url、api_key、model.name 写进 Hermes

为什么做：
- 因为阿里云这条 Token Plan 路线在 Hermes 里的官方主线就是兼容模式接入

怎么做：
- 在终端里执行：

```bash
hermes config set model.provider custom
hermes config set model.base_url https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1
hermes config set model.api_key YOUR_API_KEY
hermes config set model.name qwen3.6-plus
```

看到什么算成功：
- 这些配置已经写进 Hermes
- 官方说明里的四项映射都对齐了

失败先查什么：
- 是否把 Base URL 写错
- 是否误把普通百炼地址当成 Token Plan 团队版地址
- 是否把模型名、Key 或 provider 写错

### Step 4. 先用默认文本模型做最小验证

现在做什么：
- 先用一个文本模型确认链路可用

为什么做：
- 因为先证明文字链路能通，比先折腾多模态模型更重要

怎么做：
- 执行：

```bash
hermes chat -m qwen3.6-plus
```

看到什么算成功：
- Hermes 能正常返回一条文本回复
- 不再报 Base URL / API Key / 模型错误

失败先查什么：
- Key 是否正确
- Base URL 是否仍指向兼容模式入口
- 模型名是否写成了当前套餐入口可识别的文本模型

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
- 默认先用 `qwen3.6-plus` 做最小验证
- 默认先把文本链路跑通，再去扩展多模态能力

## ➡️ 下一步

完成后进入：
- [03-腾讯云 Token Plan](<./03-%E8%85%BE%E8%AE%AF%E4%BA%91Token%20Plan.md>)

如果你想先回到上一阶段入口重新确认位置：
- [02-国内模型总览](./01-总览.md)

## 📎 官方依据

- https://www.aliyun.com/benefit/scene/tokenplan
- https://help.aliyun.com/zh/model-studio/hermes-agent-token-plan
- https://help.aliyun.com/zh/model-studio/get-api-key

## 🧾 R2 官方同步记录

- source_id: `aliyun-bailian`
- checked_at: `2026-05-02`
- change_type: `official-source-confirmation`
- affected_doc: `docs/03-国内落地/02-国内模型/02-阿里云百炼Token plan.md`
- 本轮结论：已确认 Token Plan 团队版 OpenAI/Anthropic 兼容端点、专属 API Key 口径，以及不要混用通用百炼 API Key / Coding Plan Key 的风险。
- 后续规则：涉及价格、套餐、可用模型、控制台按钮和额度限制时，仍以厂商官方页面实时显示为准，不在本文复制长期易变表格。
- 官方来源：
  - https://help.aliyun.com/zh/model-studio/other-tools-token-plan
  - https://help.aliyun.com/zh/model-studio/token-plan-faq

---

## 🔗 模型接入关联路径

- 还没部署 Hermes：先回到[国内部署](/docs/china/deploy)确认服务器和远程环境。
- 要换国内模型：优先比较[DeepSeek](/docs/china/models/deepseek-metered-api)、[Kimi](/docs/china/models/kimi-plan)、[智谱 GLM](/docs/china/models/glm-coding-plan)、[阿里云百炼](/docs/china/models/alibaba-bailian-token-plan)和[腾讯云](/docs/china/models/tencent-token-plan)。
- 使用非内置平台：看[自定义兼容接口](/docs/china/models/openai-compatible-endpoint)，再对照[模型 Provider 与自定义 endpoint 问题](/docs/issues/provider-endpoint)。
- 要查环境变量和配置项：进入[环境变量参考](/docs/reference/environment-variables)和[Profile 命令参考](/docs/reference/profile-commands)。
