import requests

url = "https://chatgpt-42.p.rapidapi.com/gpt4"
prompt = None


while prompt != "bye":
	prompt = input("Enter the prompt to ask for chatgpt and type bye to exit:\n")

	payload = {
		"messages": [
			{
				"role": "user",
				"content": f"{prompt}"
			}
		],
		"web_access": False
	}
	headers = {
		"x-rapidapi-key": "10eba43674mshe73e9d0bc02eefdp19281bjsncda2b0322a0b",
		"x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
		"Content-Type": "application/json"
	}

	response = requests.post(url, json=payload, headers=headers)

	print(response.json()['result'])
	print("\n")