# -*- coding: utf-8 -*-
"""
以 8 月 docx 为模板，精准替换 9 月内容。

策略：
1. shutil.copy(8月 → 9月)
2. 只改日期相关段落（检查日期 / 排查日期 / 会议时间）
3. 只改内容 cell（按 cell 索引精确识别）：
   - 日管控：R1/R2 整行内容（R3 是空行、R4 是签字行不在这里改——签字日期行由 fix 修）
   - 周排查：R0C1/C2（日期范围）、R1C2（上周回顾）、R2-R4 的 C2、R5C1/C2、R6C1/C2
   - 月调度：R0C2（last_month）、R1C2（summary_find）、R2C2（summary_week）、R3C1/C2（arrange）
4. 所有 label cell（C0 / C1 中的 label、签字行）完全跳过

然后跑 fix_signature_cell_xml_replace.py 把 8 月模板的"参加人员 / （签字） / 年 月 日"
签字日期 cell XML 直接复制到 9 月对应位置（保留"年 月 日"前导空格 + 空段）。

9 月内容主题（中秋节相关内容只占 1 份 = 9.4 节后月饼下架登记）。
"""

import shutil
from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph

SRC = r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表8月2026.docx'
OUT = r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表9月2026.docx'

sept_daily = [
    {'date': '2026.9.1', 'risks': [
        ('入场销售者管理', '9 月开学季，新入场经营户档案需及时建档',
         '梳理 9 月新入场经营户名单，完成入场销售者档案建档；对接辖区学校食堂采购，办理临时通行证'),
        ('入场查验', '秋季时令水果（葡萄、苹果、梨）批量上市，索证索票台账更新',
         '要求经营户补齐进货票据与产品质量合格凭证，新增水果类农产品质量安全协议更新归档'),
    ]},
    {'date': '2026.9.3', 'risks': [
        ('场内检查', '市场内排水沟清理不彻底，异味较大',
         '组织人员疏通全场排水沟 1 次，冲洗地面，落实每周深度清洁制度'),
        ('入场查验', '白露节气前后本地叶菜批量上市，开展农药残留快速检测',
         '抽检叶菜 8 批次、豆类 4 批次，检测结果全部合格，做好原始记录和公示'),
    ]},
    {'date': '2026.9.4', 'risks': [
        ('入场查验', '中秋节后剩余月饼下架登记与保质期复核',
         '督促月饼经营户 24 小时内完成下架登记，核对进货票据，下架品按过期食品处置流程处理'),
        ('信息公示', '中秋节后食品安全宣传栏更新与农残公示',
         '更新食品安全宣传栏 1 期，含节后月饼消费提示与举报电话；公示 9.1-9.3 农残抽检数据'),
    ]},
    {'date': '2026.9.10', 'risks': [
        ('入场销售者管理', '经营户健康证年度复检与入场销售者档案季度盘点',
         '对全场经营户健康证开展 1 次年度复检，临近到期者通知续期；完成入场销售者档案季度盘点与目录更新'),
        ('食品安全管理人员', '食品安全员参加市场监管局组织的业务培训',
         '已参训 1 人次，归档培训记录与考核证明，更新培训档案'),
    ]},
    {'date': '2026.9.15', 'risks': [
        ('入场查验', '白露前后秋季时令水果专项抽检（葡萄、苹果、梨、桃）',
         '抽检秋季时令水果 10 批次，重点检测农药残留与糖度，结果全部合格并公示'),
        ('场内检查', '白露节气后全场食品安全综合检查',
         '对全场摊位开展拉网式检查，重点检查冷链、散装食品和叶菜保鲜情况'),
    ]},
    {'date': '2026.9.18', 'risks': [
        ('场所及布局', '国庆节前冷链设备专项排查',
         '对全场冷柜、冷库开展 1 次专项排查，更换老化密封条，确保国庆假期冷链运行可靠'),
        ('场内检查', '国庆节前夜间市场外围摊点卫生回潮治理',
         '与城管联动开展夜间巡查，劝离外围游商，确保国庆前场内经营秩序'),
    ]},
    {'date': '2026.9.20', 'risks': [
        ('入场查验', '秋季水果（梨、苹果、葡萄）集中上市，开展专项抽检',
         '抽检水果 12 批次，检测农药残留和糖度，结果全部合格并公示'),
        ('食品安全管理制度', '对照最新版管控清单开展制度自查',
         '完成食品安全管理制度目录更新，新增国庆节令食品应急处置预案'),
    ]},
    {'date': '2026.9.24', 'risks': [
        ('场内检查', '国庆节前全场食品安全综合检查',
         '国庆节前 1 天对全场经营户开展拉网式检查，重点检查冷链、散装食品台账'),
        ('食品安全事故处置', '国庆节前一周食品安全应急联络表更新',
         '更新食品安全应急联络表（含市场监管局、街道、卫生院、经营户代表）；公示 9.22-9.24 农残抽检数据，张贴节日食品安全消费提示'),
    ]},
]

