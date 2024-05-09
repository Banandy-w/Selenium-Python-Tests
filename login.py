# Automated functional test case for user Login of tracker.gg
# Steps
# Navigate to tracker.gg
# Select Login
# Enter login info
# Verify user is logged in
# Expected Results user is logged in
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1 Navigate to tracker.gg
## We can definitely just open the login page directly but I want to explore the navigation functionality of selenium
print('Openning firefox on page tracker.gg')
driver = webdriver.Firefox()
driver.get('https://tracker.gg/')


# Step 2 Select login and click on it
# Note to self: learn if By.NAME XPATH etc which is best by convention. Initial assumption would be by name but this element didn't have name
print('Scanning for login element')
element_login = driver.find_element(By.XPATH,'/html/body/div/div/nav/div[3]/a[2]')
element_login.send_keys(Keys.RETURN)


# Driver doesn't wait for page to load so need to learn how to wait until element appears
# Step 3 Wait for page to load
wait = WebDriverWait(driver, 10)
print("Waiting for page to load")
element_login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.trn-input:nth-child(1)")))
print('Scanning for username element')

userName = 'bananatest'
password = ''
# Step 4 Entering login data
# Need to wait for cloudflare to finish loading before we can enter the information
# Using sleep probably isn't a good method in terms of automation. Other methods are more involved that seems be used for data scraping / beyond scope of this.
time.sleep(2)

print('Entering Username and Password')
element_login.send_keys(userName)
element_login = driver.find_element(By.CSS_SELECTOR,'input.trn-input:nth-child(2)').send_keys(password,Keys.RETURN)

# Step 5 Verify login was successful