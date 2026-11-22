# -*- coding: utf-8 -*-
import os, re, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
B = r"C:\Users\Administrator\Desktop\选股系统备份"
files = ["_daV_v100_1027_2100_forum_11v.md","_daV_v101_1028_0800_forum_11v.md","_daV_v102_1028_1240_forum_11v.md",
         "_daV_v103_1028_1600_forum_11v.md","_daV_v104_1028_2100_forum_11v.md","_daV_v105_1029_0800_forum_11v.md",
         "_daV_v106_1029_1240_forum_11v.md","_daV_v107_1029_1240_forum_11v.md"]
KW = ["商业航天","卫星","军工","可控核聚变","太空算力","冰雪经济","人形机器人","机器人","低空经济",
      "固态电池","风电","液冷","脑机接口","数据中心","三季报","AI教育","钙钛矿","军工电子","光模块"]
for f in files:
    p = os.path.join(B, f)
    if not os.path.exists(p): print(f, "MISSING"); continue
    t = open(p, encoding="utf-8").read()
    c = {k: t.count(k) for k in KW if t.count(k)}
    print("%-42s len=%6d  %s" % (f, len(t), json.dumps(c, ensure_ascii=False) if False else c))
