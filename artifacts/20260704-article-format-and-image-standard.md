# Hermes 中文站文章格式与配图标准

> 用途：作为下一轮内容生产派单的前置约束。所有新文章必须先符合本标准，再进入验收。

## 1. 文章定位

- 优先写“真实应用场景”，不要写大而全的功能说明书。
- 每篇只解决一个明确问题：读者是谁、正在卡什么、看完能做成什么。
- 标题要直给：`实战：...`、`教程：...`、`...助手`、`...接入`，避免空泛概念标题。
- 正文默认中文，语气要像经验丰富的朋友带路：先给结论，再解释原因，再给步骤。
- 不把 Hermes 描述成万能工具；必须说明适合谁、不适合谁、前提条件和失败排查入口。

## 2. 文件位置与命名

- 新增实际应用文章优先放在 `docs/01-从这开始/05-实战应用/` 或对应的现有栏目下。
- 如果是“现成方案 / 助手 Pack”，放在 `docs/02-现成方案/...` 对应分类下。
- 如果是国内入口/云厂商/模型供应商，放在 `docs/03-国内落地/...`。
- 文件名使用中文标题，保留现有编号风格，例如：`23-实战：服务器自动化运维.md`。
- 同一目录内编号必须连续，不抢占已有编号。
- 图片资源优先放在 `docs/assets/`；如果属于某个国内落地子目录的操作截图，可放在该目录下的 `assets/`。

## 3. Frontmatter 规则

- 当前多数 `docs/**/*.md` 没有 frontmatter，只有少数第三方聚合页使用 frontmatter。
- 新写普通教程/实战文章默认不要加 frontmatter，保持现有主体风格。
- 只有继续维护 `docs/03-国内落地/01-国内部署/04-07` 这类第三方聚合页时，才沿用：
  - `title`
  - `module`
  - `section`
  - `slug`
  - `description`
  - `order`
  - `status`
  - `updated`
  - `source_type`

## 4. 标准文章结构

推荐结构：

1. `# 标题`
2. 一句话速答 / 一句话先说清楚
3. 首图或主结构图
4. `## 👀 适合谁` 或 `## ✨ 这条路适合谁`
5. `## 📌 先记住核心判断` / `## 🎯 为什么值得做`
6. `## 🧭 最短路线` 或 `## 🚦先选哪一种`
7. 真实用例或场景拆解
8. 分步骤操作，每一步都包含：
   - 现在做什么
   - 为什么做
   - 看到什么算成功
   - 如果没成功先查什么
9. 输出物 / 产出物说明
10. 常见坑 / 排查路径
11. 下一步建议与相关链接

不是每篇都必须完全一致，但每篇至少要有：

- 一句话结论
- 适合谁 / 不适合谁
- 前提条件
- 最短路径
- 可复制命令或 Prompt
- 成功判定
- 排错入口
- 下一步

## 5. 标题、层级与 emoji 段落标识

- H1 只出现一次。
- H2 用来分主段落，H3 用来分步骤或模式。
- 新文章必须使用 emoji 区分关键段落，保证中文用户快速扫读时能立刻识别段落功能。
- emoji 不是装饰，而是阅读路标；每个 H2 优先使用一个稳定含义的 emoji。
- 延续现有风格，优先使用：`👀` 适合谁、`🎯` 目标/为什么、`🧭` 最短路线、`🚦` 选择判断、`📦` 产出物、`⚡` 快速上手、`✅` 验收/成功标准、`🧩` 结构拆解、`🖼️` 配图/截图、`🛠️` 操作步骤、`⚠️` 常见坑、`🔗` 相关链接。
- 同一篇文章内 emoji 语义要一致，不要为了花哨频繁更换。
- 每个主段落开头先给一句“这一节解决什么”，再展开细节，避免中文读者在长文中迷路。
- 表格用于选择、对比、产出清单；不要用长表格堆砌百科信息。
- 代码块必须标注语言：`bash`、`yaml`、`dotenv`、`markdown`、`text`。

