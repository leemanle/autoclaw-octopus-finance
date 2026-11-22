# -*- coding: utf-8 -*-
import json, os, collections
C = r"C:\Users\Administrator\Desktop\选股系统备份\_dav_score\_conn"
def peek(f, n=1):
    p = os.path.join(C, f)
    if not os.path.exists(p):
        print(f, "-> MISSING"); return None
    d = json.load(open(p, encoding="utf-8"))
    print("=" * 72)
    print(f, "top:", type(d).__name__, (len(d) if hasattr(d, "__len__") else ""))
    if isinstance(d, dict):
        ks = list(d.keys())
        print(" keys sample:", ks[:12])
        for k in ks[:n]:
            v = d[k]
            print("  --", k, "=>", type(v).__name__, (len(v) if hasattr(v, "__len__") else ""))
            print("     ", json.dumps(v, ensure_ascii=False)[:700])
    elif isinstance(d, list):
        print(" len:", len(d))
        print(" ", json.dumps(d[0], ensure_ascii=False)[:900])
    return d
zt = peek("zt_hist_1240_1029.json")
cd = peek("card_1240_1029.json")
an = peek("anomaly_1029_1240.json")
if isinstance(zt, list) and zt:
    print("\nZT item keys:", list(zt[0].keys()))
    print("ZT sample:", json.dumps(zt[0], ensure_ascii=False))
if isinstance(cd, dict):
    k0 = list(cd.keys())[0]
    print("\nCARD sample:", k0, json.dumps(cd[k0], ensure_ascii=False)[:800])
if isinstance(an, dict):
    k0 = list(an.keys())[0]
    print("\nANOM sample:", k0, json.dumps(an[k0], ensure_ascii=False)[:800])
