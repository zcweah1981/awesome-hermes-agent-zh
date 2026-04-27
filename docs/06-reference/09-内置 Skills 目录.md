# 🧠 09-内置 Skills 目录

> 这页查的是 Hermes 官方 bundled skills，也就是默认随 Hermes 一起提供、安装后会复制到 `~/.hermes/skills/` 的技能库。 如果你要查按需安装的扩展技能，请看 [10-可选 Skills 目录](<./10-%E5%8F%AF%E9%80%89%20Skills%20%E7%9B%AE%E5%BD%95.md>)。

## 1. 页面用途

这一页帮助你用“目录脑图”理解 Hermes 的 bundled skills。

它适合用来查：

- bundled skills 是什么
- 它们安装后放在哪里
- 为什么 skills 不是“命令大全”
- 官方技能库大致分哪些类别
- 新手、内容用户、研究用户、开发用户分别该先看哪类 skills

这页不负责：

- 某个 skill 安装失败排障
- 某个 skill command 不显示排障
- optional skill 的完整目录

## 2. 官方来源

- 官方页面：<https://hermes-agent.nousresearch.com/docs/reference/skills-catalog>
- 官方页面标题：Bundled Skills Catalog
- 官方页面定位：Hermes 自带技能库目录

中文站这一页不会机械复制几百条 skill 目录，而是按用途重新分组，并挑高频项做中文索引。

## 3. 什么时候查这页

下面这些场景，最适合查这页：

- 你知道 Hermes 有 skills，但不知道官方自带了哪些方向
- 你想按用途快速找 skill，而不是按仓库目录硬翻
- 你想知道某个 skill 是 bundled 还是 optional
- 你想理解“skill 是能力包，不是单条命令”

## 4. 核心概念中文解释

### 4.1 Bundled Skills 是随 Hermes 一起提供的技能库

官方页面明确说：

Hermes 自带一大批 built-in skill library，安装后会复制到：

```text
~/.hermes/skills/
```

也就是说：

- 它们不是你每次都要单独从零找的第三方扩展
- 安装 Hermes 后，通常就已经具备这批官方技能的基础能力

### 4.2 Skills 不是“命令大全”

中文站这里要特别收口一个误区：

skill 本质上是能力包 / 工作流包，不是一个个零散命令按钮。

某些 skill 可能会暴露 slash command，但它本体更像：

- 一套任务方法
- 一组上下文约束
- 一种适合某类任务的工作流组织方式

### 4.3 Bundled 和 Optional 要分开看

官方 reference 实际把 skills 分成两层：

- bundled：默认自带、随项目提供
- optional：仓库里也有，但不是默认激活，需要你手动装

所以这页只负责 bundled skills。

## 5. 常用项速查

### 5.1 先记住的路径与边界

| 项目 | 你先记住什么 |
|---|---|
| bundled skills 安装后位置 | `~/.hermes/skills/` |
| 仓库内 bundled 源路径 | `skills/` |
| optional skills 源路径 | `optional-skills/` |
| optional skills 是否默认激活 | 否 |

### 5.2 按用途看 bundled skills

> 说明：下面是中文索引，不是官方全量目录逐字表。 完整目录与最新增减，以官方原文为准。

#### A. Hermes 自身帮助 / 自我使用

这类 skill 帮你理解、使用或扩展 Hermes 本身。

常见代表：

| Skill | 中文用途 |
|---|---|
| `hermes-agent` | 理解 Hermes 的 CLI、配置、gateway、skills、profiles、tools 等 |

#### B. Autonomous AI Agents / 编程代理协作

这类 skill 适合：

- 委托外部 coding agent
- 做并行实现
- 做 PR review / refactor / issue fixing

常见代表：

| Skill | 中文用途 |
|---|---|
| `claude-code` | 委托 Claude Code CLI 做编码任务 |
| `codex` | 委托 OpenAI Codex CLI 做编码任务 |
| `opencode` | 委托 OpenCode CLI 做实现或重构 |
| `hermes-agent` | 同时也是 Hermes 自身能力参考入口 |

#### C. Creative / 视觉与创意类

适合：

- ASCII art
- Excalidraw
- p5.js
- Manim
- 创意思路生成
- Web 设计参考

常见代表：

| Skill | 中文用途 |
|---|---|
| `ascii-art` | 生成 ASCII 艺术 |
| `excalidraw` | 生成手绘风格图 |
| `p5js` | 生成交互式创意视觉 |
| `manim-video` | 数学 / 技术动画 |
| `popular-web-designs` | 参考成熟 Web 设计体系 |

#### D. 数据 / 研究 / 内容 / 工作流类

常见方向包括：

- `jupyter-live-kernel`
- 各类研究 / 调研类 skill
- 工作流 / 计划类 skill
- 文档 / 写作 / 结构化输出类 skill

中文理解：

它们帮助 Hermes 进入“有方法的任务模式”，而不是裸聊模式。

#### E. DevOps / 系统 / 自动化类

