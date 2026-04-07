# 🤖 Single Agent Starter (国内极速版)

这个模板专为**追求速度和中文理解能力**的个人用户设计。默认接入 DeepSeek，让你在不需要科学上网的情况下，拥有一个最懂中文、响应最快的 AI 助手。

---

## 📂 模板包含 (What's Inside)
- `config.yaml`: 针对国内环境优化的模型配置（预设 DeepSeek）。
- `system_prompt.txt`: 精心调试的中文人设提示词。
- `run.sh`: 一键启动脚本（针对 Linux/macOS）。

---

## 🚀 快速启动 (3步跑通)

### 1. 安装依赖
确保你已经安装了 Hermes CLI。
```bash
pip install hermes-agent
```

### 2. 配置 API Key
在当前目录下执行以下命令设置环境变量：
```bash
export DEEPSEEK_API_KEY="你的_DEEPSEEK_API_KEY"
```
*(或者编辑 `config.yaml` 中的 `api_keys.deepseek` 字段)*

### 3. 一键运行
```bash
# 直接运行命令
hermes --config config.yaml
```

---

## 💡 为什么使用这个模板？
- **国内免翻**: 默认使用 `api.deepseek.com` 接口。
- **中文调优**: 系统提示词经过深度中文对齐，避免模型回复英文。
- **极简结构**: 适合作为你开发更复杂 Agent 的起点。

---
<p align="center">
  Built with ❤️ by <a href="https://hermes-zh.com">Hermes Agent 中文社区</a>
</p>
