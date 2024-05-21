import pytest, os, time
from dotenv import load_dotenv
from POM.pages.login_page import LoginPage
from POM.pages.locators import LoginPageLocators as LoginLocator

load_dotenv()
userName = os.getenv("USER")
password = os.getenv("PASSWORD")

class Test_Login():

    #decorator helps deal with fixture errors
    @pytest.fixture(autouse=True)
    def setup(self, init_driver_inLogin):
        self.driver = init_driver_inLogin
        self.loginPage = LoginPage(self.driver)
        print("Test Login Driver setup complete")

    
    def test_login_01_isVisible(self):
        print("Test Login_01 Page is Visible starting")
        assert self.loginPage.is_visible(LoginLocator.LOGIN_BUTTON)
        print("Test Login_01 Page is Visible completed")

    def test_login_02_success(self):
        print("Test Login_02 success is starting")

        print("Waiting for cloudflare to load")
        time.sleep(2)

        print('Entering Username and Password')
        self.loginPage.input_username(userName)
        self.loginPage.input_password(password)

        print('Clicking on login')
        self.loginPage.click_login()
        assert self.loginPage.is_visible(LoginLocator.USER_ICON)
        print("Test Login_02 Success completed")
    

