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

des_caps = {}
des_caps['platformName'] = 'Android'
des_caps['platformVersion'] = '10.0'
des_caps['deviceName'] = '7HX5T19918005212'
drvier = webdriver.Remote("http://localhost:4723/wd/hub", des_caps)
drvier.quit()
