# 99-solution-validator 安装说明

默认 skill：`solution-validator-ppt`

## 这个角色是干什么的
- 这个角色负责：给出 pass / pass with fixes / fail 的最终结论
- 默认 profile 名：`ppt-validator`
- 这是终点棒，不再往下交接

## 最短安装
```bash
bash ./install_to_profile.sh ppt-validator
```

## 最短运行
```bash
hermes -p ppt-validator chat --skills solution-validator-ppt -q "$(cat skills/solutions/solution-validator-ppt/examples/sample-input.md)"
```

## 跑完后先看什么
- 输出是不是已经完成这个角色该负责的那一段
- 是否已经产出能交给下一棒的明确交接物
- 如果还没压清楚，不要急着继续往下一棒走
