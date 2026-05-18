# 📦 Packs 方案包总览

这一层放的不是文档正文，也不是源码工程本体。

这里放的是：
- 可直接下载的方案包
- 可解压后安装进 Hermes profile 的工作流包
- 面向具体任务的 solo / team 运行包
- 文档页对应的可执行落地层

如果你已经在 `docs/02-现成方案/` 里找到某个方案，下一步通常就会进入这里。

## ✨ 这一层是干什么的

你可以把 `packs/` 理解成“文档里方案页的可执行落地层”。

文档页负责告诉你：
- 这个方案适合谁
- 解决什么问题
- 该怎么选 solo 还是 team

`packs/` 负责给你：
- 可下载 zip
- 安装说明
- profile 安装脚本
- SOUL / skills / sample input-output
- 真正可试跑的最小包

## 🧭 你什么时候该进这一层

当你已经完成下面任一件事时，就应该从 docs 进入 `packs/`：

- 你已经确定要试跑某个现成方案
- 你不想自己从零拼 workflow，想直接下载包
- 你已经知道自己要用 solo 版还是 team 版
- 你要把方案安装进自己的 Hermes profile

## ⚡ 默认使用顺序

进入任何一个 pack，默认都按这个顺序走：

1. 先看该包根目录的 `INSTALL.md`
2. 再判断你要进：
   - `01-super-individual`
   - 还是 `02-team`
3. 再执行安装脚本
4. 再用 sample input 试跑第一轮

## 📚 当前已开放的方案包

| 方案包 | 对应文档页 | 适合什么任务 | 当前可用模式 | 默认入口 |
|---|---|---|---|---|
| [miniapp-lab](./miniapp-lab/INSTALL.md) | [微信小程序助手](../docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md) | 微信小程序需求梳理、产品到开发接力 | Solo + Team | [miniapp-lab/INSTALL.md](./miniapp-lab/INSTALL.md) |
| [webdev-lab](./webdev-lab/INSTALL.md) | [敏捷 Web 开发助手](<../docs/02-现成方案/03-应用开发与快速原型/03-敏捷 Web 开发助手.md>) | Web 应用骨架、页面、接口和开发接力 | Solo + Team | [webdev-lab/INSTALL.md](./webdev-lab/INSTALL.md) |
| [meeting-lab](./meeting-lab/INSTALL.md) | [会议纪要助手](../docs/02-现成方案/02-办公效率与知识整理/02-会议纪要助手.md) | 会议纪要整理与结构化输出 | Solo | [meeting-lab/INSTALL.md](./meeting-lab/INSTALL.md) |
| [daily-report-lab](./daily-report-lab/INSTALL.md) | [项目日报助手](../docs/02-现成方案/02-办公效率与知识整理/03-项目日报助手.md) | 项目日报整理、汇总、跟进输出 | Solo | [daily-report-lab/INSTALL.md](./daily-report-lab/INSTALL.md) |
| [summary-lab](./summary-lab/INSTALL.md) | [资料总结助手](../docs/02-现成方案/02-办公效率与知识整理/04-资料总结助手.md) | 散资料压缩、结构化总结、发送版总结输出 | Solo | [summary-lab/INSTALL.md](./summary-lab/INSTALL.md) |
| [xhs-lab](./xhs-lab/INSTALL.md) | [小红书内容助手](../docs/02-现成方案/01-内容创作与发布/02-小红书内容助手.md) | 小红书选题、标题、正文、配图提示、发布检查 | Solo + Team | [xhs-lab/INSTALL.md](./xhs-lab/INSTALL.md) |
| [wechat-writer-lab](./wechat-writer-lab/INSTALL.md) | [公众号写作助手](../docs/02-现成方案/01-内容创作与发布/03-公众号写作助手.md) | 公众号文章选题、初稿、编辑、审校 | Solo + Team | [wechat-writer-lab/INSTALL.md](./wechat-writer-lab/INSTALL.md) |
|| [ppt-lab](./ppt-lab/INSTALL.md) | [PPT 助手](<../docs/02-现成方案/01-内容创作与发布/04-PPT 助手.md>) | PPT 内容生成、分工写稿与评审 | Solo + Team | [ppt-lab/INSTALL.md](./ppt-lab/INSTALL.md) |
|| [multi-platform-rewrite-lab](./multi-platform-rewrite-lab/INSTALL.md) | [多平台内容改写助手](../docs/02-现成方案/01-内容创作与发布/06-多平台内容改写助手.md) | 一篇内容改写成小红书、公众号、X 多平台版本 | Solo | [multi-platform-rewrite-lab/INSTALL.md](./multi-platform-rewrite-lab/INSTALL.md) |
|| [action-plan-lab](./action-plan-lab/INSTALL.md) | [行动计划助手](../docs/02-现成方案/02-办公效率与知识整理/05-行动计划助手.md) | 会议结论/目标拆成可执行行动计划表 | Solo | [action-plan-lab/INSTALL.md](./action-plan-lab/INSTALL.md) |
|| [message-summary-lab](./message-summary-lab/INSTALL.md) | [邮件群消息摘要助手](../docs/02-现成方案/02-办公效率与知识整理/06-邮件群消息摘要助手.md) | 邮件/群消息压成可转发结构化摘要 | Solo | [message-summary-lab/INSTALL.md](./message-summary-lab/INSTALL.md) |

## 🗂️ 按方案类型快速分组

### 内容创作与发布
- [xhs-lab](./xhs-lab/INSTALL.md) → 小红书内容助手
- [wechat-writer-lab](./wechat-writer-lab/INSTALL.md) → 公众号写作助手
- [ppt-lab](./ppt-lab/INSTALL.md) → PPT 助手
- [multi-platform-rewrite-lab](./multi-platform-rewrite-lab/INSTALL.md) → 多平台内容改写助手

