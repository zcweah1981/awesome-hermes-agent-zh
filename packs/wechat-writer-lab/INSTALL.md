# wechat-writer-lab 下载与安装说明

> 这个包不是只给你看写作建议，而是让你先把一个主题压成“能继续润、能继续发”的公众号文章草稿。

---

## 👀 这个包会帮你产出什么

跑完后，你最少应该拿到：
- 文章切口
- 标题候选
- 文章大纲
- 导语与正文初稿
- 小标题 / 配图建议
- 结尾 CTA
- 发布检查单

---

## 📦 包里有什么

当前提供：
- `02-team/`：团队协作版，拆成选题 / 初稿 / 编辑 / 审校 / 总体验收
- `02-team.zip`：团队协作版打包版本
- `01-super-individual/`：一个 Agent 先帮你把一篇公众号文章压成可继续润色的草稿
- `01-super-individual.zip`：可直接下载的打包版本

---

## ⚡ 最短用法

```bash
git clone git@github.com:zcweah1981/awesome-hermes-agent-zh.git
cd awesome-hermes-agent-zh/packs/wechat-writer-lab/01-super-individual
hermes profile create gzh-solo --clone
bash ./install_to_profile.sh gzh-solo
hermes -p gzh-solo chat --skills wechat-official-account-writer -q "$(cat skills/solutions/wechat-official-account-writer/examples/sample-input.md)"
```

---

## ✅ 跑完后你重点看什么

不要只看它有没有分析，重点看这 5 件事：
- 有没有先定清楚这篇文章的切口
- 有没有给多个标题备选
- 有没有把大纲、导语、正文初稿写出来
- 有没有补结尾 CTA 和配图建议
- 有没有给发前检查单和下一轮续跑句子

---

## 🤝 如果你要直接走团队协作版

如果你已经不是一个人单独写文章，而是想按角色接力推进，直接进入 `02-team/` 或下载 `02-team.zip`。

最短入口：
- 阅读团队包说明：`02-team/README.md`
- 或直接进入：`02-team/`
- 或直接下载：`02-team.zip`
