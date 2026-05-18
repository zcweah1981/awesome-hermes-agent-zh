from pathlib import Path
import os, json, time, base64, textwrap, hashlib
from io import BytesIO
from openai import OpenAI
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_URL = os.getenv('IMAGE_GEN_BASE_URL') or 'https://cliproxy.biztint.com/v1'
MODEL = os.getenv('IMAGE_GEN_MODEL') or 'gemini-3.1-flash-image'
API_KEY = os.getenv('IMAGE_GEN_API_KEY') or os.getenv('CLIPROXY_API_KEY')
if not API_KEY:
    raise SystemExit('missing IMAGE_GEN_API_KEY/CLIPROXY_API_KEY')

REPO = Path('/opt/projects/awesome-hermes-agent-zh')
ASSET_DIR = REPO / 'docs' / 'assets'
PROOF_DIR = REPO / 'docs' / 'assets' / 'proof' / 'cliproxy-batch2-20260518'
RAW_DIR = PROOF_DIR / 'raw'
PROVIDER_DIR = PROOF_DIR / 'provider'
FINAL_DIR = PROOF_DIR / 'final-previews'
for d in [RAW_DIR, PROVIDER_DIR, FINAL_DIR]:
    d.mkdir(parents=True, exist_ok=True)

FONT_REG = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
FONT_BOLD = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'
TITLE_FONT = ImageFont.truetype(FONT_BOLD, 42)
GROUP_FONT = ImageFont.truetype(FONT_BOLD, 28)
LABEL_FONT = ImageFont.truetype(FONT_REG, 24)
BADGE_FONT = ImageFont.truetype(FONT_BOLD, 22)
SMALL_FONT = ImageFont.truetype(FONT_REG, 18)

COMMON = (
    'Create a clean 16:9 technical documentation illustration for a Chinese AI tools website. '
    'Dark deep navy-black background, subtle cyan and blue glow, white/cyan/blue wireframe cards, '
    'thin connector lines, minimal geometric icons, strong spacing, generous negative space, '
    'sharp hierarchy, no readable text, no letters, no words, no numbers, no screenshot, no fake UI, '
    'no browser window, no chat app mockup, not hand-drawn, not watercolor, not poster art. '
    'The composition should look like a premium docs diagram for software workflows. '
    'Use clear card grouping, 3-5 main blocks, directional arrows, cyan edge glow, occasional tiny orange accent nodes. '
    'Leave enough clean empty space inside cards and title bands for later text overlay.'
)

