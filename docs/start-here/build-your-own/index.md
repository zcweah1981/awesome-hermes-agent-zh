# 自己造东西

![自己造东西阶段地图：从“一个已经会用的 Hermes 助手”进入“系统能力”，开始接触 Profiles、外部记忆、上下文系统、MCP 与 Plugins、API Server、Cron 与 Automation、ACP 与 IDE](../assets/rm2-5-build-your-own-index-01-system-capability-map.png)

如果你已经不满足于“把一个助手用顺”，这一阶段只做一件事：
把你的 Hermes 使用方式，从“一个助手”推进到“开始搭一套系统”。

从这里开始，你会第一次碰到多个助手、外部记忆系统、上下文系统、MCP / Plugins、API Server、Cron / Automation、ACP / IDE。
但这一页只讲阶段路径、边界、进入条件和顺序，不抢写后面子页细节。

---

## ✅ 你现在适不适合进入这一阶段

符合下面 4 条，就可以继续：

- 你已经完成过 [玩出花样](../advanced-usage/index.md)
- 你已经知道怎么稳定使用一个 Hermes 助手
- 你已经能分清人格、记忆、工具、模型这些基础层次
- 你现在想解决的是“怎么搭能力系统”，不是“怎么把单助手再细调一点”

如果你还没到这个状态，先回到：
- [玩出花样](../advanced-usage/index.md)

---

## 🎯 这一阶段会帮你拿到什么

走完这一阶段，你会完成一个关键切换：
从“我在用一个助手”，变成“我在搭一套能长期工作的 Hermes 系统”。

你会逐步开始拿到这些能力：

1. 不同助手分不同职责，而不是所有事都塞给同一个助手  
2. 记忆开始从本地偏好，进入外部记忆系统  
3. 上下文开始有固定结构，不再每次临时拼材料  
4. Hermes 可以接进外部工具、服务和工作流  
5. Hermes 可以被当成接口、自动任务或 IDE 内能力来用  

一句话说完：
这一阶段不是“再学几个功能”，而是开始理解 Hermes 的系统化用法。

---

## 🧭 这 7 个方向就是完整路径

<table>
  <colgroup>
    <col style="width: 14%;" />
    <col style="width: 22%;" />
    <col style="width: 42%;" />
    <col style="width: 22%;" />
  </colgroup>
  <thead>
    <tr>
      <th>顺位</th>
      <th>方向</th>
      <th>这一段会解决什么</th>
      <th>当前入口写法</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>第 1 步</strong></td>
      <td><strong>Profiles</strong></td>
      <td>先把“多个助手怎么分工”这件事建立起来，完成从单助手到多助手的心智切换。</td>
      <td><code>./profiles.md</code></td>
    </tr>
    <tr>
      <td><strong>第 2 步</strong></td>
      <td><strong>Memory Providers</strong></td>
      <td>开始接触外部记忆系统，理解什么时候需要把记忆放到更正式的 provider 里。</td>
      <td><code>./memory-providers/index.md</code></td>
    </tr>
    <tr>
      <td><strong>第 3 步</strong></td>
      <td><strong>Context System</strong></td>
      <td>把长期规则、上下文文件和临时引用分层，减少“每次都重新解释背景”的成本。</td>
      <td><code>./context-system/index.md</code></td>
    </tr>
    <tr>
      <td><strong>第 4 步</strong></td>
      <td><strong>MCP / Plugins</strong></td>
      <td>让 Hermes 开始接入外部工具和系统，不只停留在聊天窗口里。</td>
      <td><code>./mcp-and-plugins.md</code></td>
    </tr>
    <tr>
      <td><strong>第 5 步</strong></td>
      <td><strong>API Server</strong></td>
      <td>把 Hermes 暴露成服务接口，开始具备被其它应用调用的能力。</td>
      <td><code>./api-server.md</code></td>
    </tr>
    <tr>
      <td><strong>第 6 步</strong></td>
      <td><strong>Cron / Automation</strong></td>
      <td>让 Hermes 能按时间和规则自动跑，进入持续执行而不是手动触发。</td>
      <td><code>./cron-and-automation.md</code></td>
    </tr>
    <tr>
      <td><strong>第 7 步</strong></td>
      <td><strong>ACP / IDE</strong></td>
      <td>把这套能力带进编辑器和开发环境，让 Hermes 更像工作台的一部分。</td>
      <td><code>./acp-ide.md</code></td>
    </tr>
  </tbody>
</table>

说明：
当前仓库里这些下游页还没有落地，所以这里先只写真实路径，不造假链接，保证当前页坏链为零。

---

## 🚦 默认顺序怎么走

默认就按下面顺序推进：

1. 先看 Profiles，先把“一个助手”拆成“多个职责”  
2. 再看外部记忆，决定系统级记忆放在哪里  
3. 再看上下文系统，整理规则、材料和引用入口  
4. 再进入 MCP / Plugins，把 Hermes 接到外部工具  
5. 再考虑 API Server，让能力对外可调用  
6. 再做 Cron / Automation，让系统自己跑起来  
7. 最后再把能力带进 ACP / IDE  

这个顺序的重点不是绝对技术依赖。
而是先把系统边界立住，再做接入、服务化和自动化。

---

## 🧩 这一阶段先不解决什么

这一阶段入口页先不展开这些深坑：

- 每一种外部记忆 provider 的安装细节
- 上下文文件和上下文引用的完整语法
- 每个 MCP Server 或 Plugin 的接法差异
- API Server 的部署架构、鉴权和生产运维
- 自动化任务的复杂编排
- IDE 集成里的编辑器细节差异

这些都放到后续子页分别讲。
这一页先只帮你把系统阶段的边界看清楚，不把路走散。

---

## 🌱 什么时候算这一阶段真的开始了

不是你看完这页就算开始。
真正开始，至少要出现下面这个变化：

- 你已经明确不再只依赖一个助手处理所有事情
- 你已经准备接受“助手分工、记忆外接、上下文分层、系统接入”这套思路
- 你已经愿意按阶段顺序搭，而不是看到哪个新功能就先跳哪个

更直白一点：
当你开始把 Hermes 当成“系统能力底座”，而不只是“一个聊天助手”，这一阶段才算真正开始。

---

## 👉 现在就开始

这一阶段的下一页路径是：
- `./profiles.md`

如果你想先回到上一阶段入口重新确认位置：
- [玩出花样](../advanced-usage/index.md)

如果你想回总入口看完整学习路线：
- [从这开始](../index.md)
