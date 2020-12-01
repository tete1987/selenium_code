#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/30 8:51 
# @Author : TETE
# @File : test_form.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        sleep(2)
        self.driver.find_element(By.ID,'user_login').send_keys("huahua")
        self.driver.find_element(By.ID,'user_password').send_keys("12334345")
        self.driver.find_element(By.XPATH,'//*[@id="new_user"]//label').click()
        self.driver.find_element(By.XPATH,'//*[@class="btn btn-primary btn-lg btn-block"]').click()
        sleep(5)