### 办公效率与知识整理
- [meeting-lab](./meeting-lab/INSTALL.md) → 会议纪要助手
- [daily-report-lab](./daily-report-lab/INSTALL.md) → 项目日报助手
- [summary-lab](./summary-lab/INSTALL.md) → 资料总结助手
- [action-plan-lab](./action-plan-lab/INSTALL.md) → 行动计划助手
- [message-summary-lab](./message-summary-lab/INSTALL.md) → 邮件群消息摘要助手

### 应用开发与快速原型
- [miniapp-lab](./miniapp-lab/INSTALL.md) → 微信小程序助手
- [webdev-lab](./webdev-lab/INSTALL.md) → 敏捷 Web 开发助手

## 🔍 每个包里通常会有什么

一个标准 pack 一般包含这些层：

### 1. 根入口
- `INSTALL.md`
- `.zip` 下载包

### 2. Solo 模式
- `01-super-individual/`
- 适合你想先自己快速跑通一轮

### 3. Team 模式
- `02-team/`
- 适合你想按多角色接力跑完整工作流
- 并不是每个包都会提供 team 版

### 4. 角色与能力资产
- `SOUL.md`
- `skills/`
- `templates/`
- `references/`
- `examples/`

### 5. 安装动作
- `install_to_profile.sh`
- 或 `install_all.sh`

## ✅ 你怎么快速判断该选哪个包

### 如果你要做应用 / 原型 / 小程序类任务
直接进：
- [miniapp-lab](./miniapp-lab/INSTALL.md)
- [webdev-lab](./webdev-lab/INSTALL.md)

### 如果你要做会议整理
直接进：
- [meeting-lab](./meeting-lab/INSTALL.md)

### 如果你要做项目日报 / 日报类整理
直接进：
- [daily-report-lab](./daily-report-lab/INSTALL.md)

### 如果你要做资料整理 / 总结类输出
直接进：
- [summary-lab](./summary-lab/INSTALL.md)

### 如果你要做内容发布
直接进：
- [xhs-lab](./xhs-lab/INSTALL.md)
- [wechat-writer-lab](./wechat-writer-lab/INSTALL.md)
- [ppt-lab](./ppt-lab/INSTALL.md)
- [multi-platform-rewrite-lab](./multi-platform-rewrite-lab/INSTALL.md)

### 如果你要做行动计划 / 任务拆解
直接进：
- [action-plan-lab](./action-plan-lab/INSTALL.md)

### 如果你要做邮件 / 群消息摘要
直接进：
- [message-summary-lab](./message-summary-lab/INSTALL.md)

## 🧠 Solo 和 Team 怎么选

### 先选 Solo，如果你现在只是想：
- 先跑通一次
- 先看输出长什么样
- 先验证这个方案适不适合自己

### 选 Team，如果你现在已经明确要：
- 多角色接力
- 把任务拆给 product / writer / builder / api / qa / validator
- 跑完整流程，而不是只试一个单点输出

### 当前只提供 Solo 的包
- `meeting-lab`
- `daily-report-lab`
- `summary-lab`
- `action-plan-lab`
- `message-summary-lab`
- `multi-platform-rewrite-lab`

### 当前同时提供 Solo + Team 的包
- `miniapp-lab`
- `webdev-lab`
- `xhs-lab`
- `wechat-writer-lab`
- `ppt-lab`

## 🔗 如果你想先回文档再决定

先回这些 docs 页会更稳：
- [02-现成方案总览](../docs/02-现成方案/01-总览.md)
- [内容创作与发布](../docs/02-现成方案/01-内容创作与发布/01-总览.md)
- [办公效率与知识整理](../docs/02-现成方案/02-办公效率与知识整理/01-总览.md)
- [应用开发与快速原型](../docs/02-现成方案/03-应用开发与快速原型/01-总览.md)

## 🚫 这一层不负责什么

`packs/` 不负责：
- 解释方案为什么成立
- 详细讲解 Hermes 基础概念
- 替代 docs 正文教程

这些内容请回到：
- [01-从这开始](../docs/01-从这开始/总览.md)
- [02-现成方案](../docs/02-现成方案/01-总览.md)
- [06-reference](../docs/06-reference/01-总览.md)

## 🚀 如果你现在就想开始

默认建议：

1. 先看 [02-现成方案](../docs/02-现成方案/01-总览.md)
2. 确认你要试的方案页
3. 再回到对应 pack：
   - [miniapp-lab](./miniapp-lab/INSTALL.md)
   - [webdev-lab](./webdev-lab/INSTALL.md)
   - [meeting-lab](./meeting-lab/INSTALL.md)
   - [daily-report-lab](./daily-report-lab/INSTALL.md)
   - [summary-lab](./summary-lab/INSTALL.md)
   - [xhs-lab](./xhs-lab/INSTALL.md)
   - [wechat-writer-lab](./wechat-writer-lab/INSTALL.md)
   - [ppt-lab](./ppt-lab/INSTALL.md)
   - [multi-platform-rewrite-lab](./multi-platform-rewrite-lab/INSTALL.md)
   - [action-plan-lab](./action-plan-lab/INSTALL.md)
   - [message-summary-lab](./message-summary-lab/INSTALL.md)

如果你已经明确要先试一个，默认最适合快速起跑的是：
- [miniapp-lab/INSTALL.md](./miniapp-lab/INSTALL.md)

## 📌 看完这页你应该能马上判断什么

看完这一页，你应该已经能立刻判断：
- `packs/` 是方案包目录，不是 docs 正文目录
- 当前一共开放了哪些可直接下载和安装的方案包
- 我该先进哪个 pack
- 我应该先选 solo 还是 team
- 我下一步应该先看哪个 `INSTALL.md`
