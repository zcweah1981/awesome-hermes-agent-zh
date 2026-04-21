# 七、千问与 DashScope 接口（第二批）

## 0. 页面信息

**所属栏目**
国内落地 / 模型

**页面类型**
分页面 / 购买与使用说明页

**适合谁**
- 已经决定重点看千问与 DashScope 原生接口的人
- 想在 Hermes 里直接使用阿里云 DashScope / Qwen provider 的人
- 不想走阿里云百炼编程套餐，而是更希望使用原生 API 的人

**这页解决什么问题**
这页只回答 5 个问题：

1. DashScope / Qwen 原生接口到底是什么
2. 它和《一、阿里云百炼编程套餐》有什么区别
3. 怎么获取 API Key、地域和 Base URL
4. Hermes 里应该怎么接
5. 哪些场景更适合走原生 API，而不是走聚合订阅

---

## 1. 这到底是什么

这一页讲的不是阿里云百炼编程套餐，而是 **阿里云 DashScope / Qwen 原生 API 路线**。

Hermes 官方当前已经把 **Alibaba Cloud / DashScope / Qwen** 列成原生 provider，使用的环境变量是 `DASHSCOPE_API_KEY`，provider 名称是 `alibaba`，同时保留 `dashscope` 和 `qwen` 作为别名。这意味着，在 Hermes 里它不是“通过自定义兼容接口勉强接入”，而是官方一等支持的原生 provider。
来源：Hermes AI Providers 文档。

和很多用户直觉不同，这条线与《一、阿里云百炼编程套餐》不是同一个产品：

- **阿里云百炼编程套餐**：聚合型订阅，一份套餐里切多家模型，靠专属套餐 Key 和专属套餐 Base URL 抵扣额度。
- **千问与 DashScope 原生接口**：标准 API 路线，按模型和调用量结算，直接使用 DashScope / 百炼的常规 API Key 与常规 API / OpenAI 兼容地址。

所以这页最重要的结论是：

**这是一条“原生 API”路线，不是一条“聚合订阅”路线。**

---

## 2. 它和阿里云百炼编程套餐到底有什么区别

先把这个问题讲透，不然后面很容易买错、配错、记错。

### 2.1 产品形态不同

阿里云百炼编程套餐是固定月费的聚合型 Coding 订阅；而 DashScope / Qwen 原生接口是按模型、按 tokens 或按请求计费的标准 API。

如果你主要在 Claude Code、Qwen Code、Cline 这类编程工具里工作，而且希望一份套餐里切换多家模型，应该先看《一、阿里云百炼编程套餐》。如果你只是想把 Hermes 或你自己的程序直接接到 Qwen 模型、并按实际调用量付费，那就应该看这一页。

### 2.2 Key 和 Base URL 不同

Hermes 官方环境变量文档明确写了：DashScope 这一条线使用 `DASHSCOPE_API_KEY`，默认 `DASHSCOPE_BASE_URL` 是国际地域的 `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`，中国内地地域要改成 `https://dashscope.aliyuncs.com/compatible-mode/v1`。这已经说明 Hermes 把 DashScope 原生接口当作标准 provider 处理。
来源：Hermes Environment Variables 文档。

而阿里云官方编程套餐文档明确说明，编程套餐必须使用 **套餐专属 API Key** 和 **套餐专属 Base URL**，和普通百炼 / DashScope API Key 不互通。

### 2.3 使用目标不同

- 你想要 **Hermes 原生 provider + 原生 API 路线** → 走本页
- 你想要 **阿里云生态里的聚合订阅 + 多模型切换** → 走《一、阿里云百炼编程套餐》

这是两条完全不同的路径，不要混写。

---

## 3. 什么时候更适合走这条原生 API 路线

这条线更适合三类用户。

### 3.1 你主要用 Hermes，而不是主要用 AI 编程工具套餐

因为 Hermes 已经把 `alibaba / dashscope / qwen` 做成原生 provider。对于 Hermes 用户来说，这条路比“先买编程套餐，再研究套餐专属 Key / Base URL”更直接。

