# -*- coding: utf-8 -*-
"""
使用 Windows API 直接操作同花顺
"""

import ctypes
import time
import subprocess
from ctypes import wintypes

# 加载 user32.dll
user32 = ctypes.windll.user32

# 定义虚拟键码
VK_CONTROL = 0x11
VK_F = 0x46
VK_RETURN = 0x0D
VK_F4 = 0x73

# 定义函数
keybd_event = user32.keybd_event
FindWindowW = user32.FindWindowW
SetForegroundWindow = user32.SetForegroundWindow
GetForegroundWindow = user32.GetForegroundWindow
IsWindowVisible = user32.IsWindowVisible


def find_ths_window():
    """查找同花顺窗口"""
    # 尝试多个可能的窗口标题
    titles = [
        "同花顺(9.50.50) - A股技术分析",
        "同花顺",
        "同花顺 - 自选股",
        "网上股票交易分析系统",
        "同花顺主力版",
    ]

    for title in titles:
        hwnd = FindWindowW(None, title)
        if hwnd:
            print(f"找到窗口: {title} (hwnd={hwnd})")
            return hwnd

    return None


def send_key_to_window(hwnd, vk_code, with_ctrl=False, with_shift=False):
    """发送按键到指定窗口"""

    if not hwnd:
        print("  ❌ 窗口句柄无效")
        return False

    try:
        # 激活窗口
        SetForegroundWindow(hwnd)
        time.sleep(0.2)

        # 如果需要 Ctrl
        if with_ctrl:
            keybd_event(VK_CONTROL, 0, 0, 0)
            time.sleep(0.05)

        # 如果需要 Shift
        if with_shift:
            user32.keybd_event(0x10, 0, 0, 0)  # VK_SHIFT
            time.sleep(0.05)

        # 按下按键
        keybd_event(vk_code, 0, 0, 0)
        time.sleep(0.05)
        keybd_event(vk_code, 0, 2, 0)  # 松开
        time.sleep(0.05)

        # 松开 Shift
        if with_shift:
            user32.keybd_event(0x10, 0, 2, 0)
            time.sleep(0.05)

        # 松开 Ctrl
        if with_ctrl:
            keybd_event(VK_CONTROL, 0, 2, 0)
            time.sleep(0.05)

        return True

    except Exception as e:
        print(f"  ❌ 发送按键失败: {e}")
        return False


def type_text(text):
    """输入文本"""
    for char in text.upper():
        vk = ord(char)
        # 处理数字
        if char.isdigit():
            vk = 0x30 + int(char)

        keybd_event(vk, 0, 0, 0)
        time.sleep(0.03)
        keybd_event(vk, 0, 2, 0)
        time.sleep(0.03)


def add_stock(stock_code):
    """添加股票到自选股"""

    print(f"  添加 {stock_code}...")

    # 每次都重新查找窗口
    time.sleep(0.5)
    hwnd = find_ths_window()
    if not hwnd:
        print(f"    ❌ 找不到同花顺窗口")
        return False

    try:
        # 1. 打开搜索 (Ctrl+F)
        print(f"    步骤1: 打开搜索...")
        send_key_to_window(hwnd, VK_F, with_ctrl=True)
        time.sleep(0.8)

        # 2. 输入股票代码
        print(f"    步骤2: 输入代码 {stock_code}...")
        type_text(stock_code)
        time.sleep(0.8)

        # 3. 回车确认
        print(f"    步骤3: 确认...")
        send_key_to_window(hwnd, VK_RETURN)
        time.sleep(1.5)

        # 4. 添加到自选股 (F4)
        print(f"    步骤4: 添加到自选股...")
        send_key_to_window(hwnd, VK_F4)
        time.sleep(0.5)

        print(f"    ✅ {stock_code} 已添加")
        return True

    except Exception as e:
        print(f"    ❌ 添加失败: {e}")
        return False


def main():
    print("=" * 50)
    print("同花顺自选股添加工具 (Windows API版)")
    print("=" * 50)

    # 股票列表
    stocks = [
        ("000890", "法尔胜"),
        ("000596", "古井贡酒"),
        ("002384", "东山精密"),
    ]

    # 检查同花顺进程
    print("\n检查同花顺...")
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
            print("❌ 同花顺未运行")
            return
    except Exception as e:
        print(f"检查失败: {e}")

    print("\n开始添加股票...")
    print("⚠️ 请确保同花顺窗口可见且在最前面\n")

    for code, name in stocks:
        add_stock(code)
        time.sleep(1.5)  # 每次操作间隔

    print("\n" + "=" * 50)
    print("✅ 操作完成!")
    print("请在同花顺中按 F6 查看自选股")
    print("=" * 50)


if __name__ == '__main__':
    main()
