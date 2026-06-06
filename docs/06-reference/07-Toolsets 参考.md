# 🗂️ 07-Toolsets 参考

> 这页查的是 Hermes 的 toolsets，也就是“工具包”层，不是单个工具细节。 如果你要查具体内置工具，请看 [06-Built-in Tools 参考](<./06-Built-in%20Tools%20%E5%8F%82%E8%80%83.md>)。

## 📋 速答（你可能正在搜的）

**Hermes Agent 的 toolset 是什么？**
> Toolset 是 Hermes 的"工具权限包"——每个工具归属到一个 toolset，启用某个 toolset 时包内工具一起可用。比如开 `file` 就能用 `read_file`、`write_file`、`search_files`、`patch`，开 `web` 就能用 `web_search` + `web_extract`。

**Hermes Agent 有哪些内置 toolset？**
> 分三类：Core（`file`、`terminal`、`web`、`search`、`browser`、`skills`、`vision`、`tts`、`memory`、`session_search` 等）、Composite（`debugging`、`safe` 等组合包）、Platform（`hermes-cli`、`hermes-telegram` 等平台默认配置）。共约 15 个 core toolset。

**怎么按需开启或关闭 toolset？**
> 会话内用 `/tools enable/disable` 管理当前 session；启动时用 `hermes chat --toolsets web,file,terminal` 指定；平台级默认配置在 `config.yaml` 的 `toolsets` 列表或 `hermes tools` 命令管理。

**为什么 CLI 和 Telegram 里可用工具不一样？**
> 因为不同平台有不同的 platform toolset（如 `hermes-cli` 和 `hermes-telegram`），它们定义了各自入口的默认工具权限边界。同一个 Hermes 在不同平台上能力范围可以不同，这是设计如此而非 bug。

## 🎯 1. 页面用途

这一页帮助你查 toolsets 的概念、分类和配置方式。

它适合用来查：

- Toolset 到底是什么
- Core / Composite / Platform 三类 toolsets 的区别
- 为什么不同平台看到的工具不同
- `hermes chat --toolsets ...` 怎么理解
- `config.yaml` 里按平台配置 toolsets 的思路

这页不负责：

- 某个具体工具为什么不显示的排障
- MCP server 过滤规则排障
- gateway 平台权限异常排障

## 🔹 2. 官方来源

- 官方页面：<https://hermes-agent.nousresearch.com/docs/reference/toolsets-reference>
- 官方页面标题：Toolsets Reference
- 官方页面定位：说明 toolsets 是如何决定 agent 可用工具范围的

中文站这一页保留官方的 toolset 分类与配置思路，但会把“tool / toolset / platform toolset”之间的关系讲清楚。

## 🧭 3. 什么时候查这页

下面这些场景，最适合查这页：

- 你想按 session 限制工具能力
- 你想知道 `debugging`、`safe` 这类名字是什么
- 你想理解 `hermes-cli`、`hermes-telegram` 这种平台级 toolset
- 你想知道为什么 CLI 和 Telegram 里工具范围不一样
- 你想决定“给这个入口开哪些工具”

如果你要解决的是“为什么我明明开了还是看不到”，那更偏排障。

## 🧠 4. 核心概念中文解释

### 4.1 Toolset 可以理解成“工具权限包”

中文最容易理解的说法就是：

Toolset = 一组工具的命名打包。

你不是一个个告诉 Hermes “给我开 read_file、再开 terminal、再开 web_extract”，而是常常直接说：

- 开 `file`
- 开 `terminal`
- 开 `web`
- 或者开一个组合包

### 4.2 每个工具只属于一个 toolset

官方强调了一条核心规则：

- 每个 tool 都归属到一个 toolset
- 开启某个 toolset 时，这个包里的工具就一起可用

所以 toolsets 是配置工具可用性的主要机制。

### 4.3 三类 Toolsets

官方把 toolsets 分成三类：

- Core toolsets
- Composite toolsets
- Platform toolsets

可以把它们理解成三层：

