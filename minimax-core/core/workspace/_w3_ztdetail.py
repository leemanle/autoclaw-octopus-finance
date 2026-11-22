# -*- coding: utf-8 -*-
import json, os, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
C = r"C:\Users\Administrator\Desktop\选股系统备份\_dav_score\_conn"
an = json.load(open(os.path.join(C, "anomaly_1029_1240.json"), encoding="utf-8"))
ztA = [r for r in an if r.get("tag_name") == "涨停"]
print("涨停 %d 只（全关键词明细）" % len(ztA))
for r in sorted(ztA, key=lambda r: r["thscode"]):
    print("%-11s %-9s kw=%s" % (r["thscode"], r.get("stock_name"), " / ".join(r.get("keyword_list") or [])))
