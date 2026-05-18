# 现成方案视觉返工｜cliproxy 生图基线与提示词

更新时间：2026-05-18
适用范围：
- X/Twitter 内容与互动助手
- 行动计划助手
- 多平台内容改写助手
- 邮件群消息摘要助手

## 1. 任务结论
本组 4 篇页面的 8 张图片，统一按 **深蓝黑技术文档家族** 重做，生成方式必须走 **cliproxy OpenAI-compatible endpoint**，不得使用：
- 手画风
- 伪截图
- SVG/HTML 转 PNG
- Hermes 内置 `image_generate`
- FAL 作为替代

本次输出只定义：
1. 统一视觉基线
2. 8 张目标资产清单
3. 每张图的 cliproxy prompt
4. alt / 插入位置 / 图中文字
5. cliproxy preflight proof

不在本文件内直接产图。

---

## 2. cliproxy preflight proof

### 2.1 运行时检查结果
通过终端执行：

```bash
python - <<'PY'
import os
print('IMAGE_GEN_API_KEY', bool(os.getenv('IMAGE_GEN_API_KEY')))
print('CLIPROXY_API_KEY', bool(os.getenv('CLIPROXY_API_KEY')))
print('IMAGE_GEN_BASE_URL', os.getenv('IMAGE_GEN_BASE_URL') or 'https://cliproxy.biztint.com/v1')
print('IMAGE_GEN_MODEL', os.getenv('IMAGE_GEN_MODEL') or 'gemini-3.1-flash-image')
PY
```

实际结果：
- `IMAGE_GEN_API_KEY = True`
- `CLIPROXY_API_KEY = False`
- `IMAGE_GEN_BASE_URL = https://cliproxy.biztint.com/v1`
- `IMAGE_GEN_MODEL = gemini-3.1-flash-image`

### 2.2 生成通道约束
后续实际生图时应：
- 使用 `IMAGE_GEN_API_KEY`
- 直连 `https://cliproxy.biztint.com/v1`
- 使用 OpenAI-compatible chat completions 路径
- 明确绕过 Hermes 内置 `image_generate`
- 不允许静默回退到 FAL

### 2.3 proof 口径
验收时需明确说明：
- “本组图片将使用 cliproxy OpenAI-compatible endpoint 生成”
- “不使用 Hermes 内置 image_generate”
- “不使用 FAL 替代”

---

## 3. 现有资产审计结论

### 3.1 需要替换的 8 张资产
1. `solution-twitter-read-vs-actions-v1.png`
2. `solution-twitter-setup-chain-v1.png`
3. `solution-action-plan-output-map-v1.png`
4. `solution-action-plan-standard-vs-lite-v1.png`
5. `solution-multiplatform-output-bundle-v1.png`
6. `solution-multiplatform-solo-vs-batch-v1.png`
7. `solution-message-summary-complete-vs-quick-v1.png`
8. `solution-message-summary-output-map-v1.png`

### 3.2 实测尺寸
旧待替换图：
- 上述 8 张均为 `1600x900`（16:9）

现站点较新 cliproxy 家族参考图：
- `solution-xhs-output-map-v2-cliproxy.png` → `1376x768`
- `solution-meeting-output-map-v2-cliproxy.png` → `1376x768`
- `solution-gzh-cli-vs-acp-v2-cliproxy.png` → `1376x768`

### 3.3 可复用基线判断
虽然像素值有两套，但比例一致，统一结论：
- **画布比例固定为 16:9**
- 后续如直接走 cliproxy 生成，优先接受 `1376x768` 一类站内已存在成品尺寸
- 重点是风格统一，不强求继续保留 1600x900

### 3.4 插图家族共性
结合现有页面结构、文件命名、旧图 alt 与历史审计记录，可确认站点基线应为：
- 深蓝黑背景
- 白 / 青 / 蓝线稿卡片
- 技术文档式结构图，不做产品海报
- 中文短标签
- 强留白、强分组、强箭头关系
- 一图只解决一个阅读问题
- 不做拟真 UI，不做网页/APP 截图仿制
- 不堆小字，不塞长段落
- 不允许截断、乱码、英文拼写失控

---

## 4. 统一视觉基线（本组必须遵守）

## 页面/模块
现成方案 docs 配图家族（ready solutions docs family）

## 目标
让用户进入页面后 3 秒内看懂：
- 先怎么选路线
- 最后会拿到什么
- 怎么开始第一轮

## 用户
- 首次接触 Hermes 的中文用户
- 想快速判断“值不值得用 / 先跑哪条 / 输出长什么样”的用户
- 更偏任务导向，不想看抽象方法论的用户

