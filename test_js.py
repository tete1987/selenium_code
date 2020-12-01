#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/30 15:26 
# @Author : TETE
# @File : test_js.py
from time import sleep

from selenium.webdriver.common.by import By

from selenium_code.base import Base


class TestJs(Base):
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        sleep(1)
        self.driver.execute_script("return document.documentElement.scrollTop=10000")
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="page"]//a[10]').click()
        sleep(2)
        for code in [
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))