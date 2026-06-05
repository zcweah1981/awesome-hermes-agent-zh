# 内容仓 Link-Check 失败审计与替换/忽略映射

- **审计时间**：2026-06-06 00:30 CST
- **审计人**：ikki-content-1（Content Agent）
- **基线 commit**：`b96ce30`（main，对应 CI run #73）
- **本地工具**：Lychee 0.24.2（与 GitHub Actions `lycheeverse/lychee-action@v2` 当前默认对齐）
- **本地复跑命令**（与 CI 等价）：
  ```bash
  lychee --verbose --no-progress \
    --exclude-file .lycheeignore \
    --max-concurrency 6 --retry-wait-time 2 --timeout 20 \
    --root-dir /opt/projects/awesome-hermes-agent-zh \
    --skip-missing --exclude-path 'docs/assets/render-.*\.html' \
    './README.md' './docs/**/*.md' './governance/**/*.md' \
    './governance/**/*.yml' './governance/**/*.yaml' \
    './.github/**/*.yml' './.github/**/*.yaml' \
    './**/*.html' './packs/**/*.md' './packs/**/*.yml' './packs/**/*.yaml'
  ```
- **基线结果**：Total 2352 / Unique 644 / Errors **10** / Redirects 17 / Excluded 514

---

## 1. 失败清单与处置映射（10 条）

> 处置分类：`replace`（真实 404，换成验证可访问的官方/上级稳定页）/ `fix-relative`（仓库内相对路径错误，就地修）/ `precise-ignore`（站点对 GitHub runner 反爬返回 403/429，且无稳定镜像可换，精确写入 `.lycheeignore` 并保留来源说明）

| # | 失败 URL | 源位置（行） | 类型 | 处置 | 替换 / 处理目标 | 验证结果 |
|---|---------|-------------|------|------|----------------|---------|
| 1 | `https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-access-tokens` | `docs/01-从这开始/05-实战应用/16-安全加固.md:417` | 404 | **replace** | `https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens` | HEAD 200，redirect 到本页 |
| 2 | `https://hermes-agent.nousresearch.com/docs/user-guide/integrations/mcp` | `docs/01-从这开始/05-实战应用/18-Hermes Agent 进阶实战.md:305` | 404 | **replace** | `https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp` | HEAD 200 |
| 3 | `https://medium.com/@roanmonteiro/hermes-agent-advanced-self-evolving-skills-mcp-subagents-and-production-8c827c79ce7e` | `docs/01-从这开始/05-实战应用/18-Hermes Agent 进阶实战.md:303` | 403 | **precise-ignore** | 写入 `.lycheeignore`；正文保留链接并加访问说明 | 本地 GET 200 / GitHub runner HEAD 403（Medium 反爬） |
| 4 | `https://hermes-agent.nousresearch.com/docs/user-guide/configuration/profiles` | `docs/01-从这开始/05-实战应用/19-Hermes Agent 控制室.md:336` | 404 | **replace** | `https://hermes-agent.nousresearch.com/docs/user-guide/profiles` | HEAD 200 |
| 5 | `https://ollama.com/library/gpt-os` | `docs/01-从这开始/05-实战应用/21-Hermes Agent 与 Ollama 最快路径.md:337` | 404 | **replace** | `https://ollama.com/library/gpt-oss` | GET 200（HEAD 该站点返回 405，符合 Ollama 行为） |
| 6 | `file:///.../docs/01-从这开始/06-reference/01-总览.md` | `docs/01-从这开始/05-实战应用/22-Hermes Agent 深度拆解与自建指南.md:329` | 本地路径错误 | **fix-relative** | `../06-reference/01-总览.md` → `../../06-reference/01-总览.md`（多一层） | 仓库内 `docs/06-reference/01-总览.md` 存在 |
| 7 | `https://hermes-agent.nousresearch.com/docs/contributing/architecture` | `docs/01-从这开始/05-实战应用/22-Hermes Agent 深度拆解与自建指南.md:343` | 404 | **replace** | `https://hermes-agent.nousresearch.com/docs/developer-guide/architecture` | HEAD 200 |
| 8 | `https://hermes-agent.nousresearch.com/docs/contributing/prompt-architecture` | `docs/01-从这开始/05-实战应用/22-Hermes Agent 深度拆解与自建指南.md:344` | 404 | **replace** | `https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly` | HEAD 200 |
| 9 | `https://platform.kimi.ai/docs/guide/kimi-k2-quickstart` | `docs/03-国内落地/02-国内模型/06-Kimi登月计划.md:300` | 404 | **replace** | `https://platform.kimi.ai/docs/guide/kimi-k2-6-quickstart` | HEAD 200（页面随 K2.6 发布重命名） |
| 10 | `https://platform.kimi.ai/docs/guide/kimi-k2-quickstart` | `governance/upstream-source-registry.yaml:143` | 404 | **replace** | `https://platform.kimi.ai/docs/guide/kimi-k2-6-quickstart` | HEAD 200（同 #9，治理文件同步） |

