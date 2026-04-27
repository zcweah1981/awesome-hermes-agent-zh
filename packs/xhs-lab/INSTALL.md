# xhs-lab 下载与安装说明

> 这个包不是只给你看内容建议，而是让你先把一个主题压成“今天就能发”的小红书内容包。

---

## 👀 这个包会帮你产出什么

跑完后，你最少应该拿到：
- 选题角度
- 标题候选
- 开头钩子
- 正文底稿
- 封面短句 / 配图提示
- 评论区引导句
- 发布检查单

---

## 📦 包里有什么

当前提供：
- `02-team/`：团队协作版，拆成选题 / 初稿 / 润色 / 审校 / 总体验收
- `02-team.zip`：团队协作版打包版本
- `01-super-individual/`：一个 Agent 先帮你把一篇内容压成可发布底稿
- `01-super-individual.zip`：可直接下载的打包版本

---

## ⚡ 最短用法

```bash
git clone git@github.com:zcweah1981/awesome-hermes-agent-zh.git
cd awesome-hermes-agent-zh/packs/xhs-lab/01-super-individual
hermes profile create xhs-solo --clone
bash ./install_to_profile.sh xhs-solo
hermes -p xhs-solo chat --skills xiaohongshu-content-assistant -q "$(cat skills/solutions/xiaohongshu-content-assistant/examples/sample-input.md)"
```

---

## ✅ 跑完后你重点看什么

不要只看它有没有分析，重点看这 5 件事：
- 有没有先定清楚这篇内容的角度
- 有没有给多个标题备选
- 有没有把开头和正文底稿写出来
- 有没有补封面短句和评论区引导
- 有没有给发前检查单和下一轮续跑句子

---

## 🤝 如果你要直接走团队协作版

如果你已经不是一个人单独出稿，而是想按角色接力推进，直接进入 `02-team/` 或下载 `02-team.zip`。

最短入口：
- 阅读团队包说明：`02-team/README.md`
- 或直接进入：`02-team/`
- 或直接下载：`02-team.zip`
