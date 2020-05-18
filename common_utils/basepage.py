from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import  webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None
    _base_url = ''

    def __init__(self, driver: WebDriver = None):
        #driver没传值，给driver重新赋值。传了参数则用传入的driver
        if driver is None:
            option = Options()
            option.debugger_address = "127.0.0.1:9111"
            self._driver = webdriver.Chrome(options=option)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

        #url不为空，则访问该url地址
        if self._base_url != "":
            self._driver.get(self._base_url)

        # 查找某个元素

    def find_elem(self, by, locator):
        return self._driver.find_element(by, locator)


        # 查找元素集

    def finds_elem(self, by, locator):
        return self._driver.find_elements(by, locator)

        # 显式等待直到某个元素可被点击

    def wait_for_elemclick(self, locator, time=6):
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))

        # 显式等待某个元素直到条件成立

    def wait_for_elem(self, condition, time=10):
        WebDriverWait(self._driver, time).until(condition)




