from Base.base import Base
from Page.pageElements import PageElements
import logging


class SettingPage(Base):

    def __init__(self):
        super().__init__()
        logging.info("设置页面")

    def click_search_btn(self):
        """点击搜索按钮"""
        logging.info("点击搜索按钮")
        self.click_ele(PageElements.setting_search_btn)
