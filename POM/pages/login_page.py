
from selenium.webdriver.common.by import By
from locators import LoginPageLocators as Locator

class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.CSS_SELECTOR, "input.trn-input:nth-child(1)")
        self.password_textbox = (By.CSS_SELECTOR,'input.trn-input:nth-child(2)')
        self.login_button = (By.CSS_SELECTOR,"button.trn-button")

    def input_username(self,username):
        self.driver.find_element(*Locator.USERNAME_TEXTBOX).send_keys(username)
    
    def input_password(self,password):
        self.driver.find_element(*Locator.PASSWORD_TEXTBOX).send_keys(password)

    def click_login(self):
        self.driver.find_element(*Locator.LOGIN_BUTTON).click()