## 结构
统一采用下列三类结构模板：
1. 对比图：A 路线 vs B 路线
2. 输出图：输入 → 处理中间层 → 最终交付
3. 启动链路图：安装 / 配置 / 测试 / 启用

## 关键区块
每张图最多 3～5 个大卡片区块：
- 标题区（可无大标题，但要有清晰主结构）
- 输入区
- 处理区
- 输出区
- 风险/边界提示区（仅在需要时出现）

## 内容层级
1. 主标签：2～6 个字
2. 次标签：4～10 个字
3. 必要补充：极短说明，尽量不超过 12 个汉字

禁止：
- 一整句说明塞进卡片正文
- 小字注释铺满底部
- 多段英文命令直接上图
- 拟真窗口标题栏、聊天气泡、浏览器导航栏

## 交互/体验说明
视觉上要服务扫读，不服务“像真的软件界面”：
- 用卡片、箭头、线框表达流程
- 用颜色区分角色，不用复杂纹理
- 用留白表达层级，不靠文字堆叠
- 每张图中心只讲一个判断或一个链路

## 验收点
- 16:9
- 深蓝黑技术文档家族
- 白/青/蓝线稿卡片
- 中文短标签
- 无伪截图感
- 无小字堆叠
- 无截断
- 无乱码
- 图内不写大段描述
- 与页面相邻小节逻辑一一对应

---

## 5. 通用 cliproxy prompt 母版
后续 8 张图都基于以下母版，只替换结构内容：

```text
Create a clean 16:9 technical documentation illustration for a Chinese AI tools website. Dark deep navy-black background, subtle cyan and blue glow, white/cyan/blue wireframe cards, thin connector lines, minimal geometric icons, strong spacing, generous negative space, sharp hierarchy, readable Chinese short labels only, no paragraphs, no tiny text, no garbled text, no cut-off text, no pseudo screenshot, no fake UI, no browser window, no chat app mockup, not hand-drawn, not watercolor, not poster art. The composition should look like a premium docs diagram for software workflows. Labels must be short, centered, and crisp. Use clear card grouping, 3-5 main blocks, and directional arrows. Keep the image highly scannable in 3 seconds.
```

建议追加负向约束：
- `avoid realistic dashboards`
- `avoid mobile phone mockups`
- `avoid code screenshot`
- `avoid dense captions`
- `avoid long Chinese sentences inside the image`

---

## 6. 分页与单图规格

# A. X/Twitter 内容与互动助手

### 资产 1
- 目标文件名：`solution-twitter-read-vs-actions-v2-cliproxy.png`
- 替换文件：`solution-twitter-read-vs-actions-v1.png`
- 插入位置：`05-X-Twitter 内容与互动助手.md` 第一个配图位置，紧跟「## 🚦 它能做什么：读取 vs 写操作」段落后
- alt：对比图：左侧是默认可用的读取能力，右侧是需要显式开启的写操作，强调第三方插件边界和账号风险
- 图中文字：
  - 顶部主结构：`读取能力 vs 写操作`
  - 左侧组：`默认可用` `搜索推文` `读取上下文` `趋势查看` `提及监控`
  - 中间分隔：`第三方插件`
  - 右侧组：`显式启用` `发推` `回复` `点赞` `私信`
  - 底部提示：`非官方内置` `账号身份执行`
- cliproxy prompt：
```text
Create a clean 16:9 technical documentation illustration for a Chinese AI tools website. Dark deep navy-black background, subtle cyan and blue glow, white/cyan/blue wireframe cards, thin connector lines, minimal geometric icons, strong spacing, generous negative space, sharp hierarchy, readable Chinese short labels only, no paragraphs, no tiny text, no garbled text, no cut-off text, no pseudo screenshot, no fake UI, no browser window, no chat app mockup, not hand-drawn, not poster art.

Diagram topic: X/Twitter plugin capability boundary comparison.

Build a two-column comparison. Left column shows read-only capabilities that are available by default. Right column shows write actions that require explicit enablement. Put a narrow center boundary card to emphasize this is a third-party plugin, not official built-in Hermes capability.

Required Chinese labels only:
Top: 读取能力 vs 写操作
Left column: 默认可用, 搜索推文, 读取上下文, 趋势查看, 提及监控
Center: 第三方插件
Right column: 显式启用, 发推, 回复, 点赞, 私信
Bottom small badges: 非官方内置, 账号身份执行

Use cards and arrows, not screenshots. Keep labels crisp and short. Strong visual separation between safe default reading and higher-risk writing actions.
```
- 设计说明：必须把“第三方插件 / 非官方内置”做成图内可见边界，避免用户误判成 Hermes 官方原生能力。

