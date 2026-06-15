#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

NEW_URLS = {
    1: "https://img.heliar.top/file/1781480928018_shiny1-compressed.jpeg",
    2: "https://img.heliar.top/file/1781480932523_shiny2-compressed.jpeg",
    3: "https://img.heliar.top/file/1781480938033_shiny3-compressed.jpeg",
    4: "https://img.heliar.top/file/1781480940178_shiny4-compressed.jpeg",
    5: "https://img.heliar.top/file/1781480943293_shiny5-compressed.jpeg",
    6: "https://img.heliar.top/file/1781480942909_shiny6-compressed.jpeg",
    7: "https://img.heliar.top/file/1781480939610_shiny7-compressed.jpeg",
    8: "https://img.heliar.top/file/1781480949671_shiny8-compressed.jpeg",
    9: "https://img.heliar.top/file/1781480958455_shiny9-compressed.jpeg",
    10: "https://img.heliar.top/file/1781480945180_shiny10-compressed.jpeg",
    11: "https://img.heliar.top/file/1781480954770_shiny11-compressed.jpeg",
    12: "https://img.heliar.top/file/1781480961578_shiny12-compressed.jpeg",
    13: "https://img.heliar.top/file/1781480962614_shiny13-compressed.jpeg",
    14: "https://img.heliar.top/file/1781480962457_shiny14-compressed.jpeg",
    15: "https://img.heliar.top/file/1781480971362_shiny15-compressed.jpeg",
    16: "https://img.heliar.top/file/1781480972956_shiny16-compressed.jpeg",
    17: "https://img.heliar.top/file/1781480982911_shiny17-compressed.jpeg",
    18: "https://img.heliar.top/file/1781480975901_shiny18-compressed.jpeg",
    19: "https://img.heliar.top/file/1781480991200_shiny19-compressed.jpeg",
    20: "https://img.heliar.top/file/1781480978511_shiny20-compressed.jpeg",
    21: "https://img.heliar.top/file/1781480989273_shiny21-compressed.jpeg",
    22: "https://img.heliar.top/file/1781480997885_shiny22-compressed.jpeg",
    23: "https://img.heliar.top/file/1781481002693_shiny23-compressed.jpeg",
    24: "https://img.heliar.top/file/1781480994941_shiny24-compressed.jpeg",
    25: "https://img.heliar.top/file/1781480996902_shiny25-compressed.jpeg",
    26: "https://img.heliar.top/file/1781481001480_shiny26-compressed.jpeg",
    27: "https://img.heliar.top/file/1781481005631_shiny27-compressed.jpeg",
    28: "https://img.heliar.top/file/1781481007685_shiny28-compressed.jpeg",
    29: "https://img.heliar.top/file/1781481000587_shiny29-compressed.jpeg",
    30: "https://img.heliar.top/file/1781481007181_shiny30-compressed.jpeg",
    31: "https://img.heliar.top/file/1781481013672_shiny31-compressed.jpeg",
    32: "https://img.heliar.top/file/1781481011795_shiny32-compressed.jpeg",
    33: "https://img.heliar.top/file/1781481016281_shiny33-compressed.jpeg",
    34: "https://img.heliar.top/file/1781481009708_shiny34-compressed.jpeg",
    35: "https://img.heliar.top/file/1781481023699_shiny35-compressed.jpeg",
    36: "https://img.heliar.top/file/1781481037216_shiny36-compressed.jpeg",
    37: "https://img.heliar.top/file/1781481016820_shiny37-compressed.jpeg",
    38: "https://img.heliar.top/file/1781481040641_shiny38-compressed.jpeg",
    39: "https://img.heliar.top/file/1781481039622_shiny39-compressed.jpeg",
    40: "https://img.heliar.top/file/1781481043563_shiny40-compressed.jpeg",
    41: "https://img.heliar.top/file/1781481036475_shiny41-compressed.jpeg",
    42: "https://img.heliar.top/file/1781481048834_shiny42-compressed.jpeg",
    43: "https://img.heliar.top/file/1781481048013_shiny43-compressed.jpeg",
    44: "https://img.heliar.top/file/1781481050781_shiny44-compressed.jpeg",
    45: "https://img.heliar.top/file/1781481056098_shiny45-compressed.jpeg",
    46: "https://img.heliar.top/file/1781481060112_shiny46-compressed.jpeg",
    47: "https://img.heliar.top/file/1781481060864_shiny47-compressed.jpeg",
    48: "https://img.heliar.top/file/1781481064106_shiny48-compressed.jpeg",
    49: "https://img.heliar.top/file/1781481068274_shiny49-compressed.jpeg",
    50: "https://img.heliar.top/file/1781481059388_shiny50-compressed.jpeg",
    51: "https://img.heliar.top/file/1781481068263_shiny51-compressed.jpeg",
    52: "https://img.heliar.top/file/1781481071284_shiny52-compressed.jpeg",
    53: "https://img.heliar.top/file/1781481072846_shiny53-compressed.jpeg",
    54: "https://img.heliar.top/file/1781481076913_shiny54-compressed.jpeg",
    55: "https://img.heliar.top/file/1781481077365_shiny55-compressed.jpeg",
    56: "https://img.heliar.top/file/1781481075479_shiny56-compressed.jpeg",
    57: "https://img.heliar.top/file/1781481093399_shiny57-compressed.jpeg",
    58: "https://img.heliar.top/file/1781481099804_shiny58-compressed.jpeg",
    59: "https://img.heliar.top/file/1781481101406_shiny59-compressed.jpeg",
    60: "https://img.heliar.top/file/1781481098644_shiny60-compressed.jpeg",
    61: "https://img.heliar.top/file/1781481102428_shiny61-compressed.jpeg",
    62: "https://img.heliar.top/file/1781481102204_shiny62-compressed.jpeg",
    63: "https://img.heliar.top/file/1781481109579_shiny63-compressed.jpeg",
    64: "https://img.heliar.top/file/1781481115057_shiny64-compressed.jpeg",
    65: "https://img.heliar.top/file/1781481108437_shiny65-compressed.jpeg",
    66: "https://img.heliar.top/file/1781481116783_shiny66-compressed.jpeg",
    67: "https://img.heliar.top/file/1781481114088_shiny67-compressed.jpeg",
    68: "https://img.heliar.top/file/1781481119457_shiny68-compressed.jpeg",
    69: "https://img.heliar.top/file/1781481123815_shiny69-compressed.jpeg",
    70: "https://img.heliar.top/file/1781481128312_shiny70-compressed.jpeg",
    71: "https://img.heliar.top/file/1781481125403_shiny71-compressed.jpeg",
    72: "https://img.heliar.top/file/1781481124948_shiny72-compressed.jpeg",
    73: "https://img.heliar.top/file/1781481126927_shiny73-compressed.jpeg",
    74: "https://img.heliar.top/file/1781481131034_shiny74-compressed.jpeg",
    75: "https://img.heliar.top/file/1781481135229_shiny75-compressed.jpeg",
    76: "https://img.heliar.top/file/1781481126060_shiny76-compressed.jpeg",
    77: "https://img.heliar.top/file/1781481160750_shiny77-compressed.jpeg",
    78: "https://img.heliar.top/file/1781481157481_shiny78-compressed.jpeg",
    79: "https://img.heliar.top/file/1781481154186_shiny79-compressed.jpeg",
    80: "https://img.heliar.top/file/1781481162112_shiny80-compressed.jpeg",
    81: "https://img.heliar.top/file/1781481169068_shiny81-compressed.jpeg",
    82: "https://img.heliar.top/file/1781481162510_shiny82-compressed.jpeg",
    83: "https://img.heliar.top/file/1781481167109_shiny83-compressed.jpeg",
    84: "https://img.heliar.top/file/1781481171151_shiny84-compressed.jpeg",
    85: "https://img.heliar.top/file/1781481172365_shiny85-compressed.jpeg",
    86: "https://img.heliar.top/file/1781481165922_shiny86-compressed.jpeg",
    87: "https://img.heliar.top/file/1781481170766_shiny87-compressed.jpeg",
    88: "https://img.heliar.top/file/1781481179631_shiny88-compressed.jpeg",
    89: "https://img.heliar.top/file/1781481176634_shiny89-compressed.jpeg",
    90: "https://img.heliar.top/file/1781481182171_shiny90-compressed.jpeg",
    91: "https://img.heliar.top/file/1781481185562_shiny91-compressed.jpeg",
    92: "https://img.heliar.top/file/1781481181366_shiny92-compressed.jpeg",
    93: "https://img.heliar.top/file/1781481183072_shiny93-compressed.jpeg",
    94: "https://img.heliar.top/file/1781481181529_shiny94-compressed.jpeg",
    95: "https://img.heliar.top/file/1781481184964_shiny95-compressed.jpeg",
    96: "https://img.heliar.top/file/1781481215088_shiny96-compressed.jpeg",
    97: "https://img.heliar.top/file/1781481192766_shiny97-compressed.jpeg",
    98: "https://img.heliar.top/file/1781481214314_shiny98-compressed.jpeg",
    99: "https://img.heliar.top/file/1781481216895_shiny99-compressed.jpeg",
    100: "https://img.heliar.top/file/1781481218383_shiny100-compressed.jpeg",
    101: "https://img.heliar.top/file/1781481226185_shiny101-compressed.jpeg",
    102: "https://img.heliar.top/file/1781481226290_shiny102-compressed.jpeg",
    103: "https://img.heliar.top/file/1781481229060_shiny103-compressed.jpeg",
    104: "https://img.heliar.top/file/1781481231711_shiny104-compressed.jpeg",
    105: "https://img.heliar.top/file/1781481230851_shiny105-compressed.jpeg",
    106: "https://img.heliar.top/file/1781481234223_shiny106-compressed.jpeg",
    107: "https://img.heliar.top/file/1781481236039_shiny107-compressed.jpeg",
    108: "https://img.heliar.top/file/1781481229230_shiny108-compressed.jpeg",
    109: "https://img.heliar.top/file/1781481234086_shiny109-compressed.jpeg",
    110: "https://img.heliar.top/file/1781481235115_shiny110-compressed.jpeg",
    111: "https://img.heliar.top/file/1781481239355_shiny111-compressed.jpeg",
}

