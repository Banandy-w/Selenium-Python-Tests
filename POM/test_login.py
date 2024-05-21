import pytest
from POM.pages.login_page import LoginPage
from POM.pages.locators import LoginPageLocators as LPL
from POM.pages.locators import HomePageLocators as HPL


class Test_Login():

    #decorator helps deal with fixture errors
    @pytest.fixture(autouse=True)
    def setup(self, init_driver_inLogin):
        self.driver = init_driver_inLogin
        self.loginPage = LoginPage(self.driver)
        print("Test Login Driver setup complete")

    
    def test_login_01_isVisible(self):
        print("Test Login_01 starting")
        assert self.loginPage.is_visible(LPL.LOGIN_BUTTON)

    def test_login_02_success(self):
        pass

    

