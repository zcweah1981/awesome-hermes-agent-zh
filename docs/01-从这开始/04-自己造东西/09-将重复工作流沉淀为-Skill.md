
---
title: "将重复工作流沉淀为 Skill"
module: "从这开始"
section: "自己造东西"
slug: how-to-create-a-reusable-skill
description: "还在手动重复执行一套组合拳？本篇将带你通过一个“分析开源项目”的实战案例，学习如何将重复的工作流抽象、固化成一个可随时调用的 Hermes Skill，让你的 Agent 拥有可复用的新能力。"
order: 9
status: "published"
updated: "2026-07-05"
source_type: "original_tutorial"
---

![一名工程师正在一块巨大的数字白板前思考，白板上绘制着从混乱的手动步骤到一个结构化、可复用的 Skill 的演化流程图。](../../assets/practical-v2-04-custom-skills.webp)
*<center>将混沌化为秩序：把重复的手工操作，提炼为可一键调用的结构化能力。</center>*

## 🤷‍♂️ 适合谁

如果你发现自己经常让 Hermes 执行一套相似的、由多个步骤组成的任务（比如晨报整理、项目初始化、周报数据拉取），并且每次都需要重新输入几乎一样的指令，那么本篇教程就是为你准备的。

我们将教会你如何将这些重复劳动“沉淀”下来，打造成一个可复用的 **Skill**。

## 🎯 目标

掌握将一个重复性工作流（以“快速分析一个开源项目”为例）抽象并封装成一个 Hermes Skill 的完整过程。学习结束后，你将能够：

-   识别适合封装成 Skill 的工作流。
-   编写一个结构化的 `SKILL.md` 文件。
-   使用 `skill_manage` 工具在 Hermes 中创建和管理你的 Skill。
-   通过一个简单的指令调用你创造的 Skill，实现一键自动化。

## ⚙️ 案例：从手动分析一个开源项目开始

假设你的日常工作之一是快速了解一个新的开源项目。每次，你的操作都大同小异，就像这样：

> **你对 Hermes 说**：“帮我分析一下 `https://github.com/torvalds/linux` 这个项目。先 `clone` 下来，然后用 `pygount` 统计一下代码行数和语言分布，再用 `ls -R` 看看主要的目录结构，最后把 `README.md` 的内容给我，并总结一下这个项目是干什么的。”

这个过程涉及多个步骤，每次都要重复说一遍，很繁琐。这就是一个典型的、适合被沉淀为 Skill 的场景。

### ✍️ 手动流程拆解

我们把刚才那段话里的指令，一步步拆解成 Hermes 需要执行的原子操作：

1.  **克隆项目**：使用 `terminal` 工具执行 `git clone <repo_url>`。
2.  **分析代码**：使用 `terminal` 工具执行 `pygount --format=summary <repo_path>` 来统计代码信息。
3.  **查看结构**：使用 `terminal` 工具执行 `ls -R <repo_path> | head -n 30` 来预览目录结构。
4.  **阅读文档**：使用 `read_file` 工具读取 `<repo_path>/README.md`。
5.  **总结报告**：Agent 基于以上信息，给出一个综合报告。

这个流程清晰、固定，唯一的变量就是 `repo_url`。现在，让我们把它变成一个 Skill。

## 🛠️ 抽象步骤：创建 Skill 的配方

创建一个 Skill，就像是为 Agent 撰写一本可以反复查阅的“标准作业程序 (SOP) 手册”。这份手册就是 `SKILL.md` 文件。

### 1. 确定输入和输出

-   **输入 (Parameters)**：我们的流程需要什么变量？很明显，是项目的 Git URL。我们给它起个名字，叫 `repo_url`。
-   **输出 (Output)**：我们期望得到什么？一份关于项目的分析报告。

### 2. 编写 `SKILL.md` 骨架

每个 Skill 都是一个 `SKILL.md` 文件，它由两部分组成：

-   **Frontmatter (YAML)**: 定义 Skill 的元数据，比如名称、描述和最重要的——参数。
-   **Body (Markdown)**: 用自然语言描述执行步骤、最佳实践和注意事项。这里就是你给 Agent “上课”的地方。

现在，我们来创建 `codebase-analysis-basic.md` 文件内容。

