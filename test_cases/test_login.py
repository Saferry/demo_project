import pytest
from page_objects.login_page import LoginPage
from utils.read_config import ReadConfig


def test_login_with_captcha(driver):
    """
    测试登录功能（包含验证码处理）。
    :param driver: WebDriver 实例
    :param base_url: 基础 URL
    :param login_credentials: 登录凭证
    """
    
    config = ReadConfig()
    # 获取配置信息
    url = config.get_base_url()
    username = config.get_user_name()
    password = config.get_pass_word()
    
    # 实例化LoginPage
    login_page = LoginPage(driver)
    captcha = login_page.get_captcha_txt()
    
    # 登录完成
    login_page.login(url=url, username=username, password=password, captcha=captcha)

    # 获取验证码图片路径

    # 断言登录成功
    assert driver.current_url == base_url + "/console/mylearning"
