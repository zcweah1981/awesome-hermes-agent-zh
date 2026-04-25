# 10-可选 Skills 目录

> 这页查的是 Hermes 官方 optional skills，也就是仓库里有、但默认不会自动激活的扩展技能。 如果你要查默认随 Hermes 提供的技能库，请看 [09-内置 Skills 目录](<./09-内置 Skills 目录.md>)。

## 1. 页面用途

这一页帮助你查 optional skills 的目录和使用边界。

它适合用来查：

- optional skills 是什么
- 它们和 bundled skills 有什么区别
- 官方建议如何安装 / 卸载
- 有哪些高频 category 值得先看
- 哪些 optional skills 更适合特定工作流，而不是新手默认就装

这页不负责：

- optional skill 安装失败排障
- 某个 skill 自己的完整教程
- MCP server 本身的配置教程

## 2. 官方来源

- 官方页面：<https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog>
- 官方页面标题：Optional Skills Catalog
- 官方页面定位：记录 Hermes 官方 optional skills 目录

中文站这一页会把 optional skills 按类别与适用场景整理，不机械照抄全量目录。

## 3. 什么时候查这页

下面这些场景，最适合先查这页：

- 你已经会用 Hermes，想按工作流扩展能力
- 你想判断某个 optional skill 值不值得装
- 你想区分 bundled 与 optional 的边界
- 你要接 MCP / migration / blockchain / health / docker 等专项能力

如果你还是刚入门，通常不建议从 optional skills 开始。

## 4. 核心概念中文解释

### 4.1 Optional Skills 是“仓库自带但默认不激活”的扩展技能

官方关键定义是：

- optional skills 放在：

```bash
optional-skills/
```

- 但默认不激活
- 需要你主动安装

所以它们不是“不存在”，而是“按需启用”。

### 4.2 官方安装方式

官方给出的安装命令模式是：

```bash
hermes skills install official/<category>/<skill>
```

例如：

```bash
hermes skills install official/blockchain/solana
hermes skills install official/mlops/flash-attention
```

卸载则是：

```bash
hermes skills uninstall <skill-name>
```

### 4.3 Optional 不等于“更高级所以一定更好”

中文站这里要特别收口：

optional skill 的本质是：

- 更专项
- 更工作流化
- 更依赖特定外部工具、API 或场景

它们适合“有明确任务需求的人”，不是所有人默认都该装。

### 4.4 一个 optional skill 往往自带额外依赖

官方目录里很多 optional skills 会依赖：

- 特定 CLI
- 特定 API key
- 外部服务
- MCP addon / socket / 本地应用

所以你在查 optional skills 时，要同时判断：

- 我有没有这个场景
- 我有没有这些依赖

## 5. 常用项速查

### 5.1 先记住的安装与目录规则

| 项目 | 你先记住什么 |
|---|---|
| optional skills 源路径 | `optional-skills/` |
| 官方安装格式 | `hermes skills install official/<category>/<skill>` |
| 卸载格式 | `hermes skills uninstall <skill-name>` |
| 是否默认激活 | 否 |

### 5.2 高价值 category 速查

> 说明：这里按“中文用户最容易理解的场景价值”整理，不是全量目录逐条复制。

#### A. autonomous-ai-agents

适合：

- 接更多 автономous agent
- 给 Hermes 增强记忆或代理协作能力

高频代表：

| Skill | 中文用途 |
|---|---|
| `blackbox` | 委托 Blackbox AI CLI 代理做编码任务 |
| `honcho` | 给 Hermes 增加 Honcho memory 能力 |

#### B. blockchain

适合：

- 查链上数据
- 看余额、交易、代币、网络状态

高频代表：

| Skill | 中文用途 |
|---|---|
| `base` | 查 Base 链数据 |
| `solana` | 查 Solana 链数据 |

#### C. creative

适合：

- 3D、SVG、实时视觉、meme 生成

高频代表：

| Skill | 中文用途 |
|---|---|
| `blender-mcp` | 通过 socket 控制 Blender |
| `concept-diagrams` | 生成轻量概念图 / SVG 图 |
| `meme-generation` | 生成 meme 图片 |
| `touchdesigner-mcp` | 控制 TouchDesigner |

#### D. devops

适合：

- Docker 管理
- inference.sh 大量 AI app 调用

高频代表：

