# 🚀 项目交付看板 (Delivery Kanban)

## 1. 核心状态概览 (Dashboard)
- **项目阶段**: Phase 2 (核心内容产出)
- **总达成率**: 65%
- **当前瓶颈**: 视觉品牌设计 (Logo/Banner) 延迟。

---

## 2. 角色分工与交付明细

| 任务 ID | 任务描述 | 负责人 | 输入 | 成果 (Output) | 标准 | 达成率 | 交接给 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **A-101** | 极简仓库骨架 | **PM (Seiya)** | OPC 指令 | `/opt/projects` 物理路径 | 100% 物理纯净 | 100% | Coder |
| **B-201** | 国内模型接入配置 | **Coder (Long)** | PRD | `/examples/configs/` (DeepSeek/Qwen) | 本地配置即刻跑通 | 100% | Content |
| **B-202** | 实战 Starter 模板 | **Coder (Long)** | SSD | `/starters/` (Single/Team/Advanced) | 包含完整 config 与人设 | 100% | Content |
| **C-301** | 快速开始教程 | **Content (Ikki)** | B-201 | `docs/quick-start.md` | 30秒内从 0 到 1 | 100% | PM (Audit) |
| **C-302** | 首页架构重构 | **PM (Seiya)** | User Feedback | `docs/index.md` (V5.0) | GitHub 预览无宽表 | 100% | Designer |
| **B-203** | 飞书/钉钉 Webhook 集成 | **Coder (Long)** | SSD, API Docs | `/examples/skills/webhook-notifier/` | 代码可用且支持环境变量 | 100% | Content |
| **C-303** | 自定义工具开发教程 | **Content (Ikki)** | B-203 | `docs/custom-tools.md` | 保姆级指引 | 0% | PM (Audit) |
| **D-401** | 架构图设计 | **Designer (Shun)** | C-302 | `public/architecture.excalidraw` | 包含 PM-Coder-QA 流 | 85% | Content |
| **D-402** | 品牌视觉 (Logo/Banner) | **Designer (Shun)** | README_DRAFT | `logo.png`, `banner.png` | 符合 .ai 专业调性 | **10%** | Ops |
| **E-501** | 自动化构建与域名 | **Ops (Hyoga)** | Git Repo | CI/CD Workflow + Domain | 自动触发同步 | 0% | PM (Final) |

---

## 3. 验收标准说明 (Quality Standard)

1. **GitHub 仓库**: 严禁出现任何内部管理文档（如 PROJECT.md, PRD.md 等）。
2. **教程文档**: 必须在 3 屏内讲完核心步骤，禁止长篇大论。
3. **配置文件**: 必须支持环境变量注入，禁止硬编码 API Key。
4. **视觉资产**: 必须为 SVG 或高精 PNG，Banner 比例 16:9。

---

## 4. 实时统计 (Stats)
- **总任务数**: 8
- **已完工 (Done)**: 5
- **进行中 (Doing)**: 2 (D-401, D-402)
- **待开始 (Todo)**: 1 (E-501)
- **交接状态**: 
  - PM 已交接给 Coder 完成。
  - Coder 已交接给 Content 完成。
  - Content 正在等待 Designer 交付视觉。
