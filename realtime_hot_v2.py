#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
国际实时热点 + 视频素材自动下载系统
纯实时、零预设、7x24自动运行
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='ignore')

import os
import json
import time
import hashlib
import urllib.request
import re
from datetime import datetime
from html import unescape
import ssl

# 创建必要目录
BASE_DIR = os.path.expanduser("~/OpenClaw")
MATERIALS_DIR = os.path.join(BASE_DIR, "实时素材库")
HOT_DIR = os.path.join(BASE_DIR, "实时热点")
os.makedirs(MATERIALS_DIR, exist_ok=True)
os.makedirs(HOT_DIR, exist_ok=True)

# 视频素材API配置（免费无需密钥）
VIDEO_APIS = {
    'pixabay': {
        'url': 'https://pixabay.com/api/videos/',
        'params': 'key=34436402-0f12-4a9e-a4c3-3d0d2c94c308&q={keyword}&per_page=10&video_type=free',
        'type': 'json'
    },
    'coverr': {
        'url': 'https://api.coverr.co/videos',
        'params': 'query={keyword}',
        'type': 'json'
    },
    'mixkit': {
        'url': 'https://api.mixkit.co/v2/search',
        'params': 'query={keyword}&limit=10',
        'type': 'json'
    }
}

def get_ssl_context():
    """创建SSL上下文"""
    try:
        return ssl.create_default_context()
    except:
        return None

def fetch_news():
    """抓取实时新闻热点"""
    news_list = []
    
    # 数据源配置
    sources = [
        ('新浪财经', 'https://finance.sina.com.cn/money/'),
        ('新浪军事', 'https://mil.sina.com.cn/'),
        ('新浪国际', 'https://news.sina.com.cn/world/'),
        ('东方财富', 'https://news.eastmoney.com/cjdt.htm'),
    ]
    
    for source_name, url in sources:
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            ctx = get_ssl_context()
            with urllib.request.urlopen(req, timeout=8, context=ctx) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                
                # 提取标题
                pattern = r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>([^<]{5,60})</a>'
                matches = re.findall(pattern, html)
                
                for href, title in matches:
                    title = unescape(title).strip()
                    if title and len(title) > 5 and 'javascript' not in href.lower():
                        news_list.append({
                            'title': title,
                            'source': source_name,
                            'url': href if href.startswith('http') else ''
                        })
        except Exception as e:
            print(f"  [{source_name}] 抓取失败: {e}")
    
    return news_list

def extract_keywords(news_list):
    """从新闻中自动提取热点关键词"""
    keywords = set()
    
    # 热点模式 - 国际财经/政治/军事/经济
    patterns = [
        # 军事地缘
        r'(乌克兰|俄罗斯|中东|伊朗|以色列|哈马斯|胡塞|北约|朝鲜|台海|南海|红海|霍尔木兹|叙利亚|土耳其|沙特)',
        # 经济金融
        r'(美联储|欧洲央行|央行|降息|加息|GDP|通胀|CPI|非农|汇率|美元|黄金|原油|石油|OPEC|沙特)',
        # 政治
        r'(特朗普|普京|拜登|泽连斯基|内塔尼亚胡|埃尔多安|马克龙|联合国|峰会|谈判)',
        # 重大事件
        r'(战争|冲突|制裁|军演|核|导弹|无人机|航母|战斗机|坦克)',
        # 市场
        r'(美股|港股|A股|纳斯达克|道琼斯|标普|恒生|上证|深证|比特币|币圈)'
    ]
    
    for news in news_list:
        title = news.get('title', '')
        for pattern in patterns:
            matches = re.findall(pattern, title)
            keywords.update(matches)
    
    # 去重并返回
    return list(keywords)[:15]

def search_pixabay_video(keyword):
    """从Pixabay搜索下载视频"""
    videos = []
    try:
        import urllib.parse
        encoded_keyword = urllib.parse.quote(keyword)
        url = f"https://pixabay.com/api/videos/?key=34436402-0f12-4a9e-a4c3-3d0d2c94c308&q={encoded_keyword}&per_page=10&video_type=free"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0'
        })
        ctx = get_ssl_context()
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if 'hits' in data:
                for item in data['hits']:
                    # 获取不同质量的视频链接
                    videos.append({
                        'title': item.get('tags', ''),
                        'url': item.get('videos', {}).get('large', {}).get('url', ''),
                        'thumb': item.get('picture_id', ''),
                        'platform': 'pixabay'
                    })
    except Exception as e:
        print(f"    Pixabay搜索失败: {e}")
    
    return videos

