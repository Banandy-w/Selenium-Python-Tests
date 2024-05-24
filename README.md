# Learning Automation with Selenium Python
Mainly this project is to get an understanding of automation to improve my skillset as a QA Engineer

## Summary
In this project, I explore automation test case creation by first using a basicm but fundamental feature that will help enable learning the basics of selenium also. In this case I chose the login feature. By doing so I learn navigation and best practices for waiting and interacting with elements that have yet to be loaded. Ultimately, I want to create a test suite for more than one feature, so the design pattern of a [page object model](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models)(POM) was needed to write tests in a sustainable and scalable fashion. Hopefully when the POM is implemented, writing test cases/suites in pytest should become a simple matter.

## Journey Overview WIP
First I needed a functioning product with data that interests me. Naturally gravitated towards gaming so I chose <https://tracker.gg/> which is a website that tracks performance across various competitive online games. Second, test a feature that every user would probalby use but isn't too complicated to get our feet wet with automation. I decided login with navigation instead of directly openning to the login page. 
<details>
  <summary>Here's our first basic iteration of logging in with selenium with <a href="https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/manual_login.py"> manual_login.py</a></summary>
  <br>
  
  
  ```python
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

Some rodebumps, preserving our data privacy was solved by using [dotenv](https://github.com/theskumar/python-dotenv) and cloudflare was worked around using time.sleep()

Writing more tests in a scaleable fashion required the implementation of a POM or [page object model](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models) which lead to the creation of the following:
* [base_page.py](https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/POM/pages/base_page.py) which should have some basic functions of navigating a webpage
* [locators.py](https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/POM/pages/locators.py) has locators of all necessary elements for testing
* And [login_page.py](https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/POM/pages/login_page.py) which encapsulates functions of the login page into methods. 

In hindsight, I liked the idea of having all the locators in one file/class but it might've been easier to put the locator variables into their respective classes as class variables. Definitely would be more read-able since it wouldn't need as much importing. I am imagining that when testing more features, it will be more readable to have all the locators in one file.

Next, to make sure the POM implementation was working correctly, I incrementally replaced functions from [manual_login](https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/manual_login.py) which lead to [login.py](https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/login.py) After verifying the POM implementation works,  we just needed to implement the testing in pytest.
* Now for pytest we have the [conftest.py](https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/POM/tests/conftest.py) which has the code to set up pre-reqs in testing and [test_login.py](https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/POM/tests/test_login.py) that will test everything related to login.


Lastly is to write more tests for login and different features to and watch the POM scale

# Conclusions
# Next Steps
- [ ] Write more test cases that attack the login feature differently.
- [ ] Expand POM for another slightly more complicated feature that should also expand our understanding of Selenium. Likely considering Search


# Installation to try the code
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
3. Move terminal into the cloned files then rename example.env to .env
 ~~~
 cd .\Selenium-Python-Tests\
 ~~~
 ~~~
 mv example.env .env
 ~~~
4. In the .env file, change the values to the right of USER and PASSWORD into your account at https://tracker.gg/ with no spaces.
5. In the .env file, change the value to FIREFOX_DRIVER_PATH= to the path of your Geckodriver installation location. E.G with quotes FIREFOX_DRIVER_PATH="C:\Projects\Selenium\geckdriver"
6. Move Terminal to POM>tests folder
~~~
cd .\POM\tests\
~~~
7. Execute the tests by entering the following while terminal is in tests folder
~~~
pytest .\test_login.py
~~~

## Timeline / Roadmap
- [x] Code a script using Selenium to test a random website. Tracker.gg was chosen and the function to script is login.
- [x] Figuring out the basics and installation of Selenium
- [x] Cloudflare prevents scripts to an extent. I used time.sleep() to work around this but this is likely not best practice, but the workaround is beyond the scope/purpose of this project.
- [x] A way needed to hide credentials from github and store it locally was needed. Implemented [dotenv](https://github.com/theskumar/python-dotenv)
- [x] Script that logs user into to tracker.gg from home page to sign in is complete.
- [x] Code doesn't look scaleable so I need a better model. Introducing the Page Object Model (POM), I started implementing login_page.py as a starter
- [x] Implement a POM for a class file of locators
- [x] Implement a POM for a class file of homepage and page functions
- [ ] Implement a POM for get set elements
- [x] Implement pytest
- [x] Rewrite login.py as a test_login.py which will use pytest and POM framework to write cleaner readable test case
- [ ] Write a few more variety of login tests
- [ ] Explore search testing, likely need to expand POM

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

