# Single Agent Starter

这是最适合从 0 到 1 起步的 Hermes Starter。

如果你现在的目标是：
- 先把 Hermes 跑起来
- 先验证一个模型可用
- 先拥有一个最小可改造骨架

那就先从这个模板开始。

---

## 适合谁

- 第一次使用 Hermes 的个人开发者
- 想先做单 Agent 助手的人
- 想用最少配置跑通第一个可用版本的人

---

## 模板包含什么

当前目录包含：
- [`config.yaml`](./config.yaml)：最小可运行配置
- [`system_prompt.txt`](./system_prompt.txt)：单 Agent 的基础 system prompt

说明：
- 这个 starter 故意保持很小
- 不包含复杂团队编排
- 不包含多角色协作
- 适合你先跑通，再按自己的项目需求扩展

---

## 如何启动

### 1. 先完成基础安装
先看：
- [快速开始](../../docs/quick-start.md)
- [模型与 Provider](../../docs/models.md)

### 2. 配置 API Key
建议把密钥放在你本机的 `~/.hermes/.env`，而不是直接写进仓库文件。

例如：
```bash
DEEPSEEK_API_KEY=***
```

说明：
- 当前模板里的 `config.yaml` 仍然展示了最小结构
- 实际使用时，建议你优先走官方 provider 路径，而不是把 custom 配置继续当默认答案

### 3. 启动 Hermes
在当前目录执行：
```bash
hermes --config config.yaml
```

---

## 适用场景

适合：
- 第一个 Hermes 项目
- 个人助手
- 单任务执行器
- 用来搭你自己的最小项目骨架

不适合：
- 一开始就做多 Agent 协作
- 一开始就做完整代码团队流
- 需要 reviewer / QA / PM 分工的场景

---

## 推荐下一步

- 想继续升级到基础协作：看 [team-basic](../team-basic/README.md)
- 想看 starter 总览：看 [Starter 模板索引](../../docs/starters/index.md)
- 想看案例：看 [示例项目](../../docs/examples/index.md)
