# 📦 04-把 Hermes 装上去

现在你已经进入了正确终端，并且确认 Git 已经可以正常使用，下一步就是把 Hermes 装上去。

## 📚 官方依据

这一页只走官方推荐的一键安装路径，不展开手动安装、模型配置或第一次互动。

直接把下面这条命令放到当前终端里执行：

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

![Hermes 安装执行截图：在终端里执行官方一键安装命令后，已经开始出现安装输出](../../assets/rm2-2-install-hermes-01-install-command-running.png)

执行后，你应该能看到安装器启动、依赖检查、语言运行时准备或下载相关信息。

如果这里一开始就报错，先检查三件事：

- 安装命令是不是完整复制了
- 当前网络是否正常
- 你是不是还在正确的 Linux / macOS / WSL2 终端里执行

## 🔹 安装后重新加载 shell

安装结束后，先确认你当前用的是哪种 shell：

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

重新加载 shell 的目的是让新的 `hermes` 命令立刻生效。

## ✅ 成功标准

接下来依次执行：

```bash
hermes version
```

```bash
hermes doctor
```

![Hermes 安装成功截图：已经可以执行 hermes version 和 hermes doctor，并看到正常输出](../../assets/rm2-2-install-hermes-02-version-and-doctor-success.png)

如果两条命令都能正常返回结果，就说明安装已经真正完成，而且当前环境可以继续下一页。

如果 `hermes version` 提示 `command not found`：

- 说明 shell 还没正确重新加载，或者 PATH 还没生效

如果 `hermes doctor` 报错：

- 先按它给出的提示修当前环境，再重新执行一次

## 🔹 安装失败时先看这 5 件事

1. 安装命令是否完整复制
2. 当前网络是否正常
3. 当前终端环境是否正确
4. Git 是否已经可用
5. 重新加载 shell 以后，是否再次执行了 `hermes version` 和 `hermes doctor`

一次只修一个基础问题，修完后重新跑验证命令。

## ➡️ 下一步

完成后进入：
- <a href="05-%E9%85%8D%E5%A5%BD%20AI%20%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%B9%B6%E5%AE%8C%E6%88%90%E7%AC%AC%E4%B8%80%E6%AC%A1%E4%BA%92%E5%8A%A8.md">05-配好 AI 大模型并完成第一次互动</a>

如果你想先回到上一阶段入口重新确认位置：
- [上一阶段入口](01-总览.md)
