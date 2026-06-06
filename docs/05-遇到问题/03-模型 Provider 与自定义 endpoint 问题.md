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

先跑这 4 条，先定位，不要一边测一边同时改 5 个配置：

```bash
hermes model
hermes config
hermes version
hermes doctor
```

怎么理解结果：
- `hermes version` 跑不起来：先回 [02-安装 / 更新 / 环境问题](./02-安装更新与环境问题.md)
- `hermes config` 里 provider / model 已经和你认知不一致：先修主路线，不要继续猜
- `hermes version` 正常，`hermes model` / `doctor` 开始报鉴权、model、endpoint：继续留在本页
- 命令和模型都正常，只是 CLI / 会话行为怪：跳到 [04-CLI / TUI / 会话问题](<./04-CLI%20TUI%20与会话问题.md>)

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

## 📌 先记住这 4 个官方基线

### 1）先用 `hermes model`，不要先手改一堆配置

官方 provider 与 Custom Endpoint 的主入口都是：

```bash
hermes model
```

如果你只是第一次把 Hermes 跑通，默认先走：
- 官方 provider
- 正确的 API Key
- 最小可用模型

不要第一步就同时改：
- provider
- model
- `base_url`
- 网关
- 代理
- 本地服务

### 2）常见 provider 的正确 key 名，要和 provider 对上

按官方 providers 文档，这几组最常见：
- OpenRouter → `OPENROUTER_API_KEY`
- z.ai / GLM → `GLM_API_KEY`
- Kimi / Moonshot → `KIMI_API_KEY`
- MiniMax → `MINIMAX_API_KEY`
- DeepSeek → `DEEPSEEK_API_KEY`
- DashScope / Alibaba → `DASHSCOPE_API_KEY`
- Gemini → `GOOGLE_API_KEY` 或 `GEMINI_API_KEY`
- Custom Endpoint → 主要通过 `hermes model` 写入 `config.yaml`

如果你连 provider 名都还没分清，先不要直接怀疑 Key 无效。

### 3）官方要求模型上下文至少 64K

这一条不是“可选优化”，而是 Hermes 的硬边界之一。

如果你在接本地或自托管模型，至少先确认：
- model id 是真实存在的
- 实际 context length 足够
- 不是宣传页写很大，但实际给 Hermes 只有 8K / 16K

### 4）Custom Endpoint 先验三件事：地址、模型、兼容性

先不要上来就说“OpenAI-compatible 应该都一样”。
真正要先核对的是：
- `base_url` 是否对
- `/v1` 是否重复或缺失
- `/models` 是否能列到你要的模型
- 这个 endpoint 是否真的支持 Hermes 需要的能力

## 🧭 先做一轮最小体检

先只跑这 4 条，不要一边测一边继续改配置：

```bash
hermes model
hermes config
hermes version
hermes doctor
```

怎么看：
- `hermes version` 都不正常：先退回 [02-安装 / 更新 / 环境问题](./02-安装更新与环境问题.md)
- `hermes config` 里 provider / model 明显不是你以为那条：先修主路线，不要继续猜
- `hermes doctor` 开始报 auth / model / endpoint：继续留在本页
- 基础都正常，只是交互和工具行为怪：跳到 [04-CLI / TUI / 会话问题](<./04-CLI%20TUI%20与会话问题.md>) 或 [06-Tools / Skills / MCP 问题](<./06-Tools%20Skills%20MCP%20问题.md>)

## 🌐 `base_url` / `/v1` 最容易搞错的地方

把这张表先看一遍，再继续查 404：

| 你手里的地址长什么样 | 你在 Hermes 里通常该填什么 | 最常见错误 |
|---|---|---|
| 官方 provider，本来就支持 Hermes | 不必先手写 `base_url`，优先走 `hermes model` | 把官方 provider 硬改成 custom endpoint |
| OpenAI-compatible 根地址本身不带 `/v1` | 补成 `.../v1` 后再用 | 少一层 `/v1` |
| OpenAI-compatible 文档已经给到 `.../v1` | 直接用它给的 `.../v1` | 再手动补一次，变成双 `/v1` |
| 你手里是聊天接口全路径，如 `/v1/chat/completions` | 回退到服务级 `base_url`，不要直接贴聊天接口 | 把接口路径当 `base_url` |
| 你接的是 Ollama / vLLM / SGLang / LM Studio | 先确认它真的暴露了 OpenAI-compatible 路线 | 以为“本地服务能启动”就等于 Hermes 一定能接 |

