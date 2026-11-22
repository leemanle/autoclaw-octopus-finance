from docx import Document

# 8 月份原版在 D:\大华市场
doc = Document(r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表8月2026.docx')
print('=== 8月 docx 中含 会议时间 的段落 ===')
for p in doc.paragraphs:
    if '会议时间' in p.text:
        prefix = p.text[:6]
        print(f'prefix={prefix!r}, full={p.text!r}')
