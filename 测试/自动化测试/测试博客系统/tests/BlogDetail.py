"""
测试博客详情页
"""
from selenium.webdriver.common.by import By

from common.Utils import BlogDriver

class BlogDetail:
    url = ""
    driver = ""
    def __init__(self):
        self.url = "http://8.137.19.140:9090/blog_detail.html?blogId=263456"
        self.driver = BlogDriver.driver
        self.driver.get(self.url)
        self.driver.implicitly_wait(3)
    # 登录状态下的博客详情页的测试
    def DetailTestByLogin(self):
        # 检查标题
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.right > div > div.title")
        # 检查时间
        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.right > div > div.date")
        # 检查内容
        self.driver.find_element(By.CSS_SELECTOR, "#h2-123")
        # 屏幕截图
        BlogDriver.getScreeShot()