import urllib.request
import json
import re
import sys

# 设置输出编码
sys.stdout.reconfigure(encoding='utf-8')

# 获取财经新闻
url = 'https://newsapi.eastmoney.com/kuaixun/v1/getlist_102_ajaxResult_50_1_.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req, timeout=10)
html = response.read().decode('utf-8')

# 提取新闻标题
pattern = r'"title":"([^"]+)"'
matches = re.findall(pattern, html)

print('=== 今日财经大事 ===')
for i, title in enumerate(matches[:15], 1):
    title = title.replace('\\u0026', '&').replace('\\/', '/')
    print(f'{i}. {title}')
