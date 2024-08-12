import requests
USERNAME = "randomdude7738"
TOKEN = "kdfh984jr94j"

user_endpoint = "https://pixe.la/v1/users"
user_parameter = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url = user_endpoint , json = user_parameter)
# print(response.text)


graph_endpoint = f"{user_endpoint}/{USERNAME}/graphs"
graph_parameter = {
    "id" : "graph2",
    "name" : "CyclingGraph",
    "unit" : "K.M.",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}
response2 = requests.post(url = graph_endpoint , json = graph_parameter, headers= headers)

print(response2.text)


