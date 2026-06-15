#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Fix childhood.html
c = Path('childhood.html').read_text(encoding='utf-8')
c = c.replace(
    'src: CHILDHOOD_BASE + `童年${i}.jpg\n        caption: `',
    'src: CHILDHOOD_BASE + `童年${i}.jpg`,\n        caption: `'
)
Path('childhood.html').write_text(c, encoding='utf-8')
print('[FIX] childhood.html')

# Fix shiny.html
c = Path('shiny.html').read_text(encoding='utf-8')
c = c.replace(
    'src: `https://domiii.oss-cn-hangzhou.aliyuncs.com/shiny/shiny${id}.jpg\n        cap: `',
    'src: `https://domiii.oss-cn-hangzhou.aliyuncs.com/shiny/shiny${id}.jpg`,\n        cap: `'
)
Path('shiny.html').write_text(c, encoding='utf-8')
print('[FIX] shiny.html')

# Also check other files for similar issues 
for f in sorted(Path('.').glob('*.html')):
    c = f.read_text(encoding='utf-8')
    # Look for template literals with .jpg that might be missing closing backtick
    import re
    # Find patterns like: `...${...}.jpg\n that don't have closing backtick
    matches = re.findall(r'`[^`]*\$\{[^}]+\}\.jpg\n', c)
    if matches:
        print(f'[WARN] {f.name} might have issues: {matches}')
