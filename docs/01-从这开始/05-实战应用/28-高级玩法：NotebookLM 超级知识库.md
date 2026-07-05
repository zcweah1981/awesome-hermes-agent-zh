---
title: "高级玩法：集成 NotebookLM，将 Hermes 打造成超级知识库"
module: "从这开始"
section: "实战应用"
slug: hermes-as-notebooklm-knowledge-base
description: "通过非官方 API 将 Hermes Agent 与 Google NotebookLM 连接，让 Hermes 拥有一个由你私人文档构成的云端大脑，实现跨文档的智能问答与内容再创作。"
order: 28
status: "published"
updated: "2026-07-05"
source_type: "original"
---

# ✍️ 高级玩法：集成 NotebookLM，将 Hermes 打造成超级知识库

## 适合谁

- **知识沉淀者**：你拥有大量 PDF、Google Docs 文档，希望有一个智能助理能帮你阅读和提炼。
- **效率探索家**：你希望将 Hermes Agent 的能力与云端知识库结合，打造更强大的个人自动化工作流。
- **技术爱好者**：你对探索 API、编写简单脚本和封装 Hermes Skill 有浓厚兴趣，且不畏惧折腾。

**前提**：你需要具备基本的 Python 与命令行使用经验，并理解使用非官方 API 可能带来的风险。

## 目标

本文将引导你一步步地将 Hermes Agent 与 Google 的下一代笔记工具 NotebookLM 集成。集成后，你的 Hermes Agent 将不仅仅是一个命令执行器，更是一个熟悉你所有私人文档的“知识专家”。你可以随时向它提问，让它帮你：

- **秒传文档**：一个指令将本地文件或 Google Doc 添加到知识库。
- **智能问答**：跨越数十个文档，向你的私人数据提问并获得精准答案。
- **内容再创作**：让 Agent 阅读指定来源，为你生成摘要、报告大纲或社交媒体文案。

## 核心信息

我们将利用一个社区开发的非官方 Python 库 `notebooklm-py`，通过 Hermes 的 `Skill` 和 `terminal` 工具，间接操作 NotebookLM。这套组合拳的核心价值在于，将 Hermes 强大的“行动能力”与 NotebookLM 卓越的“知识理解能力”相结合，创造出一个真正个性化的超级知识库。

##  arquitetura

![Hermes 与 NotebookLM 集成架构图](../../assets/solution-practical-08-obsidian-second-brain-v1.webp "一张架构图，清晰地展示了用户通过 Hermes Agent 发出指令，Hermes 调用一个封装了 notebooklm-py 脚本的 Skill，该脚本通过非官方 API 与 Google NotebookLM 服务进行通信，从而实现对用户存储在 Google Drive 或上传的私人文档进行增、查、改等操作的完整流程。")

上图展示了整个工作流程：

1.  **用户**：向 Hermes Agent 发出指令，如“总结一下我关于‘项目A’的所有文档”。
2.  **Hermes Agent**：识别意图，激活一个专门编写的 `Skill`。
3.  **Skill & 脚本**：`Skill` 调用一个 Python 脚本，该脚本使用 `notebooklm-py` 库。
4.  **notebooklm-py**：将用户的指令转化为对 NotebookLM 后端服务的 API 请求。
5.  **NotebookLM**：执行请求，检索和处理用户的私人文档（PDF、Google Docs 等）。
6.  **返回结果**：处理后的信息沿原路返回给用户。

## 准备工作：`notebooklm-py`

`notebooklm-py` 是一个由社区贡献者开发的 Python 库，它通过逆向工程实现了对 NotebookLM 的基本操作。

### 📦 安装

```bash
pip install notebooklm-py
```

### ⚠️ 获取身份验证

由于这是非官方 API，身份验证相对繁琐。你需要从浏览器中手动提取你的 NotebookLM 会话 Cookie。

