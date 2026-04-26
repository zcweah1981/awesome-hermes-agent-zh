# 01-super-individual 安装说明

> 这个包适合：你先把一个主题压成一份可继续做成 PPT 的整套稿，不先上来做复杂设计系统。

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

## ⚡ 最短用法

### 1）安装
```bash
bash ./install_to_profile.sh <profile-name-or-path>
```

### 2）直接试跑
```bash
hermes -p <your-profile> chat --skills ppt-assistant -q "$(cat skills/solutions/ppt-assistant/examples/sample-input.md)"
```

---

## ✅ 跑完后你重点看什么

不要只看它有没有出结构，重点看这 4 件事：
- 有没有先把整套叙事主线定清楚
- 有没有给页序、每页标题和每页要点
- 有没有补图表 / 配图建议
- 有没有把下一轮继续做版的动作补上
