from selenium.webdriver.support.wait import WebDriverWait


class Base(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=30, poll_frequency=2):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=30, poll_frequency=2):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=30, poll_frequency=2):
        self.get_element(loc, timeout, poll_frequency).click()

    def send_keys_element(self, loc, text, timeout=30, poll_frequency=2):
        input_text = self.get_element(loc, timeout, poll_frequency)
        input_text.clear()
        input_text.send_keys(text)

    def drag_and_drop(self, origin_el, destination_el):
        self.drag_and_drop(self.get_element(origin_el), self.get_element(destination_el))

    def get_assert_res(self, loc, timeout=30, poll_frequency=2):
        return self.get_element(loc, timeout, poll_frequency)
