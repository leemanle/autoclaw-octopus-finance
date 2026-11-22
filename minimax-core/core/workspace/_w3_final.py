# -*- coding: utf-8 -*-
"""W3 · 10-29 论坛讨论 + 题材簇（只读取数 → 生成两份交付件内容）"""
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

CLUSTERS = [
 ("商业航天·卫星·军工", ["商业航天","卫星","卫星通信","军工","军工（客户成飞）","军用","有源相控阵TR组件","太空算力","太空算力（轨道激光）","星间激光","系谱激光","千帆星座","天基信息","太空光伏","宇航制造","航天材料","西部材料","SpaceX合作","SpaceX控股","电子元器件（火箭）","特种电缆","存储","可控核聚变","核电机","核电","层状金属复合材料","大飞机","冶金智能制造","5G","6G","专网通信装备","基站","移动通信网络设备","星宇星","合作Eutelsat","仿真测试技术"],
  ["商业航天","卫星","军工","航天","太空算力","火箭","可控核聚变","星间激光","千帆星座","天基信息","相控阵"]),
 ("人形机器人·具身智能", ["机器人","人形机器人","人形机器人（关节轴承）","人形机器人（线束）","智元机器人","伺服系统","工业机器人","工业缝制机械","智能成套服务商","麻醉机器人","物流分拣","物流","轮胎机械","航空轴承"],
  ["机器人","具身智能","智元","宇树","灵巧手","关节轴承"]),
 ("低空经济·无人机·无人驾驶", ["低空经济","低空文旅","无人机","无人驾驶","萝卜","出租车运营"],
  ["低空","无人机","无人驾驶","萝卜"]),
 ("风电·钙钛矿·固态电池·新能源", ["固态电池","消费类锂电池","氢能源","光伏","钙钛矿","钙钛矿电池","风电","海上风电","风机塔架","陆塔","油气船舶","海洋工程（泵阀件）","环保","设备更新","配套装备","压滤机龙头","厨卫净水","屏嵌两屏组合","跨境电商","节能环保","污水处理","岩土工程综合服务（西南水电）","绿色包装","海工装备"],
  ["风电","钙钛矿","固态电池","海上风电","光伏","储能","环保","净化","跨境"]),
 ("AI·算力·数据中心·液冷", ["人工智能","AI教育","大模型教育","AI漫剧","AI司法（阿里合作）","AI服务器测试（谷歌）","FP8","Manu","算力","算点协同","数据中心","数据中心电源","柴油发电机","液冷","热管理","MLCC","磷化硼","机器视觉","数据采集","自动化设备","间接持股长江存储","华为","华为昇腾","数字人民币","铜缆布线","高速数据网缆","重卡"],
  ["AI","算力","数据中心","液冷","数采","人工智能","大模型","MLCC","机器视觉","铜缆"]),
 ("医药·脑机接口·医疗", ["脑机接口","医疗器械","医疗服务","医美","创新药","中成药","流感药","抗菌药物","肿瘤疫苗","肺炎","生猪","镇痛","西瓜霜润喉片","老年专科医院","羊宇基","重组","实控人拟变更"],
  ["脑机接口","医药","医疗","创新药","疫苗","抗菌"]),
 ("冰雪经济·文旅·商贸", ["冰雪经济","中俄贸易受益","张家界旅游","商演","博弈","免税","百货零售","宠物经济"],
  ["冰雪","文旅","旅游","免税","景区","商贸"]),
 ("业绩增长·三季报", ["三季报增长","第三季度增长","三季度增长","三季报净利润增长","三季度净利润增长","第三季度净利润增长","业绩增长","业绩预增","现金分红","诉讼回款","股权变更"],
  ["三季报","三季度","业绩"]),
 ("食品·消费·烟草", ["速冻食品","预制菜","沙县小吃作坊扩建","抖音电商","中式面点","拓展新店型","烟草","工业大麻"],
  ["食品","预制菜","烟草","烘焙","小笼包","玩具","IP潮玩"]),
 ("化工·材料·资源", ["磷化工","高纯电子级磷酸","己二酸","化肥","溴素","钛白粉","海水淡化","煤炭","培育钻石","锆钛矿选矿","碳化硅","覆铜板","电子级碳纤布","天然气","储能","摘帽","合作群核科技","电磁材料","新能源车用扁线","比亚迪","聚酯树脂","林业","木材生产","砷化镓电池"],
  ["磷化工","钛白粉","煤炭","溴素","钻石","化工","覆铜板","碳纤","材料"]),
 ("金融·地方国资", ["银行","支付结算","证券","多元金融（香港）","互联网金融","参股小贷公司","高岸业务","锌经济","不良资产","福建","上海徐汇","国资委","央企","湖北资本网络接入股","特种船舶海运运输"],
  ["银行","金融","证券","国资","福建","支付","船舶","海运"]),
 ("影视·IP·传媒", ["影视投资","IP衍生品"], ["影视","漫剧","IP","短剧"]),
]
t2c = {}
for cn, tg, kw in CLUSTERS:
    for t in tg: t2c.setdefault(t, cn)

