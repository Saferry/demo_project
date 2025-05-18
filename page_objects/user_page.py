# !/usr/bin/env python
# _*_ coding:utf-8 _*_
#

# 导入 BasePage 类
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


# 定义 UserPage 类，继承自 BasePage
class UserPage(BasePage):
    # 用户管理页面的 URL
    URL = "http://example.com/users"
    # 页面元素定位器
    ADD_USER_BUTTON = (By.ID, "add_user")
    USER_TABLE = (By.ID, "user_table")
    DELETE_BUTTON = (By.ID, "delete_button")
    EDIT_BUTTON = (By.ID, "edit_button")

    def open_user_page(self):
        """
        打开用户管理页面。
        """
        self.browser.open_url(self.URL)

    def add_user(self, username, password):
        """
        添加新用户。
        :param username: 用户名
        :param password: 密码
        """
        # 点击添加用户按钮
        self.browser.click(self.ADD_USER_BUTTON)
        # 输入用户名
        self.browser.send_keys((By.ID, "new_username"), username)
        # 输入密码
        self.browser.send_keys((By.ID, "new_password"), password)
        # 点击保存按钮
        self.browser.click((By.ID, "save_button"))

    def delete_user(self, username):
        """
        删除用户。
        :param username: 要删除的用户名
        """
        # 点击对应用户的删除按钮
        self.browser.click((By.XPATH, f"//tr[contains(., '{username}')]/td/button[@id='delete_button']"))

    def edit_user(self, username, new_password):
        """
        编辑用户信息。
        :param username: 用户名
        :param new_password: 新密码
        """
        # 点击对应用户的编辑按钮
        self.browser.click((By.XPATH, f"//tr[contains(., '{username}')]/td/button[@id='edit_button']"))
        # 输入新密码
        self.browser.send_keys((By.ID, "edit_password"), new_password)
        # 点击保存按钮
        self.browser.click((By.ID, "save_button"))

    def search_user(self, username):
        """
        搜索用户。
        :param username: 要搜索的用户名
        :return: 搜索结果的文本内容
        """
        # 输入用户名
        self.browser.send_keys((By.ID, "search_input"), username)
        # 点击搜索按钮
        self.browser.click((By.ID, "search_button"))
        # 获取用户表格的内容
        return self.browser.get_text(self.USER_TABLE)