ASSETS = [
    {
        'filename': 'solution-twitter-read-vs-actions-v2-cliproxy.png',
        'title': '读取能力 vs 写操作',
        'layout': 'two_col',
        'prompt': COMMON + ' Diagram topic: X/Twitter plugin capability boundary comparison. Build a balanced two-column composition. Left column is safe read-only capability cards available by default. Center is a narrow boundary card. Right column is higher-risk write actions that require explicit enablement. Strong separation between left and right. No text rendered by model.',
        'left_title': '默认可用',
        'left_items': ['搜索推文', '读取上下文', '趋势查看', '提及监控'],
        'right_title': '显式启用',
        'right_items': ['发推', '回复', '点赞', '私信'],
        'center_badges': ['第三方插件'],
        'bottom_badges': ['非官方内置', '账号身份执行'],
    },
    {
        'filename': 'solution-twitter-setup-chain-v2-cliproxy.png',
        'title': '最短启动链路',
        'layout': 'flow_branch',
        'prompt': COMMON + ' Diagram topic: shortest setup chain for a third-party X/Twitter plugin inside Hermes. Build a left-to-right workflow with four main cards and one final fork to two branches. Clean central line, clear branch split, no text rendered by model.',
        'flow': ['安装插件', '配置 X API', '读取测试', '确认可用'],
        'branches': ['继续只读', '启用写操作'],
        'bottom_badges': ['先读后写'],
    },
    {
        'filename': 'solution-action-plan-standard-vs-lite-v2-cliproxy.png',
        'title': '标准版 vs 精简版',
        'layout': 'two_col',
        'prompt': COMMON + ' Diagram topic: action-plan output mode comparison. Build a balanced two-column comparison. Left side should feel fuller with richer field chips. Right side is simpler and faster for group sync. No text rendered by model.',
        'left_title': '标准行动计划',
        'left_items': ['动作项', '负责人', '截止时间', '优先级', '依赖'],
        'right_title': '精简行动清单',
        'right_items': ['动作', '负责人', '截止时间'],
        'bottom_badges': ['完整下发', '快速发群'],
    },
    {
        'filename': 'solution-action-plan-output-map-v2-cliproxy.png',
        'title': '行动计划输出地图',
        'layout': 'pipeline',
        'prompt': COMMON + ' Diagram topic: output map for an action-plan assistant. Build a center pipeline from one entry card into three parallel middle cards and one final delivery card. Premium software docs diagram, no text rendered by model.',
        'source': '目标摘要',
        'middle': ['动作计划表', '风险提醒', '执行顺序'],
        'final': '发送版正文',
        'bottom_badges': ['可直接同步'],
    },
    {
        'filename': 'solution-multiplatform-solo-vs-batch-v2-cliproxy.png',
        'title': '单平台 vs 多平台',
        'layout': 'two_col',
        'prompt': COMMON + ' Diagram topic: single-platform rewrite vs batch multi-platform rewrite. Two-column comparison. Left side feels like focused trial route. Right side feels like one source branching to multiple publishing destinations. No text rendered by model.',
        'left_title': '先改一个平台',
        'left_items': ['试跑', '先看语气', '先看格式'],
        'right_title': '批量多平台',
        'right_items': ['小红书', '公众号', 'X/Twitter'],
        'bottom_badges': ['先验证', '一次拿齐'],
    },
    {
        'filename': 'solution-multiplatform-output-bundle-v2-cliproxy.png',
        'title': '多平台输出包',
        'layout': 'hub_spoke',
        'prompt': COMMON + ' Diagram topic: multi-platform rewrite output bundle. Build a hub-and-spoke structure. One source content card flows into a central refinement card, then branches into three equal destination cards. No text rendered by model.',
        'source': '原始内容',
        'center': '核心信息',
        'outputs': ['小红书版', '公众号版', 'X/Twitter 版'],
        'bottom_badges': ['复制就能发'],
    },
    {
        'filename': 'solution-message-summary-complete-vs-quick-v2-cliproxy.png',
        'title': '完整摘要 vs 快速摘要',
        'layout': 'two_col',
        'prompt': COMMON + ' Diagram topic: complete summary vs quick summary for long messages and emails. Two-column comparison. Left side shows fuller structured summary. Right side shows compressed quick-forward version. No text rendered by model.',
        'left_title': '完整摘要',
        'left_items': ['结论', '信息点', '待办', '时间点', '风险'],
        'right_title': '快速摘要',
        'right_items': ['一句话结论', '少量待办'],
        'bottom_badges': ['信息不丢', '适合转发'],
    },
    {
        'filename': 'solution-message-summary-output-map-v2-cliproxy.png',
        'title': '摘要输出地图',
        'layout': 'merge_then_split',
        'prompt': COMMON + ' Diagram topic: summary output map for emails and group messages. Build a left-to-right flow with two input cards merging into one structured summary card, then branching into three result chips and one final forwardable card. No text rendered by model.',
        'inputs': ['原始消息', '长邮件'],
        'center': '结构化摘要',
        'outputs': ['结论', '待办', '时间点'],
        'final': '转发版',
    },
]

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def decode_payload(resp_dict):
    msg = resp_dict['choices'][0]['message']
    images = msg.get('images') or []
    for item in images:
        image_url = (((item or {}).get('image_url') or {}).get('url'))
        if image_url:
            if image_url.startswith('data:image/'):
                header, b64 = image_url.split(',', 1)
                ext = header.split('/')[1].split(';')[0]
                return ext, base64.b64decode(b64)
            raise RuntimeError('non-data-url payload not supported')
    raise RuntimeError('No image payload found')


def round_rect(draw, box, fill, outline, width=2, radius=22):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text_center(draw, xy, text, font, fill):
    bbox = draw.textbbox((0,0), text, font=font)
    w = bbox[2]-bbox[0]; h = bbox[3]-bbox[1]
    draw.text((xy[0]-w/2, xy[1]-h/2), text, font=font, fill=fill)


def fit_font(draw, text, max_width, base_font_path, start_size, min_size=16, bold=False):
    path = FONT_BOLD if bold else base_font_path
    for size in range(start_size, min_size-1, -1):
        f = ImageFont.truetype(path, size)
        bbox = draw.textbbox((0,0), text, font=f)
        if bbox[2]-bbox[0] <= max_width:
            return f
    return ImageFont.truetype(path, min_size)


def draw_badge(draw, x, y, text, fill=(10,35,62,220), outline=(77,211,255,220)):
    font = fit_font(draw, text, 200, FONT_REG, 22, 16, bold=True)
    bbox = draw.textbbox((0,0), text, font=font)
    w = bbox[2]-bbox[0] + 34
    h = bbox[3]-bbox[1] + 18
    box = (x, y, x+w, y+h)
    round_rect(draw, box, fill, outline, width=2, radius=18)
    text_center(draw, ((box[0]+box[2])/2, (box[1]+box[3])/2), text, font, (240,250,255,255))
    return w, h


