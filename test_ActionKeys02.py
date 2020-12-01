#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/27 17:18 
# @Author : TETE
# @File : test_ActionKeys02.py
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium_code.base import Base

class TestActionKeys02(Base):
    def test_action_keys02(self):
        self.driver.get("http://sahitest.com/demo/")
        self.driver.find_element_by_link_text('Label Page').click()
        text1 = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        action = ActionChains(self.driver)
        text1.click()
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

