# -*- coding: utf-8 -*-
"""
《关于加强消费基础设施建设 促进消费投资良性互动的指导意见》
政策要点摘编 及 宁国市大华中心菜市场（民营）政策利用路径建议
"""
import os
import hashlib
_orig_md5 = hashlib.md5
def _md5(*a, **kw):
    kw.pop("usedforsecurity", None)
    return _orig_md5(*a, **kw)
hashlib.md5 = _md5

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib import colors

BASE = r"C:\Users\Administrator\Desktop"
NAME = "关于加强消费基础设施建设促进消费投资良性互动的指导意见政策要点摘编及大华市场政策利用路径建议"
OUT_PDF = os.path.join(BASE, NAME + ".pdf")
OUT_DOCX = os.path.join(BASE, NAME + ".docx")

FD = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("FS", os.path.join(FD, "simfang.ttf")))
pdfmetrics.registerFont(TTFont("HT", os.path.join(FD, "simhei.ttf")))
pdfmetrics.registerFont(TTFont("KT", os.path.join(FD, "simkai.ttf")))

M, M2, M3 = 18 * mm, 20 * mm, 18 * mm
W = A4[0] - 2 * M

st_title = ParagraphStyle("t", fontName="HT", fontSize=19, leading=30, alignment=TA_CENTER,
                          spaceAfter=4, wordWrap="CJK")
st_sub = ParagraphStyle("ts", fontName="KT", fontSize=12, leading=20, alignment=TA_CENTER,
                        spaceAfter=4, wordWrap="CJK")
st_src = ParagraphStyle("src", fontName="FS", fontSize=9.5, leading=15, alignment=TA_CENTER,
                        spaceAfter=10, wordWrap="CJK")
st_h1 = ParagraphStyle("h1", fontName="HT", fontSize=14, leading=24, spaceBefore=9,
                       spaceAfter=5, wordWrap="CJK")
st_p = ParagraphStyle("p", fontName="FS", fontSize=11, leading=19, alignment=TA_JUSTIFY,
                      firstLineIndent=22, spaceAfter=2, wordWrap="CJK")
st_pb = ParagraphStyle("pb", fontName="FS", fontSize=11, leading=19, alignment=TA_JUSTIFY,
                       spaceAfter=2, wordWrap="CJK")
st_note = ParagraphStyle("n", fontName="KT", fontSize=10, leading=17, alignment=TA_JUSTIFY,
                         firstLineIndent=20, spaceAfter=2, wordWrap="CJK")
# 表格内
st_th = ParagraphStyle("th", fontName="HT", fontSize=9.5, leading=14, alignment=TA_CENTER, wordWrap="CJK")
st_td = ParagraphStyle("td", fontName="FS", fontSize=9, leading=13.5, alignment=TA_LEFT, wordWrap="CJK")
st_tdk = ParagraphStyle("tdk", fontName="KT", fontSize=9, leading=13.5, alignment=TA_LEFT, wordWrap="CJK")
st_tdb = ParagraphStyle("tdb", fontName="HT", fontSize=9, leading=13.5, alignment=TA_LEFT, wordWrap="CJK")

def P(t, s=st_td): return Paragraph(t, s)

story = []
A = story.append

A(Paragraph("《关于加强消费基础设施建设 促进消费投资良性互动的指导意见》", st_title))
A(Paragraph("政策要点摘编及宁国市大华中心菜市场（民营）政策利用路径建议", st_title))
A(Paragraph("——依据发改就业〔2026〕1508号，并结合《宁国市2026年加快发展生活性服务业促进消费提升实施方案》", st_sub))
A(Paragraph("编制日期：2026年11月2日", st_src))

# ============ 一 ============
A(Paragraph("一、我市场基本情况与政策适用性判定", st_h1))
A(Paragraph("（一）基本情况。宁国市大华市场发展有限责任公司（统一社会信用代码913418817467873726），注册地宁国市东风路，"
            "系自然人投资或控股的民营有限责任公司，注册资本300万元，法定代表人张志诒。市场于2003年由企业投资5000万元自建，"
            "2004年开业，占地50亩，摊位1100余个（含市场大厅、批发大厅、露天摊位），配套5亩停车场，日均交易额约600万元、"
            "年交易额约20亿元，带动就业1500余人，为宁国市城区中心农贸市场，隶属西津街道北园社区。", st_p))
