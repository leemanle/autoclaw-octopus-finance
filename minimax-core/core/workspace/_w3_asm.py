# -*- coding: utf-8 -*-
import json, os, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
W = r"C:\Users\Administrator\.minimax\workspace"
talk = json.load(open(os.path.join(W, "_w3_final.json"), encoding="utf-8"))["talk"]
clusters = json.load(open(os.path.join(W, "_w3_clusters.json"), encoding="utf-8"))
tag_top = json.load(open(os.path.join(W, "_w3_final.json"), encoding="utf-8"))["tag_top"]
zt = json.load(open(os.path.join(W, "_w3_zttop.json"), encoding="utf-8"))
zt_theme_top = json.load(open(os.path.join(W, "_w3_final.json"), encoding="utf-8"))["zt_theme_top"]

out = {
 "generated_at": "2026-10-29 20:0x",
 "source": {
   "pool": "C:\\Users\\Administrator\\.minimax\\tools\\_q_dzh_pool_1029_transcribe.py (POOL 67 + REASON)",
   "corpus_main": "C:\\Users\\Administrator\\Desktop\\选股系统备份\\_dav_score\\posts_merged_1240_1029.json (415帖)",
   "corpus_0800": "C:\\Users\\Administrator\\Desktop\\选股系统备份\\_dav_score\\posts_merged_0800_1029.json (381帖, 已核为1240的子集)",
   "close_hist": "C:\\Users\\Administrator\\Desktop\\选股系统备份\\_dav_score\\mkt_close_1029.json (5945只×86日, 日K到20261028)",
   "zt_pool": "C:\\Users\\Administrator\\Desktop\\选股系统备份\\_dav_score\\_conn\\anomaly_1029_1240.json (tag_name=涨停 37只)",
   "zt_high": "C:\\Users\\Administrator\\Desktop\\选股系统备份\\_dav_score\\_conn\\zt_hist_1240_1029.json + card_1240_1029.json",
   "history_reports": ["_daV_v100_1027_2100","_daV_v101_1028_0800","_daV_v102_1028_1240","_daV_v103_1028_1600","_daV_v104_1028_2100","_daV_v105_1029_0800","_daV_v106_1029_1240","_daV_v107_1029_1240"]
 },
 "caliber": {
   "mentions": "提及数 = 当日(10-29)帖子 stocks 点名次数 + 标题中股票名出现次数（语料仅标题层，无正文）",
   "threads": "讨论帖数 = 当日命中该股的帖子数（去重）",
   "title_hits": "标题提及次数（title_hits 字段）；tag_hits = 被帖子 stocks 点名次数",
   "window_note": "0800档语料为1240档子集（已核 aid 包含关系），两者不叠加计算",
   "zt_limit": "涨停判定：主板10%/创业板科创板20%/北交所30%/ST 5%；连板=连续交易日涨停（今日涨幅取大智慧信号池快照，历史日K取mkt_close）",
   "cluster_rule": "簇=REASON标签按共同主题合并；new_or_old 判据：无2板以上高标 + 簇内成员10-20~10-28无涨停史 + 当日≥2只涨停 → 新冒头；出现连板高标/簇内有前期涨停史/该题材连续多日出现 → 老热点"
 },
 "talk": talk,
 "tag_top": tag_top,
 "clusters": clusters,
 "zt_theme_top": zt_theme_top,
 "zt_raw_tag_top": zt["zt_raw_tags"],
 "zt_pool_n": zt["zt_n"]
}
js = json.dumps(out, ensure_ascii=False, indent=1)
open(os.path.join(W, "_w3_deliver.json"), "w", encoding="utf-8").write(js)
print("JSON bytes:", len(js.encode("utf-8")))
print(js[:1200])
