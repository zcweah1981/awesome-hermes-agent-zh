# Packs Map

更新时间：2026-04-30（北京时间）

本文件记录 `packs/` 当前真实开放的方案包，以及它们与 `docs/02-现成方案/` 页面之间的映射。

## 目标

- 让维护者知道每个 pack 对应哪个方案页。
- 让独立站或后续脚本可以核对 pack manifest 是否完整。
- 避免只在 docs 里写方案，但 packs 里没有可执行落地层。

## 当前开放方案包

### 应用开发与快速原型

#### `miniapp-lab`
- 标题：微信小程序助手
- 模式：Solo + Team
- 文档页：[`docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md`](../docs/02-现成方案/03-应用开发与快速原型/02-微信小程序助手.md)
- 安装入口：[`packs/miniapp-lab/INSTALL.md`](../packs/miniapp-lab/INSTALL.md)
- Manifest：[`packs/miniapp-lab/manifest.yaml`](../packs/miniapp-lab/manifest.yaml)
- 默认下载：`packs/miniapp-lab/01-super-individual.zip`

#### `webdev-lab`
- 标题：敏捷 Web 开发助手
- 模式：Solo + Team
- 文档页：[`docs/02-现成方案/03-应用开发与快速原型/03-敏捷 Web 开发助手.md`](<../docs/02-现成方案/03-应用开发与快速原型/03-敏捷 Web 开发助手.md>)
- 安装入口：[`packs/webdev-lab/INSTALL.md`](../packs/webdev-lab/INSTALL.md)
- Manifest：[`packs/webdev-lab/manifest.yaml`](../packs/webdev-lab/manifest.yaml)
- 默认下载：`packs/webdev-lab/01-super-individual.zip`

### 办公效率与知识整理

#### `meeting-lab`
- 标题：会议纪要助手
- 模式：Solo
- 文档页：[`docs/02-现成方案/02-办公效率与知识整理/02-会议纪要助手.md`](../docs/02-现成方案/02-办公效率与知识整理/02-会议纪要助手.md)
- 安装入口：[`packs/meeting-lab/INSTALL.md`](../packs/meeting-lab/INSTALL.md)
- Manifest：[`packs/meeting-lab/manifest.yaml`](../packs/meeting-lab/manifest.yaml)
- 默认下载：`packs/meeting-lab/01-super-individual.zip`

#### `daily-report-lab`
- 标题：项目日报助手
- 模式：Solo
- 文档页：[`docs/02-现成方案/02-办公效率与知识整理/03-项目日报助手.md`](../docs/02-现成方案/02-办公效率与知识整理/03-项目日报助手.md)
- 安装入口：[`packs/daily-report-lab/INSTALL.md`](../packs/daily-report-lab/INSTALL.md)
- Manifest：[`packs/daily-report-lab/manifest.yaml`](../packs/daily-report-lab/manifest.yaml)
- 默认下载：`packs/daily-report-lab/01-super-individual.zip`

#### `summary-lab`
- 标题：资料总结助手
- 模式：Solo
- 文档页：[`docs/02-现成方案/02-办公效率与知识整理/04-资料总结助手.md`](../docs/02-现成方案/02-办公效率与知识整理/04-资料总结助手.md)
- 安装入口：[`packs/summary-lab/INSTALL.md`](../packs/summary-lab/INSTALL.md)
- Manifest：[`packs/summary-lab/manifest.yaml`](../packs/summary-lab/manifest.yaml)
- 默认下载：`packs/summary-lab/01-super-individual.zip`

### 内容创作与发布

#### `xhs-lab`
- 标题：小红书内容助手
- 模式：Solo + Team
- 文档页：[`docs/02-现成方案/01-内容创作与发布/02-小红书内容助手.md`](../docs/02-现成方案/01-内容创作与发布/02-小红书内容助手.md)
- 安装入口：[`packs/xhs-lab/INSTALL.md`](../packs/xhs-lab/INSTALL.md)
- Manifest：[`packs/xhs-lab/manifest.yaml`](../packs/xhs-lab/manifest.yaml)
- 默认下载：`packs/xhs-lab/01-super-individual.zip`

#### `wechat-writer-lab`
- 标题：公众号写作助手
- 模式：Solo + Team
- 文档页：[`docs/02-现成方案/01-内容创作与发布/03-公众号写作助手.md`](../docs/02-现成方案/01-内容创作与发布/03-公众号写作助手.md)
- 安装入口：[`packs/wechat-writer-lab/INSTALL.md`](../packs/wechat-writer-lab/INSTALL.md)
- Manifest：[`packs/wechat-writer-lab/manifest.yaml`](../packs/wechat-writer-lab/manifest.yaml)
- 默认下载：`packs/wechat-writer-lab/01-super-individual.zip`

#### `ppt-lab`
- 标题：PPT 助手
- 模式：Solo + Team
- 文档页：[`docs/02-现成方案/01-内容创作与发布/04-PPT 助手.md`](<../docs/02-现成方案/01-内容创作与发布/04-PPT 助手.md>)
- 安装入口：[`packs/ppt-lab/INSTALL.md`](../packs/ppt-lab/INSTALL.md)
- Manifest：[`packs/ppt-lab/manifest.yaml`](../packs/ppt-lab/manifest.yaml)
- 默认下载：`packs/ppt-lab/01-super-individual.zip`

## 标准 pack 结构

```text
packs/<pack-id>/
├─ manifest.yaml
├─ INSTALL.md
├─ 01-super-individual/
│  ├─ INSTALL.md
│  ├─ SOUL.md
│  ├─ install_to_profile.sh
│  └─ skills/
├─ 01-super-individual.zip
└─ 02-team/                 # 仅 Team 包存在
   ├─ README.md
   ├─ install_all.sh
   ├─ 01-*/
   ├─ 02-*/
   ├─ 03-*/
   ├─ 04-*/
   └─ 99-solution-validator/
```

说明：不是每个 pack 都必须有 Team 模式。当前 `meeting-lab`、`daily-report-lab`、`summary-lab` 只提供 Solo。

## 维护规则

1. 新增 pack 时，先确保对应 docs 方案页已经存在。
2. 每个 pack 必须有 `manifest.yaml` 和 `INSTALL.md`。
3. `manifest.yaml` 的 `doc`、`install`、`download` 路径必须指向真实文件。
4. 新增、改名、删除 pack 后，同步更新：
   - `packs/README.md`
   - `governance/packs-map.md`
   - 如独立站展示 packs，则同步更新站点消费逻辑或 manifest 缓存。
5. zip 包应与目录内容保持一致，不能只更新目录不更新 zip。

## 一句话规则

`docs/02-现成方案/` 负责解释方案，`packs/` 负责提供可执行落地包；两边必须通过 manifest 和本文件保持映射一致。