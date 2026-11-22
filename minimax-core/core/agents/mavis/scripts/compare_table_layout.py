import zipfile
from xml.etree import ElementTree as ET

ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def get_table_layout(path, label):
    with zipfile.ZipFile(path) as z:
        with z.open('word/document.xml') as f:
            tree = ET.parse(f)
            root = tree.getroot()
            body = root.find('w:body', ns)
            tables = body.findall('w:tbl', ns)
            print(f'=== {label} 第 0 个表格 ===')
            t = tables[0]
            grid = t.find('w:tblGrid', ns)
            if grid is not None:
                cols = grid.findall('w:gridCol', ns)
                widths = [c.get(W + 'w') for c in cols]
                print(f'  gridCol widths (twips): {widths}')
                print(f'  总宽: {sum(int(w) for w in widths if w)} twips')
            tblPr = t.find('w:tblPr', ns)
            if tblPr is not None:
                tblW = tblPr.find('w:tblW', ns)
                if tblW is not None:
                    print(f'  tblW: w={tblW.get(W + chr(34).join(["w"])[1:-1])} type={tblW.get(W + chr(34).join(["type"])[1:-1])}')

get_table_layout(r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表8月2026.docx', '8月')
print()
get_table_layout(r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表9月2026.docx', '9月')