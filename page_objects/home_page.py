# !/usr/bin/env python
# _*_ coding:utf-8 _*_
#

# 导入 BasePage 类
from page_objects.base_page import BasePage


# 定义 HomePage 类，继承自 BasePage
class HomePage(BasePage):
    # 首页的 URL
    URL = "http://example.com/home"
    # 页面元素定位器
    WELCOME_MESSAGE = (By.ID, "welcome_message")

    def get_welcome_message(self):
        """
        获取欢迎消息的文本内容。
        :return: 欢迎消息的文本
        """
        return self.browser.get_text(self.WELCOME_MESSAGE)
