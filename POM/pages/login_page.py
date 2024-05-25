
from selenium.webdriver.common.by import By
from POM.pages.locators import LoginPageLocators as Locator
from POM.pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    """Inputs text into login textbox"""
    def input_username(self,username):
        self.driver.find_element(*Locator.USERNAME_TEXTBOX).send_keys(username)
    
    """Inputs text into login textbox"""
    def input_password(self,password):
        self.driver.find_element(*Locator.PASSWORD_TEXTBOX).send_keys(password)

    """Clicks on login button"""
    def click_login(self):
        self.driver.find_element(*Locator.LOGIN_BUTTON).click()
