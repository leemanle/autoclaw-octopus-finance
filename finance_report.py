#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
财经快报定时任务 - 由 Heartbeat 触发
运行时间: 09:00, 12:00, 15:00, 18:00, 21:00
"""
import sys
import io
import json
import os
from datetime import datetime

# 设置编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='ignore')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='ignore')

# 工作目录
WORKSPACE = r"C:\Users\Administrator\.openclaw-autoclaw\workspace"
NEWS_FILE = os.path.join(WORKSPACE, "reports", "latest_news.json")
LATEST_REPORT = os.path.join(WORKSPACE, "reports", "latest_report.md")

def get_news():
    """读取最新新闻"""
    if os.path.exists(NEWS_FILE):
        try:
            with open(NEWS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return []

def generate_report(time_slot):
    """生成快报"""
    news = get_news()
    items = news.get('news', [])[:10]
    
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    report = f"""# 📊 财经快报 - {time_slot}
**生成时间**: {now}

---

## 🔥 今日财经热点

"""
    for i, item in enumerate(items, 1):
        title = item.get('title', '无标题')
        source = item.get('source', '未知')
        url = item.get('url', '')
        report += f"{i}. [{title}]({url}) - {source}\n"
    
    report += f"""
---

*自动生成 by AutoClaw*
"""
    return report

def main():
    if len(sys.argv) < 2:
        print("用法: python finance_report.py <time_slot>")
        print("示例: python finance_report.py 早盘")
        sys.exit(1)
    
    time_slot = sys.argv[1]
    report = generate_report(time_slot)
    
    # 保存报告
    date_str = datetime.now().strftime('%Y-%m-%d')
    report_dir = os.path.join(WORKSPACE, "reports", date_str)
    os.makedirs(report_dir, exist_ok=True)
    
    time_map = {'早盘': '09', '午间': '12', '收盘': '15', '晚间': '18', '夜盘': '21'}
    time_file = time_map.get(time_slot, '00')
    
    report_path = os.path.join(report_dir, f"{time_file}.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ 快报已生成: {report_path}")
    print(report)

if __name__ == "__main__":
    main()
