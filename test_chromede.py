#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/1 16:33 
# @Author : TETE
# @File : test_chromede.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestChrome:
    def setup_method(self,method):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)

    def teardown(self):
        self.driver.quit()

    def test_chrome(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.XPATH,'//*[@id="menu_contacts"]/span').click()
        sleep(3)