from selenium.webdriver.common.by import By

"""Holds static data of locators necessary for testing"""
class LoginPageLocators():
    USERNAME_TEXTBOX = (By.CSS_SELECTOR, "input.trn-input:nth-child(1)")
    PASSWORD_TEXTBOX = (By.CSS_SELECTOR,'input.trn-input:nth-child(2)')
    LOGIN_BUTTON = (By.CSS_SELECTOR,"button.trn-button")
    USER_ICON = (By.CLASS_NAME, 'trn-game-bar-user')
    INVALID_BANNER = (By.CSS_SELECTOR, '.trn-alert-banner')

class HomePageLocators():
    SIGN_IN_ICON = (By.CSS_SELECTOR,'.trn-game-bar-auth')
    BASE_URL = 'https://tracker.gg/'
