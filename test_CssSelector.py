#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/26 15:56 
# @Author : TETE
# @File : test_CssSelector.py
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestS01():
    def setup(self):
        self.driver =webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")

    def test_css(self):
        self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("abc")
        self.driver.find_element(By.ID,'su').click()