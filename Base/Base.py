from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time, allure

class Base:

    def __init__(self, driver):
        # 初始化driver -- 供find_element 和 find_elements使用
        self.driver = driver

    def search_element(self, loc, timeout=15, poll=1.0):
        """
        定位单个元素 - 显示等待
        :param loc: 元祖 (定位类型，类型属性值) 例子:(By.ID,"com.xx.xx")
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def search_elements(self, loc, timeout=15, poll=1):
        """
        定位单个元素 - 显示等待
        :param loc: 元祖 (定位类型，类型属性值) 例子:(By.ID,"com.xx.xx")
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc):
        """
        点击元素
        :param loc:
        :return:
        """
        self.search_element(loc).click()

    def input_element(self, loc, text):
        """
        输入内容
        :param loc:
        :param text: 输入的文本
        :return:
        """
        input_text = self.search_element(loc)
        input_text.clear()
        input_text.send_keys(text)

    def get_toast(self, message):
        # 获取提示消息
        try:
            xpath = "//*[contains(@text,'{}')]".format(message)
            toast_message = self.search_element((By.XPATH,xpath), timeout=5, poll=0.1)
            return toast_message.text
        except Exception as e:
            return False

    def get_screen(self):
        # 截图名字
        image_name = "./Screen/%d.png" % int(time.time())
        # 截图
        self.driver.get_screenshot_as_file(image_name)
        # 添加截图
        with open(image_name, "rb") as f:
            allure.attach("截图名字", f.read(), allure.attach_type.PNG)
