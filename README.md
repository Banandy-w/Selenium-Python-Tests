# Selenium-Python-Tests
Using Selenium to learn automation coding practices by writing test cases.

## Requirements / Prereqs
* [Mozilla browser](https://www.mozilla.org/en-US/firefox/new/)
* Install [Geckodriver](https://github.com/mozilla/geckodriver/releases) *Need to elaborate on this for various OS*
* Rename example.env to .env and input credentials.
## Code dependecies
~~~
pip install selenium
~~~
https://selenium-python.readthedocs.io/
~~~
pip install python-dotenv
~~~
https://github.com/theskumar/python-dotenv


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

