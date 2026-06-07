# 04-CLI / TUI / 会话问题

> 一句话结论：这一页只处理“界面显示怪、按键像没反应、slash command 不出现、会话恢复不对、看起来像卡住了”这类问题。只要 `hermes` 能启动，很多时候就不是“完全坏了”，而是入口、交互方式、会话预期或终端环境没对齐。

如果你现在很急，先记住：
> 先分清你卡的是显示层、交互层、会话恢复层，还是模型响应层；不要把“界面怪”和“模型坏”混成一件事。

## 📋 速答（你可能正在搜的）

**Hermes Agent 的 TUI 和 CLI 有什么区别？**
> Classic CLI（`hermes`）是传统终端交互模式，兼容性最好。TUI（`hermes --tui`）是增强终端界面，额外支持鼠标跟踪、`/reload` 热重载、`/usage` token 统计、`/details` 详细模式、Ctrl+X 快速切换历史会话、可折叠启动 Banner。两个模式共享同一套 slash commands 核心，但 TUI 有更多交互增强。

**什么时候用 TUI，什么时候用 CLI？**
> 日常深度使用选 TUI——更好的视觉反馈和交互效率。SSH 远程连接或终端兼容性差时选 classic CLI——更轻量、兼容性更好。如果你遇到界面乱码、emoji 不显示，先试 classic CLI 排除终端兼容问题。

**TUI 模式怎么启动？**
> 运行 `hermes --tui`。TUI 独有命令包括 `/mouse`（鼠标跟踪）、`/reload`（热重载配置和 skills）、`/usage`（token 统计）、`/details`（详细输出）。这些在 classic CLI 和消息平台不一定可用。

## ⚡ 先按症状选路

你现在最像哪一种，直接跳：

