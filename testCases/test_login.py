import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException

from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import Readconfig
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from base.BasePage import BasePage

class Test_001_login():
    baseURL = Readconfig.getApplicationURL()
    user = Readconfig.getUseremail()
    pwd = Readconfig.getPassword()
    logger = LogGen.loggen()

    def test_hometitle(self,setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        # self.driver.implicitly_wait(20)
        # return self.get_title(title)
        act_title =self.driver.title

        if act_title == "Your store. Login" :
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else :
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\test_hometitle.png")
            self.driver.close()
            assert False

    # @pytest.mark.xfail(raises=TimeoutException)
    # @staticmethod
    def test_login(self,setup):
        # with pytest.raises(TimeoutException) as excinfo:
        # with pytest.raises(TimeoutException) :
            self.driver = setup
            self.driver.get(self.baseURL)
            self.lp = LoginPage(self.driver)
                #time.sleep(10)
                # self.driver.implicitly_wait(10)

            # with pytest.raises(TimeoutException) as excinfo:
            self.lp.setUsername(self.user)
            #     print(excinfo)

            self.lp.setPassword(self.pwd)
            self.lp.btnlogin()
            print("login successfull")

            # act_title = self.driver.title
            # time.sleep(10)
            # self.lp.btnlogout()

            # if act_title == "Dashboard / nopCommerce administration" :
            #     self.driver.close()
            #     assert True
            #
            # else:
            #
            #    self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            #    self.driver.close()
            #    assert False

        # assert "element  not found " in str(excinfo.value)

    # except TimeoutException:
    #
    #    print("element not found")


