# 01-super-individual 安装说明

> 这个包适合：你先把一天的工作压成一版可发送、可跟进的项目日报，不先上来做复杂协作流程。

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

## ⚡ 最短用法

### 1）安装
```bash
bash ./install_to_profile.sh <profile-name-or-path>
```

### 2）直接试跑
```bash
hermes -p <your-profile> chat --skills daily-report-assistant -q "$(cat skills/solutions/daily-report-assistant/examples/sample-input.md)"
```

---

## ✅ 跑完后你重点看什么

不要只看它有没有出摘要，重点看这 4 件事：
- 有没有把完成、进行中、阻塞、明日计划分开
- 有没有把重点结果讲清楚
- 有没有给可发送版日报正文
- 有没有把会后跟进动作补上
