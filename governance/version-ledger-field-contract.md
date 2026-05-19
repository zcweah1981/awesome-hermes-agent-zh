# 版本台账字段契约 (Version Ledger Field Contract)

更新时间：2026-05-19
Owner: Content (Ikki) → Coder (Long) 消费契约

## 目标

这份契约定义 `governance/version-ledger.yaml` 的完整字段结构，供 Long 扩展 `scripts/upstream_sync.py` 和 `.github/workflows/upstream-sync-check.yml` 时消费。Long 按 JSON Schema 级别的契约编码，不需要猜测字段含义。

## 台账文件路径

```
governance/version-ledger.yaml
```

## 顶级字段

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `ledger_meta` | object | ✅ | 台账元数据 |
| `current_content_baseline` | string | ✅ | 当前内容仓已同步的官方版本号（兼容旧 `hermes_upstream_baseline_version`） |
| `latest_seen` | string | ✅ | 上游已发布的最新版本号 |
| `last_checked_at` | string (YYYY-MM-DD) | ✅ | 最近一次检查上游的时间 |
| `source` | object | ✅ | 版本来源信息 |
| `status` | enum string | ✅ | 台账当前状态 |
| `sync_priority_tiers` | object | ✅ | P0/P1/P2 同步分级定义 |
| `versions` | array | ✅ | 版本历史记录 |
| `sync_decision_types` | array | ✅ | 同步决策类型枚举 |
| `change_categories_enum` | array of string | ✅ | 变更分类枚举 |

## 字段详细结构

### ledger_meta

```json
{
  "created_at": "YYYY-MM-DD",
  "updated_at": "YYYY-MM-DD",
  "owner": "content-maintainers",
  "project_id": "hermes-zh",
  "backward_compat_baseline_field": "hermes_upstream_baseline_version",
  "backward_compat_baseline_value": "v2026.4.30"
}
```

### source

```json
{
  "id": "hermes-official-github",
  "url": "https://github.com/NousResearch/hermes-agent",
  "check_method": "github_api_latest_release",
  "docs_url": "https://hermes-agent.nousresearch.com/docs"
}
```

### status 枚举值

| 值 | 含义 |
|---|---|
| `current` | 内容仓与上游一致 |
| `behind` | 上游有更新，需要评估同步 |
| `syncing` | 同步进行中 |
| `review_blocked` | 同步被阻塞，需要人工审核 |

### versions 数组元素

```json
{
  "version": "v2026.4.30",
  "source": "hermes-official-github",
  "checked_at": "2026-05-02",
  "status": "current_baseline",
  "change_categories": ["install", "cli"],
  "affected_docs": [
    "docs/01-从这开始/01-先跑起来/04-把 Hermes 装上去.md"
  ],
  "sync_decision": "baseline_established",
  "task_group": "hermes-zh:UPSTREAM-VERSION-LEDGER-SYNC-20260519",
  "notes": "R3 baseline"
}
```

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `version` | string | ✅ | 上游版本号 |
| `source` | string | ✅ | 来源 ID，对应 sources 中的 id |
| `checked_at` | string (YYYY-MM-DD) | ✅ | 本次检查日期 |
| `status` | enum string | ✅ | 见下表 |
| `change_categories` | array of string | ✅ | 涉及的功能域，值来自 `change_categories_enum` |
| `affected_docs` | array of string | ✅ | 受影响的中文文档路径（相对仓库根目录） |
| `sync_decision` | enum string | ✅ | 同步决策，值来自 `sync_decision_types[].id` |
| `task_group` | string \| null | ✅ | 关联的 dispatch task_group ID |
| `notes` | string | ❌ | 人工备注 |

### versions[].status 枚举值

| 值 | 含义 |
|---|---|
| `current_baseline` | 当前内容仓基线 |
| `new_detected` | 新版本已检测到 |
| `syncing` | 正在同步 |
| `synced` | 已完成同步 |
| `skipped` | 跳过（无影响） |
| `blocked` | 阻塞中 |

### sync_priority_tiers 结构

```json
{
  "P0": {
    "description": "直接阻塞安装或运行——用户跑不通",
    "categories": ["install", "cli", "configuration"],
    "affected_docs": ["docs/..."],
    "sync_sla": "48h"
  },
  "P1": {
    "description": "影响核心功能体验——用户能跑但体验受损",
    "categories": ["provider", "gateway", "tools", "skills", "mcp"],
    "affected_docs": ["docs/..."],
    "sync_sla": "1 week"
  },
  "P2": {
    "description": "周边体验与参考——不影响核心使用",
    "categories": ["memory", "troubleshooting", "profiles", "automation", "api_server"],
    "affected_docs": ["docs/..."],
    "sync_sla": "2 weeks"
  }
}
```

