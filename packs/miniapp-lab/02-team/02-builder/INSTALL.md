# 02-builder 安装说明

默认 skill：`wechat-mini-program-builder-agent`

## 这个角色是干什么的
- 这个角色负责：把前端目录骨架、页面文件建议、组件建议和 mock 方案写出来
- 默认 profile 名：`miniapp-builder`
- 下一棒默认交给 miniapp-api

## 最短安装
```bash
bash ./install_to_profile.sh miniapp-builder
```

## 最短运行
```bash
hermes -p miniapp-builder chat --skills wechat-mini-program-builder-agent -q "$(cat skills/solutions/01-微信小程序/wechat-mini-program-builder-agent/examples/sample-input.md)"
```

## 跑完后先看什么
- 输出是不是已经完成这个角色该负责的那一段
- 是否已经产出能交给下一棒的明确交接物
- 如果还没压清楚，不要急着继续往下一棒走
