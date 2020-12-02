#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/2 13:52 
# @Author : TETE
# @File : addMember.py
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium_code.wx_PageObject02.Page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        self.find(By.ID,'username').send_keys("AAAA")
        self.find(By.ID,'memberAdd_acctid').send_keys("AAAAA")
        self.find(By.ID,'memberAdd_phone').send_keys("18700090008")
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()
        return True

    def update_page(self):
        content: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        return [int(x) for x in content.split('/',1)]

    def get_member(self,value):
        self.wati_for_click((By.CSS_SELECTOR,'.ww_checkbox'))
        cur_page,total_page = self.update_page()
        while True:
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            for ele in elements:
                if value == ele.get_attribute("title"):
                    return True

            cur_page=self.update_page()
            if cur_page == total_page:
                return False
            self.find(By.CSS_SELECTOR,'.js_next_page').click()
