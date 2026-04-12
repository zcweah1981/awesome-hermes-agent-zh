# 部署与连接问题

当你已经完成安装和基础配置，但在联网、代理、证书、连接上游或部署后访问阶段被卡住时，优先看本页。

## 问题现象

你可能会看到以下现象之一：
- `SSL: CERTIFICATE_VERIFY_FAILED`
- 请求长时间无响应，最终超时
- 明明设置了代理，但请求仍失败
- 改了 `base_url` / endpoint 后开始出现兼容性异常
- 部署后运行环境与本地表现不一致

## 可能原因

- 本地代理、公司防火墙或网络中间层注入了不受信任证书
- 默认请求目标与当前网络环境不匹配
- `http_proxy` / `https_proxy` 设置不完整或与运行环境不一致
- 过早引入 custom endpoint，导致连接问题与模型问题交织
- 部署环境变量、系统 CA、运行平台行为与本地不同

## 优先排查步骤

1. 先区分是“模型不可用”还是“请求根本没出去 / 回不来”
2. 如果报 SSL 错误，先检查本地证书与代理链路
3. 如果报超时，先检查目标上游、代理设置和网络可达性
4. 如果改过 `base_url`，先回退到最小官方路径验证问题是否消失
5. 如果只在部署环境复现，逐项比对环境变量与网络出口差异

## 最终解决办法

### SSL 证书校验失败
在确定问题来自代理注入或本地证书链异常时，可先临时验证：

```bash
export CURL_CA_BUNDLE=""
```

macOS 永久修复可尝试系统 Python 的证书安装脚本：

```bash
/Applications/Python\ 3.x/Install\ Certificates.command
```

### 请求超时
显式声明代理后重试：

```bash
export http_proxy="http://127.0.0.1:你的端口"
export https_proxy="http://127.0.0.1:你的端口"
```

如果你并不依赖代理，优先确认默认上游是否可直连，而不是继续叠加更多转发配置。

### custom endpoint 异常
先回退到官方 provider 或最小可复现配置；确认最小链路正常后，再逐步恢复自定义 `base_url` 与兼容层设置。

## 证据来源

- `docs/known-issues.md` 中已有的 SSL、代理、超时相关旧版排障内容
- Hermes Agent 中文站现有模型与接入文档：`docs/custom-openai-compatible.md`、`docs/models.md`
- RM5 研究链路中对 deploy / 连接类问题的收敛结论

## 相关延伸

- [遇到问题总览](./index.md)
- [安装与环境问题](./install.md)
- [模型与 provider 问题](./models.md)
- [国内落地](../china/index.md)
