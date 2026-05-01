# 07-配置 / Profiles / 环境隔离问题

> 一句话结论：这页只处理“为什么改了配置没生效、为什么明明装过却当前看不到、为什么 session / gateway / skills 像跑到别的环境里”这类排障问题；先分清你改的是哪份配置、当前是谁在读、你现在到底在哪个 profile。

如果你现在只想先记住一句：
> 大多数配置问题，不是配置键写错，而是“你改的不是当前生效那份，或者当前运行链路根本没切到你刚改过的环境”。

## ⚡ 先按症状跳转

你现在最像哪一种：

### A. 改了 `config.yaml` / `.env`，结果像没生效
- 看这里：[#01 为什么改了配置却没生效？](#faq-config-not-applied)
- 看这里：[#02 为什么明明写了 key / model / backend，运行时还是老样子？](#faq-old-config)

### B. 一切都像切到了另一套环境
- 看这里：[#03 为什么 profile 切换后，一切都不对了？](#faq-profile-switch)
- 看这里：[#04 为什么我明明装过 / 配过 / 登录过，但当前看不到？](#faq-installed-elsewhere)
- 看这里：[#05 为什么 session 像跑到别的环境里？](#faq-session-other-env)

### C. secret、gateway、skills 像分属不同世界
- 看这里：[#06 为什么 secret / gateway / skills 像分属不同世界？](#faq-secret-gateway-skills)
- 看这里：[#07 为什么同一个 Hermes 在不同入口里表现不一致？](#faq-entry-inconsistent)

### D. 你怀疑其实不是配置问题
- 看这里：[#08 什么时候这更像工具或模型问题？](#faq-config-vs-other)

### E. 你现在需要的是重新整理路线，不是继续试配置键
- 看这里：[#09 什么时候该回 Profiles / 自己造东西相关页？](#faq-back-to-profiles)

## 🩺 先做什么：最小排查动作

先别继续盲改。先把这 4 个问题答出来：

1. 我现在到底在哪个 profile
2. 当前 CLI / gateway / session / skills 读的是不是同一套环境
3. 我改的是当前真的在生效的 `config.yaml` / `.env` 吗
4. 问题是“没写进去”，还是“写进去了但不是这一套环境在用”

如果这 4 个问题你答不清，后面所有改动都容易白改。

## 🚫 先别急着做的事

- 不要一边切 profile，一边改 `.env`、`config.yaml`、gateway
- 不要把“我之前做过这件事”当成“当前环境一定已经有这件事”
- 不要把 session、memory、skills、gateway、secret 混成一个层次
- 不要在没分清环境边界前重复安装或重复登录

## 📌 先记住这 4 个官方基线

### 1）Profile 不是换皮肤，是切整套 Hermes 环境

官方 profile 命令文档说得很清楚：
- `hermes profile use <name>` 会切活动 profile
- 之后不带 `-p` 的 Hermes 命令，都会默认走这套 profile

所以 profile 切换后，下面这些变化很多时候都是正常的：
- `config.yaml`
- `.env`
- sessions
- skills
- memories
- gateway 状态

### 2）最先该会的 profile 命令只有这几个

```bash
hermes profile list
hermes profile use <name>
hermes profile show <name>
hermes config
```

这几条最适合回答：
- 我现在在哪个 profile
- 当前默认活动 profile 是谁
- 这套 profile 的 Hermes home 在哪
- 我现在看到的 config 到底是哪份

### 3）`.env`、`config.yaml`、gateway、skills 本来就不是一层

先强行拆成四层：
1. secret 在 `.env`
2. 行为配置在 `config.yaml`
3. skills 是能力资产
4. gateway 是运行入口

如果你把这四层混成一句“怎么都不对”，几乎一定会误判。

### 4）改完文件，不等于当前运行态已经切过去

官方命令链里最容易被忽略的是：
- 你改的是哪套 profile 下的文件
- 当前 CLI / gateway / session 是不是还在旧运行态
- 你是不是在 profile A 改完，又去 profile B 测

所以“文件已经保存”不等于“当前链路已经生效”。

## ❓FAQ

<a id="faq-config-not-applied"></a>

### 01｜为什么改了配置却没生效？

先说结论：最常见不是配置系统坏了，而是你改的不是当前生效那份文件，或者当前运行链路压根还没重新读取它。

先做什么：
- 先确认当前 profile 是谁
- 先确认你改的是这套 profile 下的配置
- 先确认改完后相关入口有没有重新进入 / 重新启动

重点检查：
- 改错了 profile 的 `config.yaml`
- 改的是 `.env`，但问题其实在 `config.yaml`
- 改的是 `config.yaml`，但当前入口仍在读旧环境
- 你保存了文件，但运行态还没切过去

什么时候该跳转：
- 如果已经确认是 provider / model 层值不对，跳到 [03-模型 / Provider / 自定义 endpoint 问题](<./03-%E6%A8%A1%E5%9E%8B%20Provider%20%E4%B8%8E%E8%87%AA%E5%AE%9A%E4%B9%89%20endpoint%20%E9%97%AE%E9%A2%98.md>)
- 如果核心问题仍是“到底哪份配置在生效”，留在本页

---

<a id="faq-old-config"></a>

### 02｜为什么明明写了 key / model / backend，运行时还是老样子？

先说结论：通常不是 Hermes 忽略了你的配置，而是当前会话、当前入口、当前服务，还停留在旧运行状态。

先做什么：
- 先确认改的是谁在读的配置
- 先确认那个入口有没有重启 / 重进
- 先确认你现在测试的是新会话还是旧会话

高频原因：
- gateway 还在跑旧配置
- 当前 CLI 会话还在旧上下文里
- 你改的是 profile A，却还在 profile B 里测
- 你以为文件改了，运行态就会立即同步

什么时候该跳转：
- 如果你已经确认是 gateway 重启 / 运行态问题，跳到 [05-Gateway / Messaging / 推送问题](<./05-Gateway%20Messaging%20%E4%B8%8E%E6%8E%A8%E9%80%81%E9%97%AE%E9%A2%98.md>)
- 如果本质还是当前环境没切过来，留在本页

---

<a id="faq-profile-switch"></a>

### 03｜为什么 profile 切换后，一切都不对了？

先说结论：因为 profile 不是换皮肤，而是切到另一套完整隔离的 Hermes 环境。你看到差异，很多时候反而是正常的。

先做什么：
- 先接受“profile = 独立环境”这个前提
- 再逐项确认哪些内容本来就应该跟着切换

你应该预期会变化的东西：
- config
- `.env` / secrets
- SOUL
- memories
- sessions
- skills
- cron
- gateway

什么时候该跳转：
- 如果你还没建立 profile 心智，跳到 [02-多个助手一起工作](../01-从这开始/04-自己造东西/02-多个助手一起工作.md)
- 如果你已经知道 profile 是隔离环境，只是当前预期错位，留在本页

---

<a id="faq-installed-elsewhere"></a>

### 04｜为什么我明明装过 / 配过 / 登录过，但当前看不到？

先说结论：最常见不是东西消失，而是它留在另一套 profile、另一套入口，或者另一条运行链路里。

先做什么：
- 先别急着重复安装
- 先回忆上次到底是在什么 profile / 什么入口里做的
- 先确认当前是不是在另一套环境里找上一套环境的东西

常见表现：
- skill 装过，但当前 `skills list` 看不到
- provider 登录过，但当前环境认证状态不对
- gateway 配过，但当前 profile 不认

什么时候该跳转：
- 如果你确认根因就是 profile 隔离，留在本页
- 如果你发现其实根本没装成 / 没配成，跳回对应功能页重查

---

<a id="faq-session-other-env"></a>

### 05｜为什么 session 像跑到别的环境里？

先说结论：最常见不是 session 系统乱了，而是 session 本来就跟当前 profile、当前入口强绑定；你恢复的不是你脑子里那套环境。

先做什么：
- 先分清这是哪个 profile 下的 session
- 先分清这是 CLI session，还是 gateway 的 per-chat session
- 先分清你现在恢复的是哪条链路里的会话

典型混淆：
- 在 profile A 里的会话，去 profile B 里找
- 用 CLI 会话预期去理解消息平台会话
- 在旧环境里保存的会话，去新环境里恢复

什么时候该跳转：
- 如果更像 CLI / TUI 会话理解问题，跳到 [04-CLI / TUI / 会话问题](<./04-CLI%20TUI%20%E4%B8%8E%E4%BC%9A%E8%AF%9D%E9%97%AE%E9%A2%98.md>)
- 如果更像 gateway per-chat 行为，跳到 [05-Gateway / Messaging / 推送问题](<./05-Gateway%20Messaging%20%E4%B8%8E%E6%8E%A8%E9%80%81%E9%97%AE%E9%A2%98.md>)
- 如果根因是环境切错，留在本页

---

<a id="faq-secret-gateway-skills"></a>

### 06｜为什么 secret / gateway / skills 像分属不同世界？

先说结论：因为它们本来就在不同层。secret 多半在 `.env`，配置在 `config.yaml`，skills 是能力资产，gateway 是运行入口；跨 profile 后更不会自动同步成你想的样子。

先做什么：
- 先把层次拆开，不要一句“怎么都不对”带过去
- 先分别确认 secret、config、skills、gateway 在哪套环境里

建议按这 4 层拆：
1. secret 在哪
2. config 在哪
3. skills 在哪
4. gateway 当前用的是哪套环境

什么时候该跳转：
- 如果你主要卡在 gateway 行为，跳到 [05-Gateway / Messaging / 推送问题](<./05-Gateway%20Messaging%20%E4%B8%8E%E6%8E%A8%E9%80%81%E9%97%AE%E9%A2%98.md>)
- 如果你主要卡在 skills / MCP，跳到 [06-Tools / Skills / MCP 问题](<./06-Tools%20Skills%20MCP%20%E9%97%AE%E9%A2%98.md>)
- 如果本质是层次混线和环境隔离，留在本页

---

<a id="faq-entry-inconsistent"></a>

### 07｜为什么同一个 Hermes 在不同入口里表现不一致？

先说结论：你主观上觉得是“同一个 Hermes”，但系统层面可能已经分成不同 profile、不同入口、不同会话、不同运行状态；表现不一致并不奇怪。

先做什么：
- 先不要问“为什么不一致”
- 先问这两个入口是不是同一 profile、同一配置、同一运行状态

最常见差异来源：
- CLI 入口 vs gateway 入口
- profile A vs profile B
- 前台进程 vs 后台服务
- 新会话 vs 旧会话

什么时候该跳转：
- 如果差异主要来自消息平台行为，跳到 [05-Gateway / Messaging / 推送问题](<./05-Gateway%20Messaging%20%E4%B8%8E%E6%8E%A8%E9%80%81%E9%97%AE%E9%A2%98.md>)
- 如果差异主要来自会话交互，跳到 [04-CLI / TUI / 会话问题](<./04-CLI%20TUI%20%E4%B8%8E%E4%BC%9A%E8%AF%9D%E9%97%AE%E9%A2%98.md>)
- 如果你先要整理环境边界，留在本页

---

<a id="faq-config-vs-other"></a>

### 08｜什么时候这更像工具或模型问题？

先说结论：如果你反复遇到“我明明改过 / 装过 / 配过，但当前环境看不到”，更像配置 / Profiles；如果问题是鉴权、endpoint、工具能力边界，则更像模型或工具层。

先做什么：
- 先问自己：问题是“没有”，还是“有但不好用”
- 先问自己：是“改了没生效”，还是“调用时报错”
- 先问自己：是“环境切错”，还是“能力本身坏了”

什么时候该跳转：
- 如果更像 provider / model，跳到 [03-模型 / Provider / 自定义 endpoint 问题](<./03-%E6%A8%A1%E5%9E%8B%20Provider%20%E4%B8%8E%E8%87%AA%E5%AE%9A%E4%B9%89%20endpoint%20%E9%97%AE%E9%A2%98.md>)
- 如果更像 skills / MCP，跳到 [06-Tools / Skills / MCP 问题](<./06-Tools%20Skills%20MCP%20%E9%97%AE%E9%A2%98.md>)
- 如果更像当前环境搞错了，留在本页

---

<a id="faq-back-to-profiles"></a>

### 09｜什么时候该回 Profiles / 自己造东西相关页？

先说结论：只要你现在的问题已经不是“这一份配置哪里写错了”，而是“我到底该怎么组织多助手 / 多环境 / 记忆 / 系统边界”，就不该继续在这页硬试配置键。

先做什么：
- 先回总览，把系统边界重新整理出来
- 再回来改单点配置

这些情况更适合跳转：
- 你还没建立 profile 的整体心智
- 你同时在改助手分工、skills、gateway、memory
- 你更需要的是重新画清环境边界

什么时候该跳转：
- 跳到 [02-多个助手一起工作](../01-从这开始/04-自己造东西/02-多个助手一起工作.md)
- 或跳到 [04-自己造东西](../01-从这开始/04-自己造东西/01-总览.md)

## 🔹 官方依据

- [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
- [FAQ & Troubleshooting](https://hermes-agent.nousresearch.com/docs/reference/faq)
- [CLI Commands Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)
- [02-多个助手一起工作](../01-从这开始/04-自己造东西/02-多个助手一起工作.md)
- [04-自己造东西](../01-从这开始/04-自己造东西/01-总览.md)

## ✅ 看完这页，你应该能立刻判断

- 问题到底是配置值错了，还是当前生效环境搞错了
- 你是不是把多个 profile、多个入口、多条运行链路混在了一起
- 该继续留在配置 / Profiles 层，还是跳去模型页、工具页、gateway 页
- 当前问题到底是“参数问题”，还是“环境隔离问题”

## ➡️ 下一步

完成后进入：

- [08-Docker / Nix / SSH / 远程后端问题](<./08-Docker%20Nix%20SSH%20与远程后端问题.md>)

如果你想先回到上一阶段入口重新确认位置：

- [01-总览](<./01-总览.md>)

---

## 🔗 相关排查入口

- [多个助手一起工作](/docs/start/build/profiles)
- [Profile 命令参考](/docs/reference/profile-commands)
- [上下文系统](/docs/start/build/context-system)
- [OpenClaw 共存指南](/docs/openclaw/coexistence)

如果当前页没有命中症状，先回到[遇到问题总入口](/docs/issues)重新按问题类型分流。
