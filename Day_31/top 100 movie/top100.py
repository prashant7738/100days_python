from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text,"html.parser")
title = soup.find_all(name="h3", class_="title")
title_list= [x.string for x in title]
# print(title_list[100-i][:3] for i in range(1,100))
arranged_title = "\n".join([title_list[100-i] for i in range(1,100)])
# print(arranged_title)

with open("movies.txt","w",encoding="utf-8")as fp:
    fp.write(arranged_title)