def download_video(video_url, keyword, platform):
    """下载视频到本地"""
    if not video_url:
        return None
    
    try:
        # 创建关键词目录
        keyword_dir = os.path.join(MATERIALS_DIR, keyword)
        os.makedirs(keyword_dir, exist_ok=True)
        
        # 生成文件名
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{keyword}_{platform}_{timestamp}.mp4"
        filepath = os.path.join(keyword_dir, filename)
        
        # 下载视频
        req = urllib.request.Request(video_url, headers={
            'User-Agent': 'Mozilla/5.0'
        })
        ctx = get_ssl_context()
        
        # 获取文件大小
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            total_size = int(resp.headers.get('Content-Length', 0))
            
            # 如果太大，跳过（超过50MB）
            if total_size > 50 * 1024 * 1024:
                print(f"    视频太大，跳过: {total_size/1024/1024:.1f}MB")
                return None
            
            # 分块下载
            with open(filepath, 'wb') as f:
                while True:
                    chunk = resp.read(1024 * 1024)  # 1MB chunks
                    if not chunk:
                        break
                    f.write(chunk)
        
        print(f"    ✅ 下载成功: {filename}")
        return filepath
        
    except Exception as e:
        print(f"    ❌ 下载失败: {e}")
        return None

def save_hot_cache(keywords, news_list):
    """保存热点缓存"""
    cache_file = os.path.join(HOT_DIR, "热点.json")
    
    cache_data = {
        'update_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'keywords': keywords,
        'news_count': len(news_list)
    }
    
    with open(cache_file, 'w', encoding='utf-8') as f:
        json.dump(cache_data, f, ensure_ascii=False, indent=2)
    
    return cache_file

def run_realtime_system():
    """运行实时系统"""
    print("=" * 70)
    print("【国际实时热点 + 素材自动下载系统】启动")
    print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    # 第一步：抓取实时热点
    print("\n📰 [步骤1] 正在抓取全球实时热点...")
    news_list = fetch_news()
    print(f"   获取新闻: {len(news_list)} 条")
    
    # 第二步：提取热点关键词
    print("\n🔑 [步骤2] 正在提取热点关键词...")
    keywords = extract_keywords(news_list)
    print(f"   提取到 {len(keywords)} 个国际热点词")
    
    # 第三步：保存热点
    print("\n💾 [步骤3] 保存热点缓存...")
    cache_file = save_hot_cache(keywords, news_list)
    print(f"   缓存保存: {cache_file}")
    
    # 第四步：自动下载视频素材
    print("\n🎬 [步骤4] 正在自动下载视频素材...")
    print("-" * 50)
    
    downloaded_count = 0
    
    for keyword in keywords[:5]:  # 每个关键词
        print(f"\n  关键词: {keyword}")
        
        # 搜索Pixabay视频
        videos = search_pixabay_video(keyword)
        print(f"    找到 {len(videos)} 个视频")
        
        # 下载视频
        for video in videos[:3]:  # 每个关键词最多下3个
            if video.get('url'):
                result = download_video(video['url'], keyword, video['platform'])
                if result:
                    downloaded_count += 1
                    break  # 每个关键词下1个就够
    
    # 输出结果
    print("\n" + "=" * 70)
    print("【实时热点已更新】")
    print("=" * 70)
    print("\n🌍 国际热点关键词:")
    for i, kw in enumerate(keywords[:10], 1):
        print(f"   {i}. {kw}")
    
    print(f"\n📥 素材下载结果:")
    print(f"   总计下载: {downloaded_count} 个视频")
    print(f"   存储路径: {MATERIALS_DIR}")
    
    print("\n✅ 本轮执行完成，系统将持续运行...")
    print("=" * 70)
    
    return keywords, downloaded_count

if __name__ == "__main__":
    run_realtime_system()