# 05-实战应用 图片需求规格 — 给视觉 Designer / PM 视觉闸门

> **本文档由 Content Agent (Ikki) 产出**，供视觉 Designer 按 cliproxy 标准制作，并由 PM 做视觉闸门验收。
> **数量**：6 篇保留页 v2 重做 + 5 篇新增页 v1 首制 = **共 11 张图片**。

---

## 🎨 通用视觉硬规则（来自任务调度）

| 项 | 标准 |
|---|---|
| 生成方式 | **cliproxy**（必须） |
| 比例 | **16:9** |
| 文字 | **中文可读短标签**（不写英文长句，不写代码） |
| 底色 | **深海军蓝 / 蓝黑底** |
| 装饰 | **细网格 / 电路线** |
| 卡片 | **白 / 青线稿卡片**（线稿风，不写实） |
| 强调色 | **少量橙色节点**（仅用于关键路径节点 / 数据点） |
| 禁止 | 手画风 / SVG 转 PNG / 假截图 / 截断 / 密集文字 / UI 卡片漂移 |

**参考已接受项目图**：
- `assets/practical-11-discord-official-screenshot-zh-v1.webp`（旧版，作为风格基线）
- `assets/practical-13-ollama-official-screenshot-zh-v1.webp`
- `assets/practical-14-github-pr-review-official-screenshot-zh-v1.webp`
- `assets/practical-15-skills-official-screenshot-zh-v1.webp`
- `assets/practical-18-security-official-screenshot-zh-v1.webp`
- `assets/practical-19-voice-mode-official-screenshot-zh-v1.webp`

> ⚠️ v1 文件保留作为风格基线，**新图片用 v2 命名**，PM 视觉闸门通过后由 Ops/PM 决定是否替换 v1。

---

## 📋 11 张图片需求规格

### 重做（6 张，v2）

#### 1. `practical-11-discord-official-screenshot-zh-v2.webp`

- **文件路径**：`assets/practical-11-discord-official-screenshot-zh-v2.webp`
- **alt 文本**（已写入正文）："Hermes Agent 接入 Discord 全景：Developer Portal 创建 Application 与 Bot、Privileged Gateway Intents（Server Members + Message Content）、OAuth2 邀请链接、白名单与 Role 权限分级、频道与线程会话隔离"
- **关键元素**：6 个节点横向流程：① 创建 App/Bot → ② 开 Intents → ③ 生成邀请链接 → ④ 拉进服务器 → ⑤ 白名单/Role → ⑥ 频道/线程隔离
- **强调节点**（橙色）：② Intents（关键一步，漏了 Bot 不响应）
- **对应正文**：`docs/01-从这开始/05-实战应用/11-Discord 接入.md`

#### 2. `practical-13-ollama-official-screenshot-zh-v2.webp`

- **文件路径**：`assets/practical-13-ollama-official-screenshot-zh-v2.webp`
- **alt 文本**（已写入正文）："Hermes Agent 接入 Ollama 三层决策树：本地零账单推理路径、显存与速度边界、隐私 vs 工具上云的真实区分、三层路由（本地兜底 + 云端高难度 + 强模型专用）"
- **关键元素**：决策树结构：① 显存 ≥ 8GB？→ 走本地 → ② 任务复杂？→ 走云端兜底 → ③ 强模型专用通道。突出"本地 ≠ 隐私"提示
- **强调节点**（橙色）：决策分叉点
- **对应正文**：`docs/01-从这开始/05-实战应用/13-Ollama 本地模型.md`

#### 3. `practical-14-github-pr-review-official-screenshot-zh-v2.webp`

- **文件路径**：`assets/practical-14-github-pr-review-official-screenshot-zh-v2.webp`
- **alt 文本**（已写入正文）："Hermes Agent 做 GitHub PR 自动审查端到端：PR opened/synchronized Webhook → Hermes 触发 → diff 解析 + 测试运行 + 安全扫描 + 反模式检测 → 评论回流与 inline comment + status check"
- **关键元素**：流水线（左→右）：GitHub PR 事件 → Webhook → Hermes → 4 个并行检查模块（diff / 测试 / 安全 / 反模式）→ 评论/inline/status 三种回流
- **强调节点**（橙色）：Webhook 触发点
- **对应正文**：`docs/01-从这开始/05-实战应用/14-GitHub PR 自动审查.md`

#### 4. `practical-15-skills-official-screenshot-zh-v2.webp`

