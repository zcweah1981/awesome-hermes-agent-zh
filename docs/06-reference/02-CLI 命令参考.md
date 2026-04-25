# 02-CLI 命令参考

> 这页查的是你在终端 shell 里运行的 `hermes ...` 命令。 如果你要查聊天窗口里的 `/help`、`/tools`、`/model`，请看官方 [Slash Commands Reference](https://hermes-agent.nousresearch.com/docs/reference/slash-commands)；等中文页开放后，再从本模块进入。

## 1. 页面用途

这一页只做一件事：

帮你快速查 Hermes 的 CLI 命令，也就是你在终端里直接输入的 `hermes ...`。

它适合用来查：

- Hermes 的全局入口长什么样
- 常用 global options 是什么
- `hermes chat`、`hermes model`、`hermes setup`、`hermes gateway` 这些主命令分别干什么
- profile、config、tools、skills、mcp、sessions、dashboard 这些命令该在什么时候用
- 哪些命令只是查状态，哪些命令会真的改配置

这页不负责：

- slash commands 排查
- 命令报错排查
- provider / model 连接失败排查
- gateway 平台接入失败排查

如果你已经不是“查命令”，而是“命令不工作”，请直接跳到文末的“出问题了去哪”。

## 2. 官方来源

- 官方页面：<https://hermes-agent.nousresearch.com/docs/reference/cli-commands>
- 官方页面标题：CLI Commands Reference
- 官方页面定位：记录从 shell / terminal 里运行的 Hermes CLI 命令

中文站这一页遵循官方 Reference 的命令边界与分组思路，但会把过于专业的表述改成更容易扫读的中文说明。

## 3. 什么时候查这页

你遇到下面这些场景时，就该来这页：

- 你想确认 Hermes 的主入口命令怎么写
- 你知道要用 CLI，但记不清具体子命令
- 你想分清 `hermes model` 和 `/model` 的边界
- 你想查 profile、gateway、cron、logs、config、backup 这些命令的用途
- 你想知道某个命令是“交互式配置”，还是“脚本式调用”

如果你只是刚入门，还没建立 Hermes 使用心智，建议先看：

- [01-从这开始 / 02-开始上手 / 02-认识 Hermes 的基本使用方式](<../01-从这开始/02-开始上手/02-认识 Hermes 的基本使用方式.md>)
- [01-从这开始 / 02-开始上手 / 03-常用斜杠命令与会话管理](../01-从这开始/02-开始上手/03-常用斜杠命令与会话管理.md)

## 4. 核心概念中文解释

### 4.1 CLI 命令和 Slash Commands 不是一回事

先记住最重要的一条：

- CLI 命令：你在终端里输入 `hermes ...`
- Slash Commands：你已经进入 Hermes 对话后，在会话里输入 `/...`

例如：

```bash
hermes model
hermes chat --continue
hermes gateway status
```

这些都属于 CLI 命令。

而下面这些：

```text
/model
/tools
/help
/new
```

属于会话中的 slash commands，不属于这页。

### 4.2 Hermes 的 CLI 总入口长这样

官方的总入口格式是：

```bash
hermes [global-options] <command> [subcommand/options]
```

可以把它理解成三层：

- `hermes`：主入口
- `global-options`：这次调用的全局选项
- `command` / `subcommand`：你要执行的具体能力

### 4.3 Global options 是“这一次怎么运行”

global options 决定的是“这次运行方式”，不是某个子命令自己的内部参数。

例如：

- 这次用哪个 profile：`--profile`
- 这次恢复哪个会话：`--resume` / `--continue`
- 这次是不是要开 worktree：`--worktree`
- 这次是否跳过审批：`--yolo`
- 这次是否忽略本地 config：`--ignore-user-config`

### 4.4 Top-level commands 是“你到底要做什么”

当你写：

```bash
hermes chat
hermes model
hermes setup
hermes gateway status
```

真正决定你在干什么的，是 `chat`、`model`、`setup`、`gateway` 这些主命令。

所以阅读 CLI Reference 时，最好的方式不是死背全量命令，而是先分清命令族：

- 聊天与会话
- 模型与鉴权
- 配置与维护
- 网关与自动化
- 工具与技能
- 数据、日志与备份
- profile 与环境隔离

## 5. 常用项速查

### 5.1 最常查的入口命令

| 命令 | 中文说明 | 什么时候用 |
|---|---|---|
| `hermes` | 默认进入交互式聊天 | 直接开始用 Hermes |
| `hermes chat -q "..."` | 单次非交互提问 | 脚本、一次性调用、快速验证 |
| `hermes chat --continue` | 继续最近会话 | 接上次工作 |
| `hermes chat --resume <id>` | 恢复指定会话 | 明确知道要回哪条 session |
| `hermes model` | 交互式设置 provider 与 model | 新增 provider、填 API Key、切默认模型 |
| `hermes setup` | 进入总配置向导 | 第一次配置或集中补配置 |
| `hermes doctor` | 诊断配置和依赖问题 | 不知道哪里坏了时先查 |
| `hermes status` | 看当前状态 | 快速看模型、认证、平台状态 |
| `hermes config` | 查看 / 编辑配置 | 想改 `config.yaml` 时 |
| `hermes gateway` | 运行或管理消息网关 | Telegram / Discord / Slack / WhatsApp 等 |

### 5.2 最常用的 global options

| Option | 中文说明 | 使用场景 |
|---|---|---|
| `--version`, `-V` | 显示版本并退出 | 确认版本 |
| `--profile <name>`, `-p <name>` | 本次调用指定 profile | 临时切换环境 |
| `--resume <session>`, `-r <session>` | 恢复指定历史会话 | 精确恢复 |
| `--continue [name]`, `-c [name]` | 恢复最近会话或最近同标题会话 | 日常继续工作 |
| `--worktree`, `-w` | 在隔离 git worktree 中启动 | 并行 coding / agent 任务 |
| `--yolo` | 跳过危险命令审批提示 | 你明确知道自己在做什么时 |
| `--ignore-user-config` | 忽略 `~/.hermes/config.yaml` | 排查配置污染 |
| `--ignore-rules` | 跳过 AGENTS / SOUL / memory 等规则注入 | 做纯净对照测试 |
| `--tui` | 启动 TUI 界面 | 想直接进入 TUI |

### 5.3 最容易混淆的一组命令

| 你看到的命令 | 真正作用 | 不要混淆成什么 |
|---|---|---|
| `hermes model` | 在终端里做 provider / model 的完整配置 | 不是会话内 `/model` |
| `/model` | 在已进入的会话里切换已配置好的模型 | 不是新增 provider 的入口 |
| `hermes setup` | 总配置向导 | 不是聊天入口 |
| `hermes doctor` | 排查环境 / 配置问题 | 不是修改模型的入口 |
| `hermes gateway run` | 前台运行 gateway | 不是 systemd 服务安装命令 |
| `hermes gateway install` | 安装系统服务 | 不是立刻进入配对流程 |

## 6. 完整参考结构

### 6.1 Global entrypoint

官方总格式：

```bash
hermes [global-options] <command> [subcommand/options]
```

如果你不知道某个命令该放哪，先回到这个格式理解：

- 先决定这次 Hermes 要做什么：`chat` / `model` / `gateway` / `config` / `profile` ...
- 再决定是否要加本次全局行为：`--profile` / `--resume` / `--worktree`
- 最后再填各自子命令和参数

### 6.2 聊天与模型相关命令

#### `hermes chat`

```bash
hermes chat [options]
```

常用参数：

| 参数 | 中文说明 |
|---|---|
| `-q, --query "..."` | 单次非交互 prompt |
| `-m, --model <model>` | 本次运行临时指定模型 |
| `-t, --toolsets <csv>` | 本次运行指定 toolsets |
| `--provider <provider>` | 强制指定 provider |
| `-s, --skills <name>` | 预载入一个或多个 skills |
| `-v, --verbose` | 显示更详细输出 |
| `-Q, --quiet` | 程序化模式，减少 banner / spinner |
| `--image <path>` | 单次调用附带本地图片 |
| `--resume <session>` / `--continue [name]` | 直接从 chat 命令恢复会话 |
| `--worktree` | 为这次运行创建隔离 worktree |
| `--checkpoints` | 打开文件系统 checkpoints |

中文站补充理解：

- 想“马上开始聊天”，用 `hermes` 或 `hermes chat`
- 想“一次问完就退出”，用 `hermes chat -q`
- 想“接着上次干”，优先记住 `--continue`
- 想“这次先限制工具权限”，看 `--toolsets`

#### `hermes model`

这是终端里的完整 provider + model 配置入口。

它适合：

- 新增 provider
- 跑 OAuth 登录
- 填 API Key
- 选默认模型
- 配自定义 endpoint

最重要的边界：

- `hermes model`：终端里做完整配置
- `/model`：会话里切换已经配置好的模型

如果你要“新增 provider”，不要在会话里折腾 `/model`，直接退出会话后运行：

```bash
hermes model
```

### 6.3 配置、状态与维护命令

#### `hermes setup`

```bash
hermes setup [model|tts|terminal|gateway|tools|agent] [--non-interactive] [--reset]
```

适合第一次配置，或者你知道自己只想补某个配置块时使用。

#### `hermes config`

```bash
hermes config <subcommand>
```

常见子命令：

| 子命令 | 中文说明 |
|---|---|
| `show` | 显示当前配置 |
| `edit` | 打开 `config.yaml` |
| `set <key> <value>` | 设置一个配置值 |
| `path` | 打印 config 路径 |
| `env-path` | 打印 `.env` 路径 |
| `check` | 检查是否缺配置或配置过时 |
| `migrate` | 交互式补齐新引入配置 |

#### `hermes status`

```bash
hermes status [--all] [--deep]
```

适合快速看：

- 当前模型 / provider
- 认证状态
- 平台状态
- 是否要做更深的检查

#### `hermes doctor`

```bash
hermes doctor [--fix]
```

适合：

- 不知道哪里坏了
- 更新后状态怪异
- 想先做一次系统性体检

#### 维护相关命令

| 命令 | 中文说明 |
|---|---|
| `hermes version` | 输出版本信息 |
| `hermes update` | 更新 Hermes |
| `hermes uninstall [--full] [--yes]` | 卸载 Hermes |

### 6.4 Gateway、自动化与平台相关命令

#### `hermes gateway`

```bash
hermes gateway <subcommand>
```

常见子命令：

| 子命令 | 中文说明 |
|---|---|
| `run` | 前台运行 gateway |
| `start` | 启动后台服务 |
| `stop` | 停止服务 |
| `restart` | 重启服务 |
| `status` | 查看服务状态 |
| `install` | 安装成系统服务 |
| `uninstall` | 卸载系统服务 |
| `setup` | 交互式消息平台设置 |

官方特别提醒：

- WSL 用户优先用 `hermes gateway run`
- 不要默认把 `start` 当成 WSL 的标准方案

#### 其他自动化 / 平台命令

| 命令 | 中文说明 |
|---|---|
| `hermes whatsapp` | WhatsApp 配对 / 设置流程 |
| `hermes cron <...>` | 定时任务管理 |
| `hermes webhook <...>` | 动态 webhook 订阅管理 |
| `hermes pairing <...>` | 审批或撤销消息平台 pairing code |

### 6.5 数据、日志、备份与调试命令

| 命令 | 中文说明 | 典型用途 |
|---|---|---|
| `hermes dump` | 输出可分享的环境摘要 | 找人协助排查时给对方上下文 |
| `hermes debug share` | 上传或本地打印调试报告 | 快速支持排障 |
| `hermes logs` | 查看 / tail / 过滤日志 | 看 agent、errors、gateway 日志 |
| `hermes backup` | 备份 Hermes home | 升级前做快照 |
| `hermes import` | 从 zip 恢复备份 | 迁移或回滚配置 |
| `hermes sessions` | 管理会话 | 浏览、导出、删除、重命名 session |
| `hermes insights` | 分析最近一段时间的使用情况 | 做复盘或观察来源 |

### 6.6 工具、技能、MCP 与扩展命令

| 命令 | 中文说明 | 你通常什么时候会查 |
|---|---|---|
| `hermes tools` | 配置各平台可用工具 | 想限制 / 开启工具时 |
| `hermes skills` | 浏览、安装、更新、管理 skills | 想装 skill 或查 skill 来源时 |
| `hermes mcp` | 管理 MCP server 配置 | 想加、测、配 MCP server 时 |
| `hermes plugins` | 管理插件 | 想启用 / 禁用插件时 |
| `hermes memory` | 管理外部 memory provider | 想接 Honcho / mem0 等 |
| `hermes honcho` | 管理 Honcho 相关配置 | 使用 Honcho 记忆时 |
| `hermes acp` | 作为 ACP server 启动 Hermes | 编辑器集成时 |

### 6.7 Profile、环境隔离与迁移命令

| 命令 | 中文说明 |
|---|---|
| `hermes profile <subcommand>` | 管理多 profile 隔离环境 |
| `hermes claw migrate [options]` | 从 OpenClaw 迁移到 Hermes |
| `hermes dashboard [options]` | 启动 Web Dashboard |
| `hermes completion [bash|zsh]` | 输出 shell 自动补全脚本 |

其中 `hermes profile` 常见子命令包括：

- `list`
- `use <name>`
- `create <name>`
- `delete <name>`
- `show <name>`
- `alias <name>`
- `rename <old> <new>`
- `export <name>`
- `import <archive>`

## 7. 注意事项

### 7.1 不要把 CLI Commands 和 Slash Commands 混成一页脑内模型

这是新手最容易乱的地方：

- `hermes model` 是终端命令
- `/model` 是会话命令
- `hermes tools` 是终端命令
- `/tools` 是会话命令

它们有关联，但不是一个入口。

### 7.2 不是每个命令都适合“先背下来”

先记最常用的一层就够：

- `hermes`
- `hermes chat --continue`
- `hermes model`
- `hermes setup`
- `hermes doctor`
- `hermes gateway status`
- `hermes profile`

剩下的查表即可，不需要一上来全记住。

### 7.3 `hermes auth` 已经替代旧的 `hermes login / logout`

官方现在已明确提示：

- `hermes login` 已移除 / 废弃
- 认证管理优先看 `hermes auth`
- provider 和 model 的交互式设置入口优先看 `hermes model`

### 7.4 这页是“查命令”，不是“查为什么失败”

比如：

- 你想知道 `hermes gateway install` 是什么，这页能解决
- 你想知道为什么 gateway 装了但 Telegram 不通，这页不解决

后者请直接去故障页。

## 8. 出问题了去哪

如果你已经进入“命令会跑，但结果不对 / 命令根本不工作”的阶段，直接按这里跳：

| 你现在卡在哪 | 先去哪里 |
|---|---|
| 安装、更新、环境异常 | [05-遇到问题 / 02-安装更新与环境问题](../05-遇到问题/02-安装更新与环境问题.md) |
| `hermes model`、provider、endpoint 报错 | [05-遇到问题 / 03-模型 Provider 与自定义 endpoint 问题](<../05-遇到问题/03-模型 Provider 与自定义 endpoint 问题.md>) |
| slash command、CLI、会话异常 | [05-遇到问题 / 04-CLI TUI 与会话问题](<../05-遇到问题/04-CLI TUI 与会话问题.md>) |
| gateway / messaging 不通 | [05-遇到问题 / 05-Gateway Messaging 与推送问题](<../05-遇到问题/05-Gateway Messaging 与推送问题.md>) |
| tools / skills / MCP 不生效 | [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-遇到问题/06-Tools Skills MCP 问题.md>) |
| profile / config / 环境隔离混乱 | [05-遇到问题 / 07-配置 Profiles 与环境隔离问题](<../05-遇到问题/07-配置 Profiles 与环境隔离问题.md>) |
| 不确定问题在哪 | [05-遇到问题 / 01-总览](../05-遇到问题/01-总览.md) |

## 9. 官方原文链接

- 官方 CLI Commands Reference：<https://hermes-agent.nousresearch.com/docs/reference/cli-commands>
- 官方 Slash Commands Reference：<https://hermes-agent.nousresearch.com/docs/reference/slash-commands>

如果你需要逐项核对完整参数、完整子命令或最新变更，以官方原文为准。

## 10. 相关中文站页面

- [06-reference / 01-总览](./01-总览.md)
- [01-从这开始 / 02-开始上手 / 02-认识 Hermes 的基本使用方式](<../01-从这开始/02-开始上手/02-认识 Hermes 的基本使用方式.md>)
- [01-从这开始 / 02-开始上手 / 03-常用斜杠命令与会话管理](../01-从这开始/02-开始上手/03-常用斜杠命令与会话管理.md)
- [05-遇到问题 / 04-CLI TUI 与会话问题](<../05-遇到问题/04-CLI TUI 与会话问题.md>)
- [05-遇到问题 / 07-配置 Profiles 与环境隔离问题](<../05-遇到问题/07-配置 Profiles 与环境隔离问题.md>)

## ➡️ 下一步

完成后进入：

- [03-Slash Commands 参考（待中文页开放前先看官方原文）](https://hermes-agent.nousresearch.com/docs/reference/slash-commands)

如果你想先回到上一阶段入口重新确认位置：

- [01-总览｜Reference 参考手册](./01-总览.md)