A(Paragraph("（二）既有基础。市场已配备电子交易系统、冷藏保鲜库、果蔬农药残留检测设施；已实施“文明菜市”改造，"
            "增设垃圾分类回收站、公平秤、投诉站，统一经营户标牌与着装管理；先后完成食品安全管控记录表、"
            "制度与承诺书、创建文明市场材料等系列规范建设。", st_p))
A(Paragraph("（三）适用性判定（关键）。本市场为民营企业，不属于政府投资主体，不能直接向国家发展改革委、财政部门"
            "申报国债、专项债、中央预算内投资等财政性资金。但该文件第十八条明确“积极引导社会资本依法合规参与消费基础设施"
            "建设”，即为民营企业预留了合法参与通道。因此我市场的正确打法是：", st_pb))
A(Paragraph("　　1. 不是“向政府要钱”，而是“替政府把项目做出来”——由主管部门立项申报，我市场作为实施主体或社会资本方承接落地；", st_pb))
A(Paragraph("　　2. 不是“等文件兑现”，而是“先形成项目、争取进盘子”——主动向发改、商务、市场监管等主管部门报项目建议；", st_pb))
A(Paragraph("　　3. 不是“只靠财政补助”，而是“三条腿走路”——财政资金 + 经营权质押融资 + 自有资金改造。", st_pb))

