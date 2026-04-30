# Publishing Checklist

更新时间：2026-04-30（北京时间）

本清单用于内容仓发布前自检。它只覆盖公开仓内容质量，不替代内部 PM 派单或独立站部署流程。

## 适用场景

- 新增或修改 docs 页面。
- 新增或修改 packs 方案包。
- 调整 README、assets 或 governance。
- 准备把内容仓变更推送给独立站消费。

## 发布前必查

### 1. 仓库结构

- [ ] 新内容放在当前正式目录树内。
- [ ] 没有新增旧英文正式路径，例如 `docs/start-here/`、`docs/solutions/`。
- [ ] 没有提交内部 PM 派单、dispatch log、巡查脚本、临时执行看板。
- [ ] 如果新增顶层目录，已经说明它为什么属于公开交付。

### 2. docs 页面

- [ ] Markdown 可以在 GitHub 直接阅读。
- [ ] 页面标题、段落、链接和图片路径可读。
- [ ] 图片资源指向仓内公开路径。
- [ ] 页面没有内部状态字段、内部路径、未脱敏 token 或本地 secrets。
- [ ] 如果页面需要被独立站渲染，已更新 `governance/site-route-map.yaml`。

### 3. route-map

- [ ] `source` 指向真实存在的 Markdown 文件。
- [ ] `slug` 稳定、可读、不包含本地路径。
- [ ] `title` 与 Markdown 主标题一致或语义一致。
- [ ] `module`、`section`、`nav_group` 与目录位置一致。
- [ ] `order` 不与同组页面冲突到影响导航排序。
- [ ] `status` 为当前真实发布状态。

### 4. packs

- [ ] 每个 pack 有 `manifest.yaml`。
- [ ] 每个 pack 有 `INSTALL.md`。
- [ ] manifest YAML 可解析。
- [ ] manifest 的 `doc` 指向真实方案页。
- [ ] manifest 的 `install` 指向真实安装入口。
- [ ] manifest 的 `download` 指向真实 zip 文件。
- [ ] 如目录内容变更，zip 包已同步刷新。
- [ ] `packs/README.md` 和 `governance/packs-map.md` 已同步。

### 5. README 与 assets

- [ ] README 只链接真实存在的页面和治理文件。
- [ ] README 图片都存在于 `assets/`。
- [ ] 图片 alt 文案能说明用途。
- [ ] 没有引用本地绝对路径或临时截图路径。

### 6. governance

- [ ] `repo-structure.md` 与真实目录结构一致。
- [ ] `repo-policy.md` 的入仓边界仍然准确。
- [ ] `page-source-map.md` 覆盖当前模块入口。
- [ ] `content-contract.md` 与 route-map / packs 实际字段一致。
- [ ] `packs-map.md` 覆盖当前开放方案包。

## 推荐本地检查命令

在仓库根目录执行：

```bash
git status --short
python3 - <<'PY'
from pathlib import Path
import yaml
root = Path('.')
for mf in sorted(root.glob('packs/*/manifest.yaml')):
    data = yaml.safe_load(mf.read_text())
    for key in ['doc', 'install', 'download']:
        if key in data and not (root / data[key]).exists():
            raise SystemExit(f'{mf}: missing {key} -> {data[key]}')
print('packs manifests ok')
PY
python3 - <<'PY'
from pathlib import Path
import yaml
root = Path('.')
data = yaml.safe_load((root / 'governance/site-route-map.yaml').read_text())
missing = [r['source'] for r in data.get('routes', []) if not (root / r['source']).exists()]
if missing:
    raise SystemExit('\n'.join(missing))
print('route map sources ok')
PY
```

## 发布后必查

- [ ] 本地工作区干净。
- [ ] 本地分支已 push 到远端对应分支。
- [ ] 如果独立站需要消费最新内容，已触发独立站构建或部署。
- [ ] 如果独立站部署使用 checked-in generated manifest，需要确认 manifest 已包含本次内容变更。

## 一句话规则

内容仓发布不是“能提交就行”，而是 docs、route-map、packs、README、governance 五层都指向同一套真实存在的公开内容。