sept_weekly = [
    {'period': '9.1—9.7',
     'last_week': '8 月下旬中秋节食品安全专项检查各项措施落实到位；月饼礼盒备案、月饼专项抽检、节令食品应急演练均已完成',
     'this_week': '9 月新入场经营户建档、秋季水果集中上市索证索票更新、白露节气蔬菜农残抽检',
     'risk_info': '白露节气前后本地叶菜批量上市，需加强农残快检；秋季时令水果抽检任务重',
     'cause': '秋季时令蔬菜水果上市集中，加之 9 月开学季学校食堂采购衔接，经营户备案管理压力上升',
     'measure': '完成 9 月新入场经营户建档与学校食堂临时通行证办理；公示 9.1-9.3 农残抽检数据；更新食品安全宣传栏第一期',
     'remark': '9 月上旬天气转凉，白露节气前后重点关注叶菜农残与冷链保鲜'},
    {'period': '9.8—9.14',
     'last_week': '9 月新入场经营户建档完成；学校食堂临时通行证已办理；白露节气叶菜农残抽检全部合格',
     'this_week': '经营户健康证年度复检、入场销售者档案季度盘点、培训记录归档',
     'risk_info': '部分经营户健康证临近到期需续期；入场销售者档案季度盘点需集中更新',
     'cause': '经营户健康证年度复检制度尚未形成闭环，入场销售者档案需要按季度集中维护',
     'measure': '对全场经营户开展 1 次健康证年度复检，临近到期者 3 个工作日内完成续期；完成入场销售者档案季度盘点与目录更新；归档培训记录 1 人次',
     'remark': '9 月中旬白露节气，重点关注叶菜保鲜与经营户档案维护'},
    {'period': '9.15—9.21',
     'last_week': '经营户健康证年度复检已完成，临近到期者全部通知续期；入场销售者档案季度盘点与目录更新完成',
     'this_week': '中秋节后剩余月饼下架登记、秋季时令水果专项抽检、国庆节前冷链专项排查',
     'risk_info': '中秋节后剩余月饼需在 24 小时内完成下架登记；秋季时令水果抽检任务重；国庆节前冷链设备负荷上升需专项排查',
     'cause': '节令性消费叠加秋季换季，冷链温控与应季水果保鲜管理压力增大',
     'measure': '督促月饼经营户 24 小时内完成下架登记并按过期食品处置流程处理；抽检秋季时令水果 10 批次全部合格；冷链设备专项排查完成 1 次',
     'remark': '9 月下旬秋分前后，重点防控国庆节前冷链与节令食品安全'},
]

sept_monthly = {
    'last_month': '8 月下旬中秋节食品安全专项检查各项措施落实到位。月饼礼盒备案登记、月饼专项抽检、节令食品应急演练、节前糕点熟食保质期检查全部完成',
    'summary_find': '9 月围绕开学季对接+白露节气叶菜初查+经营户健康证年度复检与档案季度盘点+中秋节后剩余月饼下架登记+秋季时令水果专项抽检+国庆节前冷链排查+应急联络表更新 七条主线开展日管控 8 次，整改到位率 100%',
    'summary_week': '9 月周排查暴露的主要问题：1）秋季换季冷链温控与应季水果保鲜管理压力上升；2）经营户健康证年度复检与档案季度盘点需形成常态机制；3）国庆节前冷链设备负荷增大需专项排查',
    'arrange': '10 月进入国庆长假与重阳节时段：1）国庆假期值班值守与应急处置；2）秋季水果保鲜与冷链管理；3）重阳节令食品（糕点、营养品）检查；4）入场销售者档案季度更新与协议续签；5）全年食品安全工作总结与下一年度计划部署',
}


def replace_para_text(p, new_text):
    """替换 paragraph 文字"""
    if not p.runs:
        p.add_run(new_text)
        return
    p.runs[0].text = new_text
    for r in p.runs[1:]:
        r.text = ''


def replace_cell_1seg(cell, new_text):
    """内容 cell 通常 1 段：直接写第一段"""
    paras = cell.paragraphs
    if not paras:
        return
    replace_para_text(paras[0], new_text)


def replace_cell_multiseg(cell, new_text):
    """多段 cell：把内容全写第一段，其他段清空。"""
    paras = cell.paragraphs
    if not paras:
        return
    replace_para_text(paras[0], new_text)
    for i in range(1, len(paras)):
        for r in paras[i].runs:
            r.text = ''


