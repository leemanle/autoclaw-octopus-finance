# -*- coding: utf-8 -*-
"""v2 三页版：紧凑排版 + 内容压缩。"""
import os
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

OUT = r"C:\Users\Administrator\Desktop\宁国市大华市场发展有限公司_市场管理奖罚办法_v2.docx"

doc = Document()
style = doc.styles['Normal']
style.font.name = '宋体'
style.font.size = Pt(11)
style.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')

# 紧凑边距
for section in doc.sections:
    section.top_margin = Cm(1.8)
    section.bottom_margin = Cm(1.8)
    section.left_margin = Cm(2.2)
    section.right_margin = Cm(2.0)

def add_title(text, size=16):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.font.bold = True
    run.font.name = '黑体'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
    p.paragraph_format.space_after = Pt(0)

def add_h1(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.name = '黑体'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.2

def add_p(text, indent=True, line_spacing=1.2, space_after=0):
    p = doc.add_paragraph()
    if indent:
        p.paragraph_format.first_line_indent = Cm(0.7)
    run = p.add_run(text)
    run.font.size = Pt(11)
    p.paragraph_format.line_spacing = line_spacing
    p.paragraph_format.space_after = Pt(space_after)
    return p

# ===== 标题 =====
add_title("宁国市大华市场发展有限公司市场管理奖罚办法", size=16)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("（2026 年 9 月修订）")
run.font.size = Pt(10)
run.font.italic = True
p.paragraph_format.space_after = Pt(2)

# ===== 一 =====
add_h1("一、目的与依据")
add_p("为加强文明经商、整治秩序、严格管理、明确责任，依据《202__年度大华市场经营行为承诺书》所列卫生、经营秩序、文明经营、食品安全四类行为规范作为日常检查与考核标准，结合本公司实际，制定本办法。")

# ===== 二 =====
add_h1("二、适用范围")
add_p("本办法适用于本公司市场管理员、保洁员、市场部负责人及与市场日常管理相关的内勤人员。市场内经营户的日常管理按《经营户承诺书》执行，不适用本办法。")

# ===== 三 =====
add_h1("三、共同要求")
add_p("1. 员工上班时间内须着装整洁，认真执行作息时间制度。（上下班时间以公司通知为准）")
add_p("2. 上班时间内须坚守岗位，不得干私活、脱岗、玩手机，努力做好本职工作，不得消极怠工。")
add_p("3. 遵守上下班时间、请销假、考勤制度及公司各项规章制度，爱护公物。")

# ===== 四 =====
add_h1("四、市场管理、清洁人员职责范围")
add_h1("（一）清洁人员")
add_p("1. 及时清扫包干区地面，垃圾及时运输，做到包干区内无杂物、无垃圾、无脏水、地面整洁。")
add_p("2. 公共区域（通道、摊位空地、大棚内外、停车场、过车道等）按《经营户承诺书》卫生条款标准执行保洁，做到垃圾袋装化、密闭运输、不露天堆放。")
add_p("3. 服从市场部对蔬菜大棚、外围摊位的统一巡查及管理。")

add_h1("（二）管理人员")
add_p("1. 恪尽职守，坚守岗位，认真做好包干区内的各项管理工作。")
add_p("2. 按《经营户承诺书》检查标准，对包干区内经营户以下行为进行监督管理：")
add_p("（1）卫生：商品摆放整齐，不乱扔垃圾，不乱倒污水，摊位前、后 2 米责任区保持整洁。")
add_p("（2）秩序：不占道经营或堆放物品，经营用房以屋檐滴水槽为界、摊位以不出摊位为准；不私拉乱接电线，不违规使用明火或大功率电器，不占用公共通道或空摊位宰杀作业；鸡笼、鸭笼不得放置在隔离区外。")
add_p("（3）交通：车辆停放有序，不在闲置摊位和消防通道内停放；装载鲜活水产车辆须接管排放废水。")
add_p("（4）文明经营：亮证经营，不超范围，不销售过期、变质、\"三无\"及假冒伪劣商品，不短斤少两；做好进货销售台账；疫情畜禽产品及时上报。")
add_p("（5）广告牌匾：门头牌匾、遮阳篷须经市场管理部审批后规范安装，不擅自乱挂、乱画广告招牌。")
add_p("3. 包干区内地面无积水，人行通道通畅整洁。")
add_p("4. 服从市场部对蔬菜大棚、外围摊位的例行巡查及管理。")

add_h1("（三）包干人责任与处罚")
add_p("1. 包干区内出现经营户违规，管理人员未及时发现、未及时处理的，追究包干人责任，每次罚款 50 元。")
add_p("2. 一个季度内累计 3 次未及时处理的，扣除本季度奖金（按年终奖折算）。")
add_p("3. 累计 6 次未及时处理的，扣除全年奖金。")
add_p("4. 对违规经营户完成处罚（每次 100 元）并予以纠正的，免除包干人本次处罚。")
add_p("5. 对违规经营户的监督和处罚，须有现场记录仪视频或经营户签字的《违规处罚通知单》等佐证材料。")

# ===== 五 =====
add_h1("五、市场部负责人职责")
add_p("1. 认真安排市场日常管理工作，监督员工遵纪守法，认真执行作息和考勤制度。")
add_p("2. 不定期召集员工讨论评价过往工作，总结经验，合理布置以后工作，完善管理工作职责内容。")
add_p("3. 对所辖区域的安全、卫生、秩序、食品安全负总责。")
add_p("4. 牵头食品、消防、安全等专项检查，配合主管部门执法。")

# ===== 六 =====
add_h1("六、连带与问责")
add_p("1. 市场部负责人对以上员工违规处罚负连带责任。")
add_p("2. 员工违规奖金扣完时，扣除市场部负责人年终奖金的        %（由公司确定）。")
add_p("3. 因瞒报、晚报、漏报导致食品、消防、安全等重大问题扩大的，按公司《员工奖惩条例》另行处理。")

# ===== 七 =====
add_h1("七、附则")
add_p("1. 本办法自 2026 年 9 月 1 日起施行。")
add_p("2. 本办法由公司市场部负责解释。")
add_p("3. 执行过程中如遇困难，由公司研究修订；公平、公正处理所发生的违规事宜。")

# ===== 落款 =====
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
run = p.add_run("宁国市大华市场发展有限公司    2026 年 9 月 6 日")
run.font.size = Pt(11)
run.font.bold = True
p.paragraph_format.space_before = Pt(6)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
doc.save(OUT)
print("OK:", OUT)
