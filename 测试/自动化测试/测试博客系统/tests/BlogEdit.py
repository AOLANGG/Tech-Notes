"""
测试博客编辑页面
"""
import time

from selenium.webdriver.common.by import By

from common.Utils import BlogDriver

class BlogEdit:
    url = ""
    driver = ""
    def __init__(self):
        self.url = "http://8.137.19.140:9090/blog_edit.html"
        self.driver = BlogDriver.driver
        self.driver.get(self.url)
        self.driver.implicitly_wait(3)
    # 正确发布博客（登录状态下）
    def EditSucTestByLogin(self):
        self.driver.find_element(By.CSS_SELECTOR, "#title").send_keys("27号自动化测试标题")
        self.driver.find_element(By.CSS_SELECTOR, "#editor > div.editormd-toolbar > div > ul > li:nth-child(21) > a > i").click()
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        time.sleep(2)
        BlogDriver.getScreeShot()