- **文件路径**：`assets/practical-15-skills-official-screenshot-zh-v2.webp`
- **alt 文本**（已写入正文）："Hermes Agent 自定义 Skill 工作流：识别重复任务 → 写 SKILL.md（含 when_to_use/prerequisites/known_failure_modes/last_verified_against）→ 放到 ~/.hermes/skills/ → 一句话或 /skill 触发，Agent 自动加载并按步骤执行 → /reset 生效"
- **关键元素**：5 节点流程：① 识别重复 → ② 写 SKILL.md（4 个 frontmatter 字段以小卡片显示）→ ③ 放目录 → ④ 触发 → ⑤ /reset
- **强调节点**（橙色）：第 ② 步的 frontmatter 4 字段
- **对应正文**：`docs/01-从这开始/05-实战应用/15-自定义 Skills.md`

#### 5. `practical-16-security-official-screenshot-zh-v2.webp`（原 18，重命名）

- **文件路径**：`assets/practical-16-security-official-screenshot-zh-v2.webp`
- **alt 文本**（已写入正文）："Hermes Agent 生产安全加固四层纵深防御：第一层用户白名单与 Role 鉴权 → 第二层命令审批与危险操作拦截 → 第三层 Docker/SSH 执行隔离 → 第四层密钥保护与 redact_secrets，缺一不可"
- **关键元素**：4 层同心圆或 4 列纵深防御：① 白名单 → ② 命令审批 → ③ 容器隔离 → ④ 密钥保护
- **强调节点**（橙色）：每层的关键拦截点
- **对应正文**：`docs/01-从这开始/05-实战应用/16-安全加固.md`

#### 6. `practical-17-voice-mode-official-screenshot-zh-v2.webp`（原 19，重命名）

- **文件路径**：`assets/practical-17-voice-mode-official-screenshot-zh-v2.webp`
- **alt 文本**（已写入正文）："Hermes Agent 语音模式三大入口架构：CLI Ctrl+B 本地录音、Telegram 语音消息上传、Discord 语音频道加入；统一经 STT（faster-whisper）转文字 → Agent Loop → TTS（Edge TTS / OpenAI）转语音回应"
- **关键元素**：三入口汇聚到统一管线（STT → Agent → TTS），三入口用三种图标区分（终端 / 飞机 / 游戏手柄）
- **强调节点**（橙色）：Agent Loop 中央节点
- **对应正文**：`docs/01-从这开始/05-实战应用/17-语音模式.md`

---

### 新增（5 张，v1）

#### 7. `practical-18-hermes-advanced-official-screenshot-zh-v1.webp`

- **文件路径**：`assets/practical-18-hermes-advanced-official-screenshot-zh-v1.webp`
- **alt 文本**（已写入正文）："Hermes Agent 进阶实战四象限：自进化 Skills 治理（左上）、MCP 深度集成（右上）、Subagent 编排（左下）、生产可观测（右下），中央为 Agent Loop"
- **关键元素**：2×2 象限图，中央是 Agent Loop 标识。四象限标题分别为：① 自进化 Skills 治理 / ② MCP 深度集成 / ③ Subagent 编排 / ④ 生产可观测
- **强调节点**（橙色）：中央 Agent Loop 节点 + 每象限 1 个关键风险点
- **对应正文**：`docs/01-从这开始/05-实战应用/18-Hermes Agent 进阶实战.md`

#### 8. `practical-19-hermes-control-room-official-screenshot-zh-v1.webp`

- **文件路径**：`assets/practical-19-hermes-control-room-official-screenshot-zh-v1.webp`
- **alt 文本**（已写入正文）："Hermes Agent 控制室四层架构：Level 1 单 Agent、Level 2 直属专员、Level 3 Orchestrator + 任务总线、Level 4 自动化团队"
- **关键元素**：4 层阶梯式架构图：① Level 1 控制室 + 单 Agent → ② Level 2 多专员 → ③ Level 3 Orchestrator + 任务总线 → ④ Level 4 自动化
- **强调节点**（橙色）：Level 3 的 Orchestrator 节点（最易失控的一层）
- **对应正文**：`docs/01-从这开始/05-实战应用/19-Hermes Agent 控制室.md`

#### 9. `practical-20-60day-analyst-official-screenshot-zh-v1.webp`

- **文件路径**：`assets/practical-20-60day-analyst-official-screenshot-zh-v1.webp`
- **alt 文本**（已写入正文）："60 天分析师工作流六象限：Provider 选型、Tools/Skills 设计、Memory 策略、反馈循环、x402 经济、Skill 打包"
- **关键元素**：2×3 六宫格：① Provider 选型 / ② Tools & Skills 设计 / ③ Memory 策略 / ④ 反馈循环 / ⑤ x402 经济 / ⑥ Skill 打包
- **强调节点**（橙色）：每格 1 个关键洞察（如 ④ 的"6 步循环"、⑥ 的"500 token"）
- **对应正文**：`docs/01-从这开始/05-实战应用/20-60 天分析师工作流.md`

