# Webhook 飞书/钉钉集成工具 (Webhook Notification Tool)

本示例展示了如何为 Hermes Agent 编写一个自定义工具，让它能够将处理结果（如：工作周报、告警信息、代码审查结果）自动发送到飞书或钉钉群机器人。

## 目录结构
- `config.yaml`: 注册自定义工具的配置文件。
- `send_webhook.py`: 核心 Python 脚本，用于调用飞书/钉钉 API。

## 如何配置

1. **获取 Webhook URL**:
   在飞书或钉钉群中添加“机器人”，并复制生成的 Webhook URL。

2. **设置环境变量**:
   ```bash
   export WEBHOOK_URL="https://open.feishu.cn/open-apis/bot/v2/hook/..."
   ```

3. **启动 Hermes**:
   ```bash
   hermes --config config.yaml
   ```

## 实战指令示例
> “帮我把这段代码的 Review 结果通过 Webhook 发送到飞书群里。”
> “把今天的 Daily Report 自动同步到飞书。”
