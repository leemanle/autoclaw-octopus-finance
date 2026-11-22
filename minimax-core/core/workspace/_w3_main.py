# -*- coding: utf-8 -*-
import json, os, collections, re, sys, io
sys.stdout.reconfigure(encoding='utf-8')
BASE = r"C:\Users\Administrator\Desktop\选股系统备份"
D = os.path.join(BASE, "_dav_score")
C = os.path.join(D, "_conn")
TOOLS = r"C:\Users\Administrator\.minimax\tools"

# ---------- 1. POOL + REASON ----------
import importlib.util
spec = importlib.util.spec_from_file_location("pool", os.path.join(TOOLS, "_q_dzh_pool_1029_transcribe.py"))
poolmod = importlib.util.module_from_spec(spec); spec.loader.exec_module(poolmod)
POOL = poolmod.POOL; REASON = poolmod.REASON
name_by_code = {c: n for c, n, _ in POOL}
chg_by_code = {c: ch for c, _, ch in POOL}
codes = [c for c, _, _ in POOL]
print("POOL n=%d  REASON n=%d" % (len(POOL), len(REASON)))

# ---------- 2. corpus ----------
posts = json.load(open(os.path.join(D, "posts_merged_1240_1029.json"), encoding="utf-8"))
posts0800 = json.load(open(os.path.join(D, "posts_merged_0800_1029.json"), encoding="utf-8"))
aids1240 = set(p["aid"] for p in posts)
aids0800 = set(p["aid"] for p in posts0800)
print("0800 subset of 1240 ?", aids0800 <= aids1240, "| 1240 n=%d 0800 n=%d" % (len(posts), len(posts0800)))
print("0800-only posts:", len(aids0800 - aids1240))

def digit(code):
    c = str(code).strip().lower()
    c = re.sub(r'^(sh|sz|bj|hk)', '', c)
    return c if re.fullmatch(r'\d{6}', c) else None

def tagset(p):
    s = set()
    for c, n in (p.get("stocks") or []):
        d = digit(c)
        if d: s.add(d)
        if n: s.add("#" + n)
    return s

# per-post index: code -> list of posts
idx = collections.defaultdict(list)
for p in posts:
    t = (p.get("title") or "")
    ts = tagset(p)
    for c, n in (p.get("stocks") or []):
        d = digit(c)
        if d: idx[d].append(p)
    # name matches in title
    for c in codes:
        nm = name_by_code[c]
        if nm and nm in t:
            if not any(p is q for q in idx[c]):
                idx[c].append(p)

def stats(subset_codes):
    out = {}
    for c in subset_codes:
        hits = idx.get(c, [])
        day = [p for p in hits if (p.get("ct") or "")[:10] == "2026-10-29"]
        tag_m = 0; title_m = 0; title_hits = 0
        for p in day:
            for cc, nn in (p.get("stocks") or []):
                if digit(cc) == c: tag_m += 1
            nm = name_by_code[c]
            if nm and nm in (p.get("title") or ""):
                title_m += (p.get("title") or "").count(nm)
        out[c] = dict(mentions=tag_m + title_m, tag_m=tag_m, title_m=title_m,
                      threads=len(day), first_at=min([p["ct"] for p in day], default=""),
                      last_at=max([p["ct"] for p in day], default=""),
                      posts=day)
    return out

st = stats(codes)
ranked = sorted(codes, key=lambda c: (-st[c]["mentions"], -st[c]["threads"], codes.index(c)))
print("\n=== A. 当日(10-29)提及排名 全 67 只 ===")
for i, c in enumerate(ranked, 1):
    s = st[c]
    print("%2d %-7s %-9s mentions=%d(tag%d+title%d) threads=%d first=%s last=%s" % (
        i, c, name_by_code[c], s["mentions"], s["tag_m"], s["title_m"], s["threads"],
        s["first_at"][5:16] if s["first_at"] else "-", s["last_at"][5:16] if s["last_at"] else "-"))
print("提及数>0 的只数:", sum(1 for c in codes if st[c]["mentions"] > 0))
json.dump({c: {k: v for k, v in st[c].items() if k != "posts"} for c in codes},
          open(r"C:\Users\Administrator\.minimax\workspace\_w3_stats.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

# ---------- 3. TAGS from REASON ----------
raw_tags = collections.defaultdict(list)
for c, n, ch in POOL:
    r = (REASON.get(c) or "").strip()
    if not r:
        continue
    for t in r.split("+"):
        t = t.strip()
        if t: raw_tags[t].append(c)
print("\n=== B. 原始标签数: %d 个 ===" % len(raw_tags))
order = sorted(raw_tags.items(), key=lambda kv: (-len(kv[1]), kv[0]))
for t, cs in order[:30]:
    print("%3d %-28s %s" % (len(cs), t, " ".join(cs)))
print("\n无 REASON 的:", [c for c in codes if not (REASON.get(c) or "").strip()])
json.dump({"tags": {t: v for t, v in raw_tags.items()},
           "pool": [[c, n, ch] for c, n, ch in POOL],
           "reason": REASON},
          open(r"C:\Users\Administrator\.minimax\workspace\_w3_tags.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
