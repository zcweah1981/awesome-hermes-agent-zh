# 01-super-individual 安装说明

> 这个包适合：你先把一批散资料压成一版可发送、可判断、可继续补的结构化总结，不先上来做复杂协作流程。

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

## ⚡ 最短用法

### 1）创建默认 profile
```bash
hermes profile create summary-solo --clone
```

### 2）安装
```bash
bash ./install_to_profile.sh summary-solo
```

### 3）直接试跑
```bash
hermes -p summary-solo chat --skills material-summary-assistant -q "$(cat skills/solutions/material-summary-assistant/examples/sample-input.md)"
```

说明：
- 页面默认示例 profile 名就是 `summary-solo`
- 如果你想换 profile 名，也可以把上面三条命令里的 `summary-solo` 换成你自己的名字

---

## ✅ 跑完后你重点看什么

不要只看它有没有出摘要，重点看这 5 件事：
- 有没有把背景、结论、保留项、待确认项分开
- 有没有明确哪些才是真正重点
- 有没有把建议动作讲清楚
- 有没有给可发送版总结正文
- 有没有给下一轮继续补决策版总结的方向
