# 常见问题与排障指南 (Known Issues)

在国内环境下运行 Hermes Agent，你可能会遇到一些特有的坑。本页面汇总了已知的常见问题及其解决方案。

## 1. 网络与连接问题

### API 请求超时 (Timeout)
**现象**: 报错 `ConnectTimeout` 或 `Connection lost`。
**解决**:
- 检查你的网络环境。如果你在本地运行且没有科学上网，请务必使用 **DeepSeek** 或 **Qwen** 等国内可以直接访问的模型，并确保 `base_url` 配置正确。
- 如果你使用了代理，请在终端设置环境变量：
  ```bash
  export http_proxy="http://127.0.0.1:你的端口"
  export https_proxy="http://127.0.0.1:你的端口"
  ```

### SSL 证书验证失败
**现象**: 报错 `[SSL: CERTIFICATE_VERIFY_FAILED]`。
**解决**: 这通常是由于本地 Python 环境的证书库过旧。
- 在 macOS 上运行：`/Applications/Python\ 3.x/Install\ Certificates.command`
- 或者在配置文件中尝试关闭验证（不推荐，仅用于排障）。

## 2. 字符编码与显示

### Windows 终端乱码 (UTF-8)
**现象**: 中文显示为方块或乱码。
**解决**:
- 推荐使用 **Windows Terminal** 或 **VS Code 内置终端**。
- 在旧版 CMD 中，执行 `chcp 65001` 切换到 UTF-8 编码。

## 3. 依赖与安装

### pip 安装速度慢
**解决**: 使用清华大学或阿里云的镜像源。
```bash
pip install hermes-agent -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### ModuleNotFoundError: No module named 'PIL'
**现象**: 在使用图像相关功能时报错。
**解决**: 手动安装 Pillow 库。
```bash
pip install Pillow --break-system-packages
```

## 4. 模型行为

### 模型回复英文
**现象**: 虽然用中文提问，但 Agent 回复英文。
**解决**: 
- 在 `system_prompt.txt` 中明确加入指令：“请始终使用中文回答所有问题。”
- 检查你使用的模型是否原生支持中文（DeepSeek 和 Qwen 均支持良好）。

---

如果你遇到了本页未涵盖的问题，欢迎在 GitHub 上提交 Issue 或在交流群中反馈。