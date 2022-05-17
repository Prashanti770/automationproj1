from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium import webdriver

class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_sendkeys(self,by_locator,text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_elementext(self,by_locator):
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self,title):
        WebDriverWait(self.driver,10).until(EC.title_is(title))
        return self.driver.title



