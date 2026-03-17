#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
删除飞书作废的应用
使用Selenium自动控制Chrome浏览器
"""

import time
import sys
import os

# 添加workspace目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chrome_controller import ChromeController
from selenium.webdriver.common.by import By


class FeishuAppDeleter:
    def __init__(self):
        """初始化删除器"""
        self.controller = ChromeController()
        self.deleted_apps = []
        self.failed_apps = []

    def login_and_delete(self):
        """登录飞书开放平台并删除作废的应用"""
        try:
            # 1. 打开飞书开放平台
            print("\n🚀 步骤1: 打开飞书开放平台")
            self.controller.start()
            self.controller.open("https://open.feishu.cn/")
            self.controller.wait(3)

            # 截图
            screenshot_path = r"C:\Users\Administrator\.openclaw-autoclaw\workspace\feishu_screenshots"
            os.makedirs(screenshot_path, exist_ok=True)
            self.controller.screenshot(f"{screenshot_path}\\step1_open_platform.png")

            print("\n⚠️  请手动完成以下操作:")
            print("1. 如果未登录，请登录你的飞书账号")
            print("2. 找到'我的应用'或'管理应用'页面")
            print("3. 告诉我'继续'，我将开始删除应用")

            # 等待用户确认
            input("\n按回车键继续...")

            # 2. 获取所有应用列表
            print("\n🚀 步骤2: 获取应用列表")
            self.controller.screenshot(f"{screenshot_path}\\step2_apps_list.png")

            # 3. 删除作废的应用
            print("\n🚀 步骤3: 删除作废的应用")
            print("⚠️  注意: 我将删除所有看起来像作废的应用")
            print("   应用名称包含: test, 测试, temp, 临时, demo 等关键词")

            confirm = input("\n确认删除? (yes/no): ")
            if confirm.lower() != 'yes':
                print("❌ 已取消删除操作")
                return

            # 这里需要根据实际页面结构来选择和删除应用
            # 由于页面结构可能变化，这里提供通用方法

            # 查找应用列表中的所有应用
            # 这个选择器需要根据实际页面调整
            apps = self.controller.driver.find_elements(By.CSS_SELECTOR, "[data-testid^='app-card'], .app-card, .app-item")

            print(f"\n找到 {len(apps)} 个应用")

            for i, app in enumerate(apps):
                try:
                    # 获取应用名称
                    app_name = app.text
                    print(f"\n应用 {i+1}: {app_name}")

                    # 判断是否需要删除
                    if self.is_obsolete(app_name):
                        print(f"  → 删除应用: {app_name}")

                        # 找到删除按钮（需要根据实际页面调整）
                        delete_buttons = app.find_elements(By.XPATH, ".//button[contains(text(), '删除') or contains(text(), 'Delete') or contains(@aria-label, '删除')]")
                        if not delete_buttons:
                            # 尝试其他选择器
                            delete_buttons = app.find_elements(By.CSS_SELECTOR, "[role='menuitem']:last-child, .delete-btn, .remove-btn")

                        if delete_buttons:
                            delete_buttons[0].click()
                            time.sleep(1)

                            # 确认删除
                            confirm_buttons = self.controller.driver.find_elements(By.XPATH, "//button[contains(text(), '确认') or contains(text(), 'Confirm') or contains(text(), '确定')]")
                            if confirm_buttons:
                                confirm_buttons[0].click()
                                time.sleep(2)

                                self.deleted_apps.append(app_name)
                                print(f"  ✓ 已删除: {app_name}")
                            else:
                                print(f"  ✗ 删除失败: 找不到确认按钮")
                                self.failed_apps.append(app_name)
                        else:
                            print(f"  ✗ 删除失败: 找不到删除按钮")
                            self.failed_apps.append(app_name)
                    else:
                        print(f"  → 保留: {app_name}")

                    # 截图
                    self.controller.screenshot(f"{screenshot_path}\\delete_step_{i+1}.png")

                except Exception as e:
                    print(f"  ✗ 处理应用失败: {e}")
                    self.failed_apps.append(f"Unknown (error: {e})")

            # 4. 总结
            print("\n" + "="*50)
            print("删除完成!")
            print("="*50)
            print(f"✓ 成功删除: {len(self.deleted_apps)} 个应用")
            print(f"✗ 删除失败: {len(self.failed_apps)} 个应用")

            if self.deleted_apps:
                print("\n已删除的应用:")
                for app in self.deleted_apps:
                    print(f"  - {app}")

            if self.failed_apps:
                print("\n删除失败的应用:")
                for app in self.failed_apps:
                    print(f"  - {app}")

            # 最终截图
            self.controller.screenshot(f"{screenshot_path}\\final_result.png")

            # 保持浏览器打开10秒，供用户检查
            print("\n浏览器将保持打开10秒，请检查结果...")
            time.sleep(10)

        except Exception as e:
            print(f"\n❌ 错误: {e}")
            import traceback
            traceback.print_exc()

        finally:
            self.controller.close()

    def is_obsolete(self, app_name):
        """判断应用是否作废

        Args:
            app_name: 应用名称

        Returns:
            bool: 是否作废
        """
        if not app_name:
            return False

        # 作废的关键词
        obsolete_keywords = [
            'test', '测试', 'temp', '临时', 'demo', '演示',
            'sample', '样例', 'debug', '调试', 'old', '旧',
            '废弃', 'deprecated', 'unused', '未使用'
        ]

        app_name_lower = app_name.lower()

        # 检查是否包含作废关键词
        for keyword in obsolete_keywords:
            if keyword in app_name_lower:
                return True

        return False

    def delete_specific_apps(self, app_names):
        """删除指定的应用

        Args:
            app_names: 要删除的应用名称列表
        """
        print(f"将删除以下应用: {app_names}")
        # 这里可以扩展为精确删除指定的应用
        pass


def main():
    """主函数"""
    print("🦞 飞书应用删除工具")
    print("="*50)

    deleter = FeishuAppDeleter()
    deleter.login_and_delete()


if __name__ == "__main__":
    main()
