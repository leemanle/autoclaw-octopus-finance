# 智能选股与模拟交易系统架构

## 策略概述

### 选股流程

1. **板块筛选**：涨幅 > 1% 的板块
2. **个股筛选**：板块内涨幅前10的个股
3. **首板识别**：符合"首板=1"公式（首次涨停）
4. **利好分析**：新闻、公告、资金流分析
5. **智能评分**：综合打分筛选高潜力个股
6. **模拟交易**：自动买入并跟踪

---

## 系统架构设计

### 模块划分

```
┌─────────────────────────────────────────────────────────┐
│                     主控调度器                            │
│              (Main Scheduler / Coordinator)              │
└──────────────┬──────────────────────┬───────────────────┘
               │                      │
    ┌──────────▼──────────┐  ┌───────▼────────┐
    │   板块数据采集       │  │   基本面分析     │
    │  (Sector Collector) │  │ (Fundamental)   │
    └──────────┬──────────┘  └───────┬────────┘
               │                      │
    ┌──────────▼──────────┐  ┌───────▼────────┐
    │   个股数据采集       │  │   新闻舆情分析   │
    │ (Stock Collector)   │  │  (News Sentiment)│
    └──────────┬──────────┘  └───────┬────────┘
               │                      │
    ┌──────────▼──────────┐  ┌───────▼────────┐
    │   首板公式计算       │  │   资金流向分析   │
    │ (FirstBoard Engine) │  │  (Fund Flow)    │
    └──────────┬──────────┘  └───────┬────────┘
               │                      │
    ┌──────────▼──────────────────────▼──────────┐
    │               智能评分引擎                    │
    │          (Intelligent Scoring)               │
    └──────────┬──────────────────────┬───────────┘
               │                      │
    ┌──────────▼──────────┐  ┌───────▼────────┐
    │    选股结果输出     │  │   模拟交易引擎   │
    │  (Result Exporter)  │  │  (Paper Trading)│
    └─────────────────────┘  └──────────────────┘
```

---

## 核心模块详细设计

### 模块 1: 板块数据采集 (SectorCollector)

**功能：**
- 获取所有板块实时涨幅数据
- 筛选涨幅 > 1% 的板块
- 按涨幅排序

**数据来源：**
- 同花顺板块指数
- 东方财富板块数据
- 东方财富 API：`http://push2.eastmoney.com/api/qt/clist/get`

```python
class SectorCollector:
    """板块数据采集器"""

    def get_sectors(self, min_change=1.0):
        """获取涨幅 > min_change 的板块"""
        # 方案1：从同花顺桌面版读取
        sectors = self._read_from_ths()

        # 方案2：东方财富API
        sectors = self._fetch_from_eastmoney()

        # 筛选
        hot_sectors = [
            s for s in sectors
            if s['change'] >= min_change
        ]

        # 按涨幅降序
        hot_sectors.sort(key=lambda x: x['change'], reverse=True)

        return hot_sectors

    def _read_from_ths(self):
        """从同花顺读取板块数据（需要UI自动化）"""
        # TODO: 实现窗口定位和数据提取
        pass

    def _fetch_from_eastmoney(self):
        """从东方财富API获取板块数据"""
        import requests

        url = "http://push2.eastmoney.com/api/qt/clist/get"
        params = {
            'pn': 1,
            'pz': 100,
            'po': 1,
            'np': 1,
            'ut': 'bd1d9ddb0408972cf9c27f6f742628c4',
            'fltt': 2,
            'invt': 2,
            'fid': 'f62',
            'fs': 'm:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23',  # 板块
            'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152'
        }

        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        sectors = []
        for item in data['data']['diff']:
            sectors.append({
                'code': item['f12'],
                'name': item['f14'],
                'change': item['f3'] / 100,  # 涨跌幅
                'amount': item['f5'] / 10000,  # 成交额（万）
                'pe': item['f116'] / 100 if 'f116' in item else None,
            })

        return sectors
```

---

### 模块 2: 个股数据采集 (StockCollector)

**功能：**
- 获取板块内所有个股数据
- 按涨幅排序取前 N 只
- 提取K线数据用于首板判断

