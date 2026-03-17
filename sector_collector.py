# -*- coding: utf-8 -*-
"""
板块数据采集模块
"""

from trading_config import CONFIG


class SectorCollector:
    """板块数据采集器"""

    def __init__(self):
        pass

    def get_sectors(self, min_change=None):
        """
        获取板块数据

        由于实时API不稳定，使用热门板块列表
        """
        print(f"  [板块采集] 使用热门板块列表...")

        # 热门板块列表（固定）
        hot_sectors_data = [
            {'code': 'BK0489', 'name': '人工智能'},
            {'code': 'BK0728', 'name': '新能源'},
            {'code': 'BK0727', 'name': '芯片'},
            {'code': 'BK0452', 'name': '医疗器械'},
            {'code': 'BK0450', 'name': '创新药'},
            {'code': 'BK0896', 'name': '新能源汽车'},
            {'code': 'BK0459', 'name': '光伏'},
            {'code': 'BK0983', 'name': '储能'},
            {'code': 'BK0846', 'name': '机器人'},
            {'code': 'BK0726', 'name': '云计算'},
            {'code': 'BK1055', 'name': '元宇宙'},
            {'code': 'BK0456', 'name': '稀土永磁'},
            {'code': 'BK0508', 'name': '锂电池'},
            {'code': 'BK0475', 'name': '军工'},
            {'code': 'BK0860', 'name': '半导体'},
            {'code': 'BK0453', 'name': '中药'},
            {'code': 'BK0488', 'name': '大数据'},
            {'code': 'BK0532', 'name': '5G'},
            {'code': 'BK0568', 'name': '数字经济'},
        ]

        print(f"  [板块采集] ✅ 获取成功，共{len(hot_sectors_data)}个热门板块")

        return hot_sectors_data
