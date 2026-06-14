#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
SCRIPT_DIR = Path(__file__).parent.resolve()

FOOTER_HTML = '''
<div style="text-align:center;padding:20px 16px;font-size:12px;color:#C27E4A;border-top:1px solid rgba(255,149,45,0.12);margin-top:20px;background:rgba(255,248,240,0.5)">
  &copy;️ 资源来自网络，如有侵权，请联系删除
</div>
'''

count = 0
for f in sorted(SCRIPT_DIR.glob('*.html')):
    content = f.read_text(encoding='utf-8')
    if '资源来自网络' in content:
        print(f'[SKIP] {f.name} - already has footer')
        continue
    # Insert before </body>
    if '</body>' in content:
        # Make sure we put it before the page transition script
        # The page transition script is the last thing before </body>
        content = content.replace('</body>', FOOTER_HTML + '\n</body>')
        f.write_text(content, encoding='utf-8')
        print(f'[ADD] {f.name}')
        count += 1
    else:
        print(f'[ERR] {f.name} - no </body> tag')

print(f'\nDone! {count} files updated.')
