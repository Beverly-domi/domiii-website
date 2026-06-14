import os, re, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
script_dir = Path(__file__).parent.resolve()

url_new = "https://domiii.oss-cn-hangzhou.aliyuncs.com/images/"

html_files = [f for f in script_dir.glob("*.html")]

count = 0
for f in html_files:
    content = f.read_text(encoding='utf-8')
    # 把根目录的OSS地址 改成 images/ 前缀
    old = "https://domiii.oss-cn-hangzhou.aliyuncs.com/"
    new = url_new
    if old in content:
        content = content.replace(old, new)
        f.write_text(content, encoding='utf-8')
        n = content.count(new)
        count += 1
        print(f"已修改: {f.name} ({n}处)")

print(f"\n共修改 {count} 个文件")
