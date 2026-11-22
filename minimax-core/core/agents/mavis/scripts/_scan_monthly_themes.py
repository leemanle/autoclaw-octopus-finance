"""扫历史 5/6/7/7_new/8 月食品安全表的日管控主题，找季节性素材分布。"""
from docx import Document
import re

MONTHS = [
    ('5月', r'C:\Users\Administrator\Desktop\食品安全管控记录表5月2026vvv.docx'),
    ('6月', r'C:\Users\Administrator\Desktop\食品安全管控记录表6月2026.docx'),
    ('7月', r'C:\Users\Administrator\Desktop\食品安全管控记录表7月2026.docx'),
    ('7月_new', r'C:\Users\Administrator\Desktop\食品安全管控记录表7月2026_new.docx'),
    ('8月', r'C:\Users\Administrator\Desktop\食品安全管控记录表8月2026.docx'),
]

# 9 月份附件也在 v2/assets
M9 = r'C:\Users\Administrator\.minimax\v2\assets\2026\09\25\16-07-37-053-asset_20260925-160737-053_62889369b460_43a5aa96-食品安全管控记录表5月2026vvv.docx'


def scan(docx_path):
    try:
        doc = Document(docx_path)
    except Exception as e:
        print(f'ERR {docx_path}: {e}')
        return []
    out = []
    # 抓所有表格内的"解决方法" + "风险隐患描述" + "上报时间"
    for ti, tbl in enumerate(doc.tables):
        if ti >= 11:  # 只看前 11 张（8 日 + 3 周）
            break
        if len(tbl.rows) < 2:
            continue
        if len(tbl.columns) == 6:
            # 日管控
            for ri in [1, 2]:
                if ri >= len(tbl.rows):
                    break
                row = tbl.rows[ri]
                if len(row.cells) < 6:
                    continue
                ctype = row.cells[1].text.strip()
                cdes = row.cells[2].text.strip()
                csol = row.cells[4].text.strip()
                ctime = row.cells[5].text.strip()
                if cdes:
                    out.append(('日', ti, ri, ctype, cdes, csol, ctime))
        elif len(tbl.columns) == 3:
            # 周排查
            if ti in (8, 9, 10):
                for ri in range(1, len(tbl.rows) - 1):  # 不抓最后一行（签字）
                    row = tbl.rows[ri]
                    if len(row.cells) < 3:
                        continue
                    ckey = row.cells[0].text.strip().replace('\n', '|')
                    cval = row.cells[2].text.strip()
                    if cval:
                        out.append(('周', ti, ri, ckey, cval[:60], '', ''))
    return out


for label, path in MONTHS:
    # 优先用桌面版，没有就用附件版
    pass

paths = {
    '5月': r'C:\Users\Administrator\.minimax\v2\assets\2026\09\25\16-07-37-053-asset_20260925-160737-053_62889369b460_43a5aa96-食品安全管控记录表5月2026vvv.docx',
    '6月': r'C:\Users\Administrator\.minimax\v2\assets\2026\09\25\16-07-37-088-asset_20260925-160737-088_f4a6cc188a2b_e52b34e6-食品安全管控记录表6月2026.docx',
    '7月': r'C:\Users\Administrator\.minimax\v2\assets\2026\09\25\16-07-37-094-asset_20260925-160737-094_cf0545c39fe0_7f495dae-食品安全管控记录表7月2026.docx',
    '7月_new': r'C:\Users\Administrator\.minimax\v2\assets\2026\09\25\16-07-37-103-asset_20260925-160737-103_38408a6dd37c_e0b0e091-食品安全管控记录表7月2026_new.docx',
    '8月': r'C:\Users\Administrator\.minimax\v2\assets\2026\09\25\16-07-37-107-asset_20260925-160737-107_bf939cf96e2c_1fb1ffc9-食品安全管控记录表8月2026.docx',
}

for label, p in paths.items():
    print(f'\n=========== {label} ===========')
    items = scan(p)
    for typ, ti, ri, a, b, c, d in items:
        print(f'  [{typ} T{ti}R{ri}] {a} | {b[:60]}')
