# 02-drafter 安装说明

默认 skill：`xiaohongshu-drafter`

## 这个角色是干什么的
- 这个角色负责：把开头、正文底稿和分页建议写出来
- 默认 profile 名：`xhs-draft`
- 下一棒默认交给 xhs-polish

## 最短安装
```bash
bash ./install_to_profile.sh xhs-draft
```

## 最短运行
```bash
hermes -p xhs-draft chat --skills xiaohongshu-drafter -q "$(cat skills/solutions/xiaohongshu-drafter/examples/sample-input.md)"
```

## 跑完后先看什么
- 输出是不是已经完成这个角色该负责的那一段
- 是否已经产出能交给下一棒的明确交接物
- 如果还没压清楚，不要急着继续往下一棒走
