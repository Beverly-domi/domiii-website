#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""给所有 OSS 图片 URL 添加阿里云图片处理参数，加速页面加载"""

import re
import sys
import io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

SCRIPT_DIR = Path(__file__).parent.resolve()

# ==================== 压缩规则 ====================
# 不同类型的图片使用不同尺寸，保证清晰度的同时大幅缩小体积
RULES = {
    'beijing':    ('w_1200', 'q_85'),  # 首页背景大图，需要高清
    'xiaotu':     ('w_400',  'q_80'),  # 拍立得小图，400px够用
    'pig':        ('w_300',  'q_80'),  # 小猪图标，很小
    '桃心猪':     ('w_300',  'q_80'),  # 小猪图标
    'touxiang':   ('w_400',  'q_80'),  # 头像
    'kafei':      ('w_400',  'q_80'),  # 咖啡头像
    '/card/':     ('w_600',  'q_85'),  # 卡牌图，需要清晰
    '/childhood/': ('w_800', 'q_80'),  # 童年相册
    '/game/':     ('w_800',  'q_80'),  # 游戏照片
    '/shiny/':    ('w_800',  'q_80'),  # 闪耀照片
    '/weibo/':    ('w_800',  'q_80'),  # 微博照片
}

DEFAULT_RULE = ('w_600', 'q_80')

def get_params(url_path):
    """根据图片路径返回 OSS 处理参数"""
    for pattern, (w, q) in RULES.items():
        if pattern in url_path:
            return f"?x-oss-process=image/resize,{w}/quality,{q}"
    w, q = DEFAULT_RULE
    return f"?x-oss-process=image/resize,{w}/quality,{q}"

def process_html(filepath):
    """处理单个 HTML 文件"""
    content = filepath.read_text(encoding='utf-8')
    original = content

    # 1. 替换静态 HTML 中的 OSS 图片 URL（.jpg .jpeg .png .webp）
    #    匹配 https://domiii.oss-cn-hangzhou.aliyuncs.com/xxx.jpg 格式
    def replace_static(match):
        url = match.group(0)
        if '?x-oss-process=' in url:
            return url  # 已有参数，跳过
        # 提取文件路径部分用于判断规则
        return url + get_params(url)

    # 匹配完整 OSS URL（不含已在末尾的情况）
    content = re.sub(
        r'https://domiii\.oss-cn-hangzhou\.aliyuncs\.com/[^\s"\'<>)]+\.(?:jpg|jpeg|png|webp)(?![?])',
        replace_static,
        content,
        flags=re.IGNORECASE
    )

    # 2. 特殊处理：Game 页面的动态 JS URL
    #    const PHOTOS = Array.from({length:66}, (_,i) => '...game/game'+(i+1)+'.jpg');
    if "game/game'+(i+1)" in content:
        content = content.replace(
            "game/game'+(i+1)+'.jpg'",
            "game/game'+(i+1)+'.jpg?x-oss-process=image/resize,w_800/quality,q_80'"
        )
        print(f"  [OK] game.html dynamic URL processed")

    # 3. 特殊处理：Shiny 页面的模板字符串
    #    src: `.../shiny/shiny${id}.jpg`,
    if 'shiny${id}.jpg`' in content:
        content = content.replace(
            'shiny${id}.jpg`',
            'shiny${id}.jpg?x-oss-process=image/resize,w_800/quality,q_80`'
        )
        print(f"  [OK] shiny.html dynamic URL processed")

    # 4. 特殊处理：Childhood 页面的模板字符串
    #    src: CHILDHOOD_BASE + `童年${i}.jpg`,
    if '童年${i}.jpg`' in content:
        content = content.replace(
            '童年${i}.jpg`',
            '童年${i}.jpg?x-oss-process=image/resize,w_800/quality,q_80`'
        )
        print(f"  [OK] childhood.html dynamic URL processed")

    # 5. 特殊处理：Weibo 页面 - 只对 .jpg 添加参数，.mp4 不加
    #    WEIBO_BASE + f  =>  需要改成 WEIBO_BASE + f + (f.endsWith('.mp4') ? '' : PARAM)
    if 'WEIBO_BASE' in content and 'weibo' in filepath.name:
        # 添加压缩参数常量
        old_weibo_line = 'const WEIBO_BASE = "https://domiii.oss-cn-hangzhou.aliyuncs.com/weibo/";'
        new_weibo_line = 'const WEIBO_BASE = "https://domiii.oss-cn-hangzhou.aliyuncs.com/weibo/";\nconst WEIBO_THUMB = "?x-oss-process=image/resize,w_800/quality,q_80";'
        content = content.replace(old_weibo_line, new_weibo_line)
        # 替换所有 .map(f => ({ img: WEIBO_BASE + f  为  WEIBO_BASE + f + (f.endsWith('.mp4') ? '' : WEIBO_THUMB)
        content = content.replace(
            'WEIBO_BASE + f,',
            'WEIBO_BASE + f + (f.endsWith(".mp4") ? "" : WEIBO_THUMB),'
        )
        print(f"  [OK] weibo.html dynamic URL processed")

    if content != original:
        filepath.write_text(content, encoding='utf-8')
        count = len(re.findall(r'x-oss-process', content))
        print(f"[EDIT] {filepath.name} - {count} params added")
        return True
    else:
        print(f"[SKIP] {filepath.name} - no changes needed")
        return False

# ==================== 主程序 ====================
print("=" * 60)
print("OSS 图片压缩参数添加脚本")
print("=" * 60)
print()

total = 0
for html_file in sorted(SCRIPT_DIR.glob('*.html')):
    if process_html(html_file):
        total += 1

print()
print("=" * 60)
print(f"完成！共修改 {total} 个文件")
print()
print("压缩规则：")
print("  🖼️  背景/大图 → 1200px, 质量85%")
print("  📸 相册照片   → 800px, 质量80%")
print("  🃏 卡牌图片   → 600px, 质量85%")
print("  🔲 小图标/头像 → 300-400px, 质量80%")