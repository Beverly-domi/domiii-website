#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
SCRIPT_DIR = Path(__file__).parent.resolve()

count = 0
for f in sorted(SCRIPT_DIR.glob('*.html')):
    content = f.read_text(encoding='utf-8')
    # 找到裸奔的 transition JS（不在 script 标签里的）
    old = '// Page transition fade-out\n(function(){var t;document.addEventListener'
    new = '<script>// Page transition fade-out\n(function(){var t;document.addEventListener'
    if old in content and '<script>// Page transition fade-out' not in content:
        content = content.replace(old, new)
        # 确保它在 </script> 之前闭合
        content = content.replace("},230)})})();\n", "},230)})})();</script>\n")
        f.write_text(content, encoding='utf-8')
        print(f'[FIX] {f.name}')
        count += 1
    else:
        print(f'[SKIP] {f.name} - already fixed or not found')

print(f'\nDone! {count} files fixed.')
