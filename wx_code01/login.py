#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/2 11:19 
# @Author : TETE
# @File : login.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_code.wx_pageObjectDemo1.register import Register


class Login:
    def __init__(self,driver:WebDriver):
        #python3 特性，类似标签
        self._driver = driver

    def scanf(self):
        #扫码登录，暂不解决
        pass

    def goto_register(self):
        #点击立即注册
        self._driver.find_element(By.CSS_SELECTOR,'.login_registerBar_link').click()
        return Register()