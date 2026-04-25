# 01-super-individual 安装说明

这个包不是只给你一份方案说明，而是让你先把微信小程序 MVP 压成“可开工代码骨架 + 实施包”。

## 它会帮你产出什么
- 页面清单
- 数据与接口草案
- 小程序目录结构建议
- 第一批代码文件建议
- 测试检查单

## 安装
```bash
bash ./install_to_profile.sh <profile-name-or-path>
```

## 最小试跑
```bash
<your-profile> chat --skills wechat-mini-program-solo-assistant -q "$(cat skills/solutions/wechat-mini-program-solo-assistant/examples/sample-input.md)"
```

## 跑完以后重点看什么
不要只看它有没有分析，而要看它有没有输出：
- 项目骨架
- 页面文件
- 接口 stub
- 首批实现顺序
