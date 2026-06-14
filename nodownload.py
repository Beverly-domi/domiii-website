#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
SCRIPT_DIR = Path(__file__).parent.resolve()

# 给所有 img 加 draggable="false"
RE_IMG = re.compile(r'<img\s', re.IGNORECASE)

# 给页面添加禁止下载的 CSS 和 JS
PROTECT_CSS = '''
/* 禁止图片下载拖拽 */
img{-webkit-user-drag:none;user-select:none;-webkit-touch-callout:none}
'''
PROTECT_JS = '''
// 禁止右键下载图片
document.addEventListener('contextmenu',function(e){if(e.target.tagName==='IMG'){e.preventDefault()}});
'''

count = 0
for f in sorted(SCRIPT_DIR.glob('*.html')):
    content = f.read_text(encoding='utf-8')
    
    # 跳过已经加了防护的
    if '-webkit-user-drag:none' in content:
        print(f'[SKIP] {f.name} - already protected')
        continue
    
    # 1. 给所有 img 标签加 draggable="false"
    def add_draggable(m):
        return '<img draggable="false" '
    content = RE_IMG.sub(add_draggable, content)
    
    # 2. 加 CSS 防护（插在 </style> 前）
    if '</style>' in content:
        idx = content.rfind('</style>')
        content = content[:idx] + PROTECT_CSS + content[idx:]
    
    # 3. 加 JS 防右键（插在 </body> 前）
    if '</body>' in content:
        content = content.replace('</body>', '<script>' + PROTECT_JS + '</script>\n</body>')
    
    f.write_text(content, encoding='utf-8')
    print(f'[ADD] {f.name}')
    count += 1

print(f'\nDone! {count} files updated.')
