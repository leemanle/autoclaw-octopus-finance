# -*- coding: utf-8 -*-
import json, os, re, collections, sys, importlib.util
sys.stdout.reconfigure(encoding='utf-8')
D = r"C:\Users\Administrator\Desktop\选股系统备份\_dav_score"
C = os.path.join(D, "_conn")
TOOLS = r"C:\Users\Administrator\.minimax\tools"
spec = importlib.util.spec_from_file_location("pool", os.path.join(TOOLS, "_q_dzh_pool_1029_transcribe.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
POOL, REASON = m.POOL, m.REASON
name_by_code = {c: n for c, n, _ in POOL}
chg = {c: ch for c, _, ch in POOL}
codes = [c for c, _, _ in POOL]
posts = json.load(open(os.path.join(D, "posts_merged_1240_1029.json"), encoding="utf-8"))

def digit(code):
    c = re.sub(r'^(sh|sz|bj|hk)', '', str(code).strip().lower())
    return c if re.fullmatch(r'\d{6}', c) else None

def post_codes(p):
    s = set()
    for cc, _n in (p.get("stocks") or []):
        d = digit(cc)
        if d: s.add(d)
    return s

WINDOWS = {"D1_当日10-29": ("2026-10-29", "2026-10-29"),
           "W2_10-28~10-29": ("2026-10-28", "2026-10-29"),
           "W3_10-27~10-29": ("2026-10-27", "2026-10-29")}
res = {}
for wname, (lo, hi) in WINDOWS.items():
    sub = [p for p in posts if lo <= p["ct"][:10] <= hi]
    per = {}
    for c in codes:
        nm = name_by_code[c]
        hit = []
        for p in sub:
            taghit = c in post_codes(p)
            titlehit = bool(nm) and nm in (p.get("title") or "")
            if taghit or titlehit:
                hit.append((p, taghit, titlehit))
        if not hit: continue
        per[c] = dict(mentions=sum(1 + (1 if th else 0) for p, tg, th in hit),
                      tag_n=sum(1 for p, tg, th in hit if tg),
                      title_n=sum(1 for p, tg, th in hit if th),
                      threads=len(hit),
                      first_at=min(p["ct"] for p, tg, th in hit),
                      last_at=max(p["ct"] for p, tg, th in hit),
                      titles=[p["title"] for p, tg, th in hit])
    res[wname] = dict(sub_n=len(sub), per=per)
    print("\n" + "=" * 74)
    print("窗口 %s  帖子 %d 帖 · 池内被提及 %d 只" % (wname, len(sub), len(per)))
    rk = sorted(per.items(), key=lambda kv: (-kv[1]["mentions"], -kv[1]["threads"], codes.index(kv[0])))
    for i, (c, v) in enumerate(rk, 1):
        print("%2d %-7s %-8s mentions=%d threads=%d title=%d tag=%d  first=%s last=%s" % (
            i, c, name_by_code[c], v["mentions"], v["threads"], v["title_n"], v["tag_n"],
            v["first_at"][5:16], v["last_at"][5:16]))
        for t in v["titles"][:3]:
            print("      - " + t[:88])

# ---- card / zt coverage for the 67 pool ----
card = json.load(open(os.path.join(C, "card_1240_1029.json"), encoding="utf-8"))
zt = json.load(open(os.path.join(C, "zt_hist_1240_1029.json"), encoding="utf-8"))
cd = {r["code"]: r for r in card}
ztd = {r["code"]: r for r in zt}
def key(code): return code.split(".")[0]
print("\n" + "=" * 74)
print("card 覆盖池内 %d/67 ; zt_hist 覆盖池内 %d/67" % (
    sum(1 for c in codes if any(key(k) == c for k in cd)), sum(1 for c in codes if any(key(k) == c for k in ztd))))
rows = []
for c in codes:
    k = next((k for k in cd if key(k) == c), None)
    kz = next((k for k in ztd if key(k) == c), None)
    r = cd.get(k, {}) if k else {}
    z = ztd.get(kz, {}) if kz else {}
    rows.append((chg[c], c, name_by_code[c], r.get("shape"), r.get("lbc"), z.get("zt_days"), r.get("ths_reason")))
rows.sort(key=lambda x: (-x[0]))
print("\n池内逐只（大智慧涨幅 / 卡形态 / 连板数 / 涨停日 / 同花顺原因）")
for ch, c, n, sh, lbc, zd, thr in rows:
    print("%+7.2f%% %-7s %-9s shape=%-7s lbc=%-4s zt_days=%-28s thr=%s" % (
        ch, c, n, sh, lbc, ",".join(zd or []) or "-", (thr or "")[:60]))
json.dump(res, open(r"C:\Users\Administrator\.minimax\workspace\_w3_windows.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
