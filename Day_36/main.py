# lets create the bot to follow many people in my instagram account
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import datetime




chrome_driver_path = r'C:\Users\dell\OneDrive\Documents\chromedriver-win64\chromedriver.exe'
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service = service)

driver.get("https://www.instagram.com/accounts/login/?next=%2Fp%2FCIM-BKcDAJI%2F&source=desktop_nav")

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]'))).click()


def login():
    MAIL = '' 
    
    PASS = ''  # Your password
    # login to insta email
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div/div[1]/div/label/input'))).send_keys(MAIL)
    # pass 
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div/div[2]/div/label/input'))).send_keys(PASS)
    # login
    # time.sleep(5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[3]/button'))).send_keys(Keys.ENTER)

login()

# NOT now
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div'))).click()


def find_follower():
    SIMILAR_ACCOUNT = 'prabalgurung'
    driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'followers'))).click()

def get_follower():
    time.sleep(5)
    # follower_list = driver.find_elements(By.CSS_SELECTOR,'button')
    # # follow_list = WebDriverWait(driver, 10 ).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Follow")))
    # for i in follower_list:
    #     i.click()
find_follower()
get_follower()
input("Press Enter to close the browser...")
driver.quit()

