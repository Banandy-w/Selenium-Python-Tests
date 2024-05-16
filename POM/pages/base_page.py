
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage():
    
    def __init__(self, driver):
        self.driver = driver

    """Returns True if an elment is visible"""
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    def open_page(self, URL):
        self.driver.get(URL)
class HomePage:
    ...