def overlay_common(base):
    base = base.resize((1600, 900), Image.Resampling.LANCZOS).convert('RGBA')
    overlay = Image.new('RGBA', base.size, (0,0,0,0))
    d = ImageDraw.Draw(overlay)
    # darken base slightly for consistency
    d.rectangle((0,0,1600,900), fill=(3,10,22,58))
    # outer frame
    d.rounded_rectangle((24,24,1576,876), radius=28, outline=(61,176,255,110), width=2)
    d.rounded_rectangle((42,42,1558,858), radius=24, outline=(22,88,166,80), width=1)
    return Image.alpha_composite(base, overlay)


def draw_title(img, title):
    d = ImageDraw.Draw(img)
    round_rect(d, (300,42,1300,116), fill=(7,25,48,210), outline=(109,220,255,210), width=2, radius=24)
    font = fit_font(d, title, 920, FONT_BOLD, 42, 28, bold=True)
    text_center(d, (800,79), title, font, (248,251,255,255))


def draw_card(draw, box, title=None, items=None, accent='cyan'):
    fill=(8,22,43,192)
    outline=(91,222,255,220) if accent=='cyan' else (255,160,84,220)
    round_rect(draw, box, fill=fill, outline=outline, width=2, radius=26)
    x1,y1,x2,y2 = box
    if title:
        title_font = fit_font(draw, title, x2-x1-40, FONT_BOLD, 30, 18, bold=True)
        text_center(draw, ((x1+x2)/2, y1+34), title, title_font, (250,252,255,255))
        draw.line((x1+24,y1+60,x2-24,y1+60), fill=(83,187,255,120), width=1)
    if items:
        y = y1+84
        max_rows = len(items)
        avail = (y2-22)-y
        chip_h = min(50, max(34, avail // max_rows - 4))
        for item in items:
            chip_box=(x1+24, y, x2-24, y+chip_h)
            round_rect(draw, chip_box, fill=(12,36,66,165), outline=(97,203,255,120), width=1, radius=15)
            font = fit_font(draw, item, x2-x1-80, FONT_REG, 24, 14)
            text_center(draw, ((chip_box[0]+chip_box[2])/2, (chip_box[1]+chip_box[3])/2), item, font, (236,246,255,255))
            y += chip_h + 10


def draw_arrow(draw, p1, p2, fill=(93,216,255,220), width=5):
    draw.line((p1,p2), fill=fill, width=width)
    import math
    ang = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    ah = 16
    for delta in (2.6, -2.6):
        px = p2[0] - ah*math.cos(ang+delta)
        py = p2[1] - ah*math.sin(ang+delta)
        draw.line((p2, (px,py)), fill=fill, width=width)


def render_asset(defn, provider_path, final_path):
    base = Image.open(provider_path).convert('RGBA')
    img = overlay_common(base)
    d = ImageDraw.Draw(img)
    draw_title(img, defn['title'])

    if defn['layout'] == 'two_col':
        left=(130,180,690,690)
        right=(910,180,1470,690)
        center=(730,280,870,590)
        draw_card(d, left, defn['left_title'], defn['left_items'])
        draw_card(d, right, defn['right_title'], defn['right_items'])
        if defn.get('center_badges'):
            round_rect(d, center, fill=(13,26,45,188), outline=(255,163,87,220), width=2, radius=26)
            yy=355
            for badge in defn['center_badges']:
                ww,hh=draw_badge(d, 760-(90), yy, badge, fill=(42,30,16,210), outline=(255,165,96,220))
                yy += hh + 18
        if defn.get('bottom_badges'):
            x=520
            for i,b in enumerate(defn['bottom_badges']):
                w,h=draw_badge(d, x, 742, b)
                x += w + 28
        draw_arrow(d, (690,435), (730,435))
        draw_arrow(d, (870,435), (910,435), fill=(255,168,92,220))

    elif defn['layout'] == 'flow_branch':
        xs=[110,430,750,1070]
        boxes=[]
        for i,label in enumerate(defn['flow']):
            box=(xs[i],300,xs[i]+240,430)
            boxes.append(box)
            draw_card(d, box, label, None)
            if i>0:
                draw_arrow(d, (boxes[i-1][2],365), (box[0],365))
        b1=(1120,565,1350,680); b2=(1360,565,1490,680)
        draw_card(d, b1, defn['branches'][0], None)
        draw_card(d, b2, defn['branches'][1], None, accent='orange')
        draw_arrow(d, (1190,430), (1190,520))
        draw_arrow(d, (1190,520), (1235,565))
        draw_arrow(d, (1190,520), (1425,565), fill=(255,168,92,220))
        x=680
        for b in defn.get('bottom_badges',[]):
            w,h=draw_badge(d, x, 740, b)
            x += w + 26

    elif defn['layout'] == 'pipeline':
        s=(120,330,360,470); draw_card(d,s,defn['source'],None)
        mids=[(490,240,770,370),(490,405,770,535),(490,570,770,700)]
        for box,label in zip(mids, defn['middle']): draw_card(d,box,label,None)
        f=(1090,330,1420,500); draw_card(d,f,defn['final'],None, accent='orange')
        draw_arrow(d, (360,400), (490,305))
        draw_arrow(d, (360,400), (490,470))
        draw_arrow(d, (360,400), (490,635))
        for box in mids:
            draw_arrow(d, (box[2], (box[1]+box[3])//2), (1090,415))
        x=690
        for b in defn.get('bottom_badges',[]):
            w,h=draw_badge(d, x, 744, b)
            x += w + 26

    elif defn['layout'] == 'hub_spoke':
        s=(110,340,350,500); draw_card(d,s,defn['source'],None)
        c=(590,320,910,520); draw_card(d,c,defn['center'],None)
        outs=[(1120,160,1470,300),(1120,355,1470,495),(1120,550,1470,690)]
        for box,label in zip(outs,defn['outputs']): draw_card(d,box,label,None)
        draw_arrow(d, (350,420), (590,420))
        for box in outs: draw_arrow(d, (910,420), (1120,(box[1]+box[3])//2))
        x=690
        for b in defn.get('bottom_badges',[]):
            w,h=draw_badge(d, x, 742, b)
            x += w + 26

    elif defn['layout'] == 'merge_then_split':
        in1=(100,250,360,390); in2=(100,500,360,640)
        center=(540,335,880,555)
        out1=(1080,210,1320,330); out2=(1080,390,1320,510); out3=(1080,570,1320,690)
        final=(1350,335,1520,555)
        draw_card(d,in1,defn['inputs'][0],None)
        draw_card(d,in2,defn['inputs'][1],None)
        draw_card(d,center,defn['center'],None)
        for box,label in zip([out1,out2,out3], defn['outputs']): draw_card(d,box,label,None)
        draw_card(d,final,defn['final'],None, accent='orange')
        draw_arrow(d,(360,320),(540,410)); draw_arrow(d,(360,570),(540,480))
        for box in [out1,out2,out3]: draw_arrow(d,(880,445),(1080,(box[1]+box[3])//2))
        draw_arrow(d,(1320,450),(1350,445), fill=(255,168,92,220))

    # accent dots
    for pt in [(130,130),(1470,160),(1400,760),(180,740),(800,180)]:
        d.ellipse((pt[0]-4, pt[1]-4, pt[0]+4, pt[1]+4), fill=(255,154,68,220))

    img = img.filter(ImageFilter.SHARPEN)
    img.convert('RGB').save(final_path, 'PNG', optimize=True)

proof = {
    'generated_at': time.strftime('%Y-%m-%d %H:%M:%S %Z'),
    'base_url': BASE_URL,
    'model': MODEL,
    'assets': []
}

for idx,defn in enumerate(ASSETS, start=1):
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{'role':'user','content':defn['prompt']}],
    )
    data = resp.model_dump()
    raw_path = RAW_DIR / f"{idx:02d}-{defn['filename'].replace('.png','.json')}"
    raw_path.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    ext, img_bytes = decode_payload(data)
    provider_path = PROVIDER_DIR / f"{idx:02d}-{defn['filename'].replace('.png','')}-provider.{ext}"
    provider_path.write_bytes(img_bytes)
    final_path = ASSET_DIR / defn['filename']
    render_asset(defn, provider_path, final_path)
    preview_path = FINAL_DIR / defn['filename']
    Image.open(final_path).save(preview_path)
    sha = hashlib.sha256(final_path.read_bytes()).hexdigest()
    provider_sha = hashlib.sha256(provider_path.read_bytes()).hexdigest()
    proof['assets'].append({
        'filename': defn['filename'],
        'final_path': str(final_path),
        'provider_path': str(provider_path),
        'raw_response_path': str(raw_path),
        'sha256': sha,
        'provider_sha256': provider_sha,
        'prompt': defn['prompt']
    })
    print('generated', defn['filename'])

proof_path = PROOF_DIR / 'generation-proof.json'
proof_path.write_text(json.dumps(proof, ensure_ascii=False, indent=2))
print('proof', proof_path)
