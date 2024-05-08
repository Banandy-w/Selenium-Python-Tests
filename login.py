# Automated functional test case for user Login of tracker.gg
# Steps
# Navigate to tracker.gg
# Select Login
# Enter login info
# Verify user is logged in
# Expected Results user is logged in

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

# Step 1 Navigate to tracker.gg
## We can definitely just open the login page directly but I want to explore the navigation functionality of selenium
print('Openning firefox on page tracker.gg')
driver = webdriver.Firefox()
driver.get('https://tracker.gg/')

# Step 2 Select login and click on it
## 
print('Scanning for login element')
element_login = driver.find_element(By.XPATH,'/html/body/div/div/nav/div[3]/a[2]')
element_login.send_keys(Keys.RETURN)

element_login.find_element(By.NAME,'UserName')
element_login.send_keys('bananatest')

element_login.find_element(By.NAME,'Password')