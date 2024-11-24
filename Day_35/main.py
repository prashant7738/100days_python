# lets create the bot to tweet in my twitter account
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import datetime



MAIL = os.getenv('X_MAIL') 
USERNAME = 'random7738'  # Your username
PASS = os.getenv('X_PASS')  # Your password

chrome_driver_path = r'C:\Users\dell\OneDrive\Documents\chromedriver-win64\chromedriver.exe'
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service = service)

driver.get("https://x.com/i/flow/login")

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]'))).click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))).send_keys(MAIL)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))).send_keys(Keys.ENTER)


WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'))).send_keys(USERNAME)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'))).send_keys(Keys.ENTER)



WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))).send_keys(PASS)
WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))).send_keys(Keys.ENTER)

WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div'))).send_keys(f'This tweet is written in {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button'))).send_keys(Keys.ENTER)

input("Press Enter to close the browser...")
driver.quit()