# -*- coding: utf-8 -*-
import urllib.request
import re
import ssl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='ignore')

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

url = 'https://top.baidu.com/board?tab=realtime'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})
html = urllib.request.urlopen(req, timeout=15, context=ssl_context).read().decode('utf-8', errors='ignore')

print("HTML长度:", len(html))
print("---")

# 尝试多种pattern
patterns = [
    r'json\.set\("hotList",\s*(\[.*?\])\);',
    r'json\.set\("hotList",\s*(\[.*?\])',
    r'"hotList":\s*(\[.*?\])',
]

for p in patterns:
    m = re.search(p, html, re.DOTALL)
    print(f"Pattern {p[:30]}... : {'FOUND' if m else 'NOT FOUND'}")
    if m:
        print("内容:", m.group(1)[:500])
        break
