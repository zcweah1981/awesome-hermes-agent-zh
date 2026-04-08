# Hermes vs OpenClaw：深度对比与迁移指南

如果你是 OpenClaw (Clawdbot) 的资深用户，或者正在寻找一个更适合“单人公司 (OPC)”落地的 AI Agent 框架，本指南将帮助你理解 Hermes 的优势并提供平滑迁移方案。

---

## ⚖️ 核心对比 (Technical Audit)

| 特性 | OpenClaw | Hermes Agent (Hermes-Zh) |
| :--- | :--- | :--- |
| **底层协议** | 传统的串行执行 / 轮询 | **ACP (Agent Communication Protocol)**: 原生支持并发协作。 |
| **并发处理** | 模拟并发 (Python threading) | **真并发**: 基于异步流的非阻塞执行。 |
| **工具/技能注册** | 依赖外部脚本 / 复杂 Decorator | **极简 `@skill`**: 自动生成 JSON Schema，3行代码定义工具。 |
| **配置深度** | 零散配置项 | **SSoT**: 所有配置统一在 `config.yaml` 或 `profiles` 下。 |
| **内存开销** | ~1GB+ | **~128MB+**: 极致轻量化设计。 |
| **中国环境** | 手动配置 HTTP_PROXY | **原生加速**: 支持自定义 Base URL (适配 DeepSeek/Qwen)。 |

---

## 🛠️ 技能编写对比

### OpenClaw (传统模式)
```python
# OpenClaw 通常需要显式定义参数 schema
def get_weather(city: str):
    """获取天气
    Args: city (str): 城市名
    """
    pass

# 注册过程通常较繁琐
bot.register_tool(get_weather, schema=...)
```

### Hermes (极简模式)
```python
@skill
def get_weather(city: str):
    """获取指定城市的天气。"""
    return f"{city} 的天气是晴朗。"
```
*Hermes 会自动利用 Python 类型注解解析并注册工具。*

---

## 🚀 迁移步骤

1. **配置对齐**: 将你的 OpenClaw 模型密钥迁移至 `~/.hermes/config.yaml`。
2. **逻辑平移**: OpenClaw 的 Action 逻辑可以直接封装进 Hermes 的 `@skill`。
3. **架构升级**: 如果你在 OpenClaw 中使用多个 Bot 互相私聊，在 Hermes 中应改为使用 `Team` 模式。

---

## 🙋 常见问题 (FAQ)

**Q: 我的 OpenClaw 插件能直接用吗？**  
A: 需要简单包装。将逻辑放入 `skills/your_skill/run.py` 中并添加 `@skill` 装饰器即可。

**Q: 并发能力具体体现在哪？**  
A: 在多智能体团队协作时，Hermes 允许 PM、Coder、QA 同时在线并监听 ACP 广播，而无需等待上一个人彻底结束。
