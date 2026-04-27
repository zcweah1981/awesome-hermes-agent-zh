# 🔌 05-把 Hermes 接进外部系统

这一页只解决一件事：
当你想让 Hermes 去用一个已经存在的外部工具或系统时，先用 MCP 跑通第一条接入主线。

![结构图：当前阶段更自然的外部系统接入主线是 Hermes → MCP server → 外部工具系统；Plugins 在后位补充，不是这一页的主线](../../assets/rm2-5-mcp-and-plugins-01-main-route.png)

---

## 先判断：你是不是在做“外部系统接入”

下面这些情况，通常就该先看 MCP：

- 你想让 Hermes 调 GitHub、数据库、文件系统、浏览器、内部 API
- 你接的是一个已经存在的工具服务器
- 你更关心“先接上能用”，不是“先写 Hermes 内部扩展”
- 你希望这些能力以后像普通工具一样被调用

一句话：
如果你的需求是“让 Hermes 去用一个现成系统”，先看 MCP，通常最顺。

---

## 这一步为什么重要

把 Hermes 接进外部系统，能力会发生实质变化：

1. Hermes 不再只局限在聊天窗口内部
2. 它开始能直接调用外部工具和服务
3. 后面的服务化、自动化、编辑器工作流才真正有现实基础

所以这一步的意义不是多了个名词，而是 Hermes 开始真的接触外部世界。

---

## 为什么当前阶段先 MCP，不先钻 Plugins

这不是说 Plugins 不重要。

而是从用户视角，当前阶段更自然的主线是：

- 你要接外部工具系统
- MCP 就是默认入口
- 接进来后，Hermes 会把这些能力当普通工具来用

所以这一页不展开插件开发手册，只先帮你把“怎么接上一个外部系统”走通。

---

## 最短接入路径

### 第 1 步：安装 MCP 支持

在终端执行：

```bash
cd ~/.hermes/hermes-agent
uv pip install -e ".[mcp]"
```

成功后，这台 Hermes 才具备 MCP 相关能力。

### 第 2 步：在 `~/.hermes/config.yaml` 里写 `mcp_servers`

配置入口是：

```yaml
mcp_servers:
```

如果你接的是本地 stdio server，最小示例可以写成：

```yaml
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
```

如果你接的是远端 HTTP server，最小示例可以写成：

```yaml
mcp_servers:
  company_api:
    url: "https://mcp.example.com/mcp"
    headers:
      Authorization: "Bearer ***"
```

你这一步只要先分清两类：

- stdio server
- HTTP server

### 第 3 步：启动 Hermes

执行：

```bash
hermes chat
```

或者进入你平时使用的入口，只要能正常启动即可。

### 第 4 步：立刻交给它一个依赖外部系统的真实任务

例如：

- 列某个目录文件
- 查 GitHub issue / PR
- 访问某个内部 API
- 查询某个数据库结果

只有真实任务成功，才算真正接上。

---

## 成功信号

### 1. Hermes 真能通过外部系统完成一件事

这是最强成功信号。
不是“配置没报错”，而是“任务真的做成了”。

### 2. MCP 工具已经像普通工具一样被 Hermes 使用

你的心智应该变成：
Hermes 新获得了一组工具，而不是多了一套平行宇宙机制。

### 3. 你已经知道现在该继续扩哪一侧

跑通后，你会更清楚自己接下来要走：

- 更深的系统接入
- 服务化暴露
- 自动化编排

---

## 第一次失败时，先查这 5 件事

### 1. MCP extra 有没有装上

回看安装命令是否成功执行。

### 2. `mcp_servers` 是不是写在正确配置文件里

重点检查：

```text
~/.hermes/config.yaml
```

### 3. 你配置的是 stdio 还是 HTTP

两类 server 的写法不同，别混写。

### 4. 外部 server 自己能不能工作

不要只盯 Hermes，也要确认目标 server 本身是可启动、可访问的。

### 5. 你有没有用一个真实任务验收

如果没有真实任务，只看配置很难判断到底接没接上。

---

## 什么时候算通过

当你已经满足下面这些判断，这一页就算通过：

- 我知道当前阶段外部系统接入的主线是 MCP
- 我知道 MCP 更适合“让 Hermes 去用现成外部系统”
- 我知道最短接法是：安装支持、写 `mcp_servers`、启动 Hermes、做真实任务验证
- 我知道成功标准不是配置存在，而是任务真的能通过外部系统完成

---

## ➡️ 下一步
完成后进入：
- [06-把 Hermes 暴露成后端服务](<./06-把%20Hermes%20暴露成后端服务.md>)
如果你想先回到上一阶段入口重新确认位置：
- [04-自己造东西](<./01-总览.md>)
