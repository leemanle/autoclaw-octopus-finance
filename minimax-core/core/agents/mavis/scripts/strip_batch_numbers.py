"""去掉 9 月份食品安全管控记录表里所有具体批次数字。"""
import re
from docx import Document

PATH = r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表9月2026.docx'
doc = Document(PATH)


def strip_batch(text):
    """把 '抽检叶菜 8 批次、豆类 4 批次' 改成 '抽检叶菜、豆类' 等不带具体批次的形式"""
    # 抽检xxx X 批次、yyy Y 批次、...
    # 例：抽检叶菜 8 批次、豆类 4 批次 → 抽检叶菜、豆类
    # 例：抽检秋季时令水果 10 批次 → 抽检秋季时令水果
    # 例：抽检水果 12 批次 → 抽检水果
    # 例：抽检月饼 8 批次（之前版本） → 抽检月饼

    # 把"X 批次"或"X批次"删
    text = re.sub(r'[\s]*\d+\s*批次', '', text)

    # 把"抽检X、" + 末尾"的、"修整
    # 简化为：清除多余空格
    text = re.sub(r'\s+', ' ', text).strip()

    # 把"抽检叶菜、豆类，检测结果" → "抽检叶菜、豆类，检测结果"（保持原意）
    # 把"抽检秋季时令水果，结果全部合格并公示" 这种通顺
    return text


changes = []

for ti, tbl in enumerate(doc.tables):
    for ri, row in enumerate(tbl.rows):
        for ci, cell in enumerate(row.cells):
            # 只改内容 cell（C2 / 解决方法列），不动 label
            old = cell.text
            if '批次' in old:
                new = strip_batch(old)
                if new != old:
                    # 替换段落
                    if cell.paragraphs:
                        p = cell.paragraphs[0]
                        if p.runs:
                            p.runs[0].text = new
                            for r in p.runs[1:]:
                                r.text = ''
                        else:
                            p.add_run(new)
                    changes.append((ti, ri, ci, old[:60], new[:60]))

# 还要查段落
for p in doc.paragraphs:
    if '批次' in p.text:
        old = p.text
        new = strip_batch(old)
        if new != old:
            if p.runs:
                p.runs[0].text = new
                for r in p.runs[1:]:
                    r.text = ''
            changes.append(('para', '', '', old[:60], new[:60]))

for ti, ri, ci, old, new in changes:
    print(f'T{ti}R{ri}C{ci}:')
    print(f'  旧: {old}')
    print(f'  新: {new}')
    print()

doc.save(PATH)
print(f'\n共修改 {len(changes)} 处')