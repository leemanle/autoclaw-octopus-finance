# -*- coding: utf-8 -*-
"""按规则 A-G 逐条核验 13 条 cron 当前正文（DB 实时）"""
import sqlite3, io, os

D = r'C:\Users\Administrator\Desktop\选股系统备份\_cron_prompt_backup_20261020\current'
IDS = ['08e1e6d2-dc0e-4b40-be67-e7ce4f1bfd5b', 'ae876db6-c4c7-4db0-a04b-0b703feeda87',
       'cc9cacc9-8769-4e49-93f9-3017193ea4ae', '438176c5-e351-40d9-b50a-6fbaa7199499',
       '4400f518-a316-4894-9b41-0dd5d07094aa', 'c98fb932-e4c2-429d-85c1-8750d6388d49',
       '756e20e4-4434-4cd5-8458-f10b8d411361', '6912b194-d609-4a39-abf3-bf57b1aef259',
       'e22a3275-2b61-4eef-83b1-37572e431dbe', 'be37c6fb-2847-41e4-ad7a-cb70dcf8dc17',
       'd4dc649c-c869-4582-b8ab-4ff8a44ebd2f', 'cdf5eaa2-dd70-4697-ae80-8e2b3f3b3d63',
       'f7a09137-3c8d-4660-873a-e639dc480fbc']

# 作废口径「仍在使用」的特征串（出现即残留）
LIVE = ['现改用本框专用阶段涨幅闸', '本框选股闸门 = 本框专用阶段涨幅闸',
        '这是本框专用例外', '本框专用例外：', '本闸门是本框专用例外',
        '★ 例外声明：总集 §1.1', '★ 与总集 §1.1 的关系（例外声明',
        '三条全过 = 符合', '缺数据 = 不符合（缺数据不放过）',
        '基准日：一进二 / 二进三 = 昨日封板日；首阳池 = 前一交易日',
        '唯一实现：桌面\\选股系统备份\\_gate_stage.py',
        '本框留档不适用', '通过本框阶段涨幅闸只数',
        '对首板是作废项、对本框是现行闸门', '对本框三系统是现行闸门',
        '不一致必须写出卡在哪一条（5日涨幅', '复盘输出逐只标「符合 / 不符合」，不再标红线 PASS / FAIL；\n  不符合必须写出卡在哪一条（5日涨幅']

c = sqlite3.connect(r'C:\Users\Administrator\.minimax\v2\sqlite\runtime-state.sqlite')
c.row_factory = sqlite3.Row
print('%-36s %-30s %-7s %s' % ('cron_id', 'name', 'len', '核验'))
for cid in IDS:
    r = c.execute('select name,prompt from local_runtime_v2_cron_definitions where cron_id=?', (cid,)).fetchone()
    p = r['prompt'] or ''
    with io.open(os.path.join(D, cid + '.txt'), 'w', encoding='utf-8', newline='') as f:
        f.write(p)
    bad = [k for k in LIVE if k in p]
    # 必须存在的现行口径
    need = []
    if '涨幅类闸门全废' not in p and '不设任何红线' not in p:
        need.append('缺标准块')
    if '30/40/60 这组数已整组作废' in p:
        need.append('规则D已改')
    print('%-36s %-30s %-7d %s' % (cid[:36], (r['name'] or '')[:28], len(p),
                                   ('残留:' + ';'.join(bad)) if bad else ('OK ' + ','.join(need) if need else 'OK')))
c.close()
