# 02-slide-writer 安装说明

默认 skill：`ppt-slide-writer`

## 这个角色是干什么的
- 这个角色负责：把每页标题、要点和图表建议写出来
- 默认 profile 名：`ppt-slidewriter`
- 下一棒默认交给 ppt-polish

## 最短安装
```bash
bash ./install_to_profile.sh ppt-slidewriter
```

## 最短运行
```bash
hermes -p ppt-slidewriter chat --skills ppt-slide-writer -q "$(cat skills/solutions/ppt-slide-writer/examples/sample-input.md)"
```

## 跑完后先看什么
- 输出是不是已经完成这个角色该负责的那一段
- 是否已经产出能交给下一棒的明确交接物
- 如果还没压清楚，不要急着继续往下一棒走