### 资产 2
- 目标文件名：`solution-twitter-setup-chain-v2-cliproxy.png`
- 替换文件：`solution-twitter-setup-chain-v1.png`
- 插入位置：`05-X-Twitter 内容与互动助手.md` 第二个配图位置，紧跟「## ⚡ 5 分钟跑一轮（读取）」段落后
- alt：结构图：从安装 hermes-tweet、配置 X API、先跑读取验证，到确认后再决定是否启用写操作的最短链路
- 图中文字：
  - 顶部主结构：`最短启动链路`
  - 主链路：`安装插件` `配置 X API` `读取测试` `确认可用`
  - 分支卡片：`继续只读` `启用写操作`
  - 边界提示：`先读后写`
- cliproxy prompt：
```text
Create a clean 16:9 technical documentation illustration for a Chinese AI tools website. Dark deep navy-black background, subtle cyan and blue glow, white/cyan/blue wireframe cards, thin connector lines, minimal geometric icons, strong spacing, generous negative space, readable Chinese short labels only, no paragraphs, no tiny text, no garbled text, no cut-off text, no pseudo screenshot.

Diagram topic: shortest setup chain for a third-party X/Twitter plugin inside Hermes.

Build a left-to-right workflow with four main cards and one final branch. Main flow cards: 安装插件 -> 配置 X API -> 读取测试 -> 确认可用. After confirmation, split into two branches: 继续只读 and 启用写操作. Add one small safety badge: 先读后写.

Top title label: 最短启动链路

Do not show terminal screenshots or app UIs. Use abstract cards, arrows, and a calm technical-doc style.
```
- 设计说明：不画命令行窗口，不画 X 网站界面；重点是“先读取验证，再决定是否开写”。

# B. 行动计划助手

### 资产 3
- 目标文件名：`solution-action-plan-standard-vs-lite-v2-cliproxy.png`
- 替换文件：`solution-action-plan-standard-vs-lite-v1.png`
- 插入位置：`05-行动计划助手.md` 第一个配图位置，紧跟「## 🚦 先选哪一种：标准行动计划 or 精简行动清单」段落后
- alt：对比图：左侧是标准行动计划，右侧是精简行动清单，突出字段完整度与发群效率差异
- 图中文字：
  - 顶部主结构：`标准版 vs 精简版`
  - 左侧组：`标准行动计划` `动作项` `负责人` `截止时间` `优先级` `依赖`
  - 右侧组：`精简行动清单` `动作` `负责人` `截止时间`
  - 底部提示：`完整下发` `快速发群`
- cliproxy prompt：
```text
Create a clean 16:9 technical documentation illustration for a Chinese AI tools website. Dark deep navy-black background, subtle cyan and blue glow, white/cyan/blue wireframe cards, thin connector lines, minimal geometric icons, strong spacing, generous negative space, readable Chinese short labels only, no long text, no tiny text, no pseudo screenshot.

Diagram topic: action-plan output mode comparison.

Build a balanced two-column comparison. Left side is a fuller plan with richer fields. Right side is a lightweight version optimized for fast group sync.

Required Chinese labels:
Top: 标准版 vs 精简版
Left: 标准行动计划, 动作项, 负责人, 截止时间, 优先级, 依赖
Right: 精简行动清单, 动作, 负责人, 截止时间
Bottom badges: 完整下发, 快速发群

Use layered cards and field chips. Make the left side visibly denser but still clean; right side simpler and quicker.
```
- 设计说明：左侧信息更完整，但不能因为“完整”而堆小字，应以字段 chip 表达。

### 资产 4
- 目标文件名：`solution-action-plan-output-map-v2-cliproxy.png`
- 替换文件：`solution-action-plan-output-map-v1.png`
- 插入位置：`05-行动计划助手.md` 第二个配图位置，紧跟「## 📦 你最后会拿到什么」段落后
- alt：结构图：行动计划输出从目标摘要展开到动作计划、风险提醒和执行顺序，最后压成可直接发群的消息正文
- 图中文字：
  - 顶部主结构：`行动计划输出地图`
  - 起点：`目标摘要`
  - 中段：`动作计划表` `风险提醒` `执行顺序`
  - 终点：`发送版正文`
  - 辅助标签：`可直接同步`
