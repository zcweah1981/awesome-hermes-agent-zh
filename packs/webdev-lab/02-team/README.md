# 团队协作版

> 这个包适合：你已经不想让一个 Agent 什么都包了，而是想把“需求、实现、接口、验收”拆开协作。

---

## 👀 先看区别

和超级个体版相比，团队协作版不是追求“最快一把跑完”，而是追求：
- 分工清楚
- 交接清楚
- 更适合认真推进一个 Web 工具项目

如果你现在只是第一次试这套方案，先用超级个体版更容易。
如果你已经准备正式推进，再用这个包。

---

## 🤝 这里面有谁

解压后你会看到 5 个角色目录：
- `01-product/`：先拆需求、页面、边界
- `02-builder/`：再把页面变成前端骨架
- `03-api/`：再把数据和接口约定拆清楚
- `04-qa/`：再检查能不能开工
- `99-solution-validator/`：最后做总体验收

你可以把它理解成一条接力链：
需求 -> 实现 -> 接口 -> 验收 -> 最终判断

---

## ⚡ 最短用法

### 1）先创建 5 个 profile
```bash
hermes profile create webdev-product --clone
hermes profile create webdev-builder --clone
hermes profile create webdev-api --clone
hermes profile create webdev-qa --clone
hermes profile create webdev-validator --clone
```

### 2）再一键安装
```bash
bash ./install_all.sh
```

说明：
- 不传参数时，`install_all.sh` 默认使用 `webdev` 作为前缀
- 所以默认会装进：
  - `webdev-product`
  - `webdev-builder`
  - `webdev-api`
  - `webdev-qa`
  - `webdev-validator`
- 如果你想换前缀，也可以这样装：

```bash
bash ./install_all.sh webdev
```

### 3）先跑第一棒
```bash
hermes -p webdev-product chat --skills agile-web-product-agent -q "$(cat 01-product/skills/solutions/agile-web-product-agent/examples/sample-input.md)"
```

跑完第一棒后，先确认：
- 页面清单已经压出来
- 状态说明和操作流已经成型
- 已经知道下一棒该交给谁

### 4）再接第二棒
```bash
hermes -p webdev-builder chat --skills agile-web-builder-agent -q "$(cat 02-builder/skills/solutions/agile-web-builder-agent/examples/sample-input.md)"
```

### 5）最后交给 Validator
```bash
hermes -p webdev-validator chat --skills solution-validator-webdev -q "$(cat 99-solution-validator/skills/solutions/solution-validator-webdev/examples/sample-input.md)"
```

## 🤝 全链路接力图谱

| 这一棒是谁 | 这一棒主要做什么 | 交给下一棒时，手里应该有什么 |
|---|---|---|
| `webdev-product` | 定页面清单、状态说明、操作流、交接物 | 一版明确的实现起点 |
| `webdev-builder` | 产出前端目录骨架、页面文件建议、组件建议、状态流转 | 一版可落地前端骨架 |
| `webdev-api` | 补数据结构、接口约定、请求返回字段 | 一版可对接接口草案 |
| `webdev-qa` | 查检查项、风险点、是否能开工 | 一版开工前审校结论 |
| `webdev-validator` | 判断 `pass / pass with fixes / fail` | 最终“这套方案现在能不能继续推进”的结论 |

## 🚦 什么时候不要往下一棒走

- 不要交第二棒：第一棒还没把页面清单、状态说明和操作流压清楚
- 不要交第三棒：第二棒还没把目录骨架、页面文件建议和状态流转写出来
- 不要交第四棒：第三棒还没把数据结构和接口约定压清楚
- 不要交 Validator：第四棒还没把风险点、必须补的项和可开工判断压清楚