- Core：基础工具组
- Composite：把多个 core 合起来的快捷组合
- Platform：某个平台默认整套工具配置

### 4.4 Toolsets 决定“同一个 Hermes 在不同入口能做什么”

这就是为什么：

- CLI 里和 Telegram 里工具不一定一样
- 不同 session 的工具也不一定一样
- 同一个模型下，能力范围可能因为 toolset 配置不同而不同

## ⚡ 5. 常用项速查

### 5.1 三类 toolsets 速查

| 类型 | 中文解释 | 例子 |
|---|---|---|
| Core | 单一逻辑工具组 | `file`、`web`、`terminal` |
| Composite | 多个 core 的组合快捷方式 | `debugging`、`safe` |
| Platform | 某平台的整套工具配置 | `hermes-cli`、`hermes-telegram` |

### 5.2 最常见的 core toolsets

| Toolset | 主要内容 | 你通常什么时候会碰到 |
|---|---|---|
| `file` | 读写搜改文件 | 文档 / 代码改动 |
| `terminal` | shell 与进程 | 构建、测试、git、系统命令 |
| `web` | 搜索 + 抽取网页 | 查资料、抓网页正文 |
| `search` | 只搜索不抽取 | 先快速检索 |
| `browser` | 浏览器交互 | 点网页、看动态页面 |
| `skills` | skill 浏览与管理 | 查或安装 skills |
| `session_search` | 查历史会话 | 回忆过去上下文 |
| `vision` | 看图 | 图片分析 |
| `tts` | 文本转语音 | 语音输出 |
| `memory` | 持久记忆 | 跨会话记忆 |

### 5.3 最容易混淆的一组点

| 你看到的名字 | 实际更接近什么 |
|---|---|
| `file` | 基础 core toolset |
| `debugging` | 多个 core 合成的 composite toolset |
| `hermes-cli` | 平台级 toolset |
| `/tools enable browser` | 当前 session 开关层 |
| `hermes tools` | 平台配置层 |

## 🗂️ 6. 完整参考结构

### 6.1 按 session 配置 toolsets

官方常见写法：

```bash
hermes chat --toolsets web,file,terminal
hermes chat --toolsets debugging
hermes chat --toolsets all
```

中文理解：

- `web,file,terminal`：手工点名开哪些工具包
- `debugging`：使用一个合成组合包
- `all`：全部开启

中文站建议：

- 新手不要默认 `all`
- 明确知道任务边界时，再做精细开启

### 6.2 按平台配置 toolsets

官方示例：

```yaml
toolsets:
  - hermes-cli
  # - hermes-telegram
```

这里真正表达的是：

- CLI 可以有一套默认工具权限
- Telegram / Gateway 可以有另一套默认权限

也就是说，平台本身就是一层能力边界。

### 6.3 交互式管理方式

官方提到两种高频入口：

#### CLI 配置入口

```bash
hermes tools
```

它更偏平台配置层。

#### 会话内管理入口

```text
/tools list
/tools disable browser
/tools enable rl
```

它更偏当前 session 的即时控制。

### 6.4 Core toolsets 怎么理解

官方 reference 列了大量 core toolsets。 对中文用户来说，最实用的记法是按工作类型来记：

#### 内容 / 代码 / 文件类

- `file`
- `terminal`
- `web`
- `search`
- `browser`

#### 组织 / 记忆 / 辅助输出类

- `skills`
- `session_search`
- `memory`
- `todo`
- `tts`
- `vision`

#### 自动化 / 高级能力类

- `cronjob`
- `delegation`
- `code_execution`
- `messaging`
- `moa`
- `mcp` 相关能力入口（通过其他配置配合）

### 6.5 Composite toolsets 怎么理解

Composite toolset 的作用就是：

你不必手工一个个点 core toolset，而是直接用一个“组合名”。

比如：

- `debugging`
- `safe`

实际意义是：

- 快捷
- 语义更明确
- 更适合按任务类型切换能力边界

### 6.6 Platform toolsets 怎么理解

Platform toolset 是最容易被忽视、但对真实落地最重要的一层。

