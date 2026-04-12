# 内容改写工作台 agents 映射占位说明

## 作用
为 `docs/solutions/content/content-repurpose-workbench.md` 提供实现层映射占位，后续在这里补充真实 agent 编排、提示词边界、输入输出契约与脚本落点。

## 页面层来源
- 页面文件：`docs/solutions/content/content-repurpose-workbench.md`
- 页面角色：RM3 内容生产首个场景页

## 实现层占位
| 项目 | 当前说明 |
|---|---|
| coordinator | 接收素材、目标渠道与输出要求，编排最小执行单 |
| writer | 生成主发布版正文 |
| editor | 压缩、改写、统一语气与结构 |
| distributor | 生成渠道适配短版与分发说明 |
| archivist | 生成摘要、标签、归档要点 |

## 输入契约占位
- `source_material`: 原始素材或链接
- `target_channel`: 目标发布渠道
- `tone`: 语气与风格要求
- `deliverables`: 需要输出的版本清单

## 输出契约占位
- `publish_version`
- `short_version`
- `summary`
- `archive_notes`

## 当前状态
占位已建立，供 RM3 先完成实现层映射登记；后续可继续替换为真实 agents、脚本或流程文件。
