# 01-product 安装说明

默认 skill：`agile-web-product-agent`

## 这个角色是干什么的
- 这个角色负责：先把页面清单、状态说明、操作流和交接物压清楚
- 默认 profile 名：`webdev-product`
- 下一棒默认交给 webdev-builder

## 最短安装
```bash
bash ./install_to_profile.sh webdev-product
```

## 最短运行
```bash
hermes -p webdev-product chat --skills agile-web-product-agent -q "$(cat skills/solutions/agile-web-product-agent/examples/sample-input.md)"
```

## 跑完后先看什么
- 输出是不是已经完成这个角色该负责的那一段
- 是否已经产出能交给下一棒的明确交接物
- 如果还没压清楚，不要急着继续往下一棒走
