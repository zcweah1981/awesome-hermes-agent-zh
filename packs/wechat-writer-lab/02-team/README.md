# 团队协作版

> 这个包适合：已经不是一个人单独出稿，而是想把公众号文章拆成接力流程来推进。

---

## 👀 这里面有谁

- `01-article-strategist/`：你是公众号选题与结构负责人
- `02-article-writer/`：你是公众号初稿写手
- `03-editor/`：你是公众号编辑负责人
- `04-review/`：你是公众号审校负责人
- `99-solution-validator/`：你是公众号写作方案总体验收专家

## ⚡ 最短用法

### 1）先创建 5 个 profile
```bash
hermes profile create gzh-strategy --clone
hermes profile create gzh-writer --clone
hermes profile create gzh-edit --clone
hermes profile create gzh-review --clone
hermes profile create gzh-validator --clone
```

### 2）再一键安装
```bash
bash ./install_all.sh
```

说明：
- 不传参数时，`install_all.sh` 默认使用 `gzh` 作为 profile 前缀
- 如果你想换前缀，也可以这样装：

```bash
bash ./install_all.sh gzh
```

### 3）先跑第一棒
```bash
hermes -p gzh-strategy chat --skills wechat-article-strategist -q "$(cat 01-article-strategist/skills/solutions/wechat-article-strategist/examples/sample-input.md)"
```

跑完第一棒后，先确认：
- 文章切口已经压清楚
- 标题方向和大纲已经成型
- 已经知道下一棒该交给谁

### 4）再接第二棒
```bash
hermes -p gzh-writer chat --skills wechat-article-writer -q "$(cat 02-article-writer/skills/solutions/wechat-article-writer/examples/sample-input.md)"
```

### 5）最后交给 Validator
```bash
hermes -p gzh-validator chat --skills solution-validator-gzh -q "$(cat 99-solution-validator/skills/solutions/solution-validator-gzh/examples/sample-input.md)"
```

## 🤝 全链路接力图谱

| 这一棒是谁 | 这一棒主要做什么 | 交给下一棒时，手里应该有什么 |
|---|---|---|
| `gzh-strategy` | 定文章切口、标题方向、文章大纲 | 一版清楚的起稿主线 |
| `gzh-writer` | 写导语、正文初稿、段落重点 | 一版可继续润的文章骨架 |
| `gzh-edit` | 顺语气、补小标题、补配图和 CTA | 一版更适合进公众号后台的编辑稿 |
| `gzh-review` | 查结构风险、查结构问题、列必须修改项 | 一版发前审校结论 |
| `gzh-validator` | 判断 `pass / pass with fixes / fail` | 最终“这篇现在能不能发”的结论 |

## 🚦 什么时候不要往下一棒走

- 不要交第二棒：第一棒还没把文章切口、标题方向和大纲压清楚
- 不要交第三棒：第二棒还没写出可读的导语和正文初稿
- 不要交第四棒：第三棒还没把语气、小标题、摘要和 CTA 收成可发布文章
- 不要交 Validator：第四棒还没把结构风险、必须修改项和可发判断压清楚
