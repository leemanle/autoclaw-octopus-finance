# -*- coding: utf-8 -*-
"""
通过键盘自动化添加股票到同花顺自选股
"""

import subprocess
import time
import os


def add_stock_to_favorites(stock_code, stock_name=""):
    """添加单只股票到自选股"""

    print(f"正在添加: {stock_code} {stock_name}")

    # 方法1: 使用 pywinauto
    try:
        from pywinauto import application
        from pywinauto.keyboard import send_keys

        # 连接到同花顺
        app = application.Application().connect(process=16076)
        main_window = app.window(title_re=".*同花顺.*")

        if main_window.exists():
            main_window.set_focus()

            # 打开搜索 (Ctrl+F)
            send_keys('^f')
            time.sleep(0.5)

            # 输入股票代码
            send_keys(stock_code)
            time.sleep(0.5)

            # 回车确认
            send_keys('{ENTER}')
            time.sleep(0.5)

            # 添加到自选股 (F4)
            send_keys('{F4}')
            time.sleep(0.3)

            print(f"  ✅ 已添加 {stock_code}")
            return True

    except Exception as e:
        print(f"  ⚠️ pywinauto方法失败: {e}")

    # 方法2: 使用 Windows API 直接发送按键
    try:
        import ctypes
        from ctypes import wintypes

        user32 = ctypes.windll.user32

        # 查找同花顺窗口
        hwnd = user32.FindWindowW(None, "同花顺")
        if not hwnd:
            hwnd = user32.FindWindowW(None, "同花顺 - 自选股")
        if not hwnd:
            hwnd = user32.FindWindowW(None, "网上股票交易分析系统")

        if hwnd:
            print(f"  找到窗口句柄: {hwnd}")

            # 激活窗口
            user32.SetForegroundWindow(hwnd)
            time.sleep(0.3)

            # 发送 Ctrl+F
            user32.keybd_event(0x11, 0, 0, 0)  # Ctrl down
            user32.keybd_event(0x46, 0, 0, 0)  # F down
            user32.keybd_event(0x46, 0, 2, 0)  # F up
            user32.keybd_event(0x11, 0, 2, 0)  # Ctrl up
            time.sleep(0.5)

            # 输入股票代码
            for char in stock_code:
                vk = ord(char)
                user32.keybd_event(vk, 0, 0, 0)
                user32.keybd_event(vk, 0, 2, 0)
                time.sleep(0.05)
            time.sleep(0.3)

            # 回车
            user32.keybd_event(0x0D, 0, 0, 0)  # Enter down
            user32.keybd_event(0x0D, 0, 2, 0)  # Enter up
            time.sleep(0.5)

            # F4 添加到自选股
            user32.keybd_event(0x73, 0, 0, 0)  # F4 down
            user32.keybd_event(0x73, 0, 2, 0)  # F4 up

            print(f"  ✅ 已添加 {stock_code}")
            return True

    except Exception as e:
        print(f"  ⚠️ Windows API方法失败: {e}")

    return False


def main():
    """主函数"""

    print("=" * 50)
    print("同花顺自选股添加工具")
    print("=" * 50)

    # 要添加的股票列表
    stocks = [
        ("000890", "法尔胜"),
        ("000596", "古井贡酒"),
        ("002384", "东山精密"),
    ]

    # 确保同花顺在运行
    print("\n检查同花顺进程...")
    try:
        result = subprocess.run(
            ['tasklist'],
            capture_output=True,
            text=True,
            encoding='gbk',
            errors='ignore'
        )
        if 'hexin.exe' in result.stdout:
            print("✅ 同花顺正在运行")
        else:
            print("❌ 同花顺未运行，正在启动...")
            subprocess.Popen([r'D:\同花顺主本\hexinlauncher.exe'])
            time.sleep(5)
    except:
        pass

    print("\n开始添加股票到自选股...")

    for code, name in stocks:
        add_stock_to_favorites(code, name)
        time.sleep(1)  # 每次操作间隔

    print("\n" + "=" * 50)
    print("✅ 操作完成!")
    print("请在同花顺中按 F6 查看自选股")
    print("=" * 50)


if __name__ == '__main__':
    main()
