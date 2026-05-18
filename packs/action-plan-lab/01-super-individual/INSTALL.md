# 01-super-individual 安装说明

> 这个包适合：你先把一个目标、会议结论或讨论结果压成一版可执行、可发送的行动计划表，不先上来做复杂协作流程。

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

## ⚡ 最短用法

### 1）创建默认 profile
```bash
hermes profile create action-plan-solo --clone
```

### 2）安装
```bash
bash ./install_to_profile.sh action-plan-solo
```

### 3）直接试跑
```bash
hermes -p action-plan-solo chat --skills action-plan-assistant -q "$(cat skills/solutions/action-plan-assistant/examples/sample-input.md)"
```

说明：
- 页面默认示例 profile 名就是 `action-plan-solo`
- 如果你想换 profile 名，也可以把上面三条命令里的 `action-plan-solo` 换成你自己的名字

---

## ✅ 跑完后你重点看什么

不要只看它有没有出计划，重点看这 5 件事：
- 有没有把目标、动作项、负责人、截止时间分开
- 有没有明确优先级和依赖关系
- 有没有把已决策和待确认区分开
- 有没有给可发送版行动计划正文
- 有没有给下一轮继续补执行动作的方向
