from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from base.BasePage import BasePage
from base.base_driver import BaseDriver

#Identify all the locators and create pageobjects
class LoginPage(BaseDriver):
    #Locators
    # txt_username = (By.XPATH, "//input[@id='Email']")
    # txt_password = (By.ID,"Password")
    # btn_login = (By.XPATH,"//button[@class='button-1 login-button']")
    # btn_logout = (By.LINK_TEXT,"Logout")

    txtbox_username_xpath="//input[@id='Email']"
    txtbox_password_id="Password"
    btn_login_xpath="//button[@class='button-1 login-button']"
    btn_logout_ltext="Logout"

#initiate Driver
    #to access class variables we use self variable
    def __init__(self,driver):
        super().__init__(driver)
        self.driver =driver


#create action methods for the locators
    def setUsername(self,username):
        # self.do_sendkeys(self.txt_username).clear()
        # self.do_sendkeys(self.txt_username,username)
       #
       # self.driver.find_element(By.XPATH,self.txtbox_username_xpath).clear()
       # self.driver.find_element(By.XPATH,self.txtbox_username_xpath).send_keys(username)
       #  self.driver.wait_for_presence_of_all_elements(By.XPATH,self.txtbox_username_xpath).clear()
       #  return self.wait_until_element_is_clickable(By.XPATH, self.txtbox_username_xpath)
       self.wait_until_element_is_clickable(By.XPATH, self.txtbox_username_xpath).clear()
       self.wait_until_element_is_clickable(By.XPATH, self.txtbox_username_xpath).send_keys(username)

       # except TimeoutException:
       #       print("element not found")

    # def username_set(self,username):
    #     self.setUsername().clear()
    #     self.setUsername().send_keys(username)
    #
    #     self.setUsername().send_keys(Keys.ENTER)

    def setPassword(self,password):
        # self.do_sendkeys(self.txt_password).clear()
        # self.do_sendkeys(self.txt_password,password)

        # self.driver.find_element(By.ID,self.txtbox_password_id).clear()
        # self.driver.find_element(By.ID,self.txtbox_password_id).send_keys(password)
          self.wait_until_element_is_clickable(By.ID,self.txtbox_password_id).clear()

          self.wait_until_element_is_clickable(By.ID, self.txtbox_password_id).send_keys(password)

    def btnlogin(self):
        # self.do_click(self.btnlogin())
        # self.driver.find_element(By.XPATH,self.btn_login_xpath).click()
        self.wait_until_element_is_clickable(By.XPATH,self.btn_login_xpath).click()

    def btnlogout(self):
        # self.do_click(self.btnlogout())
        self.driver.find_element(By.LINK_TEXT,self.btn_logout_ltext).click()
        # self.wait_until_element_is_clickable(By.LINK_TEXT, self.btn_logout_ltext).click()