```python
class StockCollector:
    """个股数据采集器"""

    def get_top_stocks_in_sector(self, sector_code, top_n=10):
        """获取板块内涨幅前N的个股"""

        # 从东方财富获取板块个股
        url = "http://push2.eastmoney.com/api/qt/clist/get"
        params = {
            'pn': 1,
            'pz': top_n,
            'po': 1,
            'np': 1,
            'fltt': 2,
            'invt': 2,
            'fid': 'f3',
            'fs': f'b:{sector_code}',
            'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152,f117,f127'
        }

        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        stocks = []
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
                'market_cap': item['f116'] / 10000 if 'f116' in item else None,
            })

        return stocks

    def get_kline_data(self, stock_code, days=10):
        """获取K线数据（用于首板判断）"""
        # 从东方财富获取K线
        # TODO: 实现K线数据获取
        pass
```

---

### 模块 3: 首板公式引擎 (FirstBoardEngine)

**功能：**
- 将同花顺公式转换为 Python 逻辑
- 判断是否为首板
- 计算各项技术指标

```python
class FirstBoardEngine:
    """首板识别引擎"""

    def __init__(self):
        self.required_days = 5  # 需要至少5天数据

    def is_first_board(self, kline_data):
        """
        判断是否为首板

        参数：
            kline_data: K线数据列表，按时间倒序（最新的在前）
        """
        if len(kline_data) < self.required_days:
            return False, '数据不足'

        # 提取今日和过去数据
        today = kline_data[0]
        yesterday = kline_data[1]

        # 计算各项指标
        O = today['open']      # 开盘价
        C = today['close']     # 收盘价
        H = today['high']      # 最高价
        L = today['low']       # 最低价
        REF_C1 = yesterday['close']  # 昨日收盘

        # 计算涨跌幅
        涨幅 = (C - O) / O  # 实体涨幅
        涨幅2 = (C - REF_C1) / REF_C1  # 相对昨日涨幅
        冲 = (H - REF_C1) / REF_C1  # 冲高

        # 计算上下影线
        上影 = (H - max(O, C)) / max(O, C)
       上影 = (min(O, C) - L) / L

        # 计算实体
        实体 = (max(C, O) - min(C, O)) / min(C, O)

        # 判断一字板（特殊）
        一字板 = (上影 == 0) and (下影 == 0) and (涨幅 == 0)

        # 判断首板条件1
        # 冲>=0.08 AND 过去3天涨幅都<=0.085 AND 实体>=0.028 AND 涨幅2>=0.035
        首板1_冲 = 冲 >= 0.08

        # 过去3天涨幅都<=0.085
        过去3天涨幅 = [k['change'] for k in kline_data[1:4]]
        首板1_历史涨幅 = all(chg <= 0.085 for chg in 过去3天涨幅)

        首板1_实体 = 实体 >= 0.028
        首板1_涨幅2 = 涨幅2 >= 0.035

        首板1 = (首板1_冲 and 首板1_历史涨幅 and
                 首板1_实体 and 首板1_涨幅2)

        # 判断首板条件2
        # 冲>=0.08 AND 涨幅2>=0.09 AND 过去3天涨幅都<=0.087
        首板2_冲 = 冲 >= 0.08
        首板2_涨幅2 = 涨幅2 >= 0.09
        首板2_历史涨幅 = all(chg <= 0.087 for chg in 过去3天涨幅)

        首板2 = 首板2_冲 and 首板2_涨幅2 and 首板2_历史涨幅

        # 首板 = 首板1 OR 首板2
        # 且过去2天都不是首板
        首板3 = 首板1 or 首板2

        # 检查过去2天是否首板（避免连续）
        # TODO: 需要更长的历史数据来判断

        return 首板3, {
            '首板': 首板3,
            '涨幅2': 涨幅2,
            '冲': 冲,
            '实体': 实体,
            '上影': 上影,
            '下影': 下影,
            '一字板': 一字板,
        }
```

---

### 模块 4: 基本面与利好分析 (FundamentalAnalyzer)

**功能：**
- 公司基本面分析
- 重大公告识别
- 概念题材分析
- 业绩预告/财报解读

