# miniapp-lab 安装说明

## 用途
这个 pack 用来支持《现成方案 / 微信小程序助手》页面的默认实现路径。

## 安装内容
- SOUL.md
- wechat-mini-program-assistant skill
- templates / examples / runbook

## 用户怎么拿到
### 方式 1：直接 clone 当前仓库
```bash
git clone git@github.com:zcweah1981/awesome-hermes-agent-zh.git
cd awesome-hermes-agent-zh/packs/miniapp-lab
```

### 方式 2：只拷贝这个 pack 目录
把整个 `packs/miniapp-lab/` 目录拷到你本地任意位置，然后进入这个目录执行安装脚本。

## 建议安装到哪里
建议安装到一个单独 profile，而不是直接覆盖默认环境。

Hermes profile 默认目录通常是：
```text
~/.hermes/profiles/<profile-name>
```

推荐先创建一个测试 profile：
```bash
hermes profile create miniapp-lab --clone
```

## 怎么安装
在 `packs/miniapp-lab/` 目录里执行：

### 直接传 profile 名称
```bash
./install_to_profile.sh miniapp-lab
```

### 或传完整路径
```bash
./install_to_profile.sh ~/.hermes/profiles/miniapp-lab
```

安装后会把下面两部分复制进去：
- `SOUL.md` -> 目标 profile 根目录
- `skills/solutions/wechat-mini-program-assistant/` -> 目标 profile 的 skills 目录

## 怎么开始用
### 1. 进入这个 profile
```bash
miniapp-lab chat --skills wechat-mini-program-assistant
```

### 2. 或者直接单次触发
```bash
miniapp-lab chat --skills wechat-mini-program-assistant -q "$(cat skills/solutions/wechat-mini-program-assistant/examples/sample-input.md)"
```

## 最小手工验证
1. 安装 pack 到独立 profile
2. 用 `sample-input.md` 触发一次
3. 检查输出是否至少包含：
   - 页面清单
   - 功能清单
   - 数据结构建议
   - 接口建议
   - 开发顺序
   - 测试检查单
4. 再看超级个体版 / 团队协作版边界是否清楚

更完整的验证方式见：
- `skills/solutions/wechat-mini-program-assistant/references/manual-test-runbook.md`
- `skills/solutions/wechat-mini-program-assistant/templates/review-checklist.md`
