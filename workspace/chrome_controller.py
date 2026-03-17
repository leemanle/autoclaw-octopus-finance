#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用Selenium控制Chrome浏览器
不依赖扩展，直接控制
"""

import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class ChromeController:
    def __init__(self, headless=False):
        """初始化Chrome控制器

        Args:
            headless: 是否无头模式
        """
        self.driver = None
        self.headless = headless

    def start(self):
        """启动Chrome浏览器"""
        options = Options()

        # 设置Chrome浏览器路径（用户目录的Chrome）
        options.binary_location = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe"

        # 无头模式
        if self.headless:
            options.add_argument('--headless')

        # 禁用一些检测
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)

        # 用户数据目录（保持登录状态）
        # options.add_argument(r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')

        # 禁用一些不必要的提示
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')

        # 下载设置
        prefs = {
            'download.default_directory': r'C:\Users\Administrator\.openclaw-autoclaw\workspace\downloads',
            'download.prompt_for_download': False,
            'safebrowsing.enabled': False
        }
        options.add_experimental_option('prefs', prefs)

        # 自动下载并安装ChromeDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(10)

        print("✓ Chrome浏览器已启动")

    def open(self, url):
        """打开URL

        Args:
            url: 网址
        """
        if not self.driver:
            self.start()

        self.driver.get(url)
        print(f"✓ 已打开: {url}")
        time.sleep(2)

    def find_element(self, by, value, timeout=10):
        """查找元素

        Args:
            by: 查找方式
            value: 查找值
            timeout: 超时时间

        Returns:
            WebElement or None
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except Exception as e:
            print(f"✗ 未找到元素: {value}")
            return None

    def click(self, by, value, timeout=10):
        """点击元素

        Args:
            by: 查找方式
            value: 查找值
            timeout: 超时时间

        Returns:
            bool: 是否点击成功
        """
        element = self.find_element(by, value, timeout)
        if element:
            try:
                element.click()
                time.sleep(1)
                return True
            except Exception as e:
                print(f"✗ 点击失败: {e}")
                return False
        return False

    def input_text(self, by, value, text, timeout=10):
        """输入文本

        Args:
            by: 查找方式
            value: 查找值
            text: 输入文本
            timeout: 超时时间

        Returns:
            bool: 是否输入成功
        """
        element = self.find_element(by, value, timeout)
        if element:
            try:
                element.clear()
                element.send_keys(text)
                time.sleep(0.5)
                return True
            except Exception as e:
                print(f"✗ 输入失败: {e}")
                return False
        return False

    def screenshot(self, filename):
        """截图

        Args:
            filename: 文件名
        """
        if self.driver:
            self.driver.save_screenshot(filename)
            print(f"✓ 截图已保存: {filename}")

    def get_text(self, by, value, timeout=10):
        """获取元素文本

        Args:
            by: 查找方式
            value: 查找值
            timeout: 超时时间

        Returns:
            str: 元素文本
        """
        element = self.find_element(by, value, timeout)
        if element:
            return element.text
        return ""

    def wait(self, seconds):
        """等待

        Args:
            seconds: 秒数
        """
        time.sleep(seconds)

    def close(self):
        """关闭浏览器"""
        if self.driver:
            self.driver.quit()
            self.driver = None
            print("✓ Chrome浏览器已关闭")

    def __del__(self):
        """析构函数"""
        self.close()


if __name__ == "__main__":
    # 测试
    controller = ChromeController()
    controller.start()
    controller.open("https://open.feishu.cn/")
    controller.wait(5)
    controller.screenshot("test_screenshot.png")
    controller.close()
