#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='ignore')

import urllib.request
import json
import re

def get_sina_quotes():
    """获取沪深指数行情 - 新浪接口"""
    try:
        # 新浪财经指数接口
        url = "https://hq.sinajs.cn/list=s_sh000001,s_sz399001"
        req = urllib.request.Request(url, headers={
            'Referer': 'https://finance.sina.com.cn',
            'User-Agent': 'Mozilla/5.0'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('gbk', errors='ignore')
            print("=" * 50)
            print("[INDEX] 沪深两市行情")
            print("=" * 50)
            
            # 解析新浪返回的数据
            for line in content.split('\n'):
                if 's_sh000001' in line:
                    parts = line.split('"')
                    if len(parts) > 1:
                        data = parts[1].split(',')
                        print(f"上证指数: {data[1]} ({data[2]} {data[3]}%)")
                elif 's_sz399001' in line:
                    parts = line.split('"')
                    if len(parts) > 1:
                        data = parts[1].split(',')
                        print(f"深证成指: {data[1]} ({data[2]} {data[3]}%)")
    except Exception as e:
        print(f"获取行情失败: {e}")

def get_tencent_news():
    """获取腾讯财经新闻"""
    try:
        url = "https://finance.qq.com/m/news/list.htm"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('gbk', errors='ignore')
            news_list = re.findall(r'target="_blank"[^>]*>([^<]{5,40})</a>', html)
            
            # 过滤噪音，取财经新闻
            finance_news = [n for n in news_list if any(k in n for k in ['股', '市', '金', '融', '经', '济', 'IPO', 'AI', '科技', '政策'])]
            
            print("\n" + "=" * 50)
            print("[NEWS] 财经新闻热点")
            print("=" * 50)
            for i, title in enumerate(finance_news[:10], 1):
                print(f"{i}. {title}")
    except Exception as e:
        print(f"获取新闻失败: {e}")

if __name__ == "__main__":
    get_sina_quotes()
    get_tencent_news()
