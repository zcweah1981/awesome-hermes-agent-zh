# Team Basic Starter (基础多智能体协作模板)

展示了如何使用 Hermes 的 `--acp` 功能和并发任务 (`delegate_task`) 建立一个最基础的“主程序 + 子程序”团队。
这里以一个“开发(Coder) + 测试(QA)”的经典搭配为例。

## 目录结构
- `config.yaml`: 主控节点 (PM/主管) 的配置，定义了如何连接子代理。
- `system_prompt.txt`: 主控节点的人设。
- `coder_system.txt`: 开发智能体的人设。
- `qa_system.txt`: 测试智能体的人设。

## 如何使用

1. **配置环境变量**:
   确保你的国内大模型 API Key 已设置，例如 `export DEEPSEEK_API_KEY="your-key"`。

2. **启动主控节点**:
   ```bash
   hermes --config config.yaml
   ```

3. **下达任务**:
   向主控节点输入指令，例如：“帮我写一个 Python 的贪吃蛇游戏，写完后让 QA 跑一下测试。”
   主控节点会自动通过 `delegate_task` 工具将任务分发给底层的 Coder 和 QA 进行处理。