#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/30 15:54 
# @Author : TETE
# @File : test_js02.py
from selenium_code.base import Base
from time import sleep

class TestJS(Base):
    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        print(self.driver.execute_script(" return document.getElementById('train_date').value"))
        sleep(3)