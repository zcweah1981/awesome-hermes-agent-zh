# Hermes 项目目录组织规范

做 Hermes 项目时，目录结构本身就是效率工具。

这篇的目标不是给你一个“大而全”的规范，而是给你一个够用、可扩展、适合团队交接的组织方式。

---

## 一个够用的最小结构

```text
project/
├── PROJECT.md
├── TASKS.md
├── DECISIONS.md
├── CHANGELOG.md
├── prompts/
├── configs/
├── skills/
└── examples/
```

---

## 每一层为什么存在

### PROJECT.md
记录：
- 项目目标
- 当前范围
- 关键约束

### TASKS.md
记录：
- 要做什么
- 谁负责
- 当前状态

### DECISIONS.md
记录：
- 为什么这样选
- 放弃了哪些方案

### CHANGELOG.md
记录：
- 外部可感知变化
- 每次发布带来了什么

### prompts/
放角色 prompt 或 system prompt。

### configs/
放项目级配置样板。

### skills/
放可复用技能或流程。

---

## 组织原则

- 目录要为交接服务
- 文档要为执行服务
- 不要一开始就设计很重的层级

换句话说：
先够用，再扩展。

---

## 常见错误

### 错误 1：所有内容都堆在 README

README 应该是入口，不是全站数据库。

### 错误 2：角色 prompt 和项目文档混放

建议角色和项目资料分开，便于维护。

---

## 下一步

- 想看项目文件怎么写：看 [Hermes 项目文件编写指南](./project-files-guide.md)
- 想看角色和项目如何拆开：看 [SOUL 管角色，MD 管项目](./soul-md-workflow.md)
