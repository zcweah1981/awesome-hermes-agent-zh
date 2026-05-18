# action-plan-lab 下载与安装说明

> 这个包不是只给你看计划建议，而是让你先把一个目标、会议结论或讨论结果，压成"可执行、可发送"的行动计划表。

---

## 👀 这个包会帮你产出什么

跑完后，你最少应该拿到：
- 目标摘要
- 动作项（具体要做什么）
- 负责人（谁来做）
- 截止时间（什么时候交）
- 优先级（先做哪个）
- 依赖关系（哪些动作之间有先后）
- 发送版行动计划正文

---

## 📦 包里有什么

当前提供：
- `01-super-individual/`：一个 Agent 先帮你把一次目标/会议结论压成可执行行动计划表
- `01-super-individual.zip`：可直接下载的打包版本

注意：
- 这一套办公效率包当前只保留 **超级个体版**
- 不提供 `02-team/` 团队协作版

---

## ⚡ 最短用法

```bash
git clone git@github.com:zcweah1981/awesome-hermes-agent-zh.git
cd awesome-hermes-agent-zh/packs/action-plan-lab/01-super-individual
hermes profile create action-plan-solo --clone
bash ./install_to_profile.sh action-plan-solo
hermes -p action-plan-solo chat --skills action-plan-assistant -q "$(cat skills/solutions/action-plan-assistant/examples/sample-input.md)"
```

---

## ✅ 跑完后你重点看什么

不要只看它有没有出计划，重点看这 5 件事：
- 有没有把目标、动作项、负责人、截止时间分开
- 有没有明确优先级和依赖关系
- 有没有把已决策和待确认区分开
- 有没有给可发送版行动计划正文
- 有没有给下一轮继续补执行动作的方向
