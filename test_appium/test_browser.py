#!/usr/bin/env python
# encoding: utf-8
'''
@author: zixue.ren
@contact: renzixue@58.com
@file: test_browser.py
@time: 2021-03-04 19:41
@desc: 移动端web测试
'''
from time import sleep

from appium import webdriver


class TestBrowsers():
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'paltformVersion': '6.0',
            'browserName': 'Browser',
            # 'noReset': True,
            'deviceName': 'emulator-5554',
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)
