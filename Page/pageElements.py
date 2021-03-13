from selenium.webdriver.common.by import By


class PageElements:
    """管理所有页面元素"""
    # ---设置页面---
    # 搜索按钮
    setting_search_btn = (By.ID, "com.android.settings:id/search")

    # ---搜索页面---
    # 输入框
    search_input = (By.ID, "android:id/search_src_text")
    # 搜索结果
    search_result = (By.ID, "com.android.settings:id/title")





