#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/30 10:27 
# @Author : TETE
# @File : test_frame.py
from selenium_code.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #先进入到iframe中
        self.driver.switch_to_frame("iframeResult")
        #打印“请拖拽我”元素的文本
        print(self.driver.find_element_by_id("draggable").text)
        #再回到原来默认的iframe中
        self.driver.switch_to_default_content()
        #打印“点击运行”元素的文本
        print(self.driver.find_element_by_id("submitBTN").text)
