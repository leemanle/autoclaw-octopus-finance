# -*- coding: utf-8 -*-
"""
首板选股系统 - 根据用户指标
条件：首板=1 或者 首板天=0
"""

import requests
import time
from datetime import datetime, timedelta


# ============ 配置 ============
THS_PATH = r"D:\同花顺主本\hexinlauncher.exe"

# 选股条件
STOCKS = [
    # 这里会被动态替换
]

# ============ 数据获取 ============
def get_stock_kline(stock_code, days=60):
    """获取K线数据"""
    try:
        # 判断市场
        if stock_code.startswith('6') or stock_code.startswith('9'):
            market = '1'
        else:
            market = '0'

        url = "http://push2his.eastmoney.com/api/qt/stock/kline/get"
        params = {
            'secid': f'{market}.{stock_code}',
            'fields1': 'f1,f2,f3,f4,f5,f6',
            'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65',
            'klt': '101',
            'fqt': '0',
            'beg': '20250101',
            'end': '20500101'
        }

        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, params=params, headers=headers, timeout=10)
        data = response.json()

        if 'data' not in data or not data['data']:
            return []

        klines = []
        for item in data['data']['klines'][:days]:
            parts = item.split(',')
            klines.append({
                'date': parts[0],
                'open': float(parts[1]),
                'close': float(parts[2]),
                'high': float(parts[3]),
                'low': float(parts[4]),
                'volume': float(parts[5]),
                'amount': float(parts[6]),
            })

        return klines

    except Exception as e:
        print(f"  获取{stock_code}K线失败: {e}")
        return []


def calculate_indicators(klines):
    """计算各项指标"""
    if len(klines) < 10:
        return None

    # 各种涨幅计算
    for i, k in enumerate(klines):
        if i == 0:
            continue

        O = k['open']
        C = k['close']
        H = k['high']
        L = k['low']
        REF_C1 = klines[i-1]['close'] if i > 0 else C

        if REF_C1 == 0 or O == 0:
            continue

        # 计算各种涨幅
        k['涨幅'] = (C - O) / O  # 当日实体涨幅
        k['涨幅2'] = (C - REF_C1) / REF_C1  # 相对昨日收盘涨幅
        k['冲'] = (H - REF_C1) / REF_C1  # 冲高幅度
        k['上影'] = (H - max(O, C)) / max(O, C) if max(O, C) > 0 else 0
        k['下影'] = (min(O, C) - L) / L if L > 0 else 0
        k['实体'] = (max(O, C) - min(O, C)) / min(O, C) if min(O, C) > 0 else 0
        k['振幅'] = (H - L) / L if L > 0 else 0

    return klines


def check_first_board(klines):
    """
    检查是否符合首板条件
    
    条件1: 首板=1 (今日首板)
    条件2: 首板天=0 (今日就是首板日)
    
    首板公式:
    首板1:=冲>=0.08 AND EVERY(REF(涨幅2,1)<=0.085,3) AND 实体>=0.028 AND 涨幅2>=0.035
    首板2:=冲>=0.08 AND 涨幅2>=0.09 AND EVERY(REF(涨幅2,1)<=0.087,3)
    首板3:=首板1 OR 首板2
    首板:=首板3 AND EVERY(REF(首板3=0,1),2)
    """
    
    if len(klines) < 10:
        return False, {'reason': '数据不足'}

    today = klines[0]
    O = today['open']
    C = today['close']
    H = today['high']
    L = today['low']
    REF_C1 = klines[1]['close'] if len(klines) > 1 else C

    # 计算基础指标
    涨幅 = (C - O) / O if O > 0 else 0
    涨幅2 = (C - REF_C1) / REF_C1 if REF_C1 > 0 else 0
    冲 = (H - REF_C1) / REF_C1 if REF_C1 > 0 else 0
    
    max_oc = max(O, C)
    min_oc = min(O, C)
    上影 = (H - max_oc) / max_oc if max_oc > 0 else 0
    下影 = (min_oc - L) / L if L > 0 else 0
    实体 = (max_oc - min_oc) / min_oc if min_oc > 0 else 0

    # 一字板判断
    一字板 = (上影 < 0.001) and (下影 < 0.001) and (abs(涨幅) < 0.001)

    # 过去3天涨幅
    过去3天涨幅 = []
    for i in range(1, min(4, len(klines))):
        prev_close = klines[i-1]['close']
        curr_close = klines[i]['close']
        if prev_close > 0:
            过去3天涨幅.append((curr_close - prev_close) / prev_close)

    # 首板条件1
    首板1_冲 = 冲 >= 0.08
    首板1_历史 = len(过去3天涨幅) >= 3 and all(abs(chg) <= 0.085 for chg in 过去3天涨幅)
    首板1_实体 = 实体 >= 0.028
    首板1_涨幅2 = 涨幅2 >= 0.035
    首板1 = 首板1_冲 and 首板1_历史 and 首板1_实体 and 首板1_涨幅2

    # 首板条件2
    首板2_冲 = 冲 >= 0.08
    首板2_涨幅2 = 涨幅2 >= 0.09
    首板2_历史 = len(过去3天涨幅) >= 3 and all(abs(chg) <= 0.087 for chg in 过去3天涨幅)
    首板2 = 首板2_冲 and 首板2_涨幅2 and 首板2_历史

    # 首板 = 首板1 OR 首板2
    首板 = 首板1 or 首板2

    # 计算首板天 (从今天往前数，连续首板的天数)
    首板天 = 0
    if 首板:
        首板天 = 0  # 今天是首板
    else:
        # 检查最近几天是否有首板
        for i in range(1, min(30, len(klines))):
            k = klines[i]
            O_i = k['open']
            C_i = k['close']
            H_i = k['high']
            L_i = k['low']
            REF_C1_i = klines[i+1]['close'] if i+1 < len(klines) else C_i

            if REF_C1_i > 0:
                涨幅_i = (C_i - O_i) / O_i if O_i > 0 else 0
                涨幅2_i = (C_i - REF_C1_i) / REF_C1_i if REF_C1_i > 0 else 0
                冲_i = (H_i - REF_C1_i) / REF_C1_i if REF_C1_i > 0 else 0
                
                max_oc_i = max(O_i, C_i)
                min_oc_i = min(O_i, C_i)
                实体_i = (max_oc_i - min_oc_i) / min_oc_i if min_oc_i > 0 else 0
                
                上影_i = (H_i - max_oc_i) / max_oc_i if max_oc_i > 0 else 0
                下影_i = (min_oc_i - L_i) / L_i if L_i > 0 else 0
                
                # 过去3天
                过去3天涨幅_i = []
                for j in range(i+1, min(i+4, len(klines))):
                    prev = klines[j-1]['close']
                    curr = klines[j]['close']
                    if prev > 0:
                        过去3天涨幅_i.append((curr - prev) / prev)
                
                首板1_i = (冲_i >= 0.08 and 
                          len(过去3天涨幅_i) >= 3 and all(abs(c) <= 0.085 for c in 过去3天涨幅_i) and
                          实体_i >= 0.028 and 涨幅2_i >= 0.035)
                
                首板2_i = (冲_i >= 0.08 and 涨幅2_i >= 0.09 and 
                          len(过去3天涨幅_i) >= 3 and all(abs(c) <= 0.087 for c in 过去3天涨幅_i))
                
                if 首板1_i or 首板2_i:
                    首板天 = i
                    break

    return 首板 or 首板天 == 0, {
        '首板': 首板,
        '首板天': 首板天,
        '涨幅2': 涨幅2,
        '冲': 冲,
        '实体': 实体,
        '上影': 上影,
        '下影': 下影,
        '一字板': 一字板,
    }