- cliproxy prompt：
```text
Create a clean 16:9 technical documentation illustration for a Chinese AI tools website. Dark deep navy-black background, subtle cyan and blue glow, white/cyan/blue wireframe cards, thin connector lines, minimal geometric icons, generous negative space, readable Chinese short labels only, no long sentences, no pseudo screenshot.

Diagram topic: output map for an action-plan assistant.

Build a flow from one input summary block into three structured output blocks and one final delivery block. Sequence: 目标摘要 -> 动作计划表 / 风险提醒 / 执行顺序 -> 发送版正文. Add a small supporting badge: 可直接同步.

Top label: 行动计划输出地图

Use a central pipeline feeling with clean grouping and arrows. This should feel like a docs diagram, not a PM tool screenshot.
```
- 设计说明：这张图是“输出总览图”，不是流程教学图，重点让用户看懂最终拿到的交付包。

# C. 多平台内容改写助手

### 资产 5
- 目标文件名：`solution-multiplatform-solo-vs-batch-v2-cliproxy.png`
- 替换文件：`solution-multiplatform-solo-vs-batch-v1.png`
- 插入位置：`06-多平台内容改写助手.md` 第一个配图位置，紧跟「## 🚦 先选哪一种：先改两个平台 or 先改一个平台」段落后
- alt：对比图：左侧是先改单个平台，右侧是批量多平台改写，突出试跑与一次拿齐多平台成品的差别
- 图中文字：
  - 顶部主结构：`单平台 vs 多平台`
  - 左侧组：`先改一个平台` `试跑` `先看语气` `先看格式`
  - 右侧组：`批量多平台` `小红书` `公众号` `X/Twitter`
  - 底部提示：`先验证` `一次拿齐`
- cliproxy prompt：
```text
Create a clean 16:9 technical documentation illustration for a Chinese AI tools website. Dark deep navy-black background, subtle cyan and blue glow, white/cyan/blue wireframe cards, thin connector lines, minimal geometric icons, strong spacing, generous negative space, readable Chinese short labels only, no paragraphs, no tiny text, no pseudo screenshot.

Diagram topic: single-platform rewrite vs batch multi-platform rewrite.

Build a two-column comparison. Left side should feel like a focused trial route. Right side should feel like one source branching to multiple publishing destinations.

Required Chinese labels:
Top: 单平台 vs 多平台
Left: 先改一个平台, 试跑, 先看语气, 先看格式
Right: 批量多平台, 小红书, 公众号, X/Twitter
Bottom badges: 先验证, 一次拿齐

No fake social media screenshots. Use abstract content cards and output nodes only.
```
- 设计说明：右侧要体现“一源多发”的结构，但不能做成平台页面缩略图墙。

### 资产 6
- 目标文件名：`solution-multiplatform-output-bundle-v2-cliproxy.png`
- 替换文件：`solution-multiplatform-output-bundle-v1.png`
- 插入位置：`06-多平台内容改写助手.md` 第二个配图位置，紧跟「## 📦 你最后会拿到什么」段落后
- alt：结构图：同一篇原始内容先提炼核心信息，再分别输出小红书、公众号和 X/Twitter 的可直接发布版本
- 图中文字：
  - 顶部主结构：`多平台输出包`
  - 起点：`原始内容`
  - 中间：`核心信息`
  - 输出：`小红书版` `公众号版` `X/Twitter 版`
  - 底部提示：`复制就能发`
- cliproxy prompt：
```text
Create a clean 16:9 technical documentation illustration for a Chinese AI tools website. Dark deep navy-black background, subtle cyan and blue glow, white/cyan/blue wireframe cards, thin connector lines, minimal geometric icons, strong spacing, generous negative space, readable Chinese short labels only, no long text, no pseudo screenshot.

Diagram topic: multi-platform rewrite output bundle.

Build a hub-and-spoke structure. One source content card flows into a central refinement card, then branches into three destination cards.

Required Chinese labels:
Top: 多平台输出包
Source: 原始内容
Center: 核心信息
Outputs: 小红书版, 公众号版, X/Twitter版
Bottom badge: 复制就能发

Use clear arrows and equal-weight output cards. Keep the visual centered and highly scannable.
```
- 设计说明：这张图的重点不是“过程”，而是“你会一次拿到哪几份成品”。

# D. 邮件群消息摘要助手

### 资产 7
- 目标文件名：`solution-message-summary-complete-vs-quick-v2-cliproxy.png`
- 替换文件：`solution-message-summary-complete-vs-quick-v1.png`
- 插入位置：`06-邮件群消息摘要助手.md` 第一个配图位置，紧跟「## 🚦 先选哪一种：完整摘要 or 快速摘要」段落后
- alt：对比图：左侧是完整摘要，右侧是快速摘要，突出信息覆盖度和转发速度差异
- 图中文字：
  - 顶部主结构：`完整摘要 vs 快速摘要`
  - 左侧组：`完整摘要` `结论` `信息点` `待办` `时间点` `风险`
  - 右侧组：`快速摘要` `一句话结论` `少量待办`
  - 底部提示：`信息不丢` `适合转发`
