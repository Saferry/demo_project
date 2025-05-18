# 导入 pytest 和相关页面类
import pytest
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage


# 测试首页的欢迎消息
def test_home_welcome_message(driver, base_url, login_credentials):
    """
    测试首页的欢迎消息。
    :param driver: WebDriver 实例
    :param base_url: 基础 URL
    :param login_credentials: 登录凭证
    """
    login_page = LoginPage(driver)  # 创建 LoginPage 实例
    username, password = login_credentials  # 获取登录凭证
    login_page.login(username, password)  # 执行登录操作
    home_page = HomePage(driver)  # 创建 HomePage 实例
    message = home_page.get_welcome_message()  # 获取欢迎消息
    # 断言欢迎消息中包含 "Welcome"
    assert "Welcome" in message