#### 10. `practical-21-hermes-ollama-fastest-official-screenshot-zh-v1.webp`

- **文件路径**：`assets/practical-21-hermes-ollama-fastest-official-screenshot-zh-v1.webp`
- **alt 文本**（已写入正文）："Hermes + Ollama 最快路径：装 Hermes → 装配置向导 → 选 Custom OpenAI 兼容 → 指向 localhost:11434 → 选 gpt-oss:20b → 跑通"
- **关键元素**：7 步纵向流程图，每步带"⏱️ X 分钟"标注。总时长 20 分钟，总账单 $0
- **强调节点**（橙色）：Step 4 的 "Custom OpenAI-compatible endpoint"（最关键选择）
- **对应正文**：`docs/01-从这开始/05-实战应用/21-Hermes Agent 与 Ollama 最快路径.md`

#### 11. `practical-22-hermes-deep-dive-official-screenshot-zh-v1.webp`

- **文件路径**：`assets/practical-22-hermes-deep-dive-official-screenshot-zh-v1.webp`
- **alt 文本**（已写入正文）："Hermes 内核四象限：Agent Loop（左上）、System Prompt 12 段组装（右上）、Tools 自注册 registry（左下）、四种 API 模式自动切换（右下）"
- **关键元素**：2×2 象限：① Agent Loop 6 步循环图 / ② System Prompt 12 层堆叠 / ③ Tools registry 自注册（plugin 图标） / ④ 4 种 API 模式分支
- **强调节点**（橙色）：第 ② 象限的 "Frozen-Snapshot" 标记（cache 关键）
- **对应正文**：`docs/01-从这开始/05-实战应用/22-Hermes Agent 深度拆解与自建指南.md`

---

## 📐 文件命名一致性表

| 页面 | 图片文件名 | 状态 |
|---|---|---|
| 11-Discord | `practical-11-discord-official-screenshot-zh-v2.webp` | 重做 |
| 13-Ollama | `practical-13-ollama-official-screenshot-zh-v2.webp` | 重做 |
| 14-PR 审查 | `practical-14-github-pr-review-official-screenshot-zh-v2.webp` | 重做 |
| 15-Skills | `practical-15-skills-official-screenshot-zh-v2.webp` | 重做 |
| 16-安全加固 | `practical-16-security-official-screenshot-zh-v2.webp` | 新制（原 18 文件名作废） |
| 17-语音模式 | `practical-17-voice-mode-official-screenshot-zh-v2.webp` | 新制（原 19 文件名作废） |
| 18-进阶实战 | `practical-18-hermes-advanced-official-screenshot-zh-v1.webp` | 首制 |
| 19-控制室 | `practical-19-hermes-control-room-official-screenshot-zh-v1.webp` | 首制 |
| 20-60 天 | `practical-20-60day-analyst-official-screenshot-zh-v1.webp` | 首制 |
| 21-最快路径 | `practical-21-hermes-ollama-fastest-official-screenshot-zh-v1.webp` | 首制 |
| 22-深度拆解 | `practical-22-hermes-deep-dive-official-screenshot-zh-v1.webp` | 首制 |

---

## ✅ Designer 交付前自检

- [ ] 11 张图片全部为 16:9 比例
- [ ] 中文短标签可读（≤ 8 字/标签）
- [ ] 底色统一深海军蓝 / 蓝黑
- [ ] 卡片为白 / 青线稿风
- [ ] 橙色节点仅用于关键路径，不超过总元素 10%
- [ ] 没有手画风、没有假截图、没有截断、没有 UI 卡片漂移
- [ ] 文件名严格按上表
- [ ] alt 文本与正文已写入的 alt 完全一致

---

## 📤 下游 action

1. **视觉 Designer**：按本规格用 cliproxy 制作 11 张图，输出候选
2. **PM 视觉闸门**：按"通用视觉硬规则"和已接受项目图比对，通过/打回
3. **PM 通过后**：图片机械落地到 `/opt/projects/awesome-hermes-agent-zh/assets/`，覆盖/新增对应文件
4. **Ops / PM**：触发 content-sync → 站点 content-cache / search / sitemap / llms / ai-index 重建

> ⚠️ **当前阻塞**：图片未制作，正文里的图片引用是"占位引用"。**图片通过 PM 视觉闸门前**，**不要触发站点构建**——否则会出现 broken image。
