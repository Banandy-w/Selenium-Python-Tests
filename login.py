# Automated functional test case for user Login of tracker.gg
# Steps
# Navigate to tracker.gg
# Select Login
# Enter login info
# Verify user is logged in
# Expected Results user is logged in

from selenium import webdriver 

driver = webdriver.Firefox()
driver.get('https://tracker.gg/')