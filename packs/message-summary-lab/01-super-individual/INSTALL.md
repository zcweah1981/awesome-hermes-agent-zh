# 01-super-individual 安装说明

> 这个包适合：你先把一封长邮件或一堆群消息压成一版可转发、可同步的结构化摘要，不先上来做复杂协作流程。

---

## 👀 这个包会帮你产出什么

跑完后，你最少应该拿到：
- 核心结论（到底在说什么）
- 待办事项（有没有要你做的）
- 关键时间点（截止日期、会议时间等）
- 需要关注的风险或变更
- 一段可以直接转发的发送版摘要

---

## ⚡ 最短用法

### 1）创建默认 profile
```bash
hermes profile create message-summary-solo --clone
```

### 2）安装
```bash
bash ./install_to_profile.sh message-summary-solo
```

### 3）直接试跑
```bash
hermes -p message-summary-solo chat --skills message-summary-assistant -q "$(cat skills/solutions/message-summary-assistant/examples/sample-input.md)"
```

说明：
- 页面默认示例 profile 名就是 `message-summary-solo`
- 如果你想换 profile 名，也可以把上面三条命令里的 `message-summary-solo` 换成你自己的名字

---

## ✅ 跑完后你重点看什么

不要只看它有没有出摘要，重点看这 5 件事：
- 有没有把核心结论、待办、时间点分开
- 有没有明确标注负责人
- 有没有把闲聊和关键信息区分开
- 有没有给可转发版摘要正文
- 有没有给下一轮继续补方向