### 处置分布
- `replace`：8 条（5 条 Hermes 官方文档路径迁移、1 条 GitHub PAT 文档重命名、1 条 Ollama 模型卡拼写、1 条 Kimi 文档随版本重命名，治理文件镜像 1 条）
- `fix-relative`：1 条（相对路径多/少一层）
- `precise-ignore`：1 条（Medium 反爬）

---

## 2. 替换目标核验

所有 `replace` 目标均在本次任务执行期间通过本地 HTTP HEAD/GET 验证为 200，且语义上对齐原引用：

| 替换 | 原引用上下文 | 语义对齐 |
|------|------------|---------|
| `managing-your-personal-access-tokens` | 「Fine-grained PAT」（GitHub Developer 文档） | ✅ 同一 docs 节点，PAT 总入口 |
| `/docs/user-guide/features/mcp` | 「Native MCP Client」 | ✅ 同主题（路径从 `integrations/` 迁到 `features/`） |
| `/docs/user-guide/profiles` | 「Profiles」（Hermes 官方） | ✅ 同主题（`configuration/profiles` 简化为 `profiles`） |
| `/library/gpt-oss` | 「gpt-oss-20b 模型卡」 | ✅ 即原意图模型（gpt-os 系拼写错误，正确名为 gpt-oss） |
| `/docs/developer-guide/architecture` | 「Architecture Overview」 | ✅ 同主题（`contributing/` 迁到 `developer-guide/`） |
| `/docs/developer-guide/prompt-assembly` | 「System Prompt Assembly」 | ✅ 页面重命名：`prompt-architecture` → `prompt-assembly` |
| `/docs/guide/kimi-k2-6-quickstart` | Kimi K2 Quickstart | ✅ 随 K2.6 发布，原 `kimi-k2-quickstart` 重命名为 `kimi-k2-6-quickstart` |

---

## 3. .lycheeignore 增量（仅 1 条精确忽略）

```diff
+# Medium 对 GitHub Actions runner IP 返回 403（反爬），文章对普通浏览器可正常访问。
+# 此处仅忽略具体文章 URL，不放宽到整个 medium.com。
+^https?://medium\.com/@roanmonteiro/hermes-agent-advanced-self-evolving-skills-mcp-subagents-and-production-8c827c79ce7e$
```

不放宽到 `^https?://(www\.)?medium\.com/.*` 的理由：
- 任务验收明确要求「禁止粗暴忽略所有外链」。
- 当前内容仓只引这一篇 Medium 文章，整域放宽无收益且降低审计粒度。

---

## 4. 不属于本任务的 17 条 Redirect

Lychee 还报告了 17 条 301/308 重定向（如 Anthropic Prompt Caching、Aliyun、MiniMax、DingTalk 等官方域名跳转）。这些 URL 当前仍是 200 链路（重定向后可达），Lychee 不计为错误，本任务不修改正文，**仅在本审计中登记**。如后续要降低 redirect 噪音，可单独发起 follow-up 任务。

---

## 5. 给下游（PM Seiya / Coder Long / Ops Hyoga）的说明

- **PM**：本任务输出 1 个审计报告 + 5 个 markdown 文件改动 + 1 个 yaml 改动 + 1 个 `.lycheeignore` 改动，全部在内容仓 SSoT 内。
- **后续 CI 验收**：替换应用后，本地等价 Lychee 已复跑（结果见 commit body）；push 后需查询最新 GitHub Actions link-check run 状态为 `success` 才能 PM closeout。
- **不要把 Medium 这类反爬链接扩成全域 ignore；新增引用时单独审计**。
- **治理文件 `upstream-source-registry.yaml` 中 `kimi-moonshot` 条目已同步更新**，下游消费方无需再做 URL 重写。
