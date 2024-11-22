from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/dell/OneDrive/Documents/chromedriver-win64/chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service= service)

driver.get(url="https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.CLASS_NAME, 'top')
first_name.send_keys('Prashant')

last_name = driver.find_element(By.CLASS_NAME, 'middle')
last_name.send_keys('kafle')

gmail = driver.find_element(By.CLASS_NAME, 'bottom')
gmail.send_keys('prashantkafle@gmail.com')

sign_up = driver.find_element(By.CSS_SELECTOR ,'form button')
# sign_up.send_keys(Keys.ENTER)
sign_up.click()






driver.quit()