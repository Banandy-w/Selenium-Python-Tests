import pytest, time
from selenium import webdriver
from POM.pages.login_page import LoginPage
from POM.pages.locators import LoginPageLocators as LPL
from POM.pages.locators import HomePageLocators as HPL
#from POM.conftest import init_driver_inLogin

"""Starts web browser"""
@pytest.fixture(scope='class')
def init_driver():
    driver = webdriver.Firefox()

    #Yield functions as a return but also code is executed after as a teardown
    yield driver
    print('Driver quitting in 5s')
    time.sleep(5)
    driver.quit()

"""Brings user to sign in page. We could also store the sign in page in a URL and direclty open it instead of clicking it"""
@pytest.fixture(scope='class')
def init_driver_inLogin(init_driver):
    driver = init_driver
    login_page = LoginPage(driver)
    login_page.open_page('https://tracker.gg/')
    login_page.click_on(HPL.SIGN_IN_ICON)

    yield login_page


class Test_Login():

    #decorator helps deal with fixture errors
    @pytest.fixture(autouse=True)
    def setup(self, init_driver_inLogin):
        self.driver = init_driver_inLogin
        self.loginPage = LoginPage(self.driver)

    #Fail
    def test_page_isVisible(self):
        assert self.loginPage.is_visible(LPL.LOGIN_BUTTON)
