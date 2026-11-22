"""在 9 月食品安全表的月调度\"本月总结\"里加一条 \"9.23 参加宣城市快检培训\"，不写具体批次数字。"""
from docx import Document

PATH = r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表9月2026.docx'
doc = Document(PATH)

tbl = doc.tables[11]
# R1C2 本月总结
cell = tbl.rows[1].cells[2]
old = cell.text.strip()
print('修改前:')
print(old[:200])

new = old.replace(
    '应急联络表更新 七条主线开展日管控 8 次',
    '应急联络表更新+9.23 参加宣城市快检培训 1 人次 八条主线开展日管控 8 次',
)

print()
print('修改后:')
print(new[:200])
print()

# 替换第一段
p = cell.paragraphs[0]
if p.runs:
    p.runs[0].text = new
    for r in p.runs[1:]:
        r.text = ''
else:
    p.add_run(new)

doc.save(PATH)
print('已保存')