| Skill | 中文用途 |
|---|---|
| `docker-management` | 管理容器、镜像、卷、网络、Compose |
| `inference-sh-cli` | 通过 infsh 调用大量 AI app |

#### E. communication / decision frameworks

例如：

- `one-three-one-rule`

适合做：

- 技术方案比较
- 迁移决策
- 架构选择

#### F. health / email / niche workflow 类

例如：

- `agentmail`
- `fitness-nutrition`
- `neuroskill-bci`

这类很强，但通常只在明确垂直场景里才值得装。

## 6. 完整参考结构

### 6.1 Optional Skills 的官方定位

官方把 optional skills 定义为：

included with the project, but must be installed manually.

中文可以直接理解成：

- 它在官方仓库体系里
- 但默认不进你的工作流
- 只有你明确需要时才装

### 6.2 安装、卸载与目录结构

#### 安装

```bash
hermes skills install official/<category>/<skill>
```

#### 卸载

```bash
hermes skills uninstall <skill-name>
```

#### 目录结构

官方给出的通用结构包括：

```bash
optional-skills/<category>/<skill-name>/
SKILL.md
references/
templates/
scripts/
```

这意味着 optional skill 往往不仅是一份文字说明，还可能附带：

- 参考资料
- 模板
- 脚本

### 6.3 哪些 optional skills 最值得先看

对于中文站用户，通常最值得先看的，不是“最花哨”的，而是“最能解决真实工作流问题”的：

#### 如果你在做代理协作

优先看：

- `blackbox`
- `honcho`

#### 如果你在做 DevOps / 基础设施

优先看：

- `docker-management`
- `inference-sh-cli`

#### 如果你在做图形 / 创意 / 演示

优先看：

- `concept-diagrams`
- `blender-mcp`
- `meme-generation`

#### 如果你在做链上查询

优先看：

- `base`
- `solana`

### 6.4 安装前你应该先问自己的 3 个问题

1. 我真的有这个明确场景吗？
2. 这个 skill 依赖的 CLI / key / 服务，我有没有？
3. 我现在要的是“查表了解”，还是“立刻投入生产工作流”？

如果这三个问题答不出来，就先别乱装。

## 7. 注意事项

### 7.1 Optional skill 不代表新手必须安装

很多新手一看到“可选技能目录”，就会想先装一堆。

但更合理的顺序是：

- 先把 Hermes 基础跑通
- 再根据场景扩能力

### 7.2 optional skill 往往更依赖外部世界

比 bundled skills 更常见的现实情况是：

- 要额外 CLI
- 要额外 API key
- 要额外本地软件或服务

所以它不是“点一下就自然可用”的同义词。

### 7.3 查目录和实际投产是两件事

Reference 页只帮你判断“有什么、适合谁、什么时候用”。

真正安装、启用、调通，往往还要结合该 skill 自己的文档与依赖环境。

## 8. 出问题了去哪

| 你现在卡在哪 | 先去哪里 |
|---|---|
| optional skill 安装失败 / 不生效 | [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-遇到问题/06-Tools Skills MCP 问题.md>) |
| MCP 类 skill 不工作 | [08-MCP 配置参考](<./08-MCP 配置参考.md>) |
| 不知道该不该装某个 optional skill | [01-从这开始 / 02-开始上手 / 04-常用 Skills（按日常使用场景精选）](<../01-从这开始/02-开始上手/04-常用 Skills（按日常使用场景精选）.md>) |
| 不确定问题在哪 | [05-遇到问题 / 01-总览](../05-遇到问题/01-总览.md) |

## 9. 官方原文链接

- 官方 Optional Skills Catalog：<https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog>

## 10. 相关中文站页面

- [06-reference / 01-总览](./01-总览.md)
- [09-内置 Skills 目录](<./09-内置 Skills 目录.md>)
- [08-MCP 配置参考](<./08-MCP 配置参考.md>)
- [01-从这开始 / 02-开始上手 / 04-常用 Skills（按日常使用场景精选）](<../01-从这开始/02-开始上手/04-常用 Skills（按日常使用场景精选）.md>)
- [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-遇到问题/06-Tools Skills MCP 问题.md>)

## ➡️ 下一步

完成后进入：

- [01-总览｜Reference 参考手册](./01-总览.md)

如果你想先回到上一阶段入口重新确认位置：

- [文档总览](../00-文档总览.md)
