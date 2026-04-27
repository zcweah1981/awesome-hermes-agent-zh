# 微信小程序接口设计专家 示例输出

## 实体字段
### activity
- id
- title
- cover_url
- start_at
- end_at
- location
- quota
- joined_count
- status
- summary

### signup
- id
- activity_id
- user_id
- name
- phone
- company
- note
- status
- created_at

## 接口清单
- GET /api/activities
- GET /api/activities/:id
- POST /api/activities/:id/signups
- GET /api/me/signups
- GET /api/me/signups/:id

## 请求/响应关键字段
### POST /api/activities/:id/signups
请求体
- name
- phone
- company
- note

成功返回
- signup_id
- activity_id
- status
- created_at

## 错误场景
- 活动不存在：404
- 已结束或已报满：409
- 表单缺字段：422

## 下游接收点
### 给 builder
- 各页面对应的接口与字段
- 提交成功后的返回口径

### 给 qa
- 关键错误码
- 报名成功/报满/已结束三种主路径
