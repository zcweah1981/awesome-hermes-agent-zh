# 🧰 06-Built-in Tools 参考

> 这页查的是 Hermes 内置工具（built-in tools），以及它们和 toolsets、平台、凭据之间的关系。 如果你要查 MCP server 暴露出来的工具，请看 [08-MCP 配置参考](<./08-MCP%20%E9%85%8D%E7%BD%AE%E5%8F%82%E8%80%83.md>)。

## 1. 页面用途

这一页帮助你理解 Hermes 内置工具的查表逻辑。

它适合用来查：

- Hermes 内置工具有哪些大类
- 为什么工具不是永远全部可见
- built-in tools 和 MCP tools 的区别
- 哪些工具组属于 browser、file、terminal、web、skills、vision 等 toolset
- 为什么某些工具只在特定平台或凭据下出现

这页不负责：

- tools 不显示的排障
- MCP server 连不上排障
- Feishu / Home Assistant 等特定工具接入排障

## 2. 官方来源

- 官方页面：<https://hermes-agent.nousresearch.com/docs/reference/tools-reference>
- 官方页面标题：Built-in Tools Reference
- 官方页面定位：记录 Hermes tool registry 中的 built-in tools，并按 toolset 分组

中文站这一页不会把 50+ 工具原样长表堆给你，而是先帮你建立“怎么查”的结构。

## 3. 什么时候查这页

你遇到下面这些场景时，就该先查这页：

- 你想知道 Hermes 现在自带了哪些工具大类
- 你想分清 browser tools、file tools、terminal tools、web tools 的边界
- 你想知道为什么别人能用某工具，你这里却看不到
- 你想分清 built-in tools 和 MCP tools
- 你想知道某类工具通常依赖什么前提

如果你要解决的是“为什么它现在不能用”，那已经偏排障。

## 4. 核心概念中文解释

### 4.1 Built-in Tools 是 Hermes 自带注册的工具

最简单的理解方式是：

- built-in tools：Hermes 项目本身就带着的工具
- MCP tools：通过外部 MCP server 动态接进来的工具

所以你先不要把“能在 Hermes 里调用的工具”全混成一堆。

### 4.2 工具可用性不是固定不变的

官方明确指出，工具是否出现，取决于：

- 平台
- 凭据
- 已启用的 toolsets

也就是说：

- 在 CLI 里能看到，不代表 Telegram 里一定有
- 没配置 key，不代表工具“被删了”
- toolset 没开，也不会出现对应工具

### 4.3 MCP tools 会带 server-name 前缀

官方给出的典型例子是：

```text
github_create_issue
```

这里 `github` 就是 MCP server 名称前缀。

所以如果你看到这种命名，优先判断它是不是来自 MCP，而不是 Hermes 内置 registry。

### 4.4 Built-in Tools 和 Toolsets 是两层关系

你可以这样记：

- tool = 具体能力
- toolset = 一组打包后的能力

所以在实际使用中，你往往不是一个个开工具，而是启用某个 toolset。

## 5. 常用项速查

### 5.1 先记住的工具大类

| 工具大类 | 主要用途 | 常见代表 |
|---|---|---|
| browser | 交互式网页操作 | `browser_navigate`、`browser_click`、`browser_snapshot` |
| file | 文件读写查改 | `read_file`、`write_file`、`search_files`、`patch` |
| terminal | Shell 执行与进程管理 | `terminal`、`process` |
| web | Web 搜索与网页抽取 | `web_search`、`web_extract` |
| skills | Skill 浏览与管理 | `skills_list`、`skill_view`、`skill_manage` |
| memory | 持久记忆管理 | `memory` |
| vision | 图片分析 | `vision_analyze` |
| tts | 文本转语音 | `text_to_speech` |

### 5.2 最值得先理解的特殊工具

| 工具 | 中文说明 | 什么时候最常见 |
|---|---|---|
| `browser_navigate` | 浏览器会话入口 | 几乎所有 browser 工具前都要先调它 |
| `read_file` | 读文件 | 查代码 / 查 markdown |
| `search_files` | 查文件或内容 | 在 repo 里找路径 / 文本 |
| `patch` | 定位替换编辑 | 小范围安全改文件 |
| `terminal` | 执行 shell 命令 | 构建、git、测试、系统查询 |
| `execute_code` | 用 Python 串联多个工具 | 复杂多步处理 |
| `delegate_task` | 派子代理做隔离任务 | 并行研究 / 并行编码 |
| `clarify` | 向用户追问 | 需要用户决策时 |
| `cronjob` | 定时任务 | 自动巡检 / 定时执行 |

### 5.3 最容易混淆的一组点

| 你看到的现象 | 更准确的理解 |
|---|---|
| 工具没出现 | 可能是 toolset / 平台 / 凭据没满足 |
| 出现了 `github_xxx` 这类工具 | 很可能是 MCP tool，不是 built-in tool |
| browser 工具不能直接点网页 | 往往要先 `browser_navigate` |
| `search` 和 `web` 看起来像一回事 | `search` 只搜，`web` 还会抽取网页 |
| Feishu 工具没在常规聊天里出现 | 官方明确有作用域限制，不是通用暴露 |

## 6. 完整参考结构

