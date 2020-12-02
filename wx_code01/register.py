#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/2 11:20 
# @Author : TETE
# @File : register.py
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self,driver:WebDriver):
        self._driver = driver

    def register(self):
        self._driver.find_element(By.CSS_SELECTOR,'#corp_name').send_keys("aaaaa")
        self._driver.find_element(By.XPATH,'//*[@id="corp_industry"]/a/span[1]').click()
        self._driver.find_element_by_link_text("IT服务").click()
        self._driver.find_element_by_link_text("计算机软件/硬件/信息服务").click()
        sleep(2)
        self._driver.find_element(By.ID,'manager_name').send_keys("管理员A")
        sleep(3)
        self._driver.quit()
        return True


