# 快速开始 (30秒上手)

Hermes Agent 可以通过一行代码直接启动，本指南将带你使用国内的顶级大模型（如 DeepSeek 或 Qwen）快速跑通你的第一个 Agent。

## 1. 安装 Hermes

如果你使用 macOS 或 Linux，最快的安装方式是 Homebrew：

```bash
brew install nousresearch/hermes/hermes-agent
```

或者使用 `pip` (需要 Python 3.11+)：

```bash
pip install hermes-agent --break-system-packages
```

## 2. 配置国内模型 (DeepSeek)

Hermes 默认使用的是海外模型。为了极速体验，我们可以配置为直接使用国内访问无阻的 DeepSeek。

在你的终端执行以下命令，或者手动修改 `~/.hermes/config.yaml`：

```yaml
# ~/.hermes/config.yaml
api_keys:
  deepseek: "你的_DEEPSEEK_API_KEY"

providers:
  custom:
    - name: "deepseek"
      base_url: "https://api.deepseek.com/v1"
      api_key_env: "deepseek"
      models:
        - "deepseek-chat"
        - "deepseek-coder"
```

## 3. 启动并切换模型

在终端输入 `hermes` 启动交互式 CLI。

进入 CLI 后，输入以下命令切换模型：

```text
/model custom/deepseek-chat
```

现在，你可以用中文问他：“你是谁？你能帮我做什么？” 
你的专属中文 Hermes Agent 已经上线！