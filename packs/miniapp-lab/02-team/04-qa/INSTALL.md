# 04-qa 安装说明

默认 skill：`wechat-mini-program-qa-agent`

## 这个角色是干什么的
- 这个角色负责：把检查项、风险点和是否能开工的判断压清楚
- 默认 profile 名：`miniapp-qa`
- 下一棒默认交给 miniapp-validator

## 最短安装
```bash
bash ./install_to_profile.sh miniapp-qa
```

## 最短运行
```bash
hermes -p miniapp-qa chat --skills wechat-mini-program-qa-agent -q "$(cat skills/solutions/01-微信小程序/wechat-mini-program-qa-agent/examples/sample-input.md)"
```

## 跑完后先看什么
- 输出是不是已经完成这个角色该负责的那一段
- 是否已经产出能交给下一棒的明确交接物
- 如果还没压清楚，不要急着继续往下一棒走
