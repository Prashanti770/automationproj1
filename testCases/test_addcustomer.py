import time

import pytest
from selenium.webdriver.common.by import By

from testCases.testlogin1 import Test_001_testlogin1
from utilities import ExcelUtility

from utilities.readProperties import Readconfig
from pageObjects.Addcustomerpage import Addcustomer
from testCases.test_login import Test_001_login
from common_objects.commonobjects import co_commonobjects

# @pytest.mark.usefixtures("testlogin1")
# class Test_002_addcustomer(Test_001_testlogin1):
class Test_002_addcustomer:
    # co_lp = co_commonobjects.co_loginpage()
    baseURL = Readconfig.getApplicationURL()
    cust_path = ".\\TestData\\customers_1.xlsx"

    cust_rows = ExcelUtility.getRowCount(cust_path, 'Sheet1')

    expected_msg = """×
The new customer has been added successfully."""

    def test_addcustomers(self):
        # self.driver = setup
        # self.driver.get(self.baseURL)

        # Test_001_login.test_login(self, setup)
        co_commonobjects.co_loginpage(self)
        # self.co_lp(self)
        self.ac = Addcustomer(self.driver)

        for r in range(2, self.cust_rows + 1):  # starts from 2 row
            self.ac.gotocustomerspage()
            email = ExcelUtility.readData(self.cust_path, 'Sheet1', r, 1)
            password = ExcelUtility.readData(self.cust_path, 'Sheet1', r, 2)
            firstname = ExcelUtility.readData(self.cust_path, 'Sheet1', r, 3)
            lastname = ExcelUtility.readData(self.cust_path, 'Sheet1', r, 4)
            gender = ExcelUtility.readData(self.cust_path, 'Sheet1', r, 5)
            company_name = ExcelUtility.readData(self.cust_path, 'Sheet1', r,6)
                # customers_role = ExcelUtility.readData(self.cust_path, 'Sheet1', r,7)
            self.ac.addcustomertopage(email,password,firstname,lastname,gender,company_name)

            succ_msg = self.ac.verifyaddcustomer()

                # succ_msg = self.driver.find_element(By.TAG_NAME, "body").text
            print(succ_msg)


                # expected_msg = "×
                #                The new customer has been added successfully."

            if succ_msg == self.expected_msg :
                # if " The new customer has been added successfully." in succ_msg :
                print("customer added successfully")
                ExcelUtility.writeData(self.cust_path, 'Sheet1', r, 8, "Customer added success fully")
                ExcelUtility.writeData(self.cust_path, 'Sheet1', r, 9, "test passed")

            else:
                 print("Error/ not added")
                 ExcelUtility.writeData(self.cust_path, 'Sheet1', r, 8, "Error/Invalid data")
                 ExcelUtility.writeData(self.cust_path, 'Sheet1', r, 9, "test failed")

                # ExcelUtility.writeData(self.cust_path, 'Sheet1', r,8,succ_msg)




