# meeting-lab 下载与安装说明

> 这个包不是只给你看总结建议，而是让你先把一场会议压成“可发送、可执行”的会议纪要。

---

## 👀 这个包会帮你产出什么

跑完后，你最少应该拿到：
- 会议背景摘要
- 核心结论
- 已决策事项
- 待办动作表
- 未决问题清单
- 发送版纪要正文

---

## 📦 包里有什么

当前提供：
- `01-super-individual/`：一个 Agent 先帮你把一次会议压成可发送纪要
- `01-super-individual.zip`：可直接下载的打包版本

注意：
- 这一套办公效率包当前只保留 **超级个体版**
- 不提供 `02-team/` 团队协作版

---

## ⚡ 最短用法

```bash
git clone git@github.com:zcweah1981/awesome-hermes-agent-zh.git
cd awesome-hermes-agent-zh/packs/meeting-lab/01-super-individual
hermes profile create meeting-solo --clone
bash ./install_to_profile.sh meeting-solo
hermes -p meeting-solo chat --skills meeting-minutes-assistant -q "$(cat skills/solutions/meeting-minutes-assistant/examples/sample-input.md)"
```

---

## ✅ 跑完后你重点看什么

不要只看它有没有出总结，重点看这 5 件事：
- 有没有把背景、结论、待办、未决分开
- 有没有明确 owner 和截止时间
- 有没有把讨论和定案区分开
- 有没有给可发送版纪要正文
- 有没有给下一轮继续补执行动作的方向
