# 团队协作版

> 这个包适合：已经不是一个人单独出稿，而是想把小红书内容拆成接力流程来推进。

---

## 👀 这里面有谁

- `01-topic-strategist/`：你是小红书选题与角度负责人
- `02-drafter/`：你是小红书初稿写手
- `03-polisher/`：你是小红书润稿负责人
- `04-review/`：你是小红书审校负责人
- `99-solution-validator/`：你是小红书内容方案总体验收专家

## ⚡ 最短用法

### 1）先创建 5 个 profile
```bash
hermes profile create xhs-strategy --clone
hermes profile create xhs-draft --clone
hermes profile create xhs-polish --clone
hermes profile create xhs-review --clone
hermes profile create xhs-validator --clone
```

### 2）再一键安装
```bash
bash ./install_all.sh
```

说明：
- 不传参数时，`install_all.sh` 默认使用 `xhs` 作为 profile 前缀
- 如果你想换前缀，也可以这样装：

```bash
bash ./install_all.sh xhs
```

### 3）先跑第一棒
```bash
hermes -p xhs-strategy chat --skills xiaohongshu-topic-strategist -q "$(cat 01-topic-strategist/skills/solutions/xiaohongshu-topic-strategist/examples/sample-input.md)"
```

跑完第一棒后，先确认：
- 选题角度已经压清楚
- 标题方向和内容结构已经成型
- 已经知道下一棒该交给谁

### 4）再接第二棒
```bash
hermes -p xhs-draft chat --skills xiaohongshu-drafter -q "$(cat 02-drafter/skills/solutions/xiaohongshu-drafter/examples/sample-input.md)"
```

### 5）最后交给 Validator
```bash
hermes -p xhs-validator chat --skills solution-validator-xhs -q "$(cat 99-solution-validator/skills/solutions/solution-validator-xhs/examples/sample-input.md)"
```

## 🤝 全链路接力图谱

| 这一棒是谁 | 这一棒主要做什么 | 交给下一棒时，手里应该有什么 |
|---|---|---|
| `xhs-strategy` | 定选题角度、目标读者、标题方向、内容结构 | 一版清楚的起稿主线 |
| `xhs-draft` | 写开头、正文底稿、分页建议 | 一版可继续改的初稿 |
| `xhs-polish` | 压语气、补封面短句、补评论引导 | 一版更像真实发帖的润色稿 |
| `xhs-review` | 查风险点、查人设一致性、列必须修改项 | 一版发前审校结论 |
| `xhs-validator` | 判断 `pass / pass with fixes / fail` | 最终“这篇现在能不能发”的结论 |

## 🚦 什么时候不要往下一棒走

- 不要交第二棒：第一棒还没把选题角度、标题方向、内容结构压清楚
- 不要交第三棒：第二棒还没写出完整开头和正文底稿
- 不要交第四棒：第三棒还没把语气、封面短句和评论区引导收成真实帖文感
- 不要交 Validator：第四棒还没把风险点、必须修改项和可发判断压清楚
