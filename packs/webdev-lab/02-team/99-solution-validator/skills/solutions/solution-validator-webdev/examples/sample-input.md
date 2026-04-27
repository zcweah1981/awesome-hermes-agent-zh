# sample-input

请验证“敏捷 Web 开发助手”团队协作版是否已经达到可继续推进的标准。

请基于下面这组最小交付物做判断：

## product 交付摘要
- 页面：dashboard、leads、lead detail、follow-up new
- 已定版：状态机、权限矩阵、搜索属于 MVP、默认排序 created_at desc
- 已明确：Dashboard 必须动态聚合，不允许静态 mock
- 已明确：搜索默认匹配 name / company / phone
- 已明确：today_* 统计统一使用北京时间（UTC+8）

## builder 交付摘要
- 已给出 Next.js + TypeScript 目录骨架
- 已给出页面文件建议、组件建议、状态流转说明
- 已补一条“提交跟进后列表、详情、Dashboard 三处如何刷新/回显”的页面联动说明

## api 交付摘要
- 已给出 User / Lead / FollowUp 字段摘要
- 已给出 GET /mock/meta/options、PATCH /api/leads/:id/status、POST /api/leads/:id/followups 等关键接口
- 已明确 sync_status=true 时为原子化回写
- 已明确 final field contract 只认 API 合同
- 已明确 latest_follow_up_at / latest_follow_up_summary 为唯一最近跟进字段命名
- 已明确 sales 越权访问详情、状态更新、跟进提交时一律 403
- 已明确 lead detail 只认 GET /api/leads/:id 一次返回 lead + followups

## qa 交付摘要
- 已给出主链路、权限、排序、Dashboard 聚合、错误码等检查项
- 已补“提交跟进并同步改状态”的联动检查项

请输出：最终结论、判断理由、主要缺口、修正建议、是否继续推进。
