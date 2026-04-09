# Advanced Coding Team Starter

这是面向开发场景的进阶团队 starter。

如果你的目标已经不是“先跑起来”，而是搭一个更接近真实研发流程的多角色协作结构，这个模板更适合你。

---

## 适合谁

- 想做代码工作流的开发者
- 需要 PM / Coder / Reviewer 基础分工的人
- 想把 Hermes 用到更完整研发流程里的团队

---

## 模板包含什么

当前目录包含：
- [`config.yaml`](./config.yaml)：团队编排配置
- [`README.md`](./README.md)：当前模板说明
- [`reviewer_system.txt`](./reviewer_system.txt)：Reviewer 角色 prompt

注意：
- 当前配置里引用了 `system_prompt.txt` 和 `coder_system.txt`
- 但这两个文件目前并不在该目录中
- 这意味着这个 starter 还需要补齐对应 prompt 文件，或在后续执行中调整配置引用

这是当前模板已确认的缺口，我会在后续任务中继续修正，不会假装它已经完整。

---

## 如何启动

### 1. 先完成基础安装与模型配置
建议先看：
- [快速开始](../../docs/quick-start.md)
- [模型与 Provider](../../docs/models.md)

### 2. 准备 API Key
建议写入本机 `~/.hermes/.env`：
```bash
DEEPSEEK_API_KEY=***
```

### 3. 启动前先校验模板文件
由于当前目录仍缺少部分 prompt 文件，建议先确认：
- `system_prompt.txt` 是否已补齐
- `coder_system.txt` 是否已补齐
- 配置引用是否和真实文件一致

然后再执行：
```bash
hermes --config config.yaml
```

---

## 适用场景

适合：
- 需求拆解 → 代码实现 → 结果审查
- 小型代码项目协作
- 想把 reviewer 角色纳入流程的团队

不适合：
- 只想快速跑第一个单 Agent 版本
- 只做轻量问答或简单脚本任务

---

## 推荐下一步

- 想看更轻量版本：看 [team-basic](../team-basic/README.md)
- 想看 starter 总览：看 [Starter 模板索引](../../docs/starters/index.md)
- 想看案例：看 [示例项目](../../docs/examples/index.md)
