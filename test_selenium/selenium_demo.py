#!/usr/bin/env python
# encoding: utf-8
"""
@author: zixue.ren
@contact: renzixue@58.com
@file: selenium_demo.py
@time: 2021/2/28 14:12
@desc:
"""

# Generated by Selenium IDE
import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTmp:
    def setup_method(self, method):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def test_main_tmp(self):
        """
        基于首页登录
        :return:
        """
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()
        self.driver.find_element(By.XPATH, "//*[@class='login_registerBar_link']").click()
        self.driver.find_element(By.XPATH, "//*[@id='corp_name']").send_keys("xxxx")
        sleep(6)
        self.driver.close()

    def test_login_tmp(self):
        """
        基于浏览器复用后的内容进行操作
        :return:
        """
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

    def test_cookie_login(self):
        """
        利用 cookie 进行登陆
        :return:
        """
        # 存入 cookie
        # cookies = self.driver.get_cookies()
        # with open("tmp2.text","w", encoding="utf-8") as f:
        #     json.dump(cookies, f)

        # 读取 cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open("tmp2.text", "r", encoding="utf-8") as f:
            # 序列化
            cookies = json.load(f)
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        sleep(6)