```python
class FundamentalAnalyzer:
    """基本面与利好分析器"""

    def analyze_company(self, stock_code):
        """分析公司基本面和利好消息"""

        result = {
            'score': 0,
            'reasons': [],
            'warnings': []
        }

        # 1. 获取公司基本信息
        company_info = self._get_company_info(stock_code)

        # 2. 重大利好新闻
        good_news = self._get_good_news(stock_code)

        # 3. 概念题材
        concepts = self._get_concepts(stock_code)

        # 4. 资金流向
        fund_flow = self._get_fund_flow(stock_code)

        # 5. 评级
        ratings = self._get_ratings(stock_code)

        # 综合评分
        if good_news:
            result['score'] += 30
            result['reasons'].append(f"利好新闻: {len(good_news)}条")

        if len(concepts) >= 3:
            result['score'] += 20
            result['reasons'].append(f"热门概念: {len(concepts)}个")

        if fund_flow['net_inflow'] > 0:
            result['score'] += 20
            result['reasons'].append("资金净流入")

        if ratings['buy_count'] >= 3:
            result['score'] += 15
            result['reasons'].append(f"机构看好: {ratings['buy_count']}家")

        # 风险检查
        if company_info.get('st_flag'):
            result['warnings'].append("ST股票，风险较高")
            result['score'] -= 30

        if company_info.get('high_pe', 0) > 100:
            result['warnings'].append("市盈率过高")
            result['score'] -= 10

        return result

    def _get_good_news(self, stock_code):
        """获取利好新闻"""
        # 从东方财富、新浪财经等获取
        # TODO: 实现新闻获取
        return []

    def _get_concepts(self, stock_code):
        """获取概念题材"""
        # TODO: 实现概念获取
        return []

    def _get_fund_flow(self, stock_code):
        """获取资金流向"""
        # TODO: 实现资金流向获取
        return {'net_inflow': 0}

    def _get_ratings(self, stock_code):
        """获取机构评级"""
        # TODO: 实现评级获取
        return {'buy_count': 0}
```

---

### 模块 5: 新闻舆情分析 (NewsSentiment)

**功能：**
- 抓取相关新闻
- 情感分析（利好/利空）
- 去重和重要性排序

```python
class NewsSentiment:
    """新闻舆情分析器"""

    def analyze_stock_news(self, stock_code):
        """分析股票相关新闻舆情"""

        # 新闻源
        sources = [
            self._get_eastmoney_news,
            self._get_sina_news,
            self._get_10jqka_news,
        ]

        all_news = []
        for source in sources:
            try:
                news = source(stock_code)
                all_news.extend(news)
            except Exception as e:
                print(f"新闻源错误: {e}")

        # 去重
        all_news = self._deduplicate(all_news)

        # 情感分析
        sentiment_result = self._analyze_sentiment(all_news)

        return sentiment_result

    def _analyze_sentiment(self, news_list):
        """情感分析"""
        positive_keywords = ['利好', '上涨', '突破', '增长', '盈利', '业绩', '合作', '收购']
        negative_keywords = ['利空', '下跌', '下滑', '亏损', '风险', '减持', '处罚']

        positive_count = 0
        negative_count = 0

        for news in news_list:
            title = news['title']
            for kw in positive_keywords:
                if kw in title:
                    positive_count += 1
                    break

            for kw in negative_keywords:
                if kw in title:
                    negative_count += 1
                    break

        return {
            'positive': positive_count,
            'negative': negative_count,
            'news_count': len(news_list),
            'top_news': news_list[:5]
        }
```

---

### 模块 6: 智能评分引擎 (IntelligentScoring)

**功能：**
- 综合多个维度打分
- 排序输出最终结果
- 提供选股报告

