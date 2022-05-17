from testCases.test_login import Test_001_login
from base.base_driver import BaseDriver

class co_commonobjects(BaseDriver):

    def __init__(self,driver):
        self.driver = driver


    def co_loginpage(self):
        lp = Test_001_login.test_login(self)
        return lp

    #     return self.lp
    # def co_addcustomer(self):
    #     ac = Addcustomerpage()
    #     return ac
