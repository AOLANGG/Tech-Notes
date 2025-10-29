from tests import BlogList
from tests import BlogLogin
from tests import BlogDetail
from tests import BlogEdit

from common.Utils import BlogDriver

if __name__ == "__main__":
    BlogLogin.BlogLogin().LoginFailTest()
    BlogLogin.BlogLogin().LoginSuccTest()
    # 登录成功之后就可以调用博客首页的用例
    BlogList.BlogList().ListTestByLogin()
    BlogDetail.BlogDetail().DetailTestByLogin()
    # 测试博客编辑页面
    BlogEdit.BlogEdit().EditSucTestByLogin()
    BlogDriver.driver.quit()