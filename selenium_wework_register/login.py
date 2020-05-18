from selenium.webdriver.common.by import By

from selenium_wework.common_utils.basepage import BasePage
from selenium_wework.selenium_wework_register.register import Register

from selenium.webdriver.remote.webdriver import WebDriver
class Login:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def scanf(self):
        pass

    def goto_register(self):
        #click register
        self._driver.find_element(By.XPATH,'//*[@id="wework_admin.loginpage_wx_$"]/main/div[2]/a').click()
        return Register(self._driver)
