#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""深度检查所有HTML文件的潜在bug"""
import re, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

issues_found = False

for f in sorted(Path('.').glob('*.html')):
    c = f.read_text('utf-8')
    issues = []

    # 1. 检查是否有 unclosed <script> 标签
    opens = len(re.findall(r'<script\b', c, re.IGNORECASE))
    closes = len(re.findall(r'</script>', c, re.IGNORECASE))
    if opens != closes:
        issues.append(f'script标签不匹配: 打开{opens}个, 关闭{closes}个')

    # 2. 检查是否有 unclosed <style> 标签
    opens = len(re.findall(r'<style\b', c, re.IGNORECASE))
    closes = len(re.findall(r'</style>', c, re.IGNORECASE))
    if opens != closes:
        issues.append(f'style标签不匹配: 打开{opens}个, 关闭{closes}个')

    # 3. 检查 img 标签是否完整 (有 src 且有闭合)
    for m in re.finditer(r'<img\s[^>]*>', c):
        tag = m.group()
        if 'src=' not in tag:
            line = c[:m.start()].count('\n') + 1
            issues.append(f'  行{line}: img标签缺少src属性')
        # 检查是否有两个 draggable
        if tag.count('draggable') > 1:
            line = c[:m.start()].count('\n') + 1
            issues.append(f'  行{line}: img标签有多个draggable')

    # 4. 检查 OSS URL 格式是否正确
    for m in re.finditer(r'https://domiii\.oss-cn-hangzhou\.aliyuncs\.com/[^\s"\'<>)]+\.(jpg|png|jpeg|gif|webp)', c):
        url = m.group()
        # 不能有 ?x-oss-process 残留
        if '?x-oss-process=' in url:
            line = c[:m.start()].count('\n') + 1
            issues.append(f'  行{line}: OSS参数残留: {url[:60]}')

    # 5. 检查 a 标签是否有空 href
    for m in re.finditer(r'<a\s[^>]*href\s*=\s*""[^>]*>', c):
        line = c[:m.start()].count('\n') + 1
        issues.append(f'  行{line}: a标签href为空')

    # 6. 检查被 draggable="false" 插入破坏的 img 标签
    #    正常: <img draggable="false" src=...
    #    异常: <img draggable="false" draggable="false" src=...  (重复)
    if '<img draggable="false" draggable="false"' in c:
        issues.append('存在重复的draggable属性')

    # 7. 检查童年页的关键数据是否完整
    if f.name == 'childhood.html':
        if '童年${i}.jpg`,' not in c:
            # 确认反引号正确
            idx = c.find('CHILDHOOD_BASE')
            if idx >= 0:
                snippet = c[idx:idx+60]
                issues.append(f'童年页图片模板可能异常: {repr(snippet)}')

    # 8. 检查shiny页的关键数据
    if f.name == 'shiny.html':
        if 'shiny${id}.jpg`,' not in c:
            idx = c.find('shiny/shiny')
            if idx >= 0:
                snippet = c[idx:idx+50]
                issues.append(f'shiny页图片模板可能异常: {repr(snippet)}')

    # 9. 检查游戏页是否64张图
    if f.name == 'game.html':
        if 'length:66' not in c:
            issues.append('game.html PHOTOS length异常')

    # 10. 检查weibo页图片拼接
    if f.name == 'weibo.html':
        if 'WEIBO_BASE + f' not in c:
            issues.append('weibo.html 图片拼接方式异常')

    if issues:
        print(f'\n{f.name}:')
        for issue in issues:
            print(f'  {issue}')
        issues_found = True
    else:
        print(f'{f.name} ✓')

if not issues_found:
    print('\n全部通过，未发现bug！')
