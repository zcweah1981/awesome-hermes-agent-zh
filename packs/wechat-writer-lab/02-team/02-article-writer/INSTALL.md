# 02-article-writer 安装说明

默认 skill：`wechat-article-writer`

## 这个角色是干什么的
- 这个角色负责：把导语、正文初稿和段落重点写出来
- 默认 profile 名：`gzh-writer`
- 下一棒默认交给 gzh-edit

## 最短安装
```bash
bash ./install_to_profile.sh gzh-writer
```

## 最短运行
```bash
hermes -p gzh-writer chat --skills wechat-article-writer -q "$(cat skills/solutions/wechat-article-writer/examples/sample-input.md)"
```

## 跑完后先看什么
- 输出是不是已经完成这个角色该负责的那一段
- 是否已经产出能交给下一棒的明确交接物
- 如果还没压清楚，不要急着继续往下一棒走
