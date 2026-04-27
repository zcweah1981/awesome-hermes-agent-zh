# 03-editor 安装说明

默认 skill：`wechat-article-editor`

## 这个角色是干什么的
- 这个角色负责：把语气、小标题、配图建议和 CTA 收成更像可发布文章的编辑稿
- 默认 profile 名：`gzh-edit`
- 下一棒默认交给 gzh-review

## 最短安装
```bash
bash ./install_to_profile.sh gzh-edit
```

## 最短运行
```bash
hermes -p gzh-edit chat --skills wechat-article-editor -q "$(cat skills/solutions/wechat-article-editor/examples/sample-input.md)"
```

## 跑完后先看什么
- 输出是不是已经完成这个角色该负责的那一段
- 是否已经产出能交给下一棒的明确交接物
- 如果还没压清楚，不要急着继续往下一棒走
