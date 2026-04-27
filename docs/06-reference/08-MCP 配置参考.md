# 🔌 08-MCP 配置参考

> 这页查的是 `mcp_servers` 配置结构、server 字段、工具过滤规则和 resources / prompts 开关。 如果你要排查的是“为什么 MCP server 连不上”，请看 [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/06-Tools%20Skills%20MCP%20%E9%97%AE%E9%A2%98.md>)。

## 1. 页面用途

这一页只负责帮你查 MCP 配置结构。

它适合用来查：

- `mcp_servers` 根结构怎么写
- stdio server 和 HTTP server 的字段区别
- `enabled`、`timeout`、`connect_timeout` 是什么意思
- `tools.include` / `tools.exclude` 怎么生效
- `resources` / `prompts` 这些 utility tools 怎么开关
- 什么时候会因为过滤规则导致一个 server 最终根本不注册工具

这页不负责：

- MCP server 连不上排障
- OAuth 流程排障
- 某个外部 MCP server 功能本身的使用教程

## 2. 官方来源

- 官方页面：<https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference>
- 官方页面标题：MCP Config Reference
- 官方页面定位：MCP 配置的紧凑参考页

中文站这一页保留官方字段名，但把“字段含义、优先级、常见误区”按查表方式整理好。

## 3. 什么时候查这页

你在下面这些场景里，应该先查这页：

- 你已经决定要接一个 MCP server
- 你想知道 stdio 和 HTTP 两种写法的配置差异
- 你想限制某个 MCP server 只暴露一小部分工具
- 你想关闭 resources / prompts 这种 utility tools
- 你想确认某个 server 为什么最终没有任何 tool 注册出来

## 4. 核心概念中文解释

### 4.1 MCP 配置的根入口叫 `mcp_servers`

官方的根结构就是：

```yaml
mcp_servers:
  <server_name>:
    ...
```

也就是说：

- 你可以配置多个 MCP server
- 每个 server 都有自己的名字
- 这个名字也会影响工具命名和识别

### 4.2 stdio server 和 HTTP server 是两种不同接法

官方把 MCP server 分成两类接法：

#### stdio server

用：

- `command`
- `args`
- `env`

#### HTTP server

用：

- `url`
- `headers`
- `auth`

所以你不要把两套字段混写成一锅。

### 4.3 `include` 是白名单，优先级高于 `exclude`

这条必须单独记：

- `include`：只允许这些工具
- `exclude`：默认都开，只排除这些
- 如果两者同时写，`include` 优先

中文最直接的记法：

`include` 是严格白名单，优先级最高。

### 4.4 `resources` 和 `prompts` 不是 server-native tools 本体

这两组更像 utility wrappers：

- resources：`list_resources` / `read_resource`
- prompts：`list_prompts` / `get_prompt`

即使你开了它们，也要 server 本身真的暴露对应 capability，Hermes 才会注册出来。

## 5. 常用项速查

### 5.1 Root config shape

官方基础结构：

```yaml
mcp_servers:
  <server_name>:
    command: "..."
    args: []
    env: {}

    # OR
    url: "..."
    headers: {}

    enabled: true
    timeout: 120
    connect_timeout: 60
    tools:
      include: []
      exclude: []
      resources: true
      prompts: true
```

### 5.2 Server keys 速查

| Key | 中文说明 | 适用 |
|---|---|---|
| `command` | 启动 stdio server 的命令 | stdio |
| `args` | 启动参数 | stdio |
| `env` | 子进程环境变量 | stdio |
| `url` | HTTP MCP endpoint | HTTP |
| `headers` | HTTP 请求头 | HTTP |
| `enabled` | 是否启用这个 server | both |
| `timeout` | 工具调用超时 | both |
| `connect_timeout` | 初始连接超时 | both |
| `tools` | 工具过滤和 utility policy | both |
| `auth` | HTTP 认证方式，如 `oauth` | HTTP |
| `sampling` | server-initiated LLM request policy | both |

### 5.3 工具过滤规则速查

| 配置项 | 你可以怎么理解 |
|---|---|
| `include` | 白名单，只注册列出的 server-native tools |
| `exclude` | 黑名单，在默认允许前提下排除某些 tools |
| 同时写 `include` 与 `exclude` | `include` 优先 |
| `resources: false` | 禁用 `list_resources` / `read_resource` |
| `prompts: false` | 禁用 `list_prompts` / `get_prompt` |

## 6. 完整参考结构

### 6.1 Root config shape 的实际理解

你可以把官方结构分成 4 块来看：

1. server 身份：`<server_name>`
2. 连接方式：stdio 或 HTTP
3. 生命周期参数：`enabled` / `timeout` / `connect_timeout`
4. 工具暴露策略：`tools.include` / `tools.exclude` / `resources` / `prompts`

### 6.2 stdio server 的写法

典型字段：

