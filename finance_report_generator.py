#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
财经快报生成器 - 带深度分析
定时抓取全网财经新闻，生成分析报告，推送到飞书
"""
import sys
import io
import json
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='ignore')

import urllib.request
import re
from datetime import datetime
from html import unescape
import ssl

# 创建SSL上下文
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def fetch_news(url, source_name, headers=None):
    """通用新闻抓取"""
    news_list = []
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    headers = headers or default_headers
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15, context=ssl_context) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
            # 提取标题链接
            pattern = r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>([^<]{4,80})</a>'
            matches = re.findall(pattern, html)
            
            for href, title in matches[:20]:
                title = unescape(title).strip()
                if title and len(title) > 6 and 'javascript' not in href.lower():
                    full_url = href if href.startswith('http') else url.split('/')[0] + '//' + url.split('/')[2] + href
                    news_list.append({
                        'title': title,
                        'url': full_url,
                        'source': source_name,
                        'time': datetime.now().strftime('%H:%M')
                    })
    except Exception as e:
        print(f"{source_name} 抓取失败: {e}")
    
    return news_list

def fetch_all_news():
    """抓取全网财经新闻"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 开始抓取财经新闻...")
    
    all_news = []
    
    # 东方财富
    print("  📰 东方财富...")
    all_news.extend(fetch_news("https://news.eastmoney.com/cjdt.htm", "东方财富"))
    
    # 和讯网
    print("  📰 和讯网...")
    all_news.extend(fetch_news("https://news.hexun.com/jr/index.html", "和讯网"))
    
    # 新浪财经
    print("  📰 新浪财经...")
    all_news.extend(fetch_news("https://finance.sina.com.cn/news/", "新浪财经"))
    
    # 去重
    seen = set()
    unique = []
    for news in all_news:
        key = news['title'][:25].lower()
        if key not in seen:
            seen.add(key)
            unique.append(news)
    
    print(f"  ✅ 共获取 {len(unique)} 条新闻\n")
    return unique[:30]

def analyze_news(news_list):
    """深度分析新闻，识别板块和个股利好"""
    analysis = {
        '政策利好': [],
        '行业利好': [],
        '公司利好': [],
        '风险提示': []
    }
    
    # 关键词映射到板块/个股
    keywords_map = {
        # 政策类
        '降息': {'板块': '银行、保险、房地产', '利好': '银行股、保险股'},
        '降准': {'板块': '银行、保险、券商', '利好': '银行股、保险股'},
        '加息': {'板块': '银行', '风险': '高负债行业'},
        '麻辣粉': {'板块': '银行', '利好': '商业银行'},
        'MLF': {'板块': '银行', '利好': '商业银行'},
        '消费': {'板块': '消费', '利好': '白酒、食品饮料'},
        '新能源': {'板块': '新能源车、光伏', '利好': '比亚迪、宁德时代、隆基绿能'},
        '半导体': {'板块': '半导体', '利好': '中芯国际、寒武纪'},
        '人工智能': {'板块': 'AI、人工智能', '利好': '科大讯飞、寒武纪'},
        '房地产': {'板块': '房地产', '利好': '万科A、保利发展'},
        '基建': {'板块': '基建', '利好': '中国建筑、中国交建'},
        '军工': {'板块': '军工', '利好': '中航沈飞、航发动力'},
        '医药': {'板块': '医药', '利好': '恒瑞医药、片仔癀'},
        '数字经济': {'板块': '数字经济', '利好': '云计算、大数据'},
        '乡村振兴': {'板块': '农业', '利好': '北大荒、隆平高科'},
        
        # 公司类
        '业绩增长': {'板块': '业绩预增', '利好': '对应个股'},
        '业绩预增': {'板块': '业绩预增', '利好': '对应个股'},
        '定增': {'板块': '增发', '利好': '特定个股'},
        '回购': {'板块': '回购', '利好': '对应公司'},
        '分红': {'板块': '分红', '利好': '高股息个股'},
        '重组': {'板块': '并购重组', '利好': '相关个股'},
        '中标': {'板块': '基建中标', '利好': '中标公司'},
    }
    
    for news in news_list:
        title = news['title']
        found = False
        
        for keyword, info in keywords_map.items():
            if keyword in title:
                category = '风险提示' if '风险' in info else '政策利好'
                if '风险' in str(info):
                    category = '风险提示'
                elif '板块' in info:
                    category = '政策利好'
                
                analysis[category].append({
                    'title': title,
                    'source': news['source'],
                    'time': news['time'],
                    'impact': info
                })
                found = True
                break
        
        if not found:
            # 检查是否是中性偏空
            if any(k in title for k in ['下跌', '暴跌', '亏损', '退市', '减持', '风险']):
                analysis['风险提示'].append({
                    'title': title,
                    'source': news['source'],
                    'time': news['time'],
                    'impact': {'板块': '注意风险', '利好': ''}
                })
    
    return analysis

