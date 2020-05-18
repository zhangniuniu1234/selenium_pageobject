
from selenium_wework.selenium_wework_main.main import Main
from selenium_wework.selenium_wework_main.member_action import MemberAction


class TestMember:

    def setup(self):
        self.main = Main()


    # def teardown(self):
    #     self.main.driver.quit()

    def test_add_member(self):
        self.main.goto_add_member().add_member()

    def test_exist_member(self):
        assert self.main.goto_contact().find_member("15060102131")

    def test_delete_member(self):
        self.main.goto_contact().delete_member('1111')