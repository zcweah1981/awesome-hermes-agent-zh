# 官方来源同步 Registry

更新时间：2026-05-02

## 目标

这份 registry 定义 Hermes 中文内容仓在做“官方来源同步”时，哪些来源可以作为依据、哪些只能作为参考，以及 R2 国内模型 / 部署页面需要补哪些官方来源确认。

一句话规则：

> 所有会影响用户操作的技术说法，必须能追溯到官方来源或本仓真实内容；不能用旧经验、截图、二手文章直接改正式文档。

## 来源层级

| 层级 | 作用 | 能否覆盖本仓内容 | 使用边界 |
|---|---|---:|---|
| 官方来源 | Hermes Agent 官方文档、官方 GitHub | 可以 | 用于确认 Hermes 本体行为、安装、配置、CLI、Tools、Skills、MCP、Gateway、发布变化 |
| 厂商官方来源 | 云厂商 / 模型厂商官方文档 | 可以 | 用于确认国内模型、endpoint、计费口径、控制台路径、部署产品名 |
| 本仓内容 | docs、packs、route map、governance | 是中文站当前真相源 | 用于保持中文用户路径、站内链接和独立站消费协议 |
| 二级参考 | 社区文章、截图、历史笔记、实验结果 | 不可以 | 只能发现问题或辅助理解，不能直接变成公开结论 |

## 当前已登记来源

| ID | 来源 | URL | 状态 | 用途 |
|---|---|---|---|---|
| `hermes-official-docs` | Hermes Agent 官方文档 | <https://hermes-agent.nousresearch.com/docs> | 2026-05-02 可访问 | Hermes 本体行为、安装、配置、CLI、Tools、Skills、MCP、Gateway、自动化 |
| `hermes-official-github` | NousResearch/hermes-agent GitHub | <https://github.com/NousResearch/hermes-agent> | 2026-05-02 可访问 | release、README、examples、源码级确认 |
| `content-repo` | awesome-hermes-agent-zh 内容仓 | <https://github.com/zcweah1981/awesome-hermes-agent-zh> | 本仓 SSoT | 中文内容、packs、route map、公开治理 |
| `site-repo` | hermes-zh 独立站代码仓 | <https://github.com/zcweah1981/hermes-zh> | 渲染消费方 | 渲染、搜索、SEO、部署，不作为第二内容源 |

机器可读版本见：[`upstream-source-registry.yaml`](./upstream-source-registry.yaml)。

## R2 待补官方来源

R2 进入国内模型 / 部署内容更新前，必须先把以下页面对应的厂商官方来源补齐到工作记录中；如果来源稳定，也可以回写到 `upstream-source-registry.yaml`。

### 国内模型

| 页面方向 | 当前页面 | 需要确认 |
|---|---|---|
| 阿里云百炼 | `docs/03-国内落地/02-国内模型/02-阿里云百炼Token plan.md` | 官方模型控制台、API / OpenAI 兼容说明、套餐 / token 说明 |
| 腾讯云 | `docs/03-国内落地/02-国内模型/03-腾讯云Token Plan.md` | 腾讯云模型产品官方入口、鉴权、兼容接口、计费说明 |
| 智谱 GLM | `docs/03-国内落地/02-国内模型/04-智谱GLM Coding Plan.md` | 智谱开放平台官方模型、API、计费、适合编码场景的真实说明 |
| MiniMax | `docs/03-国内落地/02-国内模型/05-MiniMax Token Plan.md` | MiniMax 官方模型、API、计费和上下文能力说明 |
| Kimi / Moonshot | `docs/03-国内落地/02-国内模型/06-Kimi登月计划.md` | Moonshot / Kimi 官方 API、计费、模型能力说明 |
| DeepSeek | `docs/03-国内落地/02-国内模型/07-DeepSeek按量计费接口.md` | DeepSeek 官方 API、模型名、计费、兼容接口说明 |
| 自定义兼容接口 | `docs/03-国内落地/02-国内模型/08-自定义兼容接口.md` | Hermes 官方 provider / OpenAI-compatible 配置口径 + 兼容层约束；route-map 暂用 `custom-openai-compatible-provider` 标记 R2 待确认 |

### 国内部署

| 页面方向 | 当前页面 | 需要确认 |
|---|---|---|
| 阿里云轻量服务器 | `docs/03-国内落地/01-国内部署/02-阿里云轻量服务器部署教程.md` | 产品名、系统镜像、端口、安全组、防火墙、重装 / SSH 入口 |
| 腾讯云轻量服务器 | `docs/03-国内落地/01-国内部署/03-腾讯云轻量服务器部署教程.md` | 产品名、系统镜像、端口、安全组、防火墙、重装 / SSH 入口 |

## 每次同步必须记录什么

当某个文档因为官方来源发生变化而更新时，提交说明或工作记录至少写清：

- source ID 或官方 URL
- checked_at 日期
- 影响的 docs 路径
- 变更类型：新增 / 修正 / 删除 / 标记待确认
- 是否影响独立站路由、packs 或搜索摘要

## 不允许写入 registry 的内容

- API Key、Token、cookie、session、控制台截图中的敏感值
- 内部 dispatch / proof / runtime 日志
- 未验证价格、额度、模型能力承诺
- 只来自二手文章的结论

## 给下游的说明

- Content 更新国内模型 / 部署页时，先查本 registry 和官方来源，再改正文。
- Dev / Site loader 不消费本 Markdown 文件；如果需要机器读取，使用 `upstream-source-registry.yaml`。
- Ops / SEO 如需提交搜索或监控 proof，不把平台凭据写入本文件。
