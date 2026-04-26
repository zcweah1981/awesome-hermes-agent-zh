# 团队协作版

> 这个包适合：已经不是一个人单独出稿，而是想把工作拆成接力流程。

---

## 👀 这里面有谁

- `01-article-strategist/`：你是公众号选题与结构负责人
- `02-article-writer/`：你是公众号初稿写手
- `03-editor/`：你是公众号编辑负责人
- `04-review/`：你是公众号审校负责人
- `99-solution-validator/`：你是公众号写作方案总体验收专家

## ⚡ 最短用法

### 1）先创建 5 个 profile
```bash
hermes profile create gzh-strategy --clone
hermes profile create gzh-writer --clone
hermes profile create gzh-edit --clone
hermes profile create gzh-review --clone
hermes profile create gzh-validator --clone
```

### 2）再一键安装
```bash
bash ./install_all.sh
```