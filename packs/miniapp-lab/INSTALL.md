# miniapp-lab 下载与安装说明

> 这里别想复杂：你只需要先判断一件事——你现在是想先一个人快速跑通，还是已经准备多人协作。

---

## 👀 先看你该下哪个包

### 只想先跑通一次
下载：`01-super-individual.zip`

适合：
- 你先想验证这套方案到底能不能用
- 你先想拿到页面、目录、文件骨架
- 你不想一上来就分很多角色

### 已经准备多人协作
下载：`02-team.zip`

适合：
- 你希望产品、实现、接口、验收拆开做
- 你不想一个 Agent 什么都包
- 你要的是更清楚的接力流程

---

## 📦 解压后会看到什么

### 超级个体版
- 一个可以直接安装的目录
- 一个单 Agent skill
- sample-input / sample-output
- 最短试跑路径

### 团队协作版
- `01-product/`
- `02-builder/`
- `03-api/`
- `04-qa/`
- `99-solution-validator/`
- `install_all.sh`

---

## ⚡ 最短用法

### 超级个体版
```bash
git clone git@github.com:zcweah1981/awesome-hermes-agent-zh.git
cd awesome-hermes-agent-zh/packs/miniapp-lab/01-super-individual
hermes profile create miniapp-solo --clone
bash ./install_to_profile.sh miniapp-solo
hermes -p miniapp-solo chat --skills wechat-mini-program-solo-assistant -q "$(cat skills/solutions/01-微信小程序/wechat-mini-program-solo-assistant/examples/sample-input.md)"
```

### 团队协作版
```bash
# 先解压 02-team.zip，再进入解压后的目录
cd /path/to/02-team
hermes profile create miniapp-product --clone
hermes profile create miniapp-builder --clone
hermes profile create miniapp-api --clone
hermes profile create miniapp-qa --clone
hermes profile create miniapp-validator --clone
bash ./install_all.sh
```

说明：
- 不传参数时，`install_all.sh` 默认使用 `miniapp` 作为前缀
- 所以默认会装进：
  - `miniapp-product`
  - `miniapp-builder`
  - `miniapp-api`
  - `miniapp-qa`
  - `miniapp-validator`
- 如果你想换前缀，也可以这样装：

```bash
bash ./install_all.sh miniapp
```

---

## 🤝 如果你要直接走团队协作版

最短入口：
- 阅读团队包说明：`02-team/README.md`
- 或直接进入：`02-team/`
- 或直接下载：`02-team.zip`

---

## ✅ 跑完以后你重点看什么

### 超级个体版
你至少要看到：
- 页面拆出来了
- 目录骨架有了
- 第一批文件建议有了
- 下一句怎么继续补文件也有了

### 团队协作版
你至少要看到：
- product 先产出页面和边界
- builder 接着产出前端骨架
- api 把数据结构和接口约定补清楚
- validator 最后能给出结论

---

## 🧪 这两个包的区别，一句话记住

- 超级个体版：先快跑起来
- 团队协作版：按角色接力推进