def smart_replace(cell, new_text):
    """根据段数自动选策略"""
    n = len(cell.paragraphs)
    if n <= 1:
        replace_cell_1seg(cell, new_text)
    else:
        replace_cell_multiseg(cell, new_text)


def main():
    shutil.copy(SRC, OUT)
    doc = Document(OUT)
    body = doc.element.body

    # 收集顶层段落
    top_paras = []
    for child in body.iterchildren():
        if child.tag.split('}')[-1] == 'p':
            top_paras.append(Paragraph(child, body))

    # 1) 修改日管控日期段落
    daily_date_count = 0
    for p in top_paras:
        text = p.text
        if text.startswith('检查日期：') and daily_date_count < len(sept_daily):
            d = sept_daily[daily_date_count]['date']
            replace_para_text(p, f'检查日期：{d}                记录编号：')
            daily_date_count += 1

    # 2) 修改周排查日期段落
    weekly_dates = ['2026.9.7', '2026.9.14', '2026.9.21']
    weekly_date_count = 0
    for p in top_paras:
        text = p.text
        if text.startswith(' 排查日期') and weekly_date_count < len(weekly_dates):
            replace_para_text(p, f' 排查日期：{weekly_dates[weekly_date_count]}                  报告编号：')
            weekly_date_count += 1

    # 3) 修改月调度会议时间
    for p in top_paras:
        text = p.text
        if '会议时间' in text and '月份' not in text:
            # 8月原文是 " 会议时间：2026.8.23 ..."（1 个空格）
            replace_para_text(p, ' 会议时间：2026.9.23   会议地点：总经理办公室     纪要编号：')
            break

    # 4) 改日管控表内容：Table 0-7
    for ti in range(8):
        if ti >= len(doc.tables):
            break
        t = doc.tables[ti]
        if len(t.rows) < 5:
            continue
        risks = sept_daily[ti]['risks']
        date_str = sept_daily[ti]['date']
        # R1: 6 列内容
        for ci, txt in enumerate([str(1), risks[0][0], risks[0][1], '☑是 □否', risks[0][2], date_str]):
            smart_replace(t.rows[1].cells[ci], txt)
        # R2
        for ci, txt in enumerate([str(2), risks[1][0], risks[1][1], '☑是 □否', risks[1][2], date_str]):
            smart_replace(t.rows[2].cells[ci], txt)
        # R3 空行不动
        # R4 签字行：不动（由 fix_signature_cell_xml_replace 处理）
        # R4 列 0-1 是 label "食品安全员（签字）"+ 列 2-5 是"年 月 日"，全跳过
        # 上报时间列已经被 R1C5/R2C5 写过

    # 5) 改周排查表内容：Table 8/9/10
    for wi in range(3):
        ti = 8 + wi
        if ti >= len(doc.tables):
            break
        t = doc.tables[ti]
        w = sept_weekly[wi]
        # R0C1, R0C2 = period
        # 但 R0C0 label 是 "排查覆盖日管控/日期范围" 2 段不动
        smart_replace(t.rows[0].cells[1], w['period'])
        smart_replace(t.rows[0].cells[2], w['period'])
        # R1C2 = last_week（C0/C1 是 label 不动）
        smart_replace(t.rows[1].cells[2], w['last_week'])
        # R2C2 = this_week
        smart_replace(t.rows[2].cells[2], w['this_week'])
        # R3C2 = risk_info
        smart_replace(t.rows[3].cells[2], w['risk_info'])
        # R4C2 = cause
        smart_replace(t.rows[4].cells[2], w['cause'])
        # R5C1, R5C2 = measure
        smart_replace(t.rows[5].cells[1], w['measure'])
        smart_replace(t.rows[5].cells[2], w['measure'])
        # R6C1, R6C2 = remark
        smart_replace(t.rows[6].cells[1], w['remark'])
        smart_replace(t.rows[6].cells[2], w['remark'])
        # R7 签字行不动

    # 6) 改月调度表内容：Table 11
    if len(doc.tables) > 11:
        t = doc.tables[11]
        m = sept_monthly
        # R0: 上月回顾 R0C2 = last_month
        smart_replace(t.rows[0].cells[2], m['last_month'])
        # R1: 本月总结 R1C2 = summary_find
        smart_replace(t.rows[1].cells[2], m['summary_find'])
        # R2: 本月总结 R2C2 = summary_week
        smart_replace(t.rows[2].cells[2], m['summary_week'])
        # R3: 调度安排 R3C1/C2 = arrange
        smart_replace(t.rows[3].cells[1], m['arrange'])
        smart_replace(t.rows[3].cells[2], m['arrange'])
        # R4/R5 签字行不动

    doc.save(OUT)
    print("OK:", OUT)


if __name__ == '__main__':
    main()