```yaml
command: "..."
args: []
env: {}
```

适合：

- 本地或命令行启动的 MCP server
- 你自己能控制启动命令的场景

### 6.3 HTTP server 的写法

典型字段：

```yaml
url: "..."
headers: {}
auth: oauth
```

适合：

- 远端 MCP endpoint
- 需要 headers 或 OAuth 的服务

### 6.4 `enabled: false` 的意义

如果你把某个 server 写成：

```yaml
enabled: false
```

那它会被完全跳过。

这意味着：

- 不连接
- 不注册工具
- 不作为活跃 server 暴露给 Hermes

### 6.5 include / exclude 语义

#### 只写 `include`

```yaml
tools:
  include: [create_issue, list_issues]
```

效果：

只有这些 server-native tools 会被注册。

#### 只写 `exclude`

```yaml
tools:
  exclude: [delete_customer]
```

效果：

除黑名单外，其他 server-native tools 都可以注册。

#### 同时写两者

```yaml
tools:
  include: [create_issue]
  exclude: [create_issue, delete_issue]
```

效果：

- `include` 优先
- 最终仍以 `include` 为准

### 6.6 resources / prompts utility tools

官方原文强调，这两组工具是 capability-aware 的。

#### Resources

```text
list_resources
read_resource
```

#### Prompts

```text
list_prompts
get_prompt
```

关闭方式：

```yaml
tools:
  resources: false
```

```yaml
tools:
  prompts: false
```

但就算你写成 `true`，如果 server 根本没暴露对应 capability，也不会凭空注册出来。

### 6.7 过滤后可能“一个工具都没有”

官方有一个很关键的行为说明：

如果过滤结果导致：

- server-native tools 全被过滤掉
- utility tools 也没有注册出来

那 Hermes 不会给这个 server 造一个空 toolset。

也就是说，最终效果可能是：

这个 server 在工具层面像“没有出现过”。

## 7. 注意事项

### 7.1 不要把 stdio 和 HTTP 字段混用成教程拼盘

查表时最容易犯的错是：

- 同时写 `command` 和 `url`
- 把 `headers` 当 stdio 字段看
- 把 `env` 当 HTTP auth 方案看

### 7.2 `include` 比 `exclude` 更强

只要你写了 `include`，就要把它当成“主规则”。

### 7.3 开了 `resources` / `prompts` 也不保证一定出现

前提是 server 自己真的支持这些 capability。

### 7.4 这页是“查配置结构”，不是“教你所有 MCP server 怎么接”

如果你要查具体某个 server 的安装、授权、服务端实现，请回该 server 自己的文档。

## 8. 出问题了去哪

| 你现在卡在哪 | 先去哪里 |
|---|---|
| MCP server 连不上 / 调不通 | [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/06-Tools%20Skills%20MCP%20%E9%97%AE%E9%A2%98.md>) |
| 工具不出现 / 过滤后结果异常 | [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/06-Tools%20Skills%20MCP%20%E9%97%AE%E9%A2%98.md>) |
| gateway / 平台里行为不一致 | [05-遇到问题 / 05-Gateway Messaging 与推送问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/05-Gateway%20Messaging%20%E4%B8%8E%E6%8E%A8%E9%80%81%E9%97%AE%E9%A2%98.md>) |
| 配置改了像没生效 | [05-遇到问题 / 07-配置 Profiles 与环境隔离问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/07-%E9%85%8D%E7%BD%AE%20Profiles%20%E4%B8%8E%E7%8E%AF%E5%A2%83%E9%9A%94%E7%A6%BB%E9%97%AE%E9%A2%98.md>) |
| 不确定问题在哪 | [05-遇到问题 / 01-总览](../05-遇到问题/01-总览.md) |

## 9. 官方原文链接

- 官方 MCP Config Reference：<https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference>

## 10. 相关中文站页面

- [01-总览｜Reference 参考手册](./01-总览.md)
- [06-Built-in Tools 参考](<./06-Built-in%20Tools%20%E5%8F%82%E8%80%83.md>)
- [07-Toolsets 参考](<./07-Toolsets%20%E5%8F%82%E8%80%83.md>)
- [09-内置 Skills 目录](<./09-%E5%86%85%E7%BD%AE%20Skills%20%E7%9B%AE%E5%BD%95.md>)
- [05-遇到问题 / 06-Tools Skills MCP 问题](<../05-%E9%81%87%E5%88%B0%E9%97%AE%E9%A2%98/06-Tools%20Skills%20MCP%20%E9%97%AE%E9%A2%98.md>)

## ➡️ 下一步

完成后进入：

- [09-内置 Skills 目录](<./09-%E5%86%85%E7%BD%AE%20Skills%20%E7%9B%AE%E5%BD%95.md>)

如果你想先回到上一阶段入口重新确认位置：

- [01-总览｜Reference 参考手册](./01-总览.md)
