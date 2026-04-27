# 03-polisher 安装说明

默认 skill：`xiaohongshu-polisher`

## 这个角色是干什么的
- 这个角色负责：把语气、封面短句和评论引导收成更像真实发帖的润色稿
- 默认 profile 名：`xhs-polish`
- 下一棒默认交给 xhs-review

## 最短安装
```bash
bash ./install_to_profile.sh xhs-polish
```

## 最短运行
```bash
hermes -p xhs-polish chat --skills xiaohongshu-polisher -q "$(cat skills/solutions/xiaohongshu-polisher/examples/sample-input.md)"
```

## 跑完后先看什么
- 输出是不是已经完成这个角色该负责的那一段
- 是否已经产出能交给下一棒的明确交接物
- 如果还没压清楚，不要急着继续往下一棒走
