#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
财经新闻抓取脚本 - 最小化可行版本
"""

import urllib.request
import json
import re
from datetime import datetime

def fetch_cls():
    """财联社APP接口 - 可能有JSON接口"""
    try:
        url = "https://api3.cls.cn/nodeapi/subject/1505"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data
    except Exception as e:
        return {"error": str(e)}

def fetch_21jingji():
    """21财经 - 尝试抓取首页"""
    try:
        url = "https://m.21jingji.com/"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # 简单提取标题
            titles = re.findall(r'<a[^>]*>(.{5,50}?)</a>', html)
            return {"titles": titles[:10], "source": "21jingji"}
    except Exception as e:
        return {"error": str(e)}

def fetch_wallstreetcn():
    """华尔街见闻"""
    try:
        url = "https://api.wallstreetcn.com/apiv1/content/articles?channelId=1&clientType=web&clientVersion=1.0.0"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data
    except Exception as e:
        return {"error": str(e)}

def fetch_tencent_finance():
    """腾讯财经"""
    try:
        url = "https://finance.qq.com/m/news/list.htm"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('gbk', errors='ignore')
            # 提取标题
            titles = re.findall(r'target="_blank"[^>]*>([^<]{5,50})</a>', html)
            return {"titles": titles[:10], "source": "tencent"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 开始抓取财经新闻...\n")
    
    print("=== 尝试 21财经 ===")
    result = fetch_21jingji()
    print(json.dumps(result, ensure_ascii=False, indent=2)[:2000])
    print("\n" + "="*50 + "\n")
    
    print("=== 尝试 华尔街见闻 ===")
    result = fetch_wallstreetcn()
    print(json.dumps(result, ensure_ascii=False, indent=2)[:2000])
