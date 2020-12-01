#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/27 16:11 
# @Author : TETE
# @File : test_ActionKey01.py


'''
测试案例：
打开网址：http://sahitest.com/demo/label.htm
定位两个输入框 e1，e2
向输入框e1中输入文字：username
使用全选，复制，粘贴到输入框e2中
'''
from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium_code.base import Base
from selenium import webdriver

class TestActionKeys(Base):
    def test_action_key(self):
        self.driver.get("http://sahitest.com/demo/")
        self.driver.find_element_by_link_text('Label Page').click()
        text1 =self.driver.find_element_by_xpath('/html/body/label[1]/input')
        text2 = self.driver.find_element_by_xpath('/html/body/label[2]/table/tbody/tr/td[2]/input')
        action = ActionChains(self.driver)
        text1.click()
        action.send_keys("AAAA").perform()
        action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        text2.click()
        action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        sleep(3)


