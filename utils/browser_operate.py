# !/usr/bin/env python
# _*_ coding:utf-8 _*_
#

# 导入 Selenium 相关模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 定义 BrowserOperate 类，用于封装浏览器操作
class BrowserOperate:
    def __init__(self, driver):
        """
        初始化 BrowserOperate 类。
        :param driver: Selenium WebDriver 实例
        """
        self.driver = driver

    def open_url(self, url):
        """
        打开指定的 URL。
        :param url: 要访问的网页地址
        """
        self.driver.get(url)

    def find_element(self, locator):
        """
        查找页面元素，使用显式等待确保元素加载完成。
        :param locator: 元素定位器，格式为 (By.ID, "element_id") 等
        :return: 找到的页面元素
        """
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        """
        点击页面元素。
        :param locator: 元素定位器
        """
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        """
        向页面元素输入文本。
        :param locator: 元素定位器
        :param text: 要输入的文本
        """
        element = self.find_element(locator)
        element.clear()  # 清空输入框
        element.send_keys(text)

    def get_text(self, locator):
        """
        获取页面元素的文本内容。
        :param locator: 元素定位器
        :return: 元素的文本内容
        """
        element = self.find_element(locator)
        return element.text
