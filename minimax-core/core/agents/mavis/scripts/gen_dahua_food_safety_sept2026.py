# -*- coding: utf-8 -*-
"""按 8 月格式精确还原：行距 + 空段数 + 字体字号 + 风险类型 + 节前准备。"""
import shutil
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

SRC = r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表8月2026.docx'
OUT = r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表9月2026.docx'

shutil.copy(SRC, OUT)
doc = Document(OUT)
body = doc.element.body
sectPr = None
for child in list(body):
    if child.tag == qn('w:sectPr'):
        sectPr = child
    body.remove(child)
if sectPr is not None:
    body.append(sectPr)

# ==== 9 月日管控（8 份，按 8 月节奏） ====
daily_records = [
    ("2026.9.1", [
        ("入场销售者管理", "9 月开学季，新入场经营户档案需及时建档",
         "☑是 □否",
         "梳理 9 月新入场经营户名单，完成入场销售者档案建档；对接辖区学校食堂采购，办理临时通行证"),
        ("入场查验", "秋季时令水果（葡萄、苹果、梨）批量上市，索证索票台账更新",
         "☑是 □否",
         "要求经营户补齐进货票据与产品质量合格凭证，新增水果类农产品质量安全协议更新归档"),
    ]),
    ("2026.9.3", [
        ("场内检查", "市场内排水沟清理不彻底，异味较大",
         "☑是 □否",
         "组织人员疏通全场排水沟 1 次，冲洗地面，落实每周深度清洁制度"),
        ("入场查验", "对当日新入场蔬菜开展农药残留快速检测",
         "☑是 □否",
         "抽检叶菜 8 批次、豆类 4 批次，检测结果全部合格，做好原始记录和公示"),
    ]),
    ("2026.9.4", [
        ("入场查验", "中秋月饼礼盒上市前资质与添加剂备案检查",
         "☑是 □否",
         "要求月饼经营户出示 SC 证、第三方检测报告；核对食品添加剂使用范围，完成月饼摊位备案登记"),
        ("信息公示", "中秋食品安全宣传栏更新与农残公示",
         "☑是 □否",
         "更新食品安全宣传栏 1 期，含中秋消费提示与举报电话；公示 9.1-9.3 农残抽检数据"),
    ]),
    ("2026.9.10", [
        ("场内检查", "中秋前糕点、熟食摊位保质期与冷藏温度专项检查",
         "☑是 □否",
         "对散装糕点、豆制品、熟食摊位开展保质期与冷藏温度专项检查，全部合格"),
        ("食品安全事故处置", "中秋节令食品应急处置预案演练",
         "☑是 □否",
         "组织食品安全员开展过期月饼应急处置演练 1 次，更新应急联络表"),
    ]),
    ("2026.9.15", [
        ("入场查验", "中秋前月饼专项抽检（防腐剂、甜味剂、色素）",
         "☑是 □否",
         "抽检月饼 8 批次，重点检测防腐剂、甜味剂、色素，结果全部合格并公示"),
        ("食品安全管理人员", "食品安全员参加市场监管局组织的业务培训",
         "☑是 □否",
         "已参训 1 人次，归档培训记录与考核证明，更新培训档案"),
    ]),
    ("2026.9.18", [
        ("场所及布局", "中秋前客流量加大，提前做好通道疏导与临时摊位扩容准备",
         "☑是 □否",
         "划定中秋高峰日临时采购通道与停车引导；提前对接经营户备货，确保中秋前一周供货充足"),
        ("场内检查", "中秋前夜间市场外围摊点卫生回潮，巡查加密",
         "☑是 □否",
         "与城管联动开展夜间巡查，劝离外围游商，确保场内经营秩序"),
    ]),
    ("2026.9.20", [
        ("入场查验", "秋季水果（梨、苹果、葡萄）集中上市，开展专项抽检",
         "☑是 □否",
         "抽检水果 12 批次，检测农药残留和糖度，结果全部合格并公示"),
        ("食品安全管理制度", "对照最新版管控清单开展制度自查",
         "☑是 □否",
         "完成食品安全管理制度目录更新，新增国庆节令食品应急处置预案"),
    ]),
    ("2026.9.24", [
        ("场内检查", "中秋前全场食品安全综合检查与冷链设备排查",
         "☑是 □否",
         "中秋前 1 天对全场经营户开展拉网式检查，重点检查冷链、散装、月饼台账"),
        ("信息公示", "中秋节当日农残快检结果与节日消费提示公示",
         "☑是 □否",
         "公示 9.22-9.24 农残抽检数据；张贴节日食品安全消费提示"),
    ]),
]

