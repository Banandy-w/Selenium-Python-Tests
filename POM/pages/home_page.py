
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from .locators import LoginPageLocators

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePage:
    ...

