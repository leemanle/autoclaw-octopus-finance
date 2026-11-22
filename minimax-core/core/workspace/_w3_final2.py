# -*- coding: utf-8 -*-
"""W3 final v2 · 聚类 + 新冒头/老热点判定（口径收紧）"""
import json, os, re, collections, sys, importlib.util
sys.stdout.reconfigure(encoding='utf-8')
D = r"C:\Users\Administrator\Desktop\选股系统备份\_dav_score"
C = os.path.join(D, "_conn")
B = r"C:\Users\Administrator\Desktop\选股系统备份"
TOOLS = r"C:\Users\Administrator\.minimax\tools"
W = r"C:\Users\Administrator\.minimax\workspace"
spec = importlib.util.spec_from_file_location("pool", os.path.join(TOOLS, "_q_dzh_pool_1029_transcribe.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
POOL, REASON = m.POOL, m.REASON
name_by_code = {c: n for c, n, _ in POOL}
chg = {c: ch for c, _, ch in POOL}
codes = [c for c, _, _ in POOL]
ztinfo = json.load(open(os.path.join(W, "_w3_ztinfo.json"), encoding="utf-8"))
posts = json.load(open(os.path.join(D, "posts_merged_1240_1029.json"), encoding="utf-8"))
win = json.load(open(os.path.join(W, "_w3_windows.json"), encoding="utf-8"))
PRIOR = ["20261020","20261021","20261022","20261026","20261027","20261028"]

CL = [
 ("商业航天·卫星·军工", ["商业航天","卫星","卫星通信","军工","军工（客户成飞）","军用","太空算力","太空算力（轨道激光）","星间激光","系谱激光","千帆星座","天基信息","太空光伏","宇航制造","航天材料","电子元器件（火箭）","特种电缆","有源相控阵TR组件","仿真测试技术","合作Eutelsat","星宇星"],
   ["SpaceX合作","SpaceX控股","西部材料","层状金属复合材料","可控核聚变","核电机","核电","大飞机","冶金智能制造","存储"],
   ["商业航天","卫星","军工","航天","太空算力","火箭","可控核聚变","千帆星座","天基信息"]),
 ("人形机器人·具身智能", ["机器人","人形机器人","人形机器人（关节轴承）","人形机器人（线束）","智元机器人","伺服系统","工业机器人","工业缝制机械","智能成套服务商","麻醉机器人","物流分拣","物流","轮胎机械","航空轴承"], [],
   ["人形机器人","具身智能","机器人","智元","宇树","灵巧手","关节轴承"]),
 ("低空经济·无人机·无人驾驶", ["低空经济","低空文旅","无人机","无人驾驶","萝卜","出租车运营"], [],
   ["低空经济","低空","无人机","无人驾驶","eVTOL","萝卜"]),
 ("通信·6G·基站", ["5G","6G","基站","专网通信装备","移动通信网络设备"], [],
   ["6G","5G","基站","专网通信"]),
 ("风电·钙钛矿·固态电池·新能源", ["风电","海上风电","风机塔架","钙钛矿","钙钛矿电池","固态电池","消费类锂电池","氢能源","光伏","陆塔","油气船舶","海洋工程（泵阀件）","海工装备"], [],
   ["风电","海上风电","钙钛矿","固态电池","光伏"]),
 ("AI·算力·数据中心·液冷", ["人工智能","AI教育","大模型教育","AI司法（阿里合作）","AI服务器测试（谷歌）","FP8","Manu","算力","算点协同","数据中心","数据中心电源","柴油发电机","液冷","热管理","MLCC","磷化硼","机器视觉","数据采集","自动化设备","间接持股长江存储","华为","华为昇腾","数字人民币","铜缆布线","高速数据网缆","重卡"], [],
   ["算力","数据中心","液冷","数采","大模型","机器视觉","铜缆"]),
 ("医药·脑机接口·医疗", ["脑机接口","医疗器械","医疗服务","医美","创新药","中成药","流感药","抗菌药物","肿瘤疫苗","肺炎","生猪","镇痛","西瓜霜润喉片","老年专科医院","羊宇基"], ["重组","实控人拟变更"],
   ["脑机接口","创新药","医药","疫苗","抗菌药物"]),
 ("冰雪经济·文旅·商贸", ["冰雪经济","中俄贸易受益","张家界旅游","商演","博弈","免税","百货零售","宠物经济"], [],
   ["冰雪经济","冰雪","文旅","旅游","免税"]),
 ("业绩增长·三季报（非题材簇）", ["三季报增长","第三季度增长","三季度增长","三季报净利润增长","三季度净利润增长","第三季度净利润增长","业绩增长","业绩预增","现金分红","诉讼回款","股权变更"], [],
   ["三季报","三季度"]),
 ("食品·消费·烟草", ["速冻食品","预制菜","沙县小吃作坊扩建","抖音电商","中式面点","拓展新店型","烟草","工业大麻"], [],
   ["预制菜","速冻","中式面点","烘焙","烟草"]),
 ("化工·材料·资源", ["磷化工","高纯电子级磷酸","己二酸","化肥","溴素","钛白粉","海水淡化","煤炭","培育钻石","锆钛矿选矿","碳化硅","覆铜板","电子级碳纤布","天然气","储能","摘帽","合作群核科技","电磁材料","新能源车用扁线","比亚迪","聚酯树脂","林业","木材生产","砷化镓电池"], [],
   ["磷化工","钛白粉","煤炭","溴素","培育钻石","覆铜板","碳纤维"]),
 ("金融·地方国资", ["银行","支付结算","证券","多元金融（香港）","互联网金融","参股小贷公司","高岸业务","锌经济","不良资产","福建","上海徐汇","国资委","央企","湖北资本网络接入股"], ["特种船舶海运运输"],
   ["银行","多元金融","支付结算","互联网金融","国资"]),
 ("环保·装备制造", ["环保","设备更新","配套装备","压滤机龙头","厨卫净水","屏嵌两屏组合","跨境电商","节能环保","污水处理","岩土工程综合服务（西南水电）","绿色包装","跨境合作"], [],
   ["环保","净化","污水","跨境","压滤"]),
 ("影视·IP·传媒", ["影视投资","IP衍生品","AI漫剧"], [],
   ["AI漫剧","短剧","影视","IP潮玩"]),
]

def tags_of(c): return [t.strip() for t in (REASON.get(c) or "").split("+") if t.strip()]
REPORTS = [("_daV_v100_1027_2100_forum_11v.md","10-27 21:00"),("_daV_v101_1028_0800_forum_11v.md","10-28 08:00"),
           ("_daV_v102_1028_1240_forum_11v.md","10-28 12:40"),("_daV_v103_1028_1600_forum_11v.md","10-28 16:00"),
           ("_daV_v104_1028_2100_forum_11v.md","10-28 21:00"),("_daV_v105_1029_0800_forum_11v.md","10-29 08:00"),
           ("_daV_v106_1029_1240_forum_11v.md","10-29 12:40(v106)"),("_daV_v107_1029_1240_forum_11v.md","10-29 12:40(v107)")]
reps = {}
for fn, lab in REPORTS:
    p = os.path.join(B, fn); reps[lab] = open(p, encoding="utf-8").read() if os.path.exists(p) else ""

# 语料：标题命中（严格：只在标题里找，不看点名票）
corpus_by_day = collections.defaultdict(list)
for p in posts:
    corpus_by_day[p["ct"][:10]].append(p.get("title") or "")
D1 = win["D1_当日10-29"]["per"]; W2 = win["W2_10-28~10-29"]["per"]

clusters = []
for cn, core, sat, kws in CL:
    mem = [c for c in codes if any(t in tags_of(c) for t in core + sat)]
    core_mem = [c for c in codes if any(t in tags_of(c) for t in core)]
    if not mem: continue
    mem.sort(key=lambda c: (-chg[c], c))
    leader = mem[0]
    zt_mem = [c for c in mem if ztinfo[c]["today_zt"]]
    # 首板 = 今日涨停 且 近5交易日(10-22..10-28)无涨停；回访板 = 有历史涨停
    fb = [c for c in zt_mem if not [d for d in ztinfo[c]["ztdays"] if d in ("20261022","20261026","20261027","20261028")]]
    rv = [c for c in zt_mem if c not in fb]
    maxlbc = max([ztinfo[c]["lbc"] for c in mem] or [0])
    prior_zt = {c: [d for d in ztinfo[c]["ztdays"] if d in PRIOR] for c in mem}
    prior_zt = {c: v for c, v in prior_zt.items() if v}
    # 语料出现日（标题命中）
    cd = sorted([d for d in corpus_by_day if d >= "2026-10-20"
                 and any(any(k in ti for k in kws) for ti in corpus_by_day[d])])
    cd_prior = [d for d in cd if d < "2026-10-29"]
    # 历史档
    rep_hits = []; rep_days = []
    for lab, txt in reps.items():
        n = sum(txt.count(k) for k in kws)
        if n: rep_hits.append("%s×%d" % (lab, n)); rep_days.append(lab.split()[0])
    rep_days = sorted(set(rep_days))
    # 当日讨论（簇内成员被提及）
    talk29 = sum(D1.get(c, {}).get("mentions", 0) for c in mem)
    talk29_posts = len(set(p for c in mem for p in (D1.get(c, {}).get("titles") or [])))
    # ===== 判定 =====
    old_reasons = []
    if len(cd_prior) >= 2: old_reasons.append("论坛语料 %s 已连续出现" % ",".join(cd_prior))
    if prior_zt: old_reasons.append("簇内 %s 在 10-20~10-28 已有涨停史" % ",".join(sorted(prior_zt)))
    if maxlbc >= 2: old_reasons.append("簇内最高连板 %d（%s）" % (maxlbc, ",".join(c for c in mem if ztinfo[c]["lbc"] == maxlbc)))
    if len(rep_days) >= 2: old_reasons.append("历史档覆盖 %d 个盘日(%s)" % (len(rep_days), ",".join(rep_days)))
    fresh_reasons = []
    if maxlbc <= 1: fresh_reasons.append("簇内无 2 板以上高标（最高连板=%d）" % maxlbc)
    if not prior_zt: fresh_reasons.append("簇内成员 10-20~10-28 无涨停史")
    if len(zt_mem) >= 2: fresh_reasons.append("簇内今日涨停 %d 只(其中首板 %d)" % (len(zt_mem), len(fb)))
    if len(cd_prior) == 0: fresh_reasons.append("该题材 10-20~10-28 论坛语料无出现")
    label = "老热点" if old_reasons else ("新冒头" if (len(fb) >= 1 and len(zt_mem) >= 2 and maxlbc <= 1) else "证据不足")
    ev = ("；".join(old_reasons) if old_reasons else "；".join(fresh_reasons)) or "证据不足"
    clusters.append({"name": cn, "n": len(mem), "n_core": len(core_mem), "codes": mem,
                     "leader": "%s %s %+.2f%%" % (leader, name_by_code[leader], chg[leader]),
                     "leader_code": leader, "zt_members": zt_mem, "first_board": fb, "revisit_board": rv,
                     "max_lbc": maxlbc, "prior_zt": prior_zt,
                     "new_or_old": label, "evidence": ev,
                     "forum_1029_mentions": talk29, "forum_1029_posts": talk29_posts,
                     "corpus_days": cd, "report_hits": rep_hits})
clusters.sort(key=lambda x: (-x["n"], x["name"]))
json.dump(clusters, open(os.path.join(W, "_w3_clusters.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("=== 簇（收紧口径）===")
for c in clusters:
    print("%-26s n=%2d(核心%2d) 龙头=%-20s %s zt=%d(首板%d) maxlbc=%d 当日提及=%d" % (
        c["name"], c["n"], c["n_core"], c["leader"], c["new_or_old"], len(c["zt_members"]),
        len(c["first_board"]), c["max_lbc"], c["forum_1029_mentions"]))
    print("      证据:", c["evidence"])
    print("      语料出现日:", c["corpus_days"], "| 历史档:", c["report_hits"][:4])
print("\n池内最高连板:", max(ztinfo[c]["lbc"] for c in codes))
zt = json.load(open(os.path.join(C, "zt_hist_1240_1029.json"), encoding="utf-8"))
card = {r["code"]: r for r in json.load(open(os.path.join(C, "card_1240_1029.json"), encoding="utf-8"))}
print("市场高标（forum池内今日涨停，按连板）:")
for r in sorted([r for r in zt if "20261029" in (r.get("zt_days") or [])], key=lambda r: -(r.get("lbc") or 0)):
    print("   %-11s %-9s %-6s lbc=%s thr=%s" % (r["code"], r["name"], r.get("shape"), r.get("lbc"), (card.get(r["code"], {}).get("ths_reason") or "-")[:50]))
