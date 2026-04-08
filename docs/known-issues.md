# 🛡️ 常见问题与排障指南 (Troubleshooting)

在国内环境下运行 Hermes Agent，你可能会遇到一些特有的坑。本指南旨在帮你快速跳出困境，直接进入开发阶段。

---

## 1. 网络与连接问题

### ❌ [SSL: CERTIFICATE_VERIFY_FAILED]
**报错现象**: `urllib3.exceptions.MaxRetryError: HTTPSConnectionPool...` 或明确的 SSL 证书验证失败提示。  
**原因分析**: 国内某些网络代理软件（或公司防火墙）会拦截 HTTPS 请求并注入自签名证书，而 Python 环境不信任该证书。  
**直接解法 (推荐)**:
- **macOS/Linux**: 在终端执行：
  ```bash
  export CURL_CA_BUNDLE=""
  ```
- **Windows**: 
  ```powershell
  $env:CURL_CA_BUNDLE=""
  ```
- **永久解决 (macOS)**: 运行 `/Applications/Python\ 3.x/Install\ Certificates.command`。

---

### ❌ 请求超时 (ConnectTimeout)
**报错现象**: 程序卡住，最终抛出 `TimeoutError`。  
**原因分析**: 默认配置文件可能指向了 `api.anthropic.com`。  
**直接解法**:
- **模型检查**: 确保你已经通过 `hermes model` 选择了可用模型，或直接用 `hermes chat --provider deepseek --model deepseek-chat` 测试。
- **代理配置**: 如果你必须通过代理访问，请在终端明确设置：
  ```bash
  export http_proxy="http://127.0.0.1:你的端口"
  export https_proxy="http://127.0.0.1:你的端口"
  ```

---

## 2. 字符编码与显示问题

### ❌ 终端显示乱码 (UTF-8)
**报错现象**: 中文输出显示为 `\x..` 这种 16 进制字符，或者方块。  
**直接解法**:
- **推荐工具**: 请务必使用 **Windows Terminal**、**iTerm2** 或 **VS Code 内置终端**。
- **环境变量强制**: 在启动 `hermes` 前执行：
  ```bash
  export PYTHONIOENCODING=utf8
  ```

---

## 3. 环境与依赖问题

### ❌ [No module named 'PIL']
**报错现象**: 报错提示缺失 `PIL` 或 `Pillow`。  
**直接解法**:
```bash
pip install Pillow --break-system-packages
```

### ❌ 配置文件权限问题
**报错现象**: 提示无法写入 `~/.hermes/config.yaml`。  
**直接解法**: 检查该目录的所有权。如果是 Linux，请确保当前用户有权限：
```bash
sudo chown -R $USER:$USER ~/.hermes
```

---

## 💬 还没解决？
如果以上方案都无效，请在交流群中贴出你的 **报错全截图**。

---
<p align="center">
  Built with ❤️ by <a href="https://hermes-zh.com">Hermes Agent 中文社区</a>
</p>
