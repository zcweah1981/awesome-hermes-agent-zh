# 示例输出

## 一句话结论
先按“活动报名微信小程序 MVP”落一版可开工骨架：先用 mock 数据跑通活动列表、详情、报名、结果四个页面，再逐步替换成真实接口。

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
│  │  ├─ index.js
│  │  ├─ index.wxml
│  │  ├─ index.wxss
│  │  └─ index.json
│  ├─ activity-detail/
│  │  ├─ index.js
│  │  ├─ index.wxml
│  │  ├─ index.wxss
│  │  └─ index.json
│  ├─ signup-form/
│  │  ├─ index.js
│  │  ├─ index.wxml
│  │  ├─ index.wxss
│  │  └─ index.json
│  └─ result/
│     ├─ index.js
│     ├─ index.wxml
│     ├─ index.wxss
│     └─ index.json
├─ services/
│  └─ activity.js
├─ utils/
│  └─ mock.js
└─ components/
   └─ activity-card/
      ├─ index.js
      ├─ index.wxml
      └─ index.wxss
```

## 第一批先生成的文件
- `app.json`：先把页面路由注册完整
- `pages/activity-list/index.*`：先让列表页能打开，先展示 mock 列表
- `pages/activity-detail/index.*`：先打通从列表进入详情
- `pages/signup-form/index.*`：先把姓名、手机号、备注三项表单搭出来
- `pages/result/index.*`：先把“报名成功/失败”状态页搭出来
- `services/activity.js`：统一封装列表、详情、报名提交这几个请求入口
- `utils/mock.js`：先放假数据，后续再替换真实接口

## app.json 初版建议
```json
{
  "pages": [
    "pages/activity-list/index",
    "pages/activity-detail/index",
    "pages/signup-form/index",
    "pages/result/index"
  ],
  "window": {
    "navigationBarTitleText": "活动报名",
    "navigationBarBackgroundColor": "#ffffff",
    "navigationBarTextStyle": "black"
  }
}
```

## services/activity.js 初版职责
```js
export function getActivityList() {}
export function getActivityDetail(id) {}
export function submitSignup(payload) {}
export function getSignupResult(id) {}
```

## utils/mock.js 初版职责
```js
export const activityList = [
  {
    id: 'a1',
    title: 'Hermes 线下分享会',
    summary: '面向新用户的活动报名示例',
    startTime: '2026-04-30 19:30',
    location: '深圳南山',
    status: 'open'
  }
]
```

## 页面跳转主线
1. 列表页点击活动卡片 -> 进入详情页
2. 详情页点击“立即报名” -> 进入报名页
3. 报名页提交成功 -> 进入结果页

## 开发顺序
1. 先注册页面路由
2. 先把列表页和详情页跑起来
3. 再补报名表单与结果页
4. 再把请求统一收口到 `services/activity.js`
5. 最后把 `utils/mock.js` 替换成真实接口

## ACP 续跑时可以继续下的指令
```text
基于这版骨架继续生成真实文件：
1. 先补 pages/activity-list/index.wxml 和 index.js
2. 列表数据先读取 utils/mock.js
3. 点击卡片后跳到 activity-detail
4. 再补 pages/activity-detail/index.wxml 和 index.js
5. 暂时不要接真实后端
```

## 测试检查单
- 页面都能打开
- 列表可以进入详情
- 详情页可以进入报名页
- 表单字段能填写
- 提交后能进入结果页
- mock 数据替换点清楚
- `services/` 和 `utils/` 的职责分开了