# ---------- A. talk ----------
D1 = win["D1_当日10-29"]["per"]; W2 = win["W2_10-28~10-29"]["per"]; W3 = win["W3_10-27~10-29"]["per"]
rk = sorted(codes, key=lambda c: (-(D1.get(c, {}).get("mentions", 0)), -(D1.get(c, {}).get("threads", 0)), codes.index(c)))
talk = []
for i, c in enumerate(rk, 1):
    d1 = D1.get(c, {}); w2 = W2.get(c, {}); w3 = W3.get(c, {})
    talk.append({
        "code": c, "name": name_by_code[c], "rank_today": i,
        "mentions": d1.get("mentions", 0), "threads": d1.get("threads", 0),
        "title_hits": d1.get("title_n", 0), "tag_hits": d1.get("tag_n", 0),
        "first_at": d1.get("first_at", ""), "last_at": d1.get("last_at", ""),
        "samples": [t[:60] for t in (d1.get("titles") or [])[:3]],
        "chg": chg[c],
        "win2d_1028_1029": {"mentions": w2.get("mentions", 0), "threads": w2.get("threads", 0),
                            "first_at": w2.get("first_at", ""), "last_at": w2.get("last_at", "")},
        "win3d_1027_1029": {"mentions": w3.get("mentions", 0), "threads": w3.get("threads", 0)},
        "is_zt_1029": ztinfo[c]["today_zt"], "lbc_1029": ztinfo[c]["lbc"],
    })

# ---------- B. tags ----------
tags = collections.defaultdict(list)
for c in codes:
    for t in (REASON.get(c) or "").split("+"):
        t = t.strip()
        if t: tags[t].append(c)
tag_top = [{"tag": t, "n": len(tags[t]), "codes": tags[t]}
           for t in sorted(tags, key=lambda t: (-len(tags[t]), t))[:20]]

# ---------- B2. clusters ----------
REPORTS = [("_daV_v100_1027_2100_forum_11v.md","10-27 21:00"),("_daV_v101_1028_0800_forum_11v.md","10-28 08:00"),
           ("_daV_v102_1028_1240_forum_11v.md","10-28 12:40"),("_daV_v103_1028_1600_forum_11v.md","10-28 16:00"),
           ("_daV_v104_1028_2100_forum_11v.md","10-28 21:00"),("_daV_v105_1029_0800_forum_11v.md","10-29 08:00"),
           ("_daV_v106_1029_1240_forum_11v.md","10-29 12:40(v106)"),("_daV_v107_1029_1240_forum_11v.md","10-29 12:40(v107)")]
reps = {}
for fn, lab in REPORTS:
    p = os.path.join(B, fn)
    reps[lab] = open(p, encoding="utf-8").read() if os.path.exists(p) else ""

def digit(code):
    c = re.sub(r'^(sh|sz|bj|hk)', '', str(code).strip().lower())
    return c if re.fullmatch(r'\d{6}', c) else None
corp_txt = []
for p in posts:
    names = [n for _c, n in (p.get("stocks") or []) if n]
    corp_txt.append((p["ct"][:10], p.get("title") or "", " ".join(names), p))

clusters = []
for cn, tg, kw in CLUSTERS:
    mem = [c for c in codes if any(t in (REASON.get(c) or "").split("+") for t in tg)]
    if not mem: continue
    mem.sort(key=lambda c: (-chg[c], c))
    leader = max(mem, key=lambda c: chg[c])
    zt_mem = [c for c in mem if ztinfo[c]["today_zt"]]
    lbc_mem = sorted([c for c in mem if ztinfo[c]["lbc"] >= 2], key=lambda c: -ztinfo[c]["lbc"])
    maxlbc = max([ztinfo[c]["lbc"] for c in mem] or [0])
    # corpus appearance dates
    cdays = sorted(set(d for d, t, n, _p in corp_txt if any(k in t or k in n for k in kw)))
    cdays_recent = [d for d in cdays if d >= "2026-10-20"]
    # report appearance
    rep_hits = []
    rep_days = []
    for lab, txt in reps.items():
        n = sum(txt.count(k) for k in kw)
        if n: rep_hits.append("%s(%d次)" % (lab, n)); rep_days.append(lab.split()[0])
    rep_days = sorted(set(rep_days))
    # prior ZT in cluster (fermentation)
    prior_zt = [c for c in mem if [d for d in ztinfo[c]["ztdays"] if d != "20261029"]]
    old = bool(rep_days and len(rep_days) >= 2) or len([d for d in cdays_recent if d < "2026-10-29"]) >= 2 or bool(lbc_mem)
    fresh = (not old) and (bool(zt_mem) or len([c for c in mem if chg[c] >= 5]) >= 2)
    label = "老热点" if old else ("新冒头" if fresh else "证据不足")
    ev = ("历史档出现 %d 个盘日(%s)" % (len(rep_days), ",".join(rep_days))) if rep_days else "历史档未见"
    ev += "；论坛语料出现日 %s" % (",".join(cdays_recent) if cdays_recent else "无")
    ev += "；簇内最高连板=%d" % maxlbc
    ev += "；簇内今日涨停 %d 只" % len(zt_mem)
    if prior_zt: ev += "；%s 近10日已有涨停史" % ",".join(prior_zt)
    clusters.append({"name": cn, "n": len(mem), "codes": mem,
                     "leader": "%s %s %+.2f%%" % (leader, name_by_code[leader], chg[leader]),
                     "leader_code": leader, "zt_members": zt_mem, "max_lbc": maxlbc,
                     "new_or_old": label, "evidence": ev,
                     "report_hits": rep_hits, "corpus_days": cdays_recent})