```python
class IntelligentScoring:
    """智能评分引擎"""

    def score_stock(self, stock_data, first_board_result, fundamental_result, news_sentiment):
        """
        综合评分

        评分维度：
        1. 首板质量（技术面） - 30分
        2. 基本面利好 - 30分
        3. 新闻舆情 - 20分
        4. 资金流向 - 15分
        5. 市场热度 - 5分
        """
        score = 0
        details = {}

        # 1. 首板质量（30分）
        if first_board_result['首板']:
            score += 30
            details['首板质量'] = f"✅ 符合 (冲:{first_board_result['冲']:.2%}, 实体:{first_board_result['实体']:.2%})"

        else:
            details['首板质量'] = "❌ 不符合"

        # 2. 基本面（30分）
        score += fundamental_result['score'] * 0.3
        details['基本面'] = fundamental_result

        # 3. 新闻舆情（20分）
        sentiment = news_sentiment
        if sentiment['news_count'] > 0:
            sentiment_score = min(20, sentiment['positive'] * 5)
            score += sentiment_score
            details['舆情'] = f"利好:{sentiment['positive']}, 利空:{sentiment['negative']}"

        else:
            details['舆情'] = "无明显新闻"

        # 4. 资金流向（15分）
        # TODO: 从 fundamental_result 获取

        # 5. 市场热度（5分）
        if stock_data['change'] >= 0.098:
            score += 5  # 接近涨停
        elif stock_data['change'] >= 0.05:
            score += 3

        return {
            'final_score': min(100, score),
            'details': details
        }
```

---

### 模块 7: 模拟交易引擎 (PaperTrading)

**功能：**
- 模拟买入
- 持仓管理
- 止损止盈
- 交易记录

```python
class PaperTrading:
    """模拟交易引擎"""

    def __init__(self, initial_capital=100000):
        self.capital = initial_capital  # 初始资金
        self.positions = []  # 持仓
        self.history = []  # 交易记录

    def buy(self, stock_code, price, amount=100):
        """模拟买入"""
        cost = price * amount

        if cost > self.capital:
            return False, '资金不足'

        self.capital -= cost
        self.positions.append({
            'code': stock_code,
            'amount': amount,
            'buy_price': price,
            'buy_time': datetime.now()
        })

        self.history.append({
            'action': 'BUY',
            'code': stock_code,
            'price': price,
            'amount': amount,
            'time': datetime.now()
        })

        return True, f'买入成功 {stock_code} @ {price}'

    def sell(self, stock_code, price, amount=None):
        """模拟卖出"""
        position = next((p for p in self.positions if p['code'] == stock_code), None)

        if not position:
            return False, '无持仓'

        sell_amount = amount or position['amount']
        revenue = price * sell_amount

        self.capital += revenue
        self.positions.remove(position)

        profit = (price - position['buy_price']) * sell_amount
        profit_rate = (price - position['buy_price']) / position['buy_price']

        self.history.append({
            'action': 'SELL',
            'code': stock_code,
            'price': price,
            'amount': sell_amount,
            'profit': profit,
            'profit_rate': profit_rate,
            'time': datetime.now()
        })

        return True, f'卖出成功 {stock_code} @ {price}, 盈利: {profit:.2f} ({profit_rate:.2%})'

    def get_portfolio_status(self):
        """获取账户状态"""
        total_value = self.capital
        for p in self.positions:
            # TODO: 获取当前市价
            current_price = p['buy_price']  # 假设
            total_value += current_price * p['amount']

        return {
            'capital': self.capital,
            'positions': len(self.positions),
            'total_value': total_value,
            'profit': total_value - 100000
        }
```

---

### 主控调度器 (MainScheduler)