# ==== 9 月周排查（3 份） ====
weekly_records = [
    ("2026.9.7", "9.1—9.7", [
        ("上周回顾", "上周问题整改 / 措施落实情况",
         "8 月中下旬中秋节食品安全专项检查各项措施落实到位；9 月开学季学校食堂采购临时通行证已办理"),
        ("本周排查", "日管控发现问题及解决方法",
         "9 月新入场经营户建档、秋季水果集中上市索证索票更新、月饼礼盒备案检查"),
        ("本周排查", "其他食品安全 / 风险信息",
         "9 月上中旬月饼摊位陆续进场销售，需提前完成备案登记"),
        ("本周排查", "原因分析",
         "节令食品上市集中，需提前对接经营户与上游供应，加强备案管理"),
        ("整改措施",
         "完成中秋月饼礼盒备案登记；更新食品安全宣传栏第一期；公示 9.1-9.3 农残抽检数据",
         "完成中秋月饼礼盒备案登记；更新食品安全宣传栏第一期；公示 9.1-9.3 农残抽检数据"),
        ("备    注",
         "9 月上旬天气转凉，中秋节前市场月饼摊位陆续进场销售",
         "9 月上旬天气转凉，中秋节前市场月饼摊位陆续进场销售"),
    ]),
    ("2026.9.14", "9.8—9.14", [
        ("上周回顾", "上周问题整改 / 措施落实情况",
         "中秋月饼礼盒备案登记全部完成；食品安全宣传栏第一期已更新并公示 9.1-9.3 农残抽检数据"),
        ("本周排查", "日管控发现问题及解决方法",
         "中秋前糕点熟食摊位保质期与冷藏温度专项检查、节令食品应急预案演练"),
        ("本周排查", "其他食品安全 / 风险信息",
         "中秋节令消费集中，糕点熟食库存压力增大；应急处置预案需提前演练"),
        ("本周排查", "原因分析",
         "节令消费高峰期叠加气温仍偏高，食品保质期与冷链管理需要持续关注"),
        ("整改措施",
         "糕点熟食摊位保质期与冷藏温度专项检查全部合格；开展过期月饼应急处置演练 1 次",
         "糕点熟食摊位保质期与冷藏温度专项检查全部合格；开展过期月饼应急处置演练 1 次"),
        ("备    注",
         "中秋节前气温仍偏高，重点关注糕点熟食保质期与冷链温度",
         "中秋节前气温仍偏高，重点关注糕点熟食保质期与冷链温度"),
    ]),
    ("2026.9.21", "9.15—9.21", [
        ("上周回顾", "上周问题整改 / 措施落实情况",
         "中秋节前糕点熟食摊位保质期与冷藏温度专项检查全部合格；过期月饼应急处置演练完成"),
        ("本周排查", "日管控发现问题及解决方法",
         "中秋前月饼专项抽检、客流量加大准备工作、夜间外围摊点卫生回潮治理"),
        ("本周排查", "其他食品安全 / 风险信息",
         "中秋前一周月饼销售进入高峰，散装糕点与熟食库存压力增大；夜间市场外围游商回潮带来卫生管理压力"),
        ("本周排查", "原因分析",
         "中秋节令消费激增叠加中秋前一周备货高峰，需提前做好通道与冷链应对"),
        ("整改措施",
         "抽检月饼 8 批次全部合格；划定中秋高峰日临时采购通道；督促经营户备货充足；与城管联动夜间巡查",
         "抽检月饼 8 批次全部合格；划定中秋高峰日临时采购通道；督促经营户备货充足；与城管联动夜间巡查"),
        ("备    注",
         "中秋前一周月饼销售进入高峰，散装糕点与熟食库存压力增大",
         "中秋前一周月饼销售进入高峰，散装糕点与熟食库存压力增大"),
    ]),
]

