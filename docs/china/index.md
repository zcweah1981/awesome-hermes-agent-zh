# 国内落地

这不是一篇教你先写 custom endpoint 的配置页，而是 Hermes Agent 面向中国用户的正式落地入口。

先给结论：国内落地的默认路径，应该先判断你要解决的是“先跑起来、控制成本、补齐 provider、还是准备自部署”，而不是一上来就把所有问题都塞进 OpenAI-Compatible 配置。

## 决策结论

国内用户进入 Hermes，优先按下面顺序判断：

1. 只想最快跑通：先走官方 provider，优先看 [国内模型选择](./models.md)
2. 先把试错成本压低：直接看 [最低成本起步](./cost.md)
3. 需要统一接多家国内服务：看 [国内 provider 与聚合商](./providers.md)
4. 已经有内网模型或合规要求：看 [自托管与私有部署](./self-hosting.md)
5. 只有当官方 provider 覆盖不了你的场景时，才回到 [custom-openai-compatible](../custom-openai-compatible.md) 作为参考页

这意味着：`docs/custom-openai-compatible.md` 继续保留，但它不再是国内落地的唯一主入口。

## 适用场景

### 你是第一次在国内环境试 Hermes
你最需要的不是参数表，而是先判断哪条路最稳、最省时间、最不容易把配置写乱。

### 你已经知道会遇到代理、账户或模型可用性问题
你需要先分清到底是模型选择问题、成本问题、provider 问题，还是部署问题，再决定要不要走 custom。

### 你在给团队做内部试点
你需要的是一条可解释、可复用、能逐步放大的决策路径，而不是把所有人都绑在一套临时配置上。

## 行动建议

- 想先找到默认推荐：进入 [国内模型选择](./models.md)
- 想先压低预算再开始：进入 [最低成本起步](./cost.md)
- 想补齐渠道和接入层：进入 [国内 provider 与聚合商](./providers.md)
- 想判断是不是该自部署：进入 [自托管与私有部署](./self-hosting.md)
- 只有确认官方 provider 不满足，再回看 [custom OpenAI-Compatible 参考页](../custom-openai-compatible.md)
