# miniapp-lab 下载与安装说明

## 这个目录现在怎么用
`packs/miniapp-lab/` 对外推荐直接下载两个压缩包：

- `01-super-individual.zip`：超级个体版（单 Agent）
- `02-team.zip`：团队协作版（多 Agent，内含 validator）

目标是让用户不用再分别找很多子目录，而是下载一个 zip，解压后立刻得到可安装的目录结构。

## 你应该选哪一个
### 只想先让一个 Agent 把小程序 MVP 跑通
下载：`01-super-individual.zip`

适合：
- 个人开发者
- 先要 MVP 结构包
- 先验证需求、页面、接口、测试是否成套成立

### 想按产品 / 实现 / 接口 / 测试分工
下载：`02-team.zip`

解压后会得到：
- `02-team/01-product/`
- `02-team/02-builder/`
- `02-team/03-api/`
- `02-team/04-qa/`
- `02-team/99-solution-validator/`
- `02-team/install_all.sh`

## 用户怎么拿到
### 方式 1：直接下载 zip
在 GitHub 仓库里直接下载：
- `packs/miniapp-lab/01-super-individual.zip`
- `packs/miniapp-lab/02-team.zip`

### 方式 2：clone 仓库后本地取用
```bash
git clone git@github.com:zcweah1981/awesome-hermes-agent-zh.git
cd awesome-hermes-agent-zh/packs/miniapp-lab
```

## 建议安装到哪里
建议安装到独立 profile，而不是默认环境。

Hermes profile 默认目录通常是：
```text
~/.hermes/profiles/<profile-name>
```

## 最小使用方式
### 超级个体版
```bash
cd /path/to/01-super-individual
hermes profile create miniapp-solo --clone
bash ./install_to_profile.sh miniapp-solo
miniapp-solo chat --skills wechat-mini-program-solo-assistant -q "$(cat skills/solutions/wechat-mini-program-solo-assistant/examples/sample-input.md)"
```

### 团队协作版
```bash
cd /path/to/02-team
hermes profile create miniapp-product --clone
hermes profile create miniapp-builder --clone
hermes profile create miniapp-api --clone
hermes profile create miniapp-qa --clone
hermes profile create miniapp-validator --clone
bash ./install_all.sh
```

如果你想手动安装，也可以分别进入：
- `01-product/`
- `02-builder/`
- `03-api/`
- `04-qa/`
- `99-solution-validator/`

各自执行：
```bash
bash ./install_to_profile.sh <profile-name-or-path>
```

## 手工测试怎么做
1. 先下载并解压其中一个 zip
2. 超级个体版：确认输出包含页面、功能、数据、接口、顺序、测试六类结果
3. 团队协作版：确认 `install_all.sh` 能把 5 个角色包装进对应 profile
4. 团队协作版串跑后，再用 `99-solution-validator` 判断是否 pass / pass with fixes / fail
