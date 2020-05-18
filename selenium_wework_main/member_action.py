

from selenium.webdriver.common.by import By


from selenium_wework.common_utils.basepage import BasePage


class MemberAction(BasePage):


    def add_member(self):
        self.find_elem(By.ID, 'username').send_keys("zhangyang9")
        self.find_elem(By.ID, 'memberAdd_acctid').send_keys("29")
        self.find_elem(By.ID, 'memberAdd_phone').send_keys('15709247820')
        self.find_elem(By.CSS_SELECTOR,'.js_btn_save').click()


    def update_page(self):
        page : str=self.find_elem(By.CSS_SELECTOR,'.ww_pageNav_info_text').text
        print(page)
        return [int(x) for x in page.split('/',1)]

    def find_member(self,value: str):
        self.wait_for_elemclick((By.CSS_SELECTOR,'.ww_checkbox'))
        cur_page,total_page = self.update_page()

        global delete_elem
        while True:
            elems=self.finds_elem(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')

            for elem in elems:
                if value==elem.get_attribute('title'):
                    delete_elem=elem
                    return delete_elem

            cur_page=self.update_page()[0]
            if cur_page == total_page:
                print("该元素不存在")
                return False
            self.find_elem(By.CSS_SELECTOR, '.js_next_page').click()



    def delete_member(self,value):
        if(self.find_member(value)):
            delete_elem_box=self.find_member(value)
            delete_elem_box.click()
            self.find_elem(By.CSS_SELECTOR,'.js_del_member').click()
            self.find_elem(By.CSS_SELECTOR,'#__dialog__MNDialog__>div:nth-child(1)>div:nth-child(3)>a:nth-child(1)').click()
            print('删除{}成功'.format(value))

        else:
            print("您要删除的元素不存在")









