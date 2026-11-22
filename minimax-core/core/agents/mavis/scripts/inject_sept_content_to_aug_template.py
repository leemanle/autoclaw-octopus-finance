# -*- coding: utf-8 -*-
"""以 8 月 docx 为模板，按内容模式识别 paragraph/table，逐个替换为 9 月内容。"""
import shutil
from docx import Document
from docx.oxml.ns import qn

SRC = r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表8月2026.docx'
OUT = r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表9月2026.docx'

shutil.copy(SRC, OUT)
doc = Document(OUT)

# 9 月内容
sept_daily = [
    {'date': '2026.9.1', 'risks': [
        ('入场销售者管理', '9 月开学季，新入场经营户档案需及时建档', '☑是 □否',
         '梳理 9 月新入场经营户名单，完成入场销售者档案建档；对接辖区学校食堂采购，办理临时通行证'),
        ('入场查验', '秋季时令水果（葡萄、苹果、梨）批量上市，索证索票台账更新', '☑是 □否',
         '要求经营户补齐进货票据与产品质量合格凭证，新增水果类农产品质量安全协议更新归档'),
    ]},
    {'date': '2026.9.3', 'risks': [
        ('场内检查', '市场内排水沟清理不彻底，异味较大', '☑是 □否',
         '组织人员疏通全场排水沟 1 次，冲洗地面，落实每周深度清洁制度'),
        ('入场查验', '对当日新入场蔬菜开展农药残留快速检测', '☑是 □否',
         '抽检叶菜 8 批次、豆类 4 批次，检测结果全部合格，做好原始记录和公示'),
    ]},
    {'date': '2026.9.4', 'risks': [
        ('入场查验', '中秋月饼礼盒上市前资质与添加剂备案检查', '☑是 □否',
         '要求月饼经营户出示 SC 证、第三方检测报告；核对食品添加剂使用范围，完成月饼摊位备案登记'),
        ('信息公示', '中秋食品安全宣传栏更新与农残公示', '☑是 □否',
         '更新食品安全宣传栏 1 期，含中秋消费提示与举报电话；公示 9.1-9.3 农残抽检数据'),
    ]},
    {'date': '2026.9.10', 'risks': [
        ('场内检查', '中秋前糕点、熟食摊位保质期与冷藏温度专项检查', '☑是 □否',
         '对散装糕点、豆制品、熟食摊位开展保质期与冷藏温度专项检查，全部合格'),
        ('食品安全事故处置', '中秋节令食品应急处置预案演练', '☑是 □否',
         '组织食品安全员开展过期月饼应急处置演练 1 次，更新应急联络表'),
    ]},
    {'date': '2026.9.15', 'risks': [
        ('入场查验', '中秋前月饼专项抽检（防腐剂、甜味剂、色素）', '☑是 □否',
         '抽检月饼 8 批次，重点检测防腐剂、甜味剂、色素，结果全部合格并公示'),
        ('食品安全管理人员', '食品安全员参加市场监管局组织的业务培训', '☑是 □否',
         '已参训 1 人次，归档培训记录与考核证明，更新培训档案'),
    ]},
    {'date': '2026.9.18', 'risks': [
        ('场所及布局', '中秋前客流量加大，提前做好通道疏导与临时摊位扩容准备', '☑是 □否',
         '划定中秋高峰日临时采购通道与停车引导；提前对接经营户备货，确保中秋前一周供货充足'),
        ('场内检查', '中秋前夜间市场外围摊点卫生回潮，巡查加密', '☑是 □否',
         '与城管联动开展夜间巡查，劝离外围游商，确保场内经营秩序'),
    ]},
    {'date': '2026.9.20', 'risks': [
        ('入场查验', '秋季水果（梨、苹果、葡萄）集中上市，开展专项抽检', '☑是 □否',
         '抽检水果 12 批次，检测农药残留和糖度，结果全部合格并公示'),
        ('食品安全管理制度', '对照最新版管控清单开展制度自查', '☑是 □否',
         '完成食品安全管理制度目录更新，新增国庆节令食品应急处置预案'),
    ]},
    {'date': '2026.9.24', 'risks': [
        ('场内检查', '中秋前全场食品安全综合检查与冷链设备排查', '☑是 □否',
         '中秋前 1 天对全场经营户开展拉网式检查，重点检查冷链、散装、月饼台账'),
        ('信息公示', '中秋节当日农残快检结果与节日消费提示公示', '☑是 □否',
         '公示 9.22-9.24 农残抽检数据；张贴节日食品安全消费提示'),
    ]},
]

