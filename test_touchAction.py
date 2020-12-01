#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/27 17:42 
# @Author : TETE
# @File : test_touchAction.py
from time import sleep

from selenium.webdriver import TouchActions

from selenium_code.base import Base


class TestTouchAction(Base):
    def test_touch_action(self):
        self.driver.get("http://www.baidu.com")
        ele=self.driver.find_element_by_id("kw").send_keys('selenium测试')
        ele_click=self.driver.find_element_by_id("su")
        action = TouchActions(self.driver)
        action.tap(ele_click)
        action.perform()
        action.scroll_from_element(ele_click,0,10000).perform()
        sleep(3)