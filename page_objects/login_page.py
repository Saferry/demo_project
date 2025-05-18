# !/usr/bin/env python
# _*_ coding:utf-8 _*_
#

import os
import time
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from utils.captcha_recognition import CaptchaRecognition


class LoginPage(BasePage):
    # 通过配置文件获取登录页面的 URL
   
    # 页面元素定位器
    USERNAME_INPUT = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/form/div[1]/div[1]/div/div/input')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/form/div[1]/div[2]/div/div/input')
    # 学员端、管理端选择？
    CAPTCHA_INPUT = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/form/div[1]/div[4]/div/div/div[1]/input')
    CAPTCHA_IMAGE = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/form/div[1]/div[4]/div/div/div[2]/img')
    LOGIN_BUTTON = (By.XPATH, 'login_button')
    COLLEGE_IPTION = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[4]/div[1]')

    def login(self, url, username, password, captcha):
        """
        执行登录操作。
        :param url: 地址
        :param username: 用户名
        :param password: 密码
        :param captcha：验证码
        """
        self.browser.open_url(url)
        self.browser.send_keys(self.USERNAME_INPUT, username)
        self.browser.send_keys(self.PASSWORD_INPUT, password)
        self.browser.send_keys(self.CAPTCHA_INPUT, captcha)
        self.browser.click(self.LOGIN_BUTTON)
        self.browser.click(self.COLLEGE_IPTION)
        self.recognize_captcha = CaptchaRecognition()

    def get_captcha_image(self, url):
        """
        获取验证码图片并保存到 /temp 文件夹中。
        :return: 验证码图片的本地路径
        """
        self.browser.open_url(url)  # 打开登录页面
        captcha_image = self.browser.find_element(self.CAPTCHA_IMAGE)  # 定位验证码图片元素

        # 确保 /temp 文件夹存在
        temp_dir = "/temp"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        # 生成验证码图片的文件名（例如：captcha_1681234567.png）
        timestamp = int(time.time())
        captcha_file_path = os.path.join(temp_dir, f"captcha_{timestamp}.png")

        # 保存验证码图片到本地
        captcha_image.screenshot(captcha_file_path)

        return captcha_file_path  # 返回验证码图片的路径
    
    def get_captcha_txt(self, url):
        """
        获取验证码文本
        :return: 验证码识别内容
        """
        image_path = self.get_captcha_image(url)
        captcha_code = self.recognize_captcha.recognize_captcha(image_path)  # str
        
        return captcha_code
