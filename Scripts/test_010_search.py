import pytest
from Base.driver import Driver

from Base.page import Page

import logging


class TestSearch:

    def setup_class(self):
        # 点击搜索按钮
        Page.get_setting().click_search_btn()

    def teardown_class(self):
        """退出驱动"""
        Driver.quit_app_driver()

    # 添加数据
    @pytest.mark.parametrize("search_data, search_result", [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")])
    def test_search_data(self, search_data, search_result):
        """
        输入搜索内容 和 判断预期结果
        :param search_data: 搜索内容
        :param search_result: 预期结果
        :return:
        """
        logging.info("搜索测试用例: 搜索内容:{} --预期结果:{}".format(search_data, search_result))
        # 输入搜索内容
        Page.get_search().search_input_text(search_data)
        # 断言
        assert search_result in Page.get_search().search_result_value()
