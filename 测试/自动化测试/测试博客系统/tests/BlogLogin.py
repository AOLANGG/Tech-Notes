"""
测试博客登录页面
"""
import time

from selenium.webdriver.common.by import By

from common.Utils import BlogDriver

class BlogLogin:
    url = ""
    driver = ""
    def __init__(self):
        self.url = "http://8.137.19.140:9090/blog_login.html"
        self.driver = BlogDriver.driver
        self.driver.get(self.url)
        self.driver.implicitly_wait(2)
    # 成功登录的测试用例
    def LoginSuccTest(self):
        # #username
        self.driver.find_element(By.CSS_SELECTOR, "#username").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#password").clear()

        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("zhangsan")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()

        self.driver.find_element(By.CSS_SELECTOR, "body > div.container > div.left > div > h3")
        BlogDriver.getScreeShot()

    def LoginFailTest(self):
        # 输入正确的账号和错误的密码
        self.driver.find_element(By.CSS_SELECTOR, "#username").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#password").clear()

        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("zhangsan")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("1234567")
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()

        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()

# login = BlogLogin()
# login.LoginSuccTest()
# login.LoginFailTest()
