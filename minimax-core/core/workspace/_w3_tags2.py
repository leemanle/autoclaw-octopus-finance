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

# ---- 1. all 206 tags of the 67 pool ----
tags = collections.defaultdict(list)
for c, n, ch in POOL:
    for t in (REASON.get(c) or "").split("+"):
        t = t.strip()
        if t: tags[t].append(c)
print("=== 池内全部标签（%d 个）===" % len(tags))
for t in sorted(tags, key=lambda t: (-len(tags[t]), t)):
    print("%2d %-30s %s" % (len(tags[t]), t, " ".join(tags[t])))

# ---- 2. ZT pool themes ----
card = json.load(open(os.path.join(C, "card_1240_1029.json"), encoding="utf-8"))
zt = json.load(open(os.path.join(C, "zt_hist_1240_1029.json"), encoding="utf-8"))
cd = {r["code"]: r for r in card}
print("\n=== 涨停池 zt_hist %d 只 / card %d 只 ===" % (len(zt), len(card)))
print("zt 里 is_zt=True:", sum(1 for r in zt if r.get("is_zt")))
lbc = collections.Counter(r.get("shape") for r in zt)
print("shape 分布:", dict(lbc))
ttags = collections.defaultdict(list)
miss_reason = 0
for r in zt:
    c = cd.get(r["code"], {})
    thr = (c.get("ths_reason") or "").strip()
    if not thr:
        miss_reason += 1; continue
    for t in thr.split("+"):
        t = t.strip()
        if t: ttags[t].append(r["code"])
print("ZT 池有 ths_reason 的: %d / %d (缺 %d)" % (len(zt) - miss_reason, len(zt), miss_reason))
print("\n=== ZT 池题材标签 Top 45 ===")
for t in sorted(ttags, key=lambda t: (-len(ttags[t]), t))[:45]:
    print("%2d %-26s %s" % (len(ttags[t]), t, " ".join(ttags[t])))
json.dump({"zt_tags": ttags, "zt": zt, "cards": card},
          open(r"C:\Users\Administrator\.minimax\workspace\_w3_zttags.json", "w", encoding="utf-8"), ensure_ascii=False)
