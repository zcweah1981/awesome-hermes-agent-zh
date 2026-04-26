# 团队协作版

> 这个包适合：已经不是一个人单独出稿，而是想把工作拆成接力流程。

---

## 👀 这里面有谁

- `01-structure-planner/`：你是 PPT 结构负责人
- `02-slide-writer/`：你是 PPT 逐页内容写手
- `03-slide-polisher/`：你是 PPT 落版润色负责人
- `04-review/`：你是 PPT 审校负责人
- `99-solution-validator/`：你是 PPT 方案总体验收专家

## ⚡ 最短用法

### 1）先创建 5 个 profile
```bash
hermes profile create ppt-structure --clone
hermes profile create ppt-slidewriter --clone
hermes profile create ppt-polish --clone
hermes profile create ppt-review --clone
hermes profile create ppt-validator --clone
```

### 2）再一键安装
```bash
bash ./install_all.sh
```