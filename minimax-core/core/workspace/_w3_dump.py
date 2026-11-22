# -*- coding: utf-8 -*-
import json, os
DS = r"C:\Users\Administrator\Desktop\选股系统备份\_dav_score"
d = json.load(open(os.path.join(DS, "posts_merged_1240_1029.json"), encoding="utf-8"))
today = [x for x in d if (x.get("ct") or "")[:10] == "2026-10-29"]
today.sort(key=lambda x: x["ct"])
print("posts ct=2026-10-29 :", len(today))
for i, x in enumerate(today, 1):
    st = ";".join("%s/%s" % (c, n) for c, n in (x.get("stocks") or []))
    print("%2d | %s | %s | nick=%s | cm=%s like=%s | on_dav=%s on_extra=%s" % (
        i, x["ct"], x["title"][:90], x.get("nick"), x.get("cm"), x.get("like"), x.get("on_dav"), x.get("on_extra")))
    print("      stocks: %s" % (st if st else "(none)"))
print()
print("### posts 10-28 (top 40 by ct desc) for context ###")
prev = [x for x in d if (x.get("ct") or "")[:10] == "2026-10-28"]
prev.sort(key=lambda x: x["ct"], reverse=True)
for x in prev[:40]:
    st = ";".join("%s/%s" % (c, n) for c, n in (x.get("stocks") or []))
    print("%s | %s | %s" % (x["ct"], x["title"][:80], st[:120]))
