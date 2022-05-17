from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver

#Identify all the locators and create pageobjects
class LoginPage_1(BaseDriver):
    Link = "Customers"
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
    def logindetails(self,username,password):

       self.wait_until_element_is_clickable(By.XPATH, self.txtbox_username_xpath).clear()
       self.wait_until_element_is_clickable(By.XPATH, self.txtbox_username_xpath).send_keys(username)
       self.wait_until_element_is_clickable(By.ID,self.txtbox_password_id).clear()
       self.wait_until_element_is_clickable(By.ID, self.txtbox_password_id).send_keys(password)
       self.wait_until_element_is_clickable(By.XPATH,self.btn_login_xpath).click()

    def logoutdetails(self):

        self.wait_until_element_is_clickable(By.LINK_TEXT, self.btn_logout_ltext).click()
    # def addcust(self):
    #     self.wait_until_element_is_clickable(By.LINK_TEXT,self.Link).click()