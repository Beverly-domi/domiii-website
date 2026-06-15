#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for fname in ['massage.html', 'quote.html']:
    c = open(fname, 'r', encoding='utf-8').read()
    if '资源来自网络' in c:
        # Remove the entire footer div
        c = re.sub(
            r'<div style="text-align:center;padding:20px 16px[^>]*>.*?资源来自网络，如有侵权，请联系删除</div>\s*',
            '', c, flags=re.DOTALL
        )
        open(fname, 'w', encoding='utf-8').write(c)
        print(f'{fname}: footer removed')
    else:
        print(f'{fname}: no footer found')
