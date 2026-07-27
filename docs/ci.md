# 内容仓 CI 与 Actions 预算

> CI 状态：`降级（Actions 月度额度耗尽时可本地验证）`
>
> 合并治理：`platform-enforced`
>
> 唯一自动检查：`CI Gate`

## 1. Actions 月度预算

- 仅 `.github/workflows/content-check.yml` 在非 Draft PR 指向 `main` 时自动运行；
- 仅 `CI Gate` 自动运行，`push main` 没有独立触发器；向已开启 PR 的分支推送只刷新这一条 Gate；
- link-check、上游巡查、第三方巡查和站点同步派发全部仅手动运行；
- 仓库内零 schedule，`schedule` 数量为 0；
- 内容仓不直接构建 Next.js、不部署 Vercel、不推送 GHCR、不连接腾讯云。

这保证普通 commit 和 push 不会产生部署；已开启 PR 时，分支 push 最多只刷新一条 `CI Gate`，不会产生重复校验任务。

## 2. CI Gate

运行时为 Python 3.12，依赖锁定在 `requirements-ci.txt`。真实命令为：

```powershell
python -m pip install -r requirements-ci.txt
python -m pytest -q
python scripts/normalize_route_order.py
python scripts/content_quality_check.py
```

无数据库、浏览器和生产 Secret。检查失败不会被 `continue-on-error` 或空命令掩盖。

## 3. Actions 额度耗尽

Git commit 和 push 不依赖 Actions。额度耗尽时先在待提交版本运行：

```powershell
.\scripts\verify-local.ps1
git push -u origin HEAD
```

内容仓 `main` 有平台分支保护；若 GitHub 因额度不创建 Required `CI Gate`，平台会阻止合并。这时保持 PR open，或由仓库管理员在确认本地完整验证证据和风险后决定是否临时调整规则；不得把本地结果伪装成远端 Required Check。

站点部署不依赖本内容仓 Actions。合并或选定内容提交后，在站点仓手动运行 `content-auto-sync`，输入内容仓完整 40 位 SHA；额度仍为 0 时，由站点仓的本地发布脚本完成 Vercel、GHCR 和腾讯云发布。

## 4. 手动维护

- `link-check`：需要复核外链时手动运行；
- `upstream-sync-check`：准备上游同步时手动运行；
- `third-party-solutions-weekly-check`：名称为历史兼容，实际只手动运行；
- `trigger-hermes-zh-content-sync`：仅为有 Actions 额度时的手动 dispatch 入口，不再随 `main` 自动触发。

所有巡查默认只读。第三方或上游变化不得自动改写公开文档。
