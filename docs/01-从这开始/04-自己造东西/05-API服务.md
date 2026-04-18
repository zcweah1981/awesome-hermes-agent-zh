# API Server：把 Hermes 暴露成可被前端接入的后端服务

这一页只解决一个问题：
当你不想再只把 Hermes 用在 CLI 或单个聊天窗口里，而是想让它被前端、客户端或你自己的应用通过 HTTP 调用时，API Server 就是这一层入口。

![结构图：Open WebUI、LobeChat、LibreChat 等前端，把 OpenAI-compatible /v1 请求打到 Hermes API Server；Hermes 再用自己的工具、文件、网页、记忆、skills 等能力完成任务](../assets/rm2-5-api-server-01-openai-compatible-backend-map.png)

---

## 什么情况下值得先走 API Server

当你遇到下面这些需求时，通常就值得先走 API Server：

- 你已经不满足于只在命令行里和 Hermes 聊
- 你想把 Hermes 接到一个现成的聊天前端里
- 你想让团队成员通过统一界面来用 Hermes，而不是每个人都先学一遍 CLI
- 你想让自己的前端、内部工具或轻应用把 Hermes 当后端服务来调用
- 你需要的是“一个可接入的 HTTP 能力入口”，而不只是“我自己开一个聊天窗口”

把它说得更直白一点：
如果你的目标开始变成“让别的界面或程序也能用到 Hermes”，这一页就该看了。

---

## 它和单纯 CLI / 单个聊天窗口有什么不同

CLI 或单个聊天窗口，重点是“你本人直接在某个入口里使用 Hermes”。

API Server 的重点则是：
“让 Hermes 变成一个能被外部前端或客户端接入的后端服务”。

两者的差别可以这样理解：

<table>
  <colgroup>
    <col style="width: 26%;" />
    <col style="width: 37%;" />
    <col style="width: 37%;" />
  </colgroup>
  <thead>
    <tr>
      <th>使用方式</th>
      <th>你主要在做什么</th>
      <th>更适合什么场景</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CLI / 单个聊天窗口</td>
      <td>你自己直接和 Hermes 交互</td>
      <td>个人使用、调试、快速试验、单入口工作</td>
    </tr>
    <tr>
      <td>API Server</td>
      <td>把 Hermes 暴露成 OpenAI-compatible HTTP API，让别的前端或程序来接它</td>
      <td>接 Open WebUI、LobeChat、LibreChat、NextChat、ChatBox，或你自己的前端 / 应用</td>
    </tr>
  </tbody>
</table>

所以这一页真正要你建立的心智不是“又多了一个聊天入口”。
而是：
Hermes 可以站在后面，前面换成你想要的界面。

---

## 它到底是什么：OpenAI-compatible HTTP API

官方给出的核心定位很明确：
Hermes 可以运行一个 OpenAI-compatible HTTP API server。

这意味着：

- 暴露出来的是 OpenAI-compatible 的 `/v1` 风格接口
- 多数会说 OpenAI 格式的前端，都可以把 Hermes 当后端来接
- 典型例子包括 Open WebUI、LobeChat、LibreChat、NextChat、ChatBox 等
- 前端虽然是在用 OpenAI-compatible API，但后端真正执行任务的是 Hermes
- 请求进来后，Hermes 仍然可以使用自己的工具能力，例如终端、文件操作、网页搜索、记忆、skills 等

这一点非常关键：
API Server 不是把 Hermes 变成“只会返回文本的裸模型接口”。
它是把 Hermes 整体能力，通过 OpenAI-compatible 的 HTTP 形式暴露出去。

---

## 最短接法

这一页不展开部署架构，也不展开端点百科。
先记住最短的 5 步就够了。

### 第 1 步：在 `~/.hermes/.env` 里打开 API Server

把下面这项写进去：

```env
API_SERVER_ENABLED=true
```

这表示当前 Hermes profile 允许 gateway 同时暴露 API server。

### 第 2 步：设置 `API_SERVER_KEY`

继续在 `~/.hermes/.env` 里设置一个 key：

```env
API_SERVER_KEY=change-me-local-dev
```

你可以先把它理解成：
这是前端或客户端调用 Hermes API 时要带的 Bearer key。

### 第 3 步：如果浏览器要直连，再按需加 `API_SERVER_CORS_ORIGINS`

如果只是本机工具、桌面客户端或服务端去接，通常先不用管这项。

只有在“浏览器页面要直接请求 Hermes API”时，才按需加：

```env
API_SERVER_CORS_ORIGINS=http://localhost:3000
```

所以这一步是可选项，不是所有人都要先配。

### 第 4 步：启动 gateway

```bash
hermes gateway
```

官方快速路径里，API Server 是跟着 gateway 一起启动的。

### 第 5 步：让前端把 base URL 指到 `http://localhost:8642/v1`