# ============ 二 ============
A(Paragraph("二、国家层面可对接条款与我市场对应关系", st_h1))
t2_head = ["文件条款", "政策要求要点", "我市场对应与现有基础", "缺口与争取方式"]
t2 = [
 ["第一条\n加强城乡商品交易市场建设",
  "推动农产品批发市场、农贸市场、农村集贸市场等提档升级；完善市场摊位、给排水、供电、照明、垃圾处理等配套设施；推广电子结算、智能称重、无感支付、溯源管理等数字化应用",
  "市场摊位1100余个，已配电子交易系统；给排水、供电、照明、垃圾处理均属老旧待改项",
  "打包为“大华市场基础设施提档升级项目”，分项测算投资，配套智慧化改造（无感支付、智能称重、溯源管理）"],
 ["第二条\n支持线下消费商业设施设备更新",
  "支持商业综合体、购物中心、百货店、大型超市等更新空调、电梯、供热、冷藏、供电、照明、安防等设备",
  "现有冷藏保鲜库、照明、供电、安防监控、冷库设备均有更新需求，可形成设备清单",
  "对接“设备更新”贴息贷款口径，以设备投资额申请信贷贴息；与商务局申报改造项目争取财政补助"],
 ["第十条、十一条\n停车设施与充电设施",
  "新建停车楼、公共停车场、停车泊位；建设立体停车设施、智慧停车管理平台；新建改扩建停车场配套充电基础设施，支持社会资本参与建设运营",
  "已有5亩停车场、1100摊位人流基数，充电需求真实；停车场经营权、收费收益归公司所有，属可测算现金流",
  "停车+充电可作“建设运营一体”整体向银行融资；充电设施建成后由社会资本参与运营，兼具自营收益与政策加分"],
 ["第十三条\n构建高效冷链物流体系",
  "推进国家骨干冷链物流基地、区域冷链集散中心建设；产地预冷、低温加工分拣、产地冷藏保鲜；支持商业企业建设小型冷藏库、移动冷库；建设县域冷链集配中心、乡镇冷链服务站、村级冷藏点",
  "已有冷藏保鲜库和冷库摊位；本市场为皖苏浙边界农特产品集散地，产地集散功能具备",
  "向交通、农业农村、供销部门申报“产地低温仓储设施”“冷链集配中心”类项目，争取市级与上级专项"],
 ["第十四条\n健全县乡村三级物流体系",
  "发挥县级物流配送中心服务功能，与县域商业综合体、电商园区、农产品批发市场联动衔接；推动村级物流服务站点应建尽建，依托便民超市、卫生室、电商服务站建设综合便民服务站、村级快递服务点",
  "市场位于城区、紧邻居民区和乡镇农产品集散通道，具备承接县级配送与村级代收的天然节点条件",
  "与市供销社、市邮政分公司对接，争取承接村级综合便民服务站（快递代收+便民服务），争取运营补助"],
 ["第十五条\n加强检验检测设施建设",
  "完善市级综合消费检验检测中心功能配置，配齐理化、微生物、重金属、农兽药残留、添加剂筛查等专业设备；健全县级基础性检验检测站点；支持简易快速检测室、便民检测服务站建设；支持农产品批发市场、农贸市场、大型超市配套建设现场快检室、检测点位；鼓励第三方检测机构下沉布局",
  "市场已配备果蔬农残检测设施并承担检测工作，有人员、场地、运行数据基础，是全文与我市场契合度最高的一条",
  "主攻方向：争取财政出资配置快检室与检测设备，市场提供场地并承担运维，形成“政府配设备、市场出场地、第三方运营检测”的共建模式；同步申报区域性检验检测公共服务平台"],
 ["第十六条\n加快数字化消费设施全覆盖",
  "推进5G、千兆光网、物联网、云计算深度覆盖；支持建设智慧商圈、智慧市场、智慧店铺；普及智能收银、自助服务终端、智能电子价签；建设农产品产销对接平台、线上线下融合消费平台",
  "已有电子交易系统与智慧农商城对标对象；本地《实施方案》明确“2027年实现城区即时零售网点全覆盖”",
  "抢在2027年前完成美团、京东即时零售接入，把“智慧市场”做成可验收的政府任务；同时申报农产品产销对接平台落地我市场"],
 ["第十七条\n加强绿色消费设施建设改造",
  "大力发展绿色市场、绿色街区、绿色商场、绿色酒店；推动节能降碳改造，推广节能空调、高效照明、节水器具、智能化节电控制系统、可再生能源利用设施；鼓励建设垃圾分类回收点、可循环包装回收点、废旧物资回收驿站、专业化绿色化分拣中心、二手商品市场",
  "已建垃圾分类回收站；照明、空调、给排水、垃圾处理均为老旧设备，节能改造空间大",
  "以“创建绿色市场”为主线申报改造项目；同步布局废旧物资回收驿站与可循环包装回收点，形成可持续经营的小业态"],
 ["第十八条\n拓展投资渠道",
  "统筹用好中央和地方各类资金渠道；发挥新型政策性金融工具、不动产投资信托基金作用；引导金融机构按市场化、法治化原则提供信贷支持；积极引导社会资本依法合规参与消费基础设施建设",
  "市场年交易额20亿元、现金流稳定、资产权属清晰（自建物业），具备承贷基础",
  "本条即民营 participation 的直接依据。资金来源三选一或组合：政府立项投资、产权及收益权质押贷款、引入社会资本合作"],
 ["第十九条、第二十条\n协同联动与项目管理",
  "优化审批流程，统筹做好规划衔接、用地保障等工作；加强“软建设”，强化对各类资金支持项目的全过程监管，定期开展建设运营成效评估",
  "现有食品安全管控记录表、制度与承诺书体系，正是“软建设”与“全过程监管”所需的过程性台账",
  "把我市场既有的记录表、台账、承诺书体系包装为项目“软建设”支撑材料，作为项目申报附件一并提交；用地保障条款可用于协调改扩建审批"],
]
data2 = [[P(x, st_th) for x in t2_head]] + [[P(c, st_tdb if i == 0 else st_td) for i, c in enumerate(r)] for r in t2]
tb2 = Table(data2, colWidths=[W * 0.13, W * 0.31, W * 0.26, W * 0.30], repeatRows=1)
tb2.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 0.4, colors.black),
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8E8E8")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
    ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]))
A(tb2)

# ============ 三 ============
A(Paragraph("三、宁国市层面已明确的配套政策与资金池（能直接落地的部分）", st_h1))
A(Paragraph("依据《宁国市2026年加快发展生活性服务业促进消费提升实施方案》（宁国市人民政府办公室行政规范性文件），"
            "与本市场直接相关、且责任单位已明确的有以下若干项：", st_p))
