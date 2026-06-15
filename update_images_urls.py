#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io, re
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 新旧URL映射 (旧OSS URL → 新heliar URL)
REPLACE = {
    # xiaotu系列 (首页拍立得)
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu1.jpg": "https://img.heliar.top/file/1781481618863_xiaotu1-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu2.jpg": "https://img.heliar.top/file/1781481624856_xiaotu2-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu3.jpg": "https://img.heliar.top/file/1781481625348_xiaotu3-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu5.jpg": "https://img.heliar.top/file/1781481626155_xiaotu5-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu6.jpg": "https://img.heliar.top/file/1781481625130_xiaotu6-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu7.jpg": "https://img.heliar.top/file/1781481634532_xiaotu7-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu9.jpg": "https://img.heliar.top/file/1781481636930_xiaotu9-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu10.jpg": "https://img.heliar.top/file/1781481632417_xiaotu10-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu11.jpg": "https://img.heliar.top/file/1781481638419_xiaotu11-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu12.jpg": "https://img.heliar.top/file/1781481633697_xiaotu12-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu13.jpg": "https://img.heliar.top/file/1781481638380_xiaotu13-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu14.jpg": "https://img.heliar.top/file/1781481636249_xiaotu14-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu15.jpg": "https://img.heliar.top/file/1781481638629_xiaotu15-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu16.jpg": "https://img.heliar.top/file/1781481648560_xiaotu16-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu17.jpg": "https://img.heliar.top/file/1781481647217_xiaotu17-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/xiaotu18.jpg": "https://img.heliar.top/file/1781481645926_xiaotu18-compressed.jpeg",
    # 背景
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/beijing%20(2).jpg": "https://img.heliar.top/file/1781481615434_beijing__2_-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/beijing (2).jpg": "https://img.heliar.top/file/1781481615434_beijing__2_-compressed.jpeg",
    # 小猪
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/pig_normal.png": "https://img.heliar.top/file/1781481618465_pig_normal-compressed.jpeg",
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/pig_happy.png": "https://img.heliar.top/file/1781481624202_pig_happy-compressed.jpeg",
    # 头像
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/touxiang.jpg": "https://img.heliar.top/file/1781481615792_touxiang-compressed.jpeg",
    # 桃心猪
    "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/桃心猪.png": "https://img.heliar.top/file/1781481652372_桃心猪-compressed.jpeg",
}

total = 0
for html_file in sorted(Path('.').glob('*.html')):
    c = html_file.read_text(encoding='utf-8')
    changed = False
    for old_url, new_url in REPLACE.items():
        if old_url in c:
            c = c.replace(old_url, new_url)
            changed = True
            total += 1
    if changed:
        html_file.write_text(c, encoding='utf-8')
        print(f'[OK] {html_file.name}')
    else:
        print(f'[--] {html_file.name} 无变化')

print(f'\n共替换 {total} 处图片链接')
