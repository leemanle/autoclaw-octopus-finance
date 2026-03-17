#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
东方财富金融数据查询工具
基于 eastmoney_financial_data skill
"""

import os
import json
import requests


class EastMoneyQuery:
    def __init__(self, api_key=None):
        """初始化东方财富查询工具

        Args:
            api_key: 东方财富API Key
        """
        self.api_key = api_key or os.getenv("EASTMONEY_APIKEY")
        self.url = "https://mkapi2.dfcfs.com/finskillshub/api/claw/query"

    def query(self, text):
        """查询金融数据

        Args:
            text: 查询文本，如"茅台最新价"、"A股今日涨跌"

        Returns:
            dict: 查询结果
        """
        if not self.api_key:
            return {"error": "请先设置EASTMONEY_APIKEY环境变量"}

        headers = {
            "Content-Type": "application/json",
            "apikey": self.api_key
        }

        data = {
            "toolQuery": text
        }

        try:
            response = requests.post(self.url, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def format_result(self, result):
        """格式化查询结果

        Args:
            result: 原始查询结果

        Returns:
            str: 格式化后的文本
        """
        if "error" in result:
            return f"❌ 错误: {result['error']}"

        try:
            data = result.get("data", {})
            data_list = data.get("dataTableDTOList", [])

            if not data_list:
                return "未找到相关数据"

            output = []
            for item in data_list:
                name = item.get("entityName", "未知")
                title = item.get("title", "")

                table = item.get("table", {})
                name_map = item.get("nameMap", {})

                # 解析表格数据
                rows = []
                for col_key, col_values in table.items():
                    col_name = name_map.get(col_key, col_key)
                    if isinstance(col_values, list) and col_values:
                        value = col_values[0]
                        rows.append(f"  {col_name}: {value}")

                if rows:
                    output.append(f"📊 {name}")
                    output.append("\n".join(rows))
                    output.append("")

            return "\n".join(output)

        except Exception as e:
            return f"解析结果失败: {e}"


def main():
    """主函数"""
    print("🦞 东方财富金融数据查询工具")
    print("="*50)

    # 检查API Key
    api_key = os.getenv("EASTMONEY_APIKEY")
    if not api_key:
        print("❌ 未设置 EASTMONEY_APIKEY")
        print("\n请先获取API Key:")
        print("1. 访问 https://marketing.dfcfs.com/views/finskillshub/indexuNdYscEA")
        print("2. 获取API Key")
        print("3. 设置环境变量: set EASTMONEY_APIKEY=你的Key")
        return

    print(f"✓ API Key已设置")

    # 创建查询工具
    query = EastMoneyQuery(api_key)

    # 示例查询
    examples = [
        "茅台最新价",
        "A股今日涨停数",
        "上证指数最新点位",
    ]

    print("\n📋 示例查询:")
    for i, q in enumerate(examples, 1):
        print(f"{i}. {q}")

    print("\n" + "="*50)
    print("输入查询内容（或按Ctrl+C退出）:")

    while True:
        try:
            text = input("\n> ").strip()
            if not text:
                continue

            print("🔍 查询中...")
            result = query.query(text)
            formatted = query.format_result(result)
            print(formatted)

        except KeyboardInterrupt:
            print("\n👋 再见!")
            break
        except Exception as e:
            print(f"❌ 错误: {e}")


if __name__ == "__main__":
    main()