clusters.sort(key=lambda x: (-x["n"], x["name"]))

# ---------- C. 涨停池题材 ----------
an = json.load(open(os.path.join(C, "anomaly_1029_1240.json"), encoding="utf-8"))
ztA = [r for r in an if r.get("tag_name") == "涨停"]
ZT_THEMES = [
 ("商业航天·卫星·太空算力", ["商业航天","卫星","太空算力","航天","火箭","特种装备","卫星通信终端","激光通信"]),
 ("三季报·业绩增长", ["三季报","三季度","业绩"]),
 ("人形机器人·机器人", ["机器人","人形机器人","关节轴承","智元","宇树","具身智能","焊接机器人"]),
 ("AI·短剧·传媒·玩具", ["AI","短剧","漫剧","游戏","影院","影视","IP潮玩","玩具","职业教育"]),
 ("冰雪·文旅", ["冰雪","文旅","旅游","景区","低空文旅"]),
 ("食品·消费", ["食品","预制菜","烘焙","乳品","面点","小笼包","饼干"]),
 ("液冷·数据中心·新能源", ["液冷","水冷板","数据中心","光伏","新能源"]),
 ("资源·化工·煤炭", ["煤炭","化工","煤化工","磷","炼焦"]),
 ("特种运输·船舶·装备", ["重吊船","特种运输","输送","紧固件","液压","铝挤压"]),
 ("金融·多元金融", ["金融","银行","支付","科技"]),
 ("医药·脑机接口", ["脑机","医药","医疗","医疗服务"]),
 ("零售·重组·并购", ["重组","百货","股权转让","并购","尚阳通","收购"]),
 ("低空·雷达·探测", ["低空","雷达","探测"]),
 ("军工电子·相控阵·铜缆", ["相控阵","收发芯片","铜缆","高速数据"]),
]
zt_map = collections.defaultdict(list)
zt_tags = collections.defaultdict(list)
for r in ztA:
    kws = r.get("keyword_list") or []
    for th, kwl in ZT_THEMES:
        if any(any(k in kw for k in kwl) for kw in kws):
            zt_map[th].append(r["thscode"])
    for kw in kws:
        zt_tags[kw].append(r["thscode"])
zt_theme_top = [{"theme": th, "n": len(cs), "codes": cs,
                 "samples": [next((x.get("stock_name") for x in ztA if x["thscode"] == c), "") for c in cs[:3]]}
                for th, cs in sorted(zt_map.items(), key=lambda kv: -len(kv[1]))]
raw_tag_top_zt = [{"tag": t, "n": len(cs), "codes": cs} for t, cs in sorted(zt_tags.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:15]]

out = {"talk": talk, "tag_top": tag_top, "clusters": clusters, "zt_theme_top": zt_theme_top}
json.dump(out, open(os.path.join(W, "_w3_final.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump({"zt_raw_tags": raw_tag_top_zt, "zt_n": len(ztA)}, open(os.path.join(W, "_w3_zttop.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print("### tag_top 20 ###")
for t in tag_top: print("%2d %-22s %s" % (t["n"], t["tag"], " ".join(t["codes"])))
print("\n### clusters ###")
for c in clusters:
    print("%-26s n=%2d 龙头=%-22s %s | zt=%s maxlbc=%d" % (c["name"], c["n"], c["leader"], c["new_or_old"], ",".join(c["zt_members"]) or "-", c["max_lbc"]))
    print("      ", c["evidence"])
print("\n### zt_theme_top (涨停池 %d 只) ###" % len(ztA))
for t in zt_theme_top: print("%2d %-24s %s" % (t["n"], t["theme"], " ".join(t["codes"])))
print("\n### 涨停池原始关键词 Top15 ###")
for t in raw_tag_top_zt: print("%2d %-24s %s" % (t["n"], t["tag"], " ".join(t["codes"])))
