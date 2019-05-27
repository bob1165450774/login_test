from selenium.webdriver.common.by import By


class PageElement:
    # 我的中心
    my_info_btn_id = (By.ID, "com.yunmall.lc:id/tab_me")

    # 已有账号,去登录
    go_to_login_id = (By.ID, "com.yunmall.lc:id/textView1")

    # 手机号注册
    phone_register_id = (By.ID, "com.yunmall.lc:id/register_button")

    # 账号输入框
    login_count_id = (By.ID, "com.yunmall.lc:id/logon_account_textview")

    # 密码输入框
    login_password_id = (By.ID, "com.yunmall.lc:id/logon_password_textview")

    # 登录按钮
    login_btn_id = (By.ID, "com.yunmall.lc:id/logon_button")

    # 设置按钮
    setting_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    # 账号设置
    count_setting_xpath = (By.XPATH, "//*[contains(@text,'账号设置')]")

    # 系统设置
    system_setting_xpath = (By.XPATH, "//*[contains(@text,'系统设置')]")

    # 退出按钮
    quit_btn_id = (By.ID, "com.yunmall.lc:id/setting_logout")

    # 确认退出
    confirm_quit_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")

    # 我的订单
    my_order_list_id = (By.ID, "com.yunmall.lc:id/order_txt")
