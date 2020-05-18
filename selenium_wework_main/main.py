from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework.common_utils.basepage import BasePage
from selenium_wework.selenium_wework_main.member_action import MemberAction





class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member(self):
        # click add member点击首页的"添加成员"
        # self.driver.find_element_by_css_selector('#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt.js_service_list > a:nth-child(1) > div > span.index_service_cnt_item_title').click()
        # return AddMember(self.driver)

       #点击通讯录
        self.find_elem(By.CSS_SELECTOR, '#menu_contacts > span').click()

        def wait_add_member(x):
            elem_len = len(self.finds_elem(By.CSS_SELECTOR, '#username'))
            #元素不存在
            if elem_len <= 0:
                self.find_elem(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
            return elem_len > 0
        self.wait_for_elem(wait_add_member)
        return MemberAction(self._driver)
    def goto_contact(self):
        # 点击通讯录
        self.find_elem(By.CSS_SELECTOR, '#menu_contacts > span').click()
        return MemberAction(self._driver)

