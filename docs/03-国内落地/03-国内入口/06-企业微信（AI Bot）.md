# 企业微信接入指南 (AI Bot)

如果你的团队主协作平台是企业微信，那么这一页将帮你把 Hermes Agent 无缝地“请”进团队，成为每个人的智能助理。

我们将走官方推荐的 **AI Bot 长连接**路线，这种方式无需公网 IP 和复杂的回调配置，稳定又高效。

![企业微信接入主线图](./assets/wecom-entry-structure-v1.webp "一张流程图，展示了从在企业微信创建机器人，到获取凭据，再到配置 Hermes Gateway 并最终建立连接的完整步骤。")

> **一句话结论**：先在企业微信后台创建 AI 机器人拿到凭据，再把凭据填回 Hermes 启动 Gateway，两边就通了。

## 🔎 搜索收录速答

企业微信机器人适合把 Hermes 接到团队群、运维群或内容协作群里，核心链路是：企业微信回调接收消息、服务端调用 Hermes、再把结果回写到群聊。上线前要先处理公网 HTTPS、签名校验、超时重试和权限边界。相关入口还可以对比[飞书](/docs/china/entry/feishu)、[钉钉](/docs/china/entry/dingtalk)和[API 服务与 Open WebUI](/docs/china/entry/api-service-open-webui)。


## 🚀 接入三步走

在开始之前，请确保你的 Hermes Agent 至少已经在命令行（CLI）里跑通了。企业微信是消息入口，不是排错的第一站。

### 第 1 步：在企业微信创建 AI Bot

进入企业微信工作台，找到“智能机器人”功能，创建一个新的机器人。

- **关键点**：选择 **API 模式**，连接方式选择 **使用长连接**。

这是企业微信官方为 Agent 类应用推荐的方式，也是 Hermes 适配器支持得最好的方式。

![企业微信官方创建智能机器人入口截图](./assets/wecom-create-bot-entry-official.webp "企业微信后台创建智能机器人的官方页面截图，清晰地展示了“创建机器人”按钮。")

### 第 2 步：获取凭据

创建成功后，企业微信会提供给你两样关键的东西：
- **Bot ID**
- **Secret**

请妥善保管它们，尤其是 `Secret`，它就像是机器人的密码，绝不能泄露。

### 第 3 步：配置并启动 Hermes Gateway

现在，回到 Hermes Agent 这边。你需要将刚才获取的凭据配置到 `.env` 文件中：

```dotenv
WECOM_BOT_ID=your-bot-id
WECOM_SECRET=your-secret
```

配置好后，启动 Gateway 服务：

```bash
hermes gateway
```

如果终端没有报错，恭喜你！你的 Hermes Agent 已经成功接入企业微信，你可以在对应的机器人聊天窗口里和它对话了。

## ➡️ 下一步

- 如果你还没确定入口形态，先对比[飞书](/docs/china/entry/feishu)、[钉钉](/docs/china/entry/dingtalk)和[API 服务与 Open WebUI](/docs/china/entry/api-service-open-webui)。
- 接入完成后，可以继续了解[实战：服务器自动化运维](/docs/start/practical/server-automation-ops)，学习如何把企业微信作为告警通知入口。

## 📖 出处

- [企业微信智能机器人官方文档](https://developer.work.weixin.qq.com/document/path/101059)
- [Hermes Gateway 相关说明](/docs/china/entry/api-service-open-webui)
