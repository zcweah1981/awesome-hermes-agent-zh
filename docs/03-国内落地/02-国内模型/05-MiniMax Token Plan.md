# 05-MiniMax Token Plan

MiniMax Token Plan 这一页，只讲一件事：如果你已经订阅了 MiniMax Token Plan，怎么在 Hermes 里直接接上它。

## 这条路适合谁

- 你想在国内路线里优先考虑 MiniMax
- 你不只看文本能力，也看图像、语音、音乐、视频这些更宽的能力面
- 你接受先走订阅，再把 Hermes 跑通
- 你希望直接按 Hermes 官方支持方式接入，而不是自己手填兼容接口

## 你最需要记住的点

MiniMax Token Plan 在 Hermes 里是支持直接接入的。

对这条国内落地页来说，主线不是自定义 endpoint，而是：

- 先订阅 MiniMax Token Plan
- 获取 Token Plan 专属 API Key
- 在 Hermes 里运行 `hermes model`
- 选择 `MiniMax China (mainland China endpoint)`
- 再选择 `MiniMax-M2.7`

## 什么时候先别选它

- 你现在只想最低门槛先把 Hermes 跑起来
- 你更想先用按量计费，而不是订阅制
- 你还没确定自己是否真的需要 MiniMax 的更宽模态能力
- 你只是想先跑一个最小文本闭环，那 GLM / Kimi 往往更直接

## 1）先开通 Token Plan

先到 MiniMax Token Plan 订阅页完成开通：

- 进入 `Token Plan` 套餐页
- 选择适合你的套餐
- 完成订阅

官方文档里已经明确说明，Token Plan 是对原来 Coding Plan 的升级，核心特征是：

- 文本模型按 5 小时滚动额度计算
- 其他模型按每日配额计算
- 一个订阅覆盖多模态能力

## 2）获取 Token Plan API Key

订阅完成后，再去 Token Plan 页面查看有效套餐并获取 API Key。

这里要特别注意两点：

- 这是 `Token Plan API Key`
- 它和 MiniMax 按量计费的普通 API Key 不是同一个东西

如果你拿错 Key，后面在 Hermes 里就会配不通。

## 3）Hermes 里的正确接法

Hermes 官方文档和 MiniMax 官方 Hermes Agent 页面，都已经把这条路写清楚了。

对国内落地这页，推荐按下面这条主线走：

1. 在 `~/.hermes/.env` 中放入 `MINIMAX_CN_API_KEY`
2. 运行 `hermes model`
3. 在 provider 列表里选择 `MiniMax China (mainland China endpoint)`
4. 再选择 `MiniMax-M2.7`

这条路就是这页要介绍的主线：

- 不需要手动填写额外的 endpoint
- 不需要把 MiniMax Token Plan 当成自定义接口去手填
- Hermes 官方 provider 名写法是 `minimax-cn`
- 这页讲的是国内落地，所以应优先选 `MiniMax China`，不要误选 global endpoint

最小理解可以写成：

```bash
MINIMAX_CN_API_KEY=***
```

然后在 Hermes 里执行：

```bash
hermes model
# 选择 MiniMax China (mainland China endpoint)
# 再选择 MiniMax-M2.7
```

下面这张图，就是 MiniMax 官方 Hermes Agent 文档里给出的 provider 选择界面：

![Hermes model 设置截图：选择 MiniMax China (mainland China endpoint)](./assets/minimax-hermes-provider-cn.png)

接下来再选择模型时，官方页面给出的界面如下：

![Hermes model 设置截图：选择 MiniMax-M2.7](./assets/minimax-hermes-model-select.png)

## 4）详细配置方法

先在 `~/.hermes/.env` 中加入你的 Token Plan Key：

```bash
MINIMAX_CN_API_KEY=***
```

然后运行：

```bash
hermes model
```

进入菜单后按这三个动作完成：

1. 选择 `MiniMax China (mainland China endpoint)`
2. 选择 `MiniMax-M2.7`
3. 保存为默认 provider / model

如果你已经在 Hermes 里看到 MiniMax 的多个入口，当前这条国内落地主线要记住一件事：

- 这页优先用 `MiniMax China (mainland China endpoint)`
- 不要把 `MiniMax (global endpoint)` 当成这页默认答案

## 5）验证是否接通

完成后可以按下面几个信号判断是否已经接通：

- `hermes` 可以正常进入会话
- 默认模型已经切到 MiniMax
- 可以正常发起对话或任务
- 没有再提示你补 provider 或重新配置 API Key

如果你想先做最小验证，直接运行：

```bash
hermes
```

能正常进入并开始对话，基本就说明这条路已经打通了。

## ⚠️ 常见问题

### 1. 为什么我已经有 MiniMax Key，还是配不通？

先检查你拿的是不是 `Token Plan API Key`。

MiniMax 官方文档明确说了：

- `Token Plan API Key` 与按量付费 API Key 不可互换
- 这页讲的是 Token Plan，所以不要混用按量 API Key

### 2. Hermes 里应该选哪个 provider？

这页默认答案是：

- `MiniMax China (mainland China endpoint)`

不要把这页理解成别的接入路线，这一页的默认答案就是 Hermes 里的 `MiniMax China (mainland China endpoint)`。

### 3. 为什么还会看到 global endpoint？

因为 Hermes 同时支持 MiniMax 的不同入口。

但当前这页是国内落地页，所以默认优先写中国大陆 endpoint，对应 `minimax-cn`。

### 4. MiniMax-M2.7 和 MiniMax-M2.7-highspeed 怎么选？

如果你只是先跑通 Hermes，先从 `MiniMax-M2.7` 开始更稳。

后续再根据你订阅的套餐和实际速度需求，决定是否切到 `MiniMax-M2.7-highspeed`。

## ✅ 默认建议

- **先跑通**：先用 `MINIMAX_CN_API_KEY + hermes model` 跑通最小闭环
- **先选 provider**：优先选 `MiniMax China (mainland China endpoint)`
- **先选模型**：优先从 `MiniMax-M2.7` 开始
- **先做验证**：先确认 Hermes 能正常进入会话，再去折腾更高阶模型或更复杂工作流

## ➡️ 下一步

- 如果你想继续看另一条国内订阅路线，继续看 [Kimi登月计划](./06-Kimi登月计划.md)
- 如果你还在横向比较，回 [国内模型总览](../01-总览.md)

## 📎 官方依据

- https://platform.minimaxi.com/subscribe/token-plan
- https://platform.minimaxi.com/docs/token-plan/intro
- https://platform.minimaxi.com/docs/token-plan/hermes-agent
- https://hermes-agent.nousresearch.com/docs/integrations/providers