# ==== 9 月月调度会议（1 份） ====
monthly_record = ("2026.9.23", [
    ("上月回顾", "上月调度安排 / 落实情况",
     "8 月下旬中秋节食品安全专项检查各项措施落实到位。月饼礼盒备案登记、月饼专项抽检、节令食品应急演练、节前糕点熟食保质期检查全部完成；中秋节当天值班巡查保障有力"),
    ("本月总结", "日管控发现的 / 问题及解决方法",
     "9 月围绕中秋前备案+抽检+客流准备+保质期+应急演练、中秋节后下架与国庆节前冷链排查三条主线开展日管控 8 次，整改到位率 100%"),
    ("本月总结", "周排查问题出现的原因分析、整改措施",
     "9 月周排查暴露的主要问题：1）中秋前部分月饼经营户对食品添加剂使用范围认识需加强；2）节后剩余月饼下架时效需进一步统一；3）国庆节前冷链设备负荷上升需专项排查。整改措施：开展月饼专项抽检 8 批次、节前冷链设备专项排查 1 次、国庆前拉网式综合检查 1 次"),
    ("调度安排",
     "10 月进入国庆长假与重阳节时段：1）国庆假期值班值守与应急处置；2）秋季水果保鲜与冷链管理；3）重阳节令食品（糕点、营养品）检查；4）入场销售者档案季度更新与协议续签；5）全年食品安全工作总结与下一年度计划部署",
     "10 月进入国庆长假与重阳节时段：1）国庆假期值班值守与应急处置；2）秋季水果保鲜与冷链管理；3）重阳节令食品（糕点、营养品）检查；4）入场销售者档案季度更新与协议续签；5）全年食品安全工作总结与下一年度计划部署"),
])

# ==== 字体字号（与 8 月一致） ====
# 8 月实际值：
# - 每日标题：Normal（无字号）
# - 每日副标题：12pt 楷体_GB2312, line_sp=1.0
# - 检查日期：默认字号, line_sp=1.67
# - 承诺段落：12pt 仿宋_GB2312, line_sp=1.67
# - 周/月标题：22pt 方正小标宋简体
# - 周/月副标题：14pt 楷体_GB2312, line_sp=1.83
# - 月调度：line_sp=2.5

EMU_PER_PT = 12700

def _set_line_spacing(p, multiple):
    """multiple 倍行距 (相对 12pt 单倍)"""
    val = int(240 * multiple)
    pPr = p._element.get_or_add_pPr()
    spacing = pPr.find(qn('w:spacing'))
    if spacing is None:
        from docx.oxml import OxmlElement
        spacing = OxmlElement('w:spacing')
        pPr.insert(0, spacing)
    spacing.set(qn('w:line'), str(val))
    spacing.set(qn('w:lineRule'), 'auto')

def _set_eastasia(run, font_name):
    rPr = run._element.get_or_add_rPr()
    rfonts = rPr.find(qn('w:rFonts'))
    if rfonts is None:
        from docx.oxml import OxmlElement
        rfonts = OxmlElement('w:rFonts')
        rPr.insert(0, rfonts)
    rfonts.set(qn('w:eastAsia'), font_name)

