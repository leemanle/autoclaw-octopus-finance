# -*- coding: utf-8 -*-
import urllib.request
import json
import re
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 抓取百度热搜
def fetch_baidu_hot():
    try:
        url = 'https://top.baidu.com/board?tab=realtime'
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # 提取JSON数据
            pattern = r'json\.set\("hotList",\s*(\[.*?\])\);'
            match = re.search(pattern, html)
            if match:
                return json.loads(match.group(1))
    except Exception as e:
        print(f"百度抓取失败: {e}")
    return []

# 抓取今日头条
def fetch_toutiao_hot():
    try:
        url = 'https://www.toutiao.com/hot-event/hot_board/?origin=hot_word'
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('data', [])
    except Exception as e:
        print(f"头条抓取失败: {e}")
    return []

# 抓取微博热搜(备用)
def fetch_weibo_fallback():
    try:
        url = 'https://weibo.com/ajax/feed/favoritetimeline?is_all=1'
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0',
            'Cookie': ''  # 需要登录cookie
        })
        with urllib.request.urlopen(req, timeout=5) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except:
        pass
    return None

print("="*60)
print("【实时热点 - 国际军事类】")
print("="*60)

# 尝试百度
hot_list = fetch_baidu_hot()
if not hot_list:
    hot_list = fetch_toutiao_hot()

# 过滤国际军事
military = ['俄罗斯', '乌克兰', '中东', '伊朗', '以色列', '美国', '北约', '军事', '战争', '冲突', 
            '导弹', '普京', '朝鲜', '台海', '红海', '胡塞', '泽连斯基', '国防', '军队', '演习', 
            '航母', '核武器', '美军', '俄军', '伊朗', '沙特', '土耳其', '欧洲', '联合国', 'G7']

count = 0
mil_list = []

for item in hot_list:
    if count >= 12:
        break
    
    # 提取标题
    if 'word' in item:
        word = item.get('word', '')
    elif 'Title' in item:
        word = item.get('Title', '')
    else:
        word = str(item)
    
    if any(kw in word for kw in military):
        count += 1
        print(f"{count}. {word}")
        mil_list.append(word)

if count == 0:
    print("暂无国际军事类热搜，显示其他热点:")
    for i, item in enumerate(hot_list[:20]):
        if 'word' in item:
            print(f"{i+1}. {item.get('word', '')}")
        elif 'Title' in item:
            print(f"{i+1}. {item.get('Title', '')}")

print("="*60)
print(f"共 {count} 条国际军事热点")
print("="*60)