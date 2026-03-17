# -*- coding: utf-8 -*-
"""
基本面与利好分析模块
"""

import requests
import re
from datetime import datetime
from trading_config import CONFIG, GOOD_NEWS_KEYWORDS, GOOD_CONCEPTS, RISK_KEYWORDS


class FundamentalAnalyzer:
    """基本面与利好分析器"""

    def __init__(self):
        self.timeout = CONFIG['REQUEST_TIMEOUT']

    def analyze_company(self, stock_code):
        """
        分析公司基本面和利好消息

        参数：
            stock_code: 股票代码

        返回：
            分析结果
        """
        result = {
            'score': 0,
            'reasons': [],
            'warnings': [],
            'concepts': [],
            'good_news': [],
        }

        try:
            # 1. 获取股票基本信息
            basic_info = self._get_basic_info(stock_code)

            # 2. 获取概念题材
            concepts = self._get_concepts(stock_code)
            result['concepts'] = concepts

            # 3. 获取重大公告
            announcements = self._get_announcements(stock_code)

            # 4. 获取资金流向
            fund_flow = self._get_fund_flow(stock_code)

            # 综合评分
            # 利好新闻
            good_news_count = len(result['good_news'])
            if good_news_count > 0:
                score_add = min(30, good_news_count * 10)
                result['score'] += score_add
                result['reasons'].append(f"利好公告: {good_news_count}条")

            # 热门概念
            hot_concepts = [c for c in concepts if any(g in c for g in GOOD_CONCEPTS)]
            if len(hot_concepts) >= 2:
                result['score'] += 20
                result['reasons'].append(f"热门概念: {len(hot_concepts)}个 ({','.join(hot_concepts[:2])})")

            # 资金流入
            if fund_flow > 0:
                result['score'] += 15
                result['reasons'].append(f"资金净流入")

            # 风险检查
            if 'ST' in basic_info.get('name', ''):
                result['warnings'].append("ST股票，风险较高")
                result['score'] -= 30

            pe = basic_info.get('pe', 0)
            if pe and pe > 100:
                result['warnings'].append(f"市盈率过高 ({pe:.2f})")
                result['score'] -= 10

            # 确保分数在合理范围
            result['score'] = max(0, min(100, result['score']))

        except Exception as e:
            print(f"      [基本面] ⚠ 分析失败: {e}")

        return result

    def _get_basic_info(self, stock_code):
        """获取股票基本信息"""
        try:
            url = "http://push2.eastmoney.com/api/qt/stock/get"

            # 构造6位代码
            code = stock_code[:6]

            # 判断市场
            if code.startswith('6') or code.startswith('9'):
                market = '1'
            else:
                market = '0'

            params = {
                'secid': f'{market}.{code}',
                'fields': 'f12,f13,f14,f2,f3,f4,f5,f6,f7,f8,f9,f.f10,f11,f15,f16,f17,f18,f62,f115,f124,f58,f107,f152,f161,f162,f163,f164,f165,f166,f167,f168,f169,f170'
            }

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            response = requests.get(url, params=params, headers=headers, timeout=self.timeout)
            response.raise_for_status()

            data = response.json()

            if 'data' in data:
                return {
                    'name': data['data'].get('f14', ''),
                    'pe': data['data'].get('f9', 0) / 100 if data['data'].get('f9') else 0,
                    'market_cap': data['data'].get('f116', 0) / 10000 if 'f116' in data['data'] else 0,
                }

        except Exception as e:
            pass

        return {}

    def _get_concepts(self, stock_code):
        """获取概念题材"""
        try:
            url = "http://push2.eastmoney.com/api/qt/stock/kline/get"

            # 构造6位代码
            code = stock_code[:6]

            # 判断市场
            if code.startswith('6') or code.startswith('9'):
                market = '1'
            else:
                market = '0'

            # 使用概念板块接口
            url = "http://push2.eastmoney.com/api/qt/clist/get"
            params = {
                'pn': 1,
                'pz': 500,
                'po': 1,
                'np': 1,
                'ut': 'bd1d9ddb0408972cf9c27f6f742628c4',
                'fltt': 2,
                'invt': 2,
                'fid': 'f3',
                'fs': f'b:BK{market}',  # 概念板块
                'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152'
            }

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            response = requests.get(url, params=params, headers=headers, timeout=self.timeout)
            response.raise_for_status()

            data = response.json()

            concepts = []
            for item in data['data']['diff']:
                concepts.append(item['f14'])

            return concepts

        except Exception as e:
            return []

    def _get_announcements(self, stock_code):
        """获取重大公告"""
        try:
            url = "http://np-anotice-stock.eastmoney.com/Notice/getNoticeInfo"
            code = stock_code[:6]

            params = {
                'sr': -1,
                'lmt': 10,
                'rt': 0,
                'scode': code
            }

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Referer': 'http://data.eastmoney.com/notices/stock.html'
            }

            response = requests.get(url, params=params, headers=headers, timeout=self.timeout)
            response.raise_for_status()

            data = response.json()

            good_news = []

            if 'data' in data and 'list' in data['data']:
                for item in data['data']['list']:
                    title = item.get('notice_title', '')

                    # 检查利好关键词
                    is_good = any(kw in title for kw in GOOD_NEWS_KEYWORDS)
                    is_risk = any(kw in title for kw in RISK_KEYWORDS)

                    if is_good:
                        good_news.append(title)
                        print(f"        📰 利好: {title[:30]}")

                    elif is_risk:
                        print(f"        ⚠️  风险公告: {title[:30]}")

            return good_news

        except Exception as e:
            return []

    def _get_fund_flow(self, stock_code):
        """获取资金流向"""
        try:
            url = "http://push2.eastmoney.com/api/qt/stock/fflow/daykline/get"

            # 构造6位代码
            code = stock_code[:6]

            # 判断市场
            if code.startswith('6') or code.startswith('9'):
                market = '1'
            else:
                market = '0'

            params = {
                'secid': f'{market}.{code}',
                'fields1': 'f1,f2,f3,f7',
                'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65',
                'klt': '101',
                'fqt': '0',
                'beg': '20250101',
                'end': '20500101'
            }

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            response = requests.get(url, params=params, headers=headers, timeout=self.timeout)
            response.raise_for_status()

            data = response.json()

            if 'data' in data and data['data'] and 'items' in data['data']:
                # 取最新一天的资金流入
                latest = data['data']['items'][0]
                return float(latest.split(',')[2])  # 主力净流入

        except Exception as e:
            pass

        return 0
