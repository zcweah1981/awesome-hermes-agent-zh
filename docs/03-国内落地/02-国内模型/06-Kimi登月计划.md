# 🌙 06-Kimi登月计划

> 先分清手中的凭据属于 Moonshot 开放平台 API，还是 Kimi Code。Hermes 的 `kimi-coding` 名称不能单独说明计费路线：实际 endpoint 还取决于 Key 类型和显式覆盖配置。

复核日期：2026-09-30；依据 Hermes 官方稳定标签 **v2026.9.24（v0.21.5）**。完成文档与源码核对，未购买套餐或进行 API 调用测试。价格、会员权限、额度和可用模型请在厂商页面核对。

## 👀 适合谁

已有 Kimi / Moonshot 凭据，想正确接入 Hermes 的用户。还没准备模型账户时，可先看[国内模型总览](./01-总览.md)和[DeepSeek 按量接口](./07-DeepSeek按量计费接口.md)。

![Kimi 产品路线历史示意图](./assets/kimi-moonshot-modules-cliproxy-v2.webp)

> 图是历史产品路线示意，接入应以下面的官方原生 provider 与 Key 类型为准；不需要因为这张图先搭第三方代理。

## 🔀 两条产品路线和 Hermes 的实际映射

| 你持有的凭据 | Hermes 环境变量 / provider | 默认 endpoint | 需要核对 |
|---|---|---|---|
| Moonshot 国际开放平台 API Key | `KIMI_API_KEY` / `kimi-coding` | `https://api.moonshot.ai/v1` | 国际账户、余额、模型权限 |
| Moonshot 国内开放平台 API Key | `KIMI_CN_API_KEY` / `kimi-coding-cn` | `https://api.moonshot.cn/v1` | 国内账户、余额、模型权限 |
| Kimi Code Key（`sk-kimi-` 前缀） | 原生 Kimi provider；国际 provider 也接受 `KIMI_CODING_API_KEY` 别名 | 自动识别为 `https://api.kimi.com/coding` | Code Key 是否有效、当前套餐是否允许目标用法 |

默认 Moonshot 映射不因 provider 名称含 `coding` 而失效。另一方面，稳定版源码也确实支持按 `sk-kimi-` 前缀识别 Code endpoint，因此不能写成“接 Hermes 只能走开放平台 API”。

`KIMI_BASE_URL` 显式覆盖会优先于 Key 前缀识别。排障时检查是否遗留覆盖，而不只是反复换 Key。会员登录凭据、普通网页会话与 API Key 是不同的东西；持有会员不等于已经生成可用 Key。

厂商 SDK 示例中的 `MOONSHOT_API_KEY` 是示例变量名，不能照搬成 Hermes 原生 provider 配置。使用上表中 Hermes 实际读取的变量。

## ✍️ 上手步骤

### 1. 确认账户与 Key 类型

在 [Kimi Code 文档](https://www.kimi.com/code/docs/)或 [Moonshot 开放平台](https://platform.kimi.ai/docs/guide/start-using-kimi-api)确认 Key 来源、模型权限及计费规则。套餐价格以[官方会员页](https://www.kimi.com/membership/pricing)实时显示为准。

### 2. 使用模型向导

```bash
hermes model
```

选择对应 Kimi provider，按向导输入 Key 与当前可用模型。默认 profile 的环境变量文件位于 `~/.hermes/.env`，自定义 profile 应使用自己的凭据范围。不要把 Key 粘到聊天记录、截图、教程或 Git 仓库中。

需要直接配置 `.env` 时，开放平台国际与国内 Key 分别使用：

```dotenv
# 国际开放平台：
KIMI_API_KEY=替换为真实密钥
# 国内开放平台：
KIMI_CN_API_KEY=替换为真实密钥
```

按自己的路线填写对应变量，不要把相同 Key 同时放进两种账户线路。Kimi Code Key 按原生 provider 向导配置，并确认实际 endpoint；不要因为变量配置完成就认为账户权益已经验证。

### 3. 做一次最小问答

```bash
hermes doctor
hermes chat -Q -q "请只回复：连接正常。"
```

这是实际模型请求，可能消耗额度或产生费用。收到正常回复后，再在你的账户用量页面检查扣费或额度变化；一次成功不能证明持续稳定、所有模型或全部工具都可用。

### 4. 再验证实际任务

用不含敏感资料的小任务检查工具调用、流式回复和长上下文。如果换模型或 endpoint，需要重新验证；模型目录中有名字不等于账户具备调用权限。

## 🩺 常见问题

| 现象 | 先检查 |
|---|---|
| 401 / 无效 Key | Key 来源与 provider 匹配、变量名、profile、是否复制错误 |
| 余额不足或权益受限 | 开放平台余额与 Code 套餐分别核对，检查请求的实际 endpoint |
| 模型不存在 | 精确模型 ID、地区可用性、账户权限；不要沿用旧目录里的名字 |
| Code Key 去了 Moonshot endpoint | Key 是否为 `sk-kimi-` 前缀、是否存在 `KIMI_BASE_URL` 覆盖 |
| `.env` 已写但仍读旧配置 | 当前 profile、进程加载配置的时机；重启实际使用的入口后复测 |
| 流式输出异常 | 记录安装版本与错误；后续主干修复是否已进入你的安装版本需单独核对 |

## ✅ 过关标准

- 知道 Key 的产品与地区来源，能解释当前 provider 和实际 endpoint。
- 最小问答与目标任务成功，账户用量可核对。
- 没有把会员购买、模型目录或文档源码复核当成 API 联调通过。

## 📎 官方依据

- [稳定标签 Provider 说明](https://github.com/NousResearch/hermes-agent/blob/v2026.9.24/website/docs/integrations/providers.md)。
- [稳定标签凭据与 provider 注册](https://github.com/NousResearch/hermes-agent/blob/v2026.9.24/hermes_cli/auth.py)。
- [稳定标签 Kimi endpoint 解析](https://github.com/NousResearch/hermes-agent/blob/v2026.9.24/hermes_cli/auth_zai_kimi.py)：Key 前缀识别与显式覆盖优先级。
- [Kimi Code 官方文档](https://www.kimi.com/code/docs/)、[Moonshot API 官方文档](https://platform.kimi.ai/docs/guide/start-using-kimi-api)：使用时复核账户和模型。

## ➡️ 下一步

- 下一步：[07-DeepSeek 按量计费接口](./07-DeepSeek按量计费接口.md)
- 回到：[02-国内模型总览](./01-总览.md)
- 配置其他接口：[自定义兼容接口](/docs/china/models/openai-compatible-endpoint)
- 排障：[模型 Provider 与自定义 endpoint 问题](/docs/issues/provider-endpoint)
