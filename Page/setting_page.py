from Base.Base import Base
import Page, allure

class Setting_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step(title="进入设置页面")
    def setting_page(self):
        # 点击设置按钮
        self.click_element(Page.person_setting_btn_id)

    @allure.step(title="退出登陆操作")
    def logout_page(self):
        # 退出登录
        try:
            # 点击安全退出
            self.click_element(Page.logout_btn_id)
            allure.attach("退出状态:", "成功")
        except Exception as e:
            allure.attach("退出状态:", "失败")
            allure.attach("失败原因:", "%s" % e)