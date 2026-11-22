# -*- coding: utf-8 -*-
"""生成《宁国市大华市场发展有限公司 市场管理奖罚办法》原稿版 docx 到桌面。"""
import os
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

OUT = r"C:\Users\Administrator\Desktop\宁国市大华市场发展有限公司_市场管理奖罚办法_v1_原稿.docx"

doc = Document()

style = doc.styles['Normal']
style.font.name = '宋体'
style.font.size = Pt(11)
style.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')

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

def add_h1(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.name = '黑体'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)

def add_p(text, indent=True):
    p = doc.add_paragraph()
    if indent:
        p.paragraph_format.first_line_indent = Cm(0.74)
    run = p.add_run(text)
    run.font.size = Pt(11)
    p.paragraph_format.line_spacing = 1.5
    return p

# —— 标题 ——
add_title("大华公司市场管理奖罚办法")
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("（原 手 稿 整 理 版）")
run.font.size = Pt(12)
run.font.italic = True

doc.add_paragraph()

# —— 一 ——
add_h1("一、")
add_p(
    "为切实加强文明经商，整治有序，严格管理，明确责任，服务民众，发扬精神，"
    "实施市场管理奖罚办法如下："
)
add_p("1、本公司员工无论上班时间内必须着装整洁，认真执行作息时间制度。（上下班时间见通知为准）")
add_p("2、在上班时间内必须坚守岗位，不得串岗脱岗、说话、玩手机等，努力做好本职工作，不得消极怠工。")
add_p("3、遵守工作时间，搞好清洁卫生，要勤勤到岗，做到公司环境整洁。")

# —— 二 ——
add_h1("二、市场管理、清洁人员职责范围：")
add_p("1、清洁人员应该对清扫地段、垃圾清倒，做到地面区内无菜叶、纸屑、脏水、地面整洁。")
add_p("2、市场工人看到车辆乱停乱放，认真做好过车区内各项清理工作。如有乱倒、态度不端正，扣完考核。乱倒垃圾视查清运，地面无积水，扫地人打扫，通道场地整洁。")
add_p("3、必须服从市场部针对蔬菜大棚外围、棚内清洁，执行认真后打扫。")
add_p("4、如发现违规现象，打架、骂人、肢体冲突，每次扣罚5元。情况严重和造成财物安全事故者除处罚外，造成连续6次者扣减全年奖金。")
add_p("5、如对违规领导干部予每次处罚（每次100元）当场纠正外，并负责人的处罚。")
add_p("6、对违纪员工罚款，领导现场开具的处罚单与本人签名或电话代通知。")

# —— 三 ——
add_h1("三、")
add_p(
    "市场部负责人应认真排查市场管理日常工作等各工作条件，督促员工遵纪守法，"
    "认真执行各项消防、安全不定期自查工作或讲评纠正工作，监督各岗合理等检查后工作，"
    "按当月奖惩核算，完备各班组工作职责考核。"
)

# —— 四 ——
add_h1("四、")
add_p(
    "市场部负责人按以上违反处罚负责责任人按规定扣分，"
    "担负起对他人安全告知，陪同市场部负责人相结合安全检查。"
)

# —— 五 ——
add_h1("五、")
add_p(
    "如本制度在执行中确有困难，请签订实施执行公布，公布处理所发生的违规事项，"
    "若有考核性处理，保证字据的真实性，手续自2026年9月起施行。"
)

# —— 落款 ——
doc.add_paragraph()
doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
run = p.add_run("大华市场管理处罚规定")
run.font.size = Pt(12)
run.font.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
run = p.add_run("2026年9月6日")
run.font.size = Pt(12)
run.font.bold = True

os.makedirs(os.path.dirname(OUT), exist_ok=True)
doc.save(OUT)
print("OK:", OUT)
