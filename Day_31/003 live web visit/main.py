from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")
title = soup.find(name="span", class_="titleline")
# title_text = title.get("a").getText()
title_link = title.get("href")
score = soup.find(name="span", id = "score_41464371") 
# print(score.string)
# print(title_text)
print(title_link)
