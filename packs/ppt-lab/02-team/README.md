# 团队协作版

> 这个包适合：已经不是一个人单独做 PPT，而是想把结构、逐页写稿、润稿和审校拆成接力流程来推进。

---

## 👀 这里面有谁

- `01-structure-planner/`：你是 PPT 结构负责人
- `02-slide-writer/`：你是 PPT 逐页内容写手
- `03-slide-polisher/`：你是 PPT 落版润色负责人
- `04-review/`：你是 PPT 审校负责人
- `99-solution-validator/`：你是 PPT 方案总体验收专家

## ⚡ 最短用法

### 1）先创建 5 个 profile
```bash
hermes profile create ppt-structure --clone
hermes profile create ppt-slidewriter --clone
hermes profile create ppt-polish --clone
hermes profile create ppt-review --clone
hermes profile create ppt-validator --clone
```

### 2）再一键安装
```bash
bash ./install_all.sh
```

说明：
- 不传参数时，`install_all.sh` 默认使用 `ppt` 作为 profile 前缀
- 如果你想换前缀，也可以这样装：

```bash
bash ./install_all.sh ppt
```

### 3）先跑第一棒
```bash
hermes -p ppt-structure chat --skills ppt-structure-planner -q "$(cat 01-structure-planner/skills/solutions/ppt-structure-planner/examples/sample-input.md)"
```

跑完第一棒后，先确认：
- 主线讲法已经压清楚
- 页序和每页职责已经成型
- 已经知道下一棒该交给谁

### 4）再接第二棒
```bash
hermes -p ppt-slidewriter chat --skills ppt-slide-writer -q "$(cat 02-slide-writer/skills/solutions/ppt-slide-writer/examples/sample-input.md)"
```

### 5）最后交给 Validator
```bash
hermes -p ppt-validator chat --skills solution-validator-ppt -q "$(cat 99-solution-validator/skills/solutions/solution-validator-ppt/examples/sample-input.md)"
```

## 🤝 全链路接力图谱

| 这一棒是谁 | 这一棒主要做什么 | 交给下一棒时，手里应该有什么 |
|---|---|---|
| `ppt-structure` | 定主线、页序、每页职责 | 一版清楚的结构骨架 |
| `ppt-slidewriter` | 写每页标题、要点、图表建议 | 一版可继续润的逐页稿 |
| `ppt-polish` | 补口播备注、删减建议、页间过渡 | 一版更适合正式汇报的润稿 |
| `ppt-review` | 查结构风险、查汇报断点、列必须修改项 | 一版汇报前审校结论 |
| `ppt-validator` | 判断 `pass / pass with fixes / fail` | 最终“这份 PPT 现在能不能进正式汇报”的结论 |

## 🚦 什么时候不要往下一棒走

- 不要交第二棒：第一棒还没把主线、页序和每页职责定清楚
- 不要交第三棒：第二棒还没把每页标题、要点和图表建议写出来
- 不要交第四棒：第三棒还没补齐口播备注、页间过渡和删减建议
- 不要交 Validator：第四棒还没把结构风险、必须修改项和可讲判断压清楚
