---
quick_reference:
  - checkedAt: '2026-10-03'
    hermesVersion: v2026.9.24
    verification: docs-reviewed
    kind: model
    id: xiaomi-mimo-metered-native
    vendor: 小米 MiMo
    product: 开放平台按量 API
    region: 中国区
    connection: native
    provider: xiaomi
    protocol: openai
    endpoint: 'https://api.xiaomimimo.com/v1'
    modelIds:
      - mimo-v2.6-flash
      - mimo-v2.6-pro
    permissions: 使用开放平台按量 Key（sk），按实际用量计费；与 Token Plan 的 Key/地址不同。
    configExample: |-
      hermes config set model.provider xiaomi
      hermes config unset model.base_url
      hermes config set XIAOMI_BASE_URL https://api.xiaomimimo.com/v1
      hermes config unset model.api_mode
      hermes config set XIAOMI_API_KEY "<YOUR_API_KEY>"
      hermes config set model.default mimo-v2.6-flash
    diagnostics:
      - /docs/issues/provider-endpoint
    sources:
      - url: 'https://mimo.mi.com/docs/en-US/quick-start/summary/first-api-call'
      - url: 'https://mimo.mi.com/docs/en-US/quick-start/summary/model'
      - url: 'https://raw.githubusercontent.com/NousResearch/hermes-agent/v2026.9.24/hermes_cli/auth.py'
        revision: v2026.9.24
  - checkedAt: '2026-10-03'
    hermesVersion: v2026.9.24
    verification: docs-reviewed
    kind: model
    id: xiaomi-mimo-token-plan-native
    vendor: 小米 MiMo
    product: Token Plan
    region: 中国区
    connection: native
    provider: xiaomi
    protocol: openai
    endpoint: 'https://token-plan-cn.xiaomimimo.com/v1'
    modelIds:
      - mimo-v2.6-flash
      - mimo-v2.6-pro
    permissions: 使用套餐专属 tp / ttp Key 与套餐 endpoint，不能混用按量 Key；个人/团队额度、可用模型及用法以套餐和控制台为准。
    configExample: |-
      hermes config set model.provider xiaomi
      hermes config unset model.base_url
      hermes config set XIAOMI_BASE_URL https://token-plan-cn.xiaomimimo.com/v1
      hermes config unset model.api_mode
      hermes config set XIAOMI_API_KEY "<YOUR_API_KEY>"
      hermes config set model.default mimo-v2.6-flash
    diagnostics:
      - /docs/issues/provider-endpoint
    sources:
      - url: 'https://mimo.mi.com/docs/en-US/quick-start/summary/first-api-call'
      - url: 'https://mimo.mi.com/docs/en-US/quick-start/summary/model'
      - url: 'https://raw.githubusercontent.com/NousResearch/hermes-agent/v2026.9.24/hermes_cli/auth.py'
        revision: v2026.9.24
---
# 📱 09-MiMo V2.6 接入：按量 API 与 Token Plan

内容更新：2026-10-03（同源配置迁移）；原教程复核日期：2026-09-30；速查条目核验日期见配置卡。厂商模型更新与 Hermes v2026.9.24 原生 provider 配置分别核对；未购买套餐、下载权重或执行真实 API/桌面测试。

## 🎯 先选择产品路线

MiMo V2.6 系列于 2026-09-22 发布，已核验的模型 ID 见[本页同源模型配置卡](/docs/china/models/mimo-v26#model-quick-reference)。先按账户允许的模型选择，不能把官网能力宣传当作 Hermes 全部模态已联调。

按量与 Token Plan 的地址、密钥类型及权益见[本页同源模型配置卡](/docs/china/models/mimo-v26#model-quick-reference)。两类 Key 和地址不能混用。这里不复制尚未独立确认的价格或套餐配额；调用前查官方计费和账户余量。已有其他平台的 MiMo 额度，也不等于持有小米直连 Key。

## ⚙️ 原生 xiaomi provider

原生 provider、环境变量、endpoint 覆盖及精确模型 ID 统一见[本页同源模型配置卡](/docs/china/models/mimo-v26#model-quick-reference)。复制对应产品的最小配置，在所用 profile 中替换密钥占位符并保存；真实 Key 不放进聊天、截图或仓库。切回按量时删除或改回遗留 Base URL 覆盖，并核对实际请求路线。

## 🖥️ 桌面短配置卡

1. 在[本页同源模型配置卡](/docs/china/models/mimo-v26#model-quick-reference)选产品与区域，再把同一条路线的 Key、provider、协议与 Base URL 映射到桌面设置。
2. 在 **Settings → Model** 保存 profile 默认模型；当前聊天输入框另选同一个精确 ID，核对本机或远端后端 profile。
3. 目录没有新 ID 时用手动添加；空目录行为随版本不同，参阅[桌面教程](/docs/start/personalize/desktop-app)。
4. 自行完成短问答，再让 Agent 读取一个测试文本并总结，核对实际工具调用、产物和厂商用量。Test 与任务请求可能收费，执行前确认额度。
5. 分开记录连通、工具任务、模态和用量结果。本文未实测，不能用保存成功替代验收。

## 🔄 工具重复调用与旧模型迁移

厂商 9 月 25 日更新服务以缓解 V2.6 工具重复调用，模型 ID 不变；9 月 27 日技术文章讨论训练改进并包含 Hermes 测试场景。这是厂商证据，不是本站在你的工作流中的测试结果。遇到循环先停止任务，保存脱敏的模型 ID、版本、请求时间、工具参数与错误，勿持续重试付费或写入动作。

`mimo-v2.5` 计划于 **2026-10-21 北京时间 10:00** 弃用，固定配置应提前迁移并验收。云端同名模型更新不保证本地自托管权重同步：若要获得相关改进，需核对 MOPD 权重与部署版本，不能只改 API 模型字符串。

## 🩺 排障顺序

| 症状 | 先检查 | 验收 |
|---|---|---|
| 401 / 额度错误 | API 与 Token Plan 的 Key、地址、账户权限是否混用 | 对应控制台与真实请求匹配 |
| 模型不存在 | 精确 ID、套餐目录、手动添加及后端版本 | 实际回复来自目标模型 |
| 工具不断重复 | 服务更新时间、旧本地权重、上下文与工具返回 | 小任务完成且无多余写操作 |
| 云端修复但本地仍循环 | MOPD 权重及推理部署版本 | 隔离样例复测，不宣称 ID 相同就已修复 |

## 📖 官方依据

- [模型更新](https://mimo.mi.com/docs/en-US/updates/model)
- [首次 API 调用与产品入口](https://mimo.mi.com/docs/en-US/quick-start/summary/first-api-call)
- [模型目录与弃用](https://mimo.mi.com/docs/en-US/quick-start/summary/model)
- [工具重复调用与 MOPD](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition)
- [Hermes 稳定 provider 与覆盖变量](https://github.com/NousResearch/hermes-agent/blob/v2026.9.24/hermes_cli/auth.py)

## ➡️ 下一步

- 回到：[国内模型总览](./01-总览.md)
- 桌面操作：[桌面上手与办公实战](/docs/start/personalize/desktop-app)
- 聚合网关：[自定义兼容接口](./08-自定义兼容接口.md)