- cliproxy prompt：
```text
Create a clean 16:9 technical documentation illustration for a Chinese AI tools website. Dark deep navy-black background, subtle cyan and blue glow, white/cyan/blue wireframe cards, thin connector lines, minimal geometric icons, strong spacing, generous negative space, readable Chinese short labels only, no paragraphs, no tiny text, no pseudo screenshot.

Diagram topic: complete summary vs quick summary for long messages and emails.

Build a two-column comparison. Left side should show a fuller structured summary. Right side should show a compressed quick-forward version.

Required Chinese labels:
Top: 完整摘要 vs 快速摘要
Left: 完整摘要, 结论, 信息点, 待办, 时间点, 风险
Right: 快速摘要, 一句话结论, 少量待办
Bottom badges: 信息不丢, 适合转发

Use chips and grouped cards, not message bubbles or email client screenshots.
```
- 设计说明：必须避免做成 IM 截图拼贴；这是一张“摘要结构差异图”。

### 资产 8
- 目标文件名：`solution-message-summary-output-map-v2-cliproxy.png`
- 替换文件：`solution-message-summary-output-map-v1.png`
- 插入位置：`06-邮件群消息摘要助手.md` 第二个配图位置，紧跟「## 📦 你最后会拿到什么」段落后
- alt：结构图：原始群消息或长邮件先整理成结构化摘要，再压成可直接转发的同步消息，保留结论、待办和关键时间点
- 图中文字：
  - 顶部主结构：`摘要输出地图`
  - 输入：`原始消息` `长邮件`
  - 中间：`结构化摘要`
  - 输出：`结论` `待办` `时间点`
  - 终点：`转发版`
- cliproxy prompt：
```text
Create a clean 16:9 technical documentation illustration for a Chinese AI tools website. Dark deep navy-black background, subtle cyan and blue glow, white/cyan/blue wireframe cards, thin connector lines, minimal geometric icons, strong spacing, generous negative space, readable Chinese short labels only, no long sentences, no pseudo screenshot.

Diagram topic: summary output map for emails and group messages.

Build a left-to-right flow with two input cards merging into one structured summary card, then branching into three result chips and one final forwardable block.

Required Chinese labels:
Top: 摘要输出地图
Inputs: 原始消息, 长邮件
Center: 结构化摘要
Outputs: 结论, 待办, 时间点
Final: 转发版

No fake email UI or chat UI. Keep it abstract, card-based, and clean.
```
- 设计说明：输入侧可以是两个抽象源头卡片，但不能像 Outlook 或企业微信真实界面。

---

## 7. 生成执行规则（给后续执行人）

### 7.1 必须遵守
- 必须走 cliproxy
- 必须是深蓝黑技术文档家族
- 必须是 16:9
- 必须使用中文短标签
- 必须避免伪截图
- 必须体现页面小节逻辑

### 7.2 建议执行方式
1. 先按本文件 prompt 出 2～3 个候选
2. 选最接近站点家族的一张
3. 如图内中文出现错字/截断，优先重生，不建议后补大面积修图
4. 如个别短标签始终不稳定，可采用“生成结构 + 本地覆盖最终标签”方式，但最终视觉仍必须保持同一家族

### 7.3 本组特殊边界
仅 X/Twitter 页面额外要求：
- 必须保留 `第三方插件` / `非官方内置` 的边界提示
- 不得把能力画成 Hermes 官方原生模块
- 不得出现让用户误解为 X 官方面板或 Hermes 官方设置页的伪界面

---

## 8. 验收清单
- [x] 覆盖 4 篇页面
- [x] 列出 8 张待替换资产
- [x] 每张图包含目标文件名
- [x] 每张图包含 cliproxy prompt
- [x] 每张图包含 alt
- [x] 每张图包含插入位置
- [x] 每张图包含图中文字
- [x] 明确禁止手画 / SVG/HTML 转 PNG / FAL / 内置 image_generate
- [x] 明确 X/Twitter 为第三方插件边界
- [x] 记录 cliproxy preflight：key / base_url / model

---

## 9. 验证备注
本次视觉审计中的机器视觉分析工具因 credits 限制返回 402，未作为阻塞项；风格判断基于：
- 已存在 cliproxy 家族文件命名与尺寸
- 4 篇页面内旧图 alt 与插入位置
- 历史 ready-solutions 插图家族审计记录
- 统一站点风格规则与本次任务验收标准

因此本文件可直接作为后续 cliproxy 生图执行基线。