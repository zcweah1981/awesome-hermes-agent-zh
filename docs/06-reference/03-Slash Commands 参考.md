# 03-Slash Commands 参考

> 这页查的是你已经进入 Hermes 对话之后，在会话里输入的 `/xxx` 命令。 如果你要查终端 shell 里的 `hermes ...`，请看 [02-CLI 命令参考](<./02-CLI 命令参考.md>)。

## 1. 页面用途

这一页用来查 Hermes 的 Slash Commands，也就是你在 Hermes 对话界面里直接输入的 `/...` 命令。

它适合用来查：

- `/new`、`/reset`、`/clear` 这些会话类命令
- `/model`、`/provider`、`/verbose`、`/reasoning` 这些配置类命令
- `/tools`、`/toolsets`、`/skills`、`/browser` 这些工具与技能类命令
- `/save`、`/history`、`/undo`、`/retry` 这些日常交互命令
- Interactive CLI 和 Messaging Gateway 这两个 slash command 表面的区别
- 为什么有些 command 会动态出现

这页不负责：

- CLI 命令排查
- slash command 不显示 / 不生效的排障
- gateway 权限或平台配置失败排查
- tools / skills / MCP 失效排查

如果你要解决的是“为什么 `/tools` 结果不对”，请直接跳到文末的“出问题了去哪”。

## 2. 官方来源

- 官方页面：<https://hermes-agent.nousresearch.com/docs/reference/slash-commands>
- 官方页面标题：Slash Commands Reference
- 官方页面定位：记录 Hermes 对话中可用的 slash commands

中文站这一页保持官方的命令分组与边界，但会把“两个表面”“动态命令”“常见误区”讲得更直接。

## 3. 什么时候查这页

你在下面这些场景里，最适合来这页：

- 你已经进入 Hermes，会话里想输入 `/`，但记不清有哪些命令
- 你想区分 `/model` 和 `hermes model`
- 你想找 `/new`、`/history`、`/save`、`/undo` 这类会话命令
- 你想确认 `/tools`、`/toolsets`、`/skills`、`/browser` 的用途
- 你想知道为什么有些 slash commands 是固定的，有些是 skill 动态带出来的

如果你还没建立“CLI 命令”和“会话命令”的区别，建议先看：

- [02-CLI 命令参考](<./02-CLI 命令参考.md>)
- [01-从这开始 / 02-开始上手 / 03-常用斜杠命令与会话管理](../01-从这开始/02-开始上手/03-常用斜杠命令与会话管理.md)

## 4. 核心概念中文解释

### 4.1 Slash Commands 和 CLI Commands 的区别

这是最重要的一条：

- CLI 命令：在终端里输入 `hermes ...`
- Slash Commands：已经进入 Hermes 对话后，在会话里输入 `/...`

例如：

```bash
hermes model
hermes chat --continue
```

属于 CLI。

而：

```text
/model
/tools
/new
/help
```

属于 Slash Commands。

### 4.2 Hermes 有两个 slash command 表面

官方明确说 Hermes 有两类 slash-command surface：

- Interactive CLI
- Messaging Gateway

可以把它理解成：

- 你在本地终端里使用 Hermes 时，有一套 slash commands
- 你在 Telegram / Discord / Slack 等消息平台里使用 Hermes 时，也可能有 slash commands

它们共用一套中央注册逻辑，但不是每个平台都完全一致。

### 4.3 动态 slash commands 是“装了 skill 才会出现”

这一点很容易误解。

Hermes 里并不是所有 `/xxx` 都是写死的。

部分 slash commands 会随着你安装的 skills 动态出现。也就是说：

- 有些命令是 Hermes 自带的
- 有些命令来自已安装 skill
- 所以你和别人截图里的 `/` 菜单不一定完全一样

### 4.4 `/model` 不是新增 provider 的入口

这是最常见的误区之一。

- `/model`：切换已经配置好的 provider / model
- `hermes model`：在终端里新增 provider、做 OAuth、填 API Key、设默认模型

如果你想新增 provider，不要在会话里一直试 `/model`，应该退出到终端再运行：

```bash
hermes model
```

## 5. 常用项速查

### 5.1 最常用的会话类命令

| Command | 中文说明 | 什么时候用 |
|---|---|---|
| `/new` | 开新会话 | 想从零开始 |
| `/reset` | `/new` 的别名 | 同上 |
| `/clear` | 清屏并开始新会话 | 想把当前终端界面清干净 |
| `/history` | 查看对话历史 | 回看上下文 |
| `/save` | 保存当前对话 | 手动保存记录 |
| `/retry` | 重试上一条消息 | 上一轮回答异常 |
| `/undo` | 撤销上一轮对话 | 想回退一步 |
| `/title` | 设置当前会话标题 | 给会话命名 |
| `/status` | 看当前 session 信息 | 快速确认当前状态 |
| `/resume [name]` | 恢复历史命名会话 | 回某条旧会话 |

