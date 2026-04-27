# 04-Profile 命令参考

> 这页查的是 `hermes profile ...` 这一组命令，用来管理不同的 Hermes profile。 如果你要查一般 CLI 命令，请看 [02-CLI 命令参考](<./02-CLI%20%E5%91%BD%E4%BB%A4%E5%8F%82%E8%80%83.md>)。

## 1. 页面用途

这一页只负责帮你查 profile 相关命令。

它适合用来查：

- profile 怎么列出、切换、创建、删除
- `--clone`、`--clone-all`、`--clone-from` 是什么意思
- profile 的 alias、rename、export、import 怎么理解
- profile 管的是“隔离使用环境”，不是普通聊天标签
- 为什么 profile 的 Hermes home 路径和 terminal 工作目录不是一回事

这页不负责：

- profile 不生效排障
- 导入导出失败排障
- profile 下模型或 tools 异常排障

如果你现在的问题是“为什么我切了 profile 还是不对”，请直接去文末的“出问题了去哪”。

## 2. 官方来源

- 官方页面：<https://hermes-agent.nousresearch.com/docs/reference/profile-commands>
- 官方页面标题：Profile Commands Reference
- 官方页面定位：记录所有 `hermes profile` CLI 子命令

中文站这一页保留官方命令结构，但会把“profile 到底隔离了什么”“clone 到底复制到什么程度”讲清楚。

## 3. 什么时候查这页

下面这些场景，最适合来这页：

- 你想把工作和个人使用环境分开
- 你想给不同项目、不同客户、不同机器人建独立环境
- 你想备份或分享某个 profile
- 你想知道 `create --clone` 和 `create --clone-all` 的区别
- 你想确认 profile 的 home 目录、alias、导入导出逻辑

如果你只是刚建立多环境意识，建议结合这几页一起看：

- [02-CLI 命令参考](<./02-CLI%20%E5%91%BD%E4%BB%A4%E5%8F%82%E8%80%83.md>)
- [05-遇到问题 / 07-配置 Profiles 与环境隔离问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/07-%E9%85%8D%E7%BD%AE%20Profiles%20%E4%B8%8E%E7%8E%AF%E5%A2%83%E9%9A%94%E7%A6%BB%E9%97%AE%E9%A2%98.md>)

## 4. 核心概念中文解释

### 4.1 Profile 可以理解成“一套独立使用环境”

在中文语境里，最容易理解的说法是：

Profile 不是“聊天标签”，而是一整套隔离开的 Hermes 使用环境。

不同 profile 可以有不同的：

- config
- `.env`
- skills
- sessions
- state
- 默认模型与平台配置

所以它更像“独立工作空间入口”，而不是简单的分类标签。

### 4.2 `hermes profile` 是一组 CLI 子命令

官方总入口是：

```bash
hermes profile
hermes profile <subcommand>
```

最常见的子命令包括：

- `list`
- `use`
- `create`
- `delete`
- `show`
- `alias`
- `rename`
- `export`
- `import`

### 4.3 active profile 和 terminal 工作目录不是一回事

这个区别非常重要。

官方明确说明：

- profile 决定的是 Hermes home、配置、技能、会话等隔离环境
- 它不是自动决定 terminal 当前工作目录

如果你想指定 profile 默认进入哪个项目目录，应该看该 profile 的：

```yaml
terminal.cwd
```

### 4.4 `--clone` 和 `--clone-all` 差很多

可以简单记成：

- `--clone`：复制基础配置层
- `--clone-all`：复制整个状态层

也就是说：

- `--clone` 更适合“复制一个配置模板”
- `--clone-all` 更适合“把当前环境整体克隆一份”

## 5. 常用项速查

### 5.1 最常用的 profile 子命令

| Subcommand | 中文说明 | 什么时候用 |
|---|---|---|
| `list` | 列出所有 profiles | 看当前有哪些环境 |
| `use <name>` | 设为默认 active profile | 切换主环境 |
| `create <name>` | 创建新 profile | 新建一个隔离环境 |
| `delete <name>` | 删除 profile | 清理不用的环境 |
| `show <name>` | 查看 profile 详情 | 检查路径、模型、状态 |
| `alias <name>` | 生成或更新 wrapper alias | 想快速启动某 profile |
| `rename <old> <new>` | 重命名 profile | 调整命名 |
| `export <name>` | 导出为 tar.gz | 备份 / 迁移 / 分享 |
| `import <archive>` | 导入 profile 压缩包 | 恢复或迁移环境 |

