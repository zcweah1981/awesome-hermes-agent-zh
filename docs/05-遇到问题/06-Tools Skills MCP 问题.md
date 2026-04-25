# 06-Tools / Skills / MCP 问题

> 🎯 一句话结论：这一页不是教你重新装一遍 Skills 或 MCP，而是集中回答“为什么 tools 列表不对、为什么 skills 没加载、为什么 `/skill` 不工作、为什么 MCP server 连不上、为什么工具像被禁用了”这类高频问题。

如果你现在最焦虑，只先记住一句：

> Tools / Skills / MCP 问题最常见不是“功能彻底不存在”，而是工具集没开、skills 没装到当前环境、MCP server 没注册成功，或者你把 CLI 能力、hub 技能和 MCP 外部工具混成了一回事。

## 这页主要回答什么

这一页集中回答这几类高频问题：

- 为什么 tools 列表为空或和预期不一样？
- 为什么 skills 明明装了，但当前像没加载？
- 为什么 `/skill-name` 或 skills 调用不工作？
- 为什么 MCP server 连不上、配置后没生效？
- 为什么工具看起来存在，但 Hermes 就是不调用？

## 先做一个最小判断

如果你现在完全不知道问题卡在哪，先做这几步：

```bash
hermes tools
hermes skills list
hermes doctor
```

如果你当前在查 MCP，还要确认：

- `config.yaml` 里是否真的有 `mcp_servers`
- 你现在用的是不是支持外部工具的那套配置环境

这组最小动作的目的不是立刻修好，而是先判断：

- 是工具集根本没打开
- 还是 skill 根本不在当前环境
- 还是 MCP server 注册失败
- 还是工具存在，但当前任务根本没触发调用条件

## ⚡ 快速定位：先看你的问题

如果你不想从头往下读，先按你眼前最像的现象直接跳：

