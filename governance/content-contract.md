# Content Contract

更新时间：2026-04-30（北京时间）

本文件定义内容仓 `awesome-hermes-agent-zh` 与独立站、读者、维护者之间的公开内容合同。

## 目标

确保内容仓里的文档、路由、方案包和资源可以被稳定消费：

- 读者能直接在 GitHub 阅读。
- 独立站能按 route-map 渲染页面。
- 维护者能判断新增内容应该放在哪里。
- packs 能和方案页形成可验证映射。

## 内容分层

### 1. README 入口层

归属：`README.md`、`assets/`

职责：
- 解释中文站定位。
- 提供 6 个固定模块入口。
- 提供治理入口和仓库结构入口。

约束：
- README 只链接真实存在的页面。
- README 图片必须来自仓内公开 `assets/`。
- 不放内部开发版本号、内部派单状态、内部执行日志。

### 2. docs 正文层

归属：`docs/`

职责：
- 承载公开可读的中文文档正文。
- 使用编号中文目录树组织导航。
- 页面本身保持普通 Markdown 可读，不依赖内部系统才能理解。

约束：
- 正式路径以 `docs/00-文档总览.md` 和 6 个固定模块为准。
- 不在公开正文顶部暴露内部 `status`、`sourcePath`、`module` 等机器字段。
- 页面有配图时，图片路径必须指向仓内公开资源。
- 新增页面必须同步更新 `governance/site-route-map.yaml`，否则独立站无法稳定消费。

### 3. route-map 元数据层

归属：`governance/site-route-map.yaml`

职责：
- 作为独立站消费内容的机器合同。
- 集中维护页面 slug、模块、标题、顺序、状态和来源类型。

约束：
- 每个需要被独立站渲染的 Markdown 页面，都应有一条 route 记录。
- `source` 必须指向仓内真实存在的 Markdown 文件。
- `slug` 必须是稳定公开路径，不写本地文件系统路径。
- `status` 当前只用于发布控制，不应在读者页面显著展示。

### 4. packs 方案包层

归属：`packs/`

职责：
- 承载可下载、可安装、可试跑的方案包。
- 与 `docs/02-现成方案/` 下的方案页形成一一或一对多映射。

约束：
- 每个 pack 根目录必须有 `manifest.yaml` 和 `INSTALL.md`。
- 如果提供下载包，zip 路径应写入 `manifest.yaml`。
- 如果提供 Team 模式，应在 `02-team/README.md` 或对应安装脚本中说明角色入口。
- manifest 中的 `doc` 必须指向真实方案页。

### 5. governance 公开治理层

归属：`governance/`

职责：
- 解释公开仓为什么这样组织。
- 维护仓库结构、内容边界、来源映射、route-map 合同、packs 映射和发布前自检。

约束：
- 只放对公开维护有价值的治理文件。
- 不放内部 PM 派单、巡查脚本、dispatch log、阶段执行看板。
- 不提前铺未来占位页。

## route-map 字段合同

`governance/site-route-map.yaml` 每条 route 当前使用这些字段：

- `source`：仓内 Markdown 源文件路径。
- `slug`：独立站公开访问路径。
- `module`：所属模块标识，例如 `start`、`solutions`、`china`、`openclaw`、`issues`、`reference`。
- `page_type`：页面类型，例如 `module-overview`、`doc-page`。
- `title`：页面标题。
- `section`：页面所在子分区。
- `description`：用于站点摘要、搜索或卡片展示的简短说明。
- `order`：模块内排序。
- `status`：当前发布状态，已发布页面使用 `published`。
- `updated`：内容更新时间。
- `source_type`：来源类型，例如 `original`、`official-reference`、`curated`。
- `nav_group`：站点侧导航分组。

维护要求：
- `source`、`slug`、`title`、`module`、`order` 为关键字段。
- 新增 route 前先确认 Markdown 文件已经真实存在。
- 删除或移动 Markdown 文件时，必须同步修改 route-map。

## pack manifest 字段合同

每个 `packs/*/manifest.yaml` 当前使用这些字段：

- `id`：pack 唯一标识，通常与目录名一致。
- `title`：中文标题。
- `category`：对应方案分类。
- `summary`：一句话说明。
- `modes`：支持模式，例如 `solo`、`team`。
- `doc`：对应方案页。
- `install`：安装说明入口。
- `download`：默认下载包。
- `status`：发布状态。
- `featured`：是否重点推荐。
- `order`：展示排序。
- `tags`：检索标签。

## 新增内容流程

### 新增 docs 页面

1. 在正确的编号中文目录下新增 Markdown。
2. 确认页面可在 GitHub 直接阅读。
3. 在 `governance/site-route-map.yaml` 增加 route。
4. 如属于新模块入口，同步更新 `docs/00-文档总览.md` 和 README 入口。
5. 如涉及来源或边界变化，同步更新 `page-source-map.md` 或 `repo-policy.md`。

### 新增 pack

1. 在 `packs/` 下新增 pack 目录。
2. 添加 `manifest.yaml`、`INSTALL.md` 和必要模式目录。
3. 确认 `manifest.yaml` 的 `doc` 指向真实方案页。
4. 更新 `packs/README.md`。
5. 更新 `governance/packs-map.md`。

### 新增 README 资产

1. 图片放入根 `assets/`。
2. README 使用相对路径引用。
3. 图片 alt 文案说明用途。
4. 不提交临时评审图或无用版本图，除非它仍被 README 使用。

## 一句话规则

Markdown 负责公开可读内容，`site-route-map.yaml` 负责机器可消费元数据，`packs/manifest.yaml` 负责方案包索引；三者必须指向同一套真实存在的内容。