# -*- coding: utf-8 -*-
"""
同花顺自选股管理
"""

import os
import subprocess
import time
from datetime import datetime


class TushareFavorites:
    """同花顺自选股管理"""

    def __init__(self):
        # 查找同花顺安装路径
        self.ths_path = self.find_ths_path()
        self.favorites_file = self.find_favorites_file()

    def find_ths_path(self):
        """查找同花顺安装路径"""
        possible_paths = [
            r"C:\new_tdx\同花顺.exe",
            r"D:\new_tdx\同花顺.exe",
            r"C:\Program Files\同花顺\同花顺.exe",
            r"D:\Program Files\同花顺\同花顺.exe",
            r"C:\同花顺\同花顺.exe",
            r"D:\同花顺\同花顺.exe",
        ]

        for path in possible_paths:
            if os.path.exists(path):
                print(f"✅ 找到同花顺: {path}")
                return path

        print("❌ 未找到同花顺安装路径")
        return None

    def find_favorites_file(self):
        """查找自选股文件"""
        # 同花顺自选股文件通常在 C:\new_tdx\ 或用户目录下
        possible_paths = [
            r"C:\new_tdx\zxg.dat",
            r"C:\new_tdx\ zxg.dat",
            r"C:\new_tdx\blocknew\zxg.blk",
            r"C:\new_tdx\blocknew\zxg.dat",
        ]

        for path in possible_paths:
            if os.path.exists(path):
                print(f"✅ 找到自选股文件: {path}")
                return path

        # 尝试在用户目录查找
        import winreg
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\同花顺")
            install_path, _ = winreg.QueryValueEx(key, "InstallPath")
            zxg_path = os.path.join(install_path, "zxg.dat")

            if os.path.exists(zxg_path):
                print(f"✅ 找到自选股文件: {zxg_path}")
                return zxg_path
        except:
            pass

        return None

    def launch_ths(self):
        """启动同花顺"""
        if not self.ths_path:
            print("❌ 未找到同花顺，请手动启动")
            return False

        try:
            # 检查是否已运行
            process = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE)
            output = process.communicate()[0].decode('gbk', errors='ignore')

            if '同花顺.exe' in output:
                print("✅ 同花顺已经在运行")
                return True

            # 启动同花顺
            print(f"🚀 正在启动同花顺...")
            subprocess.Popen([self.ths_path])
            time.sleep(5)  # 等待启动
            print("✅ 同花顺启动成功")
            return True

        except Exception as e:
            print(f"❌ 启动同花顺失败: {e}")
            return False

    def add_to_favorites(self, stock_codes):
        """
        添加股票到自选股

        参数：
            stock_codes: 股票代码列表 ['000890', '000596', ...]
        """
        if not stock_codes:
            print("❌ 股票列表为空")
            return False

        print(f"\n📝 准备添加 {len(stock_codes)} 只股票到自选股:")
        for code in stock_codes:
            print(f"  - {code}")

        # 方法1: 通过文件操作（直接修改自选股文件）
        if self.add_by_file(stock_codes):
            print("✅ 已通过文件方式添加到自选股")
            return True

        # 方法2: 通过UI自动化（使用pywinauto）
        elif self.add_by_ui(stock_codes):
            print("✅ 已通过UI方式添加到自选股")
            return True

        else:
            print("❌ 添加失败")
            return False

    def add_by_file(self, stock_codes):
        """通过文件操作添加自选股"""
        try:
            if not self.favorites_file:
                # 尝试创建默认路径
                self.favorites_file = r"C:\new_tdx\zxg.dat"
                print(f"⚠️  使用默认路径: {self.favorites_file}")

            # 同花顺自选股文件格式
            # 创建新文件内容
            lines = []
            lines.append("#自选股")
            lines.append(f"#添加时间:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            for code in stock_codes:
                # 同花顺格式: 6位代码,0
                lines.append(f"{code},0")

            # 写入文件
            dir_path = os.path.dirname(self.favorites_file)
            if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path)

            with open(self.favorites_file, 'w', encoding='gbk') as f:
                f.write('\n'.join(lines))

            print(f"✅ 已写入自选股文件: {self.favorites_file}")
            return True

        except Exception as e:
            print(f"❌ 文件操作失败: {e}")
            return False

    def add_by_ui(self, stock_codes):
        """通过UI自动化添加"""
        try:
            # 尝试导入pywinauto
            import pywinauto
            from pywinauto import application
            from pywinauto.keyboard import send_keys

            print("🔧 使用pywinauto控制同花顺...")

            # 启动同花顺
            self.launch_ths()

            # 连接到同花顺窗口
            app = application.Application().connect(path="同花顺.exe")
            main_window = app.window(title_re=".*同花顺.*")

            if not main_window.exists():
                print("❌ 未找到同花顺窗口")
                return False

            main_window.set_focus()

            # 对每只股票添加到自选股
            for code in stock_codes:
                print(f"  添加 {code}...")

                # 方法1: 搜索栏搜索
                # Ctrl+F 打开搜索
                send_keys('^f')
                time.sleep(0.5)

                # 输入股票代码
                send_keys(code)
                time.sleep(0.5)

                # Enter 选中
                send_keys('{ENTER}')
                time.sleep(0.5)

                # 右键菜单或 F4 添加自选股
                send_keys('{F4}')  # F4通常用于添加自选股
                time.sleep(0.5)

                print(f"    ✅ {code} 已添加")

            return True

        except ImportError:
            print("⚠️  pywinauto未安装，尝试pip install pywinauto")
            return False
        except Exception as e:
            print(f"❌ UI操作失败: {e}")
            return False


def main():
    """主函数"""
    print("=" * 60)
    print("📊 同花顺自选股管理")
    print("=" * 60)

    # 刚才选出的3只股票
    selected_stocks = [
        '000890',  # 法尔胜
        '000596',  # 古井贡酒
        '002384',  # 东山精密
    ]

    # 创建管理器
    manager = TushareFavorites()

    # 添加到自选股
    success = manager.add_to_favorites(selected_stocks)

    if success:
        print("\n✅ 操作完成！")
        print("💡 提示: 请在同花顺中刷新自选股列表")
    else:
        print("\n❌ 操作失败，请手动添加")
        print("💡 手动添加:")
        for code in selected_stocks:
            print(f"   - {code}")


if __name__ == '__main__':
    main()