### 3.2 你只想使用千问模型，不想为“多家模型聚合”付费

阿里云模型列表当前明确说明，百炼平台里有丰富的 Qwen 系列模型，例如 `Qwen3.6-Max-Preview`、`Qwen3.6-Plus`、`Qwen3.6-Flash` 等，同时也给出了它们的最大上下文长度和最低输入 / 输出价格。也就是说，如果你已经确定自己主要就是用千问，那么原生 API 路线通常比聚合套餐更干净。
来源：阿里云《模型列表》文档。

### 3.3 你希望把模型接入到自己的程序、工作流或 Hermes 主流程里

阿里云当前官方同时提供：

- DashScope 原生 API
- OpenAI 兼容接口
- 应用 API（智能体 / 工作流）

如果你后面要做的是“程序化调用”和“业务系统集成”，原生 API 路线更自然。

---

## 4. 怎么获取 API Key

阿里云当前官方获取 API Key 的路径很明确：通过百炼 / Model Studio 的密钥管理页面创建 API Key。

这里有三个一定要保留的事实：

1. **API Key 没有失效日期**，手动删除后才失效。
2. 北京和新加坡地域的主账号在每个地域最多可创建 **50 个 API Key**；美国（弗吉尼亚）地域最多 **20 个**。
3. 如果对应 RAM 用户被禁用或删除，该用户创建的 API Key 会失效。
来源：阿里云《获取 API Key》文档。

另外，阿里云还支持 **临时 API Key**，有效期 60 秒，用来给第三方应用或短期授权场景降低长期 Key 泄露风险。这一点很适合后面要做更严格权限控制的团队用户。
来源：阿里云《获取 API Key》文档。

---

## 5. 地域、Base URL 和模型名怎么理解

这条线最容易踩的坑，就是地域、Key 和 Base URL 没对齐。

### 5.1 OpenAI 兼容 Base URL

阿里云《OpenAI Chat 接口兼容》文档当前明确给出了三个地域的兼容地址：

- 北京：`https://dashscope.aliyuncs.com/compatible-mode/v1`
- 弗吉尼亚：`https://dashscope-us.aliyuncs.com/compatible-mode/v1`
- 新加坡：`https://dashscope-intl.aliyuncs.com/compatible-mode/v1`

如果你使用 OpenAI SDK 或其他 OpenAI 兼容 SDK，这是最直接的一组地址。
来源：阿里云《OpenAI Chat 接口兼容》文档。

### 5.2 Hermes 中的默认理解

Hermes 官方环境变量文档当前默认把 `DASHSCOPE_BASE_URL` 写成国际地域的 `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`，并明确提示：如果你在中国内地地域使用，需要改成 `https://dashscope.aliyuncs.com/compatible-mode/v1`。
来源：Hermes Environment Variables 文档。

### 5.3 模型名怎么选

阿里云当前模型列表显示，Qwen 系列已经包含多档旗舰模型，例如：

- `Qwen3.6-Max-Preview`
- `Qwen3.6-Plus`
- `Qwen3.6-Flash`

其中 `Qwen3.6-Max-Preview` 面向复杂任务，`Qwen3.6-Plus` 偏效果、速度、成本均衡，`Qwen3.6-Flash` 更偏简单任务和低成本。
来源：阿里云《模型列表》文档。

所以这页不建议写成“永远推荐某一个模型”。更稳的写法是：

- 要最强效果 → 选 Max / Plus 档
- 要均衡 → 先从 Plus 开始
- 要低成本或高频轻量调用 → 看 Flash 档

---

## 6. Hermes 里怎么接

这条线最大的优势之一，就是 Hermes 已经原生支持，不需要你先走 custom provider。

### 6.1 最短路径

Hermes 官方 provider 文档当前给出的示例是：

```bash
hermes chat --provider alibaba --model qwen3.5-plus
```

并且明确说明需要在 `~/.hermes/.env` 里提供 `DASHSCOPE_API_KEY`。
来源：Hermes AI Providers 文档。

### 6.2 环境变量方式

在 `~/.hermes/.env` 里写：

