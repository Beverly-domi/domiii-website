#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
SCRIPT_DIR = Path(__file__).parent.resolve()

count = 0
for f in sorted(SCRIPT_DIR.glob('*.html')):
    content = f.read_text(encoding='utf-8')
    # 去掉 page transition 的 JS 代码块
    new = re.sub(
        r"// Page transition fade-out\s*\(function\(\).*?\{\s*window\.location\.href=h\},230\}\)\)\(\)\(\)\s*",
        '',
        content,
        flags=re.DOTALL
    )
    # 也去掉 pgIn CSS
    new = re.sub(
        r"/\* page fade in/out \*/body\{animation:pgIn\.35s ease\}@keyframes pgIn\{from\{opacity:0;transform:translateY\(10px\)\}to\{opacity:1;transform:translateY\(0\)\}\}",
        '',
        new
    )
    if new != content:
        f.write_text(new, encoding='utf-8')
        print(f'[RM] {f.name}')
        count += 1
    else:
        print(f'[--] {f.name}')

print(f'\nDone! {count} files cleaned.')
