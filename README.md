# Creating test suites with automation
Mainly this project is to get an understanding of automation to improve my skillset as a QA Engineer

## Summary
In this project, I explore automation test case creation by first using a basicm but fundamental feature that will help enable learning the basics of selenium also. In this case I chose the login feature. By doing so I learn navigation and best practices for waiting and interacting with elements that have yet to be loaded. Ultimately, I want to create a test suite for more than one feature, so the design pattern of a [page object model](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models)(POM) was needed to write tests in a sustainable and scalable fashion. Hopefully when the POM is implemented, writing test cases/suites in pytest should become a simple matter.

## Journey Overview WIP

I needed a functioning product with data that interests me. Naturally gravitated towards gaming so I chose <https://tracker.gg/> which is a website that tracks performance across various competitive online games. Second, test a feature that every user would probalby use but isn't too complicated to get our feet wet with automation. I decided login with navigation instead of directly openning to the login page. 
<details>
  <summary>Here's our first basic iteration of logging in with selenium with <a href="https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/manual_login.py"> manual_login.py</a></summary>
  <br>
  
  
  ```python

import time, os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

load_dotenv()
userName = os.getenv("USER")
password = os.getenv("PASSWORD")

# Step 1 Navigate to tracker.gg
## We can definitely just open the login page directly but I want to explore the navigation functionality of selenium
print('Openning firefox on page tracker.gg')
driver = webdriver.Firefox()
driver.get('https://tracker.gg/')


# Step 2 Select login and click on it
print('Scanning for login element')
element = driver.find_element(By.CSS_SELECTOR,'.trn-game-bar-auth')
element.send_keys(Keys.RETURN)


# Driver doesn't wait for page to load so need to learn how to wait until element appears
# Step 3 Wait for page to load
wait = WebDriverWait(driver, 15)
print("Waiting for page to load")
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.trn-input:nth-child(1)")))


# Step 4 Entering login data
# Need to wait for cloudflare to finish loading before we can enter the information
# Using sleep isn't best practice in terms of automation but cloudflare seems to be made to prevent bot purposes like this. As the following doesn't work
#wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'success-circle')))
print("Waiting for cloudflare to load")
time.sleep(2)


print('Entering Username and Password')
element.send_keys(userName)
element = driver.find_element(By.CSS_SELECTOR,'input.trn-input:nth-child(2)').send_keys(password,Keys.RETURN)

# Step 5 Verify login was successful
# Verify by checking user icon element
# Note to self: maybe a more surefire way maybe would be to use cookies. 
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'trn-game-bar-user')))
    element = driver.find_element(By.CSS_SELECTOR, '.trn-game-bar-user__container')
except TimeoutException:
    print('Test failed due to timeout. Likely due to cloudflare')
except NoSuchElementException:
    print('Test Failed. User is not logged in')
else:
    print('Success! Signed in. Browser will now close in 5s')
    time.sleep(5)
    driver.quit()
  ```
</details>

**After** the POM implementation and excluding some set up in pytest, the login test case looks much more succint and readable.


<details>
  <summary>Check out the final product here in <a href=https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/POM/tests/test_login.py>test_login.py</a> or part of it in this dropdown</summary>
  <br>

  There's some pytest magic in conftest.py file which sets up the browser, but aside from that, the method test_login_02_success essentially does what our prior code does.
  ```python
class Test_Login():

    @pytest.fixture(autouse=True)
    def setup(self, init_driver_inLogin):
        self.driver = init_driver_inLogin
        self.loginPage = LoginPage(self.driver)
        print('Test Login Driver setup complete')


    """Basic tests for login success"""
    def test_login_02_success(self):
        print('Test Login_02_success is starting')

        print('Waiting for cloudflare to load')
        time.sleep(2)

        print('Entering Username and Password')
        self.loginPage.input_username(userName)
        self.loginPage.input_password(password)

        print('Clicking on login')
        self.loginPage.click_login()
        assert self.loginPage.is_visible(LoginLocator.USER_ICON)
        print('Verifying user is logged in')
        print('Test Login_02_success completed')

        
  ```
</details>

### POM Implementation
Writing more tests in a scaleable fashion required the implementation of a POM or [page object model](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models). We only need to implement what's needed for our tests to function
which lead to the creation of the following files. *Note that the dropdown may not be as updated as the URL shown, but should atleast represent the elements necessary for that page.*
<details>
  <summary>A <a href=https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/POM/pages/base_page.py>base_page.py</a> that holds the basic functionality of the web page. All other pages should inherit from this class.</summary>
  <br>
  
  ```python
  
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

        
  ```
