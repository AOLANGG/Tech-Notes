"""
博客首页测试用例
"""
import time

from selenium.webdriver.common.by import By

from common.Utils import BlogDriver
class BlogList:
    url = ""
    driver = ""
    def __init__(self):
        self.url = "http://8.137.19.140:9090/blog_list.html"
        self.driver = BlogDriver.driver
        self.driver.get(self.url)
        self.driver.implicitly_wait(3)
    # 测试首页（登录情况下）
    def ListTestByLogin(self):
        # 测试博客的标题是否存在
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.right > div:nth-child(1) > div.title")
        # 测试博客的内容是否存在
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.right > div:nth-child(1) > div.desc")
        # 测试按钮是否存在
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.right > div:nth-child(1) > a").click()

        # 个人信息-昵称是否存在
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.left > div > h3")
        # 添加屏幕截图
        BlogDriver.getScreeShot()
    # 测试首页（未登录的情况下）
    def ListTestByNoLogin(self):
        # 测试博客的标题是否存在
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.right > div:nth-child(1) > div.title")
        # 测试博客的内容是否存在
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.right > div:nth-child(1) > div.desc")
        # 测试按钮是否存在
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.right > div:nth-child(1) > a").click()

        # 个人信息-昵称是否存在
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.left > div > h3")
        # 添加屏幕截图
        BlogDriver.getScreeShot()
# list = BlogList()
# list.ListTestByLogin()