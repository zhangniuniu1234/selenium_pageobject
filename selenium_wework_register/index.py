from selenium.webdriver.common.by import By

from selenium_wework.common_utils.basepage import BasePage
from selenium_wework.selenium_wework_register.login import Login
from selenium_wework.selenium_wework_register.register import Register
from selenium import webdriver

class  Index:
    def __init__(self):
        self._driver=webdriver.Chrome()
        self._driver.get('https://work.weixin.qq.com/')
        self._driver.maximize_window()
        self._driver.implicitly_wait(10)



    def goto_login(self):
        #index_top_operation_loginBtn
        self._driver.find_element(By.CLASS_NAME, "index_top_operation_loginBtn").click()
        return Login(self._driver)

    def goto_register(self):
        #click register
        self._driver.find_element(By.CLASS_NAME, 'index_head_info_pCDownloadBtn').click()
        return Register(self._driver)