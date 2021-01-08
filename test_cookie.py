#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/1 16:33 
# @Author : TETE
# @File : test_chromede.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestChrome:
    def setup_method(self, method):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        # print(self.driver.get_cookies())
        cookies = {'domain': '.work.weixin.qq.com', 'expiry': 1638411313, 'httpOnly': False,
                                 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                 'value': '1606811058,1606874353,1606875304'}, {'domain': '.qq.com',
                                                                                'expiry': 1606962817, 'httpOnly': False,
                                                                                'name': '_gid', 'path': '/',
                                                                                'secure': False,
                                                                                'value': 'GA1.2.887702860.1606811058'}, {
                                    'domain': '.qq.com', 'expiry': 1606876466, 'httpOnly': False, 'name': '_gat',
                                    'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com',
                                                                                  'expiry': 1669948417,
                                                                                  'httpOnly': False, 'name': '_ga',
                                                                                  'path': '/', 'secure': False,
                                                                                  'value': 'GA1.2.1123723369.1606811058'}, {
                                    'domain': '.work.weixin.qq.com', 'expiry': 1609468420.311611, 'httpOnly': False,
                                    'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {
                                    'domain': '.work.weixin.qq.com', 'expiry': 1638347048.359358, 'httpOnly': False,
                                    'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {
                                    'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid',
                                    'path': '/', 'secure': False, 'value': '27184059492011728'}, {'domain': '.qq.com',
                                                                                                  'expiry': 2147385600,
                                                                                                  'httpOnly': False,
                                                                                                  'name': 'pgv_pvi',
                                                                                                  'path': '/',
                                                                                                  'secure': False,
                                                                                                  'value': '2033898496'}, {
                                    'domain': '.qq.com', 'expiry': 2147483640.977564, 'httpOnly': False, 'name': 'RK',
                                    'path': '/', 'secure': False, 'value': 'uqj4btYTEa'}, {
                                    'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid',
                                    'path': '/', 'secure': False, 'value': '1688850785700311'}, {
                                    'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype',
                                    'path': '/', 'secure': False, 'value': '1'}, {'domain': 'work.weixin.qq.com',
                                                                                  'expiry': 1606905863.695738,
                                                                                  'httpOnly': True, 'name': 'ww_rtkey',
                                                                                  'path': '/', 'secure': False,
                                                                                  'value': '15k11f8'}, {
                                    'domain': '.qq.com', 'expiry': 2147483640.977684, 'httpOnly': False, 'name': 'ptcz',
                                    'path': '/', 'secure': False,
                                    'value': 'f416945781245808a65612452c26fe42b33c64ac1771380fa02f46b3600919e3'}, {
                                    'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/',
                                    'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com',
                                                                          'httpOnly': False, 'name': 'wwrtx.d2st',
                                                                          'path': '/', 'secure': False,
                                                                          'value': 'a2382445'}, {
                                    'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/',
                                    'secure': False,
                                    'value': 'SsjRpQMl9IX4iWi5eOG0Su9rPRfcUxY5glEos9Iom6akPCPfy5vDKYWV1JBStQsw'}, {
                                    'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid',
                                    'path': '/', 'secure': False, 'value': '1970325111201446'}, {
                                    'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/',
                                    'secure': False,
                                    'value': 'kh329F94GdkgRDzYlbPI2qFgR75YgKOHma3967osbvpNweaVi1mDZs-bWGZ_8cQEB0Vk_ojUCFq3PJBH99zSNUuesJdDrp5a0wqcbCwlUBBUKo8bj0HggYAygn5mMd_RT8rZMtnGB-FCkLK5dnrxrE26c-BHpX7llaReX2Eu0fmRYRt8WNlDGjJ48esikg5rg6KN3iXQjx6C1xKHqQOv_AwBRnFRcMeISrQQrGFFK_paZVRO7Casj6NfyIzUwwhnaxPlDRo_bJxy0YuT01AHow'}, {
                                    'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid',
                                    'path': '/', 'secure': False, 'value': '1688850785700311'}
        print(self.driver.get_cookies())
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        sleep(3)
