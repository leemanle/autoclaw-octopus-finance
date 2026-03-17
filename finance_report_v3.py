#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
财经快报生成器 - 带深度分析
使用东方财富API获取财经新闻
"""
import sys
import io
import json
import os
import re

# 设置输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='ignore')

import urllib.request
import ssl
from datetime import datetime

# SSL设置
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def fetch_eastmoney_news():
    """东方财富财经新闻"""
    news_list = []
    try:
        # 财经新闻接口
        url = "https://newsapi.eastmoney.com/kuaixun/v1/getlist_102_ajaxResult_50_1_.html"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Referer': 'https://finance.eastmoney.com/'
        })
        
        with urllib.request.urlopen(req, timeout=15, context=ssl_context) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
            # 解析JSON
            match = re.search(r'\{.*\}', html, re.DOTALL)
            if match:
                data = json.loads(match.group())
                if 'LivesList' in data:
                    for item in data['LivesList'][:30]:
                        news_list.append({
                            'title': item.get('Title', ''),
                            'url': f"https://finance.eastmoney.com{aitem.get('Url', '')}" if item.get('Url') else '',
                            'source': '东方财富',
                            'time': item.get('ShowTime', '')[-5:] if item.get('ShowTime') else '',
                            'digest': item.get('Digest', '')
                        })
    except Exception as e:
        print(f"东方财富抓取失败: {e}")
    
    return news_list

def fetch_sina_news():
    """新浪财经"""
    news_list = []
    try:
        url = "https://interface.sina.cn/news/flash/getDataByCategoryIdList-api-finance-105-0-0-50.d.html"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        })
        
        with urllib.request.urlopen(req, timeout=15, context=ssl_context) as resp:
            data = json.loads(resp.read().decode('utf-8', errors='ignore'))
            
            for item in data.get('result', [])[:20]:
                news_list.append({
                    'title': item.get('title', ''),
                    'url': item.get('url', ''),
                    'source': '新浪财经',
                    'time': item.get('ctime', ''),
                    'digest': item.get('digest', '')
                })
    except Exception as e:
        print(f"新浪财经抓取失败: {e}")
    
    return news_list

def fetch_cls_news():
    """财联社新闻"""
    news_list = []
    try:
        url = "https://www.cls.cn/nodeapi/updateTelegraph"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        })
        
        with urllib.request.urlopen(req, timeout=15, context=ssl_context) as resp:
            data = json.loads(resp.read().decode('utf-8', errors='ignore'))
            
            for item in data.get('data', {}).get('list', [])[:20]:
                news_list.append({
                    'title': item.get('title', ''),
                    'url': item.get('wapurl', ''),
                    'source': '财联社',
                    'time': datetime.fromtimestamp(item.get('utime', 0)).strftime('%H:%M'),
                    'digest': item.get('summary', '')
                })
    except Exception as e:
        print(f"财联社抓取失败: {e}")
    
    return news_list

def analyze_impact(news_list):
    """深度分析：识别板块和个股影响"""
    impacts = {
        '政策利好': [],
        '行业利好': [],
        '公司动态': [],
        '风险提示': []
    }
    
    # 关键词库
    patterns = {
        # 政策类
        ('降息', '降准', '麻辣粉', 'MLF', 'SLF', '量化宽松'): {'板块': '金融', '个股': '银行、保险、券商', 'type': '政策利好'},
        ('新能源', '光伏', '风电', '绿电'): {'板块': '新能源', '个股': '宁德时代、比亚迪、隆基绿能', 'type': '行业利好'},
        ('人工智能', 'AI', '大模型', '算力'): {'板块': 'AI/科技', '个股': '科大讯飞、寒武纪、海光信息', 'type': '行业利好'},
        ('半导体', '芯片', '集成电路'): {'板块': '半导体', '个股': '中芯国际、北方华创', 'type': '行业利好'},
        ('房地产', '地产', '购房'): {'板块': '房地产', '个股': '万科A、保利发展', 'type': '政策利好'},
        ('基建', '水利', '管网'): {'板块': '基建', '个股': '中国建筑、中国交建', 'type': '政策利好'},
        ('消费', '餐饮', '旅游', '零售'): {'板块': '消费', '个股': '茅台、五粮液', 'type': '行业利好'},
        ('医药', '创新药', '医疗器械'): {'板块': '医药', '个股': '恒瑞医药、片仔癀', 'type': '行业利好'},
        ('军工', '航天', '航空'): {'板块': '军工', '个股': '中航沈飞、航发动力', 'type': '行业利好'},
        ('数字经济', '云计算', '大数据'): {'板块': '数字经济', '个股': '浪潮信息、用友网络', 'type': '政策利好'},
        ('出口', '关税', '贸易'): {'板块': '外贸', '个股': '贸易类公司', 'type': '政策利好'},
        
        # 公司类
        ('业绩增长', '业绩预增', '扭亏'): {'板块': '业绩', '个股': '相关公司', 'type': '公司动态'},
        ('定增', '增发', '募资'): {'板块': '融资', '个股': '特定公司', 'type': '公司动态'},
        ('回购', '增持'): {'板块': '回购', '个股': '增持公司', 'type': '公司动态'},
        ('分红', '送转'): {'板块': '分红', '个股': '高股息公司', 'type': '公司动态'},
        
        # 风险类
        ('下跌', '暴跌', '大跌'): {'板块': '市场', 'type': '风险提示'},
        ('亏损', '盈利预警'): {'板块': '业绩', 'type': '风险提示'},
        ('退市', 'ST', '风险'): {'板块': '退市风险', 'type': '风险提示'},
        ('减持', '抛售'): {'板块': '减持', 'type': '风险提示'},
    }
    
    for news in news_list:
        title = news.get('title', '')
        if not title:
            continue
            
        matched = False
        for keywords, impact in patterns.items():
            if any(kw in title for kw in keywords):
                category = impact['type']
                impacts[category].append({
                    'title': title,
                    'source': news.get('source', ''),
                    'time': news.get('time', ''),
                    'impact': impact
                })
                matched = True
                break
        
        # 默认归类到要闻
        if not matched and len(impacts['政策利好']) + len(impacts['行业利好']) < 15:
            impacts['政策利好'].append({
                'title': title,
                'source': news.get('source', ''),
                'time': news.get('time', ''),
                'impact': {'板块': '综合', '个股': ''}
            })
    
    return impacts

def generate_report(news_list, impacts):
    """生成结构化报告"""
    now = datetime.now()
    
    # 确定时段
    hour = now.hour
    if 7 <= hour < 9:
        period = "早盘"
    elif 9 <= hour < 12:
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
⏰ 发布时间：{now.strftime('%Y-%m-%d %H:%M')}

## 📰 财经要闻 ({len(news_list)}条)

"""
    
    # 要闻列表
    for i, news in enumerate(news_list[:12], 1):
        report += f"**{i}.** {news.get('title', '')}\n"
        report += f"   - 来源：{news.get('source', '')} | 时间：{news.get('time', '')}\n\n"
    
    # 深度分析
    report += "\n---\n\n## 🔍 深度分析\n\n"
    
    # 政策/行业利好
    if impacts['政策利好'] or impacts['行业利好']:
        report += "### ✅ 利好板块\n\n"
        
        # 按板块分组
        sector_news = {}
        for item in impacts['政策利好'] + impacts['行业利好']:
            sector = item['impact'].get('板块', '综合')
            if sector not in sector_news:
                sector_news[sector] = []
            sector_news[sector].append(item)
        
        for sector, items in sorted(sector_news.items(), key=lambda x: -len(x[1]))[:6]:
            report += f"**📊 {sector}**\n"
            for item in items[:3]:
                report += f"- {item['title'][:60]}...\n"
                if item['impact'].get('个股'):
                    report += f"  → 个股：{item['impact'].get('个股')}\n"
            report += "\n"
    
    # 公司动态
    if impacts['公司动态']:
        report += "### 🏢 公司动态\n\n"
        for item in impacts['公司动态'][:5]:
            report += f"- {item['title'][:70]}\n"
            if item['impact'].get('个股'):
                report += f"  → {item['impact'].get('个股')}\n"
        report += "\n"
    
    # 风险提示
    if impacts['风险提示']:
        report += "### ⚠️ 风险提示\n\n"
        for item in impacts['风险提示'][:5]:
            report += f"- {item['title'][:70]}\n"
        report += "\n"
    
    # 板块机会汇总
    report += "\n---\n\n## 🧭 重点板块机会\n\n"
    report += "| 板块 | 关注度 | 驱动逻辑 |\n"
    report += "|------|--------|----------|\n"
    
    sector_count = {}
    for item in impacts['政策利好'] + impacts['行业利好']:
        sector = item['impact'].get('板块', '其他')
        sector_count[sector] = sector_count.get(sector, 0) + 1
    
    for sector, count in sorted(sector_count.items(), key=lambda x: -x[1])[:8]:
        stars = '⭐' * min(count, 4)
        report += f"| {sector} | {stars} | 政策/行业 |\n"
    
    report += f"""
---
💡 **投资提示**：以上分析仅供参考，不构成投资建议。请结合基本面和市场情绪综合判断。

🤖 *本报告由AI自动生成* | 数据来源：东方财富、新浪、财联社
"""
    
    return report

