# miniapp-lab 安装说明

## 这个目录是什么
`packs/miniapp-lab/` 不是一个单 pack，而是“微信小程序助手”方案家族目录。

当前包含 3 类内容：
- `01-super-individual/`：超级个体版（单 Agent）
- `02-team-product/`、`03-team-builder/`、`04-team-api/`、`05-team-qa/`：团队协作版（多 Agent）
- `99-solution-validator/`：方案验证包

## 用户怎么拿到
### 方式 1：直接 clone 当前仓库
```bash
git clone git@github.com:zcweah1981/awesome-hermes-agent-zh.git
cd awesome-hermes-agent-zh/packs/miniapp-lab
```

### 方式 2：只拷贝这个目录
把整个 `packs/miniapp-lab/` 目录拷到你本地任意位置，再进入对应子目录安装。

## 你应该选哪一个
### 只想一个 Agent 先帮你把方案跑通
选：`01-super-individual/`

### 想按产品 / 实现 / 接口 / 测试分工
选团队版：
- `02-team-product/`
- `03-team-builder/`
- `04-team-api/`
- `05-team-qa/`

### 想验证这个方案到底是否成立
选：`99-solution-validator/`

## 建议安装到哪里
建议安装到独立 profile，而不是默认环境。

Hermes profile 默认目录通常是：
```text
~/.hermes/profiles/<profile-name>
```

## 最小使用方式
### 超级个体版
```bash
cd 01-super-individual
hermes profile create miniapp-solo --clone
./install_to_profile.sh miniapp-solo
miniapp-solo chat --skills wechat-mini-program-solo-assistant -q "$(cat skills/solutions/wechat-mini-program-solo-assistant/examples/sample-input.md)"
```

### 团队协作版
分别安装：
- `miniapp-product`
- `miniapp-builder`
- `miniapp-api`
- `miniapp-qa`

### 方案验证
```bash
cd 99-solution-validator
hermes profile create miniapp-validator --clone
./install_to_profile.sh miniapp-validator
```

## 手工测试怎么做
1. 先跑超级个体版一次
2. 检查输出是否包含：页面、功能、数据、接口、顺序、测试 六类结果
3. 再用验证包的 runbook/checklist 判断是否 pass
4. 如果团队协作版要上线，再按 4 个角色包逐个验证交接物是否成立
