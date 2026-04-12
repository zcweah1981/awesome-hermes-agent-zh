# 开始上手

## 这一层适合谁
- 已经跑通一次 Hermes，但还不够稳定的人
- 想弄清配置边界、provider 选择、基础排错顺序的人
- 想判断 Hermes 是否适合自己的工作方式的人

## 学完能做到什么
- 理解 `.env` 和 `config.yaml` 的分工
- 会用 `hermes model` 切换 provider / model
- 知道什么时候该坚持官方路径，什么时候才考虑 custom

## 先看哪一页
1. `docs/models.md`
2. `docs/install-prep.md`
3. `docs/config-errors.md`
4. `docs/fit-guide.md`

## 需要准备什么
- 至少跑通过一次 Hermes
- 已经有一个默认 provider
- 愿意按固定流程排错，而不是随意堆配置

## 推荐动作
1. 再确认一次 secrets 放 `~/.hermes/.env`
2. 再确认非 secret 配置放 `config.yaml`
3. 用 `hermes model` 做一次切换
4. 判断自己是否真的需要 OpenRouter / custom endpoint
5. 写下适合自己的一条最短使用路径

## 常见卡点
- 继续沿用旧博客和旧截图的配置方法
- 把 custom endpoint 当成默认解法
- 不理解 provider 别名与官方支持边界
- 只会“跑通一次”，不会“稳定复现”

## 完成标志
- 你已经能稳定复现一次安装与启动流程
- 你能说清自己为什么选这个 provider
- 你知道下一步该去做案例、starter 还是迁移判断

## 下一层是什么
完成本层后进入：[玩出花样](./build-something.md)
