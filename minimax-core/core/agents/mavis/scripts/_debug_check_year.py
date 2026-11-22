"""调试脚本：检查 9 月份 docx 中 '年 月 日' 上下文（不修）"""
import zipfile
import re

PATH = r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表9月2026.docx'

with zipfile.ZipFile(PATH) as z:
    xml = z.read('word/document.xml').decode('utf-8')

# 找 年 月 日 周围 400 字符
pattern = r'年\s+月\s+日'
matches = list(re.finditer(pattern, xml))
print(f'找到 {len(matches)} 处 年 月 日')
for i, m in enumerate(matches[:8]):
    pos = m.start()
    ctx = xml[max(0, pos-400):pos+200]
    print(f'\n=== match {i} at pos {pos} ===')
    print(ctx)
    print('---')
