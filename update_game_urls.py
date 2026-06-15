#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 从用户消息中提取的所有新URL（去重）
GAME_URLS = [
    "https://img.heliar.top/file/1781481312049_game1-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481315080_game2-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481321845_game3-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481320369_game4-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481321195_game5-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480061726_R1-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481325063_game7-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481323716_game8-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481326221_game9-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481332625_game10-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481329137_game11-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480063457_R2-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480067777_R3-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480068135_R4-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480069470_R5-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480072560_R6-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481336574_game17-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481339030_game18-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480077034_R7-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480079927_R8-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480076868_R9-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480080094_R10-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481345652_game23-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480084882_R11-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480078825_R12-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480087680_R13-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480088183_R14-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480092493_R15-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481353728_game26-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480092610_R16-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480088957_R17-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480099676_R18-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481355173_game28-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480095384_SR1-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480098416_SR2-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481362068_game31-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480134187_SR3-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480133021_SR4-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481363718_game33-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481369384_game34-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481372748_game35-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480130506_SR5-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480132181_SR6-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481367448_game36-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481374611_game37-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480141361_SR7-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480134218_SR8-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481373798_game38-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480143383_SR9-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480144092_SR10-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480152348_SR11-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480149759_SR12-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480153583_SR13-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481383643_game43-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481388184_game42-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481388122_game44-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481392855_game45-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481394036_game46-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481394209_game48-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481403176_game47-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481397885_game49-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480158201_SSR8-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781480164611_SSR7-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481415304_game54-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481419787_game53-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481420963_game56-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481428396_game55-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481428125_game59-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481435566_game62-compressed-compressed.jpeg",
    "https://img.heliar.top/file/1781481437170_game65-compressed-compressed.jpeg",
]

# 去重并只取前66个
seen = set()
unique = []
for url in GAME_URLS:
    if url not in seen:
        seen.add(url)
        unique.append(url)

# 如果不够66个，用已有的循环补
while len(unique) < 66:
    unique.append(unique[len(unique) % len(unique)])

# 只取前66个
unique = unique[:66]

# 生成JS数组代码
js_lines = ['const PHOTOS = [']
for url in unique:
    js_lines.append(f"  '{url}',")
js_lines.append('];')
js_code = '\n'.join(js_lines)

# 替换
c = open('game.html', 'r', encoding='utf-8').read()
old = "const PHOTOS = Array.from({length:66}, (_,i) => 'https://domiii.oss-cn-hangzhou.aliyuncs.com/game/game'+(i+1)+'.jpg');"

if old in c:
    c = c.replace(old, js_code)
    open('game.html', 'w', encoding='utf-8').write(c)
    print(f'game.html 已更新，{len(unique)} 张图片')
else:
    print('未找到旧PHOTOS定义')
