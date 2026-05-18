from pathlib import Path
import os, json, time, base64, hashlib, math
from openai import OpenAI
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_URL = os.getenv('IMAGE_GEN_BASE_URL') or 'https://cliproxy.biztint.com/v1'
MODEL = os.getenv('IMAGE_GEN_MODEL') or 'gemini-3.1-flash-image'
API_KEY = os.getenv('IMAGE_GEN_API_KEY') or os.getenv('CLIPROXY_API_KEY')
if not API_KEY:
    raise SystemExit('missing IMAGE_GEN_API_KEY/CLIPROXY_API_KEY')

REPO = Path('/opt/projects/awesome-hermes-agent-zh')
ASSET_DIR = REPO / 'docs' / 'assets'
PROOF_DIR = ASSET_DIR / 'proof' / 'cliproxy-approved-redo-20260518'
RAW_DIR = PROOF_DIR / 'raw'
PROVIDER_DIR = PROOF_DIR / 'provider'
FINAL_DIR = PROOF_DIR / 'final-previews'
for d in [RAW_DIR, PROVIDER_DIR, FINAL_DIR]:
    d.mkdir(parents=True, exist_ok=True)

FONT_REG = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
FONT_BOLD = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'

COMMON = (
    'Create a premium 16:9 technical documentation illustration for a Chinese AI tools website. '
    'Deep navy to blue-black background, cinematic but restrained cyan glow, translucent dark glass cards, '
    'white and cyan wireframe outlines, thin luminous connector lines, a few tiny orange signal nodes, '
    'strong hierarchy, large breathing room, elegant spacing, rich but clean composition, premium docs-diagram feeling. '
    'Absolutely no realistic UI, no dashboard, no browser window, no mobile app shell, no screenshot, no code editor, no terminal screen. '
    'No logos, no watermark, no readable text, no letters, no numbers. '
    'Design abstract composition only with obvious blank card zones for later overlay text. '
    'Cards should feel layered, slightly floating, semi-transparent, and refined rather than flat rectangles. '
    'Use 3 to 5 major structural groups only. Keep the image scannable in 3 seconds.'
)