sept_weekly = [
    {'date': '2026.9.7', 'period': '9.1—9.7',
     'last_week': '8 月下旬中秋节食品安全专项检查各项措施落实到位；9 月开学季学校食堂采购临时通行证已办理',
     'this_week': '9 月新入场经营户建档、秋季水果集中上市索证索票更新、月饼礼盒备案检查',
     'risk_info': '9 月上中旬月饼摊位陆续进场销售，需提前完成备案登记',
     'cause': '节令食品上市集中，需提前对接经营户与上游供应，加强备案管理',
     'measure': '完成中秋月饼礼盒备案登记；更新食品安全宣传栏第一期；公示 9.1-9.3 农残抽检数据',
     'remark': '9 月上旬天气转凉，中秋节前市场月饼摊位陆续进场销售'},
    {'date': '2026.9.14', 'period': '9.8—9.14',
     'last_week': '中秋月饼礼盒备案登记全部完成；食品安全宣传栏第一期已更新并公示 9.1-9.3 农残抽检数据',
     'this_week': '中秋前糕点熟食摊位保质期与冷藏温度专项检查、节令食品应急预案演练',
     'risk_info': '中秋节令消费集中，糕点熟食库存压力增大；应急处置预案需提前演练',
     'cause': '节令消费高峰期叠加气温仍偏高，食品保质期与冷链管理需要持续关注',
     'measure': '糕点熟食摊位保质期与冷藏温度专项检查全部合格；开展过期月饼应急处置演练 1 次',
     'remark': '中秋节前气温仍偏高，重点关注糕点熟食保质期与冷链温度'},
    {'date': '2026.9.21', 'period': '9.15—9.21',
     'last_week': '中秋节前糕点熟食摊位保质期与冷藏温度专项检查全部合格；过期月饼应急处置演练完成',
     'this_week': '中秋前月饼专项抽检、客流量加大准备工作、夜间外围摊点卫生回潮治理',
     'risk_info': '中秋前一周月饼销售进入高峰，散装糕点与熟食库存压力增大；夜间市场外围游商回潮带来卫生管理压力',
     'cause': '中秋节令消费激增叠加中秋前一周备货高峰，需提前做好通道与冷链应对',
     'measure': '抽检月饼 8 批次全部合格；划定中秋高峰日临时采购通道；督促经营户备货充足；与城管联动夜间巡查',
     'remark': '中秋前一周月饼销售进入高峰，散装糕点与熟食库存压力增大'},
]

sept_monthly = {
    'date': '2026.9.23',
    'last_month': '8 月下旬中秋节食品安全专项检查各项措施落实到位。月饼礼盒备案登记、月饼专项抽检、节令食品应急演练、节前糕点熟食保质期检查全部完成；中秋节当天值班巡查保障有力',
    'summary_find': '9 月围绕中秋前备案+抽检+客流准备+保质期+应急演练、中秋节后下架与国庆节前冷链排查三条主线开展日管控 8 次，整改到位率 100%',
    'summary_week': '9 月周排查暴露的主要问题：1）中秋前部分月饼经营户对食品添加剂使用范围认识需加强；2）节后剩余月饼下架时效需进一步统一；3）国庆节前冷链设备负荷上升需专项排查',
    'arrange': '10 月进入国庆长假与重阳节时段：1）国庆假期值班值守与应急处置；2）秋季水果保鲜与冷链管理；3）重阳节令食品（糕点、营养品）检查；4）入场销售者档案季度更新与协议续签；5）全年食品安全工作总结与下一年度计划部署',
}

def replace_p_text(p, new_text):
    """替换段落文字（保留第一个 run 的格式）"""
    if not p.runs:
        p.add_run(new_text)
        return
    p.runs[0].text = new_text
    for r in p.runs[1:]:
        r.text = ''

def replace_cell_text(cell, new_text):
    """替换单元格文字"""
    for p in cell.paragraphs:
        replace_p_text(p, new_text)

# 直接遍历 body 子元素（按文档顺序）
body = doc.element.body

# 用 python-docx 包装
# 但 doc.paragraphs 和 doc.tables 不包含内嵌元素
# 需要手动映射：每个顶层 element（p 或 tbl）找到对应的 Paragraph/Table 对象

# 构建映射：从 XML element 到 python-docx 对象
all_paragraphs = doc.paragraphs
all_tables = doc.tables

# 但内嵌在表格里的 paragraph 也在 all_paragraphs 里
# 需要找"顶层"的 paragraph 和 table
# python-docx 的 paragraphs 包含所有 paragraph（顶层 + 表格内）
# 我们需要按 body 顺序找顶层元素

# 直接遍历 body 的子元素，对每个顶层 p 用 doc.paragraphs[i] 是不对的
# 改用：在迭代时跳过表格内的 p

# 用 body 顺序逐个处理
def get_text(elem):
    return ''.join(t.text or '' for t in elem.iter(qn('w:t')))

# 处理顶层段落和表格
p_iter = iter(all_paragraphs)
t_iter = iter(all_tables)

daily_idx = 0
weekly_idx = 0
phase = 'daily'

