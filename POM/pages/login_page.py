
from selenium.webdriver.common.by import By

class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.CSS_SELECTOR, "input.trn-input:nth-child(1)")
        self.password_textbox = (By.CSS_SELECTOR,'input.trn-input:nth-child(2)')
        self.login_button = (By.CSS_SELECTOR,"button.trn-button")

    def input_username(self,username):
        self.driver.find_element()