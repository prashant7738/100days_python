from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:/Users/dell/OneDrive/Documents/chromedriver-win64/chromedriver.exe"

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service = service)

driver.get("https://orteil.dashnet.org/cookieclicker/") 
time.sleep(20)

clicker = driver.find_element(By.ID ,'bigCookie')

timeout = time.time() + 5
cursor = driver.find_element(By.XPATH, '//*[@id="product0"]')
grandma = driver.find_element(By.XPATH , '//*[@id="product1"]')


thirty = time.time() + 30
five_min = time.time() + 5*60


while True:
    clicker.click()
    if time.time() > timeout and time.time() < thirty:
        
        cursor.click()

    elif time.time() > thirty:
        
        grandma.click()



   

    

    




driver.quit()