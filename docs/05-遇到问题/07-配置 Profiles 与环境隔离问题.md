# 07-配置 / Profiles / 环境隔离问题

> 🎯 一句话结论：这一页不是教你从头配一遍 `config.yaml`、`.env` 或 profiles，而是集中回答“为什么改了配置却没生效、为什么明明装过但另一个环境里看不到、为什么 session 像跑到别的环境、为什么 secret / profile / gateway 全混了”这类高频问题。

如果你现在最焦虑，只先记住一句：

> 配置 / Profiles 问题最常见不是 Hermes 完全失效，而是你正在看的那份配置、那套 profile、那条会话链路，根本不是当前真正生效的环境。

## 这页主要回答什么

这一页集中回答这几类高频问题：

- 为什么我改了 `config.yaml` / `.env`，结果像没生效？
- 为什么我明明装过、配过、登陆过，但当前环境里看不到？
- 为什么 session / gateway / skills 像跑到另一套环境里？
- 为什么 profile 切换后，一切都和我预期不一样？
- 什么情况下该把问题归到“环境隔离”，而不是工具、模型或 gateway？

## 先做一个最小判断

如果你现在完全不知道问题卡在哪，先问自己这 4 个问题：

1. 我现在到底在用哪个 profile？
2. 我当前会话、skills、gateway、config 读的是不是同一套环境？
3. 我改的是当前真实生效的 `config.yaml` / `.env` 吗？
4. 我的问题是“配置没写进去”，还是“写进去了但不是当前环境在用”？

很多配置问题，只要先把这 4 个问题分开，基本就不会再盲改。

## ⚡ 快速定位：先看你的问题

如果你不想从头往下读，先按你眼前最像的现象直接跳：