t3_head = ["本地政策／资金", "责任单位", "我市场具体用法", "时间节点"]
t3 = [
 ["整合设立不少于1000万元专项引导资金，统筹用于生活性服务业提升",
  "市财政局（会同发改委）",
  "我市场提档升级项目争取进入该资金盘子，是最直接的地方财政通道；由主管部门牵头申报、我市场提供项目材料",
  "按方案年度任务推进，窗口紧"],
 ["积极争取超长期特别国债、中央预算内投资等资金支持，保障重大项目及配套基础设施建设",
  "市发改委、各相关单位、市财政局",
  "我市场不能直接申报，须由发改部门立项后实施。可提请其将“大华市场基础设施提档升级”纳入市级重大项目配套",
  "随年度申报计划"],
 ["鼓励金融机构拓宽生活性服务业企业贷款抵质押品种类和范围",
  "国金局宁国支局、市财政局",
  "★民营最现实的一条。可将5亩停车场的经营权、摊位租赁收益权、冷链仓库租金收益权等作为抵质押品申请融资，破解“抵押物只有房子、租约不算数”的老问题",
  "可即行对接"],
 ["引导商业银行扩大信用贷款、增加首贷户，推广“信易贷”",
  "市财政局、市发改委等",
  "门槛最低的信用融资通道，适合先做小额设备更新（照明、冷藏设备、监控）",
  "可即行对接"],
 ["实施乡镇商贸中心、农贸市场等业态融合发展，配套餐饮、快递、农资等便民服务",
  "相关乡镇街道、市商务局",
  "我市场所在的西津街道即为责任单位。可借街道名义提需求：引入快递、农机具、农资供应等业态，填补市场配套缺口",
  "按方案推进"],
 ["培育银发经济，推动商超、农贸市场适老化改造，布局“社区养老服务+便民消费”网点",
  "市商务局、市文旅局、市民政局",
  "低成本高契合。结合既有“文明菜市”基础，增设适老化改造与便民服务点（助餐、理发、代办、量血压），可叠加为民政服务补贴",
  "按方案推进"],
 ["冷链物流体系健全完善：建设产地低温仓储设施1个，完善预冷、分拣、包装、冷藏配送全链条",
  "市交通局、市农业农村局、市林业发展中心、市发改委、市供销社、相关乡镇街道",
  "我市场已有冷藏保鲜库与集散功能，可申报为产地低温仓储设施承载点，承接山核桃、生鲜果蔬的预冷与冷藏",
  "2026年12月底前"],
 ["支持商超、便利店、生鲜门店接入美团、京东等线上平台",
  "市商务局",
  "★硬指标任务。2027年实现城区即时零售网点全覆盖，我市场若不接入即为短板，须列入年度工作计划",
  "2027年全覆盖"],
 ["全年发放市本级促消费资金400万元，力争带动消费2500万元",
  "市商务局",
  "以“徽动消费 乐享宁国”消费券活动参与商户身份接入，零售类消费券全额满减对我市场经营户直接受益",
  "按年度活动安排"],
 ["完成凤形智慧农商城功能升级，打造“智慧交易+冷链仓储+物流配送”一体化农产品交易平台",
  "市商务局",
  "既是竞争也是机会。宜主动错位，把我市场定位为“主城区中心菜市场+社区便民服务+即时零售节点”，以差异化定位向商务局争取单独任务",
  "2026年12月底前"],
]
data3 = [[P(x, st_th) for x in t3_head]] + [[P(c, st_tdb if i == 0 else st_td) for i, c in enumerate(r)] for r in t3]
tb3 = Table(data3, colWidths=[W * 0.27, W * 0.16, W * 0.42, W * 0.15], repeatRows=1)
tb3.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 0.4, colors.black),
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8E8E8")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
    ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]))
A(tb3)

# ============ 四 ============
A(Paragraph("四、民营身份下的五条可行路径（核心）", st_h1))
paths = [
 ("路径一：政府立项、民营实施",
  "把我市场的改造需求做成一份规范的项目建议书（投资测算、分项清单、场地手续、运营方案、绩效指标），"
  "报市发改、商务部门，争取由政府立项、纳入年度项目盘子，财政资金解决公共配套部分（快检室、给排水、垃圾处理、"
  "照明等），我市场承担建设实施与后续运营。这是财政资金唯一能合法进入我市场的路径——钱给的是“项目”，不是“企业”。"),
 ("路径二：政府出资、市场出场地（共建）",
  "对应第十五条快检室与检测点位：争取财政出资配置检测设备，我市场提供现有检测用房与人员，第三方机构提供检测服务，"
  "服务费按市场化机制收取。参照国务院食安办与市场监管总局的快检室建设惯例，此模式在多地已有落地基础，可行性高、"
  "争议小、见效快，是建议最先推动的一条。"),
 ("路径三：经营权与收益权质押融资",
  "对应宁国市“鼓励金融机构拓宽生活性服务业企业贷款抵质押品种类和范围”。我市场可打包三类可测算现金流："
  "①5亩停车场的经营权与收费收益；②1100余个摊位的租赁收益权；③冷藏保鲜库的对外仓储租金。"
  "以未来若干年的收益权作质押，向国金局宁国支行或本地农商行申请专项贷款，同时叠加“信易贷”信用额度补足缺口。"
  "此路径不依赖财政资金、可自主启动，应与路径一并行推进。"),
 ("路径四：与地方国企合作对接",
  "《实施方案》中“乡投集团”“宁阳控股”多次作为责任单位出现，二者是承接政府投资任务的市场化平台。"
  "我市场可主动对接，探讨以“国企投资建设运营 + 我市场输出管理运营经验”或“我市场出资产与团队 + 国企出资金与政府资源”"
  "的合作模式，从而在不丧失运营权的前提下接入政府项目资源与财政资金。"),
 ("路径五：设备更新贴息",
  "对应第二条。冷库制冷设备、照明、供电、安防监控、冷链设施等单台价值高、清单清晰，符合设备更新再贷款贴息的政策口径。"
  "建议单独梳理设备更新清单，与金融机构对接贴息融资，并同步作为改造项目申报书的附件，提高财政补助争取的成功率。"),
]
for i, (h, b) in enumerate(paths, 1):
    A(Paragraph("（%s）%s" % (cn_i := "一二三四五"[i-1], h), st_h1))
    A(Paragraph(b, st_p))

