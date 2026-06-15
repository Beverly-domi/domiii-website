#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for fname in ['massage.html', 'quote.html']:
    c = open(fname, 'r', encoding='utf-8').read()
    # Find the copyright footer by locating the unique text
    marker = '资源来自网络，如有侵权，请联系删除'
    if marker in c:
        # Find the opening div before this text
        idx = c.find(marker)
        # Go backwards to find the starting <div
        div_start = c.rfind('<div style=', 0, idx)
        if div_start == -1:
            div_start = c.rfind('<div', 0, idx)
        # Go forward to find the closing </div>
        div_end = c.find('</div>', idx) + 6
        # Include trailing whitespace
        while div_end < len(c) and c[div_end] in ' \n\r\t':
            div_end += 1
        c = c[:div_start] + c[div_end:]
        open(fname, 'w', encoding='utf-8').write(c)
        print(f'{fname}: footer removed')
    else:
        print(f'{fname}: no footer found')
