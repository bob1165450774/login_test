from base.base import Base
from page.pageelement import PageElement


class QuitLogin(Base):

    def __init__(self, driver):
        self.driver = driver

    def quit_login(self):
        phone_register_text = self.get_element(PageElement.phone_register_id).text
        a = "手机号注册"
        if a != phone_register_text:
            self.click_element(PageElement.count_setting_xpath)
            self.drag_and_drop(self.get_element(PageElement.system_setting_xpath),
                               self.get_element(PageElement.count_setting_xpath))
            self.click_element(PageElement.quit_btn_id)
            self.click_element(PageElement.confirm_quit_id)
