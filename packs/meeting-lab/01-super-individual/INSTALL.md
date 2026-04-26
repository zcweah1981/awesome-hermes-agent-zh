# 01-super-individual 安装说明

> 这个包适合：你先把一场会议压成一版可发送、可执行的会议纪要，不先上来做复杂协作流程。

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

## ⚡ 最短用法

### 1）安装
```bash
bash ./install_to_profile.sh <profile-name-or-path>
```

### 2）直接试跑
```bash
hermes -p <your-profile> chat --skills meeting-minutes-assistant -q "$(cat skills/solutions/meeting-minutes-assistant/examples/sample-input.md)"
```

---

## ✅ 跑完后你重点看什么

不要只看它有没有出总结，重点看这 4 件事：
- 有没有把背景、结论、待办、未决分开
- 有没有补 owner 和截止时间
- 有没有给可发送版纪要正文
- 有没有把会后动作补上
