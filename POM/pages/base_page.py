
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    """Returns True if an elment is visible"""
    def is_visible(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    """Opens URL"""
    def open_page(self, URL):
        self.driver.get(URL)

    """Clicks on given elment locator"""
    def click_on(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    """Waits for page to load a certain element"""
    def wait_for(self,by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator))
