# Open https://the-internet.herokuapp.com/login
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TEST_DATA = {
    'login': 'tomsmith',
    'password': 'SuperSecretPassword!',
    'invalid login': '!@#$#@$$%'
}
# Please automate next test cases:
# 1. Login with valid creds (tomsmith/SuperSecretPassword!) and assert you successfully logged in

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/login')
time.sleep(3)
driver.find_element_by_css_selector('#username').send_keys(TEST_DATA['login'])
driver.find_element_by_css_selector('#password').send_keys(TEST_DATA['password'])
driver.find_element_by_css_selector('#login > button').click()
time.sleep(2)
if 'Welcome to the Secure Area' in driver.page_source:
   driver.quit()

# 2. Login with invalid creds and check validation error


driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/login')
time.sleep(3)
driver.find_element_by_css_selector('#username').send_keys(TEST_DATA['invalid login'])
driver.find_element_by_css_selector('#password').send_keys(TEST_DATA['password'])
driver.find_element_by_css_selector('#login > button').click()
time.sleep(2)
if 'Your username is invalid!' in driver.page_source:
    driver.quit()


# 3. Logout from app and assert you successfully logged out

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/login')
time.sleep(3)
driver.find_element_by_css_selector('#username').send_keys(TEST_DATA['login'])
driver.find_element_by_css_selector('#password').send_keys(TEST_DATA['password'])
driver.find_element_by_css_selector('#login > button').click()
time.sleep(2)
driver.find_element_by_css_selector('#content > div > a').click()
if 'You logged out of the secure area!' in driver.page_source:
    driver.quit()