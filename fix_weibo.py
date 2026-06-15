#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Convert weibo.html from UTF-16LE to UTF-8
raw = open('weibo.html', 'rb').read()
text = raw.decode('utf-16-le')
if text.startswith('\ufeff'):
    text = text[1:]
open('weibo.html', 'w', encoding='utf-8').write(text)
print('weibo.html converted to UTF-8 OK')

# Now restore massage.html from git and remove its footer
import subprocess
subprocess.run(['git', 'checkout', '--', 'massage.html'], capture_output=True)
c = open('massage.html', 'r', encoding='utf-8').read()
# Check if it has the footer
if '资源来自网络' in c:
    # Remove the footer
    import re
    c = re.sub(r'<div style="text-align:center;padding:20px 16px.*?资源来自网络，如有侵权，请联系删除</div>\s*', '', c, flags=re.DOTALL)
    open('massage.html', 'w', encoding='utf-8').write(c)
    print('massage.html footer removed')
else:
    print('massage.html no footer found')

# Check quote.html
subprocess.run(['git', 'checkout', '--', 'quote.html'], capture_output=True)
c = open('quote.html', 'r', encoding='utf-8').read()
if '资源来自网络' in c:
    c = re.sub(r'<div style="text-align:center;padding:20px 16px.*?资源来自网络，如有侵权，请联系删除</div>\s*', '', c, flags=re.DOTALL)
    open('quote.html', 'w', encoding='utf-8').write(c)
    print('quote.html footer removed')
else:
    print('quote.html no footer found')

print('Done!')
