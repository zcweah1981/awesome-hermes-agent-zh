# 进入终端并连接服务器

这一步完成后，你应该已经站在一个可以继续安装 Hermes 的终端里，并且确认 Git 可以正常使用。

如果你在本地运行，重点是打开正确的终端；如果你在云主机运行，重点是通过 SSH 成功登录服务器。做完这一步，下一页就可以直接开始安装。

![本地终端与 SSH 连接路径示意图](../assets/rm2-2-connect-terminal-01-local-vs-ssh-route.png)

## 先判断你属于哪一种情况

| 你的情况 | 这一步要做什么 |
| --- | --- |
| 本地 macOS | 打开 Terminal 或 iTerm2 |
| 本地 Linux | 打开系统终端 |
| Windows WSL2 | 先进入 WSL2，再在里面继续 |
| 云主机 | 通过 SSH 登录服务器 |

## 第 1 步：打开正确的终端

### 如果你用的是 macOS

打开系统自带的 Terminal 即可，也可以使用 iTerm2。

打开后，你应该能看到类似用户名、主机名和当前目录的提示行。

### 如果你用的是 Linux

打开系统自带终端即可。大多数发行版默认就能继续后面的步骤。

### 如果你用的是 Windows WSL2

先进入 WSL2 的 Linux 环境，再继续下面的命令。

你要确认自己现在是在 Linux 终端里，而不是 PowerShell 或原生 CMD 里。一个简单判断方法是：终端提示符更像 Linux，后面安装软件时会使用 `apt` 等 Linux 命令。

## 第 2 步：如果你用云主机，用 SSH 登录服务器

SSH 是从你自己的电脑连接到远程 Linux 服务器的标准方式。

登录前，先准备这 3 样东西：

- 服务器公网 IP
- 登录用户名
- 登录密码，或者密钥文件

![SSH 登录成功后的终端示例](../assets/rm2-2-connect-terminal-02-ssh-login-success.png)

### 最常见的连接命令

如果你用密码登录：

```bash
ssh 用户名@服务器IP
```

例如：

```bash
ssh root@203.0.113.10
```

如果你用密钥文件登录：

```bash
ssh -i /你的密钥路径 用户名@服务器IP
```

例如：

```bash
ssh -i ~/.ssh/id_rsa root@203.0.113.10
```

### 第一次连接时会看到什么

第一次连某台服务器时，终端通常会问你是否信任这个主机指纹。确认无误后输入 `yes`，再继续输入密码或使用密钥登录。

成功后，你会进入服务器 shell，提示符通常会变成远程机器的用户名和主机名。

## 第 3 步：确认你已经真的进入了目标环境

无论你是本地还是远程，现在都先做一个最小检查：

```bash
pwd
whoami
```

你要确认两件事：

- 当前路径和当前用户看起来合理。
- 如果你用的是云主机，显示的已经是远程服务器环境，而不是你本地电脑。

## 第 4 步：检查 Git 是否可用

安装 Hermes 前，先确认 Git 已经能用：

```bash
git --version
```

如果看到版本号，比如 `git version 2.x.x`，就说明这一项没问题。

![SSH 登录后确认 Git 可用的终端示例](../assets/rm2-2-connect-terminal-03-ssh-git-success.png)

## 第 5 步：如果 Git 还没装，先补上

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install -y git
```

### CentOS / Rocky / AlmaLinux

```bash
sudo yum install -y git
```

如果你的系统使用 `dnf`，也可以这样装：

```bash
sudo dnf install -y git
```

### macOS

第一次执行 `git` 时，系统通常会提示安装开发者工具。按提示完成安装后，再重新执行一次 `git --version`。

## 如果这一步卡住，先看这几个地方

- SSH 命令里的用户名和 IP 有没有写错。
- 你是不是把本地终端和远程终端搞混了。
- 云主机的安全组、防火墙是否放行了 SSH 端口。
- 你使用的密钥文件路径是否正确。
- Git 安装完成后，是否重新执行了 `git --version` 验证。

## 看到什么，算这一步成功

满足下面两件事，就可以继续下一页：

1. 你已经进入了正确的终端环境。
2. 你执行 `git --version` 时能看到版本号。

下一步：

- [把 Hermes 装上去](./install-hermes.md)