ASSETS = [
    {
        'filename': 'solution-twitter-read-vs-actions-v2-cliproxy.png',
        'title': '读取能力 vs 写操作',
        'layout': 'compare_boundary',
        'prompt': COMMON + ' Topic: X/Twitter plugin capability boundary comparison. Left cluster = safer default read capability zone. Right cluster = higher-risk write action zone. Add a slim center boundary pillar between them. Keep left and right balanced, with subtle tension across the boundary.',
        'left_title': '默认可用',
        'left_items': ['搜索推文', '读取上下文', '趋势查看', '提及监控'],
        'center_badges': ['第三方插件'],
        'right_title': '显式启用',
        'right_items': ['发推', '回复', '点赞', '私信'],
        'footer': ['非官方内置', '账号身份执行'],
    },
    {
        'filename': 'solution-twitter-setup-chain-v2-cliproxy.png',
        'title': '最短启动链路',
        'layout': 'setup_flow',
        'prompt': COMMON + ' Topic: shortest setup chain for a third-party X/Twitter plugin in Hermes. Build one graceful left-to-right route of four main cards that ends in a fork of two outcomes. Composition should feel like a guided route, not a process chart screenshot.',
        'flow': ['安装插件', '配置 X API', '读取测试', '确认可用'],
        'branches': ['继续只读', '启用写操作'],
        'footer': ['先读后写'],
    },
    {
        'filename': 'solution-action-plan-standard-vs-lite-v2-cliproxy.png',
        'title': '标准版 vs 精简版',
        'layout': 'compare_weight',
        'prompt': COMMON + ' Topic: action-plan output mode comparison. Left side should feel fuller and more complete but still airy. Right side should feel lighter and faster. No business UI. Premium documentation-diagram look.',
        'left_title': '标准行动计划',
        'left_items': ['动作项', '负责人', '截止时间', '优先级', '依赖'],
        'right_title': '精简行动清单',
        'right_items': ['动作', '负责人', '截止时间'],
        'footer': ['完整下发', '快速发群'],
    },
    {
        'filename': 'solution-action-plan-output-map-v2-cliproxy.png',
        'title': '行动计划输出地图',
        'layout': 'pipeline_bundle',
        'prompt': COMMON + ' Topic: output bundle for an action-plan assistant. One source card expands into three structured mid-stage deliverables, then converges into one final send-ready card. The center should feel like a refined operations map.',
        'source': '目标摘要',
        'middle': ['动作计划表', '风险提醒', '执行顺序'],
        'final': '发送版正文',
        'footer': ['可直接同步'],
    },
    {
        'filename': 'solution-multiplatform-solo-vs-batch-v2-cliproxy.png',
        'title': '单平台 vs 多平台',
        'layout': 'compare_weight',
        'prompt': COMMON + ' Topic: single-platform rewrite versus batch multi-platform rewrite. Left = focused trial route. Right = one-source-to-many-destinations route. Right side should visibly imply branching outputs without looking like social media UI thumbnails.',
        'left_title': '先改一个平台',
        'left_items': ['试跑', '先看语气', '先看格式'],
        'right_title': '批量多平台',
        'right_items': ['小红书', '公众号', 'X/Twitter'],
        'footer': ['先验证', '一次拿齐'],
    },
    {
        'filename': 'solution-multiplatform-output-bundle-v2-cliproxy.png',
        'title': '多平台输出包',
        'layout': 'hub_spoke',
        'prompt': COMMON + ' Topic: multi-platform rewrite output bundle. One source content block, one central refinement hub, then three balanced destination cards. The image should feel centered, premium, and concise, with slim cyan routes to each destination.',
        'source': '原始内容',
        'center': '核心信息',
        'outputs': ['小红书版', '公众号版', 'X/Twitter 版'],
        'footer': ['复制就能发'],
    },
    {
        'filename': 'solution-message-summary-complete-vs-quick-v2-cliproxy.png',
        'title': '完整摘要 vs 快速摘要',
        'layout': 'compare_weight',
        'prompt': COMMON + ' Topic: complete summary versus quick summary for long messages and emails. Left side = richer structured coverage. Right side = compressed quick-forward summary. Avoid any chat-bubble look; this must feel like a structure comparison diagram.',
        'left_title': '完整摘要',
        'left_items': ['结论', '信息点', '待办', '时间点', '风险'],
        'right_title': '快速摘要',
        'right_items': ['一句话结论', '少量待办'],
        'footer': ['信息不丢', '适合转发'],
    },
    {
        'filename': 'solution-message-summary-output-map-v2-cliproxy.png',
        'title': '摘要输出地图',
        'layout': 'merge_split',
        'prompt': COMMON + ' Topic: summary output map for long emails and group messages. Two abstract source inputs merge into one structured summary card, then split into three summary chips and one final forwardable card. Elegant and abstract only.',
        'inputs': ['原始消息', '长邮件'],
        'center': '结构化摘要',
        'outputs': ['结论', '待办', '时间点'],
        'final': '转发版',
    },
]

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)


def rgba(hexstr, alpha=255):
    hexstr = hexstr.lstrip('#')
    return tuple(int(hexstr[i:i+2], 16) for i in (0, 2, 4)) + (alpha,)


def decode_payload(resp_dict):
    msg = resp_dict['choices'][0]['message']
    images = msg.get('images') or []
    for item in images:
        image_url = (((item or {}).get('image_url') or {}).get('url'))
        if image_url and image_url.startswith('data:image/'):
            header, b64 = image_url.split(',', 1)
            ext = header.split('/')[1].split(';')[0]
            return ext, base64.b64decode(b64)
    raise RuntimeError('No image payload found in cliproxy response')


def font(path, size):
    return ImageFont.truetype(path, size)


def fit_font(draw, text, max_width, path, start_size, min_size=16):
    for size in range(start_size, min_size - 1, -1):
        f = font(path, size)
        box = draw.textbbox((0, 0), text, font=f)
        if box[2] - box[0] <= max_width:
            return f
    return font(path, min_size)


def blur_glow(img, box, color, radius=22, expand=12, alpha=90):
    layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x1, y1, x2, y2 = box
    d.rounded_rectangle((x1 - expand, y1 - expand, x2 + expand, y2 + expand), radius=34, fill=color[:3] + (alpha,))
    layer = layer.filter(ImageFilter.GaussianBlur(radius))
    img.alpha_composite(layer)


