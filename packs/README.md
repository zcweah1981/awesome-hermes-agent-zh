# packs

这一层放的是可直接下载、解压、安装进 Hermes profile 的打包方案。

## 当前已开放的包

- [miniapp-lab](./miniapp-lab/)

## miniapp-lab 是什么

`miniapp-lab` 不是源码工程本体，而是一组给 Hermes 用的现成包：

- `01-super-individual`：一个 Agent 先把微信小程序需求压成可开工骨架
- `02-team`：把 product、builder、api、qa、validator 拆开协作

## 你什么时候先进这一层

如果你已经在文档里看到了某个现成方案，接下来要做的是：

- 下载 zip
- 解压
- 安装到自己的 Hermes profile
- 直接试跑

那你就会进入这一层。

## 默认入口

如果你是跟着当前文档主线来的，默认先看：

- [miniapp-lab/INSTALL.md](./miniapp-lab/INSTALL.md)

它会先帮你判断：

- 该下 `01-super-individual.zip`
- 还是该下 `02-team.zip`

## ✅ 看完这页你应该能立刻判断什么

看完这一层，你应该能马上判断：

- `packs` 是包目录，不是 docs 页面目录
- 当前有哪些可直接安装的打包方案
- 我下一步该不该进 `miniapp-lab`
