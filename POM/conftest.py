import pytest, time, os
from selenium import webdriver
from POM.pages.login_page import LoginPage
from POM.pages.locators import LoginPageLocators as LPL
from POM.pages.locators import HomePageLocators as HomePage

"""Starts web browser"""
@pytest.fixture(scope='class')
def init_driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    print("Driver started")

    #Yield functions as a return but also code is executed after as a teardown
    yield driver
    print('Driver quitting in 5s')
    time.sleep(5)
    driver.quit()
    print("Webpage is closed")

"""Brings user to sign in page. We could also store the sign in page in a URL and direclty open it instead of clicking it"""
@pytest.fixture(scope='class')
def init_driver_inLogin(init_driver):
    driver = init_driver
    login_page = LoginPage(driver)
    login_page.open_page(HomePage.BASE_URL)
    print("Navigated to webpage")
    login_page.click_on(HomePage.SIGN_IN_ICON)
    print("Navigated to login page")

    yield driver
