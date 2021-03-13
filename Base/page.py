from Page.settingPage import SettingPage
from Page.searchPage import SearchPage


class Page:

    @classmethod
    def get_setting(cls):
        """返回设置页面对象"""
        return SettingPage()

    @classmethod
    def get_search(cls):
        """返回显示页面实例化对象"""
        return SearchPage()