```env
DASHSCOPE_API_KEY=你的阿里云百炼API_KEY
# 如果你在中国内地，通常还应显式设置：
DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
```

然后在 Hermes 中选择 provider 为 `alibaba` 即可。

### 6.3 为什么不建议先走 custom provider

因为 Hermes 已经把 DashScope 做成了原生 provider。原生 provider 的好处是：

- provider 名称清晰
- 环境变量命名清晰
- 后面在模型总览、入口页、解决方案页里更容易统一写法

只有在你要接一个 Hermes 官方没有原生支持、但兼容 OpenAI 协议的第三方服务时，才更适合走《八、自定义兼容接口（第二批）》。

---

## 7. 官方推荐怎么用

### 7.1 如果你直接在程序里调

阿里云当前官方文档推荐两种常见路径：

- DashScope 原生 API
- OpenAI 兼容接口

如果你已经有 OpenAI SDK 代码，阿里云《OpenAI Chat 接口兼容》文档明确说明：只需要调整 API Key、Base URL 和模型名称，就可以把原有 OpenAI 代码迁移到阿里云百炼服务。
来源：阿里云《OpenAI Chat 接口兼容》文档。

### 7.2 如果你是 Hermes 用户

优先走 Hermes 原生 provider：

- provider：`alibaba`
- key：`DASHSCOPE_API_KEY`
- base_url：按地域决定
- model：用你要的 Qwen 模型名

这条路径比自定义兼容接口更适合写进 Hermes 中文站的主线教程。

### 7.3 如果你是工作流 / 智能体用户

阿里云还单独提供 **应用 API**，用于调用百炼的智能体应用和工作流应用。当前相关文档明确说明，这条接口适用于中国大陆版（北京地域），并要求先完成创建应用、获取 APP ID 和 API Key。
来源：阿里云《应用 DashScope API 参考》《新版智能体应用 API 参考》文档。

所以对这一页来说，最稳的分工是：

- 只要你是“模型调用” → 先用本页路线
- 如果你是“百炼应用 / 工作流调用” → 后续应在第二批另开“应用接口”页

---

## 8. 这页最容易踩的坑

### 坑 1：把它和阿里云百炼编程套餐混成一条线

这是最大的坑。编程套餐和原生 API 不是同一个产品，Key 和 Base URL 都不互通。

### 坑 2：地域和 Key 没对齐

阿里云官方文档反复强调：不同地域使用不同 API Key 和不同地址，跨地域混用会失败。

### 坑 3：在 Hermes 里明明有原生 provider，却先走 custom provider

这会让配置变复杂，也会让后面切换模型和站内教程的统一性变差。对于 DashScope / Qwen 这条线，优先走 Hermes 原生 provider 更合理。

### 坑 4：在总览页或教程页里把价格写死

阿里云模型列表更新很快，旗舰模型和价格会变。对这条线来说，更稳的是引用官方模型列表，并把“最终价格和可用模型以下单页 / 模型列表为准”写清楚。

---

## 9. 这一页的结论

如果你想要的是：

- 在 Hermes 里直接接 Qwen / DashScope
- 不想先买聚合订阅
- 想按标准 API 路线走
- 想把模型接进 Hermes 主流程、程序或业务系统

那 **千问与 DashScope 原生接口** 是一条很标准的路线。它和《一、阿里云百炼编程套餐》最大的差别，不在“模型品牌”，而在 **产品形态**：前者是原生 API，后者是聚合订阅。对 Hermes 中文站来说，这一页未来最适合承担“阿里云 Qwen 原生接入”这一条线，而不是继续让所有阿里云相关内容都压在编程套餐那一页里。

---

## 10. 下一步去哪里

- 如果你想先比较路线 → 回《中国模型总览》
- 如果你想走阿里云聚合订阅 → 去《一、阿里云百炼编程套餐》
- 如果你想继续配 Hermes 入口或使用方法 → 回站内《快速开始》或《入口怎么选》
- 如果你接的是 Hermes 官方没原生支持的兼容服务 → 去 [《八、自定义兼容接口（第二批）》](./八、自定义兼容接口（第二批）.md)
