# -*- coding: utf-8 -*-
import json, os, re, collections, sys, importlib.util
sys.stdout.reconfigure(encoding='utf-8')
D = r"C:\Users\Administrator\Desktop\选股系统备份\_dav_score"
C = os.path.join(D, "_conn")
TOOLS = r"C:\Users\Administrator\.minimax\tools"
spec = importlib.util.spec_from_file_location("pool", os.path.join(TOOLS, "_q_dzh_pool_1029_transcribe.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
POOL = m.POOL
name_by_code = {c: n for c, n, _ in POOL}
chg = {c: ch for c, _, ch in POOL}
codes = [c for c, _, _ in POOL]
mk = json.load(open(os.path.join(D, "mkt_close_1029.json"), encoding="utf-8"))
TRADE = ["20261020", "20261021", "20261022", "20261026", "20261027", "20261028"]
def suf(c):
    if c.startswith("6"): return "SH"
    if c[0] in "03": return "SZ"
    if c[0] in "489": return "BJ"
    return "SH"
def lim(c, nm):
    if "ST" in nm: return 5.0
    if c.startswith("30") or c.startswith("68"): return 20.0
    if c[0] in "489": return 30.0
    return 10.0
print("=== 池内 67 只：真实涨停史（mkt_close 10-20..10-28 + 今日大智慧涨幅）===")
ztinfo = {}
for c, n, ch in POOL:
    s = mk.get("%s.%s" % (c, suf(c))) or {}
    L = lim(c, n)
    hist = []
    for d in TRADE:
        a = s.get(d); prev = "2026102%d" % (int(d[-2:]) - 1) if d[-2:] not in ("20","21","22") else None
        # compute pct vs previous available close
        order = ["20261019","20261020","20261021","20261022","20261026","20261027","20261028"]
        if d in order:
            i = order.index(d)
            pa = s.get(order[i-1]) if i > 0 else None
            if a and pa:
                pct = (a/pa - 1)*100
                hist.append((d, pct, pct >= L - 0.35))
    # today
    today_zt = ch >= L - 0.35
    # consecutive
    ztdays = [d for d, p, z in hist if z] + (["20261029"] if today_zt else [])
    ztset = set(ztdays)
    lbc = 0
    for d in ["20261029","20261028","20261027","20261026","20261022","20261021","20261020"]:
        if d in ztset: lbc += 1
        else: break
    ztinfo[c] = dict(lbc=lbc, today_zt=today_zt, ztdays=sorted(ztset), limit=L)
    print("%-7s %-9s lim=%4.1f%% today=%+6.2f%% %s | 涨停日: %-34s 连板=%d | hist %s" % (
        c, n, L, ch, "涨停" if today_zt else "    ", ",".join(sorted(ztset)) or "-", lbc,
        " ".join("%s:%+.1f%s" % (d[4:6], p, "Z" if z else "") for d, p, z in hist)))
json.dump(ztinfo, open(r"C:\Users\Administrator\.minimax\workspace\_w3_ztinfo.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print("\n=== 池内今日涨停 %d 只 ===" % sum(1 for c in codes if ztinfo[c]["today_zt"]))
for c, n, ch in sorted(POOL, key=lambda x: -x[2]):
    if ztinfo[c]["today_zt"]:
        print("  %-7s %-9s %+6.2f%% 连板=%d ztdays=%s" % (c, n, ch, ztinfo[c]["lbc"], ",".join(ztinfo[c]["ztdays"])))

an = json.load(open(os.path.join(C, "anomaly_1029_1240.json"), encoding="utf-8"))
ztA = [r for r in an if r.get("tag_name") == "涨停"]
print("\n=== 异动源 10-29 涨停 %d 只（市场级样本）===" % len(ztA))
kwc = collections.Counter()
for r in ztA:
    for k in (r.get("keyword_list") or []): kwc[k] += 1
print("keyword Top 30:", json.dumps(kwc.most_common(30), ensure_ascii=False))
print("\n代码清单:", " ".join(sorted(r["thscode"] for r in ztA)))
