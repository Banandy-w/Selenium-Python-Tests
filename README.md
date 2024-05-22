# Selenium-Python-Tests
Using Selenium to learn automation coding practices by writing test cases. *This an overview of the journey.*
* First I needed a functioning product with data that I am personally interested so its more interesting. Naturally gravitated towards gaming so I chose https://tracker.gg/
* Second, test a feature that every user would probalby use but isn't too complicated to get our feet wet with automation. I decided login with navigation instead of directly openning to the login page. With this created [manual_login.py](https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/manual_login.py) (was login.py) which uses selenium at its core to navigate the website and login.
* Some rodebumps, preserving our data privacy was solved by using [dotenv](https://github.com/theskumar/python-dotenv) and cloudflare was worked around using time.sleep()

Writing more tests in a scaleable fashion required the implementation of a [page object model](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models) which lead to the creation of the following:
* [base_page.py](https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/POM/pages/base_page.py) which should have some basic functions of navigating a webpage
* [locators.py](https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/POM/pages/locators.py) has locators of all necessary elements for testing
* And [login_page.py](https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/POM/pages/login_page.py) which encapsulates functions of the login page into methods. 

In hindsight, it might've been easier to put the locator variables into the login_page and base_page as it might've made the code a bit cleaner with less imports. But if this was to scale more features having locators in a seperate file maybe cleaner. This is something i'll see when trying to test a different feature.

Next, to make sure the POM implementation was working correctly, I incrementally replaced functions from [manual_login](https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/manual_login.py) which lead to [login.py](https://github.com/Banandy-w/Selenium-Python-Tests/blob/main/login.py) After verifying the POM implementation works,  we just needed to implement the testing in pytest.

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
 git clone https://github.com/Banandy-w/Selenium-Python-Tests.git
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

