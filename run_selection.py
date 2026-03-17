# -*- coding: utf-8 -*-
"""
选股系统启动脚本
"""

from main_scheduler import MainScheduler
from trading_config import CONFIG



def main():
    """主函数"""
    # 创建调度器
    scheduler = MainScheduler()

    # 运行一次选股
    results = scheduler.run()

    # 如果有选股结果，保存简版报告
    if results:
        print("\n" + "=" * 70)
        print("📋 选股报告")
        print("=" * 70)

        for i, c in enumerate(results[:5], 1):
            print(f"\n{i}. {c['name']} ({c['code']})")
            print(f"   板块: {c['sector_name']}")
            print(f"   价格: {c['price']:.2f} | 涨幅: {c['change']:.2%} | 评分: {c['score']:.1f}")
            print(f"   冲高: {c['first_board_result']['冲']:.2%} | 实体: {c['first_board_result']['实体']:.2%}")

    return results


if __name__ == '__main__':
    import time

    # 单次运行
    main()

    # 持续监控模式（如果需要）
    """
    print(f"\n⏰ 开启持续监控模式，每{CONFIG['SCAN_INTERVAL']}秒扫描一次...")
    print("按 Ctrl+C 停止\n")

    try:
        while True:
            main()

            print(f"\n⏰ 下次扫描: {CONFIG['SCAN_INTERVAL']}秒后...")
            time.sleep(CONFIG['SCAN_INTERVAL'])

    except KeyboardInterrupt:
        print("\n\n👋 监控已停止")
    """