def generate_report(news_list, analysis):
    """生成报告"""
    now = datetime.now()
    hour = now.hour
    
    # 确定时段
    if 7 <= hour < 12:
        period = "上午"
    elif 12 <= hour < 14:
        period = "午间"
    elif 14 <= hour < 18:
        period = "下午"
    elif 18 <= hour < 21:
        period = "晚间"
    elif 21 <= hour < 24:
        period = "夜盘"
    else:
        period = "凌晨"
    
    report = f"""# 📈 {now.strftime('%Y-%m-%d')} {period}财经快报

---
⏰ 生成时间：{now.strftime('%Y-%m-%d %H:%M')}

## 📰 今日要闻 ({len(news_list)}条)

"""
    
    # 添加新闻列表
    for i, news in enumerate(news_list[:15], 1):
        report += f"**{i}.** {news['title']}\n"
        report += f"   - 来源：{news['source']} | 时间：{news['time']}\n\n"
    
    # 添加深度分析
    report += "\n---\n\n## 🔍 深度分析\n\n"
    
    if analysis['政策利好']:
        report += "### ✅ 政策/行业利好\n\n"
        for item in analysis['政策利好'][:8]:
            report += f"**• {item['title']}**\n"
            report += f"  - 涉及板块：{item['impact'].get('板块', '待确认')}\n"
            report += f"  - 个股利好：{item['impact'].get('利好', '待确认')}\n"
            report += f"  - 来源：{item['source']}\n\n"
    
    if analysis['公司利好']:
        report += "### 🏢 公司动态\n\n"
        for item in analysis['公司利好'][:5]:
            report += f"**• {item['title']}**\n"
            report += f"  - 影响：{item['impact'].get('利好', '待确认')}\n"
            report += f"  - 来源：{item['source']}\n\n"
    
    if analysis['风险提示']:
        report += "### ⚠️ 风险提示\n\n"
        for item in analysis['风险提示'][:5]:
            report += f"**• {item['title']}**\n"
            report += f"  - 来源：{item['source']}\n\n"
    
    # 热门板块判断
    report += "\n---\n\n## 🧭 板块机会\n\n"
    report += "| 板块 | 关注度 | 逻辑 |\n"
    report += "|------|--------|------|\n"
    
    # 简单统计
    sectors = {}
    for item in analysis['政策利好']:
        sector = item['impact'].get('板块', '其他')
        sectors[sector] = sectors.get(sector, 0) + 1
    
    for sector, count in sorted(sectors.items(), key=lambda x: -x[1])[:6]:
        report += f"| {sector} | {'⭐' * min(count, 3)} | 政策推动 |\n"
    
    report += f"""
---
📊 *本报告由AI自动生成，数据仅供参考，不构成投资建议*
"""
    
    return report

def save_report(report, period):
    """保存报告"""
    date_str = datetime.now().strftime('%Y-%m-%d')
    hour_str = datetime.now().strftime('%H')
    
    report_dir = f"C:/Users/Administrator/.openclaw-autoclaw/workspace/reports/{date_str}"
    os.makedirs(report_dir, exist_ok=True)
    
    report_path = f"{report_dir}/{hour_str}.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"📄 报告已保存: {report_path}")
    return report_path

def main():
    # 抓取新闻
    news_list = fetch_all_news()
    
    # 深度分析
    analysis = analyze_news(news_list)
    
    # 生成报告
    report = generate_report(news_list, analysis)
    
    # 保存报告
    report_path = save_report(report, "daily")
    
    # 打印报告
    print("\n" + "="*60)
    print(report)
    print("="*60)
    
    return report_path

if __name__ == "__main__":
    main()