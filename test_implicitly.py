#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/26 13:38 
# @Author : TETE
# @File : test_implicitly.py
import pytest
from selenium import webdriver
from time import sleep

class TestSelenium():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_s01(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社区").click()
        self.driver.find_element_by_xpath('//a[@title="MTSC2020 深圳大会集中问答帖"]').click()
