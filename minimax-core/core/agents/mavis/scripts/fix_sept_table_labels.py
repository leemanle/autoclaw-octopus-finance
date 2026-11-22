"""
修复 9 月份食品安全管控记录表的标签列多段重复问题。

根因：注入脚本把 8 月份模板里的多段标签（如 "排查覆盖日管控" + "日期范围" 两段）
合并成单个字符串 "排查覆盖日管控 / 日期范围"，并且重复塞进了原来的每个段落位置。

修法：把每个标签列 cell 里的重复段落清掉，恢复 8 月份的多段结构。

对应：
- 排查覆盖日管控 / 日期范围 → 排查覆盖日管控 + 日期范围（2 段）
- 上周问题整改 / 措施落实情况 → 上周问题整改 + 措施落实情况（2 段）
- 上周回顾 ×3 → 上周回顾 ×1（中间 2 段空）
- 上月调度安排 / 落实情况 → 上月调度安排 + 落实情况（2 段）
- 日管控发现的 / 问题及解决方法 → 日管控发现的 + 问题及解决方法（2 段）
- 参加人员 / （签字） → 参加人员 + （签字）（2 段）
- 企业主要负责人 / （签字） → 企业主要负责人 + （签字）（2 段）
- 年 月 日 ×3 → 年 月 日 ×1
"""

from docx import Document
from docx.shared import Pt
from copy import deepcopy

PATH = r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表9月2026.docx'

def fix_label_cell(cell, splitter):
    """
    修一个标签列 cell：
    - 把 cell 里所有段落里重复的合并字符串分离成 2 段
    - 删除多余的空段
    splitter 函数接收原始段字符串，返回修复后的段列表（不含空段）
    """
    # 收集当前段落文本列表
    raw = [p.text for p in cell.paragraphs]
    # 用 \n 拼接所有段落，模拟完整文本
    full_text = '\n'.join(raw)

    fixed_segments = splitter(full_text, raw)
    if fixed_segments is None:
        return False

    # 简化方案：直接清空 cell 的所有段落，然后塞 fixed_segments
    # 但为了保留段落格式（字体/字号），更稳的方法是：
    #   1. 保留第一个段落的格式
    #   2. 修改第一个段落的文本
    #   3. 删除多余的 paragraph elements
    paras = list(cell.paragraphs)
    if len(paras) >= 1:
        # 修改第一个段落文本（运行和 run xml 保留）
        first_p = paras[0]
        # 保留 runs 格式，但清空其文本
        for run in first_p.runs:
            run.text = ''
        # 先写入第一个 segment 到第一个段落
        if first_p.runs:
            first_p.runs[0].text = fixed_segments[0]
        else:
            # 没有 run，新建
            first_p.add_run(fixed_segments[0])
        # 给后面段落填后续 segments
        for i, seg in enumerate(fixed_segments[1:], start=1):
            if i < len(paras):
                p = paras[i]
                for run in p.runs:
                    run.text = ''
                if p.runs:
                    p.runs[0].text = seg
                else:
                    p.add_run(seg)
        # 删除多余段落
        for p in paras[len(fixed_segments):]:
            p._element.getparent().remove(p._element)
    return True


def split_with_slash(text):
    """如果文本是 'A / B' 形式，返回 ['A', 'B']；否则返回 None"""
    text = text.strip()
    if ' / ' in text:
        idx = text.find(' / ')
        left = text[:idx].strip()
        right = text[idx+3:].strip()
        if left and right:
            return [left, right]
    return None


def dedupe_paragraphs(cell):
    """把 cell 里的重复段落清掉，只留 1 段（移除重复的 + 空段）"""
    paras = list(cell.paragraphs)
    seen = []
    keep_indices = []
    for i, p in enumerate(paras):
        txt = p.text
        # 如果已有相同内容，跳过
        if any(t == txt for t in seen):
            # 删除段落
            p._element.getparent().remove(p._element)
            continue
        seen.append(txt)
        keep_indices.append(i)

    # 检查是否需要拆分（如果唯一段落是 'A / B' 形式）
    result_segs = []
    for i, p in enumerate(cell.paragraphs):
        txt = p.text
        segs = split_with_slash(txt)
        if segs:
            result_segs.append(segs)
        else:
            result_segs.append([txt])

    # 合并所有 segments
    final = []
    for segs in result_segs:
        final.extend(segs)

    # 清空段落再写
    paras = list(cell.paragraphs)
    # 修改第一段
    if len(paras) >= 1:
        first_p = paras[0]
        for run in first_p.runs:
            run.text = ''
        if first_p.runs:
            first_p.runs[0].text = final[0]
        else:
            first_p.add_run(final[0])

    # 后续段落
    for i, seg in enumerate(final[1:], start=1):
        if i < len(paras):
            p = paras[i]
            for run in p.runs:
                run.text = ''
            if p.runs:
                p.runs[0].text = seg
            else:
                p.add_run(seg)
        else:
            # 段数不够，需要新建段落
            new_p = first_p._element.makeelement(
                '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p',
            )
            new_pPr = first_p._element.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pPr')
            if new_pPr is not None:
                from copy import deepcopy
                new_p.append(deepcopy(new_pPr))
            new_r = first_p._element.makeelement(
                '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r',
            )
            new_t = first_p._element.makeelement(
                '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t',
            )
            new_t.text = seg
            new_r.append(new_t)
            new_p.append(new_r)
            first_p._element.addnext(new_p)

    # 删除多余段落（如果 final 比现有段落少）
    if len(final) < len(paras):
        for p in paras[len(final):]:
            p._element.getparent().remove(p._element)


def main():
    doc = Document(PATH)
    print(f'文档打开成功，共 {len(doc.tables)} 张表')

    # 9 月份文档的周排查表是 Table 8/9/10，月调度表是 Table 11
    target_tables = [8, 9, 10, 11]

    for ti in target_tables:
        if ti >= len(doc.tables):
            continue
        tbl = doc.tables[ti]
        print(f'\n=== Table {ti}（rows={len(tbl.rows)}, cols={len(tbl.columns)}）===')
        for ri, row in enumerate(tbl.rows):
            for ci, cell in enumerate(row.cells):
                before = len(cell.paragraphs)
                if before <= 1:
                    continue
                # 修复（不去 C2 内容列）
                if ci == 2:
                    continue
                dedupe_paragraphs(cell)
                after = len(cell.paragraphs)
                if after != before:
                    print(f'  R{ri}C{ci}: paras {before} → {after}')

    doc.save(PATH)
    print(f'\n保存：{PATH}')


if __name__ == '__main__':
    main()
