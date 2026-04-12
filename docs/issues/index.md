# 遇到问题

当你已经开始安装、配置或部署 Hermes Agent，却在某一步卡住时，先从这里进入，而不是直接在仓库里盲搜关键词。

RM5 的目标不是继续维护一篇不断膨胀的旧版 FAQ，而是把高频问题按类别拆成可持续追加的问题库。当前首批已落仓 3 个专题页：安装与环境、模型与 provider、部署与连接。

## 怎么用这个入口

1. 先按你当前卡住的阶段进入对应专题页
2. 先看“问题现象”，确认是否是同一类故障
3. 按“优先排查步骤”逐项检查，不要一上来就重装
4. 确认修复后，再看“相关延伸”判断是否需要进一步调整配置

## 当前专题页

- [安装与环境问题](./install.md) —— 安装脚本、依赖缺失、权限、Python/终端环境
- [模型与 provider 问题](./models.md) —— provider 选择、模型名不匹配、配置分层、custom endpoint 兼容
- [部署与连接问题](./deploy.md) —— SSL、代理、超时、base_url、发布后连接异常

## 常见问题速查

### 安装阶段卡住
优先看：[安装与环境问题](./install.md)

适用场景：
- 安装脚本执行失败
- 缺少 Pillow / PIL 等依赖
- `~/.hermes` 目录不可写
- 终端环境、Python 环境或权限不一致

### 模型配置后仍不可用
优先看：[模型与 provider 问题](./models.md)

适用场景：
- 模型名存在但调用失败
- provider 已配置却没有生效
- `config.yaml`、`.env`、`auth.json` 的职责混淆
- 不确定该先用官方 provider 还是 custom OpenAI-Compatible

### 部署或联网后异常
优先看：[部署与连接问题](./deploy.md)

适用场景：
- SSL 证书校验失败
- 请求超时或连接不上上游
- 代理设置后行为异常
- 自定义 `base_url` 或 endpoint 后返回错误

## 下一批页面

以下类别已冻结为正式目录口径，但本轮只登记，不扩范围：
- webui —— 网页端、浏览器、前端可见性与交互问题
- migration —— 从旧入口、旧文档或 OpenClaw 迁移时的映射与兼容问题

## 旧版参考页

- [legacy：常见问题与排障指南](../known-issues.md)

`docs/known-issues.md` 仍保留作为过渡参考页，用于承接旧链接与已有聚合内容；但从本页开始，RM5 的正式主入口已经切换到 `docs/issues/index.md`。

## 相关延伸

- [从这开始](../start/index.md)
- [国内落地](../china/index.md)
- [从 OpenClaw 过来](../openclaw-migration.md)
- [正式页面来源映射](../governance/page-source-map.md)
