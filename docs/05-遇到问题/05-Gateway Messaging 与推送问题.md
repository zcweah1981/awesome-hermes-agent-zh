# 05-Gateway / Messaging / 推送问题

> 一句话结论：这页只处理“消息为什么没进来、为什么不回、为什么会话乱、为什么 gateway status 不对”这类排障问题；先分清是平台接入层、gateway 运行层，还是会话 / 权限层。

如果你现在只想先记住一句：
> 大多数 Gateway 问题，不是 Hermes 整体坏了，而是“平台没送进来、gateway 没真的在跑、跑的不是这套配置、或者消息被权限 / 会话规则拦住了”。

## ⚡ 先按症状跳转

你现在最像哪一种：

### A. `gateway status` 不正常 / 服务像没起来
- 看这里：[#01 为什么 `hermes gateway status` 不对？](#faq-status-not-ok)
- 看这里：[#02 为什么前台能跑，服务化后反而不对？](#faq-service-vs-foreground)

### B. 平台已经配了，但消息就是收不到
- 看这里：[#03 为什么消息根本收不到？](#faq-message-not-arriving)
- 看这里：[#09 什么时候这其实不是 gateway 问题？](#faq-gateway-vs-platform)

### C. 平台显示已连接，但机器人不回复
- 看这里：[#04 为什么看起来连上了却不回？](#faq-connected-no-reply)
- 如果更像模型报错：跳转到 [03-模型 / Provider / 自定义 endpoint 问题](<./03-%E6%A8%A1%E5%9E%8B%20Provider%20%E4%B8%8E%E8%87%AA%E5%AE%9A%E4%B9%89%20endpoint%20%E9%97%AE%E9%A2%98.md>)

### D. 会话老是断 / 像总在开新对话
- 看这里：[#05 为什么消息平台里像总在开新会话？](#faq-session-reset)

### E. slash 命令、权限、pairing、allowlist 表现怪
- 看这里：[#06 为什么 slash 命令和 CLI 不一样？](#faq-slash-different)
- 看这里：[#07 为什么权限 / allowlist / pairing 不对？](#faq-access-control)

### F. 语音、cron、多平台一起用以后开始混乱
- 看这里：[#08 为什么语音 / 定时任务 / 多平台一起用时容易乱？](#faq-voice-cron-multi)

## 🩺 先做什么：最小排查动作

先不要同时改 token、profile、平台权限、模型配置。
先做这组最小检查：

```bash
hermes gateway setup
hermes gateway status
```

如果你现在是前台跑 gateway，再直接看一次前台输出：

```bash
hermes gateway
```

这一步只想回答 4 个问题：

1. gateway 到底有没有起来
2. 跑起来的是不是你现在这套 profile / 配置
3. 平台消息有没有真的送到 gateway
4. 消息进来后，是不是卡在权限、会话、模型或平台侧规则

## 🚫 先别急着做的事

- 不要一上来就重建机器人 / 重装 Hermes
- 不要同时切 profile、改 token、改平台事件订阅
- 不要把“平台显示在线”直接当成“消息链路正常”
- 不要把“前台能跑”直接当成“服务化配置也一样”

## 📌 先记住这 4 个官方基线

### 1）Gateway 的核心命令要先分清

先记住这几条：

```bash
hermes gateway setup
hermes gateway
hermes gateway status
```

如果你明确要做后台服务，再看：

```bash
hermes gateway install
hermes gateway start
hermes gateway restart
```

官方 CLI 命令参考里给出的重点是：
- `hermes gateway` = 前台运行 gateway
- `hermes gateway setup` = 交互式配置消息平台
- `hermes gateway status` = 查当前服务状态
- `install/start/restart` = Linux / macOS 的服务化链路

### 2）先跑前台，再做服务化

如果你连消息能不能进来都还没证实，先优先：

```bash
hermes gateway
```

而不是一上来就把问题压进后台服务里。

对排障最有价值的是先回答：
- 前台到底有没有收到消息
- 前台收到后有没有立即报错
- 你当前 profile / token / 平台配置是不是真的这套

### 3）平台接通，不等于 gateway 已经可稳定回复

你至少要把链路拆成 3 段：
1. 平台侧机器人 / 应用 / token / callback 配没配好
2. gateway 进程有没有真的在跑
3. 消息进来以后，是卡在权限、会话，还是 provider / model

所以“平台显示在线”只能证明一小段，不等于全链路通了。

### 4）消息平台是多用户入口，不是 CLI 原样镜像

官方 FAQ 明确把 messaging gateway 当成多用户入口。
这意味着：
- 每个平台 / chat 的会话感受可能不同于本地 CLI
- allowlist / pairing / per-chat session 都会影响你体感
- slash 命令、回复方式、会话边界，本来就不等于本地终端

## ❓FAQ

<a id="faq-status-not-ok"></a>

### 01｜为什么 `hermes gateway status` 不对？

先说结论：最常见不是平台坏了，而是 gateway 没跑起来、服务没装好，或者你看的根本不是实际在运行的那一套环境。

先做什么：
- 先分清你现在看的是前台进程，还是系统服务
- 再确认当前 profile 是不是你以为的那个
- 再确认最近改完配置后，gateway 是否真的重启过

重点检查：
- gateway 根本没启动
- 服务安装过，但并没有成功运行
- 你改了配置，但运行中的 gateway 还在读旧配置
- 你以为在看 A profile，实际跑的是 B profile

什么时候该跳转：
- 如果你连 gateway 是否在跑都没搞清，先留在本页
- 如果 gateway 在跑，但平台侧机器人 / 回调 / 事件订阅没配好，跳到 [03-国内入口 / 01-总览](../03-国内落地/03-国内入口/01-总览.md)

---

<a id="faq-service-vs-foreground"></a>

### 02｜为什么前台能跑，服务化后反而不对？

先说结论：前台运行正常，不代表服务化环境也一样。两者最常见差异是 profile、环境变量、工作目录、重启时机没对齐。

先做什么：
- 先确认你在比较的是同一套配置
- 先确认服务重启过，不是旧进程还在跑
- 先确认服务化环境能读到你以为已经存在的 token / config

典型原因：
- 前台在正确 profile 中，服务不是
- 前台 shell 里有环境变量，服务环境里没有
- 你改完配置后只重开了 CLI，没有重启服务
- 你把“前台日志正常”和“后台服务状态健康”当成一回事

什么时候该跳转：
- 如果你还没决定是否真的需要常驻服务，先用前台跑通
- 如果你已经明确需要后台常驻，再继续按本页排查服务边界

---

<a id="faq-message-not-arriving"></a>

### 03｜为什么消息根本收不到？

先说结论：多数不是 Hermes 不收，而是平台侧入口还没打通，或者消息根本没送到正确 bot / chat / 适配器。

先做什么：
- 先确认平台侧机器人 / 应用已创建完成
- 先确认 token、secret、callback、事件订阅都不是半配状态
- 先确认你是在正确的聊天对象里发消息
- 先确认 gateway 的确在运行

最常见原因：
- 平台凭据不完整或填错
- 平台侧权限、事件订阅、回调地址没开全
- 发消息的 chat / user / bot 对象不对
- 你现在查的是平台接入问题，不是 Hermes 运行问题

什么时候该跳转：
- 如果你卡在“机器人怎么建、回调怎么配、权限怎么开”，跳到 [03-国内入口 / 01-总览](../03-国内落地/03-国内入口/01-总览.md)
- 如果平台已接好，只是消息没被 gateway 吃到，留在本页

---

<a id="faq-connected-no-reply"></a>

### 04｜为什么看起来连上了却不回？

先说结论：这通常说明链路只通了一半。消息可能已经进来了，但后面被权限、会话状态、停止状态，或 provider / model 报错卡住了。

先做什么：
- 先区分“完全不回”还是“回复很慢”
- 先区分“所有 chat 都不回”还是“只有一个 chat 不回”
- 先区分“静默没反应”还是“后台其实报错了”

最常见原因：
- gateway 已连上，但当前 chat 没权限
- 当前 agent 在 provider / model 层报错
- 会话已 reset、stop，或被 access control 影响
- 你把“已连接”误读成“已可稳定回复”

什么时候该跳转：
- 如果更像模型、provider、endpoint 问题，跳到 [03-模型 / Provider / 自定义 endpoint 问题](<./03-%E6%A8%A1%E5%9E%8B%20Provider%20%E4%B8%8E%E8%87%AA%E5%AE%9A%E4%B9%89%20endpoint%20%E9%97%AE%E9%A2%98.md>)
- 如果更像某个平台的机器人权限或事件订阅问题，跳到 [03-国内入口 / 01-总览](../03-国内落地/03-国内入口/01-总览.md)

---

<a id="faq-session-reset"></a>

### 05｜为什么消息平台里像总在开新会话？

先说结论：多数不是记忆系统坏了，而是 gateway 本来就按 per-chat session 工作，再叠加 reset policy，你就会感觉“上下文总断”。

先做什么：
- 先确认你是不是换了 chat
- 先确认当前平台是不是触发了 daily / idle reset
- 先确认你期待的是“会话连续”，还是“长期记忆连续”

你要先接受的事实：
- 不同聊天对象，本来就不是同一会话
- 同一聊天对象，也可能因为重置策略切出新会话
- 消息平台里的会话感受，不等于 CLI 会话感受

什么时候该跳转：
- 如果你怀疑是 CLI 会话恢复逻辑搞混，跳到 [04-CLI / TUI / 会话问题](<./04-CLI%20TUI%20%E4%B8%8E%E4%BC%9A%E8%AF%9D%E9%97%AE%E9%A2%98.md>)
- 如果你怀疑是 profile / 环境切错导致“像丢记忆”，跳到 [07-配置 / Profiles / 环境隔离问题](<./07-%E9%85%8D%E7%BD%AE%20Profiles%20%E4%B8%8E%E7%8E%AF%E5%A2%83%E9%9A%94%E7%A6%BB%E9%97%AE%E9%A2%98.md>)

---

<a id="faq-slash-different"></a>

### 06｜为什么 slash 命令和 CLI 不一样？

先说结论：因为消息平台里的 slash commands 是 gateway 暴露出来的控制层，不等于本地 CLI 的完整交互体验。

先做什么：
- 先确认你要的是“聊天里控制 agent”
- 还是“本地终端里的完整交互能力”

你要分清的边界：
- in-chat commands 只覆盖一部分控制动作
- CLI 里的操作边界更完整
- 消息平台的 slash 手感和本地 terminal 不会完全等价

常见误判：
- 以为 CLI 有的交互，平台里也一定一模一样
- 以为 slash 命令异常，就是 gateway 整体坏了
- 以为聊天平台等于完整本地操作台

什么时候该跳转：
- 如果你真正要学的是本地交互和 slash 语义，跳到 [04-CLI / TUI / 会话问题](<./04-CLI%20TUI%20%E4%B8%8E%E4%BC%9A%E8%AF%9D%E9%97%AE%E9%A2%98.md>)
- 如果你查的是消息平台内命令边界，留在本页

---

<a id="faq-access-control"></a>

### 07｜为什么权限 / allowlist / pairing 不对？

先说结论：最常见不是 gateway 随机拒绝，而是当前 access control 规则跟你的使用预期不是一套东西。

先做什么：
- 先回答“谁应该能访问”
- 先回答“现在是私聊、群聊，还是某个平台特殊入口”
- 先回答“当前是 open、allowlist，还是 first-user pairing 一类模式”

典型混淆：
- 你以为任何人都能用，实际开了 allowlist
- 你以为它是公共 bot，实际走的是 pairing
- 你以为私聊和群聊规则一样，实际不是

什么时候该跳转：
- 如果你怀疑平台侧机器人权限没开够，跳到 [03-国内入口 / 01-总览](../03-国内落地/03-国内入口/01-总览.md)
- 如果你已经确认是访问策略预期错位，留在本页

---

<a id="faq-voice-cron-multi"></a>

### 08｜为什么语音 / 定时任务 / 多平台一起用时容易乱？

先说结论：因为这时问题已经不只是“bot 会不会回”，而是“消息从哪来、落到哪个会话、结果发回哪一端、是不是多条链路同时在跑”。

先做什么：
- 先只保留一条最简单链路做验证
- 先用纯文本消息验证平台收发
- 再单独加语音、cron 或第二个平台

高频混淆：
- 你以为 cron 没跑，实际是结果发去了别的平台
- 你以为语音链路坏了，实际文本链路没问题，坏的是转音频这段
- 你以为多个平台共用一条会话，实际是按 chat 分开的

什么时候该跳转：
- 如果你主要在查 cron / 自动化，跳到 [07-让 Hermes 自己自动跑](<../01-%E4%BB%8E%E8%BF%99%E5%BC%80%E5%A7%8B/04-%E8%87%AA%E5%B7%B1%E9%80%A0%E4%B8%9C%E8%A5%BF/07-%E8%AE%A9%20Hermes%20%E8%87%AA%E5%B7%B1%E8%87%AA%E5%8A%A8%E8%B7%91.md>)
- 如果你主要在查消息平台收发，留在本页

---

<a id="faq-gateway-vs-platform"></a>

### 09｜什么时候这其实不是 gateway 问题？

先说结论：只要你当前在解决“平台怎么创建机器人、怎么拿凭据、怎么配 callback、怎么开事件权限”，那本质上就已经是平台接入问题，不是 gateway 运行问题。

先做什么：
- 先问自己：我现在是在查 Hermes 行为，还是在查平台接法
- 只要还没分开，就不要继续混着调

这些情况更适合跳走：
- 你还没确定该走哪种平台接法
- 你还没拿到正确 token / secret
- 你还没完成平台侧机器人 / 应用创建
- 你在比较飞书、企业微信、钉钉、Telegram、Slack 等接入差异

什么时候该跳转：
- 平台接入问题：跳到 [03-国内入口 / 01-总览](../03-国内落地/03-国内入口/01-总览.md)
- Hermes gateway 运行问题：继续留在本页

## 🔹 官方依据

- [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
- [CLI Commands Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)
- [FAQ & Troubleshooting](https://hermes-agent.nousresearch.com/docs/reference/faq)
- [03-国内入口 / 01-总览](../03-国内落地/03-国内入口/01-总览.md)

## ✅ 看完这页，你应该能立刻判断

- 问题到底卡在平台接入、gateway 运行，还是权限 / 会话层
- 当前异常是“消息没进来”，还是“进来了但没回复”
- 该继续查 gateway，还是该回平台入口页
- 该把问题交给模型页、配置页，还是继续留在这里

## ➡️ 下一步

完成后进入：

- [06-Tools / Skills / MCP 问题](<./06-Tools%20Skills%20MCP%20问题.md>)

如果你想先回到上一阶段入口重新确认位置：

- [01-总览](<./01-总览.md>)
