#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 微博图片新链接列表（按weibo编号排序）
NEW_URLS = {
    1: "https://img.heliar.top/file/1781480606487_weibo1-compressed-compressed.jpeg",
    2: "https://img.heliar.top/file/1781480604058_weibo2-compressed-compressed.jpeg",
    3: "https://img.heliar.top/file/1781480599876_weibo3-compressed-compressed.jpeg",
    4: "https://img.heliar.top/file/1781480605397_weibo4-compressed-compressed.jpeg",
    5: "https://img.heliar.top/file/1781480603505_weibo5-compressed-compressed.jpeg",
    6: "https://img.heliar.top/file/1781480604952_weibo6-compressed-compressed.jpeg",
    7: "https://img.heliar.top/file/1781480615927_weibo7-compressed-compressed.jpeg",
    8: "https://img.heliar.top/file/1781480613258_weibo8-compressed-compressed.jpeg",
    9: "https://img.heliar.top/file/1781480620489_weibo9-compressed-compressed.jpeg",
    10: "https://img.heliar.top/file/1781480619101_weibo10-compressed-compressed.jpeg",
    11: "https://img.heliar.top/file/1781480621076_weibo11-compressed-compressed.jpeg",
    12: "https://img.heliar.top/file/1781480625447_weibo12-compressed-compressed.jpeg",
    13: "https://img.heliar.top/file/1781480614958_weibo13-compressed-compressed.jpeg",
    14: "https://img.heliar.top/file/1781480629045_weibo14-compressed-compressed.jpeg",
    15: "https://img.heliar.top/file/1781480626018_weibo15-compressed-compressed.jpeg",
    16: "https://img.heliar.top/file/1781480632553_weibo16-compressed-compressed.jpeg",
    17: "https://img.heliar.top/file/1781480625657_weibo17-compressed-compressed.jpeg",
    18: "https://img.heliar.top/file/1781480624176_weibo18-compressed-compressed.jpeg",
    19: "https://img.heliar.top/file/1781480635332_weibo19-compressed-compressed.jpeg",
    20: "https://img.heliar.top/file/1781480632977_weibo20-compressed-compressed.jpeg",
    21: "https://img.heliar.top/file/1781480641199_weibo21-compressed-compressed.jpeg",
    22: "https://img.heliar.top/file/1781480641730_weibo22-compressed-compressed.jpeg",
    23: "https://img.heliar.top/file/1781480665483_weibo23-compressed-compressed.jpeg",
    24: "https://img.heliar.top/file/1781480668543_weibo24-compressed-compressed.jpeg",
    25: "https://img.heliar.top/file/1781480670850_weibo25-compressed-compressed.jpeg",
    26: "https://img.heliar.top/file/1781480668757_weibo26-compressed-compressed.jpeg",
    27: "https://img.heliar.top/file/1781480679068_weibo27-compressed-compressed.jpeg",
    28: "https://img.heliar.top/file/1781480677154_weibo28-compressed-compressed.jpeg",
    29: "https://img.heliar.top/file/1781480677779_weibo29-compressed-compressed.jpeg",
    30: "https://img.heliar.top/file/1781480680854_weibo30-compressed-compressed.jpeg",
    31: "https://img.heliar.top/file/1781480677934_weibo31-compressed-compressed.jpeg",
    32: "https://img.heliar.top/file/1781480689753_weibo32-compressed-compressed.jpeg",
    33: "https://img.heliar.top/file/1781480681333_weibo33-compressed-compressed.jpeg",
    34: "https://img.heliar.top/file/1781480690519_weibo34-compressed-compressed.jpeg",
    35: "https://img.heliar.top/file/1781480695173_weibo35-compressed-compressed.jpeg",
    36: "https://img.heliar.top/file/1781480695785_weibo36-compressed-compressed.jpeg",
    37: "https://img.heliar.top/file/1781480695406_weibo37-compressed-compressed.jpeg",
    38: "https://img.heliar.top/file/1781480704002_weibo38-compressed-compressed.jpeg",
    39: "https://img.heliar.top/file/1781480696035_weibo39-compressed-compressed.jpeg",
    41: "https://img.heliar.top/file/1781480707431_weibo41-compressed-compressed.jpeg",
    42: "https://img.heliar.top/file/1781480705956_weibo42-compressed-compressed.jpeg",
    43: "https://img.heliar.top/file/1781480727923_weibo43-compressed-compressed.jpeg",
    44: "https://img.heliar.top/file/1781480728829_weibo44-compressed-compressed.jpeg",
    45: "https://img.heliar.top/file/1781480726699_weibo45-compressed-compressed.jpeg",
    47: "https://img.heliar.top/file/1781480735626_weibo47-compressed-compressed.jpeg",
    49: "https://img.heliar.top/file/1781480734198_weibo49-compressed-compressed.jpeg",
    50: "https://img.heliar.top/file/1781480741456_weibo50-compressed-compressed.jpeg",
    53: "https://img.heliar.top/file/1781480739821_weibo53-compressed-compressed.jpeg",
    55: "https://img.heliar.top/file/1781480749732_weibo55-compressed-compressed.jpeg",
    56: "https://img.heliar.top/file/1781480744473_weibo56-compressed-compressed.jpeg",
    60: "https://img.heliar.top/file/1781480752626_weibo60-compressed-compressed.jpeg",
    64: "https://img.heliar.top/file/1781480748148_weibo64-compressed-compressed.jpeg",
    66: "https://img.heliar.top/file/1781480752820_weibo66-compressed-compressed.jpeg",
    69: "https://img.heliar.top/file/1781480757397_weibo69-compressed-compressed.jpeg",
    70: "https://img.heliar.top/file/1781480758372_weibo70-compressed-compressed.jpeg",
    71: "https://img.heliar.top/file/1781480752684_weibo71-compressed-compressed.jpeg",
    73: "https://img.heliar.top/file/1781480767756_weibo73-compressed-compressed.jpeg",
    75: "https://img.heliar.top/file/1781480766178_weibo75-compressed-compressed.jpeg",
    76: "https://img.heliar.top/file/1781480772211_weibo76-compressed-compressed.jpeg",
    78: "https://img.heliar.top/file/1781480766876_weibo78-compressed-compressed.jpeg",
    79: "https://img.heliar.top/file/1781480776944_weibo79-compressed-compressed.jpeg",
    80: "https://img.heliar.top/file/1781480784923_weibo80-compressed-compressed.jpeg",
    82: "https://img.heliar.top/file/1781480798343_weibo82-compressed-compressed.jpeg",
    83: "https://img.heliar.top/file/1781480788506_weibo83-compressed-compressed.jpeg",
    84: "https://img.heliar.top/file/1781480799119_weibo84-compressed-compressed.jpeg",
    85: "https://img.heliar.top/file/1781480801872_weibo85-compressed-compressed.jpeg",
    86: "https://img.heliar.top/file/1781480809628_weibo86-compressed-compressed.jpeg",
    87: "https://img.heliar.top/file/1781480805680_weibo87-compressed-compressed.jpeg",
    88: "https://img.heliar.top/file/1781480806837_weibo88-compressed-compressed.jpeg",
    89: "https://img.heliar.top/file/1781480816346_weibo89-compressed-compressed.jpeg",
    90: "https://img.heliar.top/file/1781480809948_weibo90-compressed-compressed.jpeg",
    92: "https://img.heliar.top/file/1781480817830_weibo92-compressed-compressed.jpeg",
    93: "https://img.heliar.top/file/1781480818169_weibo93-compressed-compressed.jpeg",
    94: "https://img.heliar.top/file/1781480824697_weibo94-compressed-compressed.jpeg",
    95: "https://img.heliar.top/file/1781480822666_weibo95-compressed-compressed.jpeg",
    100: "https://img.heliar.top/file/1781480821215_weibo100-compressed-compressed.jpeg",
    102: "https://img.heliar.top/file/1781480849522_weibo102-compressed-compressed.jpeg",
    103: "https://img.heliar.top/file/1781480854100_weibo103-compressed-compressed.jpeg",
    104: "https://img.heliar.top/file/1781480858329_weibo104-compressed-compressed.jpeg",
    105: "https://img.heliar.top/file/1781480856420_weibo105-compressed-compressed.jpeg",
    106: "https://img.heliar.top/file/1781480857572_weibo106-compressed-compressed.jpeg",
}

c = open('weibo.html', 'r', encoding='utf-8').read()
count = 0
not_found = []

for num, new_url in NEW_URLS.items():
    old_name = f'weibo{num}.jpg'
    old_url = f'https://domiii.oss-cn-hangzhou.aliyuncs.com/weibo/{old_name}'
    if old_url in c:
        c = c.replace(old_url, new_url)
        count += 1
        print(f'[OK] weibo{num}.jpg 已替换')
    else:
        not_found.append(num)
        print(f'[SKIP] weibo{num}.jpg 未找到')

open('weibo.html', 'w', encoding='utf-8').write(c)
print(f'\n共替换 {count} 个微博图片链接')
if not_found:
    print(f'未找到的编号: {not_found}')
