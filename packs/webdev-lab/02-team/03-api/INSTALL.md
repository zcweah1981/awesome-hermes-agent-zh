# 03-api 安装说明

默认 skill：`agile-web-api-agent`

## 这个角色是干什么的
- 这个角色负责：把数据结构、接口约定和请求返回字段压清楚
- 默认 profile 名：`webdev-api`
- 下一棒默认交给 webdev-qa

## 最短安装
```bash
bash ./install_to_profile.sh webdev-api
```

## 最短运行
```bash
hermes -p webdev-api chat --skills agile-web-api-agent -q "$(cat skills/solutions/agile-web-api-agent/examples/sample-input.md)"
```

## 跑完后先看什么
- 输出是不是已经完成这个角色该负责的那一段
- 是否已经产出能交给下一棒的明确交接物
- 如果还没压清楚，不要急着继续往下一棒走
