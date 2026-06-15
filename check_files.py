#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全面扫描所有HTML文件，检查潜在语法问题"""
import re, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ok = True
for f in sorted(Path('.').glob('*.html')):
    c = f.read_text('utf-8')
    issues = []

    # 1. 检查模板字符串中 .jpg 后面缺反引号
    for m in re.finditer(r'`[^`]*\.jpg\n', c):
        line = c[:m.start()].count('\n') + 1
        issues.append(f'  行{line}: 模板字符串jpg后缺反引号')

    # 2. 检查模板字符串中 .png 后面缺反引号  
    for m in re.finditer(r'`[^`]*\.png\n', c):
        line = c[:m.start()].count('\n') + 1
        issues.append(f'  行{line}: 模板字符串png后缺反引号')

    # 3. 检查 .jpg?x-oss-process 残留
    if 'x-oss-process' in c:
        for m in re.finditer(r'\.jpg\?x-oss-process[^\s"\'<>)]*', c):
            line = c[:m.start()].count('\n') + 1
            issues.append(f'  行{line}: OSS参数残留')

    # 4. 检查 WEIBO_THUMB 残留
    if 'WEIBO_THUMB' in c:
        issues.append('  WEIBO_THUMB 残留')

    # 5. 检查 transition 残留
    if 'Page transition fade-out' in c:
        issues.append('  transition JS 残留')

    # 6. 检查 gaohui.html 的音频播放器完整性
    if f.name == 'gaohui.html' and 'audioPlaybackState' not in c:
        issues.append('  gaohui.html audioPlaybackState 可能丢失')

    if issues:
        print(f'{f.name}:')
        for issue in issues:
            print(issue)
        ok = False
    else:
        print(f'{f.name} - OK')

if ok:
    print('\n所有文件检查通过，无问题！')
else:
    print('\n有问题需要修复')
