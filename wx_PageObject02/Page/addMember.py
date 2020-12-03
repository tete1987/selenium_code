#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/2 13:52 
# @Author : TETE
# @File : addMember.py

from selenium.webdriver.common.by import By

from selenium_code.wx_PageObject02.Page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        self.find(By.ID,'username').send_keys("AAAA")
        self.find(By.ID,'memberAdd_acctid').send_keys("AAAAA")
        self.find(By.ID,'memberAdd_phone').send_keys("18700090008")
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()
        return True

    def update_page(self):
        #获取“翻页”功能定位及文本，将其更改为字符串格式
        content: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        #对翻页的文本进行切割，1次，并放入列表中
        return [int(x) for x in content.split('/',1)]

    def get_member(self,value):
        #点击 下一页
        self.wati_for_click((By.CSS_SELECTOR,'.ww_checkbox'))
        #将切割的列表赋值给两个变量
        cur_page,total_page = self.update_page()
        while True:
            #获取页面数据列表中的“姓名”的字段定位
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            #遍历所有姓名元素的title属性
            for ele in elements:
                if value == ele.get_attribute("title"):
                    return True
            #更新页面
            cur_page=self.update_page()
            if cur_page == total_page:
                return False
            self.find(By.CSS_SELECTOR,'.js_next_page').click()
