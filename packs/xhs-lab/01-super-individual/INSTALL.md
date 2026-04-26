# 01-super-individual 安装说明

> 这个包适合：你先把一个主题压成可发布的一篇小红书内容，不先上来做复杂运营体系。

---

## 👀 这个包会帮你产出什么

跑完后，你最少应该拿到：
- 选题角度
- 标题候选
- 开头钩子
- 正文底稿
- 封面短句 / 配图提示
- 评论区引导句
- 发布检查单

---

## ⚡ 最短用法

### 1）安装
```bash
bash ./install_to_profile.sh <profile-name-or-path>
```

### 2）直接试跑
```bash
hermes -p <your-profile> chat --skills xiaohongshu-content-assistant -q "$(cat skills/solutions/xiaohongshu-content-assistant/examples/sample-input.md)"
```

---

## ✅ 跑完后你重点看什么

不要只看它有没有写稿，重点看这 4 件事：
- 有没有先定清楚角度
- 有没有给 3～5 个标题备选
- 有没有写出能继续改的正文底稿
- 有没有把发前动作也补上
