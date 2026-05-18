from pathlib import Path
from PIL import Image
import hashlib, json

REPO = Path('/opt/projects/awesome-hermes-agent-zh')
ASSET_DIR = REPO / 'docs' / 'assets'
PROOF_DIR = ASSET_DIR / 'proof' / 'cliproxy-approved-redo-20260518'
assets = [
'solution-twitter-read-vs-actions-v2-cliproxy.png',
'solution-twitter-setup-chain-v2-cliproxy.png',
'solution-action-plan-standard-vs-lite-v2-cliproxy.png',
'solution-action-plan-output-map-v2-cliproxy.png',
'solution-multiplatform-solo-vs-batch-v2-cliproxy.png',
'solution-multiplatform-output-bundle-v2-cliproxy.png',
'solution-message-summary-complete-vs-quick-v2-cliproxy.png',
'solution-message-summary-output-map-v2-cliproxy.png',
]
report = []
for name in assets:
    p = ASSET_DIR / name
    im = Image.open(p).convert('RGB')
    w, h = im.size
    pix = im.load()
    samples = {
        'tl': pix[10,10], 'tr': pix[w-11,10], 'bl': pix[10,h-11], 'br': pix[w-11,h-11], 'c': pix[w//2,h//2]
    }
    report.append({
        'file': name,
        'size': [w,h],
        'format': Image.open(p).format,
        'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
        'bytes': p.stat().st_size,
        'corner_samples': samples,
        'is_16_9': abs((w/h) - (16/9)) < 0.02,
    })
(PROOF_DIR / 'qc-mechanical.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
print(json.dumps(report, ensure_ascii=False, indent=2))