一句话记法：
- Hermes 要的是服务级 `base_url`
- 不是单个聊天接口 URL
- `/v1` 要不要补，看上游文档原本给到哪一层

## 🔎 Custom Endpoint 最小验证法

不要一上来就拿主环境硬试。先拆成两段：

### A. 先看 Hermes 侧到底选中了什么

```bash
hermes config
hermes model
```

你至少要确认：
- 当前 provider 是不是 `custom`
- 当前 model 名是不是你想要的那个
- 现在是不是还挂着旧 provider 或旧 endpoint

### B. 再直接打 endpoint 本身

最小思路不是“先跑长对话”，而是先确认服务有没有正常暴露模型列表。

例如常见 OpenAI-compatible 检查会像这样：

```bash
curl -sS http://localhost:11434/v1/models
```

如果你拿到的是远程地址，就把上面的地址替换成你的真实 `base_url + /models`。

你最该看的是：
- 这个地址是否真的能通
- 返回里有没有你要的 model id
- 返回是不是已经在 401 / 403 / 404

如果连 `/models` 都不通，就不要先把锅甩给 Hermes。

## ❓FAQ

<a id="faq-api-key-invalid"></a>

### 01｜API Key 明明填了还是不通过

先说结论：最常见不是 Key 完全无效，而是 Key 放错变量名、provider 选错、当前 profile 不是你以为那份，或者旧的 custom endpoint 还在生效。

先做什么：
```bash
hermes model
hermes config
```

然后只确认三件事：
1. 当前实际选中的 provider 是谁
2. 这个 provider 对应的 Key 是否放进了正确变量名
3. 你当前 session / profile 看的，是不是你刚刚改过的那份环境

常见变量名：
- OpenRouter → `OPENROUTER_API_KEY`
- z.ai / GLM → `GLM_API_KEY`
- Kimi → `KIMI_API_KEY`
- MiniMax → `MINIMAX_API_KEY`
- DeepSeek → `DEEPSEEK_API_KEY`
- DashScope / Alibaba → `DASHSCOPE_API_KEY`
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

先做最小验证：
```bash
hermes config
curl -sS http://localhost:11434/v1/models
```

如果你不是本地 Ollama，就把第二条替换成你的真实 `base_url + /models`。

国内兼容层特别常见的坑：
- `/v1` 重复
- `/v1` 缺失
- 网关路径被代理层改写
- 上游只暴露聊天接口，没有暴露标准 `/models`

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

先跑最小检查：
```bash
hermes config
curl -sS http://localhost:11434/v1/models
```

如果你走的是本地模型路线，再优先怀疑：
- 模型还没加载完
- 本地服务没起来
- context 太大导致首包时间很慢
- Ollama / 本地兼容服务实际给 Hermes 的 context 没对齐

