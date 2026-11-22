# -*- coding: utf-8 -*-
import json, os, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
C = r"C:\Users\Administrator\Desktop\选股系统备份\_dav_score\_conn"
E = r"C:\Users\Administrator\首阳战法回测引擎\reports"
def peek(p, label):
    if not os.path.exists(p):
        print(label, "MISSING"); return None
    d = json.load(open(p, encoding="utf-8"))
    print("=" * 70); print(label, type(d).__name__, (len(d) if hasattr(d, "__len__") else ""))
    if isinstance(d, dict):
        ks = list(d.keys()); print(" keys:", ks[:12])
        for k in ks[:2]:
            print("  ", k, "=>", json.dumps(d[k], ensure_ascii=False)[:600])
    elif isinstance(d, list):
        print(" ", json.dumps(d[0], ensure_ascii=False)[:900])
        print(" item keys:", list(d[0].keys()) if isinstance(d[0], dict) else None)
    return d
a = peek(os.path.join(C, "zt_hist_0800_1029.json"), "zt_hist_0800_1029")
b = peek(os.path.join(C, "close_1130_1240_1029.json"), "close_1130_1240_1029")
c = peek(os.path.join(E, "best_picks_20261029.json"), "best_picks_20261029")
d = peek(os.path.join(E, "auto_select_20261029_1600.json"), "auto_select_20261029_1600")
if isinstance(a, list) and a:
    print("\nzt_hist_0800 item keys:", list(a[0].keys()))
    print("sample:", json.dumps(a[0], ensure_ascii=False)[:400])
    print("is_zt True:", sum(1 for r in a if r.get("is_zt")))
