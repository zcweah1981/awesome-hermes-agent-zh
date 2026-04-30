# Repo Policy

## 目标
定义 `awesome-hermes-agent-zh` 外部交付仓的公开保留原则，确保仓库只承载用户可见交付、正式资源与必要治理文件。

## 当前公开保留内容
- `README.md`
- `assets/`
- `docs/`
- `governance/`
- `packs/`
- `.github/workflows/content-check.yml`
- 与当前交付直接相关的公开资源文件

## 当前 docs 正式目录口径
当前正式模块目录固定为：
- `docs/00-文档总览.md`
- `docs/01-从这开始/`
- `docs/02-现成方案/`
- `docs/03-国内落地/`
- `docs/04-从OpenClaw过来/`
- `docs/05-遇到问题/`
- `docs/06-reference/`

补充规则：
- 不再把早期英文目录名（如 `docs/start-here/`、`docs/china/`、`docs/migrate/`、`docs/issues/`、`docs/solutions/`）当成当前正式路径口径。
- 页面路径、模块树和来源映射，以当前外部仓现状和 `governance/page-source-map.md` 为准。

## 入仓规则
1. 只新增已经真实开始写作、已经真实交付或已经真实需要的页面、资源和治理文件。
2. README 只维护已经真实存在的入口，不挂未来占位入口。
3. governance 只记录当前真实结构、来源映射、公开内容合同、route-map 合同、packs 映射和发布自检，不提前铺满整站未来计划。
4. packs、examples、assets 等目录只保留对用户真正有交付价值的内容。

## 严禁入仓的内容
以下内容不进入外部仓：
- 内部 PM 派单与巡查文件
- 内部阶段 checklist / runtime / dispatch log
- 本地治理脚本、巡查脚本、执行控制脚本
- 仅服务内部协作的临时研究记录
- 只对内部团队有意义的说明文件

## 一句话规则
外部仓只放公开交付；内部治理、内部节拍、内部控制全部留在内部管理主包，不混入公开仓。
