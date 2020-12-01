#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/30 16:40 
# @Author : TETE
# @File : test_upload.py
from time import sleep

from selenium.webdriver.common.by import By

from selenium_code.base import Base
import allure

@allure.feature("百度上传图片")
class TestUpload(Base):
    def test_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.XPATH,'//*[@id="sttb"]/img[1]').click()
        sleep(2)

        self.driver.find_element(By.ID,'uploadImg').send_keys("./result/b.png")
        sleep(5)

        # with allure.step('进行截图'):
        #     self.driver.save_screenshot("./result/b.png")
        #     allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)