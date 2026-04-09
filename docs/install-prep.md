# Hermes 安装前你需要准备什么

如果你想把 Hermes 一次装顺，这篇比直接复制命令更重要。

---

## 先准备这 5 件事

### 1. 可用的终端环境

推荐：
- macOS Terminal / iTerm2
- Linux Shell
- Windows WSL2
- VS Code 内置终端

不建议把原生 Windows 当主路径。

### 2. 一个可用模型密钥

最常用的准备方式：
- DeepSeek
- Qwen / DashScope
- GLM
- Kimi
- OpenRouter

密钥后续应放到 `~/.hermes/.env`。

### 3. 基本网络条件

你至少要确认：
- 能访问官方安装脚本
- 如果走代理，知道代理端口
- 如果公司网络有证书拦截，准备好排障

### 4. Python / Node 依赖心智

官方安装器会尽量自动处理依赖，但你仍应知道：
- Hermes 不是纯前端工具
- 它会涉及 Python、Node.js、系统命令能力

### 5. 你要先解决的第一个场景

不要装完再想做什么。安装前就确定一个最小目标：
- 跑通第一次对话
- 完成一次 Web 搜索
- 做一次文件处理

---

## 安装前自检清单

- 我有一个稳定终端
- 我有一个模型 key
- 我知道是否需要代理
- 我知道密钥放 `.env`
- 我已经选好第一个验证场景

---

## 下一步

- 直接安装：看 [快速开始](./quick-start.md)
- 先选模型：看 [模型与 Provider](./models.md)
- 遇到环境问题：看 [常见问题](./known-issues.md)
