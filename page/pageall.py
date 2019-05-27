from page.go_to_login import GoToLogin
from page.my_count_page import MyCountPage


class PageAll(object):
    def __init__(self, driver):
        self.driver = driver

    def get_my_count_page(self):
        return MyCountPage(self.driver)

    def get_go_to_page(self):
        return GoToLogin(self.driver)