### 🧰 tools / toolsets 不对
- 1️⃣ [为什么 tools 列表为空，或者和我预期的不一样？](#faq-tools-list)
- 2️⃣ [为什么工具明明存在，但 Hermes 像没在调用？](#faq-tool-not-called)

### 🧠 skills 不生效
- 3️⃣ [为什么 skills 明明装了，但当前像没加载？](#faq-skills-not-loaded)
- 4️⃣ [为什么 `/skill-name`、skills browse、skills list 表现不对？](#faq-skill-command)

### 🔌 MCP 连不上
- 5️⃣ [为什么 MCP server 配了，但像根本没接上？](#faq-mcp-not-connected)
- 6️⃣ [为什么 MCP tools 看起来注册了，但还是不好用？](#faq-mcp-tool-weak)

### 🧭 问题边界判断
- 7️⃣ [什么时候该把问题当成 tools / skills，而不是 provider / model？](#faq-tools-vs-provider)
- 8️⃣ [什么时候该回自己造东西总览，而不是继续在这里硬调？](#faq-back-to-build)
- 9️⃣ [为什么我感觉“全都配置了”，但最后其实是环境隔离搞错了？](#faq-env-isolation)

> 📌 建议阅读顺序
> - 先看：🧰 tools / toolsets 不对
> - 再看：🧠 skills 不生效
> - 然后看：🔌 MCP 连不上
> - 最后看：🧭 问题边界判断

## ❓FAQ 正文

<a id="faq-tools-list"></a>

### 🧰 01｜为什么 tools 列表为空，或者和我预期的不一样？

> ❓ 问题：为什么 tools 列表为空，或者和我预期的不一样？
>
> 💡 先说结论：最常见原因不是工具系统坏了，而是你当前平台 / 当前环境 / 当前 toolsets 配置，并没有把你以为会出现的那批工具真正开出来。

最常见原因是：

- 当前 toolsets 没开
- 当前平台和你以为的平台不一样
- 当前环境里缺少某些依赖或 extras
- 你把“工具存在于 Hermes 代码里”和“当前会话可用”当成了一回事

🔎 先做什么：

先从交互式工具配置入口看当前状态：

```bash
hermes tools
```

再分清：

- 我现在是在 CLI、gateway，还是别的平台环境
- 当前平台下哪些工具被启用
- 我期待的工具是否本来就属于另一套 toolset

🚦 什么时候该跳转：

- 如果你只是没分清 toolsets，留在本页
- 如果你已经发现问题其实是 provider / model 报错，回 [03-模型 / Provider / 自定义 endpoint 问题](./03-模型 Provider 与自定义 endpoint 问题.md)

---

<a id="faq-tool-not-called"></a>

### 🧰 02｜为什么工具明明存在，但 Hermes 像没在调用？

> ❓ 问题：为什么工具明明存在，但 Hermes 像没在调用？
>
> 💡 先说结论：最常见原因不是工具不可用，而是你当前任务根本没有给到足够清楚的触发条件，或者模型层根本不稳定，导致 Hermes 没有正确进入工具调用轨道。

工具存在，不等于每次都会被调用。

最常见原因是：

- 你的任务描述过于模糊
- 当前模型本身就不稳定
- 你当前在安全模式 / 受限环境下
- 你以为“列在 tools 里”就等于“必须调用”

🔎 先做什么：

先不要先怪工具。
先判断：

- 我是不是给了一个明确需要工具的任务
- 当前模型 / provider 是否稳定
- 这件事是不是其实可以纯文本回答，导致没有触发工具

🚦 什么时候该跳转：

- 如果你发现模型本身就不稳定，回模型 / Provider 页
- 如果只是触发条件不清，留在本页

---

<a id="faq-skills-not-loaded"></a>

### 🧠 03｜为什么 skills 明明装了，但当前像没加载？

> ❓ 问题：为什么 skills 明明装了，但当前像没加载？
>
> 💡 先说结论：最常见原因不是 skills 丢了，而是你装在了另一套环境 / profile / 来源里，或者当前平台没有按你想的方式启用它们。

Skills Hub 和 CLI Commands Reference 都已经说明：

- skills 有安装、浏览、列出、审计等独立生命周期
- skills 不是“装过一次，全环境自动统一等价”

最常见混淆是：

- 装在这个环境，结果去另一个 profile 里找
- 以为 hub 里的 skill 已安装，实际只是 browse 过
- 以为 CLI 可见，消息平台也一定等价可见

🔎 先做什么：

先直接检查当前环境：

```bash
hermes skills list
```

然后确认：

- 你现在用的是哪一个 profile
- 当前 skill 是“看到了”，还是“真的装了”
- 当前平台是否真的会暴露这类 skill 命令

🚦 什么时候该跳转：

- 如果你怀疑是 profile 隔离导致的，后续更该去配置 / profiles 页
- 如果只是 skills 本身没装，留在本页

---

<a id="faq-skill-command"></a>

### 🧠 04｜为什么 `/skill-name`、skills browse、skills list 表现不对？

> ❓ 问题：为什么 `/skill-name`、skills browse、skills list 表现不对？
>
> 💡 先说结论：因为这几件事本来就不是一回事：有的是“查看 registry”，有的是“查看已安装”，有的是“在交互里直接触发 skill”。

最常见混淆是：

- `browse/search` 当成已安装列表
- `list` 当成 hub 全量目录
- `/skill-name` 当成“所有看到过的 skill 都能直接调用”

CLI Commands Reference 已明确：

- `hermes skills browse`：浏览可安装技能
- `hermes skills search <query>`：搜 registry
- `hermes skills list`：看已安装技能
- `/<skill-name>`：调用已可用的 skill

🔎 先做什么：

先分清你当前到底在做哪一种：

1. 浏览可安装技能
2. 查看当前已安装技能
3. 在交互里触发 skill

只要这三件事没分开，你就会反复误判“skills 出问题了”。

🚦 什么时候该跳转：

- 如果只是命令语义没分清，留在本页
- 如果是交互式 slash 行为怪，回 [04-CLI / TUI / 会话问题](./04-CLI TUI 与会话问题.md)

---

<a id="faq-mcp-not-connected"></a>

### 🔌 05｜为什么 MCP server 配了，但像根本没接上？

> ❓ 问题：为什么 MCP server 配了，但像根本没接上？
>
> 💡 先说结论：最常见原因不是 Hermes 不支持 MCP，而是 `mcp_servers` 没写到当前实际生效的 `config.yaml`、server 根本起不来，或者 stdio / HTTP 路线本身没配对。

最常见原因是：

- `config.yaml` 不是当前环境实际在读的那份
- 你写的是 stdio server，但 command / args 本身跑不起来
- 你写的是 HTTP server，但地址或 headers 根本不对
- 你把“写了配置”误当成“已经接通了外部工具”

🔎 先做什么：

先不要直接看最终工具名。
先判断：

- 当前环境里的 `mcp_servers` 是否真的存在
- 这是 stdio server 还是 HTTP server
- server 本身有没有机会成功启动 / 连接

🚦 什么时候该跳转：

- 如果你已经确定是 MCP 配置边界问题，留在本页
- 如果你想重新理解 MCP 主线，回 [05-把 Hermes 接进外部系统](../01-从这开始/04-自己造东西/05-把 Hermes 接进外部系统.md)

---

<a id="faq-mcp-tool-weak"></a>

### 🔌 06｜为什么 MCP tools 看起来注册了，但还是不好用？

> ❓ 问题：为什么 MCP tools 看起来注册了，但还是不好用？
>
> 💡 先说结论：最常见原因不是注册失败，而是你把“工具注册成功”和“任务能稳定调用这个工具完成目标”当成了一回事。

MCP 页已经明确：

- 成功信号不是只看到配置不报错
- 更强的成功信号是 Hermes 真能通过它完成外部任务

也就是说：

- 工具名出现了 ≠ 任务一定能稳定完成
- server 连上了 ≠ 输出结果一定符合你的预期

🔎 先做什么：

先给一个最明确的外部任务：

- 列文件
- 查某个外部系统
- 读一个明确资源

而不是直接给一个模糊大任务。

🚦 什么时候该跳转：

- 如果你其实还没搞懂 MCP 主线，回 MCP 那一页
- 如果工具能调用但结果质量差，也要交叉判断是不是模型层问题

---

<a id="faq-tools-vs-provider"></a>

### 🧭 07｜什么时候该把问题当成 tools / skills，而不是 provider / model？

> ❓ 问题：什么时候该把问题当成 tools / skills，而不是 provider / model？
>
> 💡 先说结论：如果问题主要体现在“工具不出现、skill 不加载、MCP server 连不上”，更像能力层；如果问题体现在“请求慢、鉴权错、模型不认、endpoint 报错”，更像 provider / model 层。

一个很实用的分界线是：

- 工具 / skills / MCP 层关心的是“能力有没有被接进来”
- provider / model 层关心的是“推理链路本身稳不稳”

🔎 先做什么：

先问自己：

1. 我的问题发生在“调用前”，还是“调用后”？
2. 我的问题是能力缺失，还是结果生成异常？
3. 是工具压根没有，还是模型没正确用它？

🚦 什么时候该跳转：

- 如果你发现根因更像 provider / model，回 [03-模型 / Provider / 自定义 endpoint 问题](./03-模型 Provider 与自定义 endpoint 问题.md)
- 如果是能力边界问题，留在本页

---

<a id="faq-back-to-build"></a>

### 🧭 08｜什么时候该回自己造东西总览，而不是继续在这里硬调？

> ❓ 问题：什么时候该回自己造东西总览，而不是继续在这里硬调？
>
> 💡 先说结论：只要你现在连“我是要多个助手、外部记忆、MCP、API Server 还是自动化”这几条主线都没分清，就不该继续在 Tools / Skills / MCP 单点问题里硬调。

更适合回总览的情况是：

- 你还没分清 Skills、MCP、API Server、Cron 分别解决什么
- 你其实在同时改多条系统主线
- 你现在的问题已经不是“这个工具怎么连”，而是“我到底该走哪条系统化路线”

🔎 先做什么：

先回总览，把问题重新拆成：

- 多助手
- 记忆
- 上下文
- MCP / 外部系统
- API Server
- 自动化

再回来调具体点。

🚦 什么时候该跳转：

- 现在就该回：[04-自己造东西](../01-从这开始/04-自己造东西/01-总览.md)
- 如果你已经明确就是 tools / skills / MCP 单点问题，留在本页

---

<a id="faq-env-isolation"></a>

### 🧭 09｜为什么我感觉“全都配置了”，但最后其实是环境隔离搞错了？

> ❓ 问题：为什么我感觉“全都配置了”，但最后其实是环境隔离搞错了？
>
> 💡 先说结论：因为 Hermes 的很多能力都跟“当前 profile / 当前配置 / 当前环境”强绑定，装过、看过、写过，不自动等于“当前正在用的这套环境也生效了”。

这类问题最常见出现在：

- profile 切换后还按旧环境预期看东西
- skills 装在 A，结果去 B 里找
- `config.yaml` 改的是一份，当前实际跑的是另一份
- 你把“本机装过”理解成“任何入口都能用”

🔎 先做什么：

先问自己：

- 我现在到底在哪个 profile / 环境里
- 当前会话到底读的是哪套配置
- 我以为已经有的 skill / MCP server / toolset，是否真的在这个环境里可见

🚦 什么时候该跳转：

- 如果你已经明显怀疑是 profile / config 隔离问题，后续更该去配置 / profiles 页
- 如果还只是 tools / skills / MCP 本身边界不清，留在本页

## 🔹 官方依据

- [Skills Hub](https://hermes-agent.nousresearch.com/docs/skills)
- [CLI Commands Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)
- [FAQ & Troubleshooting](https://hermes-agent.nousresearch.com/docs/reference/faq)
- [04-自己造东西](../01-从这开始/04-自己造东西/01-总览.md)
- [05-把 Hermes 接进外部系统](../01-从这开始/04-自己造东西/05-把 Hermes 接进外部系统.md)

## ✅ 看完这页你应该能立刻回答什么

看完这一页，你应该能直接回答这 4 个问题：

1. 我的问题是工具集没开、skills 没装、MCP 没接上，还是模型层在拖后腿？
2. 我现在是该继续查 tools / skills / MCP，还是回 provider / model 页？
3. 我是不是把 skill registry、已安装 skills、slash 调用、MCP 工具混成了一件事？
4. 我现在到底是在查单点能力问题，还是已经该回自己造东西总览重新拆路线？

## ➡️ 下一步

完成后进入：

- [07-配置 / Profiles / 环境隔离问题](./07-配置 Profiles 与环境隔离问题.md)

如果你想先回到上一阶段入口重新确认位置：

- [01-总览](./01-总览.md)
