# Automated functional test case for user Login of tracker.gg
# Steps
# Navigate to tracker.gg
# Select Login
# Enter login info
# Verify user is logged in
# Expected Results user is logged in
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
# Note to self: learn if By.NAME XPATH etc which is best by convention. Initial assumption would be by name but this element didn't have name
print('Scanning for login element')
element = driver.find_element(By.XPATH,'/html/body/div/div/nav/div[3]/a[2]')
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