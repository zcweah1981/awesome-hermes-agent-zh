# Hermes Agent 中文站内容版本说明

本页记录公开内容仓中已经提交的主要内容变化，帮助读者判断最近更新了什么、对应哪一份
Git 提交，以及应该从哪个在线入口继续阅读。

这里记录的是 **中文内容版本**，不是 Nous Research / Hermes Agent 上游软件的官方
Release Notes。内容仓提交也不等于独立站已经部署；在线状态应以
[Hermes Agent 中文站](https://hermes-zh.com) 当前页面为准。

## 2026-07-29：核心 Hub 与上下文导航完善

- 完成“从这开始、现成方案、国内落地、遇到问题”等模块的上下文内链校正，让读者能从
  具体教程返回上级 Hub，并继续进入相关步骤。
- 公开仓库首页补充中文站首页和 5 个核心 Hub 的正式 canonical 入口。
- 代表性内容提交：
  [`1c27afb`](https://github.com/zcweah1981/awesome-hermes-agent-zh/commit/1c27afb1f9e086df8d0ca511fa1fd73116eeab31)
- README 入口提交：
  [`fc9ac33`](https://github.com/zcweah1981/awesome-hermes-agent-zh/commit/fc9ac3360257dcc73a6e11472f5938bde287bfe0)

在线入口：
[从这开始](https://hermes-zh.com/docs/start) ·
[现成方案](https://hermes-zh.com/docs/solutions) ·
[国内落地](https://hermes-zh.com/docs/china) ·
[OpenClaw 迁移](https://hermes-zh.com/docs/openclaw) ·
[遇到问题](https://hermes-zh.com/docs/issues)

## 2026-07-28：第一批搜索意图内容校正

围绕真实查询意图校正了 5 个重点页面的标题、摘要、正文结构、来源说明和下一步路径，
同时保留仍有效的安装与配置事实：

- [阿里云百炼 Token Plan](https://hermes-zh.com/docs/china/models/alibaba-bailian-token-plan)
- [腾讯云 Token Plan](https://hermes-zh.com/docs/china/models/tencent-token-plan)
- [小红书内容助手](https://hermes-zh.com/docs/solutions/xiaohongshu)
- [Home Assistant 智能家居](https://hermes-zh.com/docs/start/practical/home-assistant)
- [Provider 与自定义 endpoint 排障](https://hermes-zh.com/docs/issues/provider-endpoint)

对应内容提交：
[`53a65ed`](https://github.com/zcweah1981/awesome-hermes-agent-zh/commit/53a65ed46c89e05012298b7ad7cc82a848f3f8fe)

## 2026-07-22：对齐 Hermes Agent v0.19.0 Quicksilver

- 安装命令切换到当前官方安装入口。
- 增加 `hermes setup --portal`、会话导出、订阅管理等 v0.19.0 相关说明。
- 新增独立的
  [v0.19.0 Quicksilver 更新指南](https://hermes-zh.com/docs/reference/v019-quicksilver)。
- 更新 Built-in Tools、CLI、Slash Commands 和消息平台覆盖说明。

对应内容提交：
[`4eac166`](https://github.com/zcweah1981/awesome-hermes-agent-zh/commit/4eac1666634380abeef4b3710467f60f94ea0b5f)

## 如何判断你看到的是哪个版本

1. 本仓库的完整提交 SHA 是内容版本的唯一标识。
2. 独立站从固定内容 SHA 构建，不会在构建时隐式读取内容仓 `main` 的最新状态。
3. 只有站点完成内容锁同步并部署后，对应变化才会出现在在线页面。
4. 页面事实若受上游、模型厂商或云服务变化影响，仍应以页面标注的官方来源和复核时间为准。

