from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    USERNAME_TEXTBOX = (By.CSS_SELECTOR, "input.trn-input:nth-child(1)")
    PASSWORD_TEXTBOX = (By.CSS_SELECTOR,'input.trn-input:nth-child(2)')
    LOGIN_BUTTON = (By.CSS_SELECTOR,"button.trn-button")