### 5.2 最常用的 create 选项

| 选项 | 中文说明 | 典型用途 |
|---|---|---|
| `--clone` | 复制当前 profile 的 `config.yaml`、`.env`、`SOUL.md` | 快速复制配置模板 |
| `--clone-all` | 复制当前 profile 的所有状态 | 完整克隆一套环境 |
| `--clone-from <profile>` | 从指定 profile 克隆 | 不想从当前激活 profile 克隆 |
| `--no-alias` | 不生成 wrapper script | 不需要快速入口脚本 |

### 5.3 最容易混淆的一组点

| 你看到的概念 | 实际含义 | 不要误解成什么 |
|---|---|---|
| active profile | 默认使用的 Hermes 环境 | 不是当前 shell 目录 |
| `show` 里的 path | Hermes home 路径 | 不是 terminal cwd |
| `--clone` | 复制基础配置层 | 不是完整复制一切 |
| `--clone-all` | 复制所有状态 | 不是“只复制模型配置” |
| `alias` | 生成 wrapper 启动入口 | 不是 profile 本身 |

## 6. 完整参考结构

### 6.1 总入口

官方入口：

```bash
hermes profile <subcommand>
```

当你不知道该用哪一个子命令时，可以先按“你要做什么”来分：

- 想看现状：`list` / `show`
- 想切换环境：`use`
- 想新建环境：`create`
- 想清理环境：`delete`
- 想搬运环境：`export` / `import`
- 想优化入口：`alias`

### 6.2 `hermes profile list`

```bash
hermes profile list
```

作用：列出所有 profiles。

官方细节：

- 当前 active profile 会带 `*`
- 没有额外 options

示意理解：

```bash
default
* work
dev
personal
```

### 6.3 `hermes profile use`

```bash
hermes profile use <name>
```

作用：把 `<name>` 设为默认 active profile。

重点：

- 之后不带 `-p` 的 Hermes 命令默认走这个 profile
- 想回基础环境，用 `default`

示例：

```bash
hermes profile use work
hermes profile use default
```

### 6.4 `hermes profile create`

```bash
hermes profile create <name> [options]
```

常见参数与选项：

| Argument / Option | 中文说明 |
|---|---|
| `<name>` | 新 profile 名称 |
| `--clone` | 复制 `config.yaml`、`.env`、`SOUL.md` |
| `--clone-all` | 复制完整状态 |
| `--clone-from <profile>` | 指定克隆来源 |
| `--no-alias` | 不生成 alias wrapper |

几个高频模式：

```bash
hermes profile create work
hermes profile create client-a --clone
hermes profile create backup --clone-all
hermes profile create work2 --clone --clone-from work
```

官方特别提醒：

创建 profile 并不会自动修改终端默认工作目录。 如果你希望某个 profile 启动时进入固定项目路径，要配置：

```yaml
terminal.cwd
```

### 6.5 `hermes profile delete`

```bash
hermes profile delete <name> [--yes|-y]
```

作用：删除 profile，并移除对应 shell alias。

重点警告：

- 这是永久删除整个 profile 目录
- 不能删除当前 active profile

### 6.6 `hermes profile show`

```bash
hermes profile show <name>
```

作用：查看 profile 详情，例如：

- Hermes home 路径
- configured model
- gateway 状态
- skills 数量
- `.env` 是否存在
- `SOUL.md` 是否存在
- alias 是否存在

这页最重要的理解点是：

- 这里显示的是 profile 的 Hermes home
- 不是 terminal 当前工作目录

### 6.7 `hermes profile alias`

```bash
hermes profile alias <name> [options]
```

作用：生成或更新 shell wrapper script，默认位置类似：

```bash
~/.local/bin/<name>
```

常见选项：

| 选项 | 中文说明 |
|---|---|
| `--remove` | 删除 wrapper script |
| `--name <alias>` | 自定义 alias 名称 |

示例：

```bash
hermes profile alias work
hermes profile alias work --name mywork
hermes profile alias work --remove
```

### 6.8 `rename`、`export`、`import`

#### `rename`

```bash
hermes profile rename <old> <new>
```

用于重命名 profile。

#### `export`

