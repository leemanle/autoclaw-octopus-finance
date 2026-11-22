"""
日期归位：
- T3 (现 9.23) → 改回 9.10。R1=经营户健康证年度复检 + 档案季度盘点；R2=入场销售者档案目录更新与协议归档
- T5 (9.18) R2 = 国庆前全场食品安全综合检查（替代原"夜间市场外围卫生回潮"——卫生回潮挪到周排查 9.21 整改措施里）
- T7 (现 9.24) → 改成 9.23。R1=食品安全管理人员 / 9 月 23 日参加宣城市快检培训；R2=食品安全事故处置 / 国庆节前一周食品安全应急联络表更新
- 周排查 9.21 (Table 10) 整改措施里加上"夜间外围摊点卫生回潮治理"
"""
from docx import Document

PATH = r'D:\大华市场\市场监督局（包括农残检测\食品安全管控记录表2026\食品安全管控记录表9月2026.docx'
doc = Document(PATH)


def set_p(p, txt):
    if p.runs:
        p.runs[0].text = txt
        for r in p.runs[1:]:
            r.text = ''
    else:
        p.add_run(txt)


def set_cell(cell, txt):
    set_p(cell.paragraphs[0], txt)


# === T3 改回 9.10 ===
tbl3 = doc.tables[3]
# 找"检查日期：2026.9.23"段落改回 9.10
for p in doc.paragraphs:
    if p.text.strip().startswith('检查日期：2026.9.23'):
        set_p(p, '检查日期：2026.9.10                记录编号：')
        print(f'改 T3 表头日期：{p.text[:50]}')
        break
# R1/R2 上报时间改回 9.10
set_cell(tbl3.rows[1].cells[5], '2026.9.10')
set_cell(tbl3.rows[2].cells[5], '2026.9.10')
# R2 内容改成"入场销售者档案目录更新与协议归档"
tbl3 = doc.tables[3]
set_cell(tbl3.rows[2].cells[1], '入场销售者管理')  # 风险类型
set_cell(tbl3.rows[2].cells[2], '入场销售者档案目录更新与协议归档')  # 描述
# C4 解决方法保留为"对全场经营户健康证开展 1 次年度复检..."
# 实际上原 R2 解决方法已经是健康证年度复检，要改成"完成入场销售者档案目录更新与档案归档"
set_cell(tbl3.rows[2].cells[4], '完成入场销售者档案目录更新、协议归档与目录索引建立')

# === T5 (9.18) R2 改成"国庆前全场食品安全综合检查" ===
tbl5 = doc.tables[5]
# R1 不动：场所及布局 / 国庆节前冷链设备专项排查
# R2 改成：
set_cell(tbl5.rows[2].cells[1], '场内检查')  # 风险类型
set_cell(tbl5.rows[2].cells[2], '国庆前全场食品安全综合检查')  # 描述
set_cell(tbl5.rows[2].cells[4], '国庆前对全场经营户开展拉网式检查，重点检查冷链、散装食品台账')  # 解决方法

# === T7 改 9.23 ===
tbl7 = doc.tables[7]
# 表头改 9.23
for p in doc.paragraphs:
    if p.text.strip().startswith('检查日期：2026.9.24'):
        set_p(p, '检查日期：2026.9.23                记录编号：')
        print(f'改 T7 表头日期：{p.text[:50]}')
        break
# R1 改成：食品安全管理人员 / 9 月 23 日参加宣城市快检培训
set_cell(tbl7.rows[1].cells[1], '食品安全管理人员')
set_cell(tbl7.rows[1].cells[2], '9 月 23 日参加宣城市快检培训')
set_cell(tbl7.rows[1].cells[4], '已参训 1 人次，归档培训记录与考核证明，更新培训档案')
set_cell(tbl7.rows[1].cells[5], '2026.9.23')
# R2 改成：食品安全事故处置 / 国庆节前一周食品安全应急联络表更新
set_cell(tbl7.rows[2].cells[1], '食品安全事故处置')
set_cell(tbl7.rows[2].cells[2], '国庆节前一周食品安全应急联络表更新')
set_cell(tbl7.rows[2].cells[4], '更新食品安全应急联络表（含市场监管局、街道、卫生院、经营户代表）；公示 9.22-9.24 农残抽检数据，张贴节日食品安全消费提示')
set_cell(tbl7.rows[2].cells[5], '2026.9.23')

# === 周排查 9.21 (Table 10) R5 整改措施加入"夜间市场外围卫生回潮治理" ===
tbl10 = doc.tables[10]
old_measure = tbl10.rows[5].cells[1].text.strip()
new_measure = old_measure.replace('督促月饼经营户 24 小时内完成下架登记', '夜间市场外围摊点卫生回潮治理；督促月饼经营户 24 小时内完成下架登记')
if old_measure == new_measure:
    # 没匹配上，原文可能已变化，强制添加
    new_measure = '夜间市场外围摊点卫生回潮治理；督促月饼经营户 24 小时内完成下架登记并按过期食品处置流程处理；抽检秋季时令水果全部合格；冷链设备专项排查完成 1 次'
set_cell(tbl10.rows[5].cells[1], new_measure)
set_cell(tbl10.rows[5].cells[2], new_measure)

# 9.21 周排查"本周排查"加一句
tbl10 = doc.tables[10]
old_thisweek = tbl10.rows[2].cells[2].text.strip()
if '夜间市场外围摊点卫生回潮' not in old_thisweek:
    new_thisweek = old_thisweek + '；夜间市场外围摊点卫生回潮治理'
    set_cell(tbl10.rows[2].cells[2], new_thisweek)

# 风险信息也加
tbl10 = doc.tables[10]
old_risk = tbl10.rows[3].cells[2].text.strip()
if '夜间市场外围摊点卫生' not in old_risk:
    new_risk = old_risk + '；夜间市场外围摊点卫生回潮带来卫生管理压力'
    set_cell(tbl10.rows[3].cells[2], new_risk)

doc.save(PATH)
print('\n已保存')