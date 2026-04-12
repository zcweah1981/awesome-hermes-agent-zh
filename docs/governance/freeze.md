# Hermes Agent 中文站 V2 — P0 冻结说明

冻结时间：2026-04-12

## 本轮冻结目标
把外部仓从 legacy 顶层入口切到 V2 最小治理状态，为后续 RM1-RM6 提供统一入口与放行基线。

## 本轮冻结范围
仅包含以下四类证据：
1. `README.md` 已切换为六模块固定入口
2. `docs/governance/README_GOVERNANCE.md`
3. `docs/governance/page-source-map.md`
4. `docs/governance/freeze.md`

## 明确不纳入本轮冻结的内容
以下内容存在与否，不作为本轮 P0 是否放行的判断依据：
- `site/`
- `tests/`
- `CHANGELOG.md`
- `vercel.json` 当前改动
- `DELIVERY_KANBAN.md` 当前删除

## 放行条件
当且仅当以下四项同时满足，P0 才可视为完成并进入 RM：
1. README 六模块固定入口可见
2. governance 文件存在
3. page-source-map 文件存在
4. freeze 文件存在

## 当前状态
accepted