## 脚本消费契约

### upstream_sync.py 需要消费的字段

1. **读取** `current_content_baseline` 替代旧的 `hermes_upstream_baseline_version`
2. **写入** `latest_seen` 当检测到新版本时
3. **写入** `last_checked_at` 为当前日期
4. **写入** `status` 根据 `latest_seen` vs `current_content_baseline` 比较结果
5. **追加** `versions[]` 条目 当检测到新版本时
6. **读取** `sync_priority_tiers` 用于生成受影响文档清单

### 脚本必须保持的兼容性

- `upstream-source-registry.yaml` 的 `hermes_upstream_baseline_version` 仍然有效
- 如果 `version-ledger.yaml` 不存在，脚本仍按旧逻辑运行
- 脚本的 `check` 子命令新增 `--ledger` 参数指向 version-ledger.yaml

### CI 工作流消费契约

1. 检查 `status` 字段：如果 `behind`，触发预警 issue
2. issue 标题应包含优先级：`[P0]` / `[P1]` / `[P2]`
3. issue body 应包含 `affected_docs` 清单
4. issue 应引用 `versions[]` 中最新条目的 `version` 和 `change_categories`

## 完整示例 JSON（供 Long 直接解析）

```json
{
  "ledger_meta": {
    "created_at": "2026-05-19",
    "updated_at": "2026-05-19",
    "owner": "content-maintainers",
    "project_id": "hermes-zh",
    "backward_compat_baseline_field": "hermes_upstream_baseline_version",
    "backward_compat_baseline_value": "v2026.4.30"
  },
  "current_content_baseline": "v2026.4.30",
  "latest_seen": "v2026.5.15",
  "last_checked_at": "2026-05-19",
  "source": {
    "id": "hermes-official-github",
    "url": "https://github.com/NousResearch/hermes-agent",
    "check_method": "github_api_latest_release",
    "docs_url": "https://hermes-agent.nousresearch.com/docs"
  },
  "status": "behind",
  "sync_priority_tiers": {
    "P0": {
      "description": "直接阻塞安装或运行——用户跑不通，必须立即同步",
      "categories": ["install", "cli", "configuration"],
      "affected_docs": [
        "docs/01-从这开始/01-先跑起来/04-把 Hermes 装上去.md",
        "docs/06-reference/02-CLI 命令参考.md"
      ],
      "sync_sla": "48h"
    },
    "P1": {
      "description": "影响核心功能体验——用户能跑但体验受损",
      "categories": ["provider", "gateway", "tools", "skills", "mcp"],
      "affected_docs": [
        "docs/06-reference/08-MCP 配置参考.md"
      ],
      "sync_sla": "1 week"
    },
    "P2": {
      "description": "周边体验与参考——不影响核心使用",
      "categories": ["memory", "troubleshooting", "profiles"],
      "affected_docs": [],
      "sync_sla": "2 weeks"
    }
  },
  "versions": [
    {
      "version": "v2026.4.30",
      "source": "hermes-official-github",
      "checked_at": "2026-05-02",
      "status": "current_baseline",
      "change_categories": [],
      "affected_docs": [],
      "sync_decision": "baseline_established",
      "task_group": null,
      "notes": "R3 baseline"
    },
    {
      "version": "v2026.5.15",
      "source": "hermes-official-github",
      "checked_at": "2026-05-19",
      "status": "new_detected",
      "change_categories": ["cli", "mcp", "breaking_change"],
      "affected_docs": [
        "docs/06-reference/02-CLI 命令参考.md",
        "docs/06-reference/08-MCP 配置参考.md"
      ],
      "sync_decision": "sync_required",
      "task_group": "hermes-zh:UPSTREAM-VERSION-LEDGER-SYNC-20260519",
      "notes": "CLI 子命令重构 + MCP 配置格式变更"
    }
  ]
}
```

## 不做的事

- 不直接修改公开 docs 正文
- 不泄露 API token / secret
- 不把 dispatch proof 写入 version-ledger.yaml
- 不自动提交同步决策——需 PM/Content 确认后才更新 `sync_decision`
