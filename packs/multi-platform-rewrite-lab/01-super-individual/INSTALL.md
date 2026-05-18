# 01-super-individual 安装说明

> 这个包适合：你先把一篇已有内容改成多平台可发布稿件，不先上来做复杂协作流程。

---

## 👀 这个包会帮你产出什么

跑完后，你最少应该拿到：
- 小红书完整笔记（标题 + 正文 + 封面短句 + 话题标签）
- 公众号适配版（标题 + 导语 + 正文结构调整 + 收口）
- 1-3 条 X/Twitter 推文（核心观点 + 补充 + 引导互动）
- 每个版本都能直接复制发布

---

## ⚡ 最短用法

### 1）创建默认 profile
```bash
hermes profile create multi-platform-solo --clone
```

### 2）安装
```bash
bash ./install_to_profile.sh multi-platform-solo
```

### 3）直接试跑
```bash
hermes -p multi-platform-solo chat --skills multi-platform-rewrite-assistant -q "$(cat skills/solutions/multi-platform-rewrite-assistant/examples/sample-input.md)"
```

说明：
- 页面默认示例 profile 名就是 `multi-platform-solo`
- 如果你想换 profile 名，也可以把上面三条命令里的 `multi-platform-solo` 换成你自己的名字

---

## ✅ 跑完后你重点看什么

不要只看它有没有出改写，重点看这 5 件事：
- 有没有把原文核心信息保留住
- 小红书版本有没有 emoji、话题标签和口语感
- X 推文够不够精炼，能不能直接发
- 每个版本复制粘贴到对应平台，格式是否正常
- 有没有给下一轮继续微调各平台版本的方向
