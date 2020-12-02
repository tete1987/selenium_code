#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/2 13:45 
# @Author : TETE
# @File : main_page.py

from selenium.webdriver.common.by import By

from selenium_code.wx_PageObject02.Page.addMember import AddMember
from selenium_code.wx_PageObject02.Page.base_page import BasePage


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def teardown(self):
        self._driver.quit()

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, '#menu_contacts').click()
        self.wati_for_click((By.LINK_TEXT, '添加成员'))
        self.find(By.LINK_TEXT, '添加成员').click()
        return AddMember(self._driver)
        #def wait_add_member(x):
        #     elements_len = len(self.find(By.CSS_SELECTOR,'#username'))
        #     if elements_len <=0:
        #         self.find(By.LINK_TEXT,'添加成员').click()
        #     return elements_len > 0
        #
        # self.wait_for_elem(wait_add_member)
        # return AddMember(self._driver)