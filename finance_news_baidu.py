# -*- coding: utf-8 -*-
"""财经新闻获取 - 从百度热搜中筛选财经类"""
import urllib.request
import json
import re
import ssl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='ignore')

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def fetch_baidu_hot():
    """获取百度热搜并筛选财经类"""
    try:
        url = 'https://top.baidu.com/board?tab=realtime'
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=15, context=ssl_context) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
            # 提取JSON数据
            pattern = r'json\.set\("hotList",\s*(\[.*?\])\);'
            match = re.search(pattern, html, re.DOTALL)
            if match:
                data = json.loads(match.group(1))
                return data
    except Exception as e:
        print(f"百度抓取失败: {e}")
    return []

def filter_finance_news(hot_list):
    """筛选财经相关热搜"""
    # 财经关键词
    finance_keywords = [
        '股', 'A股', '港股', '美股', '股市', '大盘', '指数', '涨停', '跌停',
        '基金', '私募', '公募', 'ETF',
        '央行', '降息', '降准', '加息', '利率', '货币政策',
        'GDP', 'CPI', 'PPI', 'PMI', '经济', '通胀', '就业',
        '房地产', '房价', '地产', '购房',
        '新能源', '光伏', '风电', '锂电', '电池', '电动车', '汽车',
        'AI', '人工智能', '芯片', '半导体', '科技', '互联网',
        '银行', '保险', '券商', '金融',
        '外贸', '出口', '进口', '关税', '汇率', '人民币', '美元',
        '油价', '石油', '天然气', '黄金', '大宗商品',
        '财报', '业绩', '盈利', '亏损', '分红', '回购',
        'IPO', '上市', '申购', '新股',
        '特朗普', '拜登', '美联储', 'G7', '欧盟',
    ]
    
    finance_news = []
    other_news = []
    
    for item in hot_list:
        title = item.get('hotScoreDoc', {}).get('title', '')
        if not title:
            title = item.get('hotScoreDoc', {}).get('content', '')
        
        is_finance = any(kw in title for kw in finance_keywords)
        
        news_item = {
            'title': title,
            'hotScore': item.get('hotScoreDoc', {}).get('hotScore', ''),
            'url': item.get('hotScoreDoc', {}).get('url', '')
        }
        
        if is_finance:
            finance_news.append(news_item)
        else:
            other_news.append(news_item)
    
    return finance_news, other_news

if __name__ == '__main__':
    print("=" * 50)
    print("百度热搜财经资讯抓取")
    print("=" * 50)
    
    hot_list = fetch_baidu_hot()
    
    if hot_list:
        finance_news, other_news = filter_finance_news(hot_list)
        
        print(f"\n📈 财经相关热搜 ({len(finance_news)}条):")
        for i, news in enumerate(finance_news[:15], 1):
            print(f"  {i}. {news['title']}")
        
        print(f"\n📰 其他热点 ({len(other_news)}条):")
        for i, news in enumerate(other_news[:10], 1):
            print(f"  {i}. {news['title']}")
    else:
        print("未获取到数据")
