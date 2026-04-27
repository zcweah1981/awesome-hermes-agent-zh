# 04-review 安装说明

默认 skill：`wechat-article-review`

## 这个角色是干什么的
- 这个角色负责：把结构风险、必须修改项和可发判断压清楚
- 默认 profile 名：`gzh-review`
- 下一棒默认交给 gzh-validator

## 最短安装
```bash
bash ./install_to_profile.sh gzh-review
```

## 最短运行
```bash
hermes -p gzh-review chat --skills wechat-article-review -q "$(cat skills/solutions/wechat-article-review/examples/sample-input.md)"
```

## 跑完后先看什么
- 输出是不是已经完成这个角色该负责的那一段
- 是否已经产出能交给下一棒的明确交接物
- 如果还没压清楚，不要急着继续往下一棒走