### ⚙️ config / env 改了没生效
- 1️⃣ [为什么我改了 `config.yaml` / `.env`，结果像没生效？](#faq-config-not-applied)
- 2️⃣ [为什么我明明写了 key / model / backend，运行时还是老样子？](#faq-old-config)

### 👥 profile / 环境切换混乱
- 3️⃣ [为什么 profile 切换后，一切都和我预期不一样？](#faq-profile-switch)
- 4️⃣ [为什么我明明装过、配过、登陆过，但当前环境里看不到？](#faq-installed-elsewhere)
- 5️⃣ [为什么 session 像跑到别的环境里？](#faq-session-other-env)

### 🔐 secret / gateway / skills 混线
- 6️⃣ [为什么 secret、gateway、skills 看起来像分属不同世界？](#faq-secret-gateway-skills)
- 7️⃣ [为什么同一个 Hermes，在不同入口里表现不一致？](#faq-entry-inconsistent)

### 🧭 问题边界判断
- 8️⃣ [什么时候该把问题归到配置 / Profiles，而不是工具 / 模型？](#faq-config-vs-other)
- 9️⃣ [什么时候该回 Profiles / 自己造东西相关页，而不是继续在这里硬调？](#faq-back-to-profiles)

> 📌 建议阅读顺序
> - 先看：⚙️ config / env 改了没生效
> - 再看：👥 profile / 环境切换混乱
> - 然后看：🔐 secret / gateway / skills 混线
> - 最后看：🧭 问题边界判断

## ❓FAQ 正文

<a id="faq-config-not-applied"></a>

### ⚙️ 01｜为什么我改了 `config.yaml` / `.env`，结果像没生效？

> ❓ 问题：为什么我改了 `config.yaml` / `.env`，结果像没生效？
>
> 💡 先说结论：最常见原因不是配置系统坏了，而是你改的不是当前生效环境那一份，或者改完以后当前运行链路并没有重新读到它。

最常见原因是：

- 改错了 profile 的配置文件
- 改完以后当前服务 / 入口没重新读取配置
- 你改的是 `.env`，但问题其实在 `config.yaml`
- 你改的是 `config.yaml`，但真正生效的是别的 profile

🔎 先做什么：

先不要继续乱改。
先分清：

- 这是当前 profile 的 `config.yaml` 吗
- 这是当前 profile 的 `.env` 吗
- 当前运行中的 CLI / gateway / 会话会不会重新读取这些值

🚦 什么时候该跳转：

- 如果你已经确认根因在 provider / model，回 [03-模型 / Provider / 自定义 endpoint 问题](<./03-模型 Provider 与自定义 endpoint 问题.md>)
- 如果问题还是“到底哪份配置在生效”，留在本页

---

<a id="faq-old-config"></a>

### ⚙️ 02｜为什么我明明写了 key / model / backend，运行时还是老样子？

> ❓ 问题：为什么我明明写了 key / model / backend，运行时还是老样子？
>
> 💡 先说结论：这通常不是 Hermes 忽略你的配置，而是当前会话、当前入口、当前服务，根本还没切到你刚写的那份运行状态。

最常见原因是：

- 你改完配置，但当前会话还是旧上下文
- 你改完 gateway 用的配置，但没重启 gateway
- 你改的是 profile A，结果还在 profile B 里测
- 你以为“文件保存成功”就等于“运行状态立即切换成功”

🔎 先做什么：

先回答：

- 我改的是谁在读的配置
- 改完以后，那个入口有没有重新启动 / 重新进入
- 我现在是在旧会话里测，还是在新会话里测

🚦 什么时候该跳转：

- 如果你已经确认是旧会话 / 旧服务没刷新，先留在本页
- 如果你发现本质是 gateway 运行层问题，再回 [05-Gateway / Messaging / 推送问题](<./05-Gateway Messaging 与推送问题.md>)

---

<a id="faq-profile-switch"></a>

### 👥 03｜为什么 profile 切换后，一切都和我预期不一样？

> ❓ 问题：为什么 profile 切换后，一切都和我预期不一样？
>
> 💡 先说结论：因为 profile 不是“换个名字”，而是一套完整隔离的 Hermes 环境。你换过去之后，配置、记忆、会话、skills、gateway 本来就可能全部跟着变。

多个助手页已经明确：

- profile 是 fully isolated Hermes environment
- 它拥有独立的 config、env、SOUL、memories、sessions、skills、cron、gateway

也就是说，你切换 profile 之后：

- 看不到旧会话
- 技能列表不一样
- gateway 行为不一样
- key / model / personality 不一样

都不奇怪。

🔎 先做什么：

先把这个前提接受掉：

- 你切的不是“皮肤”
- 你切的是“另一套独立环境”

然后再问：

- 我预期中哪些东西应该跟着变
- 哪些东西我误以为会自动共享

🚦 什么时候该跳转：

- 如果你其实还没建立 profile 心智，回 [02-多个助手一起工作](../01-从这开始/04-自己造东西/02-多个助手一起工作.md)
- 如果只是当前环境隔离导致预期错位，留在本页

---

<a id="faq-installed-elsewhere"></a>

### 👥 04｜为什么我明明装过、配过、登陆过，但当前环境里看不到？

> ❓ 问题：为什么我明明装过、配过、登陆过，但当前环境里看不到？
>
> 💡 先说结论：最常见原因不是东西消失了，而是它被装在另一个 profile、另一个环境、另一条运行链路里。

最常见表现是：

- skill 装过，但当前 profile 里 list 不到
- provider 登陆过，但当前环境里 auth 状态不对
- gateway 配过，但当前 profile 不认

这类问题本质上都是：

- 你记得“我做过这件事”
- 但当前环境并不等于“做过那件事的环境”

🔎 先做什么：

先不要急着重复安装。
先问：

- 我上次是在哪个 profile 里做的
- 当前我是从哪个入口进来的
- 我现在是不是在另一套环境里找上一套环境的东西

🚦 什么时候该跳转：

- 如果你确认就是 profile 隔离，留在本页
- 如果你其实根本没装成，回对应功能页重查

---

<a id="faq-session-other-env"></a>

### 👥 05｜为什么 session 像跑到别的环境里？

> ❓ 问题：为什么 session 像跑到别的环境里？
>
> 💡 先说结论：最常见原因不是 session 系统乱了，而是 session 本来就跟当前 profile / 当前入口强绑定，你现在恢复的不是你脑子里想的那一套环境。

最常见混淆是：

- 你在 profile A 聊出来的会话，跑去 profile B 里找
- 你在消息平台里的 per-chat session，拿 CLI 预期去理解
- 你在旧环境里保存的会话，拿新环境去恢复

🔎 先做什么：

先分清：

- 这是哪个 profile 下的 session
- 这是 CLI session 还是 gateway per-chat session
- 你现在恢复的是哪条链路里的会话

🚦 什么时候该跳转：

- 如果你发现问题更像 CLI / TUI 会话理解不对，回 CLI 页
- 如果问题仍然是环境隔离，留在本页

---

<a id="faq-secret-gateway-skills"></a>

### 🔐 06｜为什么 secret、gateway、skills 看起来像分属不同世界？

> ❓ 问题：为什么 secret、gateway、skills 看起来像分属不同世界？
>
> 💡 先说结论：因为它们本来就在不同层：secret 多半在 `.env`，配置在 `config.yaml`，skills 是能力资产，gateway 是运行入口；你一旦跨 profile，这几层更不会自动保持你想象中的同步。

最常见混淆是：

- 以为 `.env` 里的值会自动解决 skill / gateway 的所有行为
- 以为 skill 装了，gateway 那边自然也会完全等价生效
- 以为 gateway 配过，就说明当前 profile 的 secret 一定已经全对齐

🔎 先做什么：

先把层次拆开：

1. secret 在哪
2. config 在哪
3. skills 在哪
4. gateway 用的是哪套环境

不拆开，你就会一直把四类问题混成一句“怎么都不对”。

🚦 什么时候该跳转：

- 如果你主要卡在 gateway 行为，回 [05-Gateway / Messaging / 推送问题](<./05-Gateway Messaging 与推送问题.md>)
- 如果你主要卡在 skills / MCP，回 [06-Tools / Skills / MCP 问题](<./06-Tools Skills MCP 问题.md>)
- 如果根因是环境隔离，继续留在本页

---

<a id="faq-entry-inconsistent"></a>

### 🔐 07｜为什么同一个 Hermes，在不同入口里表现不一致？

> ❓ 问题：为什么同一个 Hermes，在不同入口里表现不一致？
>
> 💡 先说结论：因为“同一个 Hermes”常常只是你主观上的同一个；在系统层，它可能已经分成了不同 profile、不同入口、不同会话、不同运行状态。

最常见差异来源是：

- CLI 入口
- gateway / 消息平台入口
- profile A 与 profile B
- 当前前台会话与后台服务

这几条链路如果不完全对齐，表现不一致是正常现象，不一定是 bug。

🔎 先做什么：

先不要问“为什么不一致”。
先问：

- 这两个入口到底是不是同一 profile
- 这两个入口到底是不是同一会话 / 同一运行状态
- 这两个入口到底是不是都读了同一套配置

🚦 什么时候该跳转：

- 如果你确认是不同行为来自不同入口，先留在本页整理边界
- 如果差异主要在消息平台行为，回 [05-Gateway / Messaging / 推送问题](<./05-Gateway Messaging 与推送问题.md>)

---

<a id="faq-config-vs-other"></a>

### 🧭 08｜什么时候该把问题归到配置 / Profiles，而不是工具 / 模型？

> ❓ 问题：什么时候该把问题归到配置 / Profiles，而不是工具 / 模型？
>
> 💡 先说结论：如果你反复出现“我明明改过 / 装过 / 配过，但当前环境看不到”的问题，那大概率更像配置 / Profiles；如果问题是明确的鉴权、endpoint、工具能力边界，那更像模型或工具层。

一个很实用的分界线是：

- 配置 / Profiles 层关心的是“当前到底哪套环境在生效”
- 模型层关心的是“推理链路是否通”
- 工具层关心的是“能力有没有接进来”

🔎 先做什么：

先问自己：

1. 我的问题是“没有”，还是“有但不好用”？
2. 我的问题是“改了没生效”，还是“调用报错”？
3. 我的问题是“环境切错”，还是“能力本身坏了”？

🚦 什么时候该跳转：

- 如果你发现更像 provider / model，回 [03-模型 / Provider / 自定义 endpoint 问题](<./03-模型 Provider 与自定义 endpoint 问题.md>)
- 如果更像 skills / MCP，回 [06-Tools / Skills / MCP 问题](<./06-Tools Skills MCP 问题.md>)
- 如果更像当前环境搞错了，留在本页

---

<a id="faq-back-to-profiles"></a>

### 🧭 09｜什么时候该回 Profiles / 自己造东西相关页，而不是继续在这里硬调？

> ❓ 问题：什么时候该回 Profiles / 自己造东西相关页，而不是继续在这里硬调？
>
> 💡 先说结论：只要你现在的问题已经不是“当前这份配置哪里错了”，而是“我到底该怎么组织多助手 / 环境 / 记忆 / 系统边界”，就不该继续在单点配置问题里硬调。

更适合回总览的情况是：

- 你还没建立 profile 的系统心智
- 你在同时改助手分工、skills、gateway、memory
- 你现在更需要重新整理环境边界，而不是继续试一个配置键

🔎 先做什么：

先回到：

- 多个助手一起工作
- 自己造东西总览

把系统边界重新整理出来，再回来改具体配置。

🚦 什么时候该跳转：

- 现在就该回：[02-多个助手一起工作](../01-从这开始/04-自己造东西/02-多个助手一起工作.md)
- 或回：[04-自己造东西](../01-从这开始/04-自己造东西/01-总览.md)

## 🔹 官方依据

- [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
- [FAQ & Troubleshooting](https://hermes-agent.nousresearch.com/docs/reference/faq)
- [CLI Commands Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)
- [02-多个助手一起工作](../01-从这开始/04-自己造东西/02-多个助手一起工作.md)
- [04-自己造东西](../01-从这开始/04-自己造东西/01-总览.md)

## ✅ 看完这页你应该能立刻回答什么

看完这一页，你应该能直接回答这 4 个问题：

1. 我的问题是配置没写进去，还是写进去了但不是当前环境在用？
2. 我是不是把多个 profile / 多个入口 / 多条运行链路混在一起了？
3. 我该继续留在配置 / Profiles 层排查，还是回模型页、tools 页、gateway 页？
4. 我现在的问题到底是“参数问题”，还是“环境隔离问题”？

## ➡️ 下一步

完成后进入：

- [08-Docker / Nix / SSH / 远程后端问题](<./08-Docker Nix SSH 与远程后端问题.md>)

如果你想先回到上一阶段入口重新确认位置：

- [01-总览](./01-总览.md)
