"""
按 OOXML 层级复制 8 月份模板里签字行的 cell XML，替换 9 月份对应 cell。

目标：
- 周排查 R7C1 / R7C2（"年 月 日"）→ 8 月份这里是 2 段 [空段, "  年 月 日"]
- 月调度 R4C1 / R4C2 → 1 段 ["  年 月 日"]（前导 2 空格）
- 月调度 R5C1 / R5C2 → 3 段 ["", "", "  年 月 日"]

注意：8 月份中 R5C1/R5C2 的 cell 有 3 段，我们的目标是让 9 月份对应 cell 也有 3 段并把内容写一致。
R4C1/R4C2 是 1 段。
"""

import copy
from docx import Document
from docx.oxml.ns import qn
from lxml import etree

SRC_AUG = r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表8月2026.docx'
DST_SEPT = r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表9月2026.docx'

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS = {'w': W_NS}


def get_cell_xml(doc, table_idx, row_idx, col_idx):
    """返回 cell 的 w:tc 元素的 deepcopy"""
    tbl = doc.tables[table_idx]
    cell = tbl.rows[row_idx].cells[col_idx]
    tc = cell._tc
    return copy.deepcopy(tc)


def replace_cell_xml(doc, table_idx, row_idx, col_idx, new_tc):
    """用新 tc XML 替换 doc 中指定 cell"""
    tbl = doc.tables[table_idx]
    cell = tbl.rows[row_idx].cells[col_idx]
    old_tc = cell._tc
    # 把 old_tc 的 tcPr 拿过来再加（保证单元格属性不被破坏）
    tcPr = old_tc.find(qn('w:tcPr'))
    if tcPr is not None:
        tcPr_copy = copy.deepcopy(tcPr)
        new_tc.insert(0, tcPr_copy) if new_tc.find(qn('w:tcPr')) is None else None
    # 替换
    parent = old_tc.getparent()
    parent.replace(old_tc, new_tc)


def main():
    src = Document(SRC_AUG)
    dst = Document(DST_SEPT)

    # 周排查：src 中 Table 8/9/10 (idx 8/9/10) R7 C1,C2 → dst 中 Table 8/9/10 R7 C1,C2
    # 但 src 周排查 idx 是 src.tables 的下标，dst 也是
    for ti in [8, 9, 10]:
        # 取 src 的 R7C1, R7C2
        for ci in [1, 2]:
            new_tc = get_cell_xml(src, ti, 7, ci)
            # 拿到 dst 的 cell，先取出其 tcPr（如果有），合并到 new_tc
            dst_cell_tc = dst.tables[ti].rows[7].cells[ci]._tc
            old_tcPr = dst_cell_tc.find(qn('w:tcPr'))
            if old_tcPr is not None:
                # 移除 new_tc 自身的 tcPr（如果有）
                new_tcPr = new_tc.find(qn('w:tcPr'))
                if new_tcPr is not None:
                    new_tc.remove(new_tcPr)
                # 把 dst 的 tcPr 插入到 new_tc 顶部
                new_tc.insert(0, copy.deepcopy(old_tcPr))
            replace_cell_xml(dst, ti, 7, ci, new_tc)

    # 月调度：src Table 11 R4/R5 → dst Table 11 R4/R5
    for ri in [4, 5]:
        for ci in [1, 2]:
            new_tc = get_cell_xml(src, 11, ri, ci)
            dst_cell_tc = dst.tables[11].rows[ri].cells[ci]._tc
            old_tcPr = dst_cell_tc.find(qn('w:tcPr'))
            if old_tcPr is not None:
                new_tcPr = new_tc.find(qn('w:tcPr'))
                if new_tcPr is not None:
                    new_tc.remove(new_tcPr)
                new_tc.insert(0, copy.deepcopy(old_tcPr))
            replace_cell_xml(dst, 11, ri, ci, new_tc)

    dst.save(DST_SEPT)
    print(f'已保存：{DST_SEPT}')


if __name__ == '__main__':
    main()
