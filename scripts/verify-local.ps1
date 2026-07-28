param([switch]$SkipInstall)

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Push-Location $repoRoot
try {
    $before = (& git status --porcelain=v1) -join "`n"
    if (-not $SkipInstall) {
        & python -m pip install -r requirements-ci.txt
        if ($LASTEXITCODE -ne 0) { throw "依赖安装失败。" }
    }
    & python -m pytest -q
    if ($LASTEXITCODE -ne 0) { throw "pytest 失败。" }
    & python scripts/normalize_route_order.py
    if ($LASTEXITCODE -ne 0) { throw "route order 校验失败。" }
    & python scripts/content_quality_check.py
    if ($LASTEXITCODE -ne 0) { throw "内容质量校验失败。" }
    & python scripts/check_repository_hygiene.py
    if ($LASTEXITCODE -ne 0) { throw "仓库体积门禁失败。" }
    $after = (& git status --porcelain=v1) -join "`n"
    if ($after -ne $before) {
        throw "验证后工作区不干净；请检查是否存在未提交的规范化结果。"
    }
    Write-Host "内容仓本地发布验证通过。"
}
finally {
    Pop-Location
}
