# 内容仓 Direct Delivery

本仓采用 Direct Delivery v3.1：普通内容修改在本地完成受影响验证和 Reviewer，
随后直接提交并推送 `main`。仓库不保留 Pull Request 门禁、GitHub Actions CI、
Required Check、Branch Protection、Ruleset 或 Auto-merge。

## 本地验证

验证依赖仍锁定在 `requirements-ci.txt`；文件名仅为历史兼容，不代表存在远端 CI。

```powershell
python -m pip install -r requirements-ci.txt
.\scripts\verify-local.ps1 -SkipInstall
```

`verify-local.ps1` 运行真实 pytest、route order、内容质量和仓库卫生检查，并确认
验证过程没有额外改写工作区。它允许工作区已有受保护修改，不要求为验证清空或
重置工作区。

## GitHub 手动工具

保留的 workflow 仅用于维护者显式手动触发：

- `link-check`：外链复核；
- `upstream-sync-check`：上游来源巡查；
- `third-party-solutions-weekly-check`：第三方来源巡查；
- `trigger-hermes-zh-content-sync`：将已在本地验证的完整内容 SHA 派发给站点仓。

这些 workflow 均无 `pull_request`、`push`、`schedule` 或 `repository_dispatch`
自动触发，不作为 commit、push、内容同步或生产部署的前置条件。

## 内容交付

```text
修改内容 → 本地受影响验证 → Reviewer → commit / push main
→ 显式选择完整内容 SHA → 站点仓本地同步 lock 与 generated
```

内容仓不直接构建 Next.js、不部署 Vercel、不推送 GHCR、不连接腾讯云。
生产部署、DNS、Secrets、权限和搜索平台真实提交仍需用户明确授权。
