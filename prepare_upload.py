#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, shutil, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 源文件夹：压缩图片所在位置
SRC = Path(r"D:\桌面\张奕然网站\照片")
# 目标文件夹：整理好的文件
DST = Path(r"D:\桌面\张奕然网站\upload_oss")

# 需要处理的子文件夹
FOLDERS = ['card', 'childhood', 'game', 'shiny', 'weibo']

total = 0
for folder in FOLDERS:
    src_dir = SRC / folder
    dst_dir = DST / folder
    
    if not src_dir.exists():
        print(f'[SKIP] {folder} - 源文件夹不存在')
        continue
    
    dst_dir.mkdir(parents=True, exist_ok=True)
    
    count = 0
    for f in sorted(src_dir.iterdir()):
        if f.is_file() and f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
            # 去掉 -compressed 后缀
            new_name = f.stem.replace('-compressed', '') + f.suffix
            dst_file = dst_dir / new_name
            shutil.copy2(f, dst_file)
            count += 1
            total += 1
    
    print(f'[OK] {folder} - {count} 个文件')

print(f'\n总计 {total} 个文件已整理到: {DST}')
print('\n上传说明：')
print(f'1. 打开 https://oss.console.aliyun.com/ ')
print(f'2. 进入 domiii 桶')
print(f'3. 分别将 {DST}/card → 上传到 OSS 的 card/')
print(f'4. 分别将 {DST}/childhood → 上传到 OSS 的 childhood/')
print(f'5. 分别将 {DST}/game → 上传到 OSS 的 game/')
print(f'6. 分别将 {DST}/shiny → 上传到 OSS 的 shiny/')
print(f'7. 分别将 {DST}/weibo → 上传到 OSS 的 weibo/')
print('注意：只能选择"追加"模式来替换，勾选同名文件覆盖')
