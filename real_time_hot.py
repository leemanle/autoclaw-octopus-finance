#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实时热点抓取 - 增强版
使用已验证可用的数据源
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='ignore')

import urllib.request
import json
import re
import os
from datetime import datetime
from html import unescape

def fetch_sina_finance():
    """抓取新浪财经"""
    news_list = []
    try:
        url = "https://finance.sina.com.cn/money/"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
            # 提取标题
            pattern = r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>([^<]{6,60})</a>'
            matches = re.findall(pattern, html)
            
            for href, title in matches:
                title = unescape(title).strip()
                if title and len(title) > 5 and 'javascript' not in href.lower():
                    news_list.append({
                        'title': title,
                        'source': '新浪财经',
                        'url': href if href.startswith('http') else 'https://finance.sina.com.cn' + href
                    })
    except Exception as e:
        print(f"新浪财经抓取失败: {e}")
    
    return news_list[:20]

def fetch_eastmoney():
    """抓取东方财富"""
    news_list = []
    try:
        url = "https://news.eastmoney.com/cjdt.htm"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
            pattern = r'<a[^>]*title=["\']([^"\']+)["\'][^>]*href=["\']([^"\']+)["\']'
            matches = re.findall(pattern, html)
            
            for title, href in matches:
                title = unescape(title).strip()
                if title and len(title) > 5:
                    news_list.append({
                        'title': title,
                        'source': '东方财富',
                        'url': href if href.startswith('http') else 'https://news.eastmoney.com' + href
                    })
    except Exception as e:
        print(f"东方财富抓取失败: {e}")
    
    return news_list[:20]

def extract_international_keywords(news_list):
    """提取国际热点关键词"""
    keywords = set()
    
    # 国际关键词模式
    patterns = [
        # 军事/地缘
        r'(乌克兰|俄罗斯|中东|伊朗|以色列|哈马斯|胡塞|北约|朝鲜|台海|南海|红海|霍尔木兹)',
        # 经济/金融
        r'(美联储|欧洲央行|央行|降息|加息|GDP|通胀|CPI|非农|汇率|美元|黄金|原油|石油)',
        # 重大事件
        r'(战争|冲突|制裁|峰会|选举|协议|谈判|停火|增兵|军演)',
        # 关键人物
        r'(特朗普|普京|马斯克|拜登|泽连斯基)'
    ]
    
    for news in news_list:
        title = news.get('title', '')
        for pattern in patterns:
            matches = re.findall(pattern, title)
            keywords.update(matches)
    
    return list(keywords)[:15]

def main():
    print("=" * 60)
    print("【实时热点抓取系统】启动")
    print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    all_news = []
    
    print("\n[1] 抓取新浪财经...")
    sina_news = fetch_sina_finance()
    all_news.extend(sina_news)
    print(f"    获取 {len(sina_news)} 条")
    
    print("\n[2] 抓取东方财富...")
    em_news = fetch_eastmoney()
    all_news.extend(em_news)
    print(f"    获取 {len(em_news)} 条")
    
    # 去重
    seen = set()
    unique_news = []
    for news in all_news:
        key = news['title'][:20]
        if key not in seen:
            seen.add(key)
            unique_news.append(news)
    
    # 提取关键词
    keywords = extract_international_keywords(unique_news)
    
    # 保存
    os.makedirs("./OpenClaw/实时热点", exist_ok=True)
    cache = {
        'update_time': datetime.now().isoformat(),
        'keywords': keywords,
        'news': unique_news[:30]
    }
    
    with open("./OpenClaw/实时热点/热点.json", 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
    
    # 输出
    print("\n" + "=" * 60)
    print("【实时热点已更新】")
    print("=" * 60)
    
    print("\n国际热点关键词:")
    for i, kw in enumerate(keywords, 1):
        print(f"  {i}. {kw}")
    
    print(f"\n共抓取 {len(unique_news)} 条新闻")
    print("缓存已保存: ./OpenClaw/实时热点/热点.json")
    
    print("\n【素材下载触发】")
    print(f"准备下载 {len(keywords)} 个热点的视频素材...")
    
    return keywords

if __name__ == "__main__":
    main()