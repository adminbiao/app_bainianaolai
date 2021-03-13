from Base.base import Base
from Page.pageElements import PageElements
import logging


class SearchPage(Base):

    def __init__(self):
        super().__init__()
        logging.info("搜索页面")

    def search_input_text(self, text):
        """
        输入搜索内容
        :param text: 输入搜索文本内容
        :return:
        """
        logging.info("输入搜索内容")
        self.send_ele(PageElements.search_input, text)

    def search_result_value(self):
        """获取搜索结果"""
        logging.info("获取搜索结果")
        res = self.search_eles(PageElements.search_result)
        value = [i.text for i in res]
        logging.info("获取的结果为:{}".format(value))
        return value
