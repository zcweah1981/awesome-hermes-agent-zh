# 04-智谱 GLM Coding Plan

> 🎯 一句话先说清楚：如果你已经偏向 GLM / z.ai 这一家，并且想用一条原生 provider 路线把 Hermes 接进去，而不是再套一层 custom endpoint，那么 GLM Coding Plan 值得先看。

这一页只解决一件事：帮你判断 GLM Coding Plan 值不值得买，以及怎么按 Hermes 原生 `z.ai / GLM` provider 路线把它接起来。

这一页先不解决：
- 最低门槛按量起步应该选哪条路
- 统一套餐聚合入口该选阿里云还是腾讯云
- 你已经有 OneAPI / NewAPI / LM Studio / Ollama 时该怎么复用兼容层

## 🚀 先看主线

![智谱 GLM Coding Plan 主线图](./assets/glm-coding-hero-v1.png)

这张图只想帮你先抓住 4 个点：
- 这是一条“单厂商深用”路线，不是统一聚合套餐页
- Hermes 已原生支持 `z.ai / GLM` provider
- 这页更适合已经决定重点看 GLM 的人
- 真正要跑通的是「订阅 / 获取 Key → 写入 `GLM_API_KEY` → `hermes model` 选 GLM → 做最小验证」

如果你现在更想先少花钱、少做选择、先验证 Hermes 能不能通，优先回看 [07-DeepSeek按量计费接口](./07-DeepSeek按量计费接口.md)。

## ✨ 这条路最适合谁

- 你已经认准 GLM / z.ai 这条产品线，想深用一家而不是继续横向比较
- 你想走 Hermes 原生 provider 路线，而不是先折腾 custom endpoint
- 你更看重单厂商的编码体验、模型能力和生态一致性
- 你愿意先做一次厂商选择，再把后面的工作流稳定下来
- 你准备长期把 GLM 放进自己的开发流程里

## 🧭 先按你的当前状态分流

| 你的当前情况 | 直接建议 |
|---|---|
| 我只想先最低门槛把 Hermes 跑起来 | 先回看 [07-DeepSeek按量计费接口](./07-DeepSeek按量计费接口.md) |
| 我已经认准 GLM / z.ai | 留在这页继续 |
| 我更想先买统一多模型入口 | 先回看 [02-阿里云百炼 Token Plan](<./02-%E9%98%BF%E9%87%8C%E4%BA%91%E7%99%BE%E7%82%BCToken%20plan.md>) 或 [03-腾讯云 Token Plan](<./03-%E8%85%BE%E8%AE%AF%E4%BA%91Token%20Plan.md>) |
| 我已经有稳定兼容层 | 优先看 [08-自定义兼容接口](./08-自定义兼容接口.md) |

如果你只记一句话：
- 认准 GLM 并想走 Hermes 原生 provider → 看这页
- 只是想先跑通 Hermes → 不要先在这页做单厂商深度决策

## 💰 先看它卖的是什么，再决定值不值得买

GLM Coding Plan 的判断逻辑，不是先问“有没有最低单次价格”，而是先问三件事：
- 你是不是已经愿意优先押 GLM 这家
- 你是不是想用一条原生 provider 路线接 Hermes
- 你是不是更关心单厂商编码体验，而不是多厂商统一入口

如果答案都是“是”，这页值得继续；如果还没到这一步，先回按量页或聚合套餐页通常更省决策成本。

## 🤖 它为什么值得单独看

### 1）它是单厂商深用路线，不是统一聚合页

这页的核心价值不在“同时买很多家模型”，而在：
- 先押一条 GLM 路线
- 把 Hermes、模型、工作流理解都收敛到同一家
- 减少中间兼容层和生态切换的复杂度

### 2）Hermes 已经原生支持 GLM provider

Hermes 官方 provider 文档已经明确列出：
- 环境变量：`GLM_API_KEY`
- provider：`zai`

这件事非常关键，因为它意味着：
- 不需要先把 GLM 包装成 custom endpoint
- 不需要先研究 OpenAI-compatible 中间层
- 你可以直接按 Hermes 原生 provider 路线来理解和配置

### 3）它更适合“已经决定认准一家”的阶段

这页和统一套餐页最大的不同在于：
- 统一套餐页是在帮你买一个入口
- GLM Coding Plan 更像是在帮你做“单厂商长期路线”决策

所以它不是第一站，而是“你已经想清楚要重点看 GLM”之后的页。

## 🧰 怎么把 GLM 接进 Hermes

这页的主线按 Hermes 原生 provider 路线来走：
- 拿到 GLM API Key
- 写入 `~/.hermes/.env`
- 在 `hermes model` 里选 `z.ai / GLM`
- 做最小验证

### Step 1. 先确认你要走的是原生 provider 路线

现在做什么：
- 先确认你不是要接自定义兼容层，而是要直接接 GLM 原生 provider

为什么做：
- 因为 Hermes 已经原生支持 GLM，这页没必要先把事情做复杂

怎么做：
- 如果你有的是 GLM 官方 API Key，就留在这页继续
- 如果你手里是第三方聚合层地址或企业网关，优先看 [08-自定义兼容接口](./08-自定义兼容接口.md)

看到什么算成功：
- 你已经明确这页讲的是 GLM 原生 provider，不是 custom endpoint

失败先查什么：
- 如果你脑子里一直在想 base_url 怎么填，说明你更像是兼容层场景

### Step 2. 获取 GLM API Key

现在做什么：
- 去 GLM / z.ai 官方入口拿到 API Key

为什么做：
- 因为后面的 Hermes provider 就是按 `GLM_API_KEY` 读取凭据

