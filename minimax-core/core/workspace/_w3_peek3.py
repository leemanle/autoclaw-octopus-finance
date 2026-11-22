# -*- coding: utf-8 -*-
import json, os, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
C = r"C:\Users\Administrator\Desktop\选股系统备份\_dav_score\_conn"
E = r"C:\Users\Administrator\首阳战法回测引擎\reports"
an = json.load(open(os.path.join(C, "anomaly_1029_1240.json"), encoding="utf-8"))
print("anomaly n=%d ; tag_name 分布:" % len(an))
tn = collections.Counter(r.get("tag_name") for r in an)
print(json.dumps(tn, ensure_ascii=False, indent=0)[:1500])
zt = json.load(open(os.path.join(C, "zt_hist_1240_1029.json"), encoding="utf-8"))
d29 = [r for r in zt if "20261029" in (r.get("zt_days") or [])]
print("\nzt_hist_1240 里 zt_days 含 20261029 的: %d 只" % len(d29))
for r in sorted(d29, key=lambda r: -(r.get("lbc") or 0)):
    print("  %-11s %-9s %-6s lbc=%s pct=%.2f" % (r["code"], r["name"], r.get("shape"), r.get("lbc"), r.get("today_pct") or 0))

bp = json.load(open(os.path.join(E, "best_picks_20261029.json"), encoding="utf-8"))
print("\n== best_picks keys:", list(bp.keys()))
print("n_candidates", bp.get("n_candidates"), "n_anom", bp.get("n_anom"), "source", bp.get("source"))
print("weights:", json.dumps(bp.get("weights"), ensure_ascii=False)[:400])
allr = bp.get("all") or []
print("all n=%d ; item keys:" % len(allr), list(allr[0].keys()) if allr else None)
if allr: print(json.dumps(allr[0], ensure_ascii=False)[:900])
top = bp.get("top") or []
if top: print("\ntop[0]:", json.dumps(top[0], ensure_ascii=False)[:900])
asx = json.load(open(os.path.join(E, "auto_select_20261029_1600.json"), encoding="utf-8"))
print("\n== auto_select keys:", list(asx.keys()))
print("systems:", json.dumps(asx.get("systems"), ensure_ascii=False)[:900])
for k in ("picks", "selected", "results", "rows", "candidates"):
    if k in asx:
        v = asx[k]
        print(k, type(v).__name__, len(v) if hasattr(v, "__len__") else "")
        if isinstance(v, list) and v: print("  sample:", json.dumps(v[0], ensure_ascii=False)[:700])
