# 国内主流模型接入总览

为了让 Hermes Agent 在国内环境下运行得最顺畅，我们推荐使用以下经过验证的模型提供商。

## 1. DeepSeek (推荐)
- **官网**: [deepseek.com](https://www.deepseek.com/)
- **特点**: 代码能力极强，响应速度快，API 价格极具竞争力。
- **推荐模型**: `deepseek-chat` (通用对话), `deepseek-coder` (编码辅助)

### 配置方法
```yaml
providers:
  custom:
    - name: "deepseek"
      base_url: "https://api.deepseek.com/v1"
      api_key_env: "deepseek"
      models: ["deepseek-chat", "deepseek-coder"]
```

## 2. 通义千问 (Qwen)
- **官网**: [dashscope.aliyun.com](https://dashscope.aliyun.com/)
- **特点**: 中文语义理解极佳，逻辑能力稳健。
- **推荐模型**: `qwen-max`, `qwen-plus`, `qwen-coder-plus`

### 配置方法
```yaml
providers:
  custom:
    - name: "qwen"
      base_url: "https://dashscope.aliyuncs.com/compatible-mode/v1"
      api_key_env: "qwen"
      models: ["qwen-max", "qwen-coder-plus"]
```

## 3. 智谱 AI (GLM)
- **官网**: [bigmodel.cn](https://open.bigmodel.cn/)
- **推荐模型**: `glm-4`

## 4. MiniMax
- **官网**: [papi.minimax.chat](https://papi.minimax.chat/)

## 5. Kimi (Moonshot)
- **官网**: [moonshot.cn](https://www.moonshot.cn/)

---

### 如何在 Hermes 中动态切换？
启动 Hermes 后，直接输入指令：
` /model custom/deepseek-chat` 或 ` /model custom/qwen-max`
即可实时生效。