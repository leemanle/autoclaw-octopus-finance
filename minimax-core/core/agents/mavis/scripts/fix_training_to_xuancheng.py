"""
把 9 月份食品安全表 Table 3 (原 9.10 日管控) 的风险 2：
- 风险类型：食品安全管理人员
- 风险描述：食品安全员参加市场监管局组织的业务培训
- 解决方法：已参训 1 人次，归档培训记录与考核证明，更新培训档案

改成 9.23 参加宣城市快检培训：
- 风险描述：9 月 23 日参加宣城市快检培训
- 解决方法：已参训 1 人次，归档培训记录与考核证明，更新培训档案
- 上报时间：2026.9.23

同时把 Table 3 的"检查日期：2026.9.10"改成"检查日期：2026.9.23"。
R1 (健康证年度复检) 的上报时间保留 9.23 (与表头一致)。
"""
from docx import Document

PATH = r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表9月2026.docx'
doc = Document(PATH)

# 1) 改 Table 3 的内容
tbl = doc.tables[3]
# R2 风险 2: C2=描述, C4=解决方法, C5=上报时间
row2 = tbl.rows[2]

def set_p(p, txt):
    if p.runs:
        p.runs[0].text = txt
        for r in p.runs[1:]:
            r.text = ''
    else:
        p.add_run(txt)

# C2 风险描述
set_p(row2.cells[2].paragraphs[0], '9 月 23 日参加宣城市快检培训')
# C4 解决方法（保留原"已参训 1 人次..."）
# 这里本来已经是 "已参训 1 人次，归档培训记录与考核证明，更新培训档案"，但 R2C4 cell 内容可能与原本有差异，先打出来
print('R2C4 当前:', row2.cells[4].text[:80])
# C5 上报时间
set_p(row2.cells[5].paragraphs[0], '2026.9.23')

# R1 上报时间也统一到 9.23（与表头一致）
row1 = tbl.rows[1]
print('R1C5 当前:', row1.cells[5].text[:80])
set_p(row1.cells[5].paragraphs[0], '2026.9.23')

# 2) 改 Table 3 表头 "检查日期：2026.9.10"
for p in doc.paragraphs:
    if p.text.strip().startswith('检查日期：2026.9.10'):
        set_p(p, '检查日期：2026.9.23                记录编号：')
        print(f'已改表头日期：{p.text[:80]}')
        break

doc.save(PATH)
print('\n已保存')