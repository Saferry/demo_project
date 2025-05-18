# 导入 pytest 和相关页面类
import pytest
from page_objects.login_page import LoginPage
from page_objects.user_page import UserPage

# 测试添加用户
def test_add_user(driver, base_url, login_credentials, test_data):
    """
    测试添加用户。
    :param driver: WebDriver 实例
    :param base_url: 基础 URL
    :param login_credentials: 登录凭证
    :param test_data: 测试数据
    """
    login_page = LoginPage(driver)  # 创建 LoginPage 实例
    username, password = login_credentials  # 获取登录凭证
    login_page.login(username, password)  # 执行登录操作
    user_page = UserPage(driver)  # 创建 UserPage 实例
    user_page.open_user_page()  # 打开用户管理页面
    new_user_data = test_data("new_user")  # 获取测试数据
    user_page.add_user(new_user_data["username"], new_user_data["password"])  # 添加用户
    # 断言用户添加成功
    assert new_user_data["username"] in user_page.search_user(new_user_data["username"])

# 测试删除用户
def test_delete_user(driver, base_url, login_credentials, test_data):
    """
    测试删除用户。
    :param driver: WebDriver 实例
    :param base_url: 基础 URL
    :param login_credentials: 登录凭证
    :param test_data: 测试数据
    """
    login_page = LoginPage(driver)  # 创建 LoginPage 实例
    username, password = login_credentials  # 获取登录凭证
    login_page.login(username, password)  # 执行登录操作
    user_page = UserPage(driver)  # 创建 UserPage 实例
    user_page.open_user_page()  # 打开用户管理页面
    new_user_data = test_data("new_user")  # 获取测试数据
    user_page.add_user(new_user_data["username"], new_user_data["password"])  # 添加用户
    user_page.delete_user(new_user_data["username"])  # 删除用户
    # 断言用户删除成功
    assert new_user_data["username"] not in user_page.search_user(new_user_data["username"])

# 测试编辑用户
def test_edit_user(driver, base_url, login_credentials, test_data):
    """
    测试编辑用户。
    :param driver: WebDriver 实例
    :param base_url: 基础 URL
    :param login_credentials: 登录凭证
    :param test_data: 测试数据
    """
    login_page = LoginPage(driver)  # 创建 LoginPage 实例
    username, password = login_credentials  # 获取登录凭证
    login_page.login(username, password)  # 执行登录操作
    user_page = UserPage(driver)  # 创建 UserPage 实例
    user_page.open_user_page()  # 打开用户管理页面
    new_user_data = test_data("new_user")  # 获取测试数据
    user_page.add_user(new_user_data["username"], new_user_data["password"])  # 添加用户
    user_page.edit_user(new_user_data["username"], new_user_data["new_password"])  # 编辑用户
    # 断言用户编辑成功
    assert new_user_data["new_password"] in user_page.search_user(new_user_data["username"])

# 测试搜索用户
def test_search_user(driver, base_url, login_credentials, test_data):
    """
    测试搜索用户。
    :param driver: WebDriver 实例
    :param base_url: 基础 URL
    :param login_credentials: 登录凭证
    :param test_data: 测试数据
    """
    login_page = LoginPage(driver)  # 创建 LoginPage 实例
    username, password = login_credentials  # 获取登录凭证
    login_page.login(username, password)  # 执行登录操作
    user_page = UserPage(driver)  # 创建 UserPage 实例
    user_page.open_user_page()  # 打开用户管理页面
    new_user_data = test_data("new_user")  # 获取测试数据
    user_page.add_user(new_user_data["username"], new_user_data["password"])  # 添加用户
    result = user_page.search_user(new_user_data["username"])  # 搜索用户
    # 断言搜索结果包含用户名
    assert new_user_data["username"] in result