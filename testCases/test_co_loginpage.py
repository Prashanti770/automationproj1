import time

import pytest

from utilities import ExcelUtility
from common_objects.commonobjects import co_commonobjects
from utilities.readProperties import Readconfig
from pageObjects.loginpage_1 import LoginPage_1


class Test_001_testlogin1():
    baseURL = Readconfig.getApplicationURL()
    # path = "C:\Prashanti M\Login2.xlsx"
    path = ".\\TestData\\Login4.xlsx"

    rows = ExcelUtility.getRowCount(path, 'Sheet1')

    @pytest.fixture(scope="function")
    def testlogin1(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        # self.lp = LoginPage_1(self.driver)

        for r in range(2, self.rows + 1):  # starts from 2 row

            username = ExcelUtility.readData(self.path, 'Sheet1', r, 1)
            password = ExcelUtility.readData(self.path, 'Sheet1', r, 2)
            exp = ExcelUtility.readData(self.path, 'Sheet1', r, 3)

            # self.lp.logindetails(username, password)
            # print("login successfull")
            act_title = self.driver.title
            # self.lp.btnlogout()
            time.sleep(5)
            lst_status = []  # empty variable to capture status
            expected_title = "Dashboard / nopCommerce administration"
            if act_title == expected_title:
                if exp == "Pass":
                    print("test is passed")
                    lst_status.append("Pass")
                    ExcelUtility.writeData(self.path, 'Sheet1', r, 4, "Pass")
                    ExcelUtility.writeData(self.path, 'Sheet1', r, 5, "test passed")
                    self.lp.logoutdetails()
                elif exp == "Fail":
                    print("test is Failed")
                    lst_status.append("Fail")
                    ExcelUtility.writeData(self.path, 'Sheet1', r, 4, "Fail")
                    ExcelUtility.writeData(self.path, 'Sheet1', r, 5, "test failed")
                    self.lp.logoutdetails()
            elif act_title != expected_title:
                if exp == "Pass":
                    print("test is passed")
                    lst_status.append("Fail")
                    ExcelUtility.writeData(self.path, 'Sheet1', r, 4, "Pass")
                    ExcelUtility.writeData(self.path, 'Sheet1', r, 5, "test failed")
                    self.lp.logoutdetails()
                elif exp == "Fail":
                    print("test is Failed")
                    lst_status.append("Pass")
                    ExcelUtility.writeData(self.path, 'Sheet1', r, 4, "Fail")
                    ExcelUtility.writeData(self.path, 'Sheet1', r, 5, "test passed")
                    self.lp.logoutdetails()


