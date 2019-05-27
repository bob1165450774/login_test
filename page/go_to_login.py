from base.base import Base
from page.pageelement import PageElement


class GoToLogin(Base):
    def __init__(self, driver):
        self.driver = driver

    def go_to_login(self, count, pwd):
        self.click_element(PageElement.go_to_login_id)
        self.send_keys_element(PageElement.login_count_id, count)
        self.send_keys_element(PageElement.login_password_id, pwd)
        self.click_element(PageElement.login_btn_id)

    def get_assert_res(self):
        return self.get_element(PageElement.my_order_list_id)
