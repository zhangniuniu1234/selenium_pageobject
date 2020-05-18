from time import sleep

from selenium_wework.common_utils.basepage import BasePage
from selenium_wework.selenium_wework_register.index import Index


class Testregister():

    def setup(self):
        self.Index = Index()


    def teardown(self):
        self.Index._driver.quit()

    def test_register(self):
        self.Index.goto_login().goto_register().register()
        sleep(5)



