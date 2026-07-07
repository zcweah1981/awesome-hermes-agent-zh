# 📦 10-把一整套 Agent 打包分享

这一页教你如何把一个完整的 Agent（含 SOUL、配置、技能、定时任务）打包成 Git 仓库，分享给别人一键安装。

![把一整套 Agent 打包分享：把本地 Profile 的 SOUL、配置、技能和定时任务脱敏后整理成 Distribution Git 仓库，再让别人通过 hermes profile install 一键安装](../../assets/rm2-5-profile-distribution-00-overview.webp)

> **一句话结论**：用 Profile Distribution 把你的 Agent 打包成一个 Git 仓库，别人一条命令就能装上、用起来。

**适合谁**：已经搭好一个完整 Agent，想把它分享给团队或社区的用户；或者想安装别人分享的 Agent 的用户。
**不适合谁**：连一个 Profile 都还没跑通、还不知道 SOUL.md 和 config.yaml 是什么的用户——先回 [02-开始上手](../../01-从这开始/02-开始上手/01-总览.md)。
**最短路径**：理解 Distribution 是什么 → 安装一个别人发的试试 → 照着模板把自己的 Agent 打包 → 推到 GitHub 分享。
**关键限制**：Distribution 不包含密钥和用户私有数据；安装后用户需要自己配 provider 凭据才能跑。
**下一步**：继续阅读下方 [这页做完以后，你应该得到什么](#-这页做完以后你应该得到什么) 章节。

> 📖 官方文档参考：[Profile Distributions](https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions)

---

## 🎯 这页做完以后，你应该得到什么

走完这一页，你需要拿到三件事：

1. **搞清楚 Profile 和 Profile Distribution 的区别**——知道"一个助手配置"和"一个可分发的助手包"不是同一件事
2. **能安装别人分享的 Agent**——拿到一个 Git 地址后，一条命令装好、跑起来
3. **能发布自己的 Agent**——把自己的完整 Agent 打包成标准 Distribution，推到 GitHub 让别人用

---

## 🧠 Profile 和 Profile Distribution 有什么区别

简单说：

- **Profile** 是你本地的 Agent 配置——它活在你机器上，包含 SOUL.md、config.yaml、技能、记忆等等
- **Profile Distribution** 是一个打包好的、可分享的 Agent 模板——它是一个 Git 仓库，别人装了之后会变成自己本地的 Profile

它们的关系就像：

| | Profile（本地配置） | Profile Distribution（分发包） |
|---|---|---|
| **是什么** | 你机器上一个具体的 Agent 实例 | 一个 Git 仓库，包含 Agent 的"图纸" |
| **在哪里** | 本地 `~/.hermes/profiles/` 下 | GitHub 或任意 Git 仓库 |
| **有没有用户数据** | 有（记忆、会话历史、状态） | 没有（只含模板文件，不含密钥和私有数据） |
| **能不能直接分享** | 不能（包含私有数据） | 能（就是为分享设计的） |
| **安装方式** | 自己手动建或 CLI 创建 | `hermes profile install <source>` 一键装 |

一句话：**Profile 是活的助手，Distribution 是助手的安装包。**

---

## 📋 distribution.yaml 长什么样

每个 Distribution 的根目录必须有一个 `distribution.yaml`，它是这个安装包的清单文件。

一个完整示例：

```yaml
name: my-daily-briefing
version: "1.2.0"
description: "一个每日新闻简报助手，自动搜索、筛选、生成晨间 briefing"
hermes_requires: ">=0.5.0"
author: "your-name"
license: "MIT"
env_requires:
  - BRAVE_API_KEY
distribution_owned:
  - SOUL.md
  - config.yaml
  - skills/
  - cron/
  - mcp.json
```

逐字段解释：

| 字段 | 作用 | 必填 |
|---|---|---|
| `name` | Distribution 的唯一标识名，安装后就是 Profile 名 | ✅ |
| `version` | 语义化版本号（semver），更新时靠它判断版本变化 | ✅ |
| `description` | 一句话描述这个 Agent 是干什么的 | ✅ |
| `hermes_requires` | 要求的 Hermes 最低版本，支持 semver 语法（如 `>=0.5.0`） | ❌ |

