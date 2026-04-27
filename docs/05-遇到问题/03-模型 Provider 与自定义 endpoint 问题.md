# 03-模型 / Provider / 自定义 endpoint 问题

> 一句话结论：这一页只处理“Key 不过、401 / 403 / 404 / 429、model 不存在、custom endpoint 半通不通”这类问题。只要 `hermes` 命令本身正常，先不要再把问题归成安装失败。

如果你现在很急，先记住：
> 先分清你卡的是 Key / 权限、model 名、endpoint 路径，还是兼容能力边界；不要把这 4 类问题混成一句“Provider 不行”。

## ⚡ 先按症状选路

你现在最像哪一种，直接跳：

### 🔐 Key / 鉴权不过
- Key 明明填了还是不通过
- 一直报 401 / 403
- 不确定自己到底在走哪个 provider
- 先看：[01｜API Key 明明填了还是不通过](#faq-api-key-invalid)
- 先看：[02｜为什么一直报 401 / 403](#faq-401-403)

### 🌐 endpoint / 路径 / 连通性异常
- 报 404
- 提示 endpoint 不存在
- Connection timeout / 连不上
- 先看：[03｜为什么一直报 404 或 endpoint 不存在](#faq-404-endpoint)
- 先看：[04｜为什么一直报 Connection timeout 或连不上](#faq-timeout)

### 🧩 model / provider 不匹配
- model 不存在
- 模型选不到
- 选完就报错
- 不知道该走官方 provider 还是 custom endpoint
- 先看：[05｜为什么提示 model 不存在或一选就报错](#faq-model-not-found)
- 先看：[06｜什么时候优先用官方 provider](#faq-official-vs-custom)

### 🇨🇳 custom endpoint / 国内兼容层半通不通
- 能聊天，但 tools 不稳
- system role / function calling 行为怪
- 不确定该继续硬调，还是回国内落地页重拆路线
- 先看：[07｜为什么 custom endpoint 能聊天，但 tools / system role / function calling 不稳定](#faq-custom-capability)
- 先看：[08｜国内中转 / OpenAI-Compatible 最容易出什么问题](#faq-china-compatible)
- 先看：[09｜什么时候该回 03-国内落地](#faq-when-back-to-china)

## 🧪 先做最小判断

先跑这 3 条，先定位，不要一边测一边同时改 5 个配置：

```bash
hermes model
hermes version
hermes doctor
```

怎么理解结果：
- `hermes version` 跑不起来：先回 [02-安装 / 更新 / 环境问题](./02-安装更新与环境问题.md)
- `hermes version` 正常，`hermes model` / `doctor` 开始报鉴权、model、endpoint：继续留在本页
- 命令和模型都正常，只是 CLI / 会话行为怪：跳到 [04-CLI / TUI / 会话问题](<./04-CLI TUI 与会话问题.md>)

## ✅ 先做什么：4 步排查清单

按这个顺序拆，最快：

1. 先确认你现在实际走的是哪个 provider
2. 再确认 Key 变量名和 provider 是否对应
3. 再确认 model 名是不是 provider 真正识别的名字
4. 最后才怀疑 custom endpoint 的兼容能力

高频误判：
- 以为自己在走官方 provider，实际还在走旧 endpoint
- 以为 Key 错了，实际是 model 无权限
- 以为 404 是模型不存在，实际是 `base_url` / `/v1` 写错
- 以为“能聊天”就等于完整兼容 Hermes 所需能力

## ❓FAQ

<a id="faq-api-key-invalid"></a>

### 01｜API Key 明明填了还是不通过

先说结论：最常见不是 Key 完全无效，而是 Key 放错变量名、provider 选错、当前 profile 不是你以为那份，或者旧的 custom endpoint 还在生效。

先做什么：
```bash
hermes model
```

然后只确认两件事：
1. 当前实际选中的 provider 是谁
2. 这个 provider 对应的 Key 是否放进了正确变量名

常见变量名：
- OpenRouter → `OPENROUTER_API_KEY`
- z.ai / GLM → `GLM_API_KEY`
- Kimi → `KIMI_API_KEY`
- DeepSeek → `DEEPSEEK_API_KEY`
- Gemini → `GOOGLE_API_KEY` / `GEMINI_API_KEY`
- Custom Endpoint → 主要通过 `hermes model` 写入 `config.yaml`

什么时候该跳转：
- 命令本身都不正常：回 [02-安装 / 更新 / 环境问题](./02-安装更新与环境问题.md)
- 你其实还没想清楚要走哪条国内模型路线：回 [03-国内落地 / 01-总览](../03-国内落地/01-总览.md)

---

<a id="faq-401-403"></a>

### 02｜为什么一直报 401 / 403

先说结论：401 / 403 大多不是 Hermes 坏了，而是鉴权失败、模型无权限、套餐不支持，或者拿错了 provider 的 Key。

先做什么：
先按这个理解：
- `401`：更像没认证上、Key 错、token 失效
- `403`：更像认证到了，但权限不够、模型不可用、套餐不支持

然后排这几件事：
- Key 是否真的属于当前 provider
- 当前模型是否在账户权限范围内
- 国内 / 国际线路的 Key 有没有混用
- 你是不是以为在走官方 provider，实际还在走 custom endpoint

什么时候该跳转：
- 已确认是套餐 / 权限 / 厂商路线问题：回 [02-国内模型 | 总览](../03-国内落地/02-国内模型/01-总览.md)
- 还没分清当前走的 provider：继续留在本页

---

<a id="faq-404-endpoint"></a>

### 03｜为什么一直报 404 或 endpoint 不存在

先说结论：最常见不是模型坏了，而是 `base_url`、`/v1`、路径前缀，或者 endpoint 类型本身写错了。

先做什么：
如果你在走 custom endpoint，优先核对：
- `base_url` 是不是多写了一层 `/v1`
- `base_url` 是不是少了一层 `/v1`
- 你填的是服务根地址，还是直接把聊天接口地址贴进去了
- 这个接口到底是不是 OpenAI-compatible

国内兼容层特别常见的坑：
- `/v1` 重复
- `/v1` 缺失
- 网关路径被代理层改写

什么时候该跳转：
- 你接的是 OneAPI / NewAPI / Ollama / LM Studio / 本地兼容层：看 [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)
- 你其实应该走官方 provider：不要继续硬调 endpoint，回 `hermes model` 重选

---

<a id="faq-timeout"></a>

### 04｜为什么一直报 Connection timeout 或连不上

先说结论：timeout 通常不是 Hermes 逻辑错误，而是网络层、代理层、本地服务没起来，或者 endpoint 在当前机器根本不可达。

先做什么：
先回答这 3 个问题：
1. 服务真的在运行吗
2. 当前这台机器真的能访问这个地址吗
3. 你有没有把本地地址、局域网地址、云主机地址混用了

如果你走的是本地模型路线，再优先怀疑：
- 模型还没加载完
- 本地服务没起来
- context 太大导致首包时间很慢

什么时候该跳转：
- 明显是国内网络 / 云主机 / 部署问题：回 [03-国内落地 / 01-总览](../03-国内落地/01-总览.md)
- 明显是本地兼容服务问题：回 [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)

---

<a id="faq-model-not-found"></a>

### 05｜为什么提示 model 不存在、选不到，或者一选就报错

先说结论：最常见不是 Hermes 不认识模型，而是你填的 model 名不等于 provider 真正识别的名字，或者模型能力根本不满足要求。

先做什么：
```bash
hermes model
```

然后确认：
- 当前 provider 下到底有哪些可选模型
- 你是不是手填了一个“自己习惯叫法”，而不是真实名
- 账户是否有这个模型权限
- 这个模型是否满足 Hermes 的上下文要求

重要边界：
- Hermes Agent 要求模型至少有 64,000 tokens context

什么时候该跳转：
- 你在国产路线里选模型：回 [02-国内模型 | 总览](../03-国内落地/02-国内模型/01-总览.md)
- 你只是 custom endpoint 模型名对不上：继续留在本页，或去 [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)

---

<a id="faq-official-vs-custom"></a>

### 06｜什么时候优先用官方 provider

先说结论：只要 Hermes 已经对这个厂商提供官方 provider，默认先走官方 provider。custom endpoint 更适合“你已经有稳定兼容层”的场景。

先做什么：
先问自己：
- 我是不是第一次把 Hermes 跑通
- 我是不是只是想尽快稳定可用
- 我是不是并不需要统一到自建网关

默认优先官方 provider 的原因：
- 少一层中转
- 少一层兼容误差
- 配置更短
- 排错边界更清楚

更适合 custom endpoint 的场景：
- 你已经有稳定 OpenAI-compatible 兼容层
- 你要接本地 Ollama / LM Studio / 企业网关
- 你明确知道自己为什么需要统一入口

什么时候该跳转：
- 只是第一次跑通 Hermes：不要先走 custom endpoint
- 你已经明确要接兼容层：去看 [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)

---

<a id="faq-custom-capability"></a>

### 07｜为什么 custom endpoint 能聊天，但 tools / system role / function calling 不稳定

先说结论：因为“能聊天”只证明最基础文本链路通了，不等于这个兼容层完整支持 Hermes 需要的全部能力。

先做什么：
先不要急着改 Hermes，先承认这更像兼容层边界问题。

然后判断：
- 你是不是应该直接切回官方 provider
- 你是不是应该更换兼容层
- 你是不是只把它当临时聊天入口，而不是稳定 Agent 入口

高频表现：
- 普通聊天能用
- 一到 tools 就异常
- 一到复杂 agent workflow 就不稳定
- system role / 流式输出 / 响应格式行为不一致

什么时候该跳转：
- 你要的是稳定 Agent 工作流：优先回官方 provider
- 你要继续走兼容层：去 [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)
- 你已经开始碰到工具调用和会话行为异常：也一起看 [04-CLI / TUI / 会话问题](<./04-CLI TUI 与会话问题.md>)、[06-Tools / Skills / MCP 问题](<./06-Tools Skills MCP 问题.md>)

---

<a id="faq-china-compatible"></a>

### 08｜国内中转 / OpenAI-Compatible 最容易出什么问题

先说结论：最常见不是完全连不上，而是路径、模型名、权限、能力支持范围、国内外线路混用这些“半通不通”的问题。

先做什么：
把问题硬拆成 4 层：
1. 地址对不对
2. Key 对不对
3. model 名对不对
4. 兼容能力够不够

常见问题：
- `/v1` 缺失或重复
- 模型名与上游暴露名不一致
- 国内版 / 国际版接口混用
- 能聊天但 tools 不稳
- 中转层做了自己的限流、鉴权、重写

什么时候该跳转：
- 你在国内落地链路里选路线：回 [03-国内落地 / 01-总览](../03-国内落地/01-总览.md)
- 你已经确定必须走兼容层：回 [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)

---

<a id="faq-when-back-to-china"></a>

### 09｜什么时候该回 03-国内落地，而不是继续在这里硬调

先说结论：只要你现在的问题已经不只是“这把 Key 对不对”，而是涉及部署、网络、路线选择、兼容层取舍，就不该继续把它当单点 provider 问题硬调。

先做什么：
如果你出现下面任一情况，就该回去重拆路线：
- 还没决定用哪家模型路线
- 同时在改 provider、endpoint、部署和入口
- 分不清该走官方 provider 还是兼容层
- 把网络、部署、模型问题全糊在一起

回去后重新拆成：
- 模型路线
- 部署位置
- 入口方式

什么时候该跳转：
- 现在就该回：[03-国内落地 / 01-总览](../03-国内落地/01-总览.md)
- 已明确必须走兼容层：继续看 [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)
- 你回头发现其实是安装 / PATH / shell 问题：退回 [02-安装 / 更新 / 环境问题](./02-安装更新与环境问题.md)

## 🔹 官方依据

- [AI Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)
- [FAQ & Troubleshooting](https://hermes-agent.nousresearch.com/docs/reference/faq)
- [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
- [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)
- [02-国内模型 | 总览](../03-国内落地/02-国内模型/01-总览.md)

## ✅ 看完这页，你应该立刻能判断

- 我现在卡的是 Key / 权限、endpoint、model 名，还是兼容能力边界
- 我应该继续用官方 provider，还是根本不该再硬调 custom endpoint
- 我现在该去厂商页、自定义兼容接口页，还是回国内落地总览重拆路线
- 我的问题到底是单点 provider 问题，还是整条国内落地链路没理顺

## ➡️ 下一步
完成后进入：
- [04-CLI / TUI / 会话问题](<./04-CLI TUI 与会话问题.md>)
如果你想先回到上一阶段入口重新确认位置：
- [01-总览](./01-总览.md)
