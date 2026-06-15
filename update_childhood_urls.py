#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 按编号从1到34排列
URLS = [
    "https://img.heliar.top/file/1781480297862_童年1.jpg",
    "https://img.heliar.top/file/1781480295306_童年2.jpg",
    "https://img.heliar.top/file/1781480295380_童年3.jpg",
    "https://img.heliar.top/file/1781480302618_童年4.jpg",
    "https://img.heliar.top/file/1781480302990_童年5.jpg",
    "https://img.heliar.top/file/1781480300248_童年6.jpg",
    "https://img.heliar.top/file/1781480299884_童年7.jpg",
    "https://img.heliar.top/file/1781480305608_童年8.jpg",
    "https://img.heliar.top/file/1781480309348_童年9.jpg",
    "https://img.heliar.top/file/1781480302418_童年10.jpg",
    "https://img.heliar.top/file/1781480310050_童年11.jpg",
    "https://img.heliar.top/file/1781480308749_童年12.jpg",
    "https://img.heliar.top/file/1781480309903_童年13.jpg",
    "https://img.heliar.top/file/1781480317205_童年14.jpg",
    "https://img.heliar.top/file/1781480310155_童年15.jpg",
    "https://img.heliar.top/file/1781480310944_童年16.jpg",
    "https://img.heliar.top/file/1781480313320_童年17.jpg",
    "https://img.heliar.top/file/1781480313313_童年18.jpg",
    "https://img.heliar.top/file/1781480323488_童年19.jpg",
    "https://img.heliar.top/file/1781480324341_童年20.jpg",
    "https://img.heliar.top/file/1781480321101_童年21.jpg",
    "https://img.heliar.top/file/1781480324853_童年22.jpg",
    "https://img.heliar.top/file/1781480361729_童年23.jpg",
    "https://img.heliar.top/file/1781480355398_童年24.jpg",
    "https://img.heliar.top/file/1781480362991_童年25.jpg",
    "https://img.heliar.top/file/1781480361801_童年26.jpg",
    "https://img.heliar.top/file/1781480367092_童年27.jpg",
    "https://img.heliar.top/file/1781480363104_童年28.jpg",
    "https://img.heliar.top/file/1781480365026_童年29.jpg",
    "https://img.heliar.top/file/1781480369773_童年30.jpg",
    "https://img.heliar.top/file/1781480372868_童年31.jpg",
    "https://img.heliar.top/file/1781480368204_童年32.jpg",
    "https://img.heliar.top/file/1781480369841_童年33.jpg",
    "https://img.heliar.top/file/1781480367767_童年34.jpg",
]

c = open('childhood.html', 'r', encoding='utf-8').read()

# 替换 CHILDHOOD_BASE + `童年${i}.jpg` 为数组查找
old = 'CHILDHOOD_BASE + `童年${i}.jpg`'

# 生成数组
js_arr = '[\n'
for url in URLS:
    js_arr += f"  '{url}',\n"
js_arr += ']'

new = f'(function(){{ const _= {js_arr}; return _[i-1]; }})()'

if old in c:
    c = c.replace(old, new)
    open('childhood.html', 'w', encoding='utf-8').write(c)
    print('childhood.html 已更新')
else:
    print('未找到模板')