### 6.1 官方定义下的 built-in tools

官方把 built-in tools 视为：

Hermes tool registry 中已经注册好的工具集合。

它们和 MCP tools 的核心区别是：

- built-in：跟着 Hermes 项目走
- MCP：跟着你配置的外部 MCP server 走

### 6.2 常见 core toolset 对应的工具组

#### Browser

适合：

- 打开网页
- 点击
- 输入
- 滚动
- 快照
- 浏览器 vision
- 控制台检查

常见工具：

- `browser_navigate`
- `browser_snapshot`
- `browser_click`
- `browser_type`
- `browser_scroll`
- `browser_press`
- `browser_console`
- `browser_get_images`
- `browser_vision`

关键注意：

大多数 browser 工具之前，要先有 `browser_navigate`。

#### File

适合：

- 读文件
- 写文件
- 搜文件
- 精准 patch 文件

常见工具：

- `read_file`
- `write_file`
- `search_files`
- `patch`

#### Terminal

适合：

- 跑 shell 命令
- 跑测试
- 执行 git
- 管理后台进程

常见工具：

- `terminal`
- `process`

#### Web

适合：

- 搜 web
- 抽取网页正文

常见工具：

- `web_search`
- `web_extract`

#### Skills / Memory / Delegation / Code Execution

这些不一定是新手首先想到的“工具”，但它们在 Hermes 里同样是非常核心的内置工具组：

- `skills_list` / `skill_view` / `skill_manage`
- `memory`
- `delegate_task`
- `execute_code`
- `todo`
- `session_search`

### 6.3 官方特别提到的几个边界

#### MCP tools 不是 built-in tools

这一点必须单独强调。

如果你通过 MCP server 加进来一堆工具，它们并不归入 built-in tools 页面本体。

#### Feishu 工具有作用域限制

官方原文里明确说明：

- Feishu doc / drive comment 相关工具并不是在所有表面都通用可见
- 它们有特定 handler 范围

所以如果你在普通 CLI / 常规消息平台里没看到，不应该先假设“文档写错了”。

#### Honcho tools 已不再算 built-in

官方还特别提到一件事：

某些 Honcho 相关工具已经转到 Honcho memory provider plugin，不再算 built-in tools 本体。

这也是为什么查工具时要分清：

- 核心内置
- 插件提供
- MCP 动态提供

## 7. 注意事项

### 7.1 这页是“查工具分类”，不是“查所有工具全量细节”

如果你要逐项核对每个工具 schema、参数、调用约束，请以官方原文为准。

中文页这里主要解决的是：

- 先帮你分类
- 先帮你分边界
- 先帮你建立脑图

### 7.2 工具不可用，不一定是 bug

更常见的原因是：

- 平台不对
- 凭据没配
- toolset 没启用
- 当前不是对应 handler / surface

### 7.3 Built-in Tools 和 Toolsets 要分两层看

如果你把它们混成一层，很容易出现两种误判：

- 以为“开了一个 tool”就等于“开了一组能力”
- 以为“toolset 名字”就是具体 tool 名字

## 8. 出问题了去哪

| 你现在卡在哪 | 先去哪里 |
|---|---|
| tools / skills / MCP 不生效 | [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/06-Tools%20Skills%20MCP%20%E9%97%AE%E9%A2%98.md>) |
| messaging 平台里工具不一致 | [05-遇到问题 / 05-Gateway Messaging 与推送问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/05-Gateway%20Messaging%20%E4%B8%8E%E6%8E%A8%E9%80%81%E9%97%AE%E9%A2%98.md>) |
| 配置改了工具还是没变 | [05-遇到问题 / 07-配置 Profiles 与环境隔离问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/07-%E9%85%8D%E7%BD%AE%20Profiles%20%E4%B8%8E%E7%8E%AF%E5%A2%83%E9%9A%94%E7%A6%BB%E9%97%AE%E9%A2%98.md>) |
| 不确定问题在哪 | [05-遇到问题 / 01-总览](../05-遇到问题/01-总览.md) |

## 9. 官方原文链接

- 官方 Built-in Tools Reference：<https://hermes-agent.nousresearch.com/docs/reference/tools-reference>
- 官方 Toolsets Reference：<https://hermes-agent.nousresearch.com/docs/reference/toolsets-reference>
- 官方 MCP Config Reference：<https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference>

## 10. 相关中文站页面

- [01-总览｜Reference 参考手册](./01-总览.md)
- [07-Toolsets 参考](<./07-Toolsets%20%E5%8F%82%E8%80%83.md>)
- [08-MCP 配置参考](<./08-MCP%20%E9%85%8D%E7%BD%AE%E5%8F%82%E8%80%83.md>)
- [09-内置 Skills 目录](<./09-%E5%86%85%E7%BD%AE%20Skills%20%E7%9B%AE%E5%BD%95.md>)
- [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/06-Tools%20Skills%20MCP%20%E9%97%AE%E9%A2%98.md>)

## ➡️ 下一步

完成后进入：

- [07-Toolsets 参考](<./07-Toolsets%20%E5%8F%82%E8%80%83.md>)

如果你想先回到上一阶段入口重新确认位置：

- [01-总览｜Reference 参考手册](./01-总览.md)
