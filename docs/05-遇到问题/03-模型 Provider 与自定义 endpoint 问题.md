# 03-模型 / Provider / 自定义 endpoint 问题

> 🎯 一句话结论：这一页不是教你重新接一遍模型，而是集中回答“为什么 API Key 不通过、为什么 401 / 403 / 404 / 429 一直报、为什么 model 不存在、为什么 custom endpoint 看起来能连但实际不稳定”这类高频问题。

如果你现在最焦虑，只先记住一句：

> 只要 `hermes version` 和 `hermes doctor` 还能正常跑，模型 / Provider 问题通常就不是安装层，而是鉴权、模型名、endpoint 或兼容能力没对齐。

## 这页主要回答什么

这一页集中回答这几类高频问题：

- 为什么 API Key 明明填了还是不通过？
- 为什么一直报 401 / 403 / 404 / 429？
- 为什么提示 model 不存在或选不到模型？
- 为什么 custom endpoint 能聊天，但一到工具 / system role / function calling 就开始异常？
- 什么情况下优先用 Hermes 官方 provider，什么情况下才该走自定义兼容接口？

## 先做一个最小判断

如果你现在完全不知道问题卡在哪，先跑这 3 条：

```bash
hermes model
hermes version
hermes doctor
```

这 3 条的作用不是立刻修好，而是先帮你判断：

- 是 provider 没选对
- 是 API Key / 权限有问题
- 是 model 名称或 context 不匹配
- 还是 custom endpoint 的兼容层本身不完整

## ⚡ 快速定位：先看你的问题

如果你不想从头往下读，先按你眼前最像的现象直接跳：

