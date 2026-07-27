# 内容资产与仓库体积策略

- 正式文档引用的图片、Pack 下载物、route map 和当前治理证据允许入仓。
- 临时候选图、原始生成任务、重复导出、日志和一次性 QA 报告不得入仓。
- 新增 tracked 单文件上限为 5 MiB，由 `python scripts/check_repository_hygiene.py` 强制。
- 超过上限的正式资产必须先压缩；仍需保留时再评估 Release/Object Storage 或 Git LFS。
- 不在本任务删除历史文件或重写 Git 历史；任何历史清理都需独立授权和可恢复清单。
