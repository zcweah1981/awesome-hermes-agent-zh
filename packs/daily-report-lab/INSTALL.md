# daily-report-lab 下载与安装说明

> 这个包不是只给你看总结建议，而是让你先把一天的零散进展压成“可发送、可跟进”的项目日报。

---

## 👀 这个包会帮你产出什么

跑完后，你最少应该拿到：
- 今日摘要
- 完成事项
- 进行中事项
- 阻塞 / 风险
- 明日计划
- 发送版日报正文

---

## 📦 包里有什么

当前提供：
- `01-super-individual/`：一个 Agent 先帮你把一天进展压成可发送日报
- `01-super-individual.zip`：可直接下载的打包版本

注意：
- 这一套办公效率包当前只保留 **超级个体版**
- 不提供 `02-team/` 团队协作版

---

## ⚡ 最短用法

```bash
git clone git@github.com:zcweah1981/awesome-hermes-agent-zh.git
cd awesome-hermes-agent-zh/packs/daily-report-lab/01-super-individual
hermes profile create daily-report-solo --clone
bash ./install_to_profile.sh daily-report-solo
hermes -p daily-report-solo chat --skills daily-report-assistant -q "$(cat skills/solutions/daily-report-assistant/examples/sample-input.md)"
```

---

## ✅ 跑完后你重点看什么

不要只看它有没有出摘要，重点看这 5 件事：
- 有没有把摘要、完成、进行中、阻塞、明日计划分开
- 有没有明确哪些是真的完成了
- 有没有把阻塞和需要协助的地方讲清楚
- 有没有给可发送版日报正文
- 有没有给下一轮继续补管理者版日报的方向
