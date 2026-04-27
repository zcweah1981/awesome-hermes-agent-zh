# 01-topic-strategist 安装说明

默认 skill：`xiaohongshu-topic-strategist`

## 这个角色是干什么的
- 这个角色负责：先把选题角度、目标读者、标题方向和内容结构压清楚
- 默认 profile 名：`xhs-strategy`
- 下一棒默认交给 xhs-draft

## 最短安装
```bash
bash ./install_to_profile.sh xhs-strategy
```

## 最短运行
```bash
hermes -p xhs-strategy chat --skills xiaohongshu-topic-strategist -q "$(cat skills/solutions/xiaohongshu-topic-strategist/examples/sample-input.md)"
```

## 跑完后先看什么
- 输出是不是已经完成这个角色该负责的那一段
- 是否已经产出能交给下一棒的明确交接物
- 如果还没压清楚，不要急着继续往下一棒走
