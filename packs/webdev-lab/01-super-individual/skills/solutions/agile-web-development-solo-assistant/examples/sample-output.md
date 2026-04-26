# sample-output

## 页面清单
- 线索列表页
- 线索详情页
- 新建线索页
- 跟进记录页
- 统计概览页

## 数据结构草案
- lead：id、name、source、status、owner、created_at
- follow_up：id、lead_id、content、next_action、created_at
- owner：id、name、team

## 接口草案
- 获取线索列表
- 获取线索详情
- 新建线索
- 提交跟进记录
- 获取统计概览

## 目录骨架
- pages/
- components/
- services/
- stores/
- utils/

## 第一批文件建议
- app.tsx
- router.ts
- pages/lead-list/index.tsx
- pages/lead-detail/index.tsx
- services/lead.ts
- utils/mock.ts

## 下一句续跑指令
先补列表页、详情页和新建表单页，再把 services/lead.ts 与 mock 数据接起来。
