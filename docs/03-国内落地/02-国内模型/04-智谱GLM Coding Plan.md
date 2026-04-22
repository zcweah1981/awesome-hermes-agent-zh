# 04-智谱GLM Coding Plan

> 🎯 一句话结论：如果你已经认准智谱，或者你想先走一条单厂商、路径直接、配置明确的 Coding Plan，GLM Coding Plan 值得先看。

## 🚀 接入主线图

![智谱 GLM Coding Plan 深色接入主线图](./assets/glm-coding-hero-v1.png)

先看图，先抓住模型、API Key、工具三个锚点，再看下面的细节。

## ✨ 这条路适合谁

- 你已经认准智谱，想少做横向比较
- 你更喜欢单厂商路径，判断更直接
- 你主要做中文编程、调试、代码库问答
- 你想先把编码工具跑通，再细化模型和工作流
- 你希望一条路里把模型、Key、工具关系看得更清楚

## 🧭 先看最短决策

| 场景 | 建议 |
|---|---|
| 已经决定走智谱这条线 | GLM Coding Plan |
| 重点是中文编码与工具兼容 | GLM Coding Plan |
| 还在多家路线间摇摆 | 先回 [国内模型总览](../01-总览.md) |

## 🤖 它支持哪些模型

官方说明里，GLM Coding Plan 支持这些代表项：

- GLM-5.1
- GLM-5-Turbo
- GLM-4.7
- GLM-4.5-Air

## 🧰 它兼容哪些工具

官方文档明确支持的主流编码工具包括：

- Claude Code
- OpenCode
- TRAE
- CodeBuddy
- Kilo Code
- OpenClaw

对我来说，重点不是工具名越多越好，而是：

- 你能不能先接通
- 接通后能不能稳定切换模型
- 你的日常工作流会不会被打散

## 🤝 Hermes 怎么接

这里要分清两条路：

1. Hermes 官方直连 GLM provider
   - 先用 `hermes model` 选择 Hermes 已内建支持的 provider / model
   - 如果是 GLM / Kimi / MiniMax / DashScope 这类已支持 provider，就把对应 API key 放进 `~/.hermes/.env`
   - 这条路不需要你手动配 `base_url`

2. 只有在你要接 OpenAI-compatible 自建网关时，才走 `custom endpoint` / `base_url`
   - 那时才需要指向真正的 OpenAI-compatible 接口
   - 这不是 Hermes 直连 GLM 的默认路径

所以，如果你的目标只是“让 Hermes 直接用 GLM”，优先看 Hermes 官方 provider 路线；不要先套 Claude Code 那组配置。

## 🔑 接入时最需要记住的点

- 这是单厂商 Coding Plan，不是聚合订阅
- 只在官方支持的工具与产品环境中使用
- 专属 Coding API 端点是 `https://open.bigmodel.cn/api/coding/paas/v4`
- 不要把通用 API 端点当成主线入口
- API Key 先保存到环境变量或配置文件，不要硬编码

## 🧭 先把最短路径跑通

### 1）注册并订阅

- 访问智谱开放平台，完成注册/登录
- 进入 GLM Coding Plan 套餐页，选择适合你的订阅

### 2）获取 API Key

- 在个人中心里进入 API Keys
- 创建新的 API Key
- 复制后妥善保存到本地配置或环境变量

### 3）Hermes 里的正确接法

Hermes 官方文档已经把 GLM 作为内建 provider 支持了，直连方式是：

1. 在 `~/.hermes/.env` 里放入 `GLM_API_KEY`
2. 运行 `hermes model`
3. 在 provider 列表里选择 `Z.AI / GLM`
4. 再选择你要用的模型

这条路就是这页要介绍的主线：

- 不需要手动填写 OpenAI Base URL
- 不需要把 GLM 当成 custom provider 来手填
- provider 名按 Hermes 官方文档写法是 `zai`

最小理解可以写成：

```bash
GLM_API_KEY=***
```

然后在 Hermes 里执行：

```bash
hermes model
# 选择 Z.AI / GLM
# 再选择目标模型
```

你真正要看的，是实际运行 `hermes model` 时的设置界面。看到 `Z.AI / GLM` 高亮后，直接确认即可：

![Hermes model 设置截图：在 Select provider 中直接选择 Z.AI / GLM](./assets/glm-hermes-model-menu-docs.png)

### 4）详细配置方法

先在 `~/.hermes/.env` 中加入你的智谱 API Key：

```bash
GLM_API_KEY=your_z..._key
```

然后运行：

```bash
hermes model
```

进入菜单后按这三个动作完成：

1. 选择 `Z.AI / GLM`
2. 选择模型
3. 保存为默认 provider / model

### 5）验证是否接通

- 能正常进入工具会话
- 能顺利调用 GLM 模型
- 日常任务可以先从 GLM-4.7 开始
- 复杂任务再切到 GLM-5.1 或 GLM-5-Turbo

## ⚠️ 什么时候先别选它

- 你现在只想最低门槛先试跑
- 你还没确定是不是要走单厂商订阅
- 你更想先在多家模型里横向切换

## ✅ 默认建议

- **先体验**：先用 GLM Coding Plan 跑通最小闭环
- **日常使用**：优先 GLM-4.7
- **复杂任务**：再切到 GLM-5.1 或 GLM-5-Turbo
- **工具选择**：先选一个最熟的工具，不要一开始铺太宽

## ➡️ 下一步

- 如果你想继续看另一条单厂商路线，继续看 [MiniMax Token Plan](./05-MiniMax Token Plan.md)
- 如果你还在横向比较，回 [国内模型总览](../01-总览.md)

## 📎 官方依据

- https://hermes-agent.nousresearch.com/docs/integrations/providers
- https://hermes-agent.nousresearch.com/docs/reference/cli-commands
- https://docs.bigmodel.cn/cn/coding-plan/overview
- https://docs.bigmodel.cn/cn/coding-plan/quick-start
- https://docs.bigmodel.cn/cn/coding-plan/faq
