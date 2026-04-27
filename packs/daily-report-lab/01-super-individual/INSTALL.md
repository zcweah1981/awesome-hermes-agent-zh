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

### 1）创建默认 profile
```bash
hermes profile create daily-report-solo --clone
```

### 2）安装
```bash
bash ./install_to_profile.sh daily-report-solo
```

### 3）直接试跑
```bash
hermes -p daily-report-solo chat --skills daily-report-assistant -q "$(cat skills/solutions/daily-report-assistant/examples/sample-input.md)"
```

说明：
- 页面默认示例 profile 名就是 `daily-report-solo`
- 如果你想换 profile 名，也可以把上面三条命令里的 `daily-report-solo` 换成你自己的名字

---

## ✅ 跑完后你重点看什么

不要只看它有没有出摘要，重点看这 5 件事：
- 有没有把摘要、完成、进行中、阻塞、明日计划分开
- 有没有明确哪些是真的完成了
- 有没有把阻塞和需要协助的地方讲清楚
- 有没有给可发送版日报正文
- 有没有给下一轮继续补管理者版日报的方向