def draw_panel(img, box, outline='#76E5FF', fill_alpha=142, glow_alpha=72, radius=28, inner=True):
    blur_glow(img, box, rgba(outline), radius=18, expand=8, alpha=glow_alpha)
    d = ImageDraw.Draw(img)
    fill = rgba('#091B32', fill_alpha)
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=rgba(outline, 230), width=2)
    if inner:
        x1, y1, x2, y2 = box
        d.rounded_rectangle((x1 + 10, y1 + 10, x2 - 10, y2 - 10), radius=max(12, radius - 8), outline=rgba('#B6F4FF', 48), width=1)


def text_center(draw, center, text, fnt, fill):
    bb = draw.textbbox((0, 0), text, font=fnt)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    draw.text((center[0] - w / 2, center[1] - h / 2), text, font=fnt, fill=fill)


def draw_chip(img, box, text, accent='cyan', title=False):
    outline = '#77E6FF' if accent == 'cyan' else '#FF9A57'
    fill_alpha = 136 if title else 118
    draw_panel(img, box, outline=outline, fill_alpha=fill_alpha, glow_alpha=58 if title else 38, radius=20 if title else 16, inner=False)
    d = ImageDraw.Draw(img)
    f = fit_font(d, text, box[2] - box[0] - 24, FONT_BOLD if title else FONT_REG, 28 if title else 22, 14)
    text_center(d, ((box[0] + box[2]) / 2, (box[1] + box[3]) / 2), text, f, rgba('#F3FBFF'))


def draw_card(img, box, title=None, items=None, accent='cyan'):
    outline = '#77E6FF' if accent == 'cyan' else '#FF9A57'
    draw_panel(img, box, outline=outline, fill_alpha=126, glow_alpha=66, radius=28, inner=True)
    d = ImageDraw.Draw(img)
    x1, y1, x2, y2 = box
    if title:
        tf = fit_font(d, title, x2 - x1 - 48, FONT_BOLD, 30, 18)
        text_center(d, ((x1 + x2) / 2, y1 + 34), title, tf, rgba('#F7FDFF'))
        d.line((x1 + 26, y1 + 62, x2 - 26, y1 + 62), fill=rgba('#89E9FF', 96), width=1)
    if items:
        y = y1 + 82
        available = (y2 - 22) - y
        rows = max(1, len(items))
        gap = 12
        chip_h = min(52, max(36, int((available - gap * (rows - 1)) / rows)))
        for item in items:
            chip = (x1 + 24, y, x2 - 24, y + chip_h)
            draw_chip(img, chip, item)
            y += chip_h + gap


def draw_title_band(img, title):
    box = (340, 40, 1260, 116)
    draw_panel(img, box, outline='#89EAFF', fill_alpha=158, glow_alpha=70, radius=26, inner=True)
    d = ImageDraw.Draw(img)
    f = fit_font(d, title, 820, FONT_BOLD, 42, 26)
    text_center(d, (800, 78), title, f, rgba('#F6FBFF'))


def draw_node(draw, x, y, color='#FF9A57', r=4):
    draw.ellipse((x - r, y - r, x + r, y + r), fill=rgba(color, 230))


def draw_line_glow(img, points, color='#7BE8FF', width=3, glow=8):
    base = Image.new('RGBA', img.size, (0, 0, 0, 0))
    bd = ImageDraw.Draw(base)
    bd.line(points, fill=rgba(color, 150), width=width + glow)
    base = base.filter(ImageFilter.GaussianBlur(5))
    img.alpha_composite(base)
    d = ImageDraw.Draw(img)
    d.line(points, fill=rgba(color, 228), width=width)


def draw_arrow(img, p1, p2, color='#7BE8FF', width=3):
    draw_line_glow(img, [p1, p2], color=color, width=width)
    d = ImageDraw.Draw(img)
    ang = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    ah = 10
    for delta in (2.55, -2.55):
        px = p2[0] - ah * math.cos(ang + delta)
        py = p2[1] - ah * math.sin(ang + delta)
        d.line((p2, (px, py)), fill=rgba(color, 228), width=width)


