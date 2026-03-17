# -*- coding: utf-8 -*-
"""
同花顺自选股添加 - 简化版
"""

import ctypes
import time
import subprocess

user32 = ctypes.windll.user32

def activate_window():
    """激活同花顺窗口"""
    result = subprocess.run(
        ['powershell', '-Command', '(Get-Process hexin).MainWindowHandle'],
        capture_output=True, text=True
    )
    hwnd = int(result.stdout.strip())
    if hwnd:
        user32.SetForegroundWindow(hwnd)
        time.sleep(0.3)
    return hwnd

def send_keys(keys):
    """发送按键序列"""
    for key in keys:
        if key == 'CTRL+F':
            user32.keybd_event(0x11, 0, 0, 0)  # Ctrl
            user32.keybd_event(0x46, 0, 0, 0)   # F
            time.sleep(0.05)
            user32.keybd_event(0x46, 0, 2, 0)
            user32.keybd_event(0x11, 0, 2, 0)
        elif key == 'ENTER':
            user32.keybd_event(0x0D, 0, 0, 0)
            time.sleep(0.05)
            user32.keybd_event(0x0D, 0, 2, 0)
        elif key == 'F4':
            user32.keybd_event(0x73, 0, 0, 0)
            time.sleep(0.05)
            user32.keybd_event(0x73, 0, 2, 0)
        else:
            # 普通字符
            vk = ord(key.upper())
            user32.keybd_event(vk, 0, 0, 0)
            time.sleep(0.05)
            user32.keybd_event(vk, 0, 2, 0)
        time.sleep(0.1)

def add_stock(code):
    """添加单只股票"""
    print(f"添加 {code}...")

    # 激活窗口
    hwnd = activate_window()
    if not hwnd:
        print("  ❌ 无法激活窗口")
        return False

    # Ctrl+F 打开搜索
    send_keys(['CTRL+F'])
    time.sleep(0.8)

    # 输入代码
    for c in code:
        send_keys([c])
    time.sleep(0.8)

    # 回车确认
    send_keys(['ENTER'])
    time.sleep(1.5)

    # F4 添加到自选
    send_keys(['F4'])
    time.sleep(0.5)

    print(f"  ✅ {code} 已添加")
    return True

def main():
    print("=" * 40)
    print("同花顺自选股添加")
    print("=" * 40)

    stocks = ["000890", "000596", "002384"]

    print(f"\n将添加 {len(stocks)} 只股票:")
    for s in stocks:
        print(f"  - {s}")

    print("\n⚠️ 请确保同花顺窗口可见...")
    time.sleep(2)

    for code in stocks:
        add_stock(code)
        time.sleep(1)

    print("\n" + "=" * 40)
    print("✅ 完成! 请按 F6 查看自选股")
    print("=" * 40)

if __name__ == '__main__':
    main()
