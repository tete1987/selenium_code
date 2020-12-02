#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/2 11:17 
# @Author : TETE
# @File : index.py
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_code.wx_pageObjectDemo1.login import Login
from selenium_code.wx_pageObjectDemo1.register import Register

class Index:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get("https://work.weixin.qq.com/")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

    def goto_login(self):
        #点击登录
        self._driver.find_element(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return Login(self._driver)

    def goto_register(self):
        #点击立即注册
        self._driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)