from bs4 import BeautifulSoup


with open("website.html", encoding='utf-8') as fp:
    contents= fp.read()

soup = BeautifulSoup(contents,"html.parser")

print(soup.title)

data = soup.select_one(selector=".heading")
print(data.string)
