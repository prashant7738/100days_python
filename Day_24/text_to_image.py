# Using this api WE CAN GENERATE IMAGE FROM TEXT

import requests

url = "https://chatgpt-42.p.rapidapi.com/texttoimage"

payload = {
	"text": "a man sitting in a couch with cigar in hand",
	"width": 512,
	"height": 512
}
headers = {
	"x-rapidapi-key": "10eba43674mshe73e9d0bc02eefdp19281bjsncda2b0322a0b",
	"x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())