for child in body:
    if child.tag == qn('w:p'):
        # 是顶层段落
        # 但需要跳过表格里的段落（它们在 body 里也是顶层？不对，表格里的 p 在 tbl 里）
        # 顶层 p 就是 body 直接子元素的 p
        # 在 all_paragraphs 里按 body 顺序：包含顶层 + 表格内
        # 实际 python-docx 的 all_paragraphs 是按 body 顺序排的（包括表格内的 p）
        p = next(p_iter)
        text = p.text
        if text.startswith('每日食品安全管控记录'):
            replace_p_text(p, '每日食品安全管控记录')
        elif text.startswith('（风险管控清单版本号'):
            replace_p_text(p, '（风险管控清单版本号：XNS202411）')
        elif text.startswith('检查日期'):
            if phase == 'daily' and daily_idx < 8:
                d = sept_daily[daily_idx]['date']
                replace_p_text(p, f'检查日期：{d}                记录编号：')
        elif text.startswith(' 排查日期'):
            if phase == 'weekly' and weekly_idx < 3:
                d = sept_weekly[weekly_idx]['date']
                replace_p_text(p, f' 排查日期：{d}                  报告编号：')
        elif text.startswith(' 会议时间'):
            if phase == 'monthly':
                d = sept_monthly['date']
                replace_p_text(p, f'  会议时间：{d}   会议地点：总经理办公室     纪要编号：')
        elif text.startswith('每周食品安全排查报告'):
            replace_p_text(p, '每周食品安全排查报告')
        elif text.startswith('每月食品安全调度会议纪要'):
            replace_p_text(p, '每月食品安全调度会议纪要')
        elif text.startswith('    本人承诺已根据'):
            replace_p_text(p, '    本人承诺已根据食品安全风险管控清单全部条款内容进行检查，检查结果如下：□未发现问题，零报告；  □发现风险隐患，问题如下：')
    elif child.tag == qn('w:tbl'):
        table = next(t_iter)
        if phase == 'daily' and daily_idx < 8:
            risks = sept_daily[daily_idx]['risks']
            date = sept_daily[daily_idx]['date']
            headers = ['序号', '风险类型', '风险隐患描述', '是否解决', '解决方法（未解决原因和防范措施）', '上报时间']
            for j, cell in enumerate(table.rows[0].cells):
                replace_cell_text(cell, headers[j])
            for i in range(2):
                rtype, desc, solved, solution = risks[i]
                cols = [str(i+1), rtype, desc, solved, solution, date]
                for j, cell in enumerate(table.rows[i+1].cells):
                    replace_cell_text(cell, cols[j])
            empty_cols = ['3', '', '', '□是 □否', '', '']
            for j, cell in enumerate(table.rows[3].cells):
                replace_cell_text(cell, empty_cols[j])
            sign_cols = ['食品安全员（签字）', '食品安全员（签字）', '年    月    日', '年    月    日', '年    月    日', '年    月    日']
            for j, cell in enumerate(table.rows[4].cells):
                replace_cell_text(cell, sign_cols[j])
            daily_idx += 1
            if daily_idx == 8:
                phase = 'weekly'
        elif phase == 'weekly' and weekly_idx < 3:
            w = sept_weekly[weekly_idx]
            row_data = [
                ('排查覆盖日管控 / 日期范围', w['period'], w['period']),
                ('上周回顾', '上周问题整改 / 措施落实情况', w['last_week']),
                ('本周排查', '日管控发现问题及解决方法', w['this_week']),
                ('本周排查', '其他食品安全 / 风险信息', w['risk_info']),
                ('本周排查', '原因分析', w['cause']),
                ('整改措施', w['measure'], w['measure']),
                ('备    注', w['remark'], w['remark']),
                ('参加人员 / （签字）', '年   月   日', '年   月   日'),
            ]
            for i, row in enumerate(table.rows):
                if i >= len(row_data):
                    break
                cols = row_data[i]
                for j, cell in enumerate(row.cells):
                    if j < len(cols):
                        replace_cell_text(cell, cols[j])
            weekly_idx += 1
            if weekly_idx == 3:
                phase = 'monthly'
        elif phase == 'monthly':
            m = sept_monthly
            row_data = [
                ('上月回顾', '上月调度安排 / 落实情况', m['last_month']),
                ('本月总结', '日管控发现的 / 问题及解决方法', m['summary_find']),
                ('本月总结', '周排查问题出现的原因分析、整改措施', m['summary_week']),
                ('调度安排', m['arrange'], m['arrange']),
                ('参加人员 / （签字）', '年   月   日', '年   月   日'),
                ('企业主要负责人 / （签字）', '年   月   日', '年   月   日'),
            ]
            for i, row in enumerate(table.rows):
                if i >= len(row_data):
                    break
                cols = row_data[i]
                for j, cell in enumerate(row.cells):
                    if j < len(cols):
                        replace_cell_text(cell, cols[j])

doc.save(OUT)
print("OK:", OUT)
print(f'daily_idx={daily_idx}, weekly_idx={weekly_idx}')