```bash
hermes profile export <name> [-o FILE]
```

用于导出 profile 为 `.tar.gz`。

适合：

- 做备份
- 迁移机器
- 分享团队模板

#### `import`

```bash
hermes profile import <archive> [--name NAME]
```

用于从压缩包恢复一个 profile。

适合：

- 恢复历史备份
- 导入别人给你的 profile 模板
- 迁移旧环境

## 7. 注意事项

### 7.1 不要把 profile 当聊天标签用

profile 的变化会影响的不只是会话名，而是整套环境。

所以不要把它理解成：

- 主题标签
- 对话分类夹
- 项目名字备注

### 7.2 导出前要注意 secrets

官方允许导出 profile，但中文站这里要特别提醒：

- 导出前先确认有没有敏感信息
- 分享给别人时不要把真实 token 和 key 裸传
- `.env` 里的 secrets 要按分享场景判断是否保留

### 7.3 `show` 看到的 path 不是 cwd

这是最容易误解、也最容易导致“我以为没切成功”的原因。

profile 管的是 Hermes home，不是 shell 当前目录。

### 7.4 这页是“查 profile 命令”，不是“查为什么 profile 行为异常”

如果你现在是：

- profile 切了但模型没变
- import 后 tools 不一致
- 不同 profile 间配置串了

那已经是排障场景。

## 8. 出问题了去哪

| 你现在卡在哪 | 先去哪里 |
|---|---|
| profile / config / 环境隔离混乱 | [05-遇到问题 / 07-配置 Profiles 与环境隔离问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/07-%E9%85%8D%E7%BD%AE%20Profiles%20%E4%B8%8E%E7%8E%AF%E5%A2%83%E9%9A%94%E7%A6%BB%E9%97%AE%E9%A2%98.md>) |
| profile 下模型 / endpoint 不对 | [05-遇到问题 / 03-模型 Provider 与自定义 endpoint 问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/03-%E6%A8%A1%E5%9E%8B%20Provider%20%E4%B8%8E%E8%87%AA%E5%AE%9A%E4%B9%89%20endpoint%20%E9%97%AE%E9%A2%98.md>) |
| tools / skills 在不同 profile 下表现不一致 | [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/06-Tools%20Skills%20MCP%20%E9%97%AE%E9%A2%98.md>) |
| 不确定问题在哪 | [05-遇到问题 / 01-总览](../05-遇到问题/01-总览.md) |

## 9. 官方原文链接

- 官方 Profile Commands Reference：<https://hermes-agent.nousresearch.com/docs/reference/profile-commands>
- 官方 CLI Commands Reference：<https://hermes-agent.nousresearch.com/docs/reference/cli-commands>

如果你需要核对完整参数、边界条件或导入导出行为，以官方原文为准。

## 10. 相关中文站页面

- [01-总览｜Reference 参考手册](./01-总览.md)
- [02-CLI 命令参考](<./02-CLI%20%E5%91%BD%E4%BB%A4%E5%8F%82%E8%80%83.md>)
- [05-遇到问题 / 07-配置 Profiles 与环境隔离问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/07-%E9%85%8D%E7%BD%AE%20Profiles%20%E4%B8%8E%E7%8E%AF%E5%A2%83%E9%9A%94%E7%A6%BB%E9%97%AE%E9%A2%98.md>)
- [04-从OpenClaw过来 / 05-从 OpenClaw 到 Hermes：迁移路径](<../04-%E4%BB%8EOpenClaw%E8%BF%87%E6%9D%A5/05-%E4%BB%8E%20OpenClaw%20%E5%88%B0%20Hermes%EF%BC%9A%E8%BF%81%E7%A7%BB%E8%B7%AF%E5%BE%84.md>)
- [04-从OpenClaw过来 / 06-OpenClaw 用户常见问题与检查清单](<../04-%E4%BB%8EOpenClaw%E8%BF%87%E6%9D%A5/06-OpenClaw%20%E7%94%A8%E6%88%B7%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E4%B8%8E%E6%A3%80%E6%9F%A5%E6%B8%85%E5%8D%95.md>)

## ➡️ 下一步

完成后进入：

- [05-环境变量参考](<./05-环境变量参考.md>)

如果你想先回到上一阶段入口重新确认位置：

- [01-总览｜Reference 参考手册](./01-总览.md)