c = open('shiny.html', 'r', encoding='utf-8').read()
count = 0

# shiny.html 使用模板字符串: `https://domiii.oss-cn-hangzhou.aliyuncs.com/shiny/shiny${id}.jpg`
# 替换整个模板字符串
old_template = '`https://domiii.oss-cn-hangzhou.aliyuncs.com/shiny/shiny${id}.jpg`'

# 改为用数组+索引查找
new_code = '''(function(){
  const SHINY_IMGS = ['https://img.heliar.top/file/1781480928018_shiny1-compressed.jpeg'/*1*/'
    +'https://img.heliar.top/file/1781480932523_shiny2-compressed.jpeg'/*2*/'
    +'https://img.heliar.top/file/1781480938033_shiny3-compressed.jpeg'/*3*/'
    +'https://img.heliar.top/file/1781480940178_shiny4-compressed.jpeg'/*4*/'
    +'https://img.heliar.top/file/1781480943293_shiny5-compressed.jpeg'/*5*/'
    +'https://img.heliar.top/file/1781480942909_shiny6-compressed.jpeg'/*6*/'
    +'https://img.heliar.top/file/1781480939610_shiny7-compressed.jpeg'/*7*/'
    +'https://img.heliar.top/file/1781480949671_shiny8-compressed.jpeg'/*8*/'
    +'https://img.heliar.top/file/1781480958455_shiny9-compressed.jpeg'/*9*/'
    +'https://img.heliar.top/file/1781480945180_shiny10-compressed.jpeg'/*10*/'
    +'https://img.heliar.top/file/1781480954770_shiny11-compressed.jpeg'/*11*/'
    +'https://img.heliar.top/file/1781480961578_shiny12-compressed.jpeg'/*12*/'
    +'https://img.heliar.top/file/1781480962614_shiny13-compressed.jpeg'/*13*/'
    +'https://img.heliar.top/file/1781480962457_shiny14-compressed.jpeg'/*14*/'
    +'https://img.heliar.top/file/1781480971362_shiny15-compressed.jpeg'/*15*/'
    +'https://img.heliar.top/file/1781480972956_shiny16-compressed.jpeg'/*16*/'
    +'https://img.heliar.top/file/1781480982911_shiny17-compressed.jpeg'/*17*/'
    +'https://img.heliar.top/file/1781480975901_shiny18-compressed.jpeg'/*18*/'
    +'https://img.heliar.top/file/1781480991200_shiny19-compressed.jpeg'/*19*/'
    +'https://img.heliar.top/file/1781480978511_shiny20-compressed.jpeg'/*20*/'
    +'https://img.heliar.top/file/1781480989273_shiny21-compressed.jpeg'/*21*/'
    +'https://img.heliar.top/file/1781480997885_shiny22-compressed.jpeg'/*22*/'
    +'https://img.heliar.top/file/1781481002693_shiny23-compressed.jpeg'/*23*/'
    +'https://img.heliar.top/file/1781480994941_shiny24-compressed.jpeg'/*24*/'
    +'https://img.heliar.top/file/1781480996902_shiny25-compressed.jpeg'/*25*/'
    +'https://img.heliar.top/file/1781481001480_shiny26-compressed.jpeg'/*26*/'
    +'https://img.heliar.top/file/1781481005631_shiny27-compressed.jpeg'/*27*/'
    +'https://img.heliar.top/file/1781481007685_shiny28-compressed.jpeg'/*28*/'
    +'https://img.heliar.top/file/1781481000587_shiny29-compressed.jpeg'/*29*/'
    +'https://img.heliar.top/file/1781481007181_shiny30-compressed.jpeg'/*30*/'
    +'https://img.heliar.top/file/1781481013672_shiny31-compressed.jpeg'/*31*/'
    +'https://img.heliar.top/file/1781481011795_shiny32-compressed.jpeg'/*32*/'
    +'https://img.heliar.top/file/1781481016281_shiny33-compressed.jpeg'/*33*/'
    +'https://img.heliar.top/file/1781481009708_shiny34-compressed.jpeg'/*34*/'
    +'https://img.heliar.top/file/1781481023699_shiny35-compressed.jpeg'/*35*/'
    +'https://img.heliar.top/file/1781481037216_shiny36-compressed.jpeg'/*36*/'
    +'https://img.heliar.top/file/1781481016820_shiny37-compressed.jpeg'/*37*/'
    +'https://img.heliar.top/file/1781481040641_shiny38-compressed.jpeg'/*38*/'
    +'https://img.heliar.top/file/1781481039622_shiny39-compressed.jpeg'/*39*/'
    +'https://img.heliar.top/file/1781481043563_shiny40-compressed.jpeg'/*40*/'
    +'https://img.heliar.top/file/1781481036475_shiny41-compressed.jpeg'/*41*/'
    +'https://img.heliar.top/file/1781481048834_shiny42-compressed.jpeg'/*42*/'
    +'https://img.heliar.top/file/1781481048013_shiny43-compressed.jpeg'/*43*/'
    +'https://img.heliar.top/file/1781481050781_shiny44-compressed.jpeg'/*44*/'
    +'https://img.heliar.top/file/1781481056098_shiny45-compressed.jpeg'/*45*/'
    +'https://img.heliar.top/file/1781481060112_shiny46-compressed.jpeg'/*46*/'
    +'https://img.heliar.top/file/1781481060864_shiny47-compressed.jpeg'/*47*/'
    +'https://img.heliar.top/file/1781481064106_shiny48-compressed.jpeg'/*48*/'
    +'https://img.heliar.top/file/1781481068274_shiny49-compressed.jpeg'/*49*/'
    +'https://img.heliar.top/file/1781481059388_shiny50-compressed.jpeg'/*50*/'
    +'https://img.heliar.top/file/1781481068263_shiny51-compressed.jpeg'/*51*/'
    +'https://img.heliar.top/file/1781481071284_shiny52-compressed.jpeg'/*52*/'
    +'https://img.heliar.top/file/1781481072846_shiny53-compressed.jpeg'/*53*/'
    +'https://img.heliar.top/file/1781481076913_shiny54-compressed.jpeg'/*54*/'
    +'https://img.heliar.top/file/1781481077365_shiny55-compressed.jpeg'/*55*/'
    +'https://img.heliar.top/file/1781481075479_shiny56-compressed.jpeg'/*56*/'
    +'https://img.heliar.top/file/1781481093399_shiny57-compressed.jpeg'/*57*/'
    +'https://img.heliar.top/file/1781481099804_shiny58-compressed.jpeg'/*58*/'
    +'https://img.heliar.top/file/1781481101406_shiny59-compressed.jpeg'/*59*/'
    +'https://img.heliar.top/file/1781481098644_shiny60-compressed.jpeg'/*60*/'
    +'https://img.heliar.top/file/1781481102428_shiny61-compressed.jpeg'/*61*/'
    +'https://img.heliar.top/file/1781481102204_shiny62-compressed.jpeg'/*62*/'
    +'https://img.heliar.top/file/1781481109579_shiny63-compressed.jpeg'/*63*/'
    +'https://img.heliar.top/file/1781481115057_shiny64-compressed.jpeg'/*64*/'
    +'https://img.heliar.top/file/1781481108437_shiny65-compressed.jpeg'/*65*/'
    +'https://img.heliar.top/file/1781481116783_shiny66-compressed.jpeg'/*66*/'
    +'https://img.heliar.top/file/1781481114088_shiny67-compressed.jpeg'/*67*/'
    +'https://img.heliar.top/file/1781481119457_shiny68-compressed.jpeg'/*68*/'
    +'https://img.heliar.top/file/1781481123815_shiny69-compressed.jpeg'/*69*/'
    +'https://img.heliar.top/file/1781481128312_shiny70-compressed.jpeg'/*70*/'
    +'https://img.heliar.top/file/1781481125403_shiny71-compressed.jpeg'/*71*/'
    +'https://img.heliar.top/file/1781481124948_shiny72-compressed.jpeg'/*72*/'
    +'https://img.heliar.top/file/1781481126927_shiny73-compressed.jpeg'/*73*/'
    +'https://img.heliar.top/file/1781481131034_shiny74-compressed.jpeg'/*74*/'
    +'https://img.heliar.top/file/1781481135229_shiny75-compressed.jpeg'/*75*/'
    +'https://img.heliar.top/file/1781481126060_shiny76-compressed.jpeg'/*76*/'
    +'https://img.heliar.top/file/1781481160750_shiny77-compressed.jpeg'/*77*/'
    +'https://img.heliar.top/file/1781481157481_shiny78-compressed.jpeg'/*78*/'
    +'https://img.heliar.top/file/1781481154186_shiny79-compressed.jpeg'/*79*/'
    +'https://img.heliar.top/file/1781481162112_shiny80-compressed.jpeg'/*80*/'
    +'https://img.heliar.top/file/1781481169068_shiny81-compressed.jpeg'/*81*/'
    +'https://img.heliar.top/file/1781481162510_shiny82-compressed.jpeg'/*82*/'
    +'https://img.heliar.top/file/1781481167109_shiny83-compressed.jpeg'/*83*/'
    +'https://img.heliar.top/file/1781481171151_shiny84-compressed.jpeg'/*84*/'
    +'https://img.heliar.top/file/1781481172365_shiny85-compressed.jpeg'/*85*/'
    +'https://img.heliar.top/file/1781481165922_shiny86-compressed.jpeg'/*86*/'
    +'https://img.heliar.top/file/1781481170766_shiny87-compressed.jpeg'/*87*/'
    +'https://img.heliar.top/file/1781481179631_shiny88-compressed.jpeg'/*88*/'
    +'https://img.heliar.top/file/1781481176634_shiny89-compressed.jpeg'/*89*/'
    +'https://img.heliar.top/file/1781481182171_shiny90-compressed.jpeg'/*90*/'
    +'https://img.heliar.top/file/1781481185562_shiny91-compressed.jpeg'/*91*/'
    +'https://img.heliar.top/file/1781481181366_shiny92-compressed.jpeg'/*92*/'
    +'https://img.heliar.top/file/1781481183072_shiny93-compressed.jpeg'/*93*/'
    +'https://img.heliar.top/file/1781481181529_shiny94-compressed.jpeg'/*94*/'
    +'https://img.heliar.top/file/1781481184964_shiny95-compressed.jpeg'/*95*/'
    +'https://img.heliar.top/file/1781481215088_shiny96-compressed.jpeg'/*96*/'
    +'https://img.heliar.top/file/1781481192766_shiny97-compressed.jpeg'/*97*/'
    +'https://img.heliar.top/file/1781481214314_shiny98-compressed.jpeg'/*98*/'
    +'https://img.heliar.top/file/1781481216895_shiny99-compressed.jpeg'/*99*/'
    +'https://img.heliar.top/file/1781481218383_shiny100-compressed.jpeg'/*100*/'
    +'https://img.heliar.top/file/1781481226185_shiny101-compressed.jpeg'/*101*/'
    +'https://img.heliar.top/file/1781481226290_shiny102-compressed.jpeg'/*102*/'
    +'https://img.heliar.top/file/1781481229060_shiny103-compressed.jpeg'/*103*/'
    +'https://img.heliar.top/file/1781481231711_shiny104-compressed.jpeg'/*104*/'
    +'https://img.heliar.top/file/1781481230851_shiny105-compressed.jpeg'/*105*/'
    +'https://img.heliar.top/file/1781481234223_shiny106-compressed.jpeg'/*106*/'
    +'https://img.heliar.top/file/1781481236039_shiny107-compressed.jpeg'/*107*/'
    +'https://img.heliar.top/file/1781481229230_shiny108-compressed.jpeg'/*108*/'
    +'https://img.heliar.top/file/1781481234086_shiny109-compressed.jpeg'/*109*/'
    +'https://img.heliar.top/file/1781481235115_shiny110-compressed.jpeg'/*110*/'
    +'https://img.heliar.top/file/1781481239355_shiny111-compressed.jpeg'/*111*/'];
  return SHINY_IMGS[id-1];
})()'''

if old_template in c:
    c = c.replace(old_template, new_code)
    open('shiny.html', 'w', encoding='utf-8').write(c)
    print('shiny.html 已更新')
else:
    print('模板未找到')
    # 检查一下当前内容
    idx = c.find('shiny')
    if idx >= 0:
        print(c[idx:idx+120])
