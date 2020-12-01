#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/26 16:50 
# @Author : TETE
# @File : test_ActionChains.py
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class TestAction():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_action(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        ele_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        ele_doubleClick=self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        ele_rightClick = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(ele_click)
        action.double_click(ele_doubleClick)
        action.context_click(ele_rightClick)
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_move(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()
        ele = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        self.driver.maximize_window()
        ele_drag = self.driver.find_element_by_id("dragger")
        ele_drag2 = self.driver.find_element_by_xpath('//div[@class="item"]')
        action = ActionChains(self.driver)
        # action.drag_and_drop(ele_drag,ele_drag2).perform()
        # action.click_and_hold(ele_drag).release(ele_drag2).perform()
        action.click_and_hold(ele_drag).move_to_element(ele_drag2).release().perform()
        sleep(3)