大多数 OpenAI-compatible 前端，核心就是填这几类信息：

- Base URL：`http://localhost:8642/v1`
- API Key：你刚才配置的 `API_SERVER_KEY`
- Model：通常填 `hermes-agent`

如果你接的是 Open WebUI、LobeChat、LibreChat、NextChat、ChatBox 这类工具，思路都一样：
把它们原本要连 OpenAI 的地方，改成连你本地 Hermes API Server。

---

## 成功信号看什么

这一页最重要的是会判断“到底有没有接上”。

你可以看 3 个成功信号。

### 1）gateway 输出 API server listening

官方快速起步里，成功启动后会出现类似输出：

```text
[04-自己造东西/API服务] API server listening on http://127.0.0.1:8642
```

这说明 API Server 已经跟着 gateway 起起来了。

### 2）`/health` 可以访问

如果健康检查可用，说明最基本的 HTTP 服务已经在响应。

当前页你只要记住：
`GET /health` 是最轻量的探活信号。

### 3）对 `/v1/chat/completions` 发请求能正常返回

例如用 `curl` 去打：

```bash
curl http://localhost:8642/v1/chat/completions \
  -H "Authorization: Bearer your-api-server-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "hermes-agent",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ]
  }'
```

如果它能正常返回结果，就说明这已经不是“服务开着而已”，而是“前端同类请求也有基础可以接通”。

一句话总结：
看启动日志、看 `/health`、看一次真实 `/v1/chat/completions` 返回，这 3 个信号最实用。

---

## 当前页只知道这些端点就够了

这一页不是 OpenAI API 规范全文。
你现在只要知道 Hermes API Server 至少覆盖这类入口：

- `POST /v1/chat/completions`
- `POST /v1/responses`
- `GET /v1/models`
- `GET /health`

当前页的重点不是背端点大全。
重点是你已经知道：
Hermes 对外暴露的是一套 OpenAI-compatible HTTP API，而且前端可以直接拿来接。

---

## 哪些情况先不在这一页展开

为了保证当前页边界清楚，这几个方向先不展开：

- OpenAI API 全量字段和完整规范
- 每个前端各自的 UI 配置差异
- 生产环境部署、反向代理、HTTPS、外网暴露
- 更细的鉴权策略和多用户隔离
- Responses API 的完整会话状态细节
- 流式事件、工具进度事件、SSE 细节
- Cron / Automation 怎么和 API Server 组合使用

这一页只先帮你建立一个稳定结论：
当你要把 Hermes 接进前端或应用时，API Server 是“服务化暴露”的那一步。

---

## 什么时候算通过

当前页学完，至少要满足下面这些判断，才算通过：

- 你已经知道什么情况下该把 Hermes 暴露成后端服务
- 你已经能说清 API Server 和 CLI / 单个聊天窗口的区别
- 你已经知道 Hermes 暴露的是 OpenAI-compatible HTTP API
- 你已经知道多数 OpenAI-compatible 前端都能接它，典型例子包括 Open WebUI、LobeChat、LibreChat、NextChat、ChatBox
- 你已经知道最短接法是：在 `~/.hermes/.env` 里打开 `API_SERVER_ENABLED`、设置 `API_SERVER_KEY`、按需加 `API_SERVER_CORS_ORIGINS`、启动 gateway、把 base URL 指向 `http://localhost:8642/v1`
- 你已经知道成功信号应该看启动日志、`/health` 和一次真实的 `/v1/chat/completions` 返回

如果一句话判断：
你已经能把“我自己在用 Hermes”切换成“别的前端也能把 Hermes 当后端来用”，这一页就算过了。

---

## 👉 下一步去哪

如果你想回到这一层入口重新确认位置：

- [04-自己造东西](../总览.md)
- [MCP / Plugins](./04-MCP与插件.md)
- [01-从这开始](../总览.md)

当前页通过后，下一步路径是：
[04-自己造东西/自动化](./06-自动化.md)

这条路径已经在仓库里落地，直接点下一页即可。

---

## 官方依据

- 官方 API Server 文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server>
- 官方 Integrations 文档：<https://hermes-agent.nousresearch.com/docs/integrations/>

这一页只使用了当前页必须用到的用户边界：

- Hermes API Server 暴露为 OpenAI-compatible HTTP API
- 多数 OpenAI-compatible 前端都能接它
- 最短接法包含 `API_SERVER_ENABLED`、`API_SERVER_KEY`、可选 `API_SERVER_CORS_ORIGINS`、启动 gateway、使用 `http://localhost:8642/v1`
- 成功信号包含 listening 日志、`/health`、以及 `/v1/chat/completions` 的正常返回
- 当前页只点到 `chat/completions`、`responses`、`models`、`health` 这些入口，不扩成端点大全
