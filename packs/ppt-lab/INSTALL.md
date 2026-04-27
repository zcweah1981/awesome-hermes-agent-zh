# ppt-lab 下载与安装说明

> 这个包不是只给你看 PPT 建议，而是让你先把一个主题压成“可继续做成 PPT 的整套稿”。

---

## 👀 这个包会帮你产出什么

跑完后，你最少应该拿到：
- 叙事切口
- 页序结构
- 每页标题与要点
- 图表 / 配图建议
- 演讲备注
- 继续做版清单

---

## 📦 包里有什么

当前提供：
- `02-team/`：团队协作版，拆成结构 / 逐页写稿 / 润稿 / 审校 / 总体验收
- `02-team.zip`：团队协作版打包版本
- `01-super-individual/`：一个 Agent 先帮你把一份 PPT 压成可继续落版的整套稿
- `01-super-individual.zip`：可直接下载的打包版本

---

## ⚡ 最短用法

```bash
git clone git@github.com:zcweah1981/awesome-hermes-agent-zh.git
cd awesome-hermes-agent-zh/packs/ppt-lab/01-super-individual
hermes profile create ppt-solo --clone
bash ./install_to_profile.sh ppt-solo
hermes -p ppt-solo chat --skills ppt-assistant -q "$(cat skills/solutions/ppt-assistant/examples/sample-input.md)"
```

---

## ✅ 跑完后你重点看什么

不要只看它有没有分析，重点看这 5 件事：
- 有没有先把主线定清楚
- 有没有把页序和每页标题定出来
- 有没有把逐页要点写出来
- 有没有补图表 / 配图 / 备注建议
- 有没有给下一轮继续落版的句子

---

## 🤝 如果你要直接走团队协作版

如果你已经不是一个人单独做 PPT，而是想按角色接力推进，直接进入 `02-team/` 或下载 `02-team.zip`。

最短入口：
- 阅读团队包说明：`02-team/README.md`
- 或直接进入：`02-team/`
- 或直接下载：`02-team.zip`
