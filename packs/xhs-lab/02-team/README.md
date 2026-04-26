# 团队协作版

> 这个包适合：已经不是一个人单独出稿，而是想把工作拆成接力流程。

---

## 👀 这里面有谁

- `01-topic-strategist/`：你是小红书选题与角度负责人
- `02-drafter/`：你是小红书初稿写手
- `03-polisher/`：你是小红书润稿负责人
- `04-review/`：你是小红书审校负责人
- `99-solution-validator/`：你是小红书内容方案总体验收专家

## ⚡ 最短用法

### 1）先创建 5 个 profile
```bash
hermes profile create xhs-strategy --clone
hermes profile create xhs-draft --clone
hermes profile create xhs-polish --clone
hermes profile create xhs-review --clone
hermes profile create xhs-validator --clone
```

### 2）再一键安装
```bash
bash ./install_all.sh
```