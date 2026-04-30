# Page Source Map

更新时间：2026-04-25（北京时间）

本文件只记录当前已经真实落仓、并且仍属于当前正式路径口径的页面来源映射。

## 当前正式路径口径
当前外部仓 docs 正式模块目录为：
- `docs/01-从这开始/`
- `docs/02-现成方案/`
- `docs/03-国内落地/`
- `docs/04-从OpenClaw过来/`
- `docs/05-遇到问题/`
- `docs/06-reference/`

旧英文目录名（如 start-here / china / migrate / issues / solutions / reference）只作为历史命名理解，不再作为当前正式路径口径。

## 上游依据
当前公开页的上游依据主要来自：
- 内部 PRD / PAGE_CARDS / CHECKLIST / PHASES 体系
- 已确认的模块级页面卡与来源整理
- 当前外部仓已真实落仓的页面内容与导航关系

说明：
- 这些上游文件大多位于内部管理主包，不全部进入外部仓
- 外部仓只记录“当前页从哪类依据来”，不复制整套内部治理资产

## 已落仓模块映射

| 外部模块 | 当前正式路径 | 主要来源类型 | 说明 |
|---|---|---|---|
| 从这开始 | `docs/01-从这开始/` | 原始 PRD、目录映射表、页面卡、逐页内容稿 | 学习主线路径模块 |
| 现成方案 | `docs/02-现成方案/` | 方案页卡、已验收页面结构、配套 packs | 解决方案与下载包模块 |
| 国内落地 | `docs/03-国内落地/` | 国内落地页面卡、逐页落地内容、真实截图与结构图 | 国内部署 / 模型 / 入口模块 |
| 从OpenClaw过来 | `docs/04-从OpenClaw过来/` | 迁移页卡、对比 / 迁移 / 共存说明 | OpenClaw 迁移模块 |
| 遇到问题 | `docs/05-遇到问题/` | FAQ 结构页、官方问题边界、排障整理 | 问题定位与排障模块 |
| Reference | `docs/06-reference/` | 官方 reference 原文、中文重写与目录化整理 | 参考手册模块 |

## 当前仓内关键入口映射

| 入口 | 当前正式目标 |
|---|---|
| 仓库首页 | `README.md` |
| 文档总览 | `docs/00-文档总览.md` |
| 从这开始 | `docs/01-从这开始/总览.md` |
| 现成方案 | `docs/02-现成方案/01-总览.md` |
| 国内落地 | `docs/03-国内落地/01-总览.md` |
| 从OpenClaw过来 | `docs/04-从OpenClaw过来/01-总览.md` |
| 遇到问题 | `docs/05-遇到问题/01-总览.md` |
| Reference | `docs/06-reference/01-总览.md` |
| 治理说明 | `governance/README.md` |
| 仓库结构 | `governance/repo-structure.md` |
| 内容合同 | `governance/content-contract.md` |
| 页面来源映射 | `governance/page-source-map.md` |
| 站点路由合同 | `governance/site-route-map.yaml` |
| 方案包映射 | `governance/packs-map.md` |
| 发布自检 | `governance/publishing-checklist.md` |
| 方案包总览 | `packs/README.md` |

## 维护规则
1. 只记录当前真实存在的入口与模块，不预写未来占位页。
2. 页面正式路径一旦切到编号中文目录树，治理文件同步跟进，不再继续维护旧英文目录口径。
3. 如果模块树、governance 文件或 packs 继续扩展，优先更新这里的模块级映射与入口映射，而不是先补内部说明性文字。

## 一句话规则
只映射当前真实落仓页面，不映射历史旧路径，不映射未来占位页。
