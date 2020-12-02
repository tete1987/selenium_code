#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/2 15:13 
# @Author : TETE
# @File : base_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self,driver:WebDriver=None):
        if driver is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=option)
            self._driver.implicitly_wait(5)

        else:
            self._driver=driver

        if self._base_url != "" :
            self._driver.get(self._base_url)

    def find(self,by ,locator):
        return self._driver.find_element(by ,locator)

    def finds(self,by ,locator):
        return self._driver.find_elements(by ,locator)

    def wati_for_click(self,locator,time=10):
        WebDriverWait(self._driver,time).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_elem(self,conditions,time=10):
        WebDriverWait(self._driver,time).until(conditions)