# ============ 五 ============
A(Paragraph("五、近期行动清单（建议两个月内完成）", st_h1))
t5_head = ["时间", "动作", "对接单位", "产出"]
t5 = [
 ["11月上旬", "编制《大华市场消费基础设施提档升级项目建议书》，含总投资测算、分项清单、绩效指标与实施主体说明",
  "内部先定稿", "项目建议书（申报附件底稿）"],
 ["11月上旬", "以书面形式报送项目建议，申请纳入市级／县级消费基础设施项目盘子",
  "市发改委、市商务局、西津街道", "项目入库或列入储备"],
 ["11月中旬", "将快检室／检测点位单列为“政府配设备、市场出场地”共建项目专题汇报",
  "市市场监管局、市财政局", "共建方案与设备配置清单"],
 ["11月中旬", "洽谈停车经营权、摊位收益权、冷库租金收益权质押融资及信易贷额度",
  "国金局宁国支局、农商行、国有大行宁国支行", "融资意向与授信方案"],
 ["11月中旬", "与乡投集团、宁阳控股探讨合作模式，争取以国企平台身份申报项目",
  "乡投集团、宁阳控股", "合作意向备忘"],
 ["11月下旬", "完成美团／京东即时零售接入方案并申报；同步启动设备更新清单梳理",
  "市商务局；设备供应商", "即时零售上线；设备更新清单"],
 ["12月底前", "对接产地低温仓储设施项目；核实市本级促消费资金与消费券活动参与资格",
  "市交通局、市农业农村局、市供销社、市商务局", "冷链项目申报材料；消费券参与资格确认"],
 ["持续", "把食品安全管控记录表、制度与承诺书等过程性台账整理成项目“软建设”支撑材料",
  "内部", "随项目报批一并提交的制度与台账汇编"],
]
data5 = [[P(x, st_th) for x in t5_head]] + [[P(c, st_td) for c in r] for r in t5]
tb5 = Table(data5, colWidths=[W * 0.11, W * 0.42, W * 0.24, W * 0.23], repeatRows=1)
tb5.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 0.4, colors.black),
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8E8E8")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
    ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]))
A(tb5)

# ============ 六 ============
A(Paragraph("六、风险提示", st_h1))
risks = [
 "文件本身不直接给钱，给的是建设方向和投融资渠道。真正有钱的是地方实施细则、项目库和年度申报通知，须盯住市发改委、市商务局的发文。",
 "财政性资金（国债、专项债、中央预算内投资、市级引导资金）的申报主体是政府或项目单位，民营企业不能作为申报主体直接申报；找部门立项才是正路，直接去要钱会被挡回。",
 "宁国市《实施方案》中冷链、凤形智慧农商城、宁云数智物流园等多项任务时限为2026年12月底前，距今不足两个月，须抢时间，不能按常规节奏走。",
 "“加快城北农贸市场建设”为市商务局另一条任务线，与我市场并非同一项目；凤形智慧农商城的“智慧交易+冷链仓储+物流配送”定位与我市场存在同质竞争，宜主动错位并向主管部门争取单独任务，避免被动。",
 "“软建设”不等于台账越多越好。项目获批后需接受全过程监管和建设运营成效评估，我市场现有记录表体系须按评估口径整理，确保台账可查、数据可核、责任可追溯。",
 "对外报送材料涉及投资额、收益测算等经营数据，报送前应经内部审定，避免口径不一致被主管部门质疑，反而影响项目入库。",
]
for r in risks:
    A(Paragraph("◆ " + r, st_note))

