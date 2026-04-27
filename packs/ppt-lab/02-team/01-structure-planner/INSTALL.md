# 01-structure-planner 安装说明

默认 skill：`ppt-structure-planner`

## 这个角色是干什么的
- 这个角色负责：先把主线、页序和每页职责压清楚
- 默认 profile 名：`ppt-structure`
- 下一棒默认交给 ppt-slidewriter

## 最短安装
```bash
bash ./install_to_profile.sh ppt-structure
```

## 最短运行
```bash
hermes -p ppt-structure chat --skills ppt-structure-planner -q "$(cat skills/solutions/ppt-structure-planner/examples/sample-input.md)"
```

## 跑完后先看什么
- 输出是不是已经完成这个角色该负责的那一段
- 是否已经产出能交给下一棒的明确交接物
- 如果还没压清楚，不要急着继续往下一棒走
