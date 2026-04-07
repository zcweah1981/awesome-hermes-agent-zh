# Advanced Coding Team Starter (进阶代码开发团队)

本模板展示了一个更接近真实开发场景的“三位一体”协作流程：**PM (主管) -> Coder (开发) -> Reviewer (审计)**。

## 协作逻辑
1. **PM**: 接收用户模糊需求，拆解为具体任务。
2. **Coder**: 编写核心逻辑，并在本地保存为文件。
3. **Reviewer**: 读取 Coder 生成的文件，检查 Bug 和性能问题，并给出修改意见。

## 目录结构
- `config.yaml`: 核心编排配置。
- `system_prompt.txt`: PM 人设。
- `coder_system.txt`: 开发人设 (Python/Rust 专家)。
- `reviewer_system.txt`: 审计人设 (代码安全与性能专家)。

## 如何启动
```bash
hermes --config config.yaml
```

## 实战指令示例
> “帮我写一个 Python 脚本，用于批量压缩当前目录下的所有图片。写完后让 Reviewer 审计代码安全性。”