### 🔐 API Key / 鉴权不过
- 1️⃣ [为什么 API Key 明明填了还是不通过？](#faq-api-key-invalid)
- 2️⃣ [为什么一直报 401 / 403？](#faq-401-403)

### 🌐 endpoint / 连接异常
- 3️⃣ [为什么一直报 404 或 endpoint 不存在？](#faq-404-endpoint)
- 4️⃣ [为什么一直报 Connection timeout 或连不上？](#faq-timeout)

### 🧩 model / provider 不匹配
- 5️⃣ [为什么提示 model 不存在、选不到，或者一选就报错？](#faq-model-not-found)
- 6️⃣ [什么时候优先用 Hermes 官方 provider，而不是 custom endpoint？](#faq-official-vs-custom)

### 🇨🇳 自定义兼容层 / 国内中转
- 7️⃣ [为什么 custom endpoint 能聊天，但 tools / system role / function calling 不稳定？](#faq-custom-capability)
- 8️⃣ [国内中转 / OpenAI-Compatible 兼容层最容易出什么问题？](#faq-china-compatible)
- 9️⃣ [什么情况下该回 03-国内落地，而不是继续在这里硬调？](#faq-when-back-to-china)

> 📌 建议阅读顺序
> - 先看：🔐 API Key / 鉴权不过
> - 再看：🌐 endpoint / 连接异常
> - 然后看：🧩 model / provider 不匹配
> - 最后看：🇨🇳 自定义兼容层 / 国内中转

## ❓FAQ 正文

<a id="faq-api-key-invalid"></a>

### 🔐 01｜为什么 API Key 明明填了还是不通过？

> ❓ 问题：为什么 API Key 明明填了还是不通过？
>
> 💡 先说结论：最常见原因不是“这个 Key 完全不能用”，而是 Key 放错位置、provider 选错、环境变量名不对，或者你以为在走官方 provider，实际却还在走旧的 custom endpoint。

最常见原因是：

- Key 填进了错误的环境变量名
- 你当前选的 provider 和 Key 对不上
- `~/.hermes/.env` 里有值，但当前实际生效的 profile 不是这份环境
- 你以为已经切到官方 provider，但 `config.yaml` 还保留着旧 endpoint

🔎 先做什么：

先重新进入交互式 provider 选择：

```bash
hermes model
```

然后确认两件事：

1. 你当前实际选中的 provider 是谁
2. 这个 provider 对应的 Key 是否放在官方要求的变量名里

官方 provider 文档里已经明确：

- OpenRouter → `OPENROUTER_API_KEY`
- z.ai / GLM → `GLM_API_KEY`
- Kimi → `KIMI_API_KEY`
- DeepSeek → `DEEPSEEK_API_KEY`
- Gemini → `GOOGLE_API_KEY` / `GEMINI_API_KEY`
- Custom Endpoint → 通过 `hermes model` 写入 `config.yaml`

🚦 什么时候该跳转：

- 如果你连 provider 是谁都没法确认，先留在本页
- 如果 provider 已确认，但问题明显是国内路线选择错误，转去 [03-国内落地 / 01-总览](../03-国内落地/01-总览.md)

---

<a id="faq-401-403"></a>

### 🔐 02｜为什么一直报 401 / 403？

> ❓ 问题：为什么一直报 401 / 403？
>
> 💡 先说结论：401 / 403 大多不是 Hermes 本体坏了，而是鉴权失败、权限不足、订阅层级不够，或者你拿错了 provider 的 Key。

最常见区别可以这样理解：

- `401`：更像是没认证上、Key 错、token 失效
- `403`：更像是认证到了，但权限不够、模型无权限、账户套餐不支持

🔎 先做什么：

优先排这几件事：

- Key 是否真的属于当前 provider
- 你请求的模型是否在当前账户权限范围内
- 你是不是把国内 / 国际线路的 Key 混用了
- 你是不是以为在走官方 provider，实际还在走 custom endpoint

如果你用的是国内 provider，尤其要注意：

- 同一厂商不同产品线可能不是同一套 Key
- 国内版 / 国际版通常不是一把 Key 通吃

🚦 什么时候该跳转：

- 如果你已经确认是套餐 / 额度 / 权限问题，转去对应厂商页
- 如果你连当前走的是哪条 provider 路线都说不清，继续留在本页

---

<a id="faq-404-endpoint"></a>

### 🌐 03｜为什么一直报 404 或 endpoint 不存在？

> ❓ 问题：为什么一直报 404 或 endpoint 不存在？
>
> 💡 先说结论：这类问题最常见不是模型坏了，而是 `base_url`、`/v1` 路径、provider 路径前缀，或者 endpoint 类型本身就写错了。

最常见原因是：

- `base_url` 多写了一层 `/v1`
- `base_url` 少了一层 `/v1`
- 你把官方 provider 当成 custom endpoint 去填
- 你把聊天接口地址直接当 base_url，而不是填服务根地址

🔎 先做什么：

如果你走的是 custom endpoint，先重点查：

- `base_url` 到底应该写服务根地址还是 `/v1` 地址
- 你接的是 OpenAI-compatible，还是别的协议
- 这个 endpoint 是否真的暴露了 `/models`、`/chat/completions` 或 `/responses`

尤其在国内兼容层里，最容易出现：

- `/v1` 重复
- `/v1` 缺失
- 网关路径被二次代理改写

🚦 什么时候该跳转：

- 如果你用的是本地兼容层 / OneAPI / NewAPI / Ollama / LM Studio，优先去看 [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)
- 如果你其实应该走官方 provider，不要继续硬调 endpoint，回 `hermes model` 重选

---

<a id="faq-timeout"></a>

### 🌐 04｜为什么一直报 Connection timeout 或连不上？

> ❓ 问题：为什么一直报 Connection timeout 或连不上？
>
> 💡 先说结论：timeout 大多不是 Hermes 逻辑错误，而是网络层、代理层、本地服务没起来，或者 endpoint 所在区域根本不通。

最常见原因是：

- 本地模型服务根本没启动
- 代理只让浏览器通，不让终端通
- 国内 / 国际网络路径不一致
- 你填的是一个存在但不可达的内网地址
- 远端 endpoint 本身可用性差

🔎 先做什么：

优先先确认：

- 这个服务在不在运行
- 这个地址是不是当前机器真的能访问到
- 你是不是把局域网地址、本地地址、云主机地址混用了

如果你是本地模型路线，超时尤其要先怀疑：

- 模型还没加载完成
- 本地服务其实没起来
- context 太大导致首包时间很慢

🚦 什么时候该跳转：

- 如果你确认是云主机 / 国内网络 / 部署层问题，回 [03-国内落地 / 01-总览](../03-国内落地/01-总览.md)
- 如果你确认是本地兼容服务问题，回 [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)

---

<a id="faq-model-not-found"></a>

### 🧩 05｜为什么提示 model 不存在、选不到，或者一选就报错？

> ❓ 问题：为什么提示 model 不存在、选不到，或者一选就报错？
>
> 💡 先说结论：最常见不是 Hermes 不认识模型，而是你填的 model 名不等于 provider 真正识别的模型字符串，或者 context / 能力要求根本不满足。

最常见原因是：

- model 名写成了你自己的叫法，不是 provider 真正识别的名字
- 你当前账户没有这个模型的权限
- custom endpoint 暴露的模型名和你手填的不一致
- 模型 context 太小，不满足 Hermes 要求

官方 Quickstart 已经明确：

- Hermes Agent 要求模型至少有 **64,000 tokens context**

也就是说，有些模型不是“完全不存在”，而是即使能连上，也不适合作为 Hermes 主模型。

🔎 先做什么：

优先回到：

```bash
hermes model
```

重新确认：

- 你当前 provider 下到底有哪些可选模型
- 你是否手填了不存在的模型名
- 你当前路线是不是应该换成官方 provider，而不是继续手填 custom model 名

🚦 什么时候该跳转：

- 如果你是在国产路线里挑模型，转去 [02-国内模型 | 总览](../03-国内落地/02-国内模型/01-总览.md)
- 如果你只是 custom endpoint 模型名对不上，继续留在本页或去自定义兼容接口页

---

<a id="faq-official-vs-custom"></a>

### 🧩 06｜什么时候优先用 Hermes 官方 provider，而不是 custom endpoint？

> ❓ 问题：什么时候优先用 Hermes 官方 provider，而不是 custom endpoint？
>
> 💡 先说结论：只要 Hermes 已经对这个厂商有官方 provider，默认先走官方 provider；custom endpoint 更适合“你已经有稳定兼容层”的场景。

为什么默认先走官方 provider：

- 少一层中转
- 少一层兼容误差
- 配置链路更短
- 排错边界更清楚

什么时候更适合 custom endpoint：

- 你已经有稳定 OpenAI-compatible 兼容层
- 你要接本地 Ollama / LM Studio / 企业网关
- 你明确知道自己为什么需要统一入口

🚦 什么时候该跳转：

- 如果你只是第一次把 Hermes 跑通，不要先走 custom endpoint
- 如果你已经有 OneAPI / NewAPI / 本地兼容层，再去看 [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)

---

<a id="faq-custom-capability"></a>

### 🇨🇳 07｜为什么 custom endpoint 能聊天，但 tools / system role / function calling 不稳定？

> ❓ 问题：为什么 custom endpoint 能聊天，但 tools / system role / function calling 不稳定？
>
> 💡 先说结论：因为“能聊天”只证明最基础的文本推理链路通了，不等于这个兼容层完整支持 Hermes 需要的全部能力。

这是 OpenAI-compatible 兼容层里最常见的误判之一。

最常见原因是：

- 兼容层只做了最基础聊天接口
- 对 tools / function calling 支持不完整
- 对 system role 处理不一致
- 流式输出、模型列表、响应格式做了部分兼容

所以一个 endpoint 出现下面情况，并不奇怪：

- 普通聊天能用
- 一到工具调用就异常
- 一到复杂 agentic workflow 就开始不稳定

🔎 先做什么：

先不要急着改 Hermes，先承认这更像兼容层能力边界问题。

然后判断：

- 你是不是应该直接切回官方 provider
- 你是不是应该更换兼容层
- 你是不是只把它当“能跑轻量聊天”的临时入口

🚦 什么时候该跳转：

- 如果你要的是稳定 Agent 工作流，优先回官方 provider
- 如果你要继续用兼容层，回 [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)

---

<a id="faq-china-compatible"></a>

### 🇨🇳 08｜国内中转 / OpenAI-Compatible 兼容层最容易出什么问题？

> ❓ 问题：国内中转 / OpenAI-Compatible 兼容层最容易出什么问题？
>
> 💡 先说结论：最常见不是“完全连不上”，而是路径、模型名、权限、能力支持范围、国内外线路混用这些半通不通的问题。

最常见问题包括：

- `/v1` 缺失或重复
- 模型名和上游实际暴露名不一致
- 国内版 / 国际版接口混用
- 能聊天但 tools 不稳定
- 中转层做了自己的限流、鉴权、重写
- 账户看似有额度，但当前模型无权限

🔎 先做什么：

优先把问题拆成 4 层：

1. 地址对不对
2. Key 对不对
3. model 名对不对
4. 兼容能力够不够

不要把这 4 层混成一句“custom endpoint 不行”。

🚦 什么时候该跳转：

- 如果你是在国内落地链路里选路线，回 [03-国内落地 / 01-总览](../03-国内落地/01-总览.md)
- 如果你已经确定必须走兼容层，回 [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)

---

<a id="faq-when-back-to-china"></a>

### 🇨🇳 09｜什么情况下该回 03-国内落地，而不是继续在这里硬调？

> ❓ 问题：什么情况下该回 03-国内落地，而不是继续在这里硬调？
>
> 💡 先说结论：只要你现在的问题已经不只是“这把 Key 对不对”，而是涉及部署、国内网络、路线选择、兼容层取舍，就不该继续把它当单点 provider 问题硬调。

下面这些情况，更适合回 03-国内落地 总览重新拆问题：

- 你还没决定用哪家模型路线
- 你同时在改 provider、endpoint、部署和入口
- 你分不清应该走官方 provider 还是兼容层
- 你把网络、部署、模型问题全糊在一起了

🔎 先做什么：

先回总览，把问题重新拆成：

- 模型路线
- 部署位置
- 入口方式

再回来调具体 provider / endpoint。

🚦 什么时候该跳转：

- 现在就该回：[03-国内落地 / 01-总览](../03-国内落地/01-总览.md)
- 如果你已经明确必须走兼容层，再继续看 [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)

## 🔹 官方依据

- [AI Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)
- [FAQ & Troubleshooting](https://hermes-agent.nousresearch.com/docs/reference/faq)
- [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
- [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)
- [02-国内模型 | 总览](../03-国内落地/02-国内模型/01-总览.md)

## ✅ 看完这页你应该能立刻回答什么

看完这一页，你应该能直接回答这 4 个问题：

1. 我现在卡的是 Key / 权限、endpoint、model 名，还是兼容能力边界？
2. 我应该继续用官方 provider，还是根本不该再硬调 custom endpoint？
3. 我现在该去厂商页、自定义兼容接口页，还是回国内落地总览重新拆路线？
4. 我的问题到底是单点 provider 问题，还是国内落地链路没理顺？

## ➡️ 下一步

完成后进入：

- [04-CLI / TUI / 会话问题](../01-从这开始/02-开始上手/01-总览.md)

如果你想先回到上一阶段入口重新确认位置：

- [01-总览](./01-总览.md)
