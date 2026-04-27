# 06-Tools / Skills / MCP 问题

> 一句话结论：这页只处理“工具为什么不出现、skills 为什么像没加载、MCP 为什么连不上、为什么明明看得到工具却就是不好用”这类排障问题；先分清是工具集没开、skill 没装到当前环境，还是 MCP server 根本没接通。

如果你现在只想先记住一句：
> 大多数 Tools / Skills / MCP 问题，不是功能不存在，而是“当前环境没暴露、你看的不是已安装列表、或者外部 server 根本没成功接进来”。

## ⚡ 先按症状跳转

你现在最像哪一种：

### A. `hermes tools` 结果不对 / 工具列表很空
- 看这里：[#01 为什么 tools 列表和预期不一样？](#faq-tools-list)
- 看这里：[#02 为什么工具存在却像没被调用？](#faq-tool-not-called)

### B. skills 明明装过，但当前像没加载
- 看这里：[#03 为什么 skills 明明装了却像没加载？](#faq-skills-not-loaded)
- 看这里：[#04 为什么 `/skill-name`、browse、list 表现不对？](#faq-skill-command)

### C. MCP server 配了，但像根本没接上
- 看这里：[#05 为什么 MCP server 配了却没接上？](#faq-mcp-not-connected)
- 看这里：[#06 为什么 MCP tools 看起来有了却还是不好用？](#faq-mcp-tool-weak)

### D. 你怀疑其实不是工具问题，而是环境或模型问题
- 看这里：[#07 什么时候这更像 provider / model 问题？](#faq-tools-vs-provider)
- 看这里：[#09 为什么最后常常其实是环境隔离搞错了？](#faq-env-isolation)

### E. 你现在路线都没分清
- 看这里：[#08 什么时候该回“自己造东西”总览？](#faq-back-to-build)

## 🩺 先做什么：最小排查动作

先做这组最小检查：

```bash
hermes tools
hermes skills list
hermes doctor
```

如果你查的是 MCP，再补两个判断：
- 当前实际生效的 `config.yaml` 里有没有 `mcp_servers`
- 当前 profile / 环境是不是你以为的那套

这一步只想回答 4 个问题：

1. 工具集有没有真的暴露出来
2. skills 是没装，还是装在别的环境
3. MCP server 是没注册，还是 server 本身起不来
4. 工具存在但没调用，究竟是触发条件问题，还是模型层问题

## 🚫 先别急着做的事

- 不要把 registry 里“看得到”当成“当前已安装”
- 不要把“工具名出现了”当成“任务一定会稳定调用它”
- 不要一边切 profile、一边改 MCP、一边重装 skills
- 不要把 tools、skills、MCP、provider、gateway 全混成一件事

## ❓FAQ

<a id="faq-tools-list"></a>

### 01｜为什么 tools 列表和预期不一样？

先说结论：最常见不是工具系统坏了，而是当前平台、当前 toolsets、当前环境依赖，并没有把你以为那批工具真正开出来。

先做什么：
- 先跑 `hermes tools`
- 先确认你现在是在 CLI、gateway，还是别的入口里看工具
- 先确认你期待的工具本来是不是属于另一套 toolset

重点检查：
- 当前 toolsets 没开
- 当前平台环境不同，暴露能力不同
- 缺依赖 / extras，导致部分工具不可用
- 你把“代码里存在”误当成“当前会话可用”

什么时候该跳转：
- 如果只是 toolsets 边界没分清，留在本页
- 如果已经发现是 provider / model 报错导致工具链失效，跳到 [03-模型 / Provider / 自定义 endpoint 问题](<./03-模型 Provider 与自定义 endpoint 问题.md>)

---

<a id="faq-tool-not-called"></a>

### 02｜为什么工具存在却像没被调用？

先说结论：工具可用，不等于每次都会自动被调用。最常见根因是任务描述不够明确、模型不稳定，或者当前任务根本不需要工具。

先做什么：
- 先给一个明确必须用工具的任务
- 先确认当前模型 / provider 是否稳定
- 先判断这件事是不是本来就能纯文本回答

高频误判：
- 以为列在 tools 里，就等于一定会调用
- 以为没调工具，就是工具系统坏了
- 以为所有模型在工具调用上都同样稳定

什么时候该跳转：
- 如果你已经怀疑是模型不稳定或 endpoint 兼容性问题，跳到 [03-模型 / Provider / 自定义 endpoint 问题](<./03-模型 Provider 与自定义 endpoint 问题.md>)
- 如果只是触发条件不清，留在本页

---

<a id="faq-skills-not-loaded"></a>

### 03｜为什么 skills 明明装了却像没加载？

先说结论：多数不是 skill 丢了，而是你装在了另一套 profile / 环境 / 来源里，当前入口并没有读到它。

先做什么：
- 先跑 `hermes skills list`
- 先确认当前 profile 是谁
- 先确认你是“浏览过 skill”，还是“真的装过 skill”

最常见原因：
- 装在 profile A，结果在 profile B 里找
- 以为 browse 过就等于已安装
- 以为 CLI 可见，消息平台里也一定同样可见

什么时候该跳转：
- 如果你已经明显怀疑是 profile / 配置隔离，跳到 [07-配置 / Profiles / 环境隔离问题](<./07-配置 Profiles 与环境隔离问题.md>)
- 如果只是 skill 没装到当前环境，留在本页

---

<a id="faq-skill-command"></a>

### 04｜为什么 `/skill-name`、browse、list 表现不对？

先说结论：因为它们本来就不是同一种动作。一个是在看可安装目录，一个是在看已安装，一个是在交互里直接调用。

先做什么：
- 先分清你现在到底在做哪一件事
- 不要把 browse、search、list、`/skill-name` 混着理解

最容易混淆的边界：
- `browse/search`：看 registry / 可安装内容
- `list`：看当前环境里已安装的 skills
- `/<skill-name>`：调用当前已可用的 skill

什么时候该跳转：
- 如果只是命令语义没分清，留在本页
- 如果你真正卡的是本地交互 / slash 行为，跳到 [04-CLI / TUI / 会话问题](<./04-CLI TUI 与会话问题.md>)

---

<a id="faq-mcp-not-connected"></a>

### 05｜为什么 MCP server 配了却没接上？

先说结论：最常见不是 Hermes 不支持 MCP，而是 `mcp_servers` 没写到当前真正生效的配置里，或者 server 本身根本起不来。

先做什么：
- 先确认当前环境实际在读哪份 `config.yaml`
- 先确认 `mcp_servers` 是否真的写在那份配置里
- 先确认这是 stdio server 还是 HTTP server
- 先确认 server 本身有没有机会启动 / 连接成功

重点检查：
- 改错了配置文件
- stdio command / args 本身跑不起来
- HTTP 地址、headers、认证信息不对
- 你把“配置写上了”误当成“连接一定成功”

什么时候该跳转：
- 如果你要重新建立 MCP 主线理解，跳到 [05-把 Hermes 接进外部系统](<../01-从这开始/04-自己造东西/05-把 Hermes 接进外部系统.md>)
- 如果你已经明确在查当前 MCP 接通失败，留在本页

---

<a id="faq-mcp-tool-weak"></a>

### 06｜为什么 MCP tools 看起来有了却还是不好用？

先说结论：工具注册成功，不等于任务就能稳定完成。很多时候是 server 能连，但任务设计、工具输出、模型调用策略没有对上。

先做什么：
- 先给一个非常小、非常明确的外部任务
- 先验证它能不能稳定完成一个简单动作
- 不要一上来就拿复杂大任务做第一验收

推荐先测的小任务：
- 列一个目录
- 读一个明确资源
- 查一个固定对象

什么时候该跳转：
- 如果你发现工具能调用，但结果质量差、调用不稳定，也要交叉看 [03-模型 / Provider / 自定义 endpoint 问题](<./03-模型 Provider 与自定义 endpoint 问题.md>)
- 如果你还没搞懂 MCP 适合解决什么，跳到 [05-把 Hermes 接进外部系统](<../01-从这开始/04-自己造东西/05-把 Hermes 接进外部系统.md>)

---

<a id="faq-tools-vs-provider"></a>

### 07｜什么时候这更像 provider / model 问题？

先说结论：如果问题体现在“工具不出现、skill 不加载、MCP server 连不上”，更像能力接入层；如果问题体现在“请求慢、鉴权错、模型不认、endpoint 报错”，更像 provider / model 层。

先做什么：
- 先问自己：问题发生在调用前，还是调用后
- 先问自己：是能力缺失，还是生成结果异常
- 先问自己：是工具没有，还是模型没正确使用它

什么时候该跳转：
- 如果根因更像 provider / model，跳到 [03-模型 / Provider / 自定义 endpoint 问题](<./03-模型 Provider 与自定义 endpoint 问题.md>)
- 如果根因更像能力没接进来，留在本页

---

<a id="faq-back-to-build"></a>

### 08｜什么时候该回“自己造东西”总览？

先说结论：只要你现在连“我到底要 skill、MCP、API server、memory 还是自动化”都没分清，就不该继续在这页单点硬调。

先做什么：
- 先把目标重新拆成系统路线
- 再回来处理具体能力点

适合先回总览的情况：
- 你同时在改 Skills、MCP、API Server、Cron
- 你还没分清这些能力各自解决什么
- 你现在的问题已经不是“为什么不工作”，而是“我该走哪条路”

什么时候该跳转：
- 现在就该回：[04-自己造东西](../01-从这开始/04-自己造东西/01-总览.md)
- 如果你已经明确就是 tools / skills / MCP 单点问题，留在本页

---

<a id="faq-env-isolation"></a>

### 09｜为什么最后常常其实是环境隔离搞错了？

先说结论：因为 tools、skills、MCP 都强依赖“当前 profile / 当前配置 / 当前环境”。你装过、看过、写过，不等于当前会话正在用。

先做什么：
- 先确认自己到底在哪个 profile / 环境里
- 先确认当前入口读的是哪份配置
- 先确认你以为已经有的 skill / MCP server / toolset 是否真在这个环境里可见

最常见场景：
- skills 装在 A，结果去 B 里找
- `config.yaml` 改的是一份，当前跑的是另一份
- 本机有的工具，以为 gateway / 远端环境也自动有

什么时候该跳转：
- 如果你已经明显进入 profile / config 隔离问题，跳到 [07-配置 / Profiles / 环境隔离问题](<./07-配置 Profiles 与环境隔离问题.md>)
- 如果还只是 tools / skills / MCP 的语义边界不清，留在本页

## 🔹 官方依据

- [Skills Hub](https://hermes-agent.nousresearch.com/docs/skills)
- [CLI Commands Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)
- [FAQ & Troubleshooting](https://hermes-agent.nousresearch.com/docs/reference/faq)
- [04-自己造东西](../01-从这开始/04-自己造东西/01-总览.md)
- [05-把 Hermes 接进外部系统](<../01-从这开始/04-自己造东西/05-把 Hermes 接进外部系统.md>)

## ✅ 看完这页，你应该能立刻判断

- 问题到底是 toolsets、skills、MCP，还是模型层在拖后腿
- 你是不是把 registry、已安装、slash 调用、外部工具混成了一件事
- 该继续留在这页，还是该跳去模型页 / 配置页 / 自己造东西总览
- 现在该先修单点能力，还是先重新整理系统路线

## ➡️ 下一步
完成后进入：
- [07-配置 / Profiles / 环境隔离问题](<./07-配置 Profiles 与环境隔离问题.md>)

如果你想先回到上一阶段入口重新确认位置：
- [01-总览](./01-总览.md)
