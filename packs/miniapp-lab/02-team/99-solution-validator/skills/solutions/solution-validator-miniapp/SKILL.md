---
name: solution-validator-miniapp
description: 验证微信小程序助手方案是否通过最小可行验收。
---

# 什么时候触发
当一个现成方案页及其 pack 已产出，需要判断是否 pass / pass with fixes / fail 时触发。

# 输入
- 页面正文
- sample-input
- sample-output
- manual-test-runbook
- review-checklist

# 输出
- pass / pass with fixes / fail
- 问题清单
- 修复建议

# 最小步骤
1. 核对页面和 pack 是否齐
2. 跑 sample-input
3. 对照 checklist 判断
4. 输出结论

# 常见坑
- 只看文档不看实际输出
- 把能跑一次误判成稳定通过
- 不区分页面问题和实现问题

# 验证方式
必须给出 pass / pass with fixes / fail 三选一。
