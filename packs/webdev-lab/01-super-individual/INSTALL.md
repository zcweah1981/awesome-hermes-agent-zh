# 01-super-individual 安装说明

> 这个包不是只给你看方案，而是让你先把一个 Web 工具想法推进到“能开始搭代码骨架”的状态。

---

## 👀 这个包会帮你产出什么

跑完后，你最少应该拿到：
- 页面清单
- 数据与接口草案
- Web 目录骨架
- 第一批代码文件建议
- 下一步继续补代码的方向

---

## ⚡ 最短用法

### 1）创建默认 profile
```bash
hermes profile create webdev-solo --clone
```

### 2）安装
```bash
bash ./install_to_profile.sh webdev-solo
```

### 3）直接试跑
```bash
hermes -p webdev-solo chat --skills agile-web-development-solo-assistant -q "$(cat skills/solutions/agile-web-development-solo-assistant/examples/sample-input.md)"
```

说明：
- 页面默认示例 profile 名就是 `webdev-solo`
- 如果你想换 profile 名，也可以把上面三条命令里的 `webdev-solo` 换成你自己的名字

---

## ✅ 跑完后你重点看什么

不要只看它有没有分析，重点看这 5 件事：
- 有没有把页面拆出来
- 有没有给目录骨架
- 有没有先把接口和数据占位
- 有没有说明先生成哪些文件
- 有没有告诉你下一步怎么继续补代码

如果这几件事都有，这个包就算真的开始帮你干活了。