A(Spacer(1, 10))
A(Paragraph("资料来源：① 国家发展改革委等部门《关于加强消费基础设施建设 促进消费投资良性互动的指导意见》"
            "（发改就业〔2026〕1508号，2026年10月19日成文、10月30日发布，国家发展改革委官网政务公开·政策·通知）；"
            "② 《宁国市2026年加快发展生活性服务业促进消费提升实施方案》（宁国市人民政府办公室行政规范性文件）；"
            "③ 《2026年“徽动消费 乐享宁国”促消费活动方案》（宁国市商务局）。", st_src))

# ---------------- PDF 输出 ----------------
doc = BaseDocTemplate(OUT_PDF, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M2, bottomMargin=M3,
                       title=NAME, author="宁国市大华市场发展有限责任公司")
def on_page(canvas, docu):
    canvas.saveState()
    canvas.setFont("FS", 9)
    n = canvas.getPageNumber()
    canvas.drawCentredString(A4[0] / 2.0, M3 * 0.45, "— %d —" % n)
    canvas.restoreState()
frame = Frame(M, M3, W, A4[1] - M2 - M3, id="f")
doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=on_page)])
doc.build(story)
print("PDF OK", os.path.getsize(OUT_PDF))

# ---------------- DOCX 输出 ----------------
from docx import Document
from docx.shared import Pt, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

d = Document()
sec = d.sections[0]
sec.page_width, sec.page_height = Mm(210), Mm(297)
sec.top_margin, sec.bottom_margin = Mm(20), Mm(18)
sec.left_margin, sec.right_margin = Mm(18), Mm(18)

def setfont(run, cn, size, bold=False):
    run.font.size = Pt(size); run.font.bold = bold
    run.font.name = "Times New Roman"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), cn)

def dp(text, cn="仿宋", size=11, bold=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY,
       indent=True, before=0, after=2, line=19):
    p = d.add_paragraph(); pf = p.paragraph_format
    pf.space_before = Pt(before); pf.space_after = Pt(after); pf.line_spacing = Pt(line)
    p.alignment = align
    if indent: pf.first_line_indent = Pt(size * 2)
    setfont(p.add_run(text), cn, size, bold)
    return p

for t in ["《关于加强消费基础设施建设 促进消费投资良性互动的指导意见》",
          "政策要点摘编及宁国市大华中心菜市场（民营）政策利用路径建议"]:
    dp(t, "黑体", 19, True, WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=30, after=2)
dp("——依据发改就业〔2026〕1508号，并结合《宁国市2026年加快发展生活性服务业促进消费提升实施方案》",
   "楷体", 12, False, WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=20, after=2)
dp("编制日期：2026年11月2日", "仿宋", 9.5, False, WD_ALIGN_PARAGRAPH.CENTER, indent=False, line=15, after=8)

def dtable(rows, widths_mm, header=True):
    t = d.add_table(rows=len(rows), cols=len(rows[0]))
    t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = t.cell(ri, ci)
            cell.text = ""
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(1.5); p.paragraph_format.space_after = Pt(1.5)
            p.paragraph_format.line_spacing = Pt(13)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if (header and ri == 0) else WD_ALIGN_PARAGRAPH.LEFT
            cn = "黑体" if (header and ri == 0) else ("黑体" if ci == 0 else "仿宋")
            sz = 9.5 if (header and ri == 0) else 9
            for li, line in enumerate(str(val).split("\n")):
                if li:
                    p = cell.add_paragraph(); p.paragraph_format.space_before = Pt(0)
                    p.paragraph_format.space_after = Pt(1.5); p.paragraph_format.line_spacing = Pt(13)
                setfont(p.add_run(line), cn, sz)
    for ci, w in enumerate(widths_mm):
        for r in t.rows:
            r.cells[ci].width = Mm(w)
    return t

