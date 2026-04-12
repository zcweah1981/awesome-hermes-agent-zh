# 安装与环境问题

当 Hermes Agent 还没真正跑起来，或者你在安装脚本、依赖、权限、Python 环境这里被卡住时，优先看本页。

## 问题现象

你可能会看到以下现象之一：
- 安装脚本执行后仍无法启动 Hermes
- 报错提示缺少 `PIL` / `Pillow` 等依赖
- 提示无法写入 `~/.hermes/config.yaml` 或相关目录
- 同一台机器上，终端里与文档中的行为不一致
- 中文输出乱码，或终端显示为 `\x..`、方块

## 可能原因

- Python 环境与执行命令不在同一上下文
- 系统级依赖未安装，或额外包未补齐
- `~/.hermes` 目录权限被 root 或其他用户占用
- 当前终端编码、Shell、WSL/本机环境与预期不一致
- 先改了太多配置，导致“安装问题”和“模型问题”混在一起

## 优先排查步骤

1. 先确认你当前使用的是哪个 Python / pip / shell 环境，不要在多个终端混用
2. 检查 Hermes 是否已完成基础安装，再判断是安装失败还是后续模型配置失败
3. 若报缺包，先补齐明确缺失的依赖，不要直接整体重装系统环境
4. 若提示目录不可写，先检查 `~/.hermes` 的所有权和当前用户权限
5. 若终端乱码，先切换到 Windows Terminal、iTerm2 或 VS Code 内置终端，并确认 UTF-8 环境变量

## 最终解决办法

### 依赖缺失：`No module named 'PIL'`
先补齐 Pillow：

```bash
pip install Pillow --break-system-packages
```

### 权限问题：无法写入 `~/.hermes`
先修正目录所有权：

```bash
sudo chown -R $USER:$USER ~/.hermes
```

### 终端乱码或 UTF-8 显示异常
在启动 Hermes 前强制设置：

```bash
export PYTHONIOENCODING=utf8
```

如果仍有乱码，优先更换终端，而不是继续在旧终端里反复试错。

## 证据来源

- `docs/known-issues.md` 中已有的 PIL / 权限 / UTF-8 相关旧版排障内容
- Hermes Agent 中文站现有安装与上手相关页面：`docs/install-prep.md`、`docs/quick-start.md`
- RM5 Method Pack 对安装类问题页的结构要求

## 相关延伸

- [遇到问题总览](./index.md)
- [模型与 provider 问题](./models.md)
- [部署与连接问题](./deploy.md)
- [从这开始](../start/index.md)
