#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
SCRIPT_DIR = Path(__file__).parent.resolve()

count = 0
for html_file in sorted(SCRIPT_DIR.glob('*.html')):
    content = html_file.read_text(encoding='utf-8')
    # 去掉 ?x-oss-process=image/... 参数
    new = re.sub(r'\?x-oss-process=image/[^\s"\'<>)]+', '', content)
    if new != content:
        html_file.write_text(new, encoding='utf-8')
        n = content.count('?x-oss-process') - new.count('?x-oss-process')
        print(f'[OK] {html_file.name} - 去掉 {n} 个参数')
        count += 1
    else:
        print(f'[--] {html_file.name} - 无变化')

print(f'\n完成！共修改 {count} 个文件')
