# 把 Hermes 装上去

现在你已经进入了运行环境，并且确认 Git 已经可以正常使用，下一步就是把 Hermes 装上去。
**离开这页时，你应该已经完成 Hermes 安装。**

---

## 1. 页面定位

这是“先跑起来”模块的第 3 页。
它的任务是把 Hermes 安装到当前环境里，并确认它已经安装成功。

---

## 2. 页面目标

用户离开这页时，应该完成：

1. 已经执行 Hermes 安装
2. 已经确认 Hermes 安装成功

---

## 3. 解决什么问题

- 官方推荐安装方式
- 最短安装命令
- 安装成功后怎么验证
- 安装失败时先看什么

---

## 4. 不解决什么

这一页不展开讲：

- AI 大模型怎么选
- 模型密钥怎么配置
- 第一次怎么和 Hermes 打招呼
- 命令行和网页界面怎么选
- 高级配置

---

## 5. 页面结构

### 5.1 官方推荐安装方式

建议优先使用 Hermes 官方的一键安装方式。

### 5.2 直接开始安装

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

### 5.3 安装完成后重新加载终端环境

#### Bash
```bash
source ~/.bashrc
```

#### Zsh
```bash
source ~/.zshrc
```

### 5.4 检查有没有安装成功

```bash
hermes version
hermes doctor
```

### 5.5 安装失败时先看什么

- 安装命令是否完整复制
- 网络是否正常
- 当前终端环境是否正确
- Git 是否已经可用
- 是否有明显报错信息

### 5.6 成功界面是什么样子

> 建议这里放一张“安装成功后的版本检查截图”。

![Hermes 安装成功后的版本检查截图](../assets/screenshots/hermes-install-success.png)

### 5.7 下一步

- [配好 AI 大模型并完成第一次互动](./first-hello.md)
