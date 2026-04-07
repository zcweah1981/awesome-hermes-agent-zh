# Single Agent Starter (国内模型版)

这是一个最基础的单智能体模板，专为国内开发者设计。它默认配置了国内顶流的大模型（如 DeepSeek），让你无需科学上网也能跑通 Hermes。

## 目录结构
- `config.yaml`: 包含模型提供商和快捷指令的配置文件。
- `system_prompt.txt`: Agent 的人设与系统提示词。

## 如何使用

1. **配置 API Key**:
   打开 `config.yaml`，将 `api_keys.deepseek` 替换为你自己的 DeepSeek API Key。
   *(或者设置环境变量 `export DEEPSEEK_API_KEY="your-key"`)*

2. **启动 Agent**:
   在当前目录运行以下命令：
   ```bash
   hermes --config config.yaml
   ```

3. **开始对话**:
   一旦进入交互界面，Agent 就会自动使用 `deepseek-chat` 模型并加载预设的人设。
