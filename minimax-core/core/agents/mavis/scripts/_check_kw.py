from docx import Document
doc = Document(r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表9月2026.docx')
print('=== 含 批次 / 培训 / 宣城 的文本 ===')
for p in doc.paragraphs:
    if any(kw in p.text for kw in ['批次', '培训', '宣城']):
        print(f'>> PARA: {p.text!r}')
for ti, tbl in enumerate(doc.tables):
    for ri, row in enumerate(tbl.rows):
        for ci, cell in enumerate(row.cells):
            t = cell.text
            if any(kw in t for kw in ['批次', '培训', '宣城']):
                print(f'>> T{ti}R{ri}C{ci}: {t[:120]!r}')