def add_title_daily(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run(text)

def add_subtitle_daily(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.size = Pt(12)
    _set_eastasia(run, '楷体_GB2312')
    _set_line_spacing(p, 1.0)

def add_p_check_date(text):
    """检查日期：line_sp=1.67"""
    p = doc.add_paragraph()
    p.add_run(text)
    _set_line_spacing(p, 1.67)

def add_p_blank_short(text='                              '):
    """短空白段（line_sp=0.5）"""
    p = doc.add_paragraph()
    p.add_run(text)
    _set_line_spacing(p, 0.5)

def add_p_commitment(text):
    """承诺段落：12pt 仿宋_GB2312, line_sp=1.67"""
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(12)
    _set_eastasia(run, '仿宋_GB2312')
    _set_line_spacing(p, 1.67)

def add_p_empty():
    """空段（无字号，无行距）"""
    doc.add_paragraph()

def add_title_section(text):
    """周/月标题：22pt 方正小标宋简体"""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.size = Pt(22)
    _set_eastasia(run, '方正小标宋简体')

def add_subtitle_section(text):
    """周/月副标题：14pt 楷体_GB2312, line_sp=1.83"""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.size = Pt(14)
    _set_eastasia(run, '楷体_GB2312')
    _set_line_spacing(p, 1.83)

def add_p_section_date(text):
    """周/月排查日期：line_sp=1.83"""
    p = doc.add_paragraph()
    p.add_run(text)
    _set_line_spacing(p, 1.83)

def add_p_meeting(text):
    """月调度会议时间：line_sp=2.5"""
    p = doc.add_paragraph()
    p.add_run(text)
    _set_line_spacing(p, 2.5)

def set_cell_daily_header(cell, text):
    cell.text = text
    for para in cell.paragraphs:
        _set_line_spacing(para, 1.0)
        for run in para.runs:
            run.font.size = Pt(12)
            _set_eastasia(run, '仿宋_GB2312')

def set_cell_daily_data(cell, text):
    cell.text = text
    for para in cell.paragraphs:
        _set_line_spacing(para, 1.0)
        for run in para.runs:
            # 不设字号
            rPr = run._element.find(qn('w:rPr'))
            if rPr is not None:
                rfonts = rPr.find(qn('w:rFonts'))
                if rfonts is not None:
                    rPr.remove(rfonts)
                sz = rPr.find(qn('w:sz'))
                if sz is not None:
                    rPr.remove(sz)

def set_cell_daily_sign(cell, text):
    cell.text = text
    for para in cell.paragraphs:
        _set_line_spacing(para, 1.0)
        for run in para.runs:
            run.font.size = Pt(12)
            _set_eastasia(run, '仿宋_GB2312')

def set_cell_section_label(cell, text):
    cell.text = text
    for para in cell.paragraphs:
        _set_line_spacing(para, 1.83)
        for run in para.runs:
            run.font.size = Pt(14)
            _set_eastasia(run, '仿宋_GB2312')

def set_cell_section_data(cell, text):
    cell.text = text
    for para in cell.paragraphs:
        _set_line_spacing(para, 1.0)
        for run in para.runs:
            rPr = run._element.find(qn('w:rPr'))
            if rPr is not None:
                rfonts = rPr.find(qn('w:rFonts'))
                if rfonts is not None:
                    rPr.remove(rfonts)
                sz = rPr.find(qn('w:sz'))
                if sz is not None:
                    rPr.remove(sz)

def add_daily_table(date, risks):
    table = doc.add_table(rows=5, cols=6)
    table.style = 'Table Grid'
    headers = ['序号', '风险类型', '风险隐患描述', '是否解决', '解决方法（未解决原因和防范措施）', '上报时间']
    for i, h in enumerate(headers):
        set_cell_daily_header(table.rows[0].cells[i], h)
    for idx, item in enumerate(risks, 1):
        rtype, desc, solved, solution = item
        row = table.rows[idx]
        set_cell_daily_data(row.cells[0], str(idx))
        set_cell_daily_data(row.cells[1], rtype)
        set_cell_daily_data(row.cells[2], desc)
        set_cell_daily_data(row.cells[3], solved)
        set_cell_daily_data(row.cells[4], solution)
        set_cell_daily_data(row.cells[5], date)
    blank_idx = len(risks) + 1
    set_cell_daily_data(table.rows[blank_idx].cells[0], str(blank_idx))
    set_cell_daily_data(table.rows[blank_idx].cells[3], '□是 □否')
    sign_row = table.rows[4]
    set_cell_daily_sign(sign_row.cells[0], '食品安全员（签字）')
    set_cell_daily_sign(sign_row.cells[1], '食品安全员（签字）')
    set_cell_daily_sign(sign_row.cells[2], '年    月    日')
    set_cell_daily_sign(sign_row.cells[3], '年    月    日')
    set_cell_daily_sign(sign_row.cells[4], '年    月    日')
    set_cell_daily_sign(sign_row.cells[5], '年    月    日')

def add_weekly_table(period, rows_data):
    table = doc.add_table(rows=8, cols=3)
    table.style = 'Table Grid'
    set_cell_section_label(table.rows[0].cells[0], '排查覆盖日管控 / 日期范围')
    set_cell_section_data(table.rows[0].cells[1], period)
    set_cell_section_data(table.rows[0].cells[2], period)
    for idx, item in enumerate(rows_data, 1):
        label, c1, c2 = item
        set_cell_section_label(table.rows[idx].cells[0], label)
        set_cell_section_data(table.rows[idx].cells[1], c1)
        set_cell_section_data(table.rows[idx].cells[2], c2)
    set_cell_section_label(table.rows[7].cells[0], '参加人员 / （签字）')
    set_cell_section_data(table.rows[7].cells[1], '年   月   日')
    set_cell_section_data(table.rows[7].cells[2], '年   月   日')

def add_monthly_table(rows_data):
    table = doc.add_table(rows=6, cols=3)
    table.style = 'Table Grid'
    for idx, item in enumerate(rows_data):
        label, c1, c2 = item
        set_cell_section_label(table.rows[idx].cells[0], label)
        set_cell_section_data(table.rows[idx].cells[1], c1)
        set_cell_section_data(table.rows[idx].cells[2], c2)
    set_cell_section_label(table.rows[4].cells[0], '参加人员 / （签字）')
    set_cell_section_data(table.rows[4].cells[1], '年   月   日')
    set_cell_section_data(table.rows[4].cells[2], '年   月   日')
    set_cell_section_label(table.rows[5].cells[0], '企业主要负责人 / （签字）')
    set_cell_section_data(table.rows[5].cells[1], '年   月   日')
    set_cell_section_data(table.rows[5].cells[2], '年   月   日')

def add_daily_record(date, risks):
    """8 月格式：标题 + 副标题 + 空段 + 检查日期 + 短空段 + 承诺 + 空段 + 表格"""
    add_title_daily("每日食品安全管控记录")
    add_subtitle_daily("（风险管控清单版本号：XNS202411）")
    add_p_empty()
    add_p_check_date(f"检查日期：{date}                记录编号：")
    add_p_blank_short()
    add_p_commitment("    本人承诺已根据食品安全风险管控清单全部条款内容进行检查，检查结果如下：□未发现问题，零报告；  □发现风险隐患，问题如下：")
    add_daily_table(date, risks)

# ==== 生成 9 月内容 ====
# 8 份日管控（无分页符，靠内容自然分页）
for date, risks in daily_records:
    add_daily_record(date, risks)
    # 8 月每份之间有 2-3 个空段
    add_p_empty()
    add_p_empty()
    add_p_empty()

# 3 份周排查
for date, period, rows_data in weekly_records:
    add_title_section("每周食品安全排查报告")
    add_subtitle_section("（风险管控清单版本号：XNS202411）")
    add_p_section_date(f"  排查日期：{date}                  报告编号：")
    add_weekly_table(period, rows_data)
    # 周之间 3 个空段
    add_p_empty()
    add_p_empty()
    add_p_empty()

# 1 份月调度
date, rows_data = monthly_record
add_title_section("每月食品安全调度会议纪要")
add_subtitle_section("（风险管控清单版本号：XNS202411）")
add_p_meeting(f"  会议时间：{date}   会议地点：总经理办公室     纪要编号：")
add_monthly_table(rows_data)

doc.save(OUT)
print("OK:", OUT)