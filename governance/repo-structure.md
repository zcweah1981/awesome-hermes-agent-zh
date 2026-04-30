# Repo Structure

更新时间：2026-04-30（北京时间）

本文件记录 `awesome-hermes-agent-zh` 内容仓当前真实公开结构。它不是未来规划清单，也不是内部执行看板。

## 当前真实公开结构

```text
.
├─ .github/
│  └─ workflows/
│     └─ content-check.yml
├─ README.md
├─ assets/
│  ├─ readme-core-features.jpg
│  ├─ readme-governance-panel.jpg
│  ├─ readme-hermes-capability-map.jpg
│  ├─ readme-hero-hub.jpg
│  ├─ readme-hero-v1.jpg
│  ├─ readme-scenarios.jpg
│  └─ readme-user-routing.jpg
├─ docs/
│  ├─ 00-文档总览.md
│  ├─ 01-从这开始/
│  │  ├─ 总览.md
│  │  ├─ 01-先跑起来/
│  │  ├─ 02-开始上手/
│  │  ├─ 03-玩出花样/
│  │  └─ 04-自己造东西/
│  ├─ 02-现成方案/
│  │  ├─ 01-总览.md
│  │  ├─ 01-内容创作与发布/
│  │  ├─ 02-办公效率与知识整理/
│  │  └─ 03-应用开发与快速原型/
│  ├─ 03-国内落地/
│  │  ├─ 01-总览.md
│  │  ├─ 01-国内部署/
│  │  ├─ 02-国内模型/
│  │  └─ 03-国内入口/
│  ├─ 04-从OpenClaw过来/
│  ├─ 05-遇到问题/
│  ├─ 06-reference/
│  ├─ assets/
│  └─ start-here/
│     └─ assets/
├─ governance/
│  ├─ README.md
│  ├─ repo-policy.md
│  ├─ repo-structure.md
│  ├─ page-source-map.md
│  ├─ site-route-map.yaml
│  ├─ content-contract.md
│  ├─ packs-map.md
│  └─ publishing-checklist.md
└─ packs/
   ├─ README.md
   ├─ daily-report-lab/
   ├─ meeting-lab/
   ├─ miniapp-lab/
   ├─ ppt-lab/
   ├─ summary-lab/
   ├─ webdev-lab/
   ├─ wechat-writer-lab/
   └─ xhs-lab/
```

## 顶层目录职责

### `README.md`
- 仓库总入口。
- 面向读者解释“这是什么、先从哪里进、有哪些模块”。
- 只链接当前真实存在的 docs / governance / packs 入口。

### `.github/workflows/content-check.yml`
- 仓库级内容完整性检查。
- 当前检查范围：`docs/` Markdown 扫描、`packs/` manifest YAML 解析、关键目录存在性。
- 它是公开仓质量门的一部分，不承载内部 PM 调度。

### `assets/`
- README 使用的公开图片资源。
- 不放内部草稿图、临时评审图、未确认视觉素材。

### `docs/`
- 公开文档主树。
- 当前正式口径为“编号 + 中文目录树”。
- 页面渲染路径、标题、模块、顺序等机器元数据集中到 `governance/site-route-map.yaml`，不再散落在每篇 Markdown 的 frontmatter 里。

### `governance/`
- 内容仓自己的公开最小治理层。
- 只解释外部仓结构、入仓边界、页面来源、route-map 合同、packs 映射和发布前检查。
- 不承载内部 PM / 巡查 / 执行控制资产。

### `packs/`
- 面向用户的可下载方案包与工作流安装资源。
- 每个方案包以 `manifest.yaml` 作为公开索引，以 `INSTALL.md` 作为默认入口。

## docs 正式模块树

```text
docs/
├─ 00-文档总览.md
├─ 01-从这开始/
│  ├─ 总览.md
│  ├─ 01-先跑起来/
│  ├─ 02-开始上手/
│  ├─ 03-玩出花样/
│  └─ 04-自己造东西/
├─ 02-现成方案/
│  ├─ 01-总览.md
│  ├─ 01-内容创作与发布/
│  ├─ 02-办公效率与知识整理/
│  └─ 03-应用开发与快速原型/
├─ 03-国内落地/
│  ├─ 01-总览.md
│  ├─ 01-国内部署/
│  ├─ 02-国内模型/
│  └─ 03-国内入口/
├─ 04-从OpenClaw过来/
├─ 05-遇到问题/
└─ 06-reference/
```

## governance 文件说明

- `README.md`：治理入口，说明每个治理文件的用途与阅读顺序。
- `repo-policy.md`：外部仓保留原则、入仓边界、禁止入仓内容。
- `repo-structure.md`：当前真实仓库结构。
- `page-source-map.md`：模块级页面来源映射和关键入口映射。
- `site-route-map.yaml`：独立站消费的页面路由合同。
- `content-contract.md`：docs / route-map / packs / assets 的公开内容合同。
- `packs-map.md`：当前开放方案包、模式、文档页和安装入口映射。
- `publishing-checklist.md`：发布前维护者自检清单。

## packs 当前开放结构

当前 `packs/` 已开放 8 个方案包：

- `miniapp-lab`：微信小程序助手，Solo + Team。
- `webdev-lab`：敏捷 Web 开发助手，Solo + Team。
- `meeting-lab`：会议纪要助手，Solo。
- `daily-report-lab`：项目日报助手，Solo。
- `summary-lab`：资料总结助手，Solo。
- `xhs-lab`：小红书内容助手，Solo + Team。
- `wechat-writer-lab`：公众号写作助手，Solo + Team。
- `ppt-lab`：PPT 助手，Solo + Team。

完整映射见 [`packs-map.md`](./packs-map.md)。

## 不再采用的旧路径口径

以下旧英文目录名仅用于历史理解，不再视为当前正式结构：

- `docs/start-here/`
- `docs/solutions/`
- `docs/china/`
- `docs/migrate/`
- `docs/issues/`
- `docs/reference/`

说明：仓内如果仍有少量历史资源目录，只按“历史资源兼容/迁移残留”处理，不能作为当前正式导航口径。

## 一句话规则

当前外部仓结构以“编号中文 docs 树 + 最小 governance + packs 方案包 + README/assets 展示资源”为准。新增结构必须先有真实内容、真实入口、真实维护价值。