### 📟 显示 / UI 异常
- 乱码、错位、emoji 不显示
- 界面看起来很怪
- classic CLI 和 `--tui` 表现差很多
- 先看：[01｜为什么 CLI / TUI 看起来乱码、错位、emoji 不显示](#faq-ui-garbled)
- 先看：[02｜为什么我明明进了 Hermes，但界面看起来很怪](#faq-ui-weird)
- 先看：[02.5｜TUI 和 classic CLI 表现不一样，怎么判断是 bug 还是正常差异](#faq-tui-vs-cli)

### ⌨️ 交互 / slash / 退出方式不符合预期
- 输入 `/` 没看到命令补全
- 不确定自己是不是在交互模式里
- Ctrl+C、清屏、退出、继续会话概念混了
- 先看：[03｜为什么输入 `/` 没看到命令或补全](#faq-slash-not-showing)
- 先看：[04｜为什么 Ctrl+C、清屏、退出这些动作和我想的不一样](#faq-ctrlc-exit)

### 💾 会话 / 恢复 / 前文记忆异常
- 退出后感觉前文没了
- `--continue` / `--resume` 恢复出来的不是想要的会话
- 看起来像“不记得前文”，但又不是完全新会话
- 先看：[05｜为什么退出以后感觉前文丢了](#faq-session-feels-lost)
- 先看：[06｜为什么 `--continue` / `--resume` 恢复出来的不是我想要的会话](#faq-continue-resume)
- 先看：[07｜为什么它看起来“不记得前文”](#faq-context-not-remembered)

### 🛑 卡顿 / 假死 / 长时间没反馈
- 输入后很久没反应
- 不确定是 CLI 卡住还是模型慢
- 先看：[08｜为什么界面像卡住了，输入后很久没反应](#faq-stuck)
- 先看：[09｜什么时候该把问题当成 CLI / TUI，而什么时候其实是模型 / Provider 在拖慢](#faq-cli-vs-provider)

## 🧪 先做最小判断

先做这组最小动作：

```bash
hermes version
hermes
```

进入后只做两件事：
- 输入 `/`，看命令补全是否出现
- 退出后再试：

```bash
hermes --continue
```

怎么理解结果：
- 连 `hermes` 都进不去：先回 [02-安装 / 更新 / 环境问题](./02-安装更新与环境问题.md)
- 能进，但 slash / 显示 / 恢复行为怪：继续留在本页
- 能进、交互也正常，但结果慢、报鉴权、报 endpoint：更像 [03-模型 / Provider / 自定义 endpoint 问题](<./03-%E6%A8%A1%E5%9E%8B%20Provider%20%E4%B8%8E%E8%87%AA%E5%AE%9A%E4%B9%89%20endpoint%20%E9%97%AE%E9%A2%98.md>)

## ✅ 先做什么：4 步排查清单

1. 先分清你在用的是哪种入口
   - `hermes` = classic CLI
   - `hermes --tui` = modern TUI
2. 再分清你是不是在交互式会话里
3. 再分清你是想“退出”“清屏”还是“下次继续回来”
4. 最后才怀疑是不是模型 / provider 响应把界面拖慢了

高频误判：
- 把 classic CLI 和 TUI 的差异当成 bug
- 把 shell 单次命令当成交互会话
- 把重新启动 `hermes` 当成自动恢复旧会话
- 把模型慢当成 CLI 假死

## ❓FAQ

<a id="faq-ui-garbled"></a>

### 01｜为什么 CLI / TUI 看起来乱码、错位、emoji 不显示

先说结论：最常见不是 Hermes 会话坏了，而是终端字体、终端宽度、emoji 渲染或当前终端环境本身不适合显示这些字符。

先做什么：
- 先把终端窗口拉宽
- 换一个正常的本地终端再试
- 先验证最基础交互是否正常，不要只盯着字符长相

怎么判断这只是显示层：
- `hermes` 能启动
- 能正常输入
- 能正常返回内容

只要上面三件事都正常，这更像显示问题，不是功能问题。

什么时候该跳转：
- 连 `hermes` 都进不去：回 [02-安装 / 更新 / 环境问题](./02-安装更新与环境问题.md)
- 只是字符不好看，但功能正常：先留在本页，不必上升到模型层

---

<a id="faq-ui-weird"></a>

### 02｜为什么我明明进了 Hermes，但界面看起来很怪

先说结论：很多“界面很怪”的问题，本质上是你在用的不是你以为的那个入口，或者把 classic CLI 和 `--tui` 的表现混在了一起。

先做什么：
分别试这两个入口：

```bash
hermes
```

```bash
hermes --tui
```

然后只回答一个问题：
- 两个都怪
- 还是只有其中一个怪

这一步的意义：
- 两个都怪 → 更像终端环境问题
- 只有一个怪 → 更像特定入口体验或交互差异

什么时候该跳转：
- 两个入口都异常，而且基础聊天也跑不顺：交叉回看 [03-模型 / Provider / 自定义 endpoint 问题](<./03-%E6%A8%A1%E5%9E%8B%20Provider%20%E4%B8%8E%E8%87%AA%E5%AE%9A%E4%B9%89%20endpoint%20%E9%97%AE%E9%A2%98.md>)
- classic CLI 正常、只有 TUI 体验怪：继续留在本页

---

<a id="faq-tui-vs-cli"></a>

### 02.5｜TUI 和 classic CLI 表现不一样，怎么判断是 bug 还是正常差异

先说结论：TUI 是 Hermes 推荐的交互式运行方式（`hermes --tui`），它在 classic CLI 基础上增加了 richer display 和额外的 slash commands。两者有些表现差异是正常的。

正常差异包括：
- TUI 有更丰富的状态行（显示工作目录、git branch、运行时间）
- TUI 支持 LaTeX 数学公式渲染为 Unicode
- TUI 有可折叠启动 Banner
- TUI 支持 `/mouse`、`/indicator` 等独有命令
- TUI 支持 Ctrl+X 快速切换会话

什么时候该怀疑是 bug：
- TUI 完全无法启动，而 classic CLI 正常
- TUI 里输入后一直没反应，而 classic CLI 同样输入正常
- TUI 里输出乱码，而 classic CLI 同样输入正常

如果 TUI 有问题，可以先回退到 classic CLI：
```bash
hermes --cli
```

---

<a id="faq-slash-not-showing"></a>

### 03｜为什么输入 `/` 没看到命令或补全

先说结论：最常见不是 slash commands 消失了，而是你根本不在交互式会话里，或者把 shell 命令和 Hermes 内部斜杠命令混在一起了。

先做什么：
先确认你是在这里：

```bash
hermes
```

而不是类似这种单次命令：

```bash
hermes chat -q "..."
```

因为单次命令本来就不是给你弹 slash 补全用的。

然后在交互界面里直接输入：
```text
/
```

什么时候该跳转：
- 你发现自己一直在非交互命令里测试：先修使用方式，不用跳页
- 进入交互后依旧完全没有 slash 行为：继续留在本页排交互问题

---

<a id="faq-ctrlc-exit"></a>

### 04｜为什么 Ctrl+C、清屏、退出这些动作和我想的不一样

先说结论：很多人把“退出当前交互”“结束当前进程”“清掉终端显示”“下次继续会话”当成同一件事，但它们根本不是一个动作。

先做什么：
先把这 3 件事强行分开：
1. 我现在是想退出交互
2. 我现在只是想清屏
3. 我下次还想继续回来

你只要不把这 3 件事拆开，就很容易把正常行为误判成“会话没了”。

什么时候该跳转：
- 你的困惑核心是“退出后怎么继续回来”：直接看下一组会话问题
- CLI 根本没进来：回 [02-安装 / 更新 / 环境问题](./02-安装更新与环境问题.md)

---

<a id="faq-session-feels-lost"></a>

### 05｜为什么退出以后感觉前文丢了

先说结论：最常见不是历史真的消失了，而是你没有用正确方式继续原会话，而是重新开了一个新会话。

先做什么：
如果你只是想继续最近一次会话：
```bash
hermes --continue
```

如果你要恢复指定会话：
```bash
hermes --resume 会话ID
```

不要把下面这个动作默认理解成“恢复旧会话”：
```bash
hermes
```

因为它更像重新进入交互入口，不自动等于恢复你脑中那一段历史。

什么时候该跳转：
- 你真正的问题是“恢复哪个会话”：继续看下一题
- 你发现自己从没用过 `--continue` / `--resume`：先不用跳别页

---

<a id="faq-continue-resume"></a>

### 06｜为什么 `--continue` / `--resume` 恢复出来的不是我想要的会话

先说结论：最常见不是 Hermes 乱恢复，而是你对“最近一次”“指定 ID”“按名字续接”的差别没有分清。

先做什么：
先记住这 3 种语义不一样：
- `--continue`：继续最近一次会话
- `--resume <id>`：恢复指定会话
- `-c "名字"`：按名字续接该 lineage 的最近会话

排查原则：
- 不确定会话目标时，不要想当然
- 先看清自己是想“最近一次”，还是“某个指定历史”
- 不要把“我以为它应该恢复 A”当成命令已经明确指定 A

什么时候该跳转：
- 只是命令语义没分清：继续留在本页
- 会话历史本身异常、像没写进去：后续再考虑配置 / profiles 层

---

<a id="faq-context-not-remembered"></a>

### 07｜为什么它看起来“不记得前文”，但又不是完全新会话

先说结论：很多时候不是“会话彻底丢了”，而是你对“当前上下文”“会话继续”“长期记忆”这几个概念的预期混了。

先做什么：
先问自己：
- 我是不是回到了正确会话
- 我期待的是“恢复最近对话”，还是“拥有长期记忆”
- 我的问题究竟是会话继续，还是 profile / memory 没生效

要点：
- 会话继续 ≠ 永远完整带着所有前文
- 当前会话上下文 ≠ memory / skills / profile

什么时候该跳转：
- 你怀疑是 profile、memory、config 层：后续更该去 [07-配置 / Profiles / 环境隔离问题](<./07-%E9%85%8D%E7%BD%AE%20Profiles%20%E4%B8%8E%E7%8E%AF%E5%A2%83%E9%9A%94%E7%A6%BB%E9%97%AE%E9%A2%98.md>)
- 只是会话恢复预期不对：继续留在本页

---

<a id="faq-stuck"></a>

### 08｜为什么界面像卡住了，输入后很久没反应

先说结论：很多“假死”不是 CLI 真挂了，而是模型响应慢、provider 在超时边缘、工具调用正在执行，或者终端没有把状态变化显示得很明显。

先做什么：
先判断是哪一种：
- 完全不能输入
- 还能输入，但迟迟不出结果
- 所有请求都慢
- 只有某一类请求慢

常见原因：
- 当前模型本来就慢
- provider / endpoint 高延迟
- 工具调用在执行
- 终端显示让你误以为没反馈

什么时候该跳转：
- 所有请求都慢，更像模型 / provider 问题：回 [03-模型 / Provider / 自定义 endpoint 问题](<./03-%E6%A8%A1%E5%9E%8B%20Provider%20%E4%B8%8E%E8%87%AA%E5%AE%9A%E4%B9%89%20endpoint%20%E9%97%AE%E9%A2%98.md>)
- 只是 Gateway 消息链路慢：回 [05-Gateway / Messaging / 推送问题](<./05-Gateway%20Messaging%20%E4%B8%8E%E6%8E%A8%E9%80%81%E9%97%AE%E9%A2%98.md>)

---

<a id="faq-cli-vs-provider"></a>

### 09｜什么时候该把问题当成 CLI / TUI，而什么时候其实是模型 / Provider 在拖慢

先说结论：如果问题主要体现在“看起来慢、像没反应、结果很久才出来”，很多时候更该先怀疑 provider / model，而不是 CLI 外壳本身。

先做什么：
先把这 3 个问题答清楚：
1. 我的问题是交互方式怪，还是结果链路慢
2. 我的问题发生在“输入前”，还是“发送后”
3. 我卡在界面，还是卡在模型响应

快速分界：
- 显示怪、补全不出、快捷键不顺、恢复方式混乱 → 更像 CLI / TUI / 会话层
- 能正常发请求，但结果慢、报鉴权、报 endpoint、报模型 → 更像 provider / model 层

什么时候该跳转：
- 是 provider / model / endpoint 层：回 [03-模型 / Provider / 自定义 endpoint 问题](<./03-%E6%A8%A1%E5%9E%8B%20Provider%20%E4%B8%8E%E8%87%AA%E5%AE%9A%E4%B9%89%20endpoint%20%E9%97%AE%E9%A2%98.md>)
- 已确认只是 CLI / TUI / 会话层：继续留在本页

---

<a id="faq-cron-not-firing"></a>

### 10｜Hermes 的 cron 定时任务不触发 / cron 跑了但 profile 不对，怎么办？

**速答**：这是 v0.13 之前的已知 bug（issue #25310）：CLI 交互式配置 cron 时写入的 profile 路径，和 gateway 后台读取 cron 时使用的 profile 路径不一致，导致 cron 要么完全不触发，要么触发后用了默认 profile 而不是你想要的那一个。v0.13.0 已修复（PR #12304，5/14 合并）。如果你还在 v0.12 或更早，先升级。

**先做这 3 步**：

1. **确认版本**：
```bash
hermes version
# 如果版本号 < 0.13.0，先升级
hermes update
```

2. **确认 cron profile 路径是否生效**：
```bash
hermes cron list
# 看每条 cron 项的 profile 字段，是否指向你期望的 profile 名
```

3. **如果版本已 ≥ 0.13 但仍不触发，按下面分类排查**：

| 症状 | 真因 | 处理 |
|------|------|------|
| `hermes cron list` 是空的 | 你只在交互式会话里说过\"每天 9 点跑\"，但没真正落到 cron 表 | `hermes cron create` 显式建 |
| cron 项有，但触发时间不对 | 时区没对齐：cron 引擎读的是系统时区，不是 Hermes 内部时区 | 检查 `timedatectl status`，必要时 `sudo timedatectl set-timezone Asia/Shanghai` |
| cron 项触发，但跑出来结果像用了默认 profile | 你触到了 issue #25310 的旧 bug | 升级到 ≥ 0.13.0 后重建该 cron 项 |
| cron 项触发，但 gateway 没收到 | systemd linger 没开，用户级服务在退出会话后被回收 | `sudo loginctl enable-linger $USER`，参考 [06-VPS 自托管 Hermes](../01-从这开始/05-实战应用/06-VPS%20自托管%20Hermes.md) |

**容易踩的误判**：
- 把 cron 不触发当成 \"模型没响应\" → 错，cron 是 Hermes 内部调度层，根本没走到模型层
- 把 cron profile 错位当成 \"SOUL.md 没加载\" → 错，这是 cron 项自己的 profile 字段问题，跳 [07-配置 / Profiles](./07-配置%20Profiles%20与环境隔离问题.md)

**cron 和 `/goal` 持久循环的区别**：
- `hermes cron` = 时间触发（每天 9 点 / 每 30 分钟）
- `/goal` = 长任务持续运行（v0.13 引入），不依赖时间，而是依赖一个目标是否达成

🚦 什么时候该跳转：

- 你的问题是 systemd / linger / VPS 守护：跳 [08-Docker / Nix / SSH 与远程后端问题](./08-Docker%20Nix%20SSH%20与远程后端问题.md)
- 你想了解 `/goal` 持久循环（v0.13 新增）：先升级到 v0.13+，再用 `/goal` 命令
- 你想在 CLI 命令参考里看 cron 全部子命令：跳 [02-CLI 命令参考](../06-reference/02-CLI%20命令参考.md)

来源：[GitHub Issue #25310](https://github.com/NousResearch/hermes-agent/issues/25310)；[修复 PR #12304](https://github.com/NousResearch/hermes-agent/pull/12304)；[更新与卸载文档](https://hermes-agent.nousresearch.com/docs/getting-started/updating)。

---

## 🔹 官方依据

- [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
- [CLI Commands Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)
- [FAQ & Troubleshooting](https://hermes-agent.nousresearch.com/docs/reference/faq)
- [02-认识 Hermes 的基本使用方式](<../01-%E4%BB%8E%E8%BF%99%E5%BC%80%E5%A7%8B/02-%E5%BC%80%E5%A7%8B%E4%B8%8A%E6%89%8B/02-%E8%AE%A4%E8%AF%86%20Hermes%20%E7%9A%84%E5%9F%BA%E6%9C%AC%E4%BD%BF%E7%94%A8%E6%96%B9%E5%BC%8F.md>)
- [03-常用斜杠命令与会话管理](../01-从这开始/02-开始上手/03-常用斜杠命令与会话管理.md)

## ✅ 看完这页，你应该立刻能判断

- 我的问题是显示 / 交互 / 会话恢复，还是其实是模型响应慢
- 我有没有把 classic CLI、TUI、单次命令和交互式会话混在一起
- 我现在该继续排 CLI / TUI / 会话层，还是回模型 / Provider 页
- 我现在的问题到底是外壳交互问题，还是推理链路问题

## ➡️ 下一步

完成后进入：

- [05-Gateway / Messaging / 推送问题](<./05-Gateway%20Messaging%20与推送问题.md>)

如果你想先回到上一阶段入口重新确认位置：

- [01-总览](<./01-总览.md>)

---

## 🔗 相关排查入口

- [CLI 命令参考](/docs/reference/cli-commands)
- [Slash Commands 参考](/docs/reference/slash-commands)
- [认识 Hermes 的基本使用方式](/docs/start/getting-started/basic-usage)
- [常用斜杠命令与会话管理](/docs/start/getting-started/slash-commands-and-sessions)

如果当前页没有命中症状，先回到[遇到问题总入口](/docs/issues)重新按问题类型分流。