def apply_frame(base):
    img = base.resize((1600, 900), Image.Resampling.LANCZOS).convert('RGBA')
    vignette = Image.new('RGBA', img.size, (0, 0, 0, 0))
    vd = ImageDraw.Draw(vignette)
    vd.rectangle((0, 0, 1600, 900), fill=(4, 10, 22, 52))
    blur_glow(vignette, (26, 26, 1574, 874), rgba('#3DD8FF'), radius=26, expand=0, alpha=16)
    img = Image.alpha_composite(img, vignette)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((22, 22, 1578, 878), radius=30, outline=rgba('#64DFFF', 118), width=2)
    d.rounded_rectangle((40, 40, 1560, 860), radius=24, outline=rgba('#235994', 92), width=1)
    return img


def draw_footer_badges(img, labels, y=748):
    if not labels:
        return
    d = ImageDraw.Draw(img)
    widths = []
    for label in labels:
        f = fit_font(d, label, 220, FONT_BOLD, 22, 14)
        bb = d.textbbox((0, 0), label, font=f)
        widths.append(bb[2] - bb[0] + 40)
    total = sum(widths) + (len(widths) - 1) * 26
    x = (1600 - total) / 2
    for label, w in zip(labels, widths):
        draw_chip(img, (x, y, x + w, y + 48), label, accent='cyan', title=False)
        x += w + 26


