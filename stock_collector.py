# -*- coding: utf-8 -*-
"""
个股数据采集模块
"""

import requests
import time
from datetime import datetime, timedelta
from trading_config import CONFIG


class StockCollector:
    """个股数据采集器"""

    def __init__(self):
        self.timeout = CONFIG['REQUEST_TIMEOUT']

    def get_top_stocks_in_sector(self, sector_code, top_n=None):
        """
        获取板块内涨幅前N的个股

        参数：
            sector_code: 板块代码
            top_n: 返回数量

        返回：
            个股列表
        """
        top_n = top_n or CONFIG['TOP_STOCKS_IN_SECTOR']

        try:
            # 使用东方财富板块成分股接口
            url = "http://push2.eastmoney.com/api/qt/clist/get"
            params = {
                'pn': 1,
                'pz': top_n,
                'po': 1,
                'np': 1,
                'fltt': 2,
                'invt': 2,
                'fid': 'f3',  # 按涨幅排序
                'fs': f'b:{sector_code}',  # 板块代码
                'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152,f117,f127'
            }

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            response = requests.get(url, params=params, headers=headers, timeout=self.timeout)
            response.raise_for_status()

            data = response.json()

            stocks = []
            if 'data' in data and data['data'] and 'diff' in data['data']:
                for item in data['data']['diff']:
                    stocks.append({
                        'code': item['f12'],
                        'name': item['f14'],
                        'price': item['f2'],
                        'change': item['f3'] / 100,
                        'volume': item['f5'],
                        'amount': item['f6'] / 10000,
                        'high': item['f15'],
                        'low': item['f16'],
                        'open': item['f17'],
                        'pe': item['f9'],
                        'market_cap': item['f116'] / 10000 if 'f116' in item else 0,
                    })

            return stocks

        except Exception as e:
            print(f"    [个股采集] ❌ 获取板块{sector_code}个股失败: {e}")
            return []

    def get_kline_data(self, stock_code, days=10):
        """
        获取K线数据

        参数：
            stock_code: 股票代码（如 '000001'）
            days: 获取天数

        返回：
            K线数据列表（倒序，最新的在前）
        """
        try:
            # 构造6位股票代码
            if len(stock_code) == 6:
                ts_code = stock_code
            else:
                ts_code = stock_code[:6]

            # 判断市场
            if ts_code.startswith('6') or ts_code.startswith('9'):
                market = '1'  # 上海
            else:
                market = '0'  # 深圳

            full_code = f'{market}.{ts_code}'

            # 从东方财富获取K线
            url = "http://push2his.eastmoney.com/api/qt/stock/kline/get"

            params = {
                'secid': full_code,
                'fields1': 'f1,f2,f3,f4,f5,f6',
                'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65',
                'klt': '101',  # 日K线
                'fqt': '0',  # 不复权
                'beg': '20240101',
                'end': '20500101'
            }

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            response = requests.get(url, params=params, headers=headers, timeout=self.timeout)
            response.raise_for_status()

            data = response.json()

            if 'data' not in data or not data['data']:
                return []

            # 解析K线数据
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
                    'change': 0  # 需要计算
                })

            # 计算涨跌幅
            for i in range(len(klines)):
                if i < len(klines) - 1:
                    if klines[i+1]['close'] != 0:
                        klines[i]['change'] = (klines[i]['close'] - klines[i+1]['close']) / klines[i+1]['close']

            return klines

        except Exception as e:
            print(f"      [K线] ❌ 获取{stock_code}K线失败: {e}")
            return []
