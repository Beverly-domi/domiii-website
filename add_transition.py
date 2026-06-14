#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
SCRIPT_DIR = Path(__file__).parent.resolve()

PAGE_TRANSITION_CSS = '''
/* page fade in/out */
body{animation:pgIn .35s ease}
@keyframes pgIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
'''

PAGE_TRANSITION_JS = '''
// Page transition fade-out
(function(){var t;document.addEventListener('click',function(e){var a=e.target.closest('a[href]');if(!a)return;var h=a.getAttribute('href');if(!h||h.startsWith('#')||h.startsWith('http')||h.startsWith('javascript'))return;e.preventDefault();clearTimeout(t);document.body.style.transition='opacity .25s ease';document.body.style.opacity='0';t=setTimeout(function(){window.location.href=h},230)})})();
'''

count = 0
for f in sorted(SCRIPT_DIR.glob('*.html')):
    content = f.read_text(encoding='utf-8')
    modified = False

    # Skip if already has page transition
    if 'pgIn' in content:
        print(f'[SKIP] {f.name} - already has transition')
        continue

    # Add CSS before </style>
    if '</style>' in content:
        # Find the last </style>
        idx = content.rfind('</style>')
        before = content[:idx]
        after = content[idx:]
        content = before + PAGE_TRANSITION_CSS + after
        modified = True

    # Add JS before </body>
    if '</body>' in content and '</script>' in content:
        content = content.replace('</body>', PAGE_TRANSITION_JS + '\n</body>')
        modified = True

    if modified:
        f.write_text(content, encoding='utf-8')
        print(f'[ADD] {f.name} - page transition added')
        count += 1
    else:
        print(f'[ERR] {f.name} - could not add transition')

print(f'\nDone! {count} files updated.')
