# summary-lab 下载与安装说明

> 这个包不是只给你看摘要建议，而是让你先把一批散资料压成“可发送、可判断、可继续补”的结构化总结。

---

## 👀 这个包会帮你产出什么

跑完后，你最少应该拿到：
- 背景摘要
- 核心结论
- 关键信息保留项
- 待确认项
- 建议动作
- 发送版总结正文

---

## 📦 包里有什么

当前提供：
- `01-super-individual/`：一个 Agent 先帮你把一批资料压成可发送总结
- `01-super-individual.zip`：可直接下载的打包版本

注意：
- 这一套办公效率包当前只保留 **超级个体版**
- 不提供 `02-team/` 团队协作版

---

## ⚡ 最短用法

```bash
git clone git@github.com:zcweah1981/awesome-hermes-agent-zh.git
cd awesome-hermes-agent-zh/packs/summary-lab/01-super-individual
hermes profile create summary-solo --clone
bash ./install_to_profile.sh summary-solo
hermes -p summary-solo chat --skills material-summary-assistant -q "$(cat skills/solutions/material-summary-assistant/examples/sample-input.md)"
```

---

## ✅ 跑完后你重点看什么

不要只看它有没有出摘要，重点看这 5 件事：
- 有没有把背景、结论、保留项、待确认项分开
- 有没有明确哪些才是真正重点
- 有没有把建议动作讲清楚
- 有没有给可发送版总结正文
- 有没有给下一轮继续补决策版总结的方向
