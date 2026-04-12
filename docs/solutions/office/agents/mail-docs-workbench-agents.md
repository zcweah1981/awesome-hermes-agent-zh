# 邮件文档工作台 agents 映射占位说明

## 作用
为 `docs/solutions/office/mail-docs-workbench.md` 提供实现层映射占位，后续在这里补充真实 agent 编排、提示词边界、输入输出契约与脚本落点。

## 页面层来源
- 页面文件：`docs/solutions/office/mail-docs-workbench.md`
- 页面角色：RM3 办公流程首个场景页

## 实现层占位
| 项目 | 当前说明 |
|---|---|
| coordinator | 接收邮件、附件与处理目标，编排最小执行单 |
| reader | 提取邮件上下文、附件重点与待确认事项 |
| drafter | 生成回复草稿、转发说明或文档整理初稿 |
| organizer | 输出待办清单、归档结构与回传说明 |
| archivist | 整理结论、版本留痕与后续跟进要点 |

## 输入契约占位
- `mail_or_docs`: 邮件正文、附件或文档链接
- `task_goal`: 处理目标
- `tone_or_format`: 回复语气或格式要求
- `deliverables`: 需要输出的结果清单

## 输出契约占位
- `summary`
- `reply_draft`
- `todo_list`
- `archive_notes`

## 当前状态
占位已建立，供 RM3 先完成实现层映射登记；后续可继续替换为真实 agents、脚本或流程文件。
