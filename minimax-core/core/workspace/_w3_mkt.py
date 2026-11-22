# -*- coding: utf-8 -*-
import json, os
p = r"C:\Users\Administrator\Desktop\选股系统备份\_dav_score\mkt_close_1029.json"
d = json.load(open(p, encoding="utf-8"))
print("top type:", type(d).__name__)
if isinstance(d, dict):
    ks = list(d.keys())
    print("nkeys:", len(ks), "sample:", ks[:15])
    for k in ks[:2]:
        v = d[k]
        print("---", k, type(v).__name__, (len(v) if hasattr(v, "__len__") else ""))
        if isinstance(v, list) and v:
            print(json.dumps(v[0], ensure_ascii=False)[:800])
        elif isinstance(v, dict):
            print(json.dumps(dict(list(v.items())[:2]), ensure_ascii=False)[:800])
elif isinstance(d, list):
    print("len:", len(d))
    print(json.dumps(d[0], ensure_ascii=False)[:1000])
