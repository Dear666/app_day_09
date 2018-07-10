from Base.Base import Base
import Page, allure

class Login_Page(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step(title="点击我的按钮")
    def click_my_btn(self):
        # 点击我的按钮
        self.click_element(Page.my_btn_xpath)

    @allure.step(title="点击登陆注册按钮")
    def click_login_sign_btn(self):
        # 点击登陆注册
        self.click_element(Page.login_sing_btn_id)

    @allure.step(title="输入用户信息")
    def login_input_page(self, username, passwd):
        # 登陆操作
        allure.attach("用户登陆信息：","用户名:%s\n密码:%s" % (username, passwd))
        # 输入用户名
        self.input_element(Page.login_name_id, username)
        # 输入密码
        self.input_element(Page.login_pwd_id, passwd)
        # 点击登陆按钮
        self.click_element(Page.login_btn_id)

    @allure.step(title="判断我的订单是否存在")
    def if_my_order_status(self):
        # 判断我的订单按钮是否存在
        try:
            self.search_element(Page.my_order_btn)
            allure.attach("状态","找到")
            return True
        except Exception as e:
            allure.attach("状态", "未找到")
            return False

    @allure.step(title="关闭登陆信息页面")
    def login_close_page(self):
        try:
            # 关闭登陆信息输入页
            self.click_element(Page.login_close_page_id)
            allure.attach("关闭状态:", "成功")
        except Exception as e:
            allure.attach("关闭状态:","失败")
            allure.attach("关闭失败原因:", "%s" % e)


