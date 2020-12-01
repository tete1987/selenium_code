#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/30 17:24 
# @Author : TETE
# @File : test_alert.py
from time import sleep

from selenium.webdriver import ActionChains

from selenium_code.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag =self.driver.find_element_by_id("draggable")
        drop =self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        print("点击alert确认")
        sleep(3)
        self.driver.switch_to.alert.accept()
        sleep(2)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)
