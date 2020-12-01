#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/26 14:08 
# @Author : TETE
# @File : test_WebDriverWait.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@id="ember31"]/a').click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@class="link-top-line"]/a')))
        self.driver.find_element(By.XPATH, '//*[@class="link-top-line"]/a').click()