## 6. 链接规则

- 站内链接使用相对路径。
- 中文文件名中的空格在链接中使用 `%20`，沿用现有写法。
- 相关内容不要重复讲，应该链接到已有权威页。
- 涉及密钥、Token、Secret 时，只写变量名和占位值，不给真实值。

## 7. 配图总原则

- 每篇新文章至少 1 张主图；重点实战文章建议 2-3 张图。
- 图不是装饰品，必须承担解释任务：路径图、结构图、对比图、流程图、真实截图证据。
- 首图应放在开头速答之后，用来让读者一眼理解文章主线。
- 结构图、流程图、对比图必须使用生图模型生成，不允许用 SVG/HTML/CSS/Mermaid 自己手绘后导出。
- 所有图片必须是 `.webp`，不新增 `.png`、`.jpg`、`.jpeg`、`.svg`。
- 图片文件名使用英文小写短横线，带主题和版本号，例如：
  - `actual-dev-workflow-mainline-v1.webp`
  - `server-devops-alert-flow-v1.webp`
  - `agent-philosophy-healthy-silence-v1.webp`
- 图片 alt 文本必须是中文长描述，说明图里表达的关系，不要只写“截图”或“流程图”。

## 7.1 结构图/流程图视觉风格

基于现有站内图（如 `practical-v2-*`、`solution-*`、`rm2-*`）抽样分析，后续结构图和流程图统一采用以下风格：

- **画幅**：优先 16:9 横图，推荐 1600×900 或 1376×768；复杂大图可用 2752×1536。
- **背景**：深蓝黑或近黑背景，带细微科技网格、电路纹理或数字蓝图质感；背景不能抢正文信息。
- **主色**：冷色科技蓝 / 青色作为主强调色，用于节点边框、连线、箭头、图标。
- **辅助色**：少量橙色/琥珀色用于关键触发、告警或最终交付；少量绿色用于成功、通过、健康状态。
- **节点**：圆角矩形卡片，深色填充，青色发光边框，轻微玻璃拟态或科技 UI 质感。
- **连线**：发光青色线条，圆角转折，清晰箭头；复杂流程允许分叉和汇聚，但不能缠绕。
- **布局**：优先模块化、留白充分；流程图强调“从左到右 / 从上到下”的方向；对比图用左右两栏；中心协作图用 hub-and-spoke。
- **字体**：现代无衬线中文字体风格，白色/浅灰文字，标题略粗；图片内文字必须短，避免整段说明。
- **图标**：使用简单线性图标或抽象 UI 图标，颜色与主色一致；不要使用复杂插画人物抢焦点。
- **可读性**：中文标签要大、短、清楚；一张图只表达一个核心关系。

生图提示词必须明确包含：

```text
16:9 futuristic tech diagram, dark blue-black background, subtle glowing grid or circuit pattern, rounded rectangular UI cards, glowing cyan borders, clean sans-serif Chinese typography, white and light gray text, cyan flow lines with rounded corners and arrowheads, small orange highlight for key trigger or alert, small green dots for success status, professional high-tech documentation style, minimalist, readable, no SVG, no hand-drawn style
```

负面约束：

```text
no cartoon characters, no messy arrows, no tiny unreadable text, no colorful gradient poster, no random icons, no 3D mascot, no photorealistic people, no decorative-only image, no SVG line art export look
```

## 8. 配图类型标准

### 8.1 主结构图 / 路径图

适合文章开头。

要求：
- 16:9 横图优先。
- 展示完整闭环，而不是孤立模块。
- 文案短，节点少，读者 5 秒内能看懂。
- 适合 P0 实战文章。

示例风格：
- `rm2-2-get-running-index-06-stage-map-closed.webp`
- `solution-practical-03-github-backup-cron-v1.webp`
- `practical-v2-05-github-pr-review.webp`

