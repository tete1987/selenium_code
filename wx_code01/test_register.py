#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/2 11:53 
# @Author : TETE
# @File : test_register.py
from selenium_code.wx_pageObjectDemo1.index import Index


class TestRegister:
    def setup(self):
        self.index = Index()

    def test_register(self):
        self.index.goto_register().register()