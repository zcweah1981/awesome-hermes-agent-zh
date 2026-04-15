# 进入终端并连接服务器

在安装 Hermes 之前，你需要先进入运行环境。
如果你使用的是本地 macOS 或 Linux，这一步通常是打开终端；如果你使用的是云主机，这一步通常是通过远程连接（SSH）进入服务器。
**离开这页时，你应该已经进入一个可以继续安装 Hermes 的终端环境，并确认 Git 已经可用。**

---

## 1. 页面定位

这是“先跑起来”模块的第 2 页。
它的任务不是安装 Hermes，而是帮助用户：

- 打开终端
- 进入服务器
- 在开始安装前确认 Git 已经可用

---

## 2. 页面目标

用户看完这一页后，应该完成下面几件事：

1. 已经打开本地终端，或者成功连接到 Linux 服务器
2. 已经知道自己使用哪个终端工具
3. 已经确认 Git 可以正常使用

---

## 3. 解决什么问题

- 打开本地终端
- 通过 SSH 远程连接 Linux 服务器
- 选择适合 Windows / macOS 的 SSH 工具
- 安装前确认 Git 是否可用

---

## 4. 不解决什么

这一页不展开讲：

- Hermes 安装步骤
- AI 大模型配置
- 第一次和 Hermes 打招呼
- Web UI 接入

---

## 5. 页面结构

### 5.1 先判断你属于哪种情况

![本地终端与 SSH 连接路径示意图](../assets/rm2-2-connect-terminal-01-local-vs-ssh-route.png)

| 你的情况 | 你这一步要做什么 |
|---|---|
| 本地 macOS | 打开终端 |
| 本地 Linux | 打开终端 |
| 云主机 | 通过远程连接（SSH）进入服务器 |
| Windows WSL2 | 先进入 WSL2，再打开终端 |

### 5.2 本地运行：先打开终端

#### macOS
macOS 自带 Terminal，也可以使用 iTerm2。

#### Linux
大多数 Linux 系统都自带终端。

### 5.3 远程连接服务器：推荐工具

#### Windows 用户推荐
- Windows Terminal
- PuTTY
- Tabby

#### macOS 用户推荐
- Terminal
- iTerm2
- Tabby

### 5.4 什么是远程连接（SSH）

远程连接（SSH）就是从你的电脑连接到 Linux 服务器的标准方式。
通常你需要准备：

![SSH 登录成功后的终端示例](../assets/rm2-2-connect-terminal-02-ssh-login-success.png)

- 服务器公网 IP
- 登录用户名
- 密码，或者密钥文件

### 5.5 最基础的连接命令

![SSH 登录后确认 Git 可用的终端示例](../assets/rm2-2-connect-terminal-03-ssh-git-success.png)
