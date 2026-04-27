# 微信小程序前端实现专家 示例输出

## 目录骨架
- pages/activity/list
- pages/activity/detail
- pages/signup/form
- pages/signup/success
- pages/me/signup-list
- pages/me/signup-detail
- components/activity-card
- components/empty-state
- components/status-badge
- services/activity.ts
- services/signup.ts

## 页面实现顺序
1. 活动列表
2. 活动详情
3. 报名表单
4. 报名成功页
5. 我的报名
6. 报名详情

## 关键组件
- activity-card：活动摘要卡片
- status-badge：展示报名中/已结束/已报满
- empty-state：无活动、无报名记录兜底
- submit-bar：报名页底部提交区

## 页面状态建议
- 列表页：loading / has-data / empty / error
- 详情页：loading / has-data / ended / full / error
- 报名页：editing / submitting / success / error
- 我的报名：loading / has-data / empty / error

## 下游接收点
### 给 api
- 页面需要的字段清单
- 各页面请求时机
- 报名提交成功后的返回字段预期

### 给 qa
- 页面实现顺序
- 每页成功态 / 空态 / 报错态
- 关键跳转链路
