# Governance

更新时间：2026-04-30（北京时间）

本目录是 `awesome-hermes-agent-zh` 内容仓的公开最小治理层。

它只回答 6 个问题：

1. 这个公开仓应该保留什么？
2. 当前真实目录结构是什么？
3. 页面从哪里来、归到哪个模块？
4. 独立站如何消费这些页面？
5. packs 方案包和 docs 方案页如何对应？
6. 发布前维护者应该检查什么？

## 当前治理文件

### 必读入口

- [`repo-policy.md`](./repo-policy.md)：外部仓保留原则、入仓边界、禁止入仓内容。
- [`repo-structure.md`](./repo-structure.md)：当前真实目录结构与正式模块口径。
- [`content-contract.md`](./content-contract.md)：docs、route-map、packs、assets 的公开内容合同。

### 映射与机器合同

- [`page-source-map.md`](./page-source-map.md)：当前已落仓页面与来源映射。
- [`site-route-map.yaml`](./site-route-map.yaml)：独立站消费的页面路由合同。
- [`packs-map.md`](./packs-map.md)：当前开放方案包、模式、文档页和安装入口映射。

### 发布自检

- [`publishing-checklist.md`](./publishing-checklist.md)：内容仓发布前自检清单。

## 当前公开仓核心结构

```text
.
├─ README.md
├─ assets/
├─ docs/
├─ governance/
└─ packs/
```

其中：

- `README.md`：读者入口。
- `assets/`：README 等公开页面使用的图片资源。
- `docs/`：公开文档正文。
- `governance/`：当前目录，公开治理说明。
- `packs/`：现成方案的可下载/可安装落地包。

## 当前 docs 正式模块目录

当前 docs 正式模块目录固定为：

- `docs/00-文档总览.md`
- `docs/01-从这开始/`
- `docs/02-现成方案/`
- `docs/03-国内落地/`
- `docs/04-从OpenClaw过来/`
- `docs/05-遇到问题/`
- `docs/06-reference/`

旧英文目录名（如 `start-here` / `solutions` / `china` / `migrate` / `issues` / `reference`）只视为历史命名，不再作为当前正式路径口径。

## 当前治理边界

### 本目录应该记录

- 当前真实公开结构。
- 页面来源与模块映射。
- 内容仓与独立站之间的 route-map 合同。
- docs 与 packs 的公开映射。
- 发布前维护者自检项。

### 本目录不应该记录

- 内部 PM 派单。
- 内部阶段 checklist。
- runtime / dispatch log。
- 巡查脚本和执行控制脚本。
- 只服务内部团队协作的临时研究记录。

## 维护顺序

如果你要改内容仓，建议按这个顺序检查：

1. 先看 [`repo-policy.md`](./repo-policy.md)，确认内容是否应该进公开仓。
2. 再看 [`repo-structure.md`](./repo-structure.md)，确认应该放在哪个目录。
3. 如果新增 docs 页面，更新 [`site-route-map.yaml`](./site-route-map.yaml)。
4. 如果新增或调整方案包，更新 [`packs-map.md`](./packs-map.md)。
5. 发布前按 [`publishing-checklist.md`](./publishing-checklist.md) 自检。

## 一句话规则

治理目录只保留公开仓真正需要的结构、合同、映射和检查清单；内部执行节拍和控制资产不进入内容仓。