# R1 官方来源同步 QA Proof

更新时间：2026-05-02 06:12:12 UTC

## 任务

- task_id: `hermes-zh:UPSTREAM-SYNC-R1-QA`
- branch: `feature/upstream-sync-r1`
- compare URL: <https://github.com/zcweah1981/awesome-hermes-agent-zh/compare/main...feature/upstream-sync-r1?expand=1>

## 本轮交付范围

- 新增官方来源 registry：`governance/upstream-source-registry.md` / `governance/upstream-source-registry.yaml`
- 新增官方来源同步规则：`governance/upstream-sync-policy.md`
- 新增 R2 国内模型 / 部署官方同步规划：`governance/r2-china-model-deployment-plan.md`
- 扩展 `governance/site-route-map.yaml`：为安装、配置、Reference、国内模型 / 部署等用户操作相关页面增加 `source_refs` / `source_review`
- 新增 side-effect safe 脚本：`scripts/upstream_sync.py`
- 新增每周 / 手动 GitHub Actions：`.github/workflows/upstream-sync-check.yml`
- 新增测试：`tests/test_upstream_sync.py`
- 更新 governance README / content contract / publishing checklist，使官方来源同步进入公开治理入口

## 本地 QA 结果

| 检查 | 命令 | 结果 |
|---|---|---:|
| upstream sync unit tests | `python3 -m pytest tests/test_upstream_sync.py -q` | 5 passed |
| full Python tests | `python3 -m pytest -q` | 5 passed |
| registry/policy check no network | `python3 scripts/upstream_sync.py check --no-network --format json` | `status=ok` |
| registry/policy check with network | `python3 scripts/upstream_sync.py check --format json` | `status=ok` |
| digest dry-run | `python3 scripts/upstream_sync.py digest --no-network` | generated |
| issue dry-run | `python3 scripts/upstream_sync.py issue --dry-run --format json --no-network` | `dry_run=true`, `side_effect=none` |
| workflow YAML parse | Python `yaml.safe_load()` over `.github/workflows/*.yml` | passed |
| actionlint | `/tmp/actionlint-bin/actionlint .github/workflows/*.yml` | passed |
| route map source refs | one-off YAML validation against registry source IDs + R2 provider IDs | `unknown_refs=[]` |
| content consumer verify | `CONTENT_REPO_PATH=/opt/projects/awesome-hermes-agent-zh npm run verify:content` in `/opt/projects/hermes-zh` | `content manifests verified` |
| content manifest build | `CONTENT_REPO_PATH=/opt/projects/awesome-hermes-agent-zh npm run build:content` in `/opt/projects/hermes-zh` | pages=87, routes=87, packs=8, search=95 |

## Route-map source review summary

```json
{
  "routes_total": 88,
  "routes_with_source_refs": 35,
  "provider_ids_count": 9,
  "unknown_refs": [],
  "source_review_states": {
    "needs-official-check": 26,
    "needs-provider-official-confirmation": 9
  }
}
```

## Remote proof

- pushed branch: `feature/upstream-sync-r1`
- compare URL: <https://github.com/zcweah1981/awesome-hermes-agent-zh/compare/main...feature/upstream-sync-r1?expand=1>

## PR 状态

PR 创建未在本机完成，原因是当前执行环境没有 GitHub CLI，也没有可用 `GITHUB_TOKEN` / `GH_TOKEN`：

- `gh`: not installed
- `hub`: not installed
- `GITHUB_TOKEN`: absent
- unauthenticated GitHub REST `POST /pulls`: HTTP `401 Requires authentication`

因此本轮可交付到远端分支与 compare URL；正式 PR 需要维护者在 GitHub 页面打开 compare URL 创建，或在执行环境补充 GitHub token 后由 Ops 继续创建。

## 风险与边界

- R1 只建立 registry / policy / QA workflow 与 R2 规划，不批量改正文事实。
- `upstream-sync-check` workflow 的 issue 创建只会在 schedule / manual dispatch 时执行；PR 分支 push 不会自动创建 issue。
- Workflow 使用 GitHub-hosted runner 自带 `gh` CLI 与 `${{ secrets.GITHUB_TOKEN }}`；本地环境缺少 `gh` 不影响 GitHub Actions 运行，但影响本地创建 PR。
- 无 token、cookie、API Key 写入仓库。
