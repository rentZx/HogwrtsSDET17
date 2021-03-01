#!/usr/bin/env python
# encoding: utf-8
"""
@author: zixue.ren
@contact: renzixue@58.com
@file: test_address.py
@time: 2021/2/28 14:27
@desc:企业微信自动化实战之通讯录添加成员
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestTmp():
    def test_address(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)
        # 点击通讯录
        self.driver.find_element_by_id("menu_contacts").click()
        # 点击添加成员
        self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[-1].click()

        def wait_names(driver):
            l = self.driver.find_elements(By.XPATH, "//*[@id='username']")
            return len(l) > 0

        WebDriverWait(self.driver, 5).until(wait_names)
        # 输入姓名
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("今天是星期3")
        # 输入账号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys("test6")
        # 输入手机号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys("13234233264")
        # 点击保存
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']").click()
