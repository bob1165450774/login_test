import pytest

from base.getData import get_data1
from base.getDriver import GetDriver
from page.pageall import PageAll


def get_data():
    # with open("C:\\Users\\bob1994\\Desktop\\aolai\\data\\count_pwd.yaml", "r", encoding="utf-8") as f:
    data_list = []
    data = get_data1().get_data("count_pwd.yaml").get("TestLoginData")
    for i in data.values():
        data_list.append((i.get("count"), i.get("pwd")))
    return data_list


class TestLogin(object):

    def setup_class(self):
        self.driver = GetDriver().get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        self.page = PageAll(self.driver)

    def teardown_class(self):
        self.driver.quit()

    # def setup(self):
    #     QuitLogin.quit_login(self.driver)

    @pytest.mark.parametrize("count,pwd", get_data())
    def test_login(self, count, pwd):
        self.page.get_my_count_page().click_my_count_btn()
        self.page.get_go_to_page().go_to_login(count, pwd)
        assert "我的订单" in self.page.get_go_to_page().get_assert_res().text