### 5.2 最常用的配置类命令

| Command | 中文说明 | 什么时候用 |
|---|---|---|
| `/model [model-name]` | 查看或切换当前模型 | 已配置好 provider 后切换模型 |
| `/provider` | 查看当前 provider 与可用 provider | 想知道当前在哪个 provider 上 |
| `/verbose` | 切换工具进度显示模式 | 调整输出详细程度 |
| `/fast [normal\|fast\|status]` | 切换 fast mode | 想调速度策略 |
| `/reasoning [level\|show\|hide]` | 管理 reasoning effort 与显示 | 想调推理力度或显示 |
| `/skin` | 查看或切换皮肤 | 想调整 CLI 视觉风格 |
| `/statusbar` | 开关状态栏 | 调整 CLI 信息显示 |
| `/voice [on\|off\|tts\|status]` | 管理语音模式 | 想开关 spoken playback |
| `/yolo` | 开关 YOLO 模式 | 跳过危险命令审批提示 |

### 5.3 最常用的工具 / 技能类命令

| Command | 中文说明 | 什么时候用 |
|---|---|---|
| `/tools [list\|disable\|enable]` | 管理当前 session 的工具 | 想临时开关某类工具 |
| `/toolsets` | 查看可用 toolsets | 想知道有哪些工具包 |
| `/browser [connect\|disconnect\|status]` | 管理本地浏览器连接 | 需要本地 Chrome CDP |
| `/skills` | 搜索、安装、查看或管理 skills | 想装 / 查 skills |
| `/plan [request]` | 进入 plan 模式 | 想先产出计划而不直接执行 |

### 5.4 最容易混淆的一组命令

| 你看到的命令 | 真正作用 | 不要混淆成什么 |
|---|---|---|
| `/model` | 切换已配置好的模型 | 不是新增 provider |
| `hermes model` | 新增 provider / API Key / OAuth / 默认模型 | 不是会话内切换命令 |
| `/tools` | 管理当前 session 工具 | 不是全局平台工具配置 |
| `hermes tools` | 管理平台级工具配置 | 不是临时会话开关 |
| `/plan` | 在会话中启用 plan skill 生成计划 | 不是直接执行任务 |
| `/browser` | 管理本地浏览器连接状态 | 不是网页搜索本身 |

## 6. 完整参考结构

### 6.1 进入方式

在 Interactive CLI 里，输入：

```text
/
```

就会打开 autocomplete 菜单。

官方说明里也强调：

- 内置 commands 大多大小写不敏感
- 但是否出现，还受当前表面和已安装 skills 影响

### 6.2 Session 类命令

官方常见的 session commands 包括：

| Command | 中文说明 |
|---|---|
| `/new` | 开启新 session |
| `/reset` | `/new` 别名 |
| `/clear` | 清屏并开新 session |
| `/history` | 查看对话历史 |
| `/save` | 保存当前会话 |
| `/retry` | 重试上一条消息 |
| `/undo` | 删除上一轮 user/assistant 交换 |
| `/title` | 给当前会话设置标题 |
| `/compress [focus topic]` | 手动压缩上下文 |
| `/rollback [number]` | 查看或恢复文件系统 checkpoints |
| `/snapshot [create\|restore <id>\|prune]` | 管理 Hermes 状态快照 |
| `/stop` | 停掉后台进程 |
| `/queue <prompt>` | 把 prompt 排到下一轮 |
| `/resume [name]` | 恢复历史命名会话 |
| `/agents` | 查看当前 session 的 active agents / tasks |
| `/background <prompt>` | 开一个后台 session 跑任务 |
| `/btw <question>` | 用当前上下文提一个不落盘的侧问 |
| `/branch [name]` | 从当前 session 分叉出一条新路径 |

补充说明：

- `/snapshot` 不只是“看快照”，还可以 create / restore / prune
- `/background` 适合不想阻塞当前 session 的任务
- `/plan` 会写计划，不会直接帮你执行落地

### 6.3 Configuration 类命令

官方把这一组作为会话内配置调整命令。

最常用的是：

| Command | 中文说明 |
|---|---|
| `/config` | 查看当前配置 |
| `/model [model-name]` | 查看或切换当前模型 |
| `/provider` | 查看当前 provider |
| `/personality` | 切换预设 personality |
| `/verbose` | 调工具显示层级 |
| `/fast [normal\|fast\|status]` | 调 fast mode |
| `/reasoning [level\|show\|hide]` | 调 reasoning |
| `/skin` | 切换 display skin |
| `/statusbar` | 开关状态栏 |
| `/voice [on\|off\|tts\|status]` | 管语音模式 |
| `/yolo` | 切换 YOLO |

其中 `/model` 支持的常见写法包括：

