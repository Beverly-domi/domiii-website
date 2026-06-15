#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

c = open('wenjianjia.html', 'r', encoding='utf-8').read()

old = '''    document.body.appendChild(blessDiv);
    setTimeout(() => blessDiv.remove(), 1500);
  });'''

new = '''    document.body.appendChild(blessDiv);
    setTimeout(() => blessDiv.remove(), 1500);

    // 随机播放语音
    (function(){
      const VOICES = [
        'https://domiii.oss-cn-hangzhou.aliyuncs.com/mp3/yuyin.mp3',
        'https://domiii.oss-cn-hangzhou.aliyuncs.com/mp3/\u8bed\u97f32.mp3',
        'https://domiii.oss-cn-hangzhou.aliyuncs.com/mp3/\u8bed\u97f33.mp3'
      ];
      const audio = new Audio(VOICES[Math.floor(Math.random() * VOICES.length)]);
      audio.volume = 0.7;
      audio.play().catch(function(){});
    })();
  });'''

if old in c:
    c = c.replace(old, new)
    open('wenjianjia.html', 'w', encoding='utf-8').write(c)
    print('OK - 语音代码已添加')
else:
    print('Pattern not found!')
    idx = c.find('blessDiv.remove()')
    if idx >= 0:
        print(repr(c[idx:idx+80]))
