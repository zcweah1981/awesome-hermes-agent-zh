# Repo Review Example

这个 example 展示的是：让 Hermes 对一个仓库做快速巡检，并产出可以直接转发的 review 结论。

适合的场景包括：
- 上线前做仓库入口检查
- 快速发现文档断层、死链、目录噪音
- 给团队输出一版“哪里还不够专业”的清单

如果你要的是项目骨架，而不是案例，请先看 [Starter 模板](../../docs/starters/index.md)。

---

## 这个示例解决什么问题

很多仓库不是不能用，而是：
- 对外入口不清楚
- README 和文档站割裂
- 目录噪音太多
- 用户不知道先看哪里

这个 example 的目标不是做复杂代码审计，而是做一轮“公开展示层 review”。

---

## 目录结构

- [`config.yaml`](./config.yaml)：示例配置
- [`system_prompt.txt`](./system_prompt.txt)：Repo Review 角色说明
- [`review_checklist.md`](./review_checklist.md)：建议检查项

---

## 如何使用

### 1. 配置模型密钥
建议把密钥写入本机 `~/.hermes/.env`：
```bash
DEEPSEEK_API_KEY=***
```

### 2. 启动 Hermes
```bash
hermes --config config.yaml
```

### 3. 给出 review 目标
例如：
- 帮我检查这个仓库是否适合第一次访问的中文开发者
- 帮我检查 README、docs 首页、examples 是否一致
- 帮我输出上线前还缺什么

---

## 适合谁

- 想快速做仓库入口体检的人
- 想在上线前做公开展示层 review 的团队
- 想避免 repo 看起来像内部半成品的人

---

## 下一步

- 想看更多案例：回到 [示例项目索引](../../docs/examples/index.md)
- 想直接整理自己的目录骨架：看 [Starter 模板](../../docs/starters/index.md)
