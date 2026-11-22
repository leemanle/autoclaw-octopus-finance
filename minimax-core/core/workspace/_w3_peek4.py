# -*- coding: utf-8 -*-
import json, os, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
E = r"C:\Users\Administrator\首阳战法回测引擎\reports"
asx = json.load(open(os.path.join(E, "auto_select_20261029_1600.json"), encoding="utf-8"))
u = asx.get("union")
print("union type:", type(u).__name__, len(u) if hasattr(u, "__len__") else "")
if isinstance(u, list) and u:
    print("item keys:", list(u[0].keys()))
    print(json.dumps(u[0], ensure_ascii=False)[:800])
    themes = collections.Counter(r.get("theme") for r in u)
    print("\nunion theme 分布:", json.dumps(themes, ensure_ascii=False, indent=0)[:1200])
    print("\nunion 里 anom_tag 分布:", collections.Counter(r.get("anom_tag") for r in u))
sd = asx.get("systems_detail")
print("\nsystems_detail type:", type(sd).__name__)
if isinstance(sd, dict):
    for k, v in sd.items():
        n = len(v) if hasattr(v, "__len__") else v
        print(" ", k, type(v).__name__, n)
        if isinstance(v, list) and v: print("     sample:", json.dumps(v[0], ensure_ascii=False)[:400])