```python
class MainScheduler:
    """主控调度器"""

    def __init__(self):
        self.sector_collector = SectorCollector()
        self.stock_collector = StockCollector()
        self.first_board_engine = FirstBoardEngine()
        self.fundamental_analyzer = FundamentalAnalyzer()
        self.news_sentiment = NewsSentiment()
        self.intelligent_scoring = IntelligentScoring()
        self.paper_trading = PaperTrading(initial_capital=100000)

    def run(self):
        """完整选股流程"""

        print("=" * 60)
        print("智能选股系统启动")
        print("=" * 60)

        # 1. 获取热门板块
        print("\n[1/6] 获取热门板块...")
        sectors = self.sector_collector.get_sectors(min_change=1.0)
        print(f"  找到 {len(sectors)} 个涨幅>1%的板块")
        for s in sectors[:5]:
            print(f"    - {s['name']}: {s['change']:.2%}")

        if not sectors:
            print("  ❌ 无符合条件板块")
            return

        # 2. 对每个板块选股
        all_candidates = []

        for sector in sectors[:3]:  # 取前3个最热板块
            print(f"\n[2/6] 分析板块: {sector['name']}")

            # 获取板块内涨幅前10的个股
            stocks = self.stock_collector.get_top_stocks_in_sector(
                sector['code'],
                top_n=10
            )

            print(f"  板块内前10涨幅股: {len(stocks)}只")

            for stock in stocks:
                print(f"    检查: {stock['name']} ({stock['code']}) 涨幅:{stock['change']:.2%}")

                # 获取K线数据
                kline_data = self.stock_collector.get_kline_data(stock['code'], days=10)

                # 判断首板
                is_first_board, fb_result = self.first_board_engine.is_first_board(kline_data)

                if not is_first_board:
                    continue

                # 基本面分析
                fundamental = self.fundamental_analyzer.analyze_company(stock['code'])

                # 新闻舆情
                sentiment = self.news.comsentiment.analyze_stock_news(stock['code'])

                # 综合评分
                score_result = self.intelligent_scoring.score_stock(
                    stock,
                    fb_result,
                    fundamental,
                    sentiment
                )

                candidate = {
                    **stock,
                    'first_board_result': fb_result,
                    'fundamental': fundamental,
                    'sentiment': sentiment,
                    'score': score_result['final_score'],
                    'score_details': score_result['details']
                }

                all_candidates.append(candidate)

                print(f"      ✅ 首板! 综合评分: {score_result['final_score']:.1f}")

        # 3. 排序输出
        print("\n[3/6] 综合评分排序...")
        all_candidates.sort(key=lambda x: x['score'], reverse=True)

        # 4. 输出结果
        print("\n[4/6] 选股结果 (Top 5):")
        for i, c in enumerate(all_candidates[:5], 1):
            print(f"\n  第{i}名: {c['name']} ({c['code']})")
            print(f"    涨幅: {c['change']:.2%} | 评分: {c['score']:.1f}")
            print(f"    基本面得分: {c['fundamental']['score']:.1f}")
            print(f"    理由: {c['fundamental']['reasons']}")

        # 5. 模拟买入
        print("\n[5/6] 模拟交易...")
        for c in all_candidates[:3]:  # 买入前3名
            result, msg = self.paper_trading.buy(
                c['code'],
                c['price']
            )
            print(f"  {msg}")

        # 6. 输出持仓
        print("\n[6/6] 当前持仓:")
        status = self.paper_trading.get_portfolio_status()
        print(f"  总资产: {status['total_value']:.2f}")
        print(f"  可用资金: {status['capital']:.2f}")
        print(f"  持仓数量: {status['positions']}")
        print(f"  总盈亏: {status['profit']:.2f}")

        print("\n" + "=" * 60)
        print("选股完成！")
        print("=" * 60)
```

---

## 部署与运行

### 安装依赖

```powershell
pip install requests pandas numpy
pip install beautifulsoup4 lxml
pip install pywinauto psutil Pillow
pip install pyautogui opencv-python
```

### 启动系统

```python
if __name__ == '__main__':
    scheduler = MainScheduler()

    # 实时监控模式
    while True:
        scheduler.run()

        # 每5分钟扫描一次
        time.sleep(300)
```

---

## 配置项

```python
# config.py
CONFIG = {
    # 选股参数
    'MIN_SECTOR_CHANGE': 0.01,  # 板块涨幅阈值
    'TOP_STOCKS_IN_SECTOR': 10,  # 板块内取前N只
    'TOP_SECTORS': 3,  # 分析前N个板块

    # 首板参数
    'MIN_CHONG': 0.08,  # 最小冲高幅度
    'MAX_HISTORY_CHANGE': 0.085,  # 历史涨幅阈值
    'MIN_ENTITY': 0.028,  # 最小实体
    'MIN_CHANGE2': 0.035,  # 最小涨幅2

    # 交易参数
    'INITIAL_CAPITAL': 100000,  # 初始资金
    'BUY_AMOUNT': 100,  # 每次买入股数（1手）
    'STOP_LOSS': 0.05,  # 止损-5%
    'STOP_PROFIT': 0.15,  # 止盈+15%

    # 运行参数
    'SCAN_INTERVAL': 300,  # 扫描间隔（秒）
}
```

---

## 下一步

需要我立即实现哪些模块？

1. ✅ 完整代码实现
2. ✅ 数据获取（板块、个股、K线）
3. ✅ 首板公式验证
4. ✅ 基本面新闻分析
5. ✅ 模拟交易功能

告诉我你的选择，我立即开始编写！
