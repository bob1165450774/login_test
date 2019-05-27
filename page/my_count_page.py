from base.base import Base
from page.pageelement import PageElement


class MyCountPage(Base):
    def __init__(self, driver):
        self.driver = driver

    def click_my_count_btn(self):
        self.click_element(PageElement.my_info_btn_id)
