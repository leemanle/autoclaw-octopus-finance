# -*- coding: utf-8 -*-
import json, os, re, collections, sys, importlib.util
sys.stdout.reconfigure(encoding='utf-8')
D = r"C:\Users\Administrator\Desktop\选股系统备份\_dav_score"
TOOLS = r"C:\Users\Administrator\.minimax\tools"
spec = importlib.util.spec_from_file_location("pool", os.path.join(TOOLS, "_q_dzh_pool_1029_transcribe.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
POOL, REASON = m.POOL, m.REASON
name_by_code = {c: n for c, n, _ in POOL}
codes = [c for c, _, _ in POOL]
posts = json.load(open(os.path.join(D, "posts_merged_1240_1029.json"), encoding="utf-8"))
raw = open(os.path.join(D, "posts_merged_1240_1029.json"), encoding="utf-8").read()

# --- sanity: raw substring hit counts for pool names across whole corpus ---
hit_any = {}
for c, n, _ in POOL:
    k = raw.count(n)
    if k: hit_any[c] = k
print("pool names appearing ANYWHERE in corpus json (by raw count):", len(hit_any))
print(sorted(hit_any.items(), key=lambda kv: -kv[1]))

# --- all distinct codes in corpus stocks, any date ---
def digit(code):
    c = re.sub(r'^(sh|sz|bj|hk)', '', str(code).strip().lower())
    return c if re.fullmatch(r'\d{6}', c) else None
allcodes = collections.Counter()
for p in posts:
    for cc, nn in (p.get("stocks") or []):
        d = digit(cc)
        if d: allcodes[d] += 1
poolset = set(codes)
print("\ncorpus distinct A-share codes:", len(allcodes), "| of which in 67-pool:", len(set(allcodes) & poolset))
print("pool codes present in corpus stocks (any date):",
      [(c, name_by_code[c], allcodes[c]) for c in codes if c in allcodes])

# --- date distribution of posts mentioning pool codes ---
bydate = collections.Counter()
for p in posts:
    d = p["ct"][:10]
    if d < "2026-10-15": continue
    for cc, _n in (p.get("stocks") or []):
        dd = digit(cc)
        if dd in poolset: bydate[d] += 1
print("\n帖子标签命中池内票数（按帖子日期, 10-15起）:", dict(sorted(bydate.items())))
