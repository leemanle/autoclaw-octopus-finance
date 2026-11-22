# -*- coding: utf-8 -*-
"""生成《宁国市大华市场发展有限公司 市场管理奖罚办法》docx 到桌面。"""
import os
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

OUT = r"C:\Users\Administrator\Desktop\宁国市大华市场发展有限公司_市场管理奖罚办法_v2.docx"

doc = Document()

# 默认中文字体
style = doc.styles['Normal']
style.font.name = '宋体'
style.font.size = Pt(11)
style.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')

# 页边距
for section in doc.sections:
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(3.0)
    section.right_margin = Cm(2.5)

def add_title(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.size = Pt(20)
    run.font.bold = True
    run.font.name = '黑体'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')

def add_subtitle(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.name = '黑体'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')

def add_h1(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = '黑体'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)

def add_h2(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.name = '黑体'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)

def add_p(text, indent=True, bold=False):
    p = doc.add_paragraph()
    if indent:
        p.paragraph_format.first_line_indent = Cm(0.74)
    run = p.add_run(text)
    run.font.size = Pt(11)
    if bold:
        run.font.bold = True
    p.paragraph_format.line_spacing = 1.5
    return p

# —— 封面标题 ——
add_title("宁国市大华市场发展有限公司")
add_subtitle("市场管理奖罚办法")

doc.add_paragraph()  # 空行

# —— 第一章 总则 ——
add_h1("第一章  总则")

add_p("第一条  目的与依据")
add_p(
    "为加强公司文明经商、整治秩序、严格管理、明确责任、服务群众、发扬企业精神，"
    "依据《劳动法》《消防法》《治安管理处罚法》《消费者权益保护法》及公司相关管理制度，"
    "结合本公司实际，特制定本办法。"
)

add_p("第二条  适用范围")
add_p("本公司全体员工、市场管理员、保洁员、值班人员及外协保洁人员。")

add_p("第三条  施行日期")
add_p("本办法自 2026 年 9 月 1 日起施行，原有相关制度与本办法不一致的，以本办法为准。")

# —— 第二章 员工行为规范 ——
add_h1("第二章  员工行为规范")

add_p("第四条  仪容仪表与考勤")
add_p("（一）全体员工上岗期间须着装整洁、佩戴工牌，仪容仪表端庄。")
add_p("（二）严格遵守公司作息时间制度（上下班时间以公司通知为准），不得迟到、早退、旷工。")

add_p("第五条  岗位纪律")
add_p("（一）上班期间须坚守岗位，不得串岗、擅离、脱岗、扎堆聊天、玩手机。")
add_p("（二）努力做好本职工作，不得消极怠工。")

add_p("第六条  卫生责任")
add_p("（一）遵守工作时间，搞好责任区清洁卫生，做到地面无菜叶、无纸屑、无脏水、无积水。")
add_p("（二）公共通道、蔬菜大棚外围、棚内均须保持干净整洁。")
add_p("（三）服从市场部统一调度，完成大棚及公共区域清扫任务。")

# —— 第三章 设施与环境管理 ——
add_h1("第三章  设施与环境管理")

add_p("第七条  车辆与场地")
add_p("（一）市场内车辆须按指定区域停放，不得乱停乱放。")
add_p("（二）保洁员对过车通道及周边区域须随脏随扫，发现乱倒垃圾、堵塞通道等情况及时处理。")
add_p("（三）对乱倒垃圾、态度不端正者，按第四章罚则处理。")

add_p("第八条  安全生产")
add_p("（一）市场部负责人须组织人员开展消防、卫生、安全等不定期自查。")
add_p("（二）对发现的安全隐患须当场纠正、当场整改，必要时通报处理并上报。")

# —— 第四章 违规处罚标准 ——
add_h1("第四章  违规处罚标准")

add_p("第九条  一般违规")
add_p("（一）发现打架、骂人、肢体冲突等违规现象，每次扣罚 5 元。")
add_p("（二）情节严重或造成财物损失、安全事故的，除按本条处罚外，另行追究相应责任。")

add_p("第十条  累犯处理")
add_p("同一员工全年累计违规达 6 次者，除每次扣罚外，另扣减全年奖金。")

add_p("第十一条  领导连带")
add_p(
    "对违规的领导干部或责任人，除按每次 100 元的标准予以处罚外，"
    "并依规追究所在部门负责人管理责任。"
)

add_p("第十二条  处罚程序")
add_p("（一）现场违规由当班领导或市场部负责人开具《处罚通知单》。")
add_p("（二）受罚人当场签字确认；如拒绝签字，由两名以上见证人签字后，拍照存档并电话通知本人。")
add_p("（三）罚款当月从工资中扣除。")

# —— 第五章 监督与责任 ——
add_h1("第五章  监督与责任")

add_p("第十三条  市场部负责人职责")
add_p("（一）日常管理：每日排查市场管理情况，做好值班记录。")
add_p("（二）员工管理：督促员工遵纪守法，开展岗前教育与定期培训。")
add_p("（三）考核管理：定期对各班组、各岗位工作进行考核，按考核结果兑现奖惩。")
add_p("（四）安全责任：检查、督导各项安全工作落实，承担本部门安全管理责任。")

add_p("第十四条  责任追究")
add_p(
    "市场部负责人对本办法执行情况负总责。"
    "对执行不力、隐瞒不报、玩忽职守的，依公司管理制度追究相应责任。"
)

# —— 第六章 附则 ——
add_h1("第六章  附则")

add_p("第十五条  奖罚结合")
add_p(
    "对严格执行本办法、积极维护市场秩序、拾金不昧、举报重大隐患等行为，"
    "公司将给予表彰和奖励。"
)

add_p("第十六条  解释权")
add_p("本办法由公司市场部负责解释。")

add_p("第十七条  施行日期")
add_p("本办法自 2026 年 9 月 1 日起施行。")

# —— 落款 ——
doc.add_paragraph()
doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
run = p.add_run("宁国市大华市场发展有限公司")
run.font.size = Pt(12)
run.font.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
run = p.add_run("2026 年 9 月 6 日")
run.font.size = Pt(12)
run.font.bold = True

# 保存
os.makedirs(os.path.dirname(OUT), exist_ok=True)
doc.save(OUT)
print("OK:", OUT)