它的意义是：

同一个 Hermes，在不同入口平台上，不一定应该拥有同样的工具权限。

例如：

- CLI：可以更强
- Telegram：更要保守
- 某些 comment handler：可能是特化工具集

## ⚠️ 7. 注意事项

### 7.1 不要默认 `all`

官方允许 `all`，但中文站建议你把它理解成：

- 调试时可能有用
- 受控环境里可能有用
- 新手 / 消息平台 / 团队环境下不该默认开满

### 7.2 `search` 和 `web` 不是完全一样

官方明确区分：

- `search`：只有 `web_search`
- `web`：`web_search` + `web_extract`

所以当你只想搜、不想抽取正文时，它们并不是一个层级。

### 7.3 toolset 配置分“当前 session”和“平台默认”两层

如果你把这两层混掉，就会以为：

- 我在会话里 enable 了，为什么重开没了？
- 我在平台里开了，为什么当前 session 表现不一样？

实际上它们就是两层不同作用域。

## 🚦 8. 出问题了去哪

| 你现在卡在哪 | 先去哪里 |
|---|---|
| toolset 开了但工具没出现 | [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/06-Tools%20Skills%20MCP%20%E9%97%AE%E9%A2%98.md>) |
| messaging 平台工具和 CLI 不一致 | [05-遇到问题 / 05-Gateway Messaging 与推送问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/05-Gateway%20Messaging%20%E4%B8%8E%E6%8E%A8%E9%80%81%E9%97%AE%E9%A2%98.md>) |
| 配置改了像没生效 | [05-遇到问题 / 07-配置 Profiles 与环境隔离问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/07-%E9%85%8D%E7%BD%AE%20Profiles%20%E4%B8%8E%E7%8E%AF%E5%A2%83%E9%9A%94%E7%A6%BB%E9%97%AE%E9%A2%98.md>) |
| 不确定问题在哪 | [05-遇到问题 / 01-总览](../05-遇到问题/01-总览.md) |

## 🌐 9. 官方原文链接

- 官方 Toolsets Reference：<https://hermes-agent.nousresearch.com/docs/reference/toolsets-reference>
- 官方 Built-in Tools Reference：<https://hermes-agent.nousresearch.com/docs/reference/tools-reference>

## 📚 10. 相关中文站页面

- [01-总览｜Reference 参考手册](./01-总览.md)
- [06-Built-in Tools 参考](<./06-Built-in%20Tools%20%E5%8F%82%E8%80%83.md>)
- [08-MCP 配置参考](<./08-MCP%20%E9%85%8D%E7%BD%AE%E5%8F%82%E8%80%83.md>)
- [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/06-Tools%20Skills%20MCP%20%E9%97%AE%E9%A2%98.md>)
- [05-遇到问题 / 05-Gateway Messaging 与推送问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/05-Gateway%20Messaging%20%E4%B8%8E%E6%8E%A8%E9%80%81%E9%97%AE%E9%A2%98.md>)

## ➡️ 下一步

完成后进入：

- [08-MCP 配置参考](<./08-MCP%20%E9%85%8D%E7%BD%AE%E5%8F%82%E8%80%83.md>)

如果你想先回到上一阶段入口重新确认位置：

- [01-总览｜Reference 参考手册](./01-总览.md)

---

## 🔗 Reference 相关入口

- 第一次使用 Hermes：先看[从这开始](/docs/start)，不要直接从参考表硬啃。
- 查命令：看[CLI 命令参考](/docs/reference/cli-commands)和[Slash Commands 参考](/docs/reference/slash-commands)。
- 查 Profiles / Tools / Skills / MCP：分别看[Profile 命令参考](/docs/reference/profile-commands)、[Built-in Tools 参考](/docs/reference/built-in-tools)、[内置 Skills 目录](/docs/reference/bundled-skills)和[MCP 配置参考](/docs/reference/mcp-config)。
- 配置报错：回到[遇到问题](/docs/issues)，按模型、Gateway、Tools、Profiles 或远程环境分类排查。