```markdown
---
name: codebase-analysis-basic
description: "通过 clone、分析代码和阅读 README，对一个 Git 仓库进行快速的基础分析。"
parameters:
  - name: "repo_url"
    description: "需要分析的 Git 仓库的完整 URL (e.g., https://github.com/user/repo)"
    type: "string"
    required: true
---

# 📖 Workflow: Codebase Analysis (Basic)

## Goal
快速分析一个给定的 Git 仓库，并生成一份包含代码统计、文件结构和项目简介的摘要报告。

## Trigger
当用户要求“分析某个 repo”、“研究一下这个项目”或类似指令，并且提供了 Git URL 时，加载并遵循此 Skill。

## Steps
1.  **Clone the Repository**:
    -   从用户输入中提取 `repo_url`。
    -   使用 `terminal` 工具执行 `git clone {{repo_url}}`。
    -   **注意**: `git clone` 会在当前目录下创建一个与仓库同名的文件夹。记录下这个文件夹路径，后续步骤将在这个路径下执行。例如，从 `https://github.com/nousresearch/hermes-agent` 克隆后，路径是 `hermes-agent`。

2.  **Analyze Code Statistics**:
    -   在克隆下来的仓库目录内，使用 `terminal` 工具执行 `pygount --format=summary .`。
    -   `pygount` 会输出代码行数、注释行数和各种语言的分布。这是评估项目规模和技术栈的关键信息。

3.  **Inspect Directory Structure**:
    -   在仓库目录内，使用 `terminal` 工具执行 `ls -R | head -n 30`。
    -   这会展示项目顶层的主要文件和目录，帮助快速理解项目结构。

4.  **Read the README File**:
    -   使用 `read_file` 工具读取仓库根目录下的 `README.md` 文件。
    -   `README.md` 通常包含项目目标、如何安装和使用等核心信息。

5.  **Synthesize and Report**:
    -   **整合** 以上所有步骤收集到的信息：代码统计、目录结构、README 内容。
    -   **生成报告**: 以清晰的结构向用户汇报，至少包含：
        -   **项目简介**: 根据 README 总结。
        -   **技术栈和规模**: 根据 `pygount` 结果总结。
        -   **核心目录结构**: 根据 `ls` 结果总结。
    -   **清理**: 最后，询问用户是否需要删除本地的克隆仓库，以保持工作目录干净。

## ⚠️ Pitfalls
-   **仓库已存在**: `git clone` 如果发现目录已存在，会失败。在执行前，可以先检查目录是否存在。
-   **依赖缺失**: `pygount` 可能未安装。如果命令失败，应先尝试执行 `pip install pygount`。
-   **README 不存在**: 并非所有项目都有 `README.md`。如果 `read_file` 失败，应优雅地跳过该步骤并在报告中注明。

## 🔗 Related Concepts
-   **工具 (Tools)**: 这个 Skill 强依赖 `terminal` 和 `read_file` 工具。确保你已熟悉它们的基本用法。
-   **记忆 (Memory)**: 如果用户经常让你分析他们自己的项目，可以考虑使用 [**记忆系统**](../03-玩出花样/03-让-Hermes-记住你.md) 记住他们的常用仓库地址。
```

### 3. 将 Skill “安装”到 Hermes

现在我们有了 `SKILL.md` 的内容，该如何让 Hermes 学会它呢？使用 `skill_manage` 工具！

你只需要把刚才写好的 markdown 内容，通过 `skill_manage` 的 `create` 动作提交即可。

```python
# 伪代码，在与 Agent 对话时直接调用
skill_manage(
  action='create',
  name='codebase-analysis-basic',
  category='software-development', # 给 Skill 分个类，便于管理
  content="""
---
name: codebase-analysis-basic
description: "通过 clone、分析代码和阅读 README，对一个 Git 仓库进行快速的基础分析。"
parameters:
  - name: "repo_url"
    description: "需要分析的 Git 仓库的完整 URL (e.g., https://github.com/user/repo)"
    type: "string"
    required: true
---

# 📖 Workflow: Codebase Analysis (Basic)
... (此处省略与上面相同的 Markdown 内容) ...
"""
)
```

执行后，Hermes 会告诉你 Skill 已创建成功。从此，你的 Agent 就正式掌握了这个“新技能”。

## ✅ 验证：一键启动新技能

Skill 安装后，要如何使用呢？非常简单。

1.  **加载 Skill**: 虽然 Hermes 会在理解任务时自动尝试加载相关 Skill，但为了确保稳定复现，你可以显式加载它。
2.  **发出指令**: 像平常一样下达指令，但这次可以简单得多。

> **你对 Hermes 说**（加载并使用新技能）:
> “`load_skill('codebase-analysis-basic')`”
> 
> “好了，现在用这个技能帮我分析一下 `https://github.com/nousresearch/hermes-agent` 这个项目。”

