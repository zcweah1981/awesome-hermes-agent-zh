# 模型与 provider 问题

当 Hermes 已经安装完成，但模型不可用、provider 不生效，或者你不确定该使用官方 provider 还是 custom endpoint 时，优先看本页。

## 问题现象

你可能会看到以下现象之一：
- 已配置模型，但运行时提示模型不可用
- 已设置 provider，但命令仍走到错误的上游
- 模型名填写后无法匹配
- 不清楚 `config.yaml`、`.env`、`auth.json` 分别该放什么
- 一开始就走 custom OpenAI-Compatible，结果排障难度迅速升高

## 可能原因

- provider 选择不当，官方支持路径与自定义接入路径混用
- 模型名、provider 名、endpoint 配置三者不匹配
- 把认证信息、默认模型、环境变量职责写混了
- 在尚未跑通官方路径前就过早引入 custom `base_url`
- 当前问题本质是网络或部署问题，却被误判为模型问题

## 优先排查步骤

1. 先确认你是否真的需要 custom OpenAI-Compatible；如果不是，优先回到官方 provider 路线
2. 核对 provider 名、模型名、认证方式是否来自同一条配置链路
3. 区分清楚默认配置与鉴权配置，避免把所有内容都堆到单一文件
4. 使用最小命令验证单个 provider / model 是否可用，再扩大到完整工作流
5. 若错误表现更像超时、SSL 或代理异常，转到部署与连接页继续排查

## 最终解决办法

### 优先使用官方 provider
如果你的目标只是先跑通，请优先使用官方支持的 provider 和模型组合，不要在第一步就引入自定义兼容层。

### 分层检查配置职责
- `config.yaml`：适合放默认 provider、模型选择与结构化配置
- `.env`：适合放环境变量型配置
- `auth.json`：适合放认证相关信息

先把职责拆开，再验证是否生效，能显著降低“看起来都配了但实际没生效”的概率。

### custom endpoint 只在明确需要时引入
只有在官方支持路径不满足你当前场景时，再引入自定义 `base_url` 或 OpenAI-Compatible 接入；否则先保证可复现的最短成功闭环。

## 证据来源

- Hermes Agent 中文站现有模型与接入页面：`docs/models.md`、`docs/custom-openai-compatible.md`
- RM5 研究链路中对 provider / 模型 / 配置分层的收敛结论
- RM5 Method Pack 对模型类问题页结构的冻结要求

## 相关延伸

- [遇到问题总览](./index.md)
- [安装与环境问题](./install.md)
- [部署与连接问题](./deploy.md)
- [国内落地](../china/index.md)
