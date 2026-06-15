#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 新URL列表 (按ID顺序)
URLS = [
    "https://img.heliar.top/file/1781480928018_shiny1-compressed.jpeg",
    "https://img.heliar.top/file/1781480932523_shiny2-compressed.jpeg",
    "https://img.heliar.top/file/1781480938033_shiny3-compressed.jpeg",
    "https://img.heliar.top/file/1781480940178_shiny4-compressed.jpeg",
    "https://img.heliar.top/file/1781480943293_shiny5-compressed.jpeg",
    "https://img.heliar.top/file/1781480942909_shiny6-compressed.jpeg",
    "https://img.heliar.top/file/1781480939610_shiny7-compressed.jpeg",
    "https://img.heliar.top/file/1781480949671_shiny8-compressed.jpeg",
    "https://img.heliar.top/file/1781480958455_shiny9-compressed.jpeg",
    "https://img.heliar.top/file/1781480945180_shiny10-compressed.jpeg",
    "https://img.heliar.top/file/1781480954770_shiny11-compressed.jpeg",
    "https://img.heliar.top/file/1781480961578_shiny12-compressed.jpeg",
    "https://img.heliar.top/file/1781480962614_shiny13-compressed.jpeg",
    "https://img.heliar.top/file/1781480962457_shiny14-compressed.jpeg",
    "https://img.heliar.top/file/1781480971362_shiny15-compressed.jpeg",
    "https://img.heliar.top/file/1781480972956_shiny16-compressed.jpeg",
    "https://img.heliar.top/file/1781480982911_shiny17-compressed.jpeg",
    "https://img.heliar.top/file/1781480975901_shiny18-compressed.jpeg",
    "https://img.heliar.top/file/1781480991200_shiny19-compressed.jpeg",
    "https://img.heliar.top/file/1781480978511_shiny20-compressed.jpeg",
    "https://img.heliar.top/file/1781480989273_shiny21-compressed.jpeg",
    "https://img.heliar.top/file/1781480997885_shiny22-compressed.jpeg",
    "https://img.heliar.top/file/1781481002693_shiny23-compressed.jpeg",
    "https://img.heliar.top/file/1781480994941_shiny24-compressed.jpeg",
    "https://img.heliar.top/file/1781480996902_shiny25-compressed.jpeg",
    "https://img.heliar.top/file/1781481001480_shiny26-compressed.jpeg",
    "https://img.heliar.top/file/1781481005631_shiny27-compressed.jpeg",
    "https://img.heliar.top/file/1781481007685_shiny28-compressed.jpeg",
    "https://img.heliar.top/file/1781481000587_shiny29-compressed.jpeg",
    "https://img.heliar.top/file/1781481007181_shiny30-compressed.jpeg",
    "https://img.heliar.top/file/1781481013672_shiny31-compressed.jpeg",
    "https://img.heliar.top/file/1781481011795_shiny32-compressed.jpeg",
    "https://img.heliar.top/file/1781481016281_shiny33-compressed.jpeg",
    "https://img.heliar.top/file/1781481009708_shiny34-compressed.jpeg",
    "https://img.heliar.top/file/1781481023699_shiny35-compressed.jpeg",
    "https://img.heliar.top/file/1781481037216_shiny36-compressed.jpeg",
    "https://img.heliar.top/file/1781481016820_shiny37-compressed.jpeg",
    "https://img.heliar.top/file/1781481040641_shiny38-compressed.jpeg",
    "https://img.heliar.top/file/1781481039622_shiny39-compressed.jpeg",
    "https://img.heliar.top/file/1781481043563_shiny40-compressed.jpeg",
    "https://img.heliar.top/file/1781481036475_shiny41-compressed.jpeg",
    "https://img.heliar.top/file/1781481048834_shiny42-compressed.jpeg",
    "https://img.heliar.top/file/1781481048013_shiny43-compressed.jpeg",
    "https://img.heliar.top/file/1781481050781_shiny44-compressed.jpeg",
    "https://img.heliar.top/file/1781481056098_shiny45-compressed.jpeg",
    "https://img.heliar.top/file/1781481060112_shiny46-compressed.jpeg",
    "https://img.heliar.top/file/1781481060864_shiny47-compressed.jpeg",
    "https://img.heliar.top/file/1781481064106_shiny48-compressed.jpeg",
    "https://img.heliar.top/file/1781481068274_shiny49-compressed.jpeg",
    "https://img.heliar.top/file/1781481059388_shiny50-compressed.jpeg",
    "https://img.heliar.top/file/1781481068263_shiny51-compressed.jpeg",
    "https://img.heliar.top/file/1781481071284_shiny52-compressed.jpeg",
    "https://img.heliar.top/file/1781481072846_shiny53-compressed.jpeg",
    "https://img.heliar.top/file/1781481076913_shiny54-compressed.jpeg",
    "https://img.heliar.top/file/1781481077365_shiny55-compressed.jpeg",
    "https://img.heliar.top/file/1781481075479_shiny56-compressed.jpeg",
    "https://img.heliar.top/file/1781481093399_shiny57-compressed.jpeg",
    "https://img.heliar.top/file/1781481099804_shiny58-compressed.jpeg",
    "https://img.heliar.top/file/1781481101406_shiny59-compressed.jpeg",
    "https://img.heliar.top/file/1781481098644_shiny60-compressed.jpeg",
    "https://img.heliar.top/file/1781481102428_shiny61-compressed.jpeg",
    "https://img.heliar.top/file/1781481102204_shiny62-compressed.jpeg",
    "https://img.heliar.top/file/1781481109579_shiny63-compressed.jpeg",
    "https://img.heliar.top/file/1781481115057_shiny64-compressed.jpeg",
    "https://img.heliar.top/file/1781481108437_shiny65-compressed.jpeg",
    "https://img.heliar.top/file/1781481116783_shiny66-compressed.jpeg",
    "https://img.heliar.top/file/1781481114088_shiny67-compressed.jpeg",
    "https://img.heliar.top/file/1781481119457_shiny68-compressed.jpeg",
    "https://img.heliar.top/file/1781481123815_shiny69-compressed.jpeg",
    "https://img.heliar.top/file/1781481128312_shiny70-compressed.jpeg",
    "https://img.heliar.top/file/1781481125403_shiny71-compressed.jpeg",
    "https://img.heliar.top/file/1781481124948_shiny72-compressed.jpeg",
    "https://img.heliar.top/file/1781481126927_shiny73-compressed.jpeg",
    "https://img.heliar.top/file/1781481131034_shiny74-compressed.jpeg",
    "https://img.heliar.top/file/1781481135229_shiny75-compressed.jpeg",
    "https://img.heliar.top/file/1781481126060_shiny76-compressed.jpeg",
    "https://img.heliar.top/file/1781481160750_shiny77-compressed.jpeg",
    "https://img.heliar.top/file/1781481157481_shiny78-compressed.jpeg",
    "https://img.heliar.top/file/1781481154186_shiny79-compressed.jpeg",
    "https://img.heliar.top/file/1781481162112_shiny80-compressed.jpeg",
    "https://img.heliar.top/file/1781481169068_shiny81-compressed.jpeg",
    "https://img.heliar.top/file/1781481162510_shiny82-compressed.jpeg",
    "https://img.heliar.top/file/1781481167109_shiny83-compressed.jpeg",
    "https://img.heliar.top/file/1781481171151_shiny84-compressed.jpeg",
    "https://img.heliar.top/file/1781481172365_shiny85-compressed.jpeg",
    "https://img.heliar.top/file/1781481165922_shiny86-compressed.jpeg",
    "https://img.heliar.top/file/1781481170766_shiny87-compressed.jpeg",
    "https://img.heliar.top/file/1781481179631_shiny88-compressed.jpeg",
    "https://img.heliar.top/file/1781481176634_shiny89-compressed.jpeg",
    "https://img.heliar.top/file/1781481182171_shiny90-compressed.jpeg",
    "https://img.heliar.top/file/1781481185562_shiny91-compressed.jpeg",
    "https://img.heliar.top/file/1781481181366_shiny92-compressed.jpeg",
    "https://img.heliar.top/file/1781481183072_shiny93-compressed.jpeg",
    "https://img.heliar.top/file/1781481181529_shiny94-compressed.jpeg",
    "https://img.heliar.top/file/1781481184964_shiny95-compressed.jpeg",
    "https://img.heliar.top/file/1781481215088_shiny96-compressed.jpeg",
    "https://img.heliar.top/file/1781481192766_shiny97-compressed.jpeg",
    "https://img.heliar.top/file/1781481214314_shiny98-compressed.jpeg",
    "https://img.heliar.top/file/1781481216895_shiny99-compressed.jpeg",
    "https://img.heliar.top/file/1781481218383_shiny100-compressed.jpeg",
    "https://img.heliar.top/file/1781481226185_shiny101-compressed.jpeg",
    "https://img.heliar.top/file/1781481226290_shiny102-compressed.jpeg",
    "https://img.heliar.top/file/1781481229060_shiny103-compressed.jpeg",
    "https://img.heliar.top/file/1781481231711_shiny104-compressed.jpeg",
    "https://img.heliar.top/file/1781481230851_shiny105-compressed.jpeg",
    "https://img.heliar.top/file/1781481234223_shiny106-compressed.jpeg",
    "https://img.heliar.top/file/1781481236039_shiny107-compressed.jpeg",
    "https://img.heliar.top/file/1781481229230_shiny108-compressed.jpeg",
    "https://img.heliar.top/file/1781481234086_shiny109-compressed.jpeg",
    "https://img.heliar.top/file/1781481235115_shiny110-compressed.jpeg",
    "https://img.heliar.top/file/1781481239355_shiny111-compressed.jpeg",
]

# 生成正确的JavaScript代码
js_code = 'const SHINY_IMGS = [\n'
for i, url in enumerate(URLS):
    comma = ',' if i < len(URLS) - 1 else ''
    js_code += f"  '{url}'{comma}\n"
js_code += '];'

# 替换shiny.html中的内容
c = open('shiny.html', 'r', encoding='utf-8').read()

# 找到旧的src模板并替换
old = '`https://domiii.oss-cn-hangzhou.aliyuncs.com/shiny/shiny${id}.jpg`'
new = f'(function(){{ {js_code}; return SHINY_IMGS[id-1]; }})()'

if old in c:
    c = c.replace(old, new)
    open('shiny.html', 'w', encoding='utf-8').write(c)
    print('shiny.html 已更新')
else:
    print('未找到旧模板')
    # 可能已经被上次更新搞坏了，看看现在是什么
    idx = c.find('SHINY_IMGS')
    if idx >= 0:
        print('SHINY_IMGS 已存在，说明已经更新过了')
