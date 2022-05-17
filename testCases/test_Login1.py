import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from base.BasePage import BasePage
from pageObjects.Homepage1 import Homepage1

class Test_001_login(BasePage):


    def test_logintitle(self):
        self.Homepage1 = Homepage1(self.driver)
        title = self.Homepage1.get_title()

    def test_login(self):
        self.Homepage1=Homepage1(self.driver)
        self.Homepage1.dologin(self.user,self.pwd)

