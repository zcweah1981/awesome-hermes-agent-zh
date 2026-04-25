# 示例输出

## 页面清单
1. `pages/activity-list/`：活动列表页
2. `pages/activity-detail/`：活动详情页
3. `pages/signup-form/`：报名表单页
4. `pages/result/`：报名结果页

## 功能清单
- 浏览活动列表
- 查看活动详情
- 提交报名表单
- 查看报名结果

## 数据结构建议
### activity
- `id`
- `title`
- `summary`
- `startTime`
- `location`
- `status`

### signup
- `activityId`
- `name`
- `phone`
- `remark`
- `submitTime`

## 接口建议
- `GET /activities`
- `GET /activities/:id`
- `POST /signups`
- `GET /signups/:id/result`

## 小程序代码骨架建议
```text
miniprogram/
├─ app.js
├─ app.json
├─ app.wxss
├─ pages/
│  ├─ activity-list/
│  ├─ activity-detail/
│  ├─ signup-form/
│  └─ result/
├─ services/
│  └─ activity.js
├─ utils/
│  └─ mock.js
└─ components/
   └─ activity-card/
```

## 第一批先生成的文件
- `app.json`：先把页面路由注册完整
- `pages/activity-list/index.*`：先让列表页能打开
- `pages/activity-detail/index.*`：先打通详情页跳转
- `pages/signup-form/index.*`：先把表单结构搭出来
- `services/activity.js`：先用 mock 数据返回列表/详情
- `utils/mock.js`：先放假数据，后续再替换真实接口

## 开发顺序
1. 先注册页面路由
2. 先用 mock 数据跑通页面
3. 再接表单提交
4. 最后替换成真实接口

## 测试检查单
- 页面都能打开
- 列表可以进入详情
- 表单字段能填写
- 提交后能进入结果页
- mock 数据替换点清楚