```text
/model
/model claude-sonnet-4
/model provider:model
/model custom:model
/model custom:name:model
/model custom --global
```

重点记住：

- 不加 `--global`，通常只影响当前 session
- `--global` 才会把变更持久化到 config

### 6.4 Tools & Skills 类命令

这是会话里最常查的一组：

| Command | 中文说明 |
|---|---|
| `/tools [list\|disable\|enable] [name...]` | 管理当前 session 工具 |
| `/toolsets` | 查看可用 toolsets |
| `/browser [connect\|disconnect\|status]` | 管理 browser CDP 连接 |
| `/skills` | 搜索 / 安装 / 查看 skills |
| `/plan [request]` | 调用 bundled plan skill |

对于这组命令，建议把脑内模型记成两层：

- `/tools`：当前会话现在能不能用
- `hermes tools` / `hermes skills`：全局 / 平台层怎么配

### 6.5 需要特别知道的官方细节

#### `/q` 有冲突

官方页面明确提到一个值得知道的细节：

- `/q` 同时被 `/queue` 和 `/quit` 占用过
- 实际上最后注册生效的通常是 `/quit`

所以如果你真要排队 prompt，不要偷懒写 `/q`，直接写：

```text
/queue <prompt>
```

#### `/plan` 来自 bundled skill

`/plan` 不只是一个普通内置命令，它背后会加载 bundled `plan` skill，并把计划写到 `.hermes/plans/`。

这也正好能帮助理解“动态 slash commands”的逻辑。

#### slash commands 会跨表面变化

同一个 slash command 思路，在 CLI 和 Messaging Gateway 上不一定 1:1。

所以：

- 能在 CLI 里看到，不代表消息平台一定一样
- 消息平台里不生效，也不代表 command 本身不存在

## 7. 注意事项

### 7.1 不要把 `/model` 当成完整配置向导

会话里的 `/model` 更像“切换器”，不是“初始化器”。

如果你要：

- 新增 provider
- 做 OAuth
- 填 API Key
- 配自定义 endpoint

请回终端用 `hermes model`。

### 7.2 动态命令不是 bug 的同义词

有些用户看到别人有 `/plan`、自己没有，就会以为坏了。

但更常见的原因是：

- skill 没装
- 当前平台不支持
- 当前表面不是同一类 surface

### 7.3 Slash Commands 是“会话内管理层”，不是全部能力总表

很多能力会在 slash commands 中暴露入口，但真正的配置和系统管理仍然要回 CLI。

比如：

- `/tools` 管的是当前 session
- `hermes tools` 管的是平台工具配置

### 7.4 这页是“查会话命令”，不是“查为什么 slash command 失效”

如果你现在的问题是：

- `/tools` 看起来不对
- `/` 菜单弹不出来
- messaging 平台里 slash command 不生效

这已经是排障，不是查表。

## 8. 出问题了去哪

| 你现在卡在哪 | 先去哪里 |
|---|---|
| slash command 看不到 / 会话异常 | [05-遇到问题 / 04-CLI TUI 与会话问题](<../05-遇到问题/04-CLI TUI 与会话问题.md>) |
| `/tools`、skill command、MCP 相关不对 | [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-遇到问题/06-Tools Skills MCP 问题.md>) |
| messaging 平台里的 command 不工作 | [05-遇到问题 / 05-Gateway Messaging 与推送问题](<../05-遇到问题/05-Gateway Messaging 与推送问题.md>) |
| 配置改了但会话行为不一致 | [05-遇到问题 / 07-配置 Profiles 与环境隔离问题](<../05-遇到问题/07-配置 Profiles 与环境隔离问题.md>) |
| 不确定问题在哪 | [05-遇到问题 / 01-总览](../05-遇到问题/01-总览.md) |

## 9. 官方原文链接

- 官方 Slash Commands Reference：<https://hermes-agent.nousresearch.com/docs/reference/slash-commands>
- 官方 CLI Commands Reference：<https://hermes-agent.nousresearch.com/docs/reference/cli-commands>

如果你需要逐项核对所有 command 名称、平台差异与最新行为，以官方原文为准。

## 10. 相关中文站页面

- [06-reference / 01-总览](./01-总览.md)
- [02-CLI 命令参考](<./02-CLI 命令参考.md>)
- [01-从这开始 / 02-开始上手 / 03-常用斜杠命令与会话管理](../01-从这开始/02-开始上手/03-常用斜杠命令与会话管理.md)
- [05-遇到问题 / 04-CLI TUI 与会话问题](<../05-遇到问题/04-CLI TUI 与会话问题.md>)
- [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-遇到问题/06-Tools Skills MCP 问题.md>)

## ➡️ 下一步

完成后进入：

- [04-Profile 命令参考](<./04-Profile 命令参考.md>)

如果你想先回到上一阶段入口重新确认位置：

- [01-总览｜Reference 参考手册](./01-总览.md)
