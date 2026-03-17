#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='ignore')
"""
财经新闻抓取脚本 - 增强版
目标：从可访问的财经网站抓取头条新闻
"""

import urllib.request
import re
import json
from datetime import datetime
from html import unescape

def fetch_hexun():
    """和讯网财经新闻"""
    news_list = []
    try:
        url = "https://news.hexun.com/jr/index.html"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
            # 提取标题和链接
            # 格式: <a href="..." target="_blank">标题</a>
            pattern = r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>([^<]{4,50})</a>'
            matches = re.findall(pattern, html)
            
            for href, title in matches[:15]:
                title = unescape(title).strip()
                if title and len(title) > 5 and 'javascript' not in href.lower():
                    news_list.append({
                        'title': title,
                        'url': href if href.startswith('http') else 'https://news.hexun.com' + href,
                        'source': '和讯网',
                        'time': datetime.now().strftime('%Y-%m-%d %H:%M')
                    })
    except Exception as e:
        print(f"和讯网抓取失败: {e}")
    
    return news_list

def fetch_eastmoney():
    """东方财富网新闻"""
    news_list = []
    try:
        # 东方财富财经新闻接口
        url = "https://news.eastmoney.com/cjdt.htm"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
            # 提取新闻标题
            pattern = r'<a[^>]*title=["\']([^"\']+)["\'][^>]*href=["\']([^"\']+)["\']'
            matches = re.findall(pattern, html)
            
            for title, href in matches[:15]:
                title = unescape(title).strip()
                if title and len(title) > 5:
                    news_list.append({
                        'title': title,
                        'url': href if href.startswith('http') else 'https://news.eastmoney.com' + href,
                        'source': '东方财富',
                        'time': datetime.now().strftime('%Y-%m-%d %H:%M')
                    })
    except Exception as e:
        print(f"东方财富抓取失败: {e}")
    
    return news_list

def fetch_sina():
    """新浪财经"""
    news_list = []
    try:
        url = "https://finance.sina.com.cn/money/"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
            # 提取新闻链接和标题 - 简化正则
            pattern = r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>([^<]{6,60})</a>'
            matches = re.findall(pattern, html)
            
            seen = set()
            for href, title in matches:
                title = unescape(title).strip()
                if title and len(title) > 5 and title not in seen:
                    seen.add(title)
                    news_list.append({
                        'title': title,
                        'url': href if href.startswith('http') else 'https://finance.sina.com.cn' + href,
                        'source': '新浪财经',
                        'time': datetime.now().strftime('%Y-%m-%d %H:%M')
                    })
    except Exception as e:
        print(f"新浪财经抓取失败: {e}")
    
    return news_list[:10]

def fetch_cfi():
    """中国金融新闻网"""
    news_list = []
    try:
        url = "https://www.financialnews.com.cn/cj/index.html"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
            # 提取标题
            pattern = r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>([^<]{4,50})</a>'
            matches = re.findall(pattern, html)
            
            for href, title in matches[:10]:
                title = unescape(title).strip()
                if title and len(title) > 5 and 'index' not in title.lower():
                    news_list.append({
                        'title': title,
                        'url': href if href.startswith('http') else 'https://www.financialnews.com.cn' + href,
                        'source': '金融时报',
                        'time': datetime.now().strftime('%Y-%m-%d %H:%M')
                    })
    except Exception as e:
        print(f"金融时报抓取失败: {e}")
    
    return news_list

def deduplicate(news_list):
    """去重（基于标题相似度）"""
    seen = set()
    unique = []
    for news in news_list:
        # 简单去重：标题前20个字符
        key = news['title'][:20].lower()
        if key not in seen:
            seen.add(key)
            unique.append(news)
    return unique

def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 开始抓取财经新闻...\n")
    
    all_news = []
    
    print("📰 抓取和讯网...")
    all_news.extend(fetch_hexun())
    print(f"   获取 {len(all_news)} 条\n")
    
    print("📰 抓取东方财富...")
    before = len(all_news)
    all_news.extend(fetch_eastmoney())
    print(f"   新增 {len(all_news) - before} 条\n")
    
    print("📰 抓取新浪财经...")
    before = len(all_news)
    all_news.extend(fetch_sina())
    print(f"   新增 {len(all_news) - before} 条\n")
    
    print("📰 抓取金融时报...")
    before = len(all_news)
    all_news.extend(fetch_cfi())
    print(f"   新增 {len(all_news) - before} 条\n")
    
    # 去重
    unique_news = deduplicate(all_news)
    
    print(f"总计获取 {len(all_news)} 条，去重后 {len(unique_news)} 条\n")
    
    # 保存到文件
    output = {
        'timestamp': datetime.now().isoformat(),
        'count': len(unique_news),
        'news': unique_news[:20]  # 最多保留20条
    }
    
    output_path = "C:/Users/Administrator/.openclaw-autoclaw/workspace/reports/latest_news.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已保存到: {output_path}\n")
    
    # 打印前10条
    print("="*60)
    print("📊 今日财经热点（前10条）:")
    print("="*60)
    for i, news in enumerate(unique_news[:10], 1):
        print(f"{i}. [{news['source']}] {news['title']}")
    print()
    
    return unique_news

if __name__ == "__main__":
    main()