def get_sector_stocks(sector_code):
    """获取板块内个股"""
    try:
        url = "http://push2.eastmoney.com/api/qt/clist/get"
        params = {
            'pn': 1,
            'pz': 20,
            'po': 1,
            'fltt': 2,
            'invt': 2,
            'fid': 'f3',
            'fs': f'b:{sector_code}',
            'fields': 'f2,f3,f4,f5,f12,f14,f15,f16,f17'
        }

        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, params=params, headers=headers, timeout=10)
        data = response.json()

        stocks = []
        if 'data' in data and data['data'] and 'diff' in data['data']:
            diff = data['data']['diff']
            # diff可能是dict或list
            items = diff.values() if isinstance(diff, dict) else diff
            for item in items:
                stocks.append({
                    'code': item['f12'],
                    'name': item['f14'],
                    'price': item['f2'],
                    'change': item['f3'] / 100,
                    'high': item['f15'],
                    'low': item['f16'],
                    'open': item['f17'],
                })

        return stocks

    except Exception as e:
        print(f"  获取板块{sector_code}失败: {e}")
        return []


def scan_sectors():
    """扫描热门板块找首板股"""
    
    # 热门板块列表
    sectors = [
        ('BK0489', '人工智能'),
        ('BK0728', '新能源'),
        ('BK0727', '芯片'),
        ('BK0459', '光伏'),
        ('BK0983', '储能'),
        ('BK0846', '机器人'),
        ('BK0896', '新能源汽车'),
        ('BK0450', '创新药'),
    ]

    results = []

    print("=" * 60)
    print("首板选股系统")
    print("条件: 首板=1 或 首板天=0")
    print("=" * 60)

    for sector_code, sector_name in sectors:
        print(f"\n📊 板块: {sector_name}")

        stocks = get_sector_stocks(sector_code)
        if not stocks:
            print(f"    ⚠️ 无个股数据")
            continue

        # 只检查涨幅前10
        for stock in stocks[:10]:
            code = stock['code']
            name = stock['name']
            change = stock['change']

            print(f"  🔍 {name} ({code}) 涨幅:{change:.2%}")

            # 获取K线
            klines = get_stock_kline(code, days=30)
            if not klines:
                continue

            # 计算指标
            klines = calculate_indicators(klines)
            if not klines:
                continue

            # 检查首板条件
            is_match, info = check_first_board(klines)

            if is_match:
                print(f"    ✅ 符合条件! 首板={info['首板']}, 首板天={info['首板天']}")
                results.append({
                    **stock,
                    'sector': sector_name,
                    '首板': info['首板'],
                    '首板天': info['首板天'],
                    '冲': info['冲'],
                    '实体': info['实体'],
                    '涨幅2': info['涨幅2'],
                })
            else:
                reason = '数据不足' if info.get('reason') else f'非首板'
                print(f"    ❌ {reason}")

    return results


def main():
    """主函数"""
    print("\n🚀 开始首板选股...")
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    results = scan_sectors()

    print("\n" + "=" * 60)
    print(f"🏆 选股结果: {len(results)}只")
    print("=" * 60)

    if results:
        print(f"\n{'代码':<8} {'名称':<10} {'涨幅':<8} {'板块':<10} {'首板':<6} {'首板天':<6}")
        print("-" * 60)
        for r in results:
            print(f"{r['code']:<8} {r['name']:<10} {r['change']:>6.2%} {r['sector']:<10} {r['首板']:<6} {r['首板天']:<6}")
    else:
        print("\n❌ 未找到符合首板条件的股票")

    return results


if __name__ == '__main__':
    main()
