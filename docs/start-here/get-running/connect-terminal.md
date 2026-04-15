# 进入终端并连接服务器

这一步只解决一件事：让你站到一个可以继续安装 Hermes 的终端里。  
**离开这页时，你应该已经进入正确终端，并且确认 Git 已经可用。**

---

## <img src="../assets/icon-terminal-entry.svg" width="18" alt="终端图标" /> 先判断你现在走哪条路

先不要急着输命令，先判断你现在属于哪一种情况。

![进入终端路线图：先判断你属于本地终端、WSL2 还是云主机 SSH，两条路径最后统一落到 Git 可用](../assets/rm2-2-connect-terminal-01-local-vs-ssh-route-gemini-v3.png)

<table>
  <colgroup>
    <col style="width: 28%;" />
    <col style="width: 32%;" />
    <col style="width: 40%;" />
  </colgroup>
  <thead>
    <tr>
      <th>你的情况</th>
      <th>这一步要做什么</th>
      <th>什么时候算你已经能继续</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>本地 macOS / Linux</td>
      <td>打开本地终端</td>
      <td>已经看到可输入命令的终端窗口</td>
    </tr>
    <tr>
      <td>Windows WSL2</td>
      <td>先进入 WSL2 的 Linux 终端</td>
      <td>已经进入 Linux 风格提示符，不再停在 PowerShell / CMD</td>
    </tr>
    <tr>
      <td>云主机</td>
      <td>通过 SSH 登录服务器</td>
      <td>已经进入远程服务器提示符</td>
    </tr>
  </tbody>
</table>

现在做什么：
- 先对照上表，确认自己属于哪一种情况。
- 没判断清楚前，不要直接跳到安装页。

为什么做这一步：
- 你后面输入的命令、看到的提示符、判断是否成功的方式，都取决于这里的路线。

看到什么算成功：
- 你已经能明确回答：自己现在走的是本地终端、WSL2，还是云主机 SSH。

如果没看到这个结果，先检查什么：
- 你是不是还没决定 Hermes 跑在本地还是云主机。
- 你是不是把 Windows 原生命令行和 WSL2 终端混在一起了。

---

## <img src="../assets/icon-terminal-entry.svg" width="18" alt="本地终端图标" /> 本地终端怎么进入

### macOS / Linux

现在做什么：
- macOS 打开 Terminal，或者你平时使用的 iTerm2。
- Linux 打开系统自带终端。

为什么做这一步：
- 后面的命令必须在真正的终端里执行，不是在浏览器里执行。

看到什么算成功：
- 你已经看到一个可以输入命令的终端窗口。
- 光标停在提示符后面，允许继续输入命令。

如果没看到这个结果，先检查什么：
- 你是不是打开了别的应用，而不是终端。
- 终端是不是没有正常启动。

### Windows WSL2

现在做什么：
- 打开 Windows Terminal 或你常用的终端工具。
- 进入 WSL2 的 Linux 终端。

为什么做这一步：
- 这套教程后面的命令按 Linux 终端来执行，不是在 PowerShell 或 CMD 里执行。

看到什么算成功：
- 你已经进入 WSL2 的 Linux 终端。
- 提示符已经是 Linux 风格，可以继续输入 Linux 命令。

如果没看到这个结果，先检查什么：
- 你是不是还停在 PowerShell / CMD。
- WSL2 是否已经正确安装并能正常启动。

> <img src="../assets/icon-terminal-entry.svg" width="16" alt="终端提示图标" /> 如果你走的是本地 / WSL2 路线，这一页通过的关键不是“看懂终端是什么”，而是你已经真的进入了可以继续执行命令的终端。

---

## <img src="../assets/icon-cloud-ssh.svg" width="18" alt="云主机 SSH 图标" /> 云主机怎么连接

如果你走的是云主机路线，先准备这三样：
- 服务器公网 IP
- 登录用户名
- 密码，或者密钥文件

最基础的连接命令是：

```bash
ssh 用户名@服务器IP
```

如果你使用密钥文件：

```bash
ssh -i /你的密钥路径 用户名@服务器IP
```

![SSH 登录成功截图：先看到 ssh 连接命令，再看到远程服务器提示符和 hostname 返回](../assets/rm2-2-connect-terminal-02-ssh-login-success.png)

现在做什么：
- 在当前终端里执行 SSH 命令。
- 第一次连接时，如果提示是否信任主机指纹，确认无误后再继续。

为什么做这一步：
- 只有真正进入远程服务器，你后面的安装才是在正确机器上完成。

看到什么算成功：
- 你的提示符已经从本地终端变成远程服务器提示符。
- 你执行 `hostname` 时，能看到远程服务器主机名返回结果。

如果没看到这个结果，先检查什么：
- 用户名、IP、密钥路径有没有写错。
- 你是不是根本没有真正进入远程 shell。
- 安全组、防火墙是否允许 SSH 连接。

---

## <img src="../assets/icon-check-success.svg" width="18" alt="成功检查图标" /> 怎么确认你已经进入正确终端

无论你走哪条路，这一页最后都要做同一个检查：

```bash
git --version
```

![Git 可用成功截图：已经登录服务器，在远程提示符下执行 git --version 并返回版本号](../assets/rm2-2-connect-terminal-03-ssh-git-success.png)

现在做什么：
- 在你当前所在的终端里执行 `git --version`。

为什么做这一步：
- 官方安装前提就是 Git 可用；如果这一步没过，下一页安装会直接卡住。

看到什么算成功：
- 终端返回 Git 版本号，例如 `git version 2.x.x`。
- 命令执行完以后，提示符回到下一行。

如果没看到这个结果，先检查什么：
- 你是不是还没进入正确终端。
- 你是不是还没装 Git。

---

## <img src="../assets/icon-check-success.svg" width="18" alt="最小检查图标" /> 常见连接问题先查这几件事

如果你还没通过这一页，先只查最小的 4 件事：

1. 我现在是不是已经进入正确终端了。
2. 如果是云主机，我是不是已经真的进入远程服务器提示符了。
3. `git --version` 有没有正常返回版本号。
4. 如果 Git 没装，我有没有先补装再重查。

如果你现在还没有安装 Git，可以先执行：

### Ubuntu / Debian
```bash
sudo apt update
sudo apt install -y git
```

### CentOS / Rocky / AlmaLinux
```bash
sudo yum install -y git
```

或：

```bash
sudo dnf install -y git
```

### macOS
系统第一次执行 `git` 时，通常会提示安装开发者工具。按提示完成后，再重新执行一次 `git --version`。

---

## 👉 下一步

当下面两件事同时成立，这一页就算通过：

1. 你已经进入一个可以继续执行命令的正确终端。  
2. `git --version` 已经能正常返回版本号。  

下一步：
- [把 Hermes 装上去](./install-hermes.md)