官方 FAQ 里还提到一个本地端点常见补救：
```bash
HERMES_STREAM_READ_TIMEOUT=1800
```

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
- 你已经开始碰到工具调用和会话行为异常：也一起看 [04-CLI / TUI / 会话问题](<./04-CLI%20TUI%20与会话问题.md>)、[06-Tools / Skills / MCP 问题](<./06-Tools%20Skills%20MCP%20问题.md>)

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
- [Environment Variables Reference](https://hermes-agent.nousresearch.com/docs/reference/environment-variables)
- [FAQ & Troubleshooting](https://hermes-agent.nousresearch.com/docs/reference/faq)
- [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
- [08-自定义兼容接口](../03-国内落地/02-国内模型/08-自定义兼容接口.md)
- [02-国内模型 | 总览](../03-国内落地/02-国内模型/01-总览.md)

---

<a id="faq-glm-auxiliary-404"></a>

### 10｜智谱 GLM 报 429 / 404，或 auxiliary_client 启动失败，怎么办？

**速答**：智谱 GLM 用户最常见的两个坑——(1) endpoint 路径填错导致 429 或 404；(2) `auxiliary_client` 启动报错。根因都是同一个：智谱官方同时存在 `/api/paas/v4`（标准 Paas v4）和 `/api/anthropic`（Anthropic 兼容层）两条路径，但 Hermes 默认走的是其中一条，需要你在 `hermes model` 里明确选 provider 而不是手动改 `base_url`。

**先做这 3 步**：

1. **先确认走的是哪条路径**：
```bash
hermes config | grep -i glm
```

2. **如果 `base_url` 是手动改的**，先撤销，回 `hermes model` 重选：
```bash
hermes model
# 选 z.ai / GLM 这个 provider，不要选 Custom Endpoint
```

3. **如果 429 持续**，先确认 GLM Coding Plan 额度没耗尽：
   - 登录智谱开放平台查 RPM / TPM 限流
   - 见 [04-智谱 GLM Coding Plan](../03-国内落地/02-国内模型/04-智谱GLM%20Coding%20Plan.md)

**`auxiliary_client` 报错的常见根因**：

| 报错 | 真正原因 | 处理 |
|------|---------|------|
| `auxiliary_client: connection refused` | 走的是 Paas v4 但 model 名不识别 | 改用 GLM Coding Plan 模型名，不要手填 `glm-4-plus` 之类 |
| `auxiliary_client: 404 not found` | base_url 写成了聊天接口而不是服务根 | 回 `hermes model`，不要手填 base_url |
| `auxiliary_client: 429` | Coding Plan 额度或 RPM 超限 | 检查智谱控制台 |

**5 路径绕过手填 base_url 速查**：

1. `hermes model` 选 GLM provider → 填 `GLM_API_KEY` → 自动配置
2. 如要走 Anthropic 兼容层（GLM Coding Plan 走 Claude Code 模式），同样 `hermes model` 选 GLM，不要手动改 base_url
3. 不要把 `https://open.bigmodel.cn/api/paas/v4/chat/completions` 当 base_url，要去掉 `/chat/completions`
4. 不要把 `/api/anthropic/v1/messages` 当 base_url，要去掉 `/v1/messages`
5. 走 OneAPI / NewAPI 中转时，model 名必须用中转层暴露的真实名（通常是 `glm-4-plus` 或智谱官方 model id），不是 Hermes 内置名

来源：[GitHub Issue #18302](https://github.com/NousResearch/hermes-agent/issues/18302)（社区完整根因分析）；[智谱 GLM Coding Plan](../03-国内落地/02-国内模型/04-智谱GLM%20Coding%20Plan.md)。

---

<a id="faq-anthropic-vs-openai-modes"></a>

### 11｜Hermes 接 Custom Endpoint 时，`anthropic_messages` / `chat_completions` / `codex_responses` 三种模式有什么区别？

**速答**：这三种是 Hermes 处理上游 LLM API 的三种协议模式，决定请求/响应格式。绝大多数用户走 `chat_completions`（OpenAI 兼容，最通用）。

| 模式 | 适用上游 | 协议 | 典型用例 |
|------|---------|------|---------|
| `chat_completions` | OpenAI-Compatible（默认） | OpenAI `/v1/chat/completions` | OneAPI / NewAPI / Ollama / LM Studio / 99% 兼容层 |
| `anthropic_messages` | Anthropic 原生 | Anthropic `/v1/messages` | Claude 官方 API、智谱 GLM Coding Plan（Anthropic 兼容层） |
| `codex_responses` | OpenAI Codex / Responses API | OpenAI `/v1/responses` | 早期 Codex 接入，少见 |

**怎么选**：

- 上游是 OpenAI-compatible 兼容层 → `chat_completions`
- 上游是 Anthropic 官方或 Anthropic 兼容层（GLM Coding Plan 走 Claude Code 模式） → `anthropic_messages`
- 你不知道上游是哪种 → 默认 `chat_completions`，先用 `curl /v1/models` 试

**不要混的两种误判**：
- 以为"GLM 一定要走 anthropic_messages"——错。GLM Coding Plan 才走 Anthropic 兼容层，标准 Paas v4 走 chat_completions。
- 以为"所有自定义兼容层都走 chat_completions"——错。如果中转层只暴露 Anthropic 协议，必须走 anthropic_messages。

参考：[官方文档 — Integrations: Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)。

---

<a id="faq-anthropic-baseurl-slash-v1"></a>

### 12｜Anthropic / 智谱 GLM 自定义 base_url 末尾带 `/v1`，请求直接 404，怎么办？

**速答**：这是 v0.12 之前的高频坑——你在 `base_url` 里写成了 `https://api.anthropic.com/v1` 或 `https://open.bigmodel.cn/api/anthropic/v1`，Hermes 内部又会自动追加 `/v1/messages`，结果路径变成 `/v1/v1/messages`，上游返回 404。同一日三个独立 PR（#24877 / #24873 / #24876）修复了同一个症状：Hermes 启动时自动剥离末尾 `/v1`。v0.13.0 已合并修复。如果你还在 v0.12 或更早，先升级；如果已经升级，按下面排查。

**先做这 3 步**：

1. **确认 Hermes 版本**：
```bash
hermes version
# 如果 < 0.13.0，先升级
hermes update
```

2. **检查你当前 `base_url` 写法**：
```bash
hermes config | grep -i base_url
# 看 ANTHROPIC_BASE_URL / GLM_BASE_URL 末尾是不是 /v1
```

3. **如果末尾确实是 `/v1`**，二选一处理：

| 写法 | 是否正确 | 说明 |
|------|---------|------|
| `https://api.anthropic.com` | ✅ 正确 | Hermes 自动追加 `/v1/messages` |
| `https://api.anthropic.com/v1` | ⚠️ v0.13+ 自动剥离 | v0.12 及更早会触发 404 |
| `https://api.anthropic.com/v1/messages` | ❌ 错 | 多了 `/v1/messages`，Hermes 会再追加一次 |
| `https://open.bigmodel.cn/api/anthropic` | ✅ 正确（智谱 Anthropic 兼容） | Hermes 自动追加 |
| `https://open.bigmodel.cn/api/anthropic/v1` | ⚠️ v0.13+ 自动剥离 | 同上 |

**手动剥离（如果你无法立即升级）**：

打开 `~/.hermes/config.yaml`（或对应 profile 的 config.yaml），把 `base_url` 末尾的 `/v1` 删掉：

```yaml
providers:
  anthropic:
    base_url: https://api.anthropic.com   # 不要带 /v1
    api_key: ${ANTHROPIC_API_KEY}
```

改完保存，重启 Hermes 即可。

**容易混的两个误判**：
- 以为是 \"Anthropic Key 失效\" → 错，401/403 才是 Key 问题，404 几乎都是路径
- 以为是 \"Hermes 不兼容 Anthropic 协议\" → 错，Hermes 原生支持 `anthropic_messages` 模式，参考 FAQ #11

**同类问题：智谱 GLM 的 `/v1` 重复**

智谱 Anthropic 兼容层（GLM Coding Plan 走 Claude Code 模式时使用）有完全一样的症状。如果你在 `hermes model` 里选了 GLM 但手动改了 `base_url`，也会触发 `/v1/v1/messages` 404。处理方式和 Anthropic 完全一致：删末尾 `/v1`，或升级到 v0.13+。

🚦 什么时候该跳转：

- 你的报错是 401/403（不是 404）：跳 [FAQ 02｜为什么一直报 401 / 403](#faq-401-403)
- 你的报错是 timeout 而不是 404：跳 [FAQ 04｜为什么一直报 Connection timeout](#faq-timeout)
- 你想搞清楚三种协议模式（chat_completions / anthropic_messages / codex_responses）：跳 [FAQ 11｜三种协议模式对比](#faq-anthropic-vs-openai-modes)
- 你的 base_url 已经不带 `/v1`，但智谱 GLM 还是 429/404：跳 [FAQ 10｜智谱 GLM 429/404 + auxiliary_client](#faq-glm-auxiliary-404)

来源：[GitHub PR #24877](https://github.com/NousResearch/hermes-agent/pull/24877)；[PR #24873](https://github.com/NousResearch/hermes-agent/pull/24873)；[PR #24876](https://github.com/NousResearch/hermes-agent/pull/24876)（三 PR 同日独立修复同一症状）；[官方文档 — Environment Variables](https://hermes-agent.nousresearch.com/docs/reference/environment-variables)。

---

## ✅ 看完这页，你应该立刻能判断

- 我现在卡的是 Key / 权限、endpoint、model 名，还是兼容能力边界
- 我应该继续用官方 provider，还是根本不该再硬调 custom endpoint
- 我现在该去厂商页、自定义兼容接口页，还是回国内落地总览重拆路线
- 我的问题到底是单点 provider 问题，还是整条国内落地链路没理顺

## ➡️ 下一步

完成后进入：

- [04-CLI / TUI / 会话问题](<./04-CLI%20TUI%20与会话问题.md>)

如果你想先回到上一阶段入口重新确认位置：

- [01-总览](<./01-总览.md>)

---

## 🔗 相关排查入口

- [国内模型](/docs/china/models)
- [自定义兼容接口](/docs/china/models/openai-compatible-endpoint)
- [环境变量参考](/docs/reference/environment-variables)
- [Profile 命令参考](/docs/reference/profile-commands)

如果当前页没有命中症状，先回到[遇到问题总入口](/docs/issues)重新按问题类型分流。
