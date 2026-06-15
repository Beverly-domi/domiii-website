#!/usr/bin/env python3
# -*- coding: utf-8 -*-
c = open('weibo.html', 'r', encoding='utf-8').read()
old = 'const WEIBO_BASE = "https://domiii.oss-cn-hangzhou.aliyuncs.com/weibo/";'
new = 'const WEIBO_BASE = "";'
if old in c:
    c = c.replace(old, new)
    open('weibo.html', 'w', encoding='utf-8').write(c)
    print('WEIBO_BASE cleared')
else:
    print('Pattern not found')