dp("一、我市场基本情况与政策适用性判定", "黑体", 14, False, WD_ALIGN_PARAGRAPH.LEFT, indent=False, before=8, after=4, line=24)
for txt in [
 "（一）基本情况。宁国市大华市场发展有限责任公司（统一社会信用代码913418817467873726），注册地宁国市东风路，系自然人投资或控股的民营有限责任公司，注册资本300万元，法定代表人张志诒。市场于2003年由企业投资5000万元自建，2004年开业，占地50亩，摊位1100余个（含市场大厅、批发大厅、露天摊位），配套5亩停车场，日均交易额约600万元、年交易额约20亿元，带动就业1500余人，为宁国市城区中心农贸市场，隶属西津街道北园社区。",
 "（二）既有基础。市场已配备电子交易系统、冷藏保鲜库、果蔬农药残留检测设施；已实施“文明菜市”改造，增设垃圾分类回收站、公平秤、投诉站，统一经营户标牌与着装管理；先后完成食品安全管控记录表、制度与承诺书、创建文明市场材料等系列规范建设。",
 "（三）适用性判定（关键）。本市场为民营企业，不属于政府投资主体，不能直接向国家发展改革委、财政部门申报国债、专项债、中央预算内投资等财政性资金。但该文件第十八条明确“积极引导社会资本依法合规参与消费基础设施建设”，即为民营企业预留了合法参与通道。因此我市场的正确打法是：",
]:
    dp(txt)
for txt in [
 "1. 不是“向政府要钱”，而是“替政府把项目做出来”——由主管部门立项申报，我市场作为实施主体或社会资本方承接落地；",
 "2. 不是“等文件兑现”，而是“先形成项目、争取进盘子”——主动向发改、商务、市场监管等主管部门报项目建议；",
 "3. 不是“只靠财政补助”，而是“三条腿走路”——财政资金 + 经营权质押融资 + 自有资金改造。",
]:
    dp(txt, indent=False)

dp("二、国家层面可对接条款与我市场对应关系", "黑体", 14, False, WD_ALIGN_PARAGRAPH.LEFT, indent=False, before=8, after=4, line=24)
dtable([["文件条款", "政策要求要点", "我市场对应与现有基础", "缺口与争取方式"]] + t2, [22, 52, 44, 50])
d.add_paragraph()

dp("三、宁国市层面已明确的配套政策与资金池（能直接落地的部分）", "黑体", 14, False, WD_ALIGN_PARAGRAPH.LEFT, indent=False, before=8, after=4, line=24)
dp("依据《宁国市2026年加快发展生活性服务业促进消费提升实施方案》（宁国市人民政府办公室行政规范性文件），与本市场直接相关、且责任单位已明确的有以下若干项：")
dtable([["本地政策／资金", "责任单位", "我市场具体用法", "时间节点"]] + t3, [45, 27, 70, 26])
d.add_paragraph()

dp("四、民营身份下的五条可行路径（核心）", "黑体", 14, False, WD_ALIGN_PARAGRAPH.LEFT, indent=False, before=8, after=4, line=24)
for h, b in paths:
    dp("（%s）%s" % ("一二三四五"[paths.index((h, b))], h), "黑体", 12, False, WD_ALIGN_PARAGRAPH.LEFT, indent=False, before=4, after=2, line=22)
    dp(b)

dp("五、近期行动清单（建议两个月内完成）", "黑体", 14, False, WD_ALIGN_PARAGRAPH.LEFT, indent=False, before=8, after=4, line=24)
dtable([["时间", "动作", "对接单位", "产出"]] + t5, [18, 70, 40, 40])
d.add_paragraph()

dp("六、风险提示", "黑体", 14, False, WD_ALIGN_PARAGRAPH.LEFT, indent=False, before=8, after=4, line=24)
for r in risks:
    dp("◆ " + r, "楷体", 10, False, WD_ALIGN_PARAGRAPH.JUSTIFY, indent=False, after=2, line=17)

dp("资料来源：① 国家发展改革委等部门《关于加强消费基础设施建设 促进消费投资良性互动的指导意见》（发改就业〔2026〕1508号，2026年10月19日成文、10月30日发布，国家发展改革委官网政务公开·政策·通知）；② 《宁国市2026年加快发展生活性服务业促进消费提升实施方案》（宁国市人民政府办公室行政规范性文件）；③ 《2026年“徽动消费 乐享宁国”促消费活动方案》（宁国市商务局）。",
   "仿宋", 9.5, False, WD_ALIGN_PARAGRAPH.JUSTIFY, indent=False, before=8, line=15)

d.save(OUT_DOCX)
print("DOCX OK", os.path.getsize(OUT_DOCX))
