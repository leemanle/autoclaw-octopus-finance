# -*- coding: utf-8 -*-
import urllib.request
import json
import ssl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='ignore')

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# 尝试多个新闻源
sources = [
    ("百度热搜", "https://top.baidu.com/board?tab=realtime"),
    ("今日头条", "https://www.toutiao.com/hot-event/hot_board/?origin=hot_word"),
    ("微博热搜", "https://weibo.com/ajax/side/hotSearch"),
]

for name, url in sources:
    try:
        print(f"尝试 {name}...")
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=10, context=ssl_context) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            print(f"{name}: 成功, 长度={len(content)}")
            print(content[:500])
            print("---")
    except Exception as e:
        print(f"{name}: 失败 - {e}")
