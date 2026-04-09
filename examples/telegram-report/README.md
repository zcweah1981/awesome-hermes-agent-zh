# Telegram Report Example

这个 example 展示的是：让 Hermes 把阶段结果整理成简洁中文汇报，并发送到 Telegram。

它适合两类典型场景：
- 项目日报 / 周报自动发送到群或私聊
- 任务执行完成后自动同步一条进展消息

如果你要的是“从空目录开始搭项目”，请先看 [Starter 模板](../../docs/starters/index.md)。

---

## 这个示例解决什么问题

很多团队已经用 Telegram 做协作，但真正麻烦的不是“发一条消息”，而是：
- 怎么把执行结果整理成可读汇报
- 怎么控制输出格式稳定
- 怎么避免每次都手工复制粘贴

这个 example 提供一个最小闭环：
- 配置模型
- 绑定 Telegram 输出目标
- 用固定 prompt 让 Agent 产出结构化汇报

---

## 目录结构

- [`config.yaml`](./config.yaml)：示例配置
- [`system_prompt.txt`](./system_prompt.txt)：汇报型 Agent 的 system prompt
- [`report_template.md`](./report_template.md)：汇报结构模板

---

## 如何使用

### 1. 准备模型密钥
建议写入本机 `~/.hermes/.env`：
```bash
DEEPSEEK_API_KEY=***
```

### 2. 替换 Telegram 目标
编辑 [`config.yaml`](./config.yaml)，把其中示例 chat id 改成你的目标群或私聊。

### 3. 启动 Hermes
```bash
hermes --config config.yaml
```

### 4. 直接下达汇报型任务
例如：
- 把今天的项目推进情况整理后发到 Telegram
- 把 repo 清理进度发到群里
- 把代码巡检结果整理成简报发送

---

## 适合谁

- 用 Telegram 做项目同步的人
- 想让 Hermes 输出稳定进展汇报的人
- 想要一个最小消息通知闭环的人

---

## 下一步

- 想看更多示例：回到 [示例项目索引](../../docs/examples/index.md)
- 想搭项目骨架：看 [Starter 模板](../../docs/starters/index.md)