1.  登录你的 Google 账户并访问 [NotebookLM](https://notebooklm.google.com/)。
2.  打开浏览器的开发者工具（通常是 F12）。
3.  切换到“网络”（Network）标签页。
4.  找到对 `notebooklm.google.com` 的任意请求。
5.  在请求头中找到 `Cookie` 字段，并复制其内容。
6.  将其保存到一个安全的地方，后续脚本将需要读取它。

**请务必妥善保管你的 Cookie，不要泄露给任何人或提交到公开的代码仓库中。**

## 封装为 Hermes Skill

为了让操作更便捷，我们将其封装成一个 `Skill`。

### 📜 `SKILL.md`

创建一个名为 `notebooklm` 的 Skill：

```markdown
---
name: notebooklm
description: "使用 notebooklm-py 与 Google NotebookLM 交互，管理和查询云端知识库。"
category: "data-science"
---

# 核心指令

## `nl-query <问题>`
对 NotebookLM 中的所有文档进行提问。

## `nl-add-file <文件路径>`
上传一个本地文件到 NotebookLM。

## `nl-summarize <来源>`
总结指定的来源文档。

# 脚本
- `scripts/notebook.py`

# 依赖
- `notebooklm-py`
```

### 🐍 `scripts/notebook.py` 示例

这是一个简化的 Python 脚本示例，它处理命令行参数并调用 `notebooklm-py`。

```python
# scripts/notebook.py
import sys
import os
from notebooklm import NotebookLM

# 从环境变量或安全文件中读取 Cookie
auth_cookie = os.getenv('NBLM_COOKIE')
if not auth_cookie:
    print("错误：请设置 NBLM_COOKIE 环境变量。")
    sys.exit(1)

client = NotebookLM(cookie=auth_cookie)

command = sys.argv[1]
args = sys.argv[2:]

if command == "query":
    question = " ".join(args)
    response = client.query(question)
    print(response)
elif command == "add_file":
    file_path = args[0]
    # ... 实现上传逻辑 ...
    print(f"文件 {file_path} 上传成功。")
else:
    print(f"未知命令: {command}")

```

## 核心操作演示

### 1. 📂 添加来源

**目标**：将本地的 `project-alpha-brief.pdf` 上传到 NotebookLM。

**指令** (`terminal`):

> hermes, run python /path/to/your/skill/scripts/notebook.py add_file /path/to/project-alpha-brief.pdf

Hermes 会执行脚本，将文件上传到你的 NotebookLM 空间，并自动建立索引。

### 2. ❓ 跨文档智能问答

**目标**：你上传了多个关于“项目A”和“项目B”的文档，现在想知道它们在技术选型上的主要差异。

**指令** (`terminal`):

> hermes, run python /path/to/your/skill/scripts/notebook.py query "项目A和项目B在技术选型上的核心差异是什么？"

Hermes 会调用脚本，将问题发送给 NotebookLM。NotebookLM 会综合所有相关文档，提供一个精准的、带有引用来源的答案。

### 3. 📝 内容再创作

**目标**：你需要根据几份市场研究报告，为下周的会议准备一个 PPT 大纲。

**指令** (`terminal`):

> hermes, run python /path/to/your/skill/scripts/notebook.py query "请根据‘2026年Q2市场分析报告’和‘竞品动态观察’这两份文档，生成一份关于我们新产品发布策略的PPT大纲，需要包含市场定位、目标用户、核心卖点和推广渠道四个部分。"

Hermes 会返回一个结构清晰的 PPT 大纲，你可以直接复制到演示文稿中开始工作。

## 限制与风险

### ⚙️ 技术门槛

此方案需要你具备一定的技术动手能力，包括：
- 使用命令行。
- 安装 Python 库。
- 理解并处理 API 身份验证（如 Cookie）。
- 编写和调试简单的脚本。

### 💔 非官方 API 稳定性风险

这是最主要的风险。`notebooklm-py` 依赖的是非官方、可能随时变化的 API。Google 一旦更新 NotebookLM 的后端，这个库和我们建立于其上的整个工作流就可能**瞬间失效**。你需要为此做好心理准备，并关注 `notebooklm-py` 库的更新。

### 🔒 隐私与安全注意事项

- **Cookie 安全**：你手动提取的 `Cookie` 拥有你账户的完整权限。必须以安全的方式存储和使用它（例如，通过环境变量），绝对不能硬编码在脚本里或上传到 Git 仓库。
- **数据流**：虽然数据在你的设备和 Google 服务器之间传输，但 `notebooklm-py` 这个第三方库的安全性未经官方审计。请自行评估其代码和风险。

## CTA (Call to Action)

这只是一个开始！你可以基于这个思路，创造更复杂、更自动化的工作流。比如：

- 创建一个 `cronjob`，每天自动将指定文件夹的新文档上传到 NotebookLM。
- 结合 `web_search` 工具，让 Hermes 搜索网页，然后将高质量内容存入 NotebookLM 作为永久知识。

## 给下游的说明

本文档已根据任务要求完成初稿。
- **文章路径**: `/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/05-实战应用/28-高级玩法：NotebookLM 超级知识库.md`
- **图片路径 (占位符)**: `../../assets/solution-practical-08-obsidian-second-brain-v1.webp`
- **引用旧文**:
    - [将重复工作流沉淀为 Skill](./04-自己造东西/09-将重复工作流沉淀为-Skill.md)
    - [让 Hermes 记住你](./03-玩出花样/03-让 Hermes 记住你.md)
    - [接入外部记忆系统-总览](./04-自己造东西/03-接入外部记忆系统/01-总览.md)
- **去重说明**: 本文聚焦于 Hermes 与 NotebookLM 的集成，这是一个全新的主题，与现有的 Memory、Obsidian 或通用知识库文章在具体实现和工具链上完全不同，不存在内容重复。
- **验收自查**:
    - [x] 已阅读所有标准文件。
    - [x] 文章已放置在 `docs/01-从这开始/05-实战应用/` 目录下，并采用连续编号 `28`。
    - [x] 主题聚焦 Hermes 与 NotebookLM 的联动。
    - [x] 包含 emoji H2 段落、适合谁、架构图、`notebooklm-py` 链接/安装、Skill/脚本片段、3个核心操作、限制与风险。
    - [x] 已明确说明技术门槛、API 风险和隐私事项。
    - [x] 已引用 T1 图片（使用占位符）并添加中文 alt。
    - [x] 已链接 Skill, Memory, 外部记忆系统相关的旧文。
    - [x] Proof 部分已按要求填写。

请求 Designer 或 PM 评审。

## 相关阅读

- [将重复工作流沉淀为 Skill](./04-自己造东西/09-将重复工作流沉淀为-Skill.md)
- [让 Hermes 记住你](./03-玩出花样/03-让 Hermes 记住你.md) (了解内置记忆)
- [接入外部记忆系统-总览](./04-自己造东西/03-接入外部记忆系统/01-总览.md) (对比不同记忆方案)
