# !/usr/bin/env python
# _*_ coding:utf-8 _*_
#

# 导入 pytest 和 Selenium 相关模块
import pytest
from selenium import webdriver
from utils.read_config import ReadConfig

# 创建 ReadConfig 实例，加载配置文件
config = ReadConfig("config/config.yaml")


# 定义 driver 固件，作用域为 session 级别
@pytest.fixture(scope="session")
def driver():
    """
    创建 WebDriver 实例，并在测试结束后关闭浏览器。
    :return: WebDriver 实例
    """
    driver = webdriver.Chrome()  # 使用 Chrome 浏览器
    yield driver  # 提供 driver 实例给测试用例
    driver.quit()  # 测试结束后关闭浏览器


# 定义 base_url 固件，提供基础 URL
@pytest.fixture(scope="session")
def base_url():
    """
    提供基础 URL。
    :return: 基础 URL
    """
    return config.get_base_url()


# 定义 login_credentials 固件，提供登录凭证
@pytest.fixture(scope="session")
def login_credentials():
    """
    提供登录凭证。
    :return: 登录用户名和密码
    """
    return config.get_login_credentials()


# 定义 test_data 固件，提供测试数据
@pytest.fixture(scope="session")
def test_data():
    """
    提供测试数据。
    :return: 测试数据字典
    """
    return config.get_test_data
