import requests

url = "https://runwayml.p.rapidapi.com/generate/text"

payload = {
	"text_prompt": "masterpiece, cinematic, young man studying infront of mount everest, wearing hat",
	"width": 1344,
	"height": 768,
	"motion": 5,
	"seed": 0,
	"upscale": True,
	"interpolate": True,
	"callback_url": ""
}
headers = {
	"x-rapidapi-key": "10eba43674mshe73e9d0bc02eefdp19281bjsncda2b0322a0b",
	"x-rapidapi-host": "runwayml.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())