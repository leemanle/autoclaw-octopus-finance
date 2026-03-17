# -*- coding: utf-8 -*-
import urllib.request
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

# 打印HTML中的script部分
import re
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
for i, s in enumerate(scripts):
    if 'hot' in s.lower() or 'list' in s.lower() or 'score' in s.lower():
        print(f"--- Script {i} ---")
        print(s[:1000])
        print("---")
