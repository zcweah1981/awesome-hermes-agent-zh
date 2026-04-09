# Hermes 常见配置错误排查

这篇专门处理“不是安装失败，而是配置写错”的问题。

---

## 最常见的 6 类错误

### 1. 密钥放错地方

正确做法：
- secret 放 `~/.hermes/.env`
- 参数放 `~/.hermes/config.yaml`

错误后果：
- 密钥泄漏
- 配置混乱
- 后续切模型时很难维护

### 2. provider 名称写错

例如文档里明明是官方 provider，结果自己写成 custom，或者 provider 名称和模型服务不一致。

建议：
- 先用 `hermes model`
- 再参考 [模型与 Provider](./models.md)

### 3. base_url 对了，但 model 写错

很多 OpenAI-compatible 接口问题，本质不是 URL，而是模型名不对。

### 4. `.env` 写了，但当前 shell 没生效

你需要确认：
- 文件位置是否正确
- 变量名是否正确
- 当前 Hermes 是否真的读取到该环境

### 5. 复制了旧文档配置

Hermes 迭代很快，旧博客或旧截图很容易过时。优先看：
- 官方文档
- 当前仓库最新页面

### 6. 一上来就写很多自定义项

对新用户最稳的方式通常是：
- `hermes setup`
- `hermes model`
- 跑通后再加高级配置

---

## 一个判断原则

如果你的目标只是“先跑通”，那配置应越少越好。

优先级建议：
1. 官方 provider
2. `.env` 密钥
3. `hermes model`
4. 最后才是复杂 custom 配置

---

## 排查顺序

1. 先确认 provider 是否官方支持
2. 再确认 API key 变量名
3. 再确认 model 名
4. 最后才检查 base_url / 代理 / 证书

---

## 下一步

- 先回基础路径：看 [快速开始](./quick-start.md)
- 先校验 provider：看 [模型与 Provider](./models.md)
- 如果是网络或证书问题：看 [常见问题](./known-issues.md)
