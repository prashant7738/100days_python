from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/dell/OneDrive/Documents/chromedriver-win64/chromedriver.exe"

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service = service)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

no =driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')

print(no.text)