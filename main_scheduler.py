# -*- coding: utf-8 -*-
"""
主控调度器
"""

import time
import json
from datetime import datetime
from trading_config import CONFIG

# 导入各模块
from sector_collector import SectorCollector
from stock_collector import StockCollector
from first_board_engine import FirstBoardEngine
from fundamental_analyzer import FundamentalAnalyzer
from intelligent_scoring import IntelligentScoring


class MainScheduler:
    """主控调度器"""

    def __init__(self):
        self.sector_collector = SectorCollector()
        self.stock_collector = StockCollector()
        self.first_board_engine = FirstBoardEngine()
        self.fundamental_analyzer = FundamentalAnalyzer()
        self.intelligent_scoring = IntelligentScoring()

        # 选股结果存储
        self.all_candidates = []

    def run(self):
        """完整选股流程"""

        print("=" * 70)
        print("🚀 智能选股系统启动")
        print("=" * 70)
        print(f"⏰ 开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        # 1. 获取热门板块
        print("=" * 70)
        print("[步骤 1/5] 获取热门板块")
        print("=" * 70)

        sectors = self.sector_collector.get_sectors(min_change=CONFIG['MIN_SECTOR_CHANGE'])

        if not sectors:
            print("\n❌ 无符合条件的板块，选股结束")
            return []

        print(f"\n✅ 找到 {len(sectors)} 个热门板块\n")

        print(f"{'排名':<4} {'板块名称':<12} {'板块代码':<10}")
        print("-" * 70)
        for i, s in enumerate(sectors[:10], 1):
            print(f"{i:<4} {s['name']:<12} {s['code']:<10}")

        # 2. 分析板块内个股
        print("\n" + "=" * 70)
        print("[步骤 2/5] 分析板块内个股")
        print("=" * 70)

        top_sectors = sectors[:CONFIG['TOP_SECTORS']]
        print(f"\n重点分析前 {len(top_sectors)} 个最热板块:\n")

        all_candidates = []

        for idx, sector in enumerate(top_sectors, 1):
            print(f"\n📊 [{idx}/{len(top_sectors)}] 板块: {sector['name']} ({sector['code']})")
            print("-" * 70)

            # 获取板块内涨幅前N的个股
            stocks = self.stock_collector.get_top_stocks_in_sector(
                sector['code'],
                top_n=CONFIG['TOP_STOCKS_IN_SECTOR']
            )

            if not stocks:
                print("  ❌ 未获取到个股数据")
                continue

            print(f"  板块内涨幅前{CONFIG['TOP_STOCKS_IN_SECTOR']}个股: {len(stocks)}只\n")

            # 检查每只股票
            for stock in stocks:
                stock_name = stock['name']
                stock_code = stock['code']
                stock_change = stock['change']

                print(f"  🔍 检查: {stock_name} ({stock_code}) 涨幅:{stock_change:.2%}")

                # 获取K线数据
                kline_data = self.stock_collector.get_kline_data(stock_code, days=10)

                if len(kline_data) < 5:
                    print(f"      ⚠️  K线数据不足，跳过")
                    continue

                # 判断首板
                is_first_board, fb_result = self.first_board_engine.is_first_board(kline_data)

                if not is_first_board:
                    print(f"      ❌ 非首板")
                    continue

                print(f"      ✅ 首板！冲:{fb_result['冲']:.2%}, 实体:{fb_result['实体']:.2%}")

                # 基本面分析
                print(f"      📋 基本面分析...")
                fundamental = self.fundamental_analyzer.analyze_company(stock_code)

                # 综合评分
                score_result = self.intelligent_scoring.score_stock(
                    stock,
                    fb_result,
                    fundamental
                )

                candidate = {
                    **stock,
                    'sector_name': sector['name'],
                    'sector_code': sector['code'],
                    'first_board_result': fb_result,
                    'fundamental': fundamental,
                    'score': score_result['final_score'],
                    'score_details': score_result['details']
                }

                all_candidates.append(candidate)

                print(f"      📊 综合评分: {score_result['final_score']:.1f}/100")

        # 3. 排序输出结果
        print("\n" + "=" * 70)
        print("[步骤 3/5] 综合评分排序")
        print("=" * 70)

        all_candidates.sort(key=lambda x: x['score'], reverse=True)

        print(f"\n✅ 共选出 {len(all_candidates)} 只首板股\n")

        # 4. 输出详细结果
        print("=" * 70)
        print("[步骤 4/5] 选股结果详情")
        print("=" * 70)

        if not all_candidates:
            print("\n❌ 未选出符合条件的股票\n")
            return []

        print(f"\n🏆 Top {min(10, len(all_candidates))} 选股结果:\n")
        print(f"{'排名':<4} {'股票名称':<12} {'代码':<10} {'涨幅':<8} {'评分':<8} {'板块':<12}")
        print("-" * 70)

        for i, c in enumerate(all_candidates[:10], 1):
            print(f"{i:<4} {c['name']:<12} {c['code']:<10} {c['change']:>6.2%} {c['score']:>6.1f} {c['sector_name']:<12}")

        # 详细分析前5名
        print("\n" + "=" * 70)
        print("Top 5 详细分析")
        print("=" * 70)

        for i, c in enumerate(all_candidates[:5], 1):
            print(f"\n🥇 第{i}名: {c['name']} ({c['code']})")
            print(f"  所属板块: {c['sector_name']} ({c['sector_code']})")
            print(f"  当前价格: {c['price']:.2f}")
            print(f"  涨跌幅: {c['change']:.2%}")
            print(f"  综合评分: {c['score']:.1f}/100")

            # 首板详情
            fb = c['first_board_result']
            print(f"\n  📈 首板分析:")
            print(f"    冲高: {fb['冲']:.2%}")
            print(f"    实体: {fb['实体']:.2%}")
            print(f"    上影: {fb['上影']:.2%}")
            print(f"    下影: {fb['下影']:.2%}")

            # 基本面
            fund = c['fundamental']
            print(f"\n  📋 基本面 (得分: {fund['score']:.1f}):")
            if fund['reasons']:
                for reason in fund['reasons']:
                    print(f"    ✅ {reason}")
            if fund['warnings']:
                for warning in fund['warnings']:
                    print(f"    ⚠️  {warning}")

            # 评分详情
            details = c['score_details']
            print(f"\n  🎯 评分详情:")
            for key, value in details.items():
                if key != '基本面':
                    if isinstance(value, str):
                        print(f"    {key}: {value}")

        # 5. 保存结果
        print("\n" + "=" * 70)
        print("[步骤 5/5] 保存选股结果")
        print("=" * 70)

        self.save_results(all_candidates)

        print("\n" + "=" * 70)
        print("✅ 选股完成！")
        print("=" * 70)
        print(f"⏰ 完成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📊 选出股票: {len(all_candidates)}只")

        return all_candidates

    def save_results(self, candidates):
        """保存选股结果"""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"selection_result_{timestamp}.json"

            # 准备保存的数据（简化，避免循环引用）
            save_data = []
            for c in candidates:
                save_data.append({
                    'rank': candidates.index(c) + 1,
                    'code': c['code'],
                    'name': c['name'],
                    'price': c['price'],
                    'change': c['change'],
                    'sector': c['sector_name'],
                    'score': c['score'],
                    'first_board': c['first_board_result'].get('首板', False),
                    'fundamental_score': c['fundamental'].get('score', 0),
                })

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, ensure_ascii=False, indent=2)

            print(f"\n✅ 结果已保存到: {filename}")

        except Exception as e:
            print(f"\n⚠️  保存失败: {e}")


if __name__ == '__main__':
    # 创建调度器
    scheduler = MainScheduler()

    # 运行一次选股
    results = scheduler.run()

    # 可选：持续监控模式
    """
    while True:
        print(f"\n⏰ 下次扫描: {CONFIG['SCAN_INTERVAL']}秒后...")
        time.sleep(CONFIG['SCAN_INTERVAL'])
        scheduler.run()
    """
