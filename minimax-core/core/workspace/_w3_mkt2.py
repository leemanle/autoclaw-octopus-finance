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
codes = [c for c, _, _ in POOL]
mk = json.load(open(os.path.join(D, "mkt_close_1029.json"), encoding="utf-8"))
print("mkt_close stocks:", len(mk))
sufs = collections.Counter(k.split(".")[-1] for k in mk)
print("suffixes:", dict(sufs))
dates = set()
for k, v in mk.items():
    dates.update(v.keys())
ds = sorted(d for d in dates if d >= "20261020")
print("date keys 20261020+:", ds)

def suf(c):
    if c.startswith("6"): return "SH"
    if c[0] in "03": return "SZ"
    if c[0] in "489": return "BJ"
    return "SH"

def series(c):
    k = "%s.%s" % (c, suf(c))
    return mk.get(k)

print("\n--- 池内 67 只：mkt_close 覆盖率与 10-29 实际涨幅 ---")
miss = []
for c, n, ch in POOL:
    s = series(c)
    if not s:
        miss.append(c); continue
    c28 = s.get("20261028"); c29 = s.get("20261029")
    if c28 and c29:
        pct = (c29 / c28 - 1) * 100
        print("%-7s %-9s dz=%+7.2f%%  mkt=%+7.2f%%  (c28=%.3f c29=%.3f)" % (c, n, ch, pct, c28, c29))
    else:
        print("%-7s %-9s dz=%+7.2f%%  mkt= 缺 %s/%s" % (c, n, ch, s.get("20261028"), s.get("20261029")))
print("mkt_close 缺:", miss)

# market-wide ZT on 10-29 from mkt_close
def limit_of(c, name):
    if "ST" in name or "*ST" in name: return 5.0
    if c.startswith("30") or c.startswith("68"): return 20.0
    if c[0] in "489": return 30.0
    return 10.0
zt_all = []
for k, v in mk.items():
    a, b = v.get("20261028"), v.get("20261029")
    if not a or not b: continue
    pct = (b / a - 1) * 100
    base = k.split(".")[0]
    if pct >= 9.8:
        zt_all.append((k, pct))
print("\nmkt_close 推算 10-29 涨幅>=9.8%% 的股票数: %d" % len(zt_all))
