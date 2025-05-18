# !/usr/bin/env python
# _*_ coding:utf-8 _*_
#

# 导入 Selenium 相关模块
# from selenium.webdriver.common.by import By
from utils.browser_operate import BrowserOperate


# 定义 BasePage 类，作为所有页面对象的基类
class BasePage:
    def __init__(self, driver):
        """
        初始化 BasePage 类。
        :param driver: Selenium WebDriver 实例
        """
        self.driver = driver
        # 初始化 BrowserOperate 实例，用于封装浏览器操作
        self.browser = BrowserOperate(driver)
