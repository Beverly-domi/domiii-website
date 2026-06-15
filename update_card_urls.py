#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 新图片URL映射表 - 卡片文件名 → 新链接
NEW_URLS = {
    "R1.jpg":  "https://img.heliar.top/file/1781480061726_R1-compressed-compressed.jpeg",
    "R2.jpg":  "https://img.heliar.top/file/1781480063457_R2-compressed-compressed.jpeg",
    "R3.jpg":  "https://img.heliar.top/file/1781480067777_R3-compressed-compressed.jpeg",
    "R4.jpg":  "https://img.heliar.top/file/1781480068135_R4-compressed-compressed.jpeg",
    "R5.jpg":  "https://img.heliar.top/file/1781480069470_R5-compressed-compressed.jpeg",
    "R6.jpg":  "https://img.heliar.top/file/1781480072560_R6-compressed-compressed.jpeg",
    "R7.jpg":  "https://img.heliar.top/file/1781480077034_R7-compressed-compressed.jpeg",
    "R8.jpg":  "https://img.heliar.top/file/1781480079927_R8-compressed-compressed.jpeg",
    "R9.jpg":  "https://img.heliar.top/file/1781480076868_R9-compressed-compressed.jpeg",
    "R10.jpg": "https://img.heliar.top/file/1781480080094_R10-compressed-compressed.jpeg",
    "R11.jpg": "https://img.heliar.top/file/1781480084882_R11-compressed-compressed.jpeg",
    "R12.jpg": "https://img.heliar.top/file/1781480078825_R12-compressed-compressed.jpeg",
    "R13.jpg": "https://img.heliar.top/file/1781480087680_R13-compressed-compressed.jpeg",
    "R14.jpg": "https://img.heliar.top/file/1781480088183_R14-compressed-compressed.jpeg",
    "R15.jpg": "https://img.heliar.top/file/1781480092493_R15-compressed-compressed.jpeg",
    "R16.jpg": "https://img.heliar.top/file/1781480092610_R16-compressed-compressed.jpeg",
    "R17.jpg": "https://img.heliar.top/file/1781480088957_R17-compressed-compressed.jpeg",
    "R18.jpg": "https://img.heliar.top/file/1781480099676_R18-compressed-compressed.jpeg",
    "R19.jpg": "https://domiii.oss-cn-hangzhou.aliyuncs.com/card/R19.jpg",
    "SR1.jpg": "https://img.heliar.top/file/1781480095384_SR1-compressed-compressed.jpeg",
    "SR2.jpg": "https://img.heliar.top/file/1781480098416_SR2-compressed-compressed.jpeg",
    "SR3.jpg": "https://img.heliar.top/file/1781480134187_SR3-compressed-compressed.jpeg",
    "SR4.jpg": "https://img.heliar.top/file/1781480133021_SR4-compressed-compressed.jpeg",
    "SR5.jpg": "https://img.heliar.top/file/1781480130506_SR5-compressed-compressed.jpeg",
    "SR6.jpg": "https://img.heliar.top/file/1781480132181_SR6-compressed-compressed.jpeg",
    "SR7.jpg": "https://img.heliar.top/file/1781480141361_SR7-compressed-compressed.jpeg",
    "SR8.jpg": "https://img.heliar.top/file/1781480134218_SR8-compressed-compressed.jpeg",
    "SR9.jpg": "https://img.heliar.top/file/1781480143383_SR9-compressed-compressed.jpeg",
    "SR10.jpg":"https://img.heliar.top/file/1781480144092_SR10-compressed-compressed.jpeg",
    "SR11.jpg":"https://img.heliar.top/file/1781480152348_SR11-compressed-compressed.jpeg",
    "SR12.jpg":"https://img.heliar.top/file/1781480149759_SR12-compressed-compressed.jpeg",
    "SR13.jpg":"https://img.heliar.top/file/1781480153583_SR13-compressed-compressed.jpeg",
    "SSR1.jpg":"https://img.heliar.top/file/1781480154957_SSR1-compressed-compressed.jpeg",
    "SSR2.jpg":"https://img.heliar.top/file/1781480158595_SSR2-compressed-compressed.jpeg",
    "SSR3.jpg":"https://img.heliar.top/file/1781480157464_SSR3-compressed-compressed.jpeg",
    "SSR4.jpg":"https://img.heliar.top/file/1781480154212_SSR4-compressed-compressed.jpeg",
    "SSR5.jpg":"https://img.heliar.top/file/1781480163412_SSR5-compressed-compressed.jpeg",
    "SSR6.jpg":"https://img.heliar.top/file/1781480162211_SSR6-compressed-compressed.jpeg",
    "SSR7.jpg":"https://img.heliar.top/file/1781480164611_SSR7-compressed-compressed.jpeg",
    "SSR8.jpg":"https://domiii.oss-cn-hangzhou.aliyuncs.com/card/SSR8.jpg",
    "SP1.jpg": "https://img.heliar.top/file/1781480093885_SP1-compressed.jpeg",
    "SP2.jpg": "https://img.heliar.top/file/1781480093977_SP2-compressed-compressed.jpeg",
}

# 读入card.html
c = open('card.html', 'r', encoding='utf-8').read()
count = 0

# 替换每个旧OSS地址为新的img.heliar.top地址
for old_name, new_url in NEW_URLS.items():
    old_url = f'https://domiii.oss-cn-hangzhou.aliyuncs.com/card/{old_name}'
    if old_url in c:
        c = c.replace(old_url, new_url)
        count += 1
        print(f'[OK] {old_name} 已替换')
    else:
        print(f'[SKIP] {old_name} 未找到')

open('card.html', 'w', encoding='utf-8').write(c)
print(f'\n共替换 {count} 个图片链接')
