import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver

class Addcustomer(BaseDriver):
    # cust_xpath = "//a[@class='nav-link active' and @href='#']"
    cust_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p/i"
    # cust_xpath ="//a[@class='nav-link active']/../ul"

    # customers_linktext = " Customers"
    customers_xp = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    addnew_xpath = "//a[@class='btn btn-primary']"
    cust_email_xp = "//input[@name='Email']"
    cust_password_xp ="//input[@name='Password']"
    cust_firstname_xp = "//input[@name='FirstName']"
    cust_lastname_xp = "//input[@name='LastName']"
    # gender_male_xp = "//input[@value='M']"
    # gender_female_xp = "//input[@value='F']"
    companyname_xp = "//input[@name='Company']"
    customer_role_xp ="//ul[@id='SelectedCustomerRoleIds_taglist']"
    save_xp = "//button[@name='save']"
    # success_msg_xp = "//div[@class='alert alert-success alert-dismissable']"
    success_msg_xp = "/html/body/div[3]/div[1]/div[1]"
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def gotocustomerspage(self):
        time.sleep(10)
        self.wait_until_element_is_clickable(By.XPATH, self.cust_xpath).click()
        self.wait_until_element_is_clickable(By.XPATH, self.customers_xp).click()

    def addcustomertopage(self,email,password,fname,lname,companyname):
        self.wait_until_element_is_clickable(By.XPATH,self.addnew_xpath).click()
        self.wait_until_element_is_clickable(By.XPATH,self.cust_email_xp).send_keys(email)
        self.wait_until_element_is_clickable(By.XPATH, self.cust_password_xp).send_keys(password)
        self.wait_until_element_is_clickable(By.XPATH, self.cust_firstname_xp).send_keys(fname)
        self.wait_until_element_is_clickable(By.XPATH, self.cust_lastname_xp).send_keys(lname)
        # self.wait_until_element_is_clickable(By.XPATH, self.gender_male_xp).send_keys(gender)
        self.wait_until_element_is_clickable(By.XPATH, self.companyname_xp).clear()
        self.wait_until_element_is_clickable(By.XPATH, self.companyname_xp).send_keys(companyname)
        # self.wait_until_element_is_clickable(By.XPATH, self.customer_role_xp).send_keys(customerrole)
        self.wait_until_element_is_clickable(By.XPATH, self.save_xp).click()


    def verifyaddcustomer(self):
        alert_msg = self.wait_until_element_is_clickable(By.XPATH,self.success_msg_xp)
        return alert_msg.text