def render_asset(defn, provider_path, final_path):
    img = apply_frame(Image.open(provider_path))
    draw_title_band(img, defn['title'])

    if defn['layout'] == 'compare_boundary':
        draw_card(img, (118, 176, 668, 688), defn['left_title'], defn['left_items'])
        draw_card(img, (932, 176, 1482, 688), defn['right_title'], defn['right_items'], accent='orange')
        draw_panel(img, (720, 252, 880, 612), outline='#FF9A57', fill_alpha=110, glow_alpha=52, radius=32, inner=True)
        yy = 378
        for badge in defn['center_badges']:
            draw_chip(img, (742, yy, 858, yy + 46), badge, accent='orange', title=False)
            yy += 60
        draw_arrow(img, (668, 430), (720, 430), color='#77E6FF', width=3)
        draw_arrow(img, (880, 430), (932, 430), color='#FF9A57', width=3)
        d = ImageDraw.Draw(img)
        for pt in [(694, 430), (906, 430)]:
            draw_node(d, pt[0], pt[1], color='#FF9A57', r=4)
        draw_footer_badges(img, defn.get('footer', []))

    elif defn['layout'] == 'compare_weight':
        draw_card(img, (118, 178, 724, 692), defn['left_title'], defn['left_items'])
        draw_card(img, (876, 216, 1482, 654), defn['right_title'], defn['right_items'])
        draw_arrow(img, (724, 420), (876, 420), color='#7BE8FF', width=3)
        d = ImageDraw.Draw(img)
        for pt in [(800, 420), (842, 420)]:
            draw_node(d, pt[0], pt[1], color='#FF9A57', r=4)
        draw_footer_badges(img, defn.get('footer', []))

    elif defn['layout'] == 'setup_flow':
        boxes = [(92, 324, 340, 452), (404, 260, 668, 388), (742, 324, 1006, 452), (1088, 260, 1352, 388)]
        for box, label in zip(boxes, defn['flow']):
            draw_card(img, box, label, None)
        draw_arrow(img, (340, 388), (404, 324))
        draw_arrow(img, (668, 324), (742, 388))
        draw_arrow(img, (1006, 388), (1088, 324))
        leftb = (1062, 548, 1308, 662)
        rightb = (1334, 548, 1518, 662)
        draw_card(img, leftb, defn['branches'][0], None)
        draw_card(img, rightb, defn['branches'][1], None, accent='orange')
        draw_arrow(img, (1220, 388), (1220, 512))
        draw_arrow(img, (1220, 512), (1185, 548))
        draw_arrow(img, (1220, 512), (1426, 548), color='#FF9A57')
        draw_footer_badges(img, defn.get('footer', []), y=736)

    elif defn['layout'] == 'pipeline_bundle':
        source = (92, 336, 340, 472)
        mids = [(496, 188, 792, 322), (496, 384, 792, 518), (496, 580, 792, 714)]
        final = (1070, 318, 1454, 490)
        draw_card(img, source, defn['source'], None)
        for box, label in zip(mids, defn['middle']):
            draw_card(img, box, label, None)
        draw_card(img, final, defn['final'], None, accent='orange')
        for target in [(496, 255), (496, 451), (496, 647)]:
            draw_arrow(img, (340, 404), target)
        for box in mids:
            draw_arrow(img, (box[2], (box[1] + box[3]) // 2), (1070, 404))
        draw_footer_badges(img, defn.get('footer', []), y=742)

    elif defn['layout'] == 'hub_spoke':
        source = (104, 338, 340, 474)
        center = (572, 302, 936, 510)
        outs = [(1164, 146, 1492, 282), (1164, 378, 1492, 514), (1164, 610, 1492, 746)]
        draw_card(img, source, defn['source'], None)
        draw_card(img, center, defn['center'], None)
        for box, label in zip(outs, defn['outputs']):
            draw_card(img, box, label, None)
        draw_arrow(img, (340, 406), (572, 406))
        for box in outs:
            draw_arrow(img, (936, 406), (1164, (box[1] + box[3]) // 2))
        draw_footer_badges(img, defn.get('footer', []), y=786)

    elif defn['layout'] == 'merge_split':
        in1 = (94, 214, 340, 340)
        in2 = (94, 554, 340, 680)
        center = (512, 304, 878, 590)
        outs = [(1060, 180, 1320, 304), (1060, 386, 1320, 510), (1060, 592, 1320, 716)]
        final = (1364, 304, 1520, 590)
        draw_card(img, in1, defn['inputs'][0], None)
        draw_card(img, in2, defn['inputs'][1], None)
        draw_card(img, center, defn['center'], None)
        for box, label in zip(outs, defn['outputs']):
            draw_card(img, box, label, None)
        draw_card(img, final, defn['final'], None, accent='orange')
        draw_arrow(img, (340, 276), (512, 396))
        draw_arrow(img, (340, 616), (512, 500))
        for box in outs:
            draw_arrow(img, (878, 446), (1060, (box[1] + box[3]) // 2))
        draw_arrow(img, (1320, 446), (1364, 446), color='#FF9A57')

    d = ImageDraw.Draw(img)
    for pt in [(122, 136), (1482, 158), (1412, 786), (188, 758), (802, 162), (936, 744)]:
        draw_node(d, pt[0], pt[1], color='#FF9A57', r=4)

    img = img.filter(ImageFilter.SHARPEN)
    img.convert('RGB').save(final_path, 'PNG', optimize=True)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


proof = {
    'generated_at': time.strftime('%Y-%m-%d %H:%M:%S %Z'),
    'base_url': BASE_URL,
    'model': MODEL,
    'assets': []
}

for idx, defn in enumerate(ASSETS, start=1):
    resp = client.chat.completions.create(model=MODEL, messages=[{'role': 'user', 'content': defn['prompt']}])
    data = resp.model_dump()
    raw_path = RAW_DIR / f"{idx:02d}-{defn['filename'].replace('.png', '.json')}"
    raw_path.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    ext, img_bytes = decode_payload(data)
    provider_path = PROVIDER_DIR / f"{idx:02d}-{defn['filename'].replace('.png', '')}-provider.{ext}"
    provider_path.write_bytes(img_bytes)
    final_path = ASSET_DIR / defn['filename']
    render_asset(defn, provider_path, final_path)
    preview_path = FINAL_DIR / defn['filename']
    Image.open(final_path).save(preview_path)
    proof['assets'].append({
        'filename': defn['filename'],
        'final_path': str(final_path),
        'provider_path': str(provider_path),
        'raw_response_path': str(raw_path),
        'sha256': sha256(final_path),
        'provider_sha256': sha256(provider_path),
        'prompt': defn['prompt'],
    })
    print('generated', defn['filename'])

proof_path = PROOF_DIR / 'generation-proof.json'
proof_path.write_text(json.dumps(proof, ensure_ascii=False, indent=2))
print('proof', proof_path)
