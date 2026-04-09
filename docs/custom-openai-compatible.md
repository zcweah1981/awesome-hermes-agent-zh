# Hermes 自定义 OpenAI-Compatible 接口配置指南

当官方 provider 不覆盖你的模型服务时，才需要这篇文章。

这篇不会把 custom endpoint 写成默认路径，而是告诉你：什么时候该用，怎么用，怎么避免把配置写乱。

---

## 什么情况下才需要 custom endpoint

只有这些情况才建议你走这条路：
- 你在用自建 vLLM / SGLang / OpenAI-compatible 网关
- 你接的是官方暂未内建的一家服务
- 你必须使用自定义 base URL、模型名或鉴权方式

如果你用的是：
- DeepSeek
- Qwen / DashScope
- GLM
- Kimi

那通常应该优先走 [模型与 Provider](./models.md) 里的官方 provider 路线。

---

## 配置原则

### Secret 放 `.env`

例如：

```bash
CUSTOM_API_KEY=***
```

### 参数放 `config.yaml`

例如：
- base_url
- model
- temperature
- provider 名称

这样做的好处是：
- 密钥不进仓库
- 参数更容易维护
- 更符合 Hermes 的配置习惯

---

## 一个最小示例

```yaml
providers:
  custom:
    mygateway:
      api_key_env: CUSTOM_API_KEY
      base_url: https://api.example.com/v1
      models:
        - name: my-chat-model
          mode: chat
```

说明：
- `api_key_env` 指向 `.env` 中的变量名
- `base_url` 指向你的 OpenAI-compatible 服务
- `models` 使用列表结构，方便后续挂多个模型

---

## 推荐使用方式

### 方式 1：只把 custom 当补充

最稳的做法是：
- 主模型走官方 provider
- 特殊模型或内部模型走 custom

### 方式 2：一个网关下挂多个模型

适合：
- 你有统一代理层
- 你想在一个 provider 下接多个模型
- 你想减少配置碎片

---

## 常见错误

### 错误 1：把密钥写进 `config.yaml`

不推荐。密钥应放 `.env`。

### 错误 2：把所有模型都塞进 custom

如果官方已支持，就不要人为增加复杂度。

### 错误 3：只写 base_url，不校验模型名

很多问题不是 URL 错，而是模型名不对。

---

## 验收标准

配置完后，你应该能回答：
- 为什么这里必须用 custom，而不是官方 provider
- 密钥应该放在哪
- 参数应该放在哪
- 一个 provider 下怎么挂多个模型

---

## 下一步

- 想先判断是否真需要 custom：看 [模型与 Provider](./models.md)
- 想先完成基础安装：看 [快速开始](./quick-start.md)