</details>

Our locators which help us interact with the elements of the webpage are all *located* heh, in this file. Keeping all the locators in one place allows for us to adapt to any changes possibly done to the website by changing it here.
<details>
  <summary><a href=https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/POM/pages/login_page.py>locators.py</a></summary>
  <br>
  
  ```python
from selenium.webdriver.common.by import By

"""Holds static data of locators necessary for testing"""
class LoginPageLocators():
    USERNAME_TEXTBOX = (By.CSS_SELECTOR, "input.trn-input:nth-child(1)")
    PASSWORD_TEXTBOX = (By.CSS_SELECTOR,'input.trn-input:nth-child(2)')
    LOGIN_BUTTON = (By.CSS_SELECTOR,"button.trn-button")
    USER_ICON = (By.CLASS_NAME, 'trn-game-bar-user')

class HomePageLocators():
    SIGN_IN_ICON = (By.CSS_SELECTOR,'.trn-game-bar-auth')
    BASE_URL = 'https://tracker.gg/'
        
  ```
</details>

With the locators encapsulated as class variables and some basic webpage functionality in base_page. I finally encapsulate the essence of what one would do in a login page into methods here:
<br>

<details>
  <summary><a href=https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/POM/pages/login_page.py>login_page.py</a></summary>
  <br>
  
  ```python

from selenium.webdriver.common.by import By
from POM.pages.locators import LoginPageLocators as Locator
from POM.pages.base_page import BasePage

class LoginPage(BasePage, Locator):

    def __init__(self,driver):
        super().__init__(driver)

    """Inputs text into login textbox"""
    def input_username(self,username):
        self.driver.find_element(*Locator.USERNAME_TEXTBOX).send_keys(username)
    
    """Inputs text into login textbox"""
    def input_password(self,password):
        self.driver.find_element(*Locator.PASSWORD_TEXTBOX).send_keys(password)

    """Clicks on login button"""
    def click_login(self):
        self.driver.find_element(*Locator.LOGIN_BUTTON).click()
        
  ```
</details>



### Pytest WIP
Now for pytest we have the [conftest.py](https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/POM/tests/conftest.py) which has the code to set up pre-reqs in testing and [test_login.py](https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/POM/tests/test_login.py) that will test everything related to login.

## Conclusions WIP
In hindsight, I liked the idea of having all the locators in one file/class but it might've been easier to put the locator variables into their respective classes as class variables. Definitely would be more read-able since it wouldn't need as much importing. I am imagining that when testing more features, it will be more readable to have all the locators in one file.

## Next Steps
- [ ] Write more test cases that attack the login feature differently.
- [ ] Expand POM for another slightly more complicated feature that should also expand our understanding of Selenium. Likely considering Search
- [ ] Implement the tests for multiple browsers


# Try this for yourself!
## Requirements / Prereqs
* [Mozilla browser](https://www.mozilla.org/en-US/firefox/new/)
* Download [Geckodriver](https://github.com/mozilla/geckodriver/releases) and note the path to Geckdriver
* Make a dummy test account at https://tracker.gg/
## Code dependecies
~~~
pip install selenium
~~~
https://selenium-python.readthedocs.io/
~~~
pip install python-dotenv
~~~
https://github.com/theskumar/python-dotenv
~~~
pip install pytest
~~~
## Setting up and trying the code
1. Get the files
~~~
 git clone your_forked_repository_url.git
 ~~~
2. Move terminal into the cloned files then rename example.env to .env
 ~~~
 cd .\Selenium-Python-Tests\
 ~~~
 ~~~
 mv example.env .env
 ~~~
3. In the .env file, change the values to the right of USER and PASSWORD into your account at https://tracker.gg/ with no spaces.
4. In the .env file, change the value to FIREFOX_DRIVER_PATH= to the path of your Geckodriver installation location. E.G with quotes FIREFOX_DRIVER_PATH="C:\Projects\Selenium\geckdriver"
5. Move Terminal to POM>tests folder
~~~
cd .\POM\tests\
~~~
6. Execute the tests by entering the following while terminal is in tests folder
~~~
pytest .\test_login.py
~~~

# References
Documentation
* https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/
* https://selenium-python.readthedocs.io/
* https://www.geeksforgeeks.org/selenium-python-introduction-and-installation/

Tutorials
* https://www.colibri-software.com/2021/07/page-object-model-pom-in-selenium-using-python/
* https://www.youtube.com/watch?v=P9ZWOWm7i0k
* https://www.youtube.com/watch?v=0kHbK5iZkN0
* https://www.youtube.com/watch?v=qBK5I_QApCg

