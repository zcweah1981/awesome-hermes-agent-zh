# multi-platform-rewrite-lab 下载与安装说明

> 这个包不是只给你看改写建议，而是让你先把一篇已有内容，直接改成适配小红书、公众号、X/Twitter 等不同平台风格的可发布稿件。

---

## 👀 这个包会帮你产出什么

跑完后，你最少应该拿到：
- 小红书版本（标题带 emoji、正文口语化、末尾带话题标签）
- 公众号版本（深度完整、小标题清晰、引导关注）
- X/Twitter 版本（精炼犀利、拆成 1-3 条推文）
- 每个版本都是可以直接复制发布的完整稿件

---

## 📦 包里有什么

当前提供：
- `01-super-individual/`：一个 Agent 先帮你把一篇原文改成多平台可发布稿件
- `01-super-individual.zip`：可直接下载的打包版本

注意：
- 这一套内容创作包当前只保留 **超级个体版**
- 不提供 `02-team/` 团队协作版

---

## ⚡ 最短用法

```bash
git clone git@github.com:zcweah1981/awesome-hermes-agent-zh.git
cd awesome-hermes-agent-zh/packs/multi-platform-rewrite-lab/01-super-individual
hermes profile create multi-platform-solo --clone
bash ./install_to_profile.sh multi-platform-solo
hermes -p multi-platform-solo chat --skills multi-platform-rewrite-assistant -q "$(cat skills/solutions/multi-platform-rewrite-assistant/examples/sample-input.md)"
```

---

## ✅ 跑完后你重点看什么

不要只看它有没有出改写，重点看这 5 件事：
- 有没有把原文核心信息保留住
- 小红书版本有没有 emoji、话题标签和口语感
- X 推文够不够精炼，能不能直接发
- 每个版本复制粘贴到对应平台，格式是否正常
- 有没有给下一轮继续微调各平台版本的方向
