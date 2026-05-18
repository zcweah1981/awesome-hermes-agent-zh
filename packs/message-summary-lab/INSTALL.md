# message-summary-lab 下载与安装说明

> 这个包不是只给你看摘要建议，而是让你先把一封长邮件或一堆群消息，压成"能转发、能同步、不用再解释"的结构化摘要。

---

## 👀 这个包会帮你产出什么

跑完后，你最少应该拿到：
- 核心结论（到底在说什么）
- 待办事项（有没有要你做的）
- 关键时间点（截止日期、会议时间等）
- 需要关注的风险或变更
- 一段可以直接转发的发送版摘要

---

## 📦 包里有什么

当前提供：
- `01-super-individual/`：一个 Agent 先帮你把邮件或群消息压成可转发结构化摘要
- `01-super-individual.zip`：可直接下载的打包版本

注意：
- 这一套办公效率包当前只保留 **超级个体版**
- 不提供 `02-team/` 团队协作版

---

## ⚡ 最短用法

```bash
git clone git@github.com:zcweah1981/awesome-hermes-agent-zh.git
cd awesome-hermes-agent-zh/packs/message-summary-lab/01-super-individual
hermes profile create message-summary-solo --clone
bash ./install_to_profile.sh message-summary-solo
hermes -p message-summary-solo chat --skills message-summary-assistant -q "$(cat skills/solutions/message-summary-assistant/examples/sample-input.md)"
```

---

## ✅ 跑完后你重点看什么

不要只看它有没有出摘要，重点看这 5 件事：
- 有没有把核心结论、待办、时间点分开
- 有没有明确标注负责人
- 有没有把闲聊和关键信息区分开
- 有没有给可转发版摘要正文
- 有没有给下一轮继续补方向
