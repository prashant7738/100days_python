from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/dell/OneDrive/Documents/chromedriver-win64/chromedriver.exe"

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service = service)

driver.get("https://www.python.org/")

event_time = driver.find_elements(By.CSS_SELECTOR,'.event-widget time')


event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for n in range(len(event_time)):
    events[n]= {
        "time" : event_time[n].text,
        "name" : event_names[n].text
    }


print(events)




driver.quit()
