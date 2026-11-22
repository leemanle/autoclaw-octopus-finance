# -*- coding: utf-8 -*-
import json, collections, os
DS = r"C:\Users\Administrator\Desktop\选股系统备份\_dav_score"
for f in ("posts_merged_1240_1029.json", "posts_merged_0800_1029.json"):
    p = os.path.join(DS, f)
    d = json.load(open(p, encoding="utf-8"))
    print("=" * 70)
    print(f, "posts:", len(d))
    keys = collections.Counter()
    for x in d:
        keys.update(x.keys())
    print("field coverage:", dict(keys))
    cts = sorted(x.get("ct", "") for x in d)
    print("ct min/max:", cts[0], "|", cts[-1])
    print("date prefixes:", collections.Counter(c[:10] for c in cts))
    print("srcs:", collections.Counter(s for x in d for s in (x.get("srcs") or [])))
    print("on_dav:", collections.Counter(x.get("on_dav") for x in d),
          "on_extra:", collections.Counter(x.get("on_extra") for x in d))
    print("stocks empty:", sum(1 for x in d if not x.get("stocks")))
    print("like nonempty:", sum(1 for x in d if x.get("like")))
    ne = [x for x in d if x.get("cm")]
    print("cm nonempty:", len(ne))
    if ne:
        print("SAMPLE cm post:", json.dumps(ne[0], ensure_ascii=False)[:900])