Hermes 接收到指令后：
1.  它会识别到 `codebase-analysis-basic` 这个 Skill 与你的任务高度相关。
2.  它会阅读 `SKILL.md` 里的步骤，就像一个人类员工阅读 SOP 一样。
3.  它会严格按照 `Steps` 部分的指示，一步步执行 `git clone`, `pygount`, `ls -R`, `read_file`...
4.  最后，它会整合信息，并向你提交一份完整的报告。

整个过程不再需要你重复那些繁琐的细节，真正实现了一键启动。

## 🤯 常见误区与提示 (Pitfalls)

1.  **Skill 并非银弹**: Skill 适用于“流程固定”的重复任务。对于高度创新、没有固定模式的探索性任务，直接与 Agent 对话更有效。
2.  **参数是关键**: `parameters` 定义了 Skill 的“输入接口”。清晰的参数定义是保证 Skill 可复用性的核心。
3.  **在 Pitfalls 中记录失败经验**: 如果你在手动执行流程时遇到过坑（比如工具没装、网络超时），一定要把它们写进 `⚠️ Pitfalls` 部分。这等于是在为你的 Agent 注入“经验”，让它在未来能自主规避同样的问题。
4.  **从小处着手**: 不要试图一开始就创建一个无所不能的庞大 Skill。从一个简单、核心的流程开始，验证可行后，再逐步迭代扩展。

## 🚀 CTA (现在就动手!)

现在，轮到你了！

-   **思考一下**：在你与 Hermes 的日常互动中，有没有哪些是你经常重复的、由 2-3 个以上步骤组成的工作流？
-   **尝试一下**：选择其中一个，按照本文的“手动拆解 -> 抽象步骤 -> 编写 MD -> 安装 Skill”的流程，创建属于你自己的第一个 Skill！

将重复工作流沉淀为 Skill，是让你的 Agent 从一个“聊天工具”进化为“高效助理”的关键一步。

---
## 给下游的说明
- **文章路径**: `/opt/projects/awesome-hermes-agent-zh/docs/01-从这开始/04-自己造东西/09-将重复工作流沉淀为-Skill.md`
- **图片路径**: 文章引用的首图路径为 `../../assets/practical-v2-04-custom-skills.webp` (T1 任务产出)。请确保该图片存在于内容仓的 `assets/images` 目录下，并使用此相对路径。
- **引用旧文**:
    - `../03-玩出花样/03-让-Hermes-记住你.md`
- **去重说明**:
    - 本文是第一篇系统性介绍“如何创建 Skill”的实战教程，此前没有类似内容的文章。
    - 教程以一个全新的、具体的“代码分析”案例贯穿，而非泛泛地解释 Skill 的概念，避免了与未来可能出现的“Skill 概念总览”文章重复。
    - 关键概念（如 `tool`, `memory`）通过链接指向已有文章，避免了重复解释。
- **验收自查**:
    - [x] **标准文件**: 已阅读治理文件。
    - [x] **位置与命名**: 文章已按规范创建于 `docs/01-从这开始/04-自己造东西/09-将重复工作流沉淀为-Skill.md`。
    - [x] **贯穿案例**: 使用了“分析一个开源项目”作为案例。
    - [x] **结构与路标**: 包含了“适合谁”、“手动流程”、“抽象步骤”、“SKILL.md 示例”、“skill_manage 使用”、“验证方式”、“常见坑”，并使用了 emoji H2 标题。
    - [x] **示例**: 提供了完整的 `SKILL.md` 示例和使用 prompt 示例。
    - [x] **图片引用**: 已按要求引用图片，并提供了中文 alt 描述（体现在 markdown 的图片描述中，由前端渲染为 alt）。
    - [x] **链接旧文**: 已链接到关于 `Memory` 的文章。
    - [x] **Proof**: 本节已包含所有要求的 Proof 信息。
