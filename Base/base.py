from selenium.webdriver.support.wait import WebDriverWait
from Base.driver import Driver
import logging


class Base:

    def __init__(self):
        # 赋值自定义声明driver
        self.driver = Driver.get_app_driver()

    def search_ele(self, loc, timeout=5, poll=1.0):
        """
        定位单个元素
        :param loc: 元组 (By.ID,属性值) (By.XPATH,属性值) (By.CSS,属性值)...
        :param timeout: 搜索元素超时时间
        :param poll: 搜索元素间隔时间
        :return: 定位对象
        """
        logging.info("操作元素:{}".format(loc))
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll=1.0):
        """
        定位一组元素
        :param loc: 元组 (By.ID,属性值) (By.XPATH,属性值) (By.CSS,属性值)...
        :param timeout: 搜索元素超时时间
        :param poll: 搜索元素间隔时间
        :return: 定位对象列表
        """
        logging.info("操作一组元素:{}".format(loc))
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll=1.0):
        """
        点击元素
        :param loc: 元组 (By.ID,属性值) (By.XPATH,属性值) (By.CSS,属性值)....
        :param timeout: 搜索元素超时时间
        :param poll: 搜索元素间隔时间
        :return:
        """
        logging.info("执行点击操作")
        self.search_ele(loc, timeout, poll).click()

    def send_ele(self, loc, text, timeout=5, poll=1.0):
        """
        输入框输入内容
        :param loc: 元组 (By.ID,属性值) (By.XPATH,属性值) (By.CSS,属性值)....
        :param text: 输入文本
        :param timeout: 搜索元素超时时间
        :param poll: 搜索元素间隔时间
        :return:
        """
        logging.info("执行输入动作，输入内容为:{}".format(text))
        # 定位
        input_text = self.search_ele(loc, timeout, poll)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)
