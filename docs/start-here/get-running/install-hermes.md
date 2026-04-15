# 把 Hermes 装上去

现在你已经进入了运行环境，并且确认 Git 已经可以正常使用，下一步就是把 Hermes 装上去。  
**离开这页时，你应该已经完成 Hermes 安装，并且能正常执行 `hermes` 命令。**

---

## <img src="../assets/icon-run.svg" width="18" alt="安装图标" /> 官方推荐安装方式

这一页只走官方推荐的一键安装路径，不在这里展开手动安装、模型配置或第一次互动。

现在做什么：
- 先按官方推荐方式安装，不要自己拆成一堆手动步骤。

为什么做这一步：
- 第一次安装最重要的是尽快形成闭环，官方一键安装是最短路径。

看到什么算成功：
- 你已经决定这一步直接执行官方安装命令，而不是绕去做额外配置。

如果没看到这个结果，先检查什么：
- 你是不是还在回头研究模型配置或别的高级项。
- 你是不是还没确认 Git 已经可用。

---

## <img src="../assets/icon-build.svg" width="18" alt="执行安装图标" /> 直接开始安装

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

![Hermes 安装执行截图：在终端里输入官方一键安装命令，并已经开始出现安装输出](../assets/rm2-2-install-hermes-01-install-command-running.png)

现在做什么：
- 在当前终端里执行上面的官方安装命令。

为什么做这一步：
- 这条命令会开始安装 Hermes，并自动处理主要安装步骤和依赖准备。

看到什么算成功：
- 终端已经开始出现安装输出。
- 你能看到安装器启动、依赖检查、语言运行时准备或下载相关信息。
- 命令不是一开始就停在明显报错上。

如果没看到这个结果，先检查什么：
- 安装命令是不是完整复制了。
- 当前网络是否正常。
- 你是不是在正确的 Linux / macOS / WSL2 终端里执行。

> <img src="../assets/icon-check-success.svg" width="16" alt="安装提示图标" /> 这张图只负责证明“安装已经开始并在真实执行”，不负责证明“安装已经完成”；安装完成要看下面的验证步骤。

---

## <img src="../assets/icon-terminal-entry.svg" width="18" alt="重新加载图标" /> 安装完成后重新加载当前 shell

先执行下面这条命令，确认你当前用的是哪种 shell：

```bash
echo $SHELL
```

如果结果里是 Bash，再执行：

```bash
source ~/.bashrc
```

如果结果里是 Zsh，再执行：

```bash
source ~/.zshrc
```

现在做什么：
- 先用 `echo $SHELL` 判断自己当前是 Bash 还是 Zsh。
- 再执行对应的 `source` 命令重新加载 shell。

为什么做这一步：
- 安装结束后，重新加载 shell 才能让新的 `hermes` 命令立刻生效。

看到什么算成功：
- `echo $SHELL` 已经让你明确知道自己当前用的是哪种 shell。
- `source` 命令执行后没有报错。
- 终端回到提示符，允许继续输入下一条命令。

如果没看到这个结果，先检查什么：
- 你是不是搞错了自己当前使用的 shell。
- 对应的配置文件是否存在。
- 你是不是执行了和当前 shell 不对应的 `source` 命令。

---

## <img src="../assets/icon-check-success.svg" width="18" alt="验证安装图标" /> 检查有没有安装成功

先执行：

```bash
hermes version
```

再执行：

```bash
hermes doctor
```

![Hermes 安装成功截图：已经可以执行 hermes version 和 hermes doctor，并看到正常输出](../assets/rm2-2-install-hermes-02-version-and-doctor-success.png)

现在做什么：
- 先执行 `hermes version`。
- 再执行 `hermes doctor`。

为什么做这一步：
- 只有这两条命令都能正常工作，才说明安装真正完成，而且当前环境适合进入下一步。

看到什么算成功：
- `hermes version` 返回真实版本信息。
- `hermes doctor` 返回可继续使用的检查结果。
- 执行完后，终端回到提示符，可以继续下一页。

如果没看到这个结果，先检查什么：
- 如果 `hermes version` 提示 `command not found`：说明 shell 还没正确重新加载，或者 PATH 还没生效。
- 如果 `hermes doctor` 报错：先按它给出的提示修当前环境，再重新执行一次。

---

## <img src="../assets/icon-check-success.svg" width="18" alt="排查图标" /> 安装失败时先看什么

先只查下面这 5 件事：

1. 安装命令是否完整复制。  
2. 当前网络是否正常。  
3. 当前终端环境是否正确。  
4. Git 是否已经可用。  
5. 重新加载 shell 以后，是否再次执行了 `hermes version` 和 `hermes doctor`。  

现在做什么：
- 只要有一步没过，就先回到这组最小检查，不要直接跳到模型配置页。

为什么做这一步：
- 这一页的目标不是“命令跑过”，而是“安装已经真正完成并可进入下一页”。

看到什么算成功：
- 你已经定位到问题是在命令、网络、终端环境、Git，还是 shell 生效这几个基础项之一。

如果没看到这个结果，先检查什么：
- 你是不是还没有把报错落到具体一项。
- 你是不是在安装没闭环之前就想往后跳。

---

## 👉 下一步

当下面两件事同时成立，这一页就算通过：

1. 终端已经能识别 `hermes` 命令。  
2. 你执行 `hermes version` 和 `hermes doctor` 时，都已经看到正常输出。  

下一步：
- [配好 AI 大模型并完成第一次互动](./first-hello.md)
