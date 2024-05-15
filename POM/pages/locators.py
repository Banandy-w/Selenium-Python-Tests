from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    username_textbox = (By.CSS_SELECTOR, "input.trn-input:nth-child(1)")
    password_textbox = (By.CSS_SELECTOR,'input.trn-input:nth-child(2)')
    login_button = (By.CSS_SELECTOR,"button.trn-button")