怎么做：
- 完成你选择的订阅 / 开通流程
- 在官方开发者或控制台入口里生成 API Key
- 保存好这把 Key

看到什么算成功：
- 你已经拿到可用的 `GLM_API_KEY`

失败先查什么：
- 是否还没真正完成开通或订阅
- 是否复制了错误字段而不是 API Key 本身

### Step 3. 把 `GLM_API_KEY` 写进 `~/.hermes/.env`

现在做什么：
- 在 Hermes 环境变量文件里写入 GLM Key

为什么做：
- 因为 Hermes 官方 provider 文档就是按这个变量读取 GLM 凭据

怎么做：
- 打开 `~/.hermes/.env`
- 写入：

```bash
GLM_API_KEY=***
```

看到什么算成功：
- `~/.hermes/.env` 里已经有一行 `GLM_API_KEY=***

失败先查什么：
- 是否写错变量名
- 是否写进了别的文件而不是 `~/.hermes/.env`
- 是否复制时混入了空格、引号或残缺值

### Step 4. 用 `hermes model` 选择 `z.ai / GLM`

现在做什么：
- 在 Hermes 里把 provider 切到 GLM

为什么做：
- 只有 provider 真正切过去，后面的会话才会走 GLM

怎么做：
- 运行：

```bash
hermes model
```

- 在 provider 列表里选择 `z.ai / GLM`
- 再选择你当前要测试的 GLM 模型

官方文档截图里也能看到 Hermes 的 provider 选择入口：

![Hermes model 设置截图：选择 GLM / z.ai provider](./assets/glm-hermes-model-menu-docs.png)

看到什么算成功：
- Hermes 已经保存 GLM 作为当前 provider
- 模型已切到你准备测试的那一档

失败先查什么：
- `GLM_API_KEY` 是否已经被 Hermes 正常读取
- 你是不是还停留在别的 provider 上
- 当前模型是否是你账号真正可用的模型

### Step 5. 先做一次最小验证

现在做什么：
- 先用一条最简单的问题证明链路可用

为什么做：
- 因为“Key 已写入”不等于“模型真的能返回结果”

怎么做：
- 启动 Hermes
- 先发一句最短问题，例如让它做一句自我介绍
- 先确认会话能正常返回，再继续跑更复杂的任务

看到什么算成功：
- Hermes 能正常进入会话
- 不再报 provider / API Key 错误
- GLM 模型能稳定返回一条回复

失败先查什么：
- Key 是否复制错误
- provider 是否没有真正切到 GLM
- 模型是否选到了当前账号不可用的那一档

## ❓FAQ

### 1. 这页为什么不是默认起步页？

因为这页默认你已经做了“我要重点看 GLM / z.ai”这个厂商选择。

如果你现在只是想先跑通 Hermes，按量页通常更轻。

### 2. 为什么这里不先讲 custom endpoint？

因为 Hermes 已经原生支持 GLM provider。

只有在你不是拿官方 GLM Key、而是拿第三方兼容层地址时，才更应该去看自定义兼容接口页。

### 3. 这页最核心的配置是什么？

最核心的就是两件事：
- `GLM_API_KEY`
- 在 `hermes model` 里选 `z.ai / GLM`

## ⚠️ 风险点与默认建议

### 风险点
- 其实是兼容层场景，却误把自己当成原生 provider 场景
- 还没完成开通，就直接在 Hermes 里切 provider
- 一上来就折腾复杂模型，而不是先做最小验证

### 默认建议
- 如果你已经认准 GLM，再看这页最值
- 默认先走原生 provider，不要先走 custom endpoint
- 默认先完成一次最小验证，再去细化模型和工作流

## ➡️ 下一步

完成后进入：
- [05-MiniMax Token Plan](<./05-MiniMax%20Token%20Plan.md>)

如果你想先回到上一阶段入口重新确认位置：
- [02-国内模型总览](./01-总览.md)

## 📎 官方依据

- https://hermes-agent.nousresearch.com/docs/integrations/providers
- https://z.ai/subscribe
- https://docs.z.ai/

## 🧾 R2 官方同步记录

- source_id: `zhipu-glm`
- checked_at: `2026-05-02`
- change_type: `official-source-confirmation`
- affected_doc: `docs/03-国内落地/02-国内模型/04-智谱GLM Coding Plan.md`
- 本轮结论：已确认 GLM Coding Plan 快速开始、API Key 获取、Claude Code/通用兼容配置和 HTTP API 端点口径。
- 后续规则：涉及价格、套餐、可用模型、控制台按钮和额度限制时，仍以厂商官方页面实时显示为准，不在本文复制长期易变表格。
- 官方来源：
  - https://docs.bigmodel.cn/cn/coding-plan/quick-start
  - https://docs.bigmodel.cn/cn/guide/develop/http/introduction

---

## 🔗 模型接入关联路径

- 还没部署 Hermes：先回到[国内部署](/docs/china/deploy)确认服务器和远程环境。
- 要换国内模型：优先比较[DeepSeek](/docs/china/models/deepseek-metered-api)、[Kimi](/docs/china/models/kimi-plan)、[智谱 GLM](/docs/china/models/glm-coding-plan)、[阿里云百炼](/docs/china/models/alibaba-bailian-token-plan)和[腾讯云](/docs/china/models/tencent-token-plan)。
- 使用非内置平台：看[自定义兼容接口](/docs/china/models/openai-compatible-endpoint)，再对照[模型 Provider 与自定义 endpoint 问题](/docs/issues/provider-endpoint)。
- 要查环境变量和配置项：进入[环境变量参考](/docs/reference/environment-variables)和[Profile 命令参考](/docs/reference/profile-commands)。
