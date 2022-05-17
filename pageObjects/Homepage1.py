from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from base.BasePage import BasePage
from base.base_driver import BaseDriver

#Identify all the locators and create pageobjects
class Homepage1(BasePage):
    txt_username = (By.XPATH, "//input[@id='Email']")
    txt_password = (By.ID,"Password")
    btn_login = (By.XPATH,"//button[@class='button-1 login-button']")
    btn_logout = (By.LINK_TEXT,"Logout")

    def __init__(self, driver):
        super().__init__(driver)

    def get_pagetitle(self,title):
        return self.get_title(title)
    def dologin(self,username,password):
        self.do_sendkeys(self.txt_username, username)
        self.do_sendkeys(self.txt_password, password)
        self.do_click(self.btn_login)