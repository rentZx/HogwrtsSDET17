#!/usr/bin/env python
# encoding: utf-8
'''
@author: zixue.ren
@contact: renzixue@58.com
@file: appium_Demo.py
@time: 2021-03-02 15:25
@desc:
'''
from appium import webdriver


class TestAppDriver():
    def setup(self):
        des_caps = {}
        des_caps['platformName'] = 'Android'
        # des_caps['platformVersion'] = '6.0'
        des_caps['deviceName'] = 'emulator-5554'
        des_caps['appPackage'] = 'com.tencent.wework'
        des_caps['appActivity'] = '.launch.LaunchSplashActivity'
        des_caps['noRest'] = True
        des_caps['skipServerInstallation'] = True
        des_caps['unicodeKeyBoard'] = "true"
        des_caps['unicodeKeyBoard'] = "true"
        self.drvier = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.drvier.implicitly_wait(5)

    def teardown(self):
        pass

    def test_earch(self):
        pass