def save_report(report):
    """保存报告"""
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    hour_str = now.strftime('%H')
    
    report_dir = f"C:/Users/Administrator/.openclaw-autoclaw/workspace/reports/{date_str}"
    os.makedirs(report_dir, exist_ok=True)
    
    report_path = f"{report_dir}/{hour_str}.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ 报告已保存: {report_path}")
    return report_path

def send_to_feishu(report):
    """发送到飞书（如果可用）"""
    try:
        import requests
        # 这里需要飞书webhook或API
        # 暂时跳过
        pass
    except:
        pass

def main():
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 财经快报生成器启动\n")
    
    # 抓取新闻
    all_news = []
    
    print("📰 抓取财联社新闻...")
    all_news.extend(fetch_cls_news())
    
    print("📰 抓取新浪财经...")
    all_news.extend(fetch_sina_news())
    
    print("📰 抓取东方财富...")
    all_news.extend(fetch_eastmoney_news())
    
    # 去重
    seen = set()
    unique = []
    for news in all_news:
        key = news.get('title', '')[:20]
        if key and key not in seen:
            seen.add(key)
            unique.append(news)
    
    print(f"✅ 共获取 {len(unique)} 条新闻\n")
    
    # 深度分析
    impacts = analyze_impact(unique)
    
    # 生成报告
    report = generate_report(unique, impacts)
    
    # 保存报告
    report_path = save_report(report)
    
    # 打印报告前100行
    print("\n" + "="*60)
    print("报告预览:")
    print("="*60)
    lines = report.split('\n')
    for line in lines[:80]:
        print(line)
    print("..." if len(lines) > 80 else "")
    
    return report_path

if __name__ == "__main__":
    main()