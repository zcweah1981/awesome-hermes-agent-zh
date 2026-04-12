# 仓库巡检工作台 agents 映射占位说明

## 作用
为 `docs/solutions/dev/repo-inspection-workbench.md` 提供实现层映射占位，后续在这里补充真实 agent 编排、提示词边界、输入输出契约与脚本落点。

## 页面层来源
- 页面文件：`docs/solutions/dev/repo-inspection-workbench.md`
- 页面角色：RM3 开发交付首个场景页

## 实现层占位
| 项目 | 当前说明 |
|---|---|
| coordinator | 接收仓库任务、文件边界与验收标准，编排最小执行单 |
| inspector | 盘点文件现状、约束与可改动面 |
| implementer | 执行最小改动并生成可回传结果 |
| verifier | 汇总 diff、stat、git status 与验收结论 |
| archivist | 整理变更记录、限制条件与后续跟进要点 |

## 输入契约占位
- `repo_context`: 仓库路径或任务上下文
- `allowed_scope`: 允许修改的文件范围
- `acceptance`: 验收标准
- `evidence_required`: 需要回传的证据清单

## 输出契约占位
- `modified_files`
- `diff_summary`
- `git_status`
- `next_actions`

## 当前状态
占位已建立，供 RM3 先完成实现层映射登记；后续可继续替换为真实 agents、脚本或流程文件。