### 8.2 对比图

适合解释选择。

要求：
- 左右两栏或三栏对比。
- 每栏只放关键差异。
- 必须配正文解释“看这张图时抓哪两个判断点”。

示例风格：
- `solution-webdev-solo-vs-team-map-v1.webp`
- `solution-xhs-cli-vs-acp-v3-cliproxy-g31.webp`
- `rm2-4-soul-02-soul-behavior-diff.webp`

### 8.3 真实截图 / 操作证据

适合云厂商、企业微信、桌面端、终端验证。

要求：
- 截图中不能出现真实 token、secret、手机号、私人群名等敏感信息。
- 截图必须对应正文中的某一步。
- 正文必须说明这张图证明什么。
- 如果截图来自官方页面，要在正文说明“官方截图/官方入口”。

示例风格：
- `tencent-server-list-login-entry.webp`
- `wecom-create-bot-entry-official.webp`
- `desktop-07-real-chat-v1.webp`

### 8.4 输出物总览图

适合“现成方案”类文章。

要求：
- 展示用户最终拿到什么。
- 最好拆成 3 个阶段：输入 → 处理 → 产出 / 下一步。
- 不要只做漂亮海报，要能帮助读者判断是否值得用。

示例风格：
- `solution-webdev-3-layer-map-v1.webp`
- `solution-message-summary-output-map-v1.webp`
- `office-daily-output-gemini-3-pro-image-preview.webp`

## 9. 配图数量建议

- P0 实战长文：3 张
  1. 首图：端到端闭环图
  2. 中段：关键选择/架构对比图
  3. 后段：输出物或验证结果图
- P1 教程：2 张
  1. 首图：路径图
  2. 中段：步骤或产出结构图
- 小更新/参考页：0-1 张，不强行配图。
- 如果无法获得真实截图，优先画结构图，不要编造“真实界面”。

## 10. 图片引用格式

示例：

```markdown
![Hermes Agent 做服务器自动化运维闭环：Cron 定时巡检磁盘、内存和 Nginx 状态，异常时通过企业微信告警，正常时保持沉默](../../assets/server-devops-alert-flow-v1.webp)
```

要求：
- alt 文本必须包含：主体、动作、结果。
- 路径必须从当前文章位置正确相对引用。
- 图片下面正文要解释读图方式：
  - “看这张图时，你只需要抓住两点：...”

## 11. 内容质量验收清单

每篇文章交付前必须自查：

- 是否与现有 SOUL / Ollama / MCP 等文章重复？
- 是否有明确读者画像？
- 是否有真实场景，而不是功能罗列？
- 是否有最短路径？
- 是否有可复制命令、配置或 Prompt？
- 是否说明成功标准？
- 是否说明失败时查哪里？
- 是否引用已有文章而不是重复讲？
- 是否至少有 1 张有解释价值的 `.webp` 主图？
- 图片 alt 是否具体、中文、可读？
- 是否未泄露任何 token、secret、手机号、私有路径？

## 12. 派单时必须写进任务的约束

后续内容生产任务必须包含：

```text
你必须遵守 /opt/projects/awesome-hermes-agent-zh/artifacts/20260704-article-format-and-image-standard.md。
文章必须是实际应用导向，不写大而全教程。
文章必须使用稳定语义的 emoji 区分关键段落，保证中文用户快速扫读时能看懂结构。
每个主段落开头先给一句“这一节解决什么”，再展开细节。
每篇 P0/P1 新文章至少包含符合标准的 .webp 配图方案；结构图、流程图、对比图必须用生图模型生成，不允许用 SVG/HTML/CSS/Mermaid 自己手绘后导出。
如果任务包含实际写图，图片需放入 docs/assets/ 或同目录 assets/，并用中文长 alt 引用。
交付时必须列出：文章路径、图片路径、生图提示词、负面提示词、引用的已有文章、去重说明、验收自查结果。
```
