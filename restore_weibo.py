#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

c = open('weibo.html', 'r', encoding='utf-8').read()

# 1. Add copyright footer (before </body>)
footer_html = '''
<div style="text-align:center;padding:20px 16px;font-size:12px;color:#C27E4A;border-top:1px solid rgba(255,149,45,0.12);margin-top:20px;background:rgba(255,248,240,0.5)">
  &copy;️ 资源来自网络，如有侵权，请联系删除
</div>
'''

if '资源来自网络' not in c:
    c = c.replace('</body>', footer_html + '\n</body>')
    print('Footer added')

# 2. Add draggable="false" to all img tags
c = re.sub(r'<img\s', '<img draggable="false" ', c, flags=re.IGNORECASE)
print('Draggable added')

# 3. Add image protection CSS (before </style>)
protect_css = 'img{-webkit-user-drag:none;user-select:none;-webkit-touch-callout:none}\n'
if '-webkit-user-drag:none' not in c:
    c = c.replace('</style>', protect_css + '</style>')
    print('Image protection CSS added')

# 4. Add image protection JS (before </body>)
protect_js = '<script>\ndocument.addEventListener(\'contextmenu\',function(e){if(e.target.tagName===\'IMG\'){e.preventDefault()}});\n</script>\n'
if 'contextmenu' not in c:
    c = c.replace('</body>', protect_js + '</body>')
    print('Image protection JS added')

open('weibo.html', 'w', encoding='utf-8').write(c)
print('weibo.html all changes applied')

# Verify
c2 = open('weibo.html','r',encoding='utf-8').read()
print('Has 哈喽:', '哈喽' in c2)
print('Has footer:', '资源来自网络' in c2)
print('Has draggable:', 'draggable="false"' in c2)
print('Has CSS protection:', '-webkit-user-drag:none' in c2)
print('Has JS protection:', 'contextmenu' in c2)
print('Has transition:', 'transition fade-out' in c2)
print('Has WEIBO_THUMB:', 'WEIBO_THUMB' in c2)
