# 01-super-individual 安装说明

> 这个包不是只给你看方案，而是让你先把微信小程序想法推进到“能开始搭代码”的状态。

---

## 👀 这个包会帮你产出什么

跑完后，你最少应该拿到：
- 页面清单
- 数据与接口草案
- 小程序目录骨架
- 第一批代码文件建议
- 下一步继续补代码的方向

---

## ⚡ 最短用法

### 1）创建默认 profile
```bash
hermes profile create miniapp-solo --clone
```

### 2）安装
```bash
bash ./install_to_profile.sh miniapp-solo
```

### 3）直接试跑
```bash
hermes -p miniapp-solo chat --skills wechat-mini-program-solo-assistant -q "$(cat skills/solutions/01-微信小程序/wechat-mini-program-solo-assistant/examples/sample-input.md)"
```

说明：
- 页面默认示例 profile 名就是 `miniapp-solo`
- 如果你想换 profile 名，也可以把上面三条命令里的 `miniapp-solo` 换成你自己的名字

---

## ✅ 跑完后你重点看什么

不要只看它有没有分析，重点看这 5 件事：
- 有没有把页面拆出来
- 有没有给目录骨架
- 有没有说明先写哪些文件
- 有没有把 mock 数据和接口草案占住
- 有没有告诉你下一步怎么继续补代码

如果这几件事都有，这个包就算真的开始帮你干活了。
