# -*- coding: utf-8 -*-
import json, os, datetime, sys
sys.stdout.reconfigure(encoding='utf-8')
W = r"C:\Users\Administrator\.minimax\workspace"
p = os.path.join(W, "_w3_deliver.json")
d = json.load(open(p, encoding="utf-8"))
d["generated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
d["output_path"] = "C:\\Users\\Administrator\\.minimax\\tools\\_q_dzh_w3_论坛题材_1029.json"
d["note"] = "本文件为 W3(舆情/题材取数员) 只读取数产物；未写入桌面/引擎目录，未修改任何源文件。"
js = json.dumps(d, ensure_ascii=False, indent=1)
open(p, "w", encoding="utf-8").write(js)
# 校验
d2 = json.load(open(p, encoding="utf-8"))
print("JSON OK · bytes=%d · keys=%s" % (len(js.encode("utf-8")), list(d2.keys())))
print("talk=%d  tag_top=%d  clusters=%d  zt_theme_top=%d  zt_pool_n=%s" % (
    len(d2["talk"]), len(d2["tag_top"]), len(d2["clusters"]), len(d2["zt_theme_top"]), d2["zt_pool_n"]))
print("cluster names:", [c["name"] for c in d2["clusters"]])
print("new_or_old:", collections.Counter(c["new_or_old"] for c in d2["clusters"]) if False else "")
import collections as _c
print("label counter:", dict(_c.Counter(c["new_or_old"] for c in d2["clusters"])))
print("talk 提及>0:", [(t["rank_today"], t["code"], t["name"], t["mentions"]) for t in d2["talk"] if t["mentions"] > 0])
mdp = os.path.join(W, "_w3_deliver.md")
md = open(mdp, encoding="utf-8").read()
md = md.replace("生成：2026-10-29 晚 · 舆情/题材取数员（W3）· 数据源全本地只读",
                "生成：%s · 舆情/题材取数员（W3）· 数据源全本地只读（未修改任何源文件）" % d["generated_at"])
open(mdp, "w", encoding="utf-8").write(md)
print("MD OK · chars=%d" % len(md))
