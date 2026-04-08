# 快速开始

本页基于 Hermes Agent 官方文档整理，目标不是重复写一套“民间配置”，而是把官方最新安装流程、官方 provider 能力、以及中文环境下的落地建议合并成一条最短成功路径。

官方参考：
- Installation: https://hermes-agent.nousresearch.com/docs/getting-started/installation
- Quickstart: https://hermes-agent.nousresearch.com/docs/getting-started/quickstart/
- AI Providers: https://hermes-agent.nousresearch.com/docs/integrations/providers/
- Configuration: https://hermes-agent.nousresearch.com/docs/user-guide/configuration/

---

## 这页适合谁

- 第一次安装 Hermes Agent 的中文用户
- 希望优先走官方支持路径，而不是手写大量自定义配置的用户
- 需要使用 DeepSeek、Qwen、GLM、Kimi 等新 provider 的用户

## 你将获得什么

- 一套和官方文档对齐的安装方式
- 一条优先使用 `hermes setup` / `hermes model` 的配置路径
- 一份中文环境下的常见坑说明

---

## 路径 A：推荐安装方式（跟官方保持一致）

官方当前推荐使用一键安装脚本。

### Linux / macOS / WSL2

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc   # 或 source ~/.zshrc
```

说明：
- Windows 原生不作为官方主路径，建议使用 WSL2
- 官方安装器会自动处理大部分依赖，包括 Python、Node.js、ripgrep、ffmpeg、venv 和全局 `hermes` 命令
- 安装结束后通常会进入 setup wizard

### 如果你跳过了初始化

```bash
hermes setup
```

这一步是关键。我们仓库后续所有说明，都默认你优先使用官方交互式配置，而不是直接手改一大段 YAML。

---

## 路径 B：手动安装（适合想完全控制环境的人）

如果你需要可控安装过程，可以走官方手动安装路线：

```bash
git clone --recurse-submodules https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv venv --python 3.11
export VIRTUAL_ENV="$(pwd)/venv"
uv pip install -e ".[all]"
```

然后启动：

```bash
hermes
```

说明：
- 官方文档当前强调 Python 3.11 路线，不建议继续写旧的 3.10+ 口径
- 如果你只想用核心功能，可按官方 extras 拆分安装

---

## 第一步：先用官方 provider，不要急着自定义

这是当前仓库最重要的纠偏。

Hermes 已经内建支持很多 provider，很多国内模型现在不需要再手写 `providers.custom`。优先顺序如下：

1. 用 `hermes model`
2. 用 `hermes setup`
3. 用 `hermes config set`
4. 只有在官方没有一等支持时，才考虑 custom endpoint

### 当前官方已明确支持/文档已列出的 provider

- DeepSeek（provider: `deepseek`）
- Alibaba / DashScope / Qwen（provider: `alibaba`，别名 `dashscope`、`qwen`）
- z.ai / GLM（provider: `zai`）
- Kimi / Moonshot（provider: `kimi-coding`）
- MiniMax（provider: `minimax` / `minimax-cn`）
- OpenRouter
- Anthropic
- Hugging Face
- Nous Portal
- OpenAI Codex
- GitHub Copilot

结论：
- DeepSeek、Qwen、GLM、Kimi 这类主流模型，优先走官方 provider
- 不要再把“custom endpoint”写成默认方案

---

## 第二步：最短成功路径

### 方案 1：交互式选择模型（最推荐）

```bash
hermes model
```

然后：
- 选择 provider
- 输入 API key（如果需要）
- 选择模型
- 直接开始聊天

这是最稳的路径，因为它和官方能力演进同步，不容易因为仓库文档过期而误导用户。

### 方案 2：先写 `.env`，再启动

根据官方文档，密钥优先放在：

`~/.hermes/.env`

示例：

```bash
DEEPSEEK_API_KEY=sk-xxx
DASHSCOPE_API_KEY=sk-xxx
GLM_API_KEY=xxx
KIMI_API_KEY=sk-xxx
OPENROUTER_API_KEY=sk-or-xxx
```

然后运行：

```bash
hermes model
hermes
```

说明：
- secrets 放 `.env`
- 非 secret 配置放 `config.yaml`
- 这和官方 Configuration 文档一致

---

## 第三步：启动对话

```bash
hermes
```

或显式指定：

```bash
hermes chat --provider deepseek --model deepseek-chat
```

如果你要切到 Qwen / DashScope：

```bash
hermes chat --provider alibaba --model qwen-max
```

如果你要切到 GLM：

```bash
hermes chat --provider zai --model glm-4
```

如果你要切到 Kimi：

```bash
hermes chat --provider kimi-coding --model moonshot-v1-auto
```

注意：具体模型可用性会随着官方 provider 更新而变化，因此仓库里更应该强调 provider 路径，而不是把一堆易过时的 model 名称写死。

---

## 中文环境建议

### 1. Windows 用户

官方主路径是 WSL2，不建议继续把原生 Windows 当作主线文档。

### 2. 安装慢

如果你使用的是 pip 安装某些附加依赖，可以临时加国内镜像；但 Hermes 官方主安装路径本身已经尽量自动化，优先相信官方 installer。

### 3. 代理环境

如果你所在网络必须走代理：

```bash
export http_proxy="http://127.0.0.1:端口"
export https_proxy="http://127.0.0.1:端口"
```

### 4. SSL / 证书问题

如果遇到公司网络或代理导致的证书问题，请看本仓库的 `known-issues.md`，不要在 quick-start 里塞太多特殊分支。

---

## 验收标准

你完成本页后，应能做到：

- 成功安装 `hermes`
- 成功执行 `hermes setup` 或 `hermes model`
- 成功配置至少一个官方 provider
- 成功启动一次对话

---

## 下一步

- 模型与 provider 选择：`./models.md`
- 常见问题排查：`./known-issues.md`
- 与 OpenClaw 的差异：`./openclaw-compare.md`
