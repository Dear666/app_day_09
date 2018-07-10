from Page.login_page import Login_Page

from Page.setting_page import Setting_Page

class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_login_page(self):
        # 返回登陆页面对象
        return Login_Page(self.driver)

    def get_setting_page(self):
        # 返回设置页面对象
        return Setting_Page(self.driver)