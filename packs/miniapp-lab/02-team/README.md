# 02-team 团队协作版

> 这个包适合：你已经不想让一个 Agent 什么都包了，而是想把“产品、实现、接口、验收”拆开协作。

---

## 👀 先看区别

和超级个体版相比，团队协作版不是追求“最快一把跑完”，而是追求：
- 分工清楚
- 交接清楚
- 更适合认真推进一个项目

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
产品 -> 实现 -> 接口 -> 验收

---

## ⚡ 最短用法

### 1）先创建 5 个 profile
```bash
hermes profile create miniapp-product --clone
hermes profile create miniapp-builder --clone
hermes profile create miniapp-api --clone
hermes profile create miniapp-qa --clone
hermes profile create miniapp-validator --clone
```

### 2）再一键安装
```bash
bash ./install_all.sh
```

---

## ✅ 跑完后你应该看到什么

至少应该看到这几件事：
- 产品 Agent 产出页面、功能、边界
- Builder Agent 产出前端骨架建议
- API Agent 产出接口与数据结构
- QA Agent 产出检查项
- Validator 最后能判断 pass / pass with fixes / fail

如果你想手动安装，也可以分别进入每个子目录执行：
```bash
bash ./install_to_profile.sh <profile>
```
