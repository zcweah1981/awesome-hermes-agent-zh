# Team Basic Starter

这是从单 Agent 过渡到基础多角色协作的 starter。

如果你已经不满足于“一个 Agent 做完所有事情”，但也不想一上来搭很重的团队系统，这个模板就是最稳的下一步。

---

## 适合谁

- 已经跑通过单 Agent 的用户
- 想尝试基础多 Agent 协作的团队
- 需要最简单的任务拆解、执行、校验闭环的人

---

## 模板包含什么

当前目录包含：
- [`config.yaml`](./config.yaml)：主控配置
- [`system_prompt.txt`](./system_prompt.txt)：主控角色 prompt
- [`coder_system.txt`](./coder_system.txt)：执行角色 prompt
- [`qa_system.txt`](./qa_system.txt)：校验角色 prompt

说明：
- 这是一个轻量多角色模板
- 目标不是做完整企业级编排
- 而是先让你体验“拆任务 → 执行 → 校验”的基本闭环

---

## 如何启动

### 1. 先确保你已完成基础安装
建议先看：
- [快速开始](../../docs/quick-start.md)
- [模型与 Provider](../../docs/models.md)

### 2. 配置模型密钥
建议把密钥放在本机 `~/.hermes/.env` 中，例如：
```bash
DEEPSEEK_API_KEY=***
```

### 3. 在当前目录启动
```bash
hermes --config config.yaml
```

### 4. 下达一个基础协作任务
例如：
- 帮我写一个 Python 小工具，然后让 QA 检查输出结果
- 帮我整理一个脚本方案，并校验潜在风险

---

## 适用场景

适合：
- 轻量研发协作
- 代码生成 + 基础校验
- 小团队的最小分工验证
- 从单 Agent 向多 Agent 升级

不适合：
- 复杂 reviewer 流程
- 严格代码审计流程
- 大型团队编排

---

## 推荐下一步

- 想看更完整的开发流：看 [advanced-coding-team](../advanced-coding-team/README.md)
- 想看 starter 总览：看 [Starter 模板索引](../../docs/starters/index.md)
- 想理解多 Agent 场景：看 [多 Agent 协作](../../docs/team-flow.md)