例如：

- webhook subscriptions
- 部署与自动化相关 skill
- 系统巡检、服务管理、平台接入类 skill

#### F. Dogfood / QA / 内部质量类

例如：

- `dogfood`
- `adversarial-ux-test`

适合做：

- Web 应用探索式 QA
- 对产品做对抗性体验测试

## 6. 完整参考结构

### 6.1 Bundled Skills 的官方定位

官方把 bundled skills 视为：

跟随 Hermes 一起交付的内建技能库。

所以从用户角度，最重要的不是“它们在 repo 哪一行”，而是：

- 它们能帮我做什么
- 什么时候该调用这类 skill
- 它和普通对话有什么差别

### 6.2 按目录看的一般规律

官方目录里 bundled skills 分布在很多 category 下。 中文站建议你按“任务类型”看，而不是按目录名死记：

#### 开发 / 编程代理

适合：

- 写代码
- 重构
- PR review
- 长任务并行

#### 创意 / 图形 / 媒体

适合：

- 图形、视觉、动画、音频、创意生成

#### 研究 / 数据 / 笔记 / 工作流

适合：

- 文档化研究
- 数据分析
- 结构化计划
- 知识整理

#### DevOps / 平台 / 系统整合

适合：

- 平台接入
- 服务管理
- 系统自动化

### 6.3 新手如何看 bundled skills

如果你刚接触 Hermes，不建议先从“安装一堆 skill”开始。

更合理的顺序是：

1. 先理解 Hermes 基础使用
2. 再理解常用 slash commands
3. 再回来按任务类型选 skill

### 6.4 做方案 / 多代理 / 系统化工作时最常查的 bundled skills

如果你已经进入更高级使用层，最常查的通常是：

- autonomous-ai-agents 类
- workflow / planning 类
- devops / integration 类
- research / docs / media 类

## 7. 注意事项

### 7.1 不要把 skills 当作“另一套命令行总表”

skill 的本体是任务能力包，不是单独命令库。

### 7.2 bundled 不等于“每个场景都默认该用”

官方自带，只说明“可用”，不说明“你现在一定应该开”。

### 7.3 查目录和实际安装 / 启用是两件事

Reference 页帮你查“有哪些”，但具体是否启用、在哪个平台启用，还是要回 skills 管理或配置层。

## 8. 出问题了去哪

| 你现在卡在哪 | 先去哪里 |
|---|---|
| skill 不显示 / skill command 不出现 | [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/06-Tools%20Skills%20MCP%20%E9%97%AE%E9%A2%98.md>) |
| slash command 看起来不对 | [05-遇到问题 / 04-CLI TUI 与会话问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/04-CLI%20TUI%20%E4%B8%8E%E4%BC%9A%E8%AF%9D%E9%97%AE%E9%A2%98.md>) |
| 不知道该用哪个 skill | [01-从这开始 / 02-开始上手 / 04-常用 Skills（按日常使用场景精选）](<../01-%E4%BB%8E%E8%BF%99%E5%BC%80%E5%A7%8B/02-%E5%BC%80%E5%A7%8B%E4%B8%8A%E6%89%8B/04-%E5%B8%B8%E7%94%A8%20Skills%EF%BC%88%E6%8C%89%E6%97%A5%E5%B8%B8%E4%BD%BF%E7%94%A8%E5%9C%BA%E6%99%AF%E7%B2%BE%E9%80%89%EF%BC%89.md>) |
| 不确定问题在哪 | [05-遇到问题 / 01-总览](../05-遇到问题/01-总览.md) |

## 9. 官方原文链接

- 官方 Bundled Skills Catalog：<https://hermes-agent.nousresearch.com/docs/reference/skills-catalog>

## 10. 相关中文站页面

- [01-总览｜Reference 参考手册](./01-总览.md)
- [10-可选 Skills 目录](<./10-%E5%8F%AF%E9%80%89%20Skills%20%E7%9B%AE%E5%BD%95.md>)
- [01-从这开始 / 02-开始上手 / 04-常用 Skills（按日常使用场景精选）](<../01-%E4%BB%8E%E8%BF%99%E5%BC%80%E5%A7%8B/02-%E5%BC%80%E5%A7%8B%E4%B8%8A%E6%89%8B/04-%E5%B8%B8%E7%94%A8%20Skills%EF%BC%88%E6%8C%89%E6%97%A5%E5%B8%B8%E4%BD%BF%E7%94%A8%E5%9C%BA%E6%99%AF%E7%B2%BE%E9%80%89%EF%BC%89.md>)
- [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/06-Tools%20Skills%20MCP%20%E9%97%AE%E9%A2%98.md>)

## ➡️ 下一步

完成后进入：

- [10-可选 Skills 目录](<./10-%E5%8F%AF%E9%80%89%20Skills%20%E7%9B%AE%E5%BD%95.md>)

如果你想先回到上一阶段入口重新确认位置：

- [01-总览｜Reference 参考手册](./01-总览.md)
