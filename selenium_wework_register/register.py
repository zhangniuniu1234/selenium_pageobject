from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework.common_utils.basepage import BasePage


class Register:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def register(self):
        # send content,click element
        self._driver.find_element(By.ID,'corp_name').send_keys("hello")
        self._driver.find_element(By.ID,'manager_name').send_keys('加油呀')




