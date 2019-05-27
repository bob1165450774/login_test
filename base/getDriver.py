from appium import webdriver


class GetDriver(object):

    def get_driver(self, pac, act):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = pac
        desired_caps['appActivity'] = act

        # app在手机中没有使用过
        desired_caps['noReset'] = 'false'
        # 声明driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return self.driver
