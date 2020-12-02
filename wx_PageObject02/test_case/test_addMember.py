#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/2 14:04 
# @Author : TETE
# @File : test_addMember.py

from selenium_code.wx_PageObject02.Page.main_page import Index


class TestAddMember():
    def setup(self):
        self.main_page = Index()

    def test_addMember(self):
        add_member = self.main_page.goto_add_member()
        add_member.add_member()
        assert add_member.get_member("李四")