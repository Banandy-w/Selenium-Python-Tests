
from selenium.webdriver.common.by import By
from POM.pages.locators import LoginPageLocators as Locator
from POM.pages.home_page import BasePage

class LoginPage(BasePage):

    def input_username(self,username):
        self.driver.find_element(*Locator.USERNAME_TEXTBOX).send_keys(username)
    
    def input_password(self,password):
        self.driver.find_element(*Locator.PASSWORD_TEXTBOX).send_keys(password)

    def click_login(self):
        self.driver.find_element(*Locator.LOGIN_BUTTON).click()