#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/30 9:57 
# @Author : TETE
# @File : test_window.py
from time import sleep

from selenium.webdriver.common.by import By

from selenium_code.base import Base


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        print("登录页面",self.driver.current_window_handle)
        print("所有页面：",self.driver.window_handles)
        sleep(3)
        self.driver.find_element_by_link_text("立即注册").click()
        print("立即注册页面：",self.driver.current_window_handle)
        print("所有页面：",self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        sleep(2)
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__userName').send_keys("aaaaa")
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__phone').send_keys("18900389202")
        sleep(2)
        self.driver.switch_to_window(windows[0])
        self.driver.find_element(By.ID,'TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element(By.ID,'TANGRAM__PSP_11__userName').send_keys("dddd")
        self.driver.find_element(By.ID,'TANGRAM__PSP_11__password').send_keys("234345")
        self.driver.find_element(By.ID,'TANGRAM__PSP_11__submit').click()
        sleep(3)