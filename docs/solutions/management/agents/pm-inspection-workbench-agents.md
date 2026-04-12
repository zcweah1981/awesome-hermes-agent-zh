# PM 巡查工作台 agents 映射占位说明

## 作用
为 `docs/solutions/management/pm-inspection-workbench.md` 提供实现层映射占位，后续在这里补充真实 agent 编排、提示词边界、输入输出契约与脚本落点。

## 页面层来源
- 页面文件：`docs/solutions/management/pm-inspection-workbench.md`
- 页面角色：RM3 项目管理首个场景页

## 实现层占位
| 项目 | 当前说明 |
|---|---|
| coordinator | 接收项目目标、当前块与约束，编排最小执行单 |
| inspector | 汇总状态、识别阻塞与风险 |
| dispatcher | 把结论压成任务拆分与责任分发 |
| reporter | 生成状态汇报与下一步摘要 |
| archivist | 整理留痕、结论与后续跟进要点 |

## 输入契约占位
- `project_goal`: 项目目标
- `current_block`: 当前执行块
- `blockers`: 已知阻塞
- `timeline`: 期望交付时间或节奏

## 输出契约占位
- `inspection_summary`
- `task_breakdown`
- `risk_list`
- `next_actions`

## 当前状态
占位已建立，供 RM3 先完成实现层映射登记；后续可继续替换为真实 agents、